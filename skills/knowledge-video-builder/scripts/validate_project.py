#!/usr/bin/env python3
"""Validate required artifacts, state gates, and basic data consistency."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

sys.path.insert(0, str(Path(__file__).resolve().parent))
# project.py owns the phase list, the status vocabulary, and the artifact gate.
# Importing them keeps this validator from drifting into a second opinion about
# what a phase requires.
from project import PHASES, REQUIRED_ARTIFACTS as REQ, VALID_STATUS

def load(p): return json.loads(p.read_text(encoding="utf-8"))

def main():
 ap=argparse.ArgumentParser(); ap.add_argument("project"); ap.add_argument("--phase",choices=PHASES,default="render"); args=ap.parse_args(); project=Path(args.project).resolve()
 issues=[]; statep=project/"project-state.json"
 if not statep.exists(): issues.append(("critical",f"Missing {statep}")); state=None
 else: state=load(statep)
 upto=PHASES.index(args.phase)
 for phase in PHASES[:upto+1]:
  for rel in REQ[phase]:
   if not (project/rel).exists(): issues.append(("high",f"Missing required artifact for {phase}: {rel}"))
  if state:
   entry=state.get("phases",{}).get(phase)
   if entry is None: issues.append(("high",f"Missing state entry for phase: {phase}"))
   else:
    status=entry.get("status")
    # A status outside VALID_STATUS is drift, not a gate failure. Reporting it as
    # "not approved" sends the reader looking for a missing approval that happened.
    if status not in VALID_STATUS: issues.append(("high",f"Invalid status {status!r} for phase {phase}; expected one of {sorted(VALID_STATUS)}"))
    elif phase!=args.phase and status!="approved": issues.append(("high",f"Upstream phase not approved: {phase} (status: {status})"))
 if state:
  for key in state.get("phases",{}):
   if key not in PHASES: issues.append(("info",f"Unknown phase key in state: {key}; project.py only tracks {PHASES}"))
 planp=project/"script/scene-plan.json"; timep=project/"timing/scenes.json"; evp=project/"analysis/evidence-map.json"
 if planp.exists():
  try:
   plan=load(planp); scenes=plan.get("scenes",[]); ids=[x.get("id") for x in scenes]
   if len(ids)!=len(set(ids)): issues.append(("high","Duplicate scene IDs"))
   if evp.exists():
    ev=load(evp); valid={x.get("id") for x in ev.get("claims",ev if isinstance(ev,list) else [])}
    for s in scenes:
     for eid in s.get("evidence_ids",[]):
      if eid not in valid: issues.append(("high",f"Scene {s.get('id')} references missing evidence {eid}"))
   if timep.exists():
    tm=load(timep); tids={x.get("id") for x in tm.get("scenes",[])}
    for sid in ids:
     if sid not in tids: issues.append(("high",f"Missing timing for scene {sid}"))
  except Exception as e: issues.append(("critical",f"Invalid project JSON: {e}"))
 # The canvas is declared in three files. When they disagree the project renders at
 # one size and lays out for another, which stays invisible until a frame comes back
 # with the content off-centre or clipped.
 canvases={}
 for rel,key in (("project-config.json","video"),("script/scene-plan.json","project"),("motion/style-tokens.json","canvas")):
  p=project/rel
  if not p.exists(): continue
  try: block=load(p).get(key) or {}
  except Exception as e: issues.append(("critical",f"Invalid JSON in {rel}: {e}")); continue
  if block.get("width") and block.get("height"): canvases[rel]=(int(block["width"]),int(block["height"]))
 if len(set(canvases.values()))>1:
  issues.append(("high","Canvas size disagrees between files: "+"; ".join(f"{r}={w}x{h}" for r,(w,h) in canvases.items())))
 if issues:
  for sev,msg in issues: print(f"[{sev.upper()}] {msg}")
  if any(s in {"critical","high"} for s,_ in issues): sys.exit(1)
 else: print(f"Validation passed through phase: {args.phase}")

if __name__=="__main__": main()
