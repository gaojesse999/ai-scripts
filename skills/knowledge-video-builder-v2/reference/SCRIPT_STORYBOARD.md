# Script and Storyboard

`SCRIPT.md` contains only spoken words. `STORYBOARD.md` explains visuals. `scene-plan.json` is the canonical narrative/visual model.

A scene is a stable conceptual canvas, not one sentence. Each scene defines persistent elements and semantic beats but does not assign final timestamps before audio alignment.

Each beat anchors to narration through a `cue`: a short verbatim phrase from that scene's narration, placed on the key noun, number, name, or conclusion. Cues must run in beat order within a scene so they resolve by monotonic forward search, and an unresolved cue is a build error rather than an estimated time.

Use short screen text. A spoken paragraph may map to a title, three labels, a process, or a before/after diagram—not a transcript pasted on screen.
