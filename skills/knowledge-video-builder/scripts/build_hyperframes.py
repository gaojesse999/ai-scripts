#!/usr/bin/env python3
'''Generate a timed HyperFrames scaffold with a reusable editorial explainer system.

The output is a starting point, not a deliverable. Each generated composition still
needs its bespoke art direction and the beats from motion/motion-plan.yaml before it
is rendered. See reference/HYPERFRAMES_BUILD.md, "Never ship the scaffold".
'''
from __future__ import annotations

import argparse
import html
import json
import re
import shutil
from pathlib import Path


GSAP_VENDOR_REL = "assets/vendor/gsap.min.js"
GSAP_SOURCE_URL = "https://cdn.jsdelivr.net/npm/gsap@3/dist/gsap.min.js"
CJK_FONT_REL = "assets/fonts/NotoSansSC-VF.ttf"
CJK_FONT_URL = "https://github.com/notofonts/noto-cjk/raw/main/Sans/Variable/TTF/NotoSansSC-VF.ttf"

# The compiler has no deterministic mapping for "Microsoft YaHei" and silently
# substitutes a fallback, so CJK text must come from a vendored face. A variable
# font also avoids the synthesized bold that single-weight families produce.
FONT_CSS = f'''
@font-face{{font-family:"ProjectSans";src:url("{CJK_FONT_REL}") format("truetype");font-weight:100 900;font-display:block}}
'''

SCENE_CSS = r'''
:root{--bg:#171917;--surface:#292b29;--surface2:#343735;--ink:#f5f5f0;--muted:#8b9089;--accent:#ff9f0a;--danger:#ff5362;--success:#39d98a;--blue:#5f8fff;--purple:#a875ff;--teal:#26c4aa;--line:#656963}
*{box-sizing:border-box}html,body{margin:0;width:100%;height:100%;overflow:hidden;background:var(--bg);font-family:"ProjectSans",sans-serif;color:var(--ink)}
.frame{position:relative;width:__W__px;height:__H__px;padding:92px __PADX__px 140px;background:var(--bg)}
.content{height:100%;display:flex;flex-direction:column;justify-content:center;gap:34px}.headline{font-size:78px;line-height:1.06;max-width:__MEASURE__px;margin:0;font-weight:900;letter-spacing:.01em}.accent-line{height:8px;width:138px;background:var(--accent);border-radius:8px;transform-origin:left center}
.visual{min-height:300px;display:flex;align-items:center;justify-content:center}.cards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:22px;width:100%}.card{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:28px 30px;min-height:120px;font-size:31px;font-weight:800}.card small{display:block;color:var(--muted);font-size:20px;margin-top:12px;font-weight:600}.card.accent{border-color:var(--accent)}.card.danger{border-color:var(--danger)}.card.success{border-color:var(--success)}.card.blue{border-color:var(--blue)}.card.purple{border-color:var(--purple)}.card.teal{border-color:var(--teal)}
.columns{display:grid;grid-template-columns:1fr 1fr;gap:28px;width:100%}.column{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:26px 30px;min-height:240px}.column h3{margin:0 0 18px;color:var(--accent);font-size:28px}.column.danger{border-color:var(--danger)}.column.danger h3{color:var(--danger)}.column.success{border-color:var(--success)}.column.success h3{color:var(--success)}.column ul{list-style:none;margin:0;padding:0}.column li{font-size:28px;padding:11px 0;border-bottom:1px solid #444844}.column li:last-child{border-bottom:0}
.flow{display:flex;align-items:center;justify-content:center;gap:14px;width:100%}.step{min-width:220px;background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:28px 22px;text-align:center;font-size:28px;font-weight:800}.step.active{border-color:var(--accent);color:var(--accent)}.arrow{color:var(--accent);font-size:40px;font-weight:900}
.code-panel{width:100%;background:#101210;border:2px solid var(--accent);border-radius:16px;padding:28px 34px}.code-panel .code-label{color:var(--accent);font-size:22px;font-weight:800;margin-bottom:14px}.code-panel pre{margin:0;color:#e7e9e4;font-family:"JetBrains Mono",monospace;font-size:27px;line-height:1.48;white-space:pre-wrap}
.nodes{position:relative;width:100%;min-height:300px}.node{position:absolute;background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:22px 28px;min-width:220px;text-align:center;font-size:26px;font-weight:800}.node.central{left:50%;top:0;transform:translateX(-50%);border-color:var(--accent);color:var(--accent)}.node-row{position:absolute;left:0;right:0;bottom:0;display:flex;justify-content:space-between;gap:20px}.node-row .node{position:static;flex:1}.node-row .node:nth-child(2){border-color:var(--blue)}.node-row .node:nth-child(3){border-color:var(--purple)}.node-row .node:nth-child(4){border-color:var(--teal)}.node-row .node:nth-child(5){border-color:var(--danger)}.connector{position:absolute;left:50%;top:84px;width:2px;height:100px;background:var(--accent);transform-origin:top center}
.metric-grid{display:grid;grid-template-columns:repeat(4,minmax(0,1fr));gap:22px;width:100%}.metric{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:26px}.metric .value{font-size:56px;color:var(--accent);font-weight:900}.metric .label{font-size:24px;font-weight:800;margin-top:10px}
.summary{display:grid;grid-template-columns:1fr 100px 1fr;gap:24px;align-items:center;width:100%}.summary-panel{background:var(--surface);border:2px solid var(--line);border-radius:16px;padding:30px;font-size:32px;font-weight:800;min-height:180px}.summary-panel.good{border-color:var(--success)}.summary-panel.bad{border-color:var(--danger)}.summary-arrow{font-size:58px;color:var(--accent);text-align:center}
'''

# Reveals accumulate, then a focus pass walks the enumerated items in narration order
# and restores the full set. Only opacity is tweened on grouped items: several layouts
# carry a CSS transform (.node.central), which GSAP would discard if it also owned it.
SCENE_JS = r'''
(function () {
  var D = __DURATION__;
  var tl = gsap.timeline({ paused: true });
  var q = function (s) { return Array.prototype.slice.call(document.querySelectorAll(s)); };

  tl.fromTo('.accent-line', { scaleX: 0 }, { scaleX: 1, duration: 0.45, ease: 'power2.out' }, 0.08);
  tl.fromTo('.headline', { opacity: 0, y: 42 }, { opacity: 1, y: 0, duration: 0.6, ease: 'power3.out' }, 0.15);
  tl.fromTo('.node.central', { opacity: 0 }, { opacity: 1, duration: 0.45, ease: 'power2.out' }, 0.55);
  tl.fromTo('.connector', { scaleY: 0 }, { scaleY: 1, duration: 0.5, ease: 'power2.out' }, 0.75);
  tl.fromTo('.code-panel', { opacity: 0, y: 22 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power2.out' }, 0.8);

  var items = q('.cards .card, .columns .column, .flow .step, .metric-grid .metric, .node-row .node, .summary .summary-panel');
  var revealFrom = 0.9;
  var revealTo = Math.min(D * 0.5, revealFrom + items.length * 0.8);
  var stride = items.length > 1 ? (revealTo - revealFrom) / (items.length - 1) : 0;

  items.forEach(function (el, i) {
    tl.fromTo(el, { opacity: 0, y: 24 }, { opacity: 1, y: 0, duration: 0.5, ease: 'power2.out' }, revealFrom + i * stride);
  });
  tl.fromTo('.arrow', { opacity: 0 }, { opacity: 1, duration: 0.3, stagger: 0.1 }, revealFrom + 0.2);

  // Hold the complete structure on screen unless there is real time left to walk it.
  var focusFrom = revealTo + 0.8;
  var focusSpan = D - focusFrom - 0.8;
  if (items.length > 1 && focusSpan > items.length * 0.9) {
    var slot = focusSpan / items.length;
    tl.to(items, { opacity: 0.5, duration: 0.3, ease: 'power2.inOut' }, focusFrom - 0.3);
    items.forEach(function (el, i) {
      var at = focusFrom + i * slot;
      tl.to(el, { opacity: 1, duration: 0.3, ease: 'power2.out' }, at);
      tl.to(el, { opacity: 0.5, duration: 0.3, ease: 'power2.inOut' }, at + slot - 0.3);
    });
    tl.to(items, { opacity: 1, duration: 0.5, ease: 'power2.out' }, focusFrom + focusSpan);
  }

  tl.set({}, {}, D);
  window.__timelines = window.__timelines || {};
  window.__timelines[__SID__] = tl;
})();
'''

# The rail spans the whole video rather than resetting once per scene, so it lives
# here with the caption layer instead of inside each composition.
ROOT_JS = r'''
(function () {
  var tl = gsap.timeline({ paused: true });
  tl.fromTo('#rail-fill', { scaleX: 0 }, { scaleX: 1, duration: __TOTAL__, ease: 'none' }, 0);
  tl.set({}, {}, __TOTAL__);
  window.__timelines = window.__timelines || {};
  window.__timelines[__SID__] = tl;
})();
'''

# A fixed-width label slot keeps the track from shifting sideways when a longer
# chapter name swaps in at a scene boundary.
LABEL_SLOT = 420
ROOT_RAIL_CSS = r'''
.chapter-label{position:absolute;left:__PADX__px;top:30px;height:30px;width:__SLOT__px;display:flex;align-items:center;gap:14px;white-space:nowrap;color:#8b9089;font:700 20px/1.2 "ProjectSans",sans-serif;z-index:25}
.chapter-index{color:#ff9f0a;font-variant-numeric:tabular-nums}
#rail-track{position:absolute;left:__RAILX__px;right:__PADX__px;top:42px;height:5px;background:#343735;border-radius:5px;overflow:hidden;z-index:25}
#rail-fill{height:100%;width:100%;background:#ff9f0a;transform-origin:left center}
'''


# The canvas may be 16:9 or 21:9, so every horizontal constant is derived from the
# configured width rather than written for 1920. Side padding scales with the canvas
# to keep the optical margin constant, but the text measure does not: the extra width
# of an ultrawide canvas is horizontal room for the layout, never a longer line.
def geometry(width, height, measure_cap):
    pad_x = round(width * 124 / 1920)
    return {
        "__W__": str(width),
        "__H__": str(height),
        "__PADX__": str(pad_x),
        "__SLOT__": str(LABEL_SLOT),
        "__RAILX__": str(pad_x + LABEL_SLOT),
        "__MEASURE__": str(min(measure_cap, width - 2 * pad_x)),
    }


def fill(text, geo):
    for token, value in geo.items():
        text = text.replace(token, value)
    return text


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


def scene_html(scene, duration, geo):
    sid = safe_id(scene["id"])
    width, height = geo["__W__"], geo["__H__"]
    title = scene.get("title") or (scene.get("screen_text") or [scene.get("purpose") or scene.get("chapter") or sid])[0]
    timeline = SCENE_JS.replace("__DURATION__", f"{duration:.6f}").replace("__SID__", js(sid))
    return f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><script src="{GSAP_VENDOR_REL}"></script><style>{FONT_CSS}{fill(SCENE_CSS, geo)}</style></head><body>
<div class="frame" data-composition-id="{sid}" data-width="{width}" data-height="{height}"><div class="content"><div class="accent-line"></div><h1 class="headline">{esc(title)}</h1><div class="visual">{render_visual(scene)}</div></div></div>
<script>{timeline}</script></body></html>'''


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
    assets = hf / "assets"
    (assets / "vendor").mkdir(parents=True, exist_ok=True)
    cfg = plan.get("project", {})
    width = int(cfg.get("width", 2520))
    height = int(cfg.get("height", 1080))
    canvas = (load(project / "motion/style-tokens.json", {}) or {}).get("canvas") or {}
    geo = geometry(width, height, int(canvas.get("max_measure", 1440)))
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
    labels = []
    total = float(timing.get("duration", 0) or 0)

    for index, scene in enumerate(scenes):
        sid = scene["id"]
        timed = tmap.get(sid)
        if not timed:
            raise SystemExit(f"Missing timing for scene {sid}")
        start = float(timed["start"])
        duration = float(timed.get("duration", float(timed["end"]) - start))
        # Scene hosts and chapter labels must tile the timeline with no holes. Any
        # inter-scene silence would otherwise land on a frame with no scene at all,
        # which reads as a black flash. Sizing to the next scene's start holds the
        # outgoing scene's last frame through the pause; GSAP clamps a seek past the
        # timeline's end, so the composition's own duration stays at its audio length.
        nxt = tmap.get(scenes[index + 1]["id"]) if index + 1 < len(scenes) else None
        covered = float(nxt["start"]) - start if nxt else duration
        chapter_index = chapter_indexes.get(scene.get("chapter", ""), 1)
        (comps / f"{safe_id(sid)}.html").write_text(scene_html(scene, duration, geo), encoding="utf-8")
        hosts.append(f'<div data-composition-id="host-{safe_id(sid)}" data-composition-src="compositions/{safe_id(sid)}.html" data-start="{start:.6f}" data-duration="{covered:.6f}" data-track-index="1"></div>')
        labels.append(f'<div id="chapter-label-{safe_id(sid)}" class="chapter-label clip" data-start="{start:.6f}" data-duration="{covered:.6f}" data-track-index="3"><span class="chapter-index">{chapter_index:02d} / {chapter_count:02d}</span><span class="chapter-name">{esc(scene.get("chapter", ""))}</span></div>')
        total = max(total, float(timed["end"]))

    # Compositions are served with the project root as base URL, so a "../audio/..."
    # reference resolves above the root and 404s. Copy the narration in instead.
    narration = project / "audio/narration.wav"
    if narration.exists():
        shutil.copyfile(narration, assets / "narration.wav")
        audio = f'<audio class="clip" src="assets/narration.wav" data-start="0" data-duration="{total:.6f}" data-track-index="0"></audio>'
    else:
        audio = '<!-- audio/narration.wav not found -->'

    captions = render_captions(project / "timing/captions.srt")
    rootid = "knowledge-video"
    root_timeline = ROOT_JS.replace("__TOTAL__", f"{total:.6f}").replace("__SID__", js(rootid))
    index = f'''<!doctype html><html lang="zh-CN"><head><meta charset="utf-8"><style>{FONT_CSS}*{{box-sizing:border-box}}html,body{{margin:0;width:100%;height:100%;overflow:hidden;background:#171917}}.caption{{position:absolute;left:50%;bottom:44px;transform:translateX(-50%);max-width:min(78%,{geo["__MEASURE__"]}px);padding:18px 28px;border-radius:10px;background:rgba(0,0,0,.94);color:#fff;text-align:center;font:800 30px/1.35 "ProjectSans",sans-serif;z-index:20}}{fill(ROOT_RAIL_CSS, geo)}</style><script src="{GSAP_VENDOR_REL}"></script></head><body><main data-composition-id="{rootid}" data-start="0" data-duration="{total:.6f}" data-width="{width}" data-height="{height}">{audio}{''.join(hosts)}<div id="rail-track"><div id="rail-fill"></div></div>{''.join(labels)}{captions}</main>
<script>{root_timeline}</script></body></html>'''
    (hf / "index.html").write_text(index, encoding="utf-8")
    config = {"$schema": "https://hyperframes.heygen.com/schema/hyperframes.json", "registry": "https://raw.githubusercontent.com/heygen-com/hyperframes/main/registry", "paths": {"blocks": "compositions", "components": "compositions/components", "assets": "assets"}}
    (hf / "hyperframes.json").write_text(json.dumps(config, indent=2) + "\n", encoding="utf-8")

    print(hf / "index.html")
    print("Generated an editorial-technical-dark scaffold with reusable layouts and a timed caption layer.")
    (assets / "fonts").mkdir(exist_ok=True)
    for label, rel, url, consequence in (
        ("GSAP", GSAP_VENDOR_REL, GSAP_SOURCE_URL, "every composition will freeze on frame one"),
        ("The CJK font", CJK_FONT_REL, CJK_FONT_URL, "text will fall back to a substituted face"),
    ):
        if not (hf / rel).exists():
            print(f"\n!! {label} is missing; {consequence} until you run:\n   curl -Lo {hf / rel} {url}")
    print(
        "\nThis is a scaffold, not a deliverable. Before rendering, each scene still needs:\n"
        "  1. bespoke art direction driven by the scene's own claim, not the default layout;\n"
        "  2. the beats from motion/motion-plan.yaml at their measured anchor times;\n"
        "  3. a snapshot diff across two beats to prove the timeline is actually driven."
    )


if __name__ == "__main__":
    main()
