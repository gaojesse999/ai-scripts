# Quality Assurance

## Severity

- **Critical:** factual error, wrong source attribution, missing audio, blank frames, broken render, severe desync
- **High:** unsupported claim, unreadable text, wrong pronunciation, material scene mismatch, clipped content
- **Medium:** weak pacing, redundant text, inconsistent visual language, minor caption drift
- **Low:** polish issue that does not affect understanding

Final render is blocked by unresolved Critical or High issues.

## Content checks

- Every factual capability and limitation has evidence.
- Inferences are visibly qualified.
- Narration, screen text, and demo do not contradict each other.
- The subject's boundary is explained.
- Commands and current APIs were verified when time-sensitive.

## Voice checks

- Technical names and English terms are pronounced correctly.
- No truncation, repeated words, synthetic artifacts, or unnatural silence.
- Segment joins are smooth.
- Captions reflect final audio.
- Spoken narration and TTS inputs contain no pseudo control tags such as `<#1#>` or `[pause]`.
- Every enabled exact pause in `script/voice-plan.json` has a current application record whose output hash matches the chapter WAV.
- Exact pauses occur after the declared aligned unit and match the requested duration within one audio frame.
- Provider request chunks stay below the configured duration cap; a returned take at the cap is reviewed for truncation.
- `audio/voice-production.json` matches the current TTS plan and records every candidate, rejection reason, and selected take.
- Every selected take passes the configured ASR-coverage, tail-coverage, and active-speech-rate thresholds.
- Every merged chunk ends the configured release after its last audible sample; a chunk trimmed inside its final syllable is a defect even when ASR coverage passed.
- Adjacent selected chunks remain within the configured pace delta; style instructions alone are not evidence of continuity.
- Every normalized chunk is within the LUFS tolerance, below the true-peak ceiling, and has flat factor `0.000`.

## Sync gate

Run `scripts/check_sync.py` after alignment and before rendering. Critical and High findings block the render.

- Every chapter has a current alignment, generated after its audio.
- Any exact pause plan is applied before the final alignment; changing either the plan or chapter WAV invalidates the application record.
- No chapter's audio predates the last script edit.
- Chapter match rate is at or above threshold; low-scoring lines are reviewed against what was heard, not dismissed as recogniser noise.
- Caption cues are ordered, non-empty, inside the chapter, within the character limit, and never truncated with an ellipsis.
- Every beat referenced by a composition exists.
- No keyframe is still written as a literal second.
- Every composition timeline actually builds. `check_timelines.js` runs each one against a stubbed GSAP, because an anchor that throws leaves the timeline unregistered — lint passes, the render succeeds, and every frame shows the initial state.

The failure this gate exists for is silent. A line gets edited, one chapter is not re-recorded, and every downstream number stays plausible while the voice says something else — watching the video does not reliably catch it, because the picture and the caption agree with each other and only the audio disagrees.

## Visual checks

- No text overflow.
- Mobile-readable type size.
- Safe margins respected. Measure the left and right content margins on a frame taken from the **assembled render**, not from a scene snapshot: an unscoped `#root` padding rule shifts the whole film sideways and clips the far edge while every absolutely positioned layer stays correct. See "Sub-composition CSS is only half scoped" in [HYPERFRAMES_BUILD.md](HYPERFRAMES_BUILD.md).
- Scene duration allows comprehension.
- Motion reinforces narration.
- Active accents follow the current sentence or clause. In enumerated scenes, focus advances in spoken order and does not remain fixed on one item.
- No important visual appears before its explanation without intent.
- Missing assets are not hidden with misleading placeholders.

## Technical checks

- All paths resolve.
- HyperFrames lint and inspect pass or exceptions are documented.
- Audio and video duration match within tolerance.
- Correct resolution and aspect ratio.
- Final output opens and seeks correctly.

## QA report structure

```markdown
# QA Report

## Build
## Source accuracy
## Voice and captions
## Visual layout
## Timing
## Technical validation
## Open issues
## Final decision
```
