#!/usr/bin/env python3
'''Build a static storyboard review page from the canonical scene plan.'''
from __future__ import annotations
import argparse, html, json
from pathlib import Path


def read_json(p: Path, default=None):
    if not p.exists(): return default
    return json.loads(p.read_text(encoding="utf-8"))


def fmt(t):
    if t is None: return "—"
    m=int(t//60); s=t-m*60
    return f"{m:02d}:{s:05.2f}"


def main():
    ap=argparse.ArgumentParser(); ap.add_argument("project"); args=ap.parse_args()
    project=Path(args.project).resolve()
    plan=read_json(project/"script/scene-plan.json")
    if not plan: raise SystemExit("Missing script/scene-plan.json")
    timing=read_json(project/"timing/scenes.json", {"scenes":[]})
    tmap={x["id"]:x for x in timing.get("scenes",[])}
    cards=[]
    for scene in plan.get("scenes",[]):
        sid=scene.get("id","?"); t=tmap.get(sid,{})
        texts="".join(f"<li>{html.escape(str(x))}</li>" for x in scene.get("screen_text",[])) or "<li>—</li>"
        beats="".join(f"<li><b>{html.escape(str(x.get('anchor','')))}</b> {html.escape(str(x.get('action','')))}</li>" for x in scene.get("visual_beats",[])) or "<li>—</li>"
        evidence=", ".join(scene.get("evidence_ids",[])) or "—"
        assets=", ".join(map(str,scene.get("assets",[]))) or "—"
        layout=html.escape(str(scene.get("layout", scene.get("visual_type", ""))))
        visual_data=html.escape(json.dumps(scene.get("visual_data", {}), ensure_ascii=False))
        caption=html.escape(json.dumps(scene.get("caption", {}), ensure_ascii=False))
        cards.append(f'''<article class="scene">
<header><div><span class="id">{html.escape(sid)}</span><h2>{html.escape(scene.get('chapter',''))}</h2></div><div class="time">{fmt(t.get('start'))}–{fmt(t.get('end'))}<small>{t.get('duration',scene.get('estimated_duration','—'))}s</small></div></header>
<div class="grid"><section><h3>Purpose</h3><p>{html.escape(scene.get('purpose',''))}</p><h3>Narration</h3><p class="narration">{html.escape(scene.get('narration',''))}</p></section>
<section><h3>Screen text</h3><ul>{texts}</ul><h3>Visual</h3><p><b>{layout}</b> — {html.escape(scene.get('visual_description',''))}</p><p><b>Visual data:</b> {visual_data}</p><p><b>Caption:</b> {caption}</p></section></div>
<div class="grid foot"><section><h3>Visual beats</h3><ul>{beats}</ul></section><section><h3>Evidence / Assets</h3><p>Evidence: {html.escape(evidence)}</p><p>Assets: {html.escape(assets)}</p></section></div>
</article>''')
    title=html.escape(plan.get("project",{}).get("title", project.name))
    doc=f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} Storyboard</title>
<style>*{{box-sizing:border-box}}body{{margin:0;background:#f4f5f7;color:#15171a;font-family:Arial,"Microsoft YaHei",sans-serif}}main{{width:min(1440px,94vw);margin:56px auto}}.hero{{margin-bottom:40px}}h1{{font-size:48px;margin:0 0 10px}}.sub{{color:#616974}}.scene{{background:#fff;border:1px solid #dde1e6;border-radius:22px;margin:24px 0;padding:30px;box-shadow:0 8px 24px rgba(15,23,42,.05)}}header{{display:flex;justify-content:space-between;gap:20px;border-bottom:1px solid #e8ebef;padding-bottom:20px;margin-bottom:24px}}header>div:first-child{{display:flex;align-items:center;gap:16px}}.id{{font-weight:800;background:#111827;color:white;padding:9px 13px;border-radius:9px}}h2{{margin:0;font-size:28px}}.time{{font-variant-numeric:tabular-nums;font-size:20px;text-align:right}}.time small{{display:block;color:#7b8491;margin-top:4px}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:32px}}.foot{{margin-top:18px;padding-top:18px;border-top:1px solid #eef0f3}}h3{{font-size:14px;text-transform:uppercase;letter-spacing:.08em;color:#687180;margin:0 0 8px}}p,li{{font-size:18px;line-height:1.65}}.narration{{font-size:21px}}ul{{padding-left:22px}}@media(max-width:800px){{.grid{{grid-template-columns:1fr}}h1{{font-size:36px}}header{{flex-direction:column}}.time{{text-align:left}}}}</style></head><body><main><section class="hero"><h1>{title}</h1><div class="sub">Storyboard review generated from scene-plan.json and timing/scenes.json</div></section>{''.join(cards)}</main></body></html>'''
    out=project/"review/storyboard.html"; out.parent.mkdir(parents=True,exist_ok=True); out.write_text(doc,encoding="utf-8")
    print(out)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    args = ap.parse_args()
    project = Path(args.project).resolve()
    plan = read_json(project / "script/scene-plan.json")
    if not plan:
        raise SystemExit("Missing script/scene-plan.json")
    timing = read_json(project / "timing/scenes.json", {"scenes": []})
    tmap = {item["id"]: item for item in timing.get("scenes", [])}
    cards = []
    for scene in plan.get("scenes", []):
        sid = str(scene.get("id", "?"))
        timed = tmap.get(sid, {})
        texts = "".join(f"<li>{html.escape(str(item))}</li>" for item in scene.get("screen_text", [])) or "<li>None</li>"
        beat_rows = []
        for beat in scene.get("visual_beats", []):
            if isinstance(beat, dict):
                beat_rows.append(f"<li><b>{html.escape(str(beat.get('anchor', '')))}</b> {html.escape(str(beat.get('action', '')))}</li>")
            else:
                beat_rows.append(f"<li>{html.escape(str(beat))}</li>")
        beats = "".join(beat_rows) or "<li>None</li>"
        evidence = ", ".join(map(str, scene.get("evidence_ids", []))) or "None"
        assets = ", ".join(map(str, scene.get("assets", []))) or "None"
        layout = html.escape(str(scene.get("layout", scene.get("visual_type", ""))))
        visual_data = html.escape(json.dumps(scene.get("visual_data", {}), ensure_ascii=False))
        caption = html.escape(json.dumps(scene.get("caption", {}), ensure_ascii=False))
        start = fmt(timed.get("start"))
        end = fmt(timed.get("end"))
        duration = timed.get("duration", scene.get("estimated_duration", "--"))
        cards.append(f'''<article class="scene"><header><div><span class="id">{html.escape(sid)}</span><h2>{html.escape(str(scene.get("chapter", "")))}</h2></div><div class="time">{start} &rarr; {end}<small>{duration}s</small></div></header>
<div class="grid"><section><h3>Purpose</h3><p>{html.escape(str(scene.get("purpose", "")))}</p><h3>Narration</h3><p class="narration">{html.escape(str(scene.get("narration", "")))}</p></section>
<section><h3>Screen text</h3><ul>{texts}</ul><h3>Visual</h3><p><b>{layout}</b> &bull; {html.escape(str(scene.get("visual_description", "")))}</p><p><b>Visual data:</b> {visual_data}</p><p><b>Caption:</b> {caption}</p></section></div>
<div class="grid foot"><section><h3>Visual beats</h3><ul>{beats}</ul></section><section><h3>Evidence / Assets</h3><p>Evidence: {html.escape(evidence)}</p><p>Assets: {html.escape(assets)}</p></section></div></article>''')
    title = html.escape(str(plan.get("project", {}).get("title", project.name)))
    doc = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width,initial-scale=1"><title>{title} Storyboard</title><style>*{{box-sizing:border-box}}body{{margin:0;background:#f4f5f7;color:#15171a;font-family:Arial,"Microsoft YaHei",sans-serif}}main{{width:min(1440px,94vw);margin:56px auto}}h1{{font-size:48px;margin:0 0 10px}}.sub{{color:#616974;margin-bottom:40px}}.scene{{background:#fff;border:1px solid #dde1e6;border-radius:16px;margin:24px 0;padding:30px;box-shadow:0 8px 24px rgba(15,23,42,.05)}}header{{display:flex;justify-content:space-between;gap:20px;border-bottom:1px solid #e8ebef;padding-bottom:20px;margin-bottom:24px}}header>div:first-child{{display:flex;align-items:center;gap:16px}}.id{{font-weight:800;background:#111827;color:white;padding:9px 13px;border-radius:8px}}h2{{margin:0;font-size:28px}}.time{{font-variant-numeric:tabular-nums;font-size:20px;text-align:right}}.time small{{display:block;color:#7b8491;margin-top:4px}}.grid{{display:grid;grid-template-columns:1fr 1fr;gap:32px}}.foot{{margin-top:18px;padding-top:18px;border-top:1px solid #eef0f3}}h3{{font-size:14px;text-transform:uppercase;letter-spacing:.08em;color:#687180;margin:0 0 8px}}p,li{{font-size:18px;line-height:1.65}}.narration{{font-size:21px}}ul{{padding-left:22px}}@media(max-width:800px){{.grid{{grid-template-columns:1fr}}h1{{font-size:36px}}header{{flex-direction:column}}.time{{text-align:left}}}}</style></head><body><main><h1>{title}</h1><div class="sub">Storyboard review generated from scene-plan.json and timing/scenes.json</div>{''.join(cards)}</main></body></html>'''
    out = project / "review/storyboard.html"
    out.parent.mkdir(parents=True, exist_ok=True)
    out.write_text(doc, encoding="utf-8")
    print(out)


if __name__ == "__main__":
    main()
