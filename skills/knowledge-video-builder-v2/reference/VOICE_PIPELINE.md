# Voice and Timing Pipeline

1. Lock narration wording.
2. Generate/import scene-level audio.
3. Correct pronunciation and pacing locally.
4. Merge to a final audio master.
5. Align the final master to words/sentences/scenes.
6. Produce captions from the same final audio.
7. Verify audio and subtitle correspondence.

Visual timing must follow this final master. SRT controls subtitle visibility; word/sentence timing controls semantic reveal points when available.

Prefer engine boundary metadata for step 5. With `edge-tts` pass `boundary="WordBoundary"`; the default is sentence-level and too coarse for beat anchoring. Use forced alignment or ASR only for supplied audio or engines without boundary events.

Keep trailing silence out of synthesis and store per-scene padding in `audio/tail-silence.json`, so pacing changes rebuild the master without re-synthesizing voice.
