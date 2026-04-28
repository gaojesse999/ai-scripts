#!/usr/bin/env python3

from __future__ import annotations

import argparse
import hashlib
import json
import os
import platform
import shlex
import shutil
import subprocess
import sys
import tarfile
import tempfile
from pathlib import Path
from urllib.request import urlopen

SCRIPT_DIR = Path(__file__).resolve().parent
PROJECT_ROOT = (SCRIPT_DIR / "../l1sw").resolve()
LOCKFILE_PATH = PROJECT_ROOT / "skills-lock.json"
SKILLS_STAGING_ROOT = PROJECT_ROOT / ".agents" / "skills"
SKILLS_TARGET_ROOT = PROJECT_ROOT / ".copilot" / "skills"
LOCAL_NODE_ROOT = Path.home() / ".local" / "share" / "nodejs"
LOCAL_NODE_CURRENT = LOCAL_NODE_ROOT / "current"
LOCAL_BIN_DIR = Path.home() / ".local" / "bin"
NODE_DIST_INDEX_URL = "https://nodejs.org/dist/index.json"
NODE_VERSION_ENV = "SKILLS_BOOTSTRAP_NODE_VERSION"

CONFIGURED_SKILLS = (
    ("https://github.com/anthropics/skills", "skill-creator"),
    ("https://github.com/vercel-labs/skills.git", "find-skills"),
    ("https://github.com/anthropics/claude-code", "Agent Development"),
)

SKILL_DIR_MAP = {
    "skill-creator": "skill-creator",
    "find-skills": "find-skills",
    "Agent Development": "agent-development",
}

RUNTIME_ENV = os.environ.copy()


def log(message: str) -> None:
    print(f"[skills-bootstrap] {message}")


def fail(message: str) -> None:
    print(f"[skills-bootstrap] ERROR: {message}", file=sys.stderr)
    raise SystemExit(1)


def format_command(args: list[str]) -> str:
    return shlex.join(str(arg) for arg in args)


def run_command(
    args: list[str],
    *,
    cwd: Path | None = None,
    env: dict[str, str] | None = None,
    capture_output: bool = False,
) -> subprocess.CompletedProcess[str]:
    result = subprocess.run(
        [str(arg) for arg in args],
        cwd=str(cwd) if cwd else None,
        env=env or RUNTIME_ENV,
        text=True,
        capture_output=capture_output,
        check=False,
    )

    if result.returncode != 0:
        detail = f"exit code {result.returncode}"
        if capture_output:
            stderr = (result.stderr or "").strip()
            stdout = (result.stdout or "").strip()
            if stderr:
                detail = stderr
            elif stdout:
                detail = stdout
        raise RuntimeError(f"Command failed ({format_command(args)}): {detail}")

    return result


def prepend_runtime_path(path: Path) -> None:
    path_str = str(path)
    current_entries = [entry for entry in RUNTIME_ENV.get("PATH", "").split(os.pathsep) if entry]
    if path_str not in current_entries:
        current_entries.insert(0, path_str)
        RUNTIME_ENV["PATH"] = os.pathsep.join(current_entries)


def refresh_local_node_paths() -> None:
    for candidate in (LOCAL_BIN_DIR, LOCAL_NODE_CURRENT / "bin"):
        if candidate.exists():
            prepend_runtime_path(candidate)


def have_command(name: str) -> bool:
    return shutil.which(name, path=RUNTIME_ENV.get("PATH")) is not None


def remove_path(path: Path) -> None:
    if path.is_symlink() or path.is_file():
        path.unlink()
        return

    if path.is_dir():
        shutil.rmtree(path)


def replace_with_symlink(path: Path, target: Path) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    if path.exists() or path.is_symlink():
        remove_path(path)
    path.symlink_to(target)


def ensure_shell_path_export() -> None:
    profile_path = Path.home() / ".bash_profile"
    export_line = 'export PATH="$HOME/.local/bin:$PATH"'

    existing_text = profile_path.read_text(encoding="utf-8") if profile_path.exists() else ""
    if export_line in existing_text:
        return

    with profile_path.open("a", encoding="utf-8") as profile_file:
        if existing_text and not existing_text.endswith("\n"):
            profile_file.write("\n")
        profile_file.write(f"{export_line}\n")


def require_privilege_prefix() -> list[str]:
    if os.geteuid() == 0:
        return []

    sudo_path = shutil.which("sudo")
    if sudo_path:
        return [sudo_path, "-n"]

    raise RuntimeError("Package installation requires root or passwordless sudo.")


def install_node_toolchain_with_package_manager() -> bool:
    prefix = require_privilege_prefix()

    if have_command("apt-get"):
        log("Installing nodejs and npm with apt-get")
        run_command(prefix + ["apt-get", "update"])
        run_command(prefix + ["apt-get", "install", "-y", "nodejs", "npm"])
        return True

    if have_command("dnf"):
        log("Installing nodejs and npm with dnf")
        run_command(prefix + ["dnf", "install", "-y", "nodejs", "npm"])
        return True

    if have_command("yum"):
        log("Installing nodejs and npm with yum")
        run_command(prefix + ["yum", "install", "-y", "nodejs", "npm"])
        return True

    return False


def resolve_node_architecture() -> str:
    machine = platform.machine().lower()
    arch_map = {
        "x86_64": "x64",
        "amd64": "x64",
        "aarch64": "arm64",
        "arm64": "arm64",
    }

    try:
        return arch_map[machine]
    except KeyError as exc:
        raise RuntimeError(f"Unsupported architecture for Node.js bootstrap: {machine}") from exc


def fetch_text(url: str) -> str:
    with urlopen(url, timeout=30) as response:
        return response.read().decode("utf-8")


def resolve_latest_lts_version() -> str:
    override = os.environ.get(NODE_VERSION_ENV, "").strip()
    if override:
        return override if override.startswith("v") else f"v{override}"

    releases = json.loads(fetch_text(NODE_DIST_INDEX_URL))
    for release in releases:
        if release.get("lts"):
            return release["version"]

    raise RuntimeError("Could not resolve a Node.js LTS version from nodejs.org")


def sha256sum(file_path: Path) -> str:
    digest = hashlib.sha256()
    with file_path.open("rb") as file_handle:
        while True:
            chunk = file_handle.read(1024 * 1024)
            if not chunk:
                break
            digest.update(chunk)
    return digest.hexdigest()


def install_node_toolchain_locally() -> None:
    version = resolve_latest_lts_version()
    arch = resolve_node_architecture()
    archive_name = f"node-{version}-linux-{arch}.tar.xz"
    install_dir = LOCAL_NODE_ROOT / archive_name.removesuffix(".tar.xz")

    if install_dir.is_dir():
        log(f"Reusing local Node.js install: {install_dir}")
    else:
        base_url = f"https://nodejs.org/dist/{version}"
        shasums_text = fetch_text(f"{base_url}/SHASUMS256.txt")
        expected_checksum = ""

        for line in shasums_text.splitlines():
            parts = line.split()
            if len(parts) == 2 and parts[1] == archive_name:
                expected_checksum = parts[0]
                break

        if not expected_checksum:
            raise RuntimeError(f"Checksum entry not found for Node.js archive: {archive_name}")

        LOCAL_NODE_ROOT.mkdir(parents=True, exist_ok=True)
        if install_dir.exists() or install_dir.is_symlink():
            remove_path(install_dir)

        with tempfile.TemporaryDirectory(prefix="nodejs-bootstrap-") as temp_dir:
            archive_path = Path(temp_dir) / archive_name
            archive_url = f"{base_url}/{archive_name}"

            log(f"Downloading Node.js {version} for linux-{arch}")
            with urlopen(archive_url, timeout=120) as response, archive_path.open("wb") as archive_file:
                shutil.copyfileobj(response, archive_file)

            actual_checksum = sha256sum(archive_path)
            if actual_checksum != expected_checksum:
                raise RuntimeError(
                    f"Checksum mismatch for {archive_name}: expected {expected_checksum}, got {actual_checksum}"
                )

            log(f"Installing Node.js {version} into {LOCAL_NODE_ROOT}")
            with tarfile.open(archive_path) as archive:
                archive.extractall(LOCAL_NODE_ROOT)

    replace_with_symlink(LOCAL_NODE_CURRENT, install_dir)
    LOCAL_BIN_DIR.mkdir(parents=True, exist_ok=True)

    for tool_name in ("node", "npm", "npx"):
        tool_path = LOCAL_NODE_CURRENT / "bin" / tool_name
        if not tool_path.exists():
            raise RuntimeError(f"Installed Node.js archive is missing expected tool: {tool_path}")
        replace_with_symlink(LOCAL_BIN_DIR / tool_name, tool_path)

    ensure_shell_path_export()
    refresh_local_node_paths()


def log_tool_versions() -> None:
    node_version = run_command(["node", "--version"], capture_output=True).stdout.strip()
    npm_version = run_command(["npm", "--version"], capture_output=True).stdout.strip()
    log(f"node: {node_version}")
    log(f"npm:  {npm_version}")


def ensure_node_toolchain() -> None:
    refresh_local_node_paths()

    if have_command("npx"):
        log("npx already available")
        log_tool_versions()
        return

    try:
        install_attempted = install_node_toolchain_with_package_manager()
    except RuntimeError as exc:
        install_attempted = False
        log(f"Package manager installation failed, falling back to a user-local Node.js install: {exc}")

    if install_attempted:
        refresh_local_node_paths()

    if not have_command("npx"):
        log("Installing a user-local Node.js toolchain under ~/.local")
        install_node_toolchain_locally()

    for tool_name in ("node", "npm", "npx"):
        if not have_command(tool_name):
            fail(f"{tool_name} is still unavailable after installation")

    log_tool_versions()


def skill_dir_name(skill_name: str) -> str:
    try:
        return SKILL_DIR_MAP[skill_name]
    except KeyError as exc:
        raise RuntimeError(f"Unknown skill directory mapping for: {skill_name}") from exc


def target_skill_path(skill_name: str) -> Path:
    return SKILLS_TARGET_ROOT / skill_dir_name(skill_name)


def staging_skill_path(skill_name: str) -> Path:
    return SKILLS_STAGING_ROOT / skill_dir_name(skill_name)


def staging_skill_link_target(skill_name: str) -> Path:
    return Path("../../.agents/skills") / skill_dir_name(skill_name)


def link_skill_to_copilot_dir(skill_name: str) -> None:
    source_dir = staging_skill_path(skill_name)
    source_link_target = staging_skill_link_target(skill_name)
    target_dir = target_skill_path(skill_name)

    if not source_dir.is_dir():
        fail(f"Expected installed skill directory not found: {source_dir}")

    SKILLS_TARGET_ROOT.mkdir(parents=True, exist_ok=True)
    if target_dir.exists() or target_dir.is_symlink():
        remove_path(target_dir)
    target_dir.symlink_to(source_link_target)
    log(f"Linked GitHub Copilot skill directory: {target_dir} -> {source_link_target}")


def confirm_reinstall(skill_name: str) -> bool:
    existing_dir = target_skill_path(skill_name)

    if not sys.stdin.isatty():
        log(f"Skill already exists and no interactive terminal is available, skipping reinstall: {skill_name}")
        return False

    while True:
        answer = input(
            f'[skills-bootstrap] Skill "{skill_name}" already exists at {existing_dir}. Force reinstall? [y/N] '
        ).strip()

        if answer in {"y", "Y"}:
            return True
        if answer in {"n", "N", ""}:
            return False
        log("Please answer y or n")


def install_skill_if_needed(source: str, skill_name: str) -> None:
    staging_dir = staging_skill_path(skill_name)
    target_dir = target_skill_path(skill_name)

    if target_dir.exists() or target_dir.is_symlink():
        if not confirm_reinstall(skill_name):
            log(f"Keeping existing skill unchanged: {skill_name}")
            return
    elif staging_dir.is_dir():
        log(f"Skill already exists in project metadata, recreating GitHub Copilot link: {skill_name}")
        link_skill_to_copilot_dir(skill_name)
        return

    log(f"Installing skill: {skill_name}")
    run_command(
        ["npx", "--yes", "skills", "add", source, "--skill", skill_name, "-y"],
        cwd=PROJECT_ROOT,
    )

    link_skill_to_copilot_dir(skill_name)


def install_configured_skills() -> None:
    for source, skill_name in CONFIGURED_SKILLS:
        install_skill_if_needed(source, skill_name)

    if LOCKFILE_PATH.is_file():
        log(f"skills-lock.json present: {LOCKFILE_PATH}")
    else:
        log("skills-lock.json was not created by the skills CLI")

    log("Skill directories in this project:")
    log(f"  skill-creator: {SKILLS_TARGET_ROOT / 'skill-creator'}")
    log(f"  find-skills: {SKILLS_TARGET_ROOT / 'find-skills'}")
    log(f"  Agent Development: {SKILLS_TARGET_ROOT / 'agent-development'}")
    log("Configured skills processing completed")


def parse_args(argv: list[str] | None = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog=str(Path(__file__)),
        description=(
            "Bootstrap node/npm/npx in the current container and optionally process the fixed "
            "project-level Copilot skills for the sibling l1sw workspace."
        ),
        epilog=(
            "What it does:\n"
            "  1. Ensures node, npm, and npx are installed in the current container.\n"
            "  2. With --bootstrap, installs the configured project-level skills into the sibling l1sw project.\n"
            "  3. If a configured skill already exists in the current project, the script asks\n"
            "     whether to force reinstall it.\n"
            "  4. The skills CLI keeps its project metadata in .agents/skills, then the script\n"
            "     links .copilot/skills entries back to .agents/skills so Copilot and the CLI\n"
            "     share one source of truth.\n"
            "\n"
            "Examples:\n"
            "  python3 ../vscode/npx-skills.sh --bootstrap\n"
            "      Ensure Node.js tooling is available, then process the fixed skills.\n"
            "\n"
            "  python3 ../vscode/npx-skills.sh --skip-skills\n"
            "      Only bootstrap node, npm, and npx.\n"
            "\n"
            "  ../vscode/npx-skills.sh --bootstrap\n"
            "      Run the same flow through the script shebang.\n"
        ),
        formatter_class=argparse.RawDescriptionHelpFormatter,
    )
    mode_group = parser.add_mutually_exclusive_group()
    mode_group.add_argument(
        "--bootstrap",
        action="store_true",
        help="Ensure node, npm, and npx are available, then process the fixed skills.",
    )
    mode_group.add_argument(
        "--skip-skills",
        action="store_true",
        help="Only ensure node, npm, and npx are available.",
    )
    return parser.parse_args(argv)


def main() -> int:
    if len(sys.argv) == 1:
        parse_args(["--help"])
        return 0

    args = parse_args()

    if not PROJECT_ROOT.is_dir():
        fail(f"Expected sibling project directory not found: {PROJECT_ROOT}")

    ensure_node_toolchain()

    if args.skip_skills:
        log("Skill installation is disabled for this run.")
        log(f"Project root: {PROJECT_ROOT}")
        return 0

    install_configured_skills()
    return 0


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except KeyboardInterrupt:
        fail("Interrupted")
    except RuntimeError as exc:
        fail(str(exc))