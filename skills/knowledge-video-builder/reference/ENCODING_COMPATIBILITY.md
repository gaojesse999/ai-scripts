# Encoding Compatibility

Default universal delivery:

- 2520×1080 for the default 21:9 canvas, or 1920×1080 for 16:9
- 30 fps constant frame rate
- H.264 Baseline-compatible / Constrained Baseline
- no B-frames
- Level chosen from the canvas — see [Pick the level from the canvas](#pick-the-level-from-the-canvas-not-from-habit)
- yuv420p
- AAC 48 kHz, 128 kbps+
- MP4 fast start

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -profile:v baseline -level:v 5.0 \
  -pix_fmt yuv420p -r 30 -fps_mode cfr \
  -x264-params "bframes=0" \
  -movflags +faststart \
  -c:a aac -ar 48000 -b:a 128k \
  final-1080p-universal.mp4
```

## Pick the level from the canvas, not from habit

A level is a claim about what a decoder must be able to handle, and x264 checks the
claim. Give it a level that is too low and it prints

```text
frame MB size (158x68) > level limit (8192)
MB rate (322320) > level limit (245760)
```

and then **encodes anyway and exits 0**. The result is a stream that violates the
level it declares, which is the opposite of what this pass exists for, and nothing
in the exit code or the file listing tells you.

The default 21:9 canvas does not fit Level 4.0:

| canvas | macroblocks | MB rate @30 | smallest level that covers it |
|---|---|---|---|
| 2520×1080 (21:9) | 158×68 = 10744 | 322320 | **5.0** (22080 / 589824) |
| 1920×1080 (16:9) | 120×68 = 8160 | 244800 | 4.0 (8192 / 245760) |
| 1680×720 (21:9 preview) | 105×45 = 4725 | 141750 | 4.0 |

Baseline constrains features — no B-frames, no CABAC — not level, so
`-profile:v baseline -level:v 5.0` is a valid pairing.

Verify the result instead of trusting the command; a wrong level does not fail:

```bash
ffprobe -v error -select_streams v \
  -show_entries stream=profile,level,has_b_frames,pix_fmt -of default=nw=1 out.mp4
```

Do not pass `-s`/`-vf scale`: the master already carries the canvas size from the composition, and rescaling here is how an aspect gets silently changed during the compatibility pass.

Also produce a lightweight 720p preview when in-app/browser preview compatibility matters — `1680x720` at 21:9, `1280x720` at 16:9, both an exact two-thirds of the master. A High/Main Profile master may be included separately, but should not be the only deliverable unless verified.
