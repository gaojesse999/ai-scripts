#!/usr/bin/env python3
"""Validate required artifacts, state gates, and basic data consistency."""
from __future__ import annotations
import argparse, json, sys
from pathlib import Path

PHASES=["analysis","brief","script","voice","visual","render"]
REQ={
 "analysis":["analysis/overview.md","analysis/evidence-map.json"],
 "brief":["content/content-brief.md"],
 "script":["script/SCRIPT.md","script/STORYBOARD.md","script/scene-plan.json","script/voice-plan.json"],
 "voice":["audio/narration.wav","audio/voice-production.json","timing/scenes.json"],
 "visual":["review/storyboard.html","hyperframes/index.html"],
 "render":["qa/report.md"]}

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
  if state and phase!=args.phase and state["phases"][phase]["status"]!="approved": issues.append(("high",f"Upstream phase not approved: {phase}"))
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
 if issues:
  for sev,msg in issues: print(f"[{sev.upper()}] {msg}")
  if any(s in {"critical","high"} for s,_ in issues): sys.exit(1)
 else: print(f"Validation passed through phase: {args.phase}")

if __name__=="__main__": main()
