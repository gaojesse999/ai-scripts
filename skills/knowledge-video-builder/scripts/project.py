#!/usr/bin/env python3
"""Initialize and manage a gated knowledge-video project."""
from __future__ import annotations
import argparse, hashlib, json, os, re, shutil, sys
from datetime import datetime, timezone
from pathlib import Path

PHASES = ["analysis", "brief", "script", "voice", "visual", "render"]
VALID_STATUS = {"not_started", "in_progress", "pending_review", "approved", "needs_revision", "blocked", "invalidated"}


def now():
    return datetime.now(timezone.utc).isoformat()


def slugify(value: str) -> str:
    value = value.strip().lower()
    value = re.sub(r"[^a-z0-9\u4e00-\u9fff]+", "-", value)
    return value.strip("-") or "knowledge-video"


def sha256_path(path: Path) -> str:
    if not path.exists() or not path.is_file():
        return ""
    h = hashlib.sha256()
    with path.open("rb") as f:
        for chunk in iter(lambda: f.read(1024 * 1024), b""):
            h.update(chunk)
    return h.hexdigest()


def load_state(project: Path) -> dict:
    p = project / "project-state.json"
    if not p.exists():
        raise SystemExit(f"Missing state file: {p}")
    return json.loads(p.read_text(encoding="utf-8"))


def save_state(project: Path, state: dict) -> None:
    p = project / "project-state.json"
    tmp = p.with_suffix(".json.tmp")
    tmp.write_text(json.dumps(state, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    tmp.replace(p)


def event(state: dict, action: str, phase: str, note: str = "") -> None:
    state.setdefault("history", []).append({"at": now(), "action": action, "phase": phase, "note": note})


# Single source for the per-phase artifact gate. validate_project.py imports
# this so a new required artifact cannot be added to one gate and forgotten in
# the other.
#
# Each artifact sits in the phase that first needs it, not the phase that
# happens to produce it early. The storyboard and the scene plan are visual
# authoring, so demanding them at the script gate would force a full
# visualisation pass through every narration revision.
REQUIRED_ARTIFACTS = {
    "analysis": ["analysis/overview.md", "analysis/evidence-map.json"],
    "brief": ["content/content-brief.md"],
    "script": [
        "script/SCRIPT.md",
        "timing/chapters.json",
    ],
    "voice": [
        "script/voice-plan.json",
        "audio/narration.wav",
        "audio/voice-production.json",
        "timing/scenes.json",
    ],
    "visual": [
        "script/STORYBOARD.md",
        "script/scene-plan.json",
        "review/storyboard.html",
        "hyperframes/index.html",
    ],
    "render": ["qa/report.md"],
}


def artifact_requirements(project: Path, phase: str) -> list[Path]:
    return [project / rel for rel in REQUIRED_ARTIFACTS[phase]]


def require_previous_approved(state: dict, phase: str) -> None:
    idx = PHASES.index(phase)
    if idx == 0:
        return
    prev = PHASES[idx - 1]
    if state["phases"][prev]["status"] != "approved":
        raise SystemExit(f"Cannot operate on '{phase}': prerequisite '{prev}' is not approved.")


def cmd_init(args):
    project = Path(args.project).resolve()
    project.mkdir(parents=True, exist_ok=True)
    for d in ["inputs","analysis","content","script","audio/segments","timing","motion","review","hyperframes/compositions","hyperframes/assets","qa","outputs"]:
        (project/d).mkdir(parents=True, exist_ok=True)
    skill_root = Path(__file__).resolve().parents[1]
    templates = skill_root/"templates"
    copies = {
        templates/"project-config.json": project/"project-config.json",
        templates/"evidence-map.json": project/"analysis/evidence-map.json",
        templates/"content-brief.md": project/"content/content-brief.md",
        templates/"SCRIPT.md": project/"script/SCRIPT.md",
        templates/"scene-plan.json": project/"script/scene-plan.json",
        templates/"pronunciation.json": project/"script/pronunciation.json",
        templates/"voice-plan.json": project/"script/voice-plan.json",
        templates/"motion-plan.yaml": project/"motion/motion-plan.yaml",
        templates/"style-tokens.json": project/"motion/style-tokens.json",
        templates/"attention-plan.json": project/"motion/attention-plan.json",
    }
    for src, dst in copies.items():
        if not dst.exists(): shutil.copy2(src, dst)
    source = Path(args.source).expanduser() if args.source else None
    source_info = {"path": str(source) if source else "", "sha256": sha256_path(source) if source else ""}
    # The state template is the schema of record; filling it here keeps the file
    # in templates/ from becoming a second, silently diverging definition.
    state = json.loads((templates/"project-state.json").read_text(encoding="utf-8"))
    state.update({
        "project_id": slugify(args.title),
        "title": args.title,
        "source": source_info,
        "history": [{"at": now(), "action": "init", "phase": "analysis", "note": f"Source: {source_info['path']}"}],
    })
    save_state(project, state)
    print(f"Initialized: {project}")
    print("Current phase: analysis")


def cmd_status(args):
    project = Path(args.project).resolve(); state = load_state(project)
    print(f"Project: {state['title']} ({state['project_id']})")
    print(f"Current phase: {state['current_phase']}")
    for p in PHASES:
        x = state["phases"][p]
        print(f"- {p:8s} {x['status']:15s} v{x.get('version',0)}")


def cmd_mark(args):
    project = Path(args.project).resolve(); state = load_state(project); phase=args.phase
    require_previous_approved(state, phase)
    if args.status not in VALID_STATUS: raise SystemExit("Invalid status")
    state["phases"][phase]["status"] = args.status
    state["phases"][phase]["note"] = args.note or ""
    if args.status in {"in_progress","pending_review","needs_revision"}:
        state["current_phase"] = phase
    event(state, f"mark:{args.status}", phase, args.note or "")
    save_state(project,state); print(f"{phase}: {args.status}")


def cmd_approve(args):
    project = Path(args.project).resolve(); state = load_state(project); phase=args.phase
    require_previous_approved(state, phase)
    missing=[str(p) for p in artifact_requirements(project,phase) if not p.exists()]
    if missing and not args.force:
        raise SystemExit("Cannot approve; missing artifacts:\n- " + "\n- ".join(missing))
    x=state["phases"][phase]
    x["status"]="approved"; x["approved_at"]=now(); x["note"]=args.note or ""; x["version"]=max(1,int(x.get("version",0)))
    idx=PHASES.index(phase)
    if idx+1 < len(PHASES):
        nxt=PHASES[idx+1]
        if state["phases"][nxt]["status"] in {"blocked","invalidated"}: state["phases"][nxt]["status"]="not_started"
        state["current_phase"] = nxt
    else:
        state["current_phase"] = phase; state["status"]="completed"
    event(state,"approve",phase,args.note or "")
    save_state(project,state); print(f"Approved: {phase}")
    if idx+1 < len(PHASES): print(f"Unlocked: {PHASES[idx+1]} (not executed)")


def invalidate_downstream(state: dict, phase: str):
    idx=PHASES.index(phase)
    for p in PHASES[idx+1:]:
        state["phases"][p]["status"]="invalidated"
        state["phases"][p]["approved_at"]=None


def cmd_revise(args):
    project=Path(args.project).resolve(); state=load_state(project); phase=args.phase
    state["phases"][phase]["status"]="needs_revision"
    state["phases"][phase]["version"]=int(state["phases"][phase].get("version",0))+1
    state["phases"][phase]["approved_at"]=None
    state["phases"][phase]["note"]=args.note or ""
    invalidate_downstream(state,phase); state["current_phase"]=phase
    event(state,"revise",phase,args.note or ""); save_state(project,state)
    print(f"Revision requested: {phase}; downstream phases invalidated.")


def cmd_rollback(args):
    project=Path(args.project).resolve(); state=load_state(project); phase=args.phase
    state["phases"][phase]["status"]="needs_revision"; state["phases"][phase]["approved_at"]=None
    invalidate_downstream(state,phase); state["current_phase"]=phase; state["status"]="active"
    event(state,"rollback",phase,args.note or ""); save_state(project,state)
    print(f"Rolled back to: {phase}")


def parser():
    p=argparse.ArgumentParser(); sub=p.add_subparsers(dest="cmd",required=True)
    s=sub.add_parser("init"); s.add_argument("project"); s.add_argument("--title",required=True); s.add_argument("--source",default=""); s.set_defaults(func=cmd_init)
    s=sub.add_parser("status"); s.add_argument("project"); s.set_defaults(func=cmd_status)
    for name,func in [("approve",cmd_approve),("revise",cmd_revise),("rollback",cmd_rollback)]:
        s=sub.add_parser(name); s.add_argument("project"); s.add_argument("phase",choices=PHASES); s.add_argument("--note",default="")
        if name=="approve": s.add_argument("--force",action="store_true")
        s.set_defaults(func=func)
    s=sub.add_parser("mark"); s.add_argument("project"); s.add_argument("phase",choices=PHASES); s.add_argument("status",choices=sorted(VALID_STATUS)); s.add_argument("--note",default=""); s.set_defaults(func=cmd_mark)
    return p

if __name__=="__main__":
    a=parser().parse_args(); a.func(a)
