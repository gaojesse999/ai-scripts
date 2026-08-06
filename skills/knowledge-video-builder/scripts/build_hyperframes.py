#!/usr/bin/env python3
'''Generate a timed HyperFrames scaffold with a reusable editorial explainer system.'''
from __future__ import annotations

import argparse
import html
import json
import re
from pathlib import Path


SCENE_CSS = r'''
:root{--bg:#171917;--surface:#292b29;--surface2:#343735;--ink:#f5f5f0;--muted:#8b9089;--accent:#ff9f0a;--danger:#ff5362;--success:#39d98a;--blue:#5f8fff;--purple:#a875ff;--teal:#26c4aa;--line:#656963}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:var(--bg);font-family:Arial,"Microsoft YaHei",sans-serif;color:var(--ink)}
.frame{position:relative;width:1920px;height:1080px;padding:92px 124px 140px;background:var(--bg)}
.top{position:absolute;top:30px;left:124px;right:124px;height:30px;display:flex;align-items:center;gap:14px;color:var(--muted);font-size:20px;font-weight:700}.chapter-index{color:var(--accent);font-variant-numeric:tabular-nums}.chapter-name{white-space:nowrap}.rail{height:5px;flex:1;background:#343735;border-radius:5px;overflow:hidden;margin-left:18px}.rail-fill{height:100%;background:var(--accent);transform-origin:left center}
.content{height:100%;display:flex;flex-direction:column;justify-content:center;gap:34px}.eyebrow{display:inline-flex;align-self:flex-start;padding:10px 18px;border:1px solid var(--accent);border-radius:24px;color:var(--accent);font-size:22px;font-weight:800;letter-spacing:.02em}.headline{font-size:78px;line-height:1.06;max-width:1440px;margin:0;font-weight:900;letter-spacing:.01em}.lede{max-width:1180px;color:var(--muted);font-size:30px;line-height:1.45;margin:0}.accent-line{height:8px;width:138px;background:var(--accent);border-radius:8px;transform-origin:left center}
.visual{min-height:300px;display:flex;align-items:center;justify-content:center}.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;width:100%}.card{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:28px 30px;min-height:120px;font-size:31px;font-weight:800}.card small{display:block;color:var(--muted);font-size:20px;margin-top:12px;font-weight:600}.card.accent{border-color:var(--accent)}.card.danger{border-color:var(--danger)}.card.success{border-color:var(--success)}.card.blue{border-color:var(--blue)}.card.purple{border-color:var(--purple)}.card.teal{border-color:var(--teal)}
.columns{display:grid;grid-template-columns:1fr 1fr;gap:28px;width:100%}.column{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:26px 30px;min-height:240px}.column h3{margin:0 0 18px;color:var(--accent);font-size:28px}.column.danger{border-color:var(--danger)}.column.danger h3{color:var(--danger)}.column.success{border-color:var(--success)}.column.success h3{color:var(--success)}.column ul{list-style:none;margin:0;padding:0}.column li{font-size:28px;padding:11px 0;border-bottom:1px solid #444844}.column li:last-child{border-bottom:0}
.flow{display:flex;align-items:center;justify-content:center;gap:14px;width:100%}.step{min-width:220px;background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:28px 22px;text-align:center;font-size:28px;font-weight:800}.step.active{border-color:var(--accent);color:var(--accent)}.arrow{color:var(--accent);font-size:40px;font-weight:900}
.code-panel{width:100%;background:#101210;border:2px solid var(--accent);border-radius:16px;padding:28px 34px}.code-panel .code-label{color:var(--accent);font-size:22px;font-weight:800;margin-bottom:14px}.code-panel pre{margin:0;color:#e7e9e4;font-family:Consolas,"Courier New",monospace;font-size:27px;line-height:1.48;white-space:pre-wrap}
.nodes{position:relative;width:100%;min-height:300px}.node{position:absolute;background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:22px 28px;min-width:220px;text-align:center;font-size:26px;font-weight:800}.node.central{left:50%;top:0;transform:translateX(-50%);border-color:var(--accent);color:var(--accent)}.node-row{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;gap:20px}.node-row .node{position:static;flex:1}.node-row .node:nth-child(2){border-color:var(--blue)}.node-row .node:nth-child(3){border-color:var(--purple)}.node-row .node:nth-child(4){border-color:var(--teal)}.node-row .node:nth-child(5){border-color:var(--danger)}.connector{position:absolute;left:50%;top:84px;width:2px;height:100px;background:var(--accent);transform-origin:top center}.metric-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;width:100%}.metric{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:26px}.metric .value{font-size:56px;color:var(--accent);font-weight:900}.metric .label{font-size:24px;font-weight:800;margin-top:10px}.summary{display:grid;grid-template-columns:1fr 100px 1fr;gap:24px;align-items:center;width:100%}.summary-panel{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:30px;font-size:32px;font-weight:800;min-height:180px}.summary-panel.good{border-color:var(--success)}.summary-panel.bad{border-color:var(--danger)}.summary-arrow{font-size:58px;color:var(--accent);text-align:center}
.caption{position:absolute;left:50%;bottom:44px;transform:translateX(-50%);max-width:78%;padding:18px 28px;border-radius:10px;background:rgba(0,0,0,.94);color:#fff;text-align:center;font-size:30px;line-height:1.35;font-weight:800;z-index:5}.footer{position:absolute;left:124px;bottom:42px;color:var(--muted);font-size:18px;letter-spacing:.04em}
'''

SCENE_MOTION_CSS = r'''
.stage-nav{position:absolute;top:76px;left:124px;right:124px;display:flex;gap:18px;z-index:3}.stage{flex:1;text-align:center;padding:9px 14px;border:1px solid var(--surface2);border-radius:24px;color:var(--muted);font:800 20px/1.2 Arial,"Microsoft YaHei",sans-serif}.stage.active{border-color:var(--accent);color:var(--accent);box-shadow:inset 0 -3px 0 var(--accent);background:rgba(255,159,10,.08)}
'''


def load(path: Path, default=None):
    if not path.exists():
        return default
    return json.loads(path.read_text(encoding="utf-8"))


def js(value) -> str:
    return json.dumps(value, ensure_ascii=False)


def safe_id(value: str) -> str:
    return re.sub(r"[^A-Za-z0-9_-]", "-", value)


def esc(value) -> str:
    return html.escape(str(value or ""))


def render_cards(items, tone=""):
    items = items or ["One primary idea"]
    return '<div class="cards">' + ''.join(
        f'<div class="card {esc(tone)}">{esc(item)}</div>' for item in items[:6]
    ) + '</div>'


def render_visual(scene):
    data = scene.get("visual_data") or {}
    layout = scene.get("layout") or scene.get("visual_type") or "hero"
    items = scene.get("screen_text") or [scene.get("purpose", "One primary idea")]

    if layout == "compare":
        columns = data.get("columns") or []
        if not columns:
            mid = max(1, len(items) // 2)
            columns = [
                {"label": "Before", "items": items[:mid], "tone": "danger"},
                {"label": "After", "items": items[mid:], "tone": "success"},
            ]
        body = []
        for column in columns[:2]:
            li = ''.join(f'<li>{esc(item)}</li>' for item in column.get("items", []))
            body.append(f'<div class="column {esc(column.get("tone", ""))}"><h3>{esc(column.get("label", ""))}</h3><ul>{li}</ul></div>')
        return '<div class="columns">' + ''.join(body) + '</div>'

    if layout == "flow":
        steps = data.get("steps") or [{"label": item} for item in items[:6]]
        body = []
        for index, step in enumerate(steps):
            if index:
                body.append('<div class="arrow">&rarr;</div>')
            body.append(f'<div class="step {"active" if step.get("active") else ""}">{esc(step.get("label", ""))}</div>')
        return '<div class="flow">' + ''.join(body) + '</div>'

    if layout == "code":
        code = data.get("code") or "// Add a short source excerpt here"
        return f'<div class="code-panel"><div class="code-label">{esc(data.get("label", "Source excerpt"))}</div><pre>{esc(code)}</pre></div>'

    if layout == "architecture":
        nodes = data.get("nodes") or [{"label": item} for item in items[:5]]
        children = ''.join(f'<div class="node">{esc(node.get("label", ""))}</div>' for node in nodes[:5])
        central = esc(data.get("central", scene.get("purpose", "System")))
        return f'<div class="nodes"><div class="node central">{central}</div><div class="connector"></div><div class="node-row">{children}</div></div>'

    if layout == "metric-grid":
        metrics = data.get("metrics") or [{"value": item, "label": ""} for item in items[:4]]
        body = ''.join(f'<div class="metric"><div class="value">{esc(metric.get("value", ""))}</div><div class="label">{esc(metric.get("label", ""))}</div></div>' for metric in metrics[:4])
        return '<div class="metric-grid">' + body + '</div>'

    if layout == "summary":
        panels = data.get("panels") or [
            {"label": "Problem", "tone": "bad", "items": items[:1]},
            {"label": "Solution", "tone": "good", "items": items[1:2] or items[:1]},
        ]
        panel_html = []
        for panel in panels[:2]:
            text = '<br>'.join(esc(item) for item in panel.get("items", []))
            panel_html.append(f'<div class="summary-panel {esc(panel.get("tone", ""))}"><small>{esc(panel.get("label", ""))}</small><br>{text}</div>')
        return '<div class="summary">' + panel_html[0] + '<div class="summary-arrow">&rarr;</div>' + panel_html[1] + '</div>'

    return render_cards(items, "accent" if layout == "hero" else "")


def parse_srt(path: Path):
    if not path.exists():
        return []
    content = path.read_text(encoding="utf-8-sig")
    blocks = re.split(r"\r?\n\r?\n+", content.strip())
    cue_re = re.compile(r"(?P<h>\d{2}):(?P<m>\d{2}):(?P<s>\d{2}),(?P<ms>\d{3})")

    def seconds(value):
        match = cue_re.match(value)
        if not match:
            return 0.0
        return int(match.group("h")) * 3600 + int(match.group("m")) * 60 + int(match.group("s")) + int(match.group("ms")) / 1000

    cues = []
    for block in blocks:
        lines = block.splitlines()
        time_line = next((line for line in lines if "-->" in line), None)
        if not time_line:
            continue
        start_text, end_text = [part.strip() for part in time_line.split("-->", 1)]
        text = " ".join(line.strip() for line in lines if line.strip() and "-->" not in line and not line.strip().isdigit())
        cues.append({"start": seconds(start_text), "end": seconds(end_text), "text": text})
    return cues


def render_captions(path: Path):
    cues = parse_srt(path)
    return ''.join(
        f'<div class="caption clip" data-start="{cue["start"]:.3f}" data-duration="{max(0.01, cue["end"] - cue["start"]):.3f}" data-track-index="2">{esc(cue["text"])}</div>'
        for cue in cues if cue["text"]
    )


def render_stage_nav(scene, active_index):
    labels = scene.get("stage_labels") or ["Script", "Assets", "Space", "Prompt", "Shot", "Deliver"]
    spans = []
    for index, label in enumerate(labels[:6], 1):
        state = " active" if index == active_index else ""
        spans.append(f'<span class="stage{state}">{esc(label)}</span>')
    return '<div class="stage-nav">' + "".join(spans) + '</div>'


def scene_html(scene, duration, width, height, chapter_index, chapter_count):
    sid = safe_id(scene["id"])
    layout = scene.get("layout") or scene.get("visual_type") or "hero"
    title = scene.get("title") or (scene.get("screen_text") or [scene.get("purpose") or scene.get("chapter") or sid])[0]
    desc = scene.get("visual_description", "")
    percent = min(100, max(0, chapter_index / max(1, chapter_count) * 100))
    caption = scene.get("caption_text", "")
    caption_html = f'<div class="caption">{esc(caption)}</div>' if caption else ''
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script><style>{SCENE_CSS}</style></head><body>
<div class="frame" data-composition-id="{sid}" data-width="{width}" data-height="{height}"><div class="top"><span class="chapter-index">{chapter_index:02d} / {chapter_count:02d}</span><span class="chapter-name">{esc(scene.get('chapter', ''))}</span><div class="rail"><div class="rail-fill" style="width:{percent:.2f}%"></div></div></div><div class="content"><div class="eyebrow">{esc(layout)}</div><div class="accent-line"></div><h1 class="headline">{esc(title)}</h1><p class="lede">{esc(desc)}</p><div class="visual">{render_visual(scene)}</div></div><div class="footer">{esc(scene.get('visual_type', 'knowledge'))} · {duration:.2f}s</div>{caption_html}</div>
<script>const tl=gsap.timeline({{paused:true}});tl.from('.rail-fill',{{scaleX:0,duration:.45}},0);tl.from('.eyebrow,.accent-line',{{opacity:0,y:16,duration:.35,stagger:.08}},.05);tl.from('.headline',{{opacity:0,y:42,duration:.6,ease:'power3.out'}},.15);tl.from('.lede',{{opacity:0,y:18,duration:.45}},.42);tl.from('.visual > *',{{opacity:0,y:20,duration:.55,ease:'power2.out'}},.42);tl.set({{}},{{}},{duration:.6f});window.__timelines=window.__timelines||{{}};window.__timelines[{js(sid)}]=tl;</script></body></html>'''


# Keep the generated composition deterministic and give the renderer a richer default
# than a single generic fade. This definition intentionally shadows the legacy helper
# above so older projects can be regenerated without a migration step.
def scene_html(scene, duration, width, height, chapter_index, chapter_count):
    sid = safe_id(scene["id"])
    layout = scene.get("layout") or scene.get("visual_type") or "hero"
    title = scene.get("title") or (scene.get("screen_text") or [scene.get("purpose") or scene.get("chapter") or sid])[0]
    desc = scene.get("visual_description", "")
    percent = min(100, max(0, chapter_index / max(1, chapter_count) * 100))
    caption = scene.get("caption_text", "")
    caption_html = f'<div class="caption">{esc(caption)}</div>' if caption else ""
    footer = f'{esc(scene.get("visual_type", "knowledge"))} &bull; {duration:.2f}s'
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script><style>{SCENE_CSS}{SCENE_MOTION_CSS}</style></head><body>
<div class="frame" data-composition-id="{sid}" data-width="{width}" data-height="{height}"><div class="top"><span class="chapter-index">{chapter_index:02d} / {chapter_count:02d}</span><span class="chapter-name">{esc(scene.get("chapter", ""))}</span><div class="rail"><div class="rail-fill" style="width:{percent:.2f}%"></div></div></div>{render_stage_nav(scene, chapter_index)}<div class="content"><div class="eyebrow">{esc(layout)}</div><div class="accent-line"></div><h1 class="headline">{esc(title)}</h1><p class="lede">{esc(desc)}</p><div class="visual">{render_visual(scene)}</div></div><div class="footer">{footer}</div>{caption_html}</div>
<script>const tl=gsap.timeline({{paused:true}});tl.from('.rail-fill',{{scaleX:0,duration:.45}},0);tl.from('.stage',{{opacity:0,y:-10,duration:.3,stagger:.05,ease:'power2.out'}},.02);tl.from('.eyebrow,.accent-line',{{opacity:0,y:16,duration:.35,stagger:.08}},.05);tl.from('.headline',{{opacity:0,y:42,duration:.6,ease:'power3.out'}},.15);tl.from('.lede',{{opacity:0,y:18,duration:.45}},.42);tl.from('.visual > *',{{opacity:0,y:20,duration:.55,ease:'power2.out'}},.42);tl.from('.flow .step,.columns .column,.code-panel,.node,.metric,.summary-panel',{{opacity:0,y:22,duration:.5,stagger:.12,ease:'power2.out'}},.72);tl.from('.connector,.arrow',{{scaleX:0,transformOrigin:'left center',duration:.6,ease:'power2.out'}},.9);tl.set({{}},{{}},{duration:.6f});window.__timelines=window.__timelines||{{}};window.__timelines[{js(sid)}]=tl;</script></body></html>'''


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("project")
    args = ap.parse_args()
    project = Path(args.project).resolve()
    plan = load(project / "script/scene-plan.json")
    timing = load(project / "timing/scenes.json")
    if not plan:
        raise SystemExit("Missing script/scene-plan.json")
    if not timing:
        raise SystemExit("Missing timing/scenes.json; final visuals require real audio timing")

    hf = project / "hyperframes"
    comps = hf / "compositions"
    comps.mkdir(parents=True, exist_ok=True)
    (hf / "assets").mkdir(exist_ok=True)
    cfg = plan.get("project", {})
    width = int(cfg.get("width", 1920))
    height = int(cfg.get("height", 1080))
    scenes = plan.get("scenes", [])
    chapter_names = []
    for scene in scenes:
        chapter = scene.get("chapter", "")
        if chapter not in chapter_names:
            chapter_names.append(chapter)
    chapter_count = int(cfg.get("visual_system", {}).get("chapter_count", 0) or len(chapter_names) or 1)
    chapter_indexes = {name: index + 1 for index, name in enumerate(chapter_names)}
    tmap = {item["id"]: item for item in timing.get("scenes", [])}
    hosts = []
    total = float(timing.get("duration", 0) or 0)

    for scene in scenes:
        sid = scene["id"]
        timed = tmap.get(sid)
        if not timed:
            raise SystemExit(f"Missing timing for scene {sid}")
        duration = float(timed.get("duration", float(timed["end"]) - float(timed["start"])))
        chapter_index = chapter_indexes.get(scene.get("chapter", ""), 1)
        (comps / f"{safe_id(sid)}.html").write_text(scene_html(scene, duration, width, height, chapter_index, chapter_count), encoding="utf-8")
        hosts.append(f'<div data-composition-id="host-{safe_id(sid)}" data-composition-src="compositions/{safe_id(sid)}.html" data-start="{float(timed["start"]):.6f}" data-duration="{duration:.6f}" data-track-index="1"></div>')
        total = max(total, float(timed["end"]))

    audio_rel = "../audio/narration.wav"
    audio = f'<audio class="clip" src="{audio_rel}" data-start="0" data-duration="{total:.6f}" data-track-index="0"></audio>' if (project / "audio/narration.wav").exists() else '<!-- narration.wav not found -->'
    captions = render_captions(project / "timing/captions.srt")
    rootid = "knowledge-video"
    index = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>*{{box-sizing:border-box}}html,body{{margin:0;width:100%;height:100%;overflow:hidden;background:#171917}}.caption{{position:absolute;left:50%;bottom:44px;transform:translateX(-50%);max-width:78%;padding:18px 28px;border-radius:10px;background:rgba(0,0,0,.94);color:#fff;text-align:center;font:800 30px/1.35 Arial,"Microsoft YaHei",sans-serif;z-index:20}}</style><script src="https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"></script></head><body><main data-composition-id="{rootid}" data-width="{width}" data-height="{height}">{audio}{''.join(hosts)}{captions}</main><script>const tl=gsap.timeline({{paused:true}});tl.set({{}},{{}},{total:.6f});window.__timelines=window.__timelines||{{}};window.__timelines['{rootid}']=tl;</script></body></html>'''
    (hf / "index.html").write_text(index, encoding="utf-8")
    config = {"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json", "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry", "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"}}
    (hf / "hyperframes.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")
    print(hf / "index.html")
    print("Generated an editorial-technical-dark scaffold with reusable layouts and a timed caption layer.")


if __name__ == "__main__":
    main()
