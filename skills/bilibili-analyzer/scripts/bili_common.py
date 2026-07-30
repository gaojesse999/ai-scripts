#!/usr/bin/env python3
"""Shared helpers for bilibili-analyzer scripts.

Provides:
- A common User-Agent.
- Cookie loading from environment (BILI_COOKIE / BILI_COOKIE_FILE).
- A lightweight network preflight check that fails fast with a proxy hint.
- DASH stream selection and ffmpeg-based audio/video merging.

Proxy note: urllib's default opener already honors the standard
http_proxy / https_proxy environment variables, so simply exporting them
before running any script routes all requests through the proxy.
"""

from __future__ import annotations

import json
import os
import sys
from pathlib import Path
from shutil import which
from urllib.request import Request, urlopen

USER_AGENT = (
    "Mozilla/5.0 (X11; Linux x86_64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/123.0.0.0 Safari/537.36"
)


def load_cookie() -> str | None:
    """Load a Bilibili cookie string from the environment, if provided.

    Priority:
    1. BILI_COOKIE      - the raw cookie string.
    2. BILI_COOKIE_FILE - path to a file containing the cookie string.
    """
    cookie = os.environ.get("BILI_COOKIE")
    if cookie and cookie.strip():
        return cookie.strip()

    cookie_file = os.environ.get("BILI_COOKIE_FILE")
    if cookie_file:
        path = Path(cookie_file)
        if path.exists():
            lines = [
                line.strip()
                for line in path.read_text(encoding="utf-8").splitlines()
                if line.strip() and not line.lstrip().startswith("#")
            ]
            content = " ".join(lines).strip()
            if content:
                return content
    return None


def build_headers(referer: str, accept: str = "application/json, text/plain, */*") -> dict:
    headers = {
        "User-Agent": USER_AGENT,
        "Referer": referer,
        "Accept": accept,
    }
    cookie = load_cookie()
    if cookie:
        headers["Cookie"] = cookie
    return headers


def preflight(timeout: int = 8) -> tuple[bool, str]:
    """Perform a lightweight connectivity check against the Bilibili API.

    Returns (ok, message). Uses a tiny, well-known public endpoint so the
    request stays cheap and fast.
    """
    test_url = "https://api.bilibili.com/x/web-interface/view?bvid=BV1GJ411x7h7"
    try:
        request = Request(test_url, headers=build_headers("https://www.bilibili.com"))
        with urlopen(request, timeout=timeout) as response:
            payload = json.loads(response.read().decode("utf-8"))
    except Exception as exc:  # noqa: BLE001 - surface any connectivity failure
        return False, str(exc)

    code = payload.get("code")
    if code == 0 or code == -404:
        # code 0 = ok; -404 = video removed but network path is healthy.
        return True, "ok"
    return True, f"reachable (api code={code})"


def ensure_network(timeout: int = 8) -> None:
    """Abort early with a clear proxy hint when Bilibili is unreachable."""
    ok, message = preflight(timeout)
    if ok:
        return

    print("[ERROR] 无法连接 Bilibili，网络不可用，已提前终止任务以节约时间/成本。", file=sys.stderr)
    print(f"[ERROR] 详情: {message}", file=sys.stderr)
    print("[HINT] 该环境可能需要配置代理后重试，例如:", file=sys.stderr)
    print("[HINT]   export http_proxy=http://<proxy-host>:<port>", file=sys.stderr)
    print("[HINT]   export https_proxy=http://<proxy-host>:<port>", file=sys.stderr)
    print("[HINT] 配置代理后重新运行同一命令即可。", file=sys.stderr)
    raise SystemExit(3)


def stream_base_url(stream: dict) -> str | None:
    return stream.get("baseUrl") or stream.get("base_url")


def pick_dash_streams(dash: dict, max_height: int | None = 1080) -> tuple[dict, dict | None] | None:
    """Select the best video and audio stream from a DASH payload.

    ``max_height`` caps the vertical resolution to avoid downloading
    unnecessarily large 4K/HDR streams for frame-based analysis. Frames are
    sampled at a low fps, so 1080p is a sensible default ceiling. Pass
    ``None`` to always take the absolute best stream.
    """
    videos = dash.get("video") or []
    if not videos:
        return None

    candidates = videos
    if max_height is not None:
        eligible = [v for v in videos if (v.get("height") or 0) <= max_height]
        if eligible:
            candidates = eligible

    best_video = max(candidates, key=lambda v: (v.get("height", 0), v.get("id", 0), v.get("bandwidth", 0)))

    audios: list[dict] = list(dash.get("audio") or [])
    # Include FLAC / Dolby tracks when present.
    flac = (dash.get("flac") or {}).get("audio")
    if flac:
        audios.append(flac)
    dolby = (dash.get("dolby") or {}).get("audio") or []
    if isinstance(dolby, list):
        audios.extend(dolby)

    best_audio = max(audios, key=lambda a: a.get("bandwidth", 0)) if audios else None
    return best_video, best_audio


def get_ffmpeg() -> str:
    """Return a usable ffmpeg executable path.

    Prefers the bundled imageio-ffmpeg binary, then a system ffmpeg.
    """
    try:
        import imageio_ffmpeg

        return imageio_ffmpeg.get_ffmpeg_exe()
    except Exception:  # noqa: BLE001 - fall back to system ffmpeg
        pass

    system_ffmpeg = which("ffmpeg")
    if system_ffmpeg:
        return system_ffmpeg

    raise RuntimeError(
        "ffmpeg not found. Install it via 'pip install imageio-ffmpeg' or a system package."
    )


def merge_streams(video_stream: Path, audio_stream: Path | None, output_path: Path) -> None:
    """Mux separate DASH video/audio streams into a single MP4 (stream copy)."""
    import subprocess

    ffmpeg = get_ffmpeg()
    command = [ffmpeg, "-y", "-i", str(video_stream)]
    if audio_stream is not None:
        command += ["-i", str(audio_stream)]
    command += ["-c", "copy", str(output_path)]

    result = subprocess.run(
        command,
        stdout=subprocess.PIPE,
        stderr=subprocess.PIPE,
    )
    if result.returncode != 0:
        raise RuntimeError(
            "ffmpeg merge failed:\n" + result.stderr.decode("utf-8", errors="ignore")
        )
