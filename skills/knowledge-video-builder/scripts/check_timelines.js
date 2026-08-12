// Executes each composition's timeline script with a stubbed GSAP.
// A thrown anchor lookup would otherwise surface only as a video whose every
// frame is the initial state, which is easy to miss and expensive to find.
import { readdirSync, readFileSync } from "fs";
import { join } from "path";

const dir = process.argv[2];
let failed = 0;

for (const file of readdirSync(dir).filter((f) => /^S\d+\.html$/.test(f)).sort()) {
  const html = readFileSync(join(dir, file), "utf8");
  const script = html.match(/<script>([\s\S]*?)<\/script>\s*<\/body>/)?.[1]
    ?? html.match(/<script>([\s\S]*)<\/script>/)?.[1];
  if (!script) { console.log(`${file}: no timeline script`); failed++; continue; }

  const cues = [];
  const track = (kind) => (target, a, b, c) => {
    const at = kind === "fromTo" ? c : b;
    cues.push({ kind, target: String(target), at: typeof at === "number" ? at : null });
  };
  const tl = {
    to: track("to"), fromTo: track("fromTo"), set: track("set"),
    call: track("call"), add: track("add"),
  };
  const gsap = { timeline: () => tl };
  const win = { __timelines: {} };

  try {
    new Function("gsap", "window", "document", script)(gsap, win, {
      getElementById: () => ({ style: {}, textContent: "" }),
    });
  } catch (err) {
    console.log(`${file}: ${err.message}`);
    failed++;
    continue;
  }

  const timed = cues.filter((c) => c.at !== null);
  const duration = Number(script.match(/const D = ([\d.]+);/)?.[1] ?? 0);
  const outside = timed.filter((c) => c.at < -0.001 || c.at > duration + 0.001);
  const late = [...timed].sort((a, b) => b.at - a.at)[0];
  console.log(
    `${file}: ${timed.length} keyframes, ${outside.length} outside 0-${duration}, ` +
    `last at ${late ? late.at.toFixed(2) : "-"}s`
  );
  for (const c of outside) {
    console.log(`   ! ${c.target} at ${c.at.toFixed(2)}s`);
    failed++;
  }
}

process.exit(failed ? 1 : 0);
