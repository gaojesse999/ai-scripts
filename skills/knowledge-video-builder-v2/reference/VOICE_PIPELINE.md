# Voice and Timing Pipeline

Narration audio comes from the user by default. Built-in TTS is the fallback.

## Handoff

1. Lock narration wording.
2. Deliver the script and ask the user to produce the audio from it: per-scene files preferred, 48 kHz WAV, no music bed, no added tail silence, plus any timing metadata their engine exports.
3. Ask once. This is a required input, not an approval gate, so it applies in direct production mode too.

## Path A ¡ª supplied audio (default)

1. Verify the spoken wording matches `SCRIPT.md`, checking the start and end of every segment.
2. Where delivery deviates, the audio wins: rewrite `SCRIPT.md` to what was spoken and re-anchor any beat cue whose wording changed.
3. Keep originals under `inputs/voice/`; normalize copies to 48 kHz WAV.
4. Derive scene boundaries from per-scene files, or from sentence positions in the alignment output ¡ª never from duration arithmetic.
5. Force-align against the known script to get word timing. Verify each scene's aligned span against its measured audio span.

## Path B ¡ª generated audio (fallback)

Use when the user cannot supply audio, asks for synthesis, or provides nothing after being asked.

1. Synthesize per scene, respecting `script/pronunciation.json`.
2. Capture engine word boundaries during synthesis. With `edge-tts` pass `boundary="WordBoundary"`; the default is sentence-level and too coarse for beat anchoring.
3. Correct pronunciation and pacing by re-synthesizing only the affected segment.
4. Label the result as placeholder-grade voice.

## Shared

1. Merge to a final master, then measure it and report any deviation from the expected sum.
2. Produce word/sentence/scene timing and captions from that measured master.
3. Verify audio and subtitle correspondence.
4. Record the source path and timing method in `audio/tts-manifest.json`.

Visual timing must follow this final master. SRT controls subtitle visibility; word/sentence timing controls semantic reveal points.

Keep trailing silence out of the segments and store per-scene padding in `audio/tail-silence.json`, so pacing changes rebuild the master without touching voice.
