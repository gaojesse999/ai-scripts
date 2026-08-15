#!/usr/bin/env python3
"""Recommend a `--workers` value for `hyperframes render` from free memory.

HyperFrames already sizes workers from memory, but it reads *total* RAM:
`floor(total_mb * 0.5 / 1536)`. A 16 GB host therefore asks for five Chrome
workers whether 12 GB or 1 GB is actually free, and a render started against
the second case thrashes or loses a worker mid-capture. This script closes that
gap by sizing against *available* memory, and it never proposes more workers
than HyperFrames would have picked on its own — raising the count past that
point runs into the V8 heap advisory and buys nothing.

The per-worker figure is an estimate, not a measurement. `render --help`
documents roughly 256 MB per Chrome process; the internal planner reserves
1536 MB. The default here sits between the two. Once a real render on this host
has been measured, pass the observed figure through `--per-worker-mb` and
record it in `render-env.sh` so later chapters inherit a calibrated number
instead of this guess.

Exits non-zero when not even one worker fits, so it can gate a render.
"""

from __future__ import annotations

import argparse
import ctypes
import json
import os
import platform
import re
import subprocess
import sys
from pathlib import Path

# Read out of hyperframes 0.7.107 dist/cli.js (parallelCoordinator.ts,
# systemMemory.ts). Kept here so the recommendation can be compared against
# what the renderer would have done unaided.
HF_MEMORY_PER_WORKER_MB = 1536
HF_MIN_FRAMES_PER_WORKER = 30
HF_MIN_PARALLEL_FRAMES = 120
HF_LOW_MEMORY_TOTAL_MB = 8192
HF_ABSOLUTE_MAX_WORKERS = 24

DEFAULT_PER_WORKER_MB = 512
DEFAULT_RESERVE_MB = 1536  # node parent + ffmpeg encode pass + OS headroom


def _windows_memory() -> tuple[int, int, str]:
    class Status(ctypes.Structure):
        _fields_ = [
            ("dwLength", ctypes.c_ulong),
            ("dwMemoryLoad", ctypes.c_ulong),
            ("ullTotalPhys", ctypes.c_ulonglong),
            ("ullAvailPhys", ctypes.c_ulonglong),
            ("ullTotalPageFile", ctypes.c_ulonglong),
            ("ullAvailPageFile", ctypes.c_ulonglong),
            ("ullTotalVirtual", ctypes.c_ulonglong),
            ("ullAvailVirtual", ctypes.c_ulonglong),
            ("ullAvailExtendedVirtual", ctypes.c_ulonglong),
        ]

    status = Status()
    status.dwLength = ctypes.sizeof(Status)
    if not ctypes.windll.kernel32.GlobalMemoryStatusEx(ctypes.byref(status)):
        raise SystemExit("GlobalMemoryStatusEx failed")
    mib = 1024 * 1024
    return status.ullTotalPhys // mib, status.ullAvailPhys // mib, "GlobalMemoryStatusEx"


def _cgroup_limit_mb() -> int | None:
    """Container memory headroom, which the host's /proc/meminfo cannot see."""
    mib = 1024 * 1024
    v2 = Path("/sys/fs/cgroup/memory.max")
    if v2.exists():
        raw = v2.read_text().strip()
        if raw != "max":
            current = Path("/sys/fs/cgroup/memory.current")
            used = int(current.read_text().strip()) if current.exists() else 0
            return max(0, (int(raw) - used) // mib)
    v1 = Path("/sys/fs/cgroup/memory/memory.limit_in_bytes")
    if v1.exists():
        limit = int(v1.read_text().strip())
        # v1 reports an absurd sentinel rather than absence when uncapped.
        if limit < 2 ** 60:
            usage = Path("/sys/fs/cgroup/memory/memory.usage_in_bytes")
            used = int(usage.read_text().strip()) if usage.exists() else 0
            return max(0, (limit - used) // mib)
    return None


def _linux_memory() -> tuple[int, int, str]:
    fields = {}
    for line in Path("/proc/meminfo").read_text().splitlines():
        key, _, rest = line.partition(":")
        fields[key] = int(rest.strip().split()[0]) // 1024  # kB -> MB
    total = fields.get("MemTotal", 0)
    available = fields.get("MemAvailable", fields.get("MemFree", 0))
    source = "/proc/meminfo"
    cgroup = _cgroup_limit_mb()
    if cgroup is not None and cgroup < available:
        available = cgroup
        source = "/proc/meminfo + cgroup"
    return total, available, source


def _darwin_memory() -> tuple[int, int, str]:
    mib = 1024 * 1024
    total = int(subprocess.run(["sysctl", "-n", "hw.memsize"], capture_output=True,
                               text=True, check=True).stdout.strip()) // mib
    raw = subprocess.run(["vm_stat"], capture_output=True, text=True, check=True).stdout
    page_size = int(re.search(r"page size of (\d+)", raw).group(1))
    counts = dict(re.findall(r"^(.+?):\s+(\d+)\.$", raw, re.MULTILINE))
    reusable = sum(
        int(counts.get(name, 0))
        for name in ("Pages free", "Pages inactive", "Pages speculative", "Pages purgeable")
    )
    return total, reusable * page_size // mib, "vm_stat"


def read_memory() -> tuple[int, int, str]:
    system = platform.system()
    if system == "Windows":
        return _windows_memory()
    if system == "Linux":
        return _linux_memory()
    if system == "Darwin":
        return _darwin_memory()
    raise SystemExit(f"Unsupported platform: {system}; pass --available-mb explicitly")


def hyperframes_auto_workers(total_mb: int, cpu_count: int, frames: int) -> tuple[int, str]:
    """Replicate the renderer's own auto-sizing so we only ever cap it down."""
    if frames < HF_MIN_FRAMES_PER_WORKER * 2:
        return 1, "too_few_frames"
    cpu_based = max(1, cpu_count - 2)
    memory_based = max(1, int(total_mb * 0.5 // HF_MEMORY_PER_WORKER_MB))
    frame_based = frames // HF_MIN_FRAMES_PER_WORKER
    safe_max = max(6, min(16, cpu_count // 8))
    optimal = min(cpu_based, memory_based, frame_based)
    bound = ("cpu" if optimal == cpu_based
             else "memory" if optimal == memory_based
             else "frames")
    floor = 2 if frames >= HF_MIN_PARALLEL_FRAMES else 1
    workers = max(floor, min(safe_max, optimal))
    return min(workers, HF_ABSOLUTE_MAX_WORKERS), bound


def job_frames(args) -> tuple[int, float, int]:
    if args.frames:
        fps = args.fps or 30
        return args.frames, args.frames / fps, fps
    duration, fps = args.duration, args.fps
    if args.project:
        if duration is None:
            scenes = args.project / "timing/scenes.json"
            if scenes.exists():
                duration = float(json.loads(scenes.read_text(encoding="utf-8"))["duration"])
        if fps is None:
            config = args.project / "project-config.json"
            if config.exists():
                fps = int(json.loads(config.read_text(encoding="utf-8"))["video"]["fps"])
    if duration is None:
        raise SystemExit("Cannot determine job size; pass --frames, or --duration, "
                         "or a --project holding timing/scenes.json")
    fps = fps or 30
    return round(duration * fps), duration, fps


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__,
                                 formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--project", type=Path,
                    help="read duration from timing/scenes.json and fps from project-config.json")
    ap.add_argument("--frames", type=int, help="override the frame count")
    ap.add_argument("--duration", type=float, help="override the duration in seconds")
    ap.add_argument("--fps", type=int, help="override the frame rate")
    ap.add_argument("--per-worker-mb", type=int, default=DEFAULT_PER_WORKER_MB,
                    help=f"measured cost of one capture worker (default {DEFAULT_PER_WORKER_MB})")
    ap.add_argument("--reserve-mb", type=int, default=DEFAULT_RESERVE_MB,
                    help=f"held back for node, ffmpeg, and the OS (default {DEFAULT_RESERVE_MB})")
    ap.add_argument("--available-mb", type=int, help="override the detected available memory")
    args = ap.parse_args()

    cpu_count = os.cpu_count() or 1
    total_mb, detected_mb, source = read_memory()
    available_mb = args.available_mb if args.available_mb is not None else detected_mb
    if args.available_mb is not None:
        source = "--available-mb"

    frames, duration, fps = job_frames(args)
    auto_workers, bound_by = hyperframes_auto_workers(total_mb, cpu_count, frames)

    usable_mb = available_mb - args.reserve_mb
    supported = usable_mb // args.per_worker_mb if usable_mb > 0 else 0
    recommended = max(1, min(auto_workers, supported))

    print(f"memory        total {total_mb} MB   available {available_mb} MB   (via {source})")
    print(f"job           {frames} frames   {duration:.2f}s @ {fps} fps")
    print(f"cpu           {cpu_count} cores")
    print()
    print("hyperframes auto-sizing (reads TOTAL memory, ignores what is free)")
    print(f"  would use   {auto_workers} worker{'' if auto_workers == 1 else 's'}"
          f"   bound by: {bound_by}")
    if total_mb <= HF_LOW_MEMORY_TOTAL_MB:
        print(f"  note        low-memory profile auto-engages (total <= {HF_LOW_MEMORY_TOTAL_MB} MB):"
              " 1 worker, screenshot capture")
    print()
    print("available-memory budget (this script)")
    print(f"  reserve     {args.reserve_mb} MB   node parent + ffmpeg + OS headroom")
    print(f"  usable      {max(0, usable_mb)} MB")
    print(f"  per worker  {args.per_worker_mb} MB   (estimate; recalibrate from a measured render)")
    print(f"  supports    {supported} workers")
    print()

    if supported < 1:
        need = args.reserve_mb + args.per_worker_mb
        print(f"BLOCKED       free memory first, or render with --low-memory-mode")
        print(f"              one worker needs about {need} MB available; {available_mb} MB is present")
        sys.exit(1)

    if supported >= auto_workers:
        print("RECOMMENDED   omit --workers (auto-sizing is already within budget)")
        print(f"              free memory supports {supported}; hyperframes would use {auto_workers}")
    else:
        print(f"RECOMMENDED   --workers {recommended}")
        print(f"              free memory supports {supported} of the {auto_workers} workers "
              "hyperframes would launch unaided")


if __name__ == "__main__":
    main()
