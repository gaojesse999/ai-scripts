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

## Visual checks

- No text overflow.
- Mobile-readable type size.
- Safe margins respected.
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
