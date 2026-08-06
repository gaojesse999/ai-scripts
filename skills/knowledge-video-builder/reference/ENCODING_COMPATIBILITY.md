# Encoding Compatibility

Default universal delivery:

- 1920×1080
- 30 fps constant frame rate
- H.264 Baseline-compatible / Constrained Baseline
- no B-frames
- Level 4.0
- yuv420p
- AAC 48 kHz, 128 kbps+
- MP4 fast start

```bash
ffmpeg -i input.mp4 \
  -c:v libx264 -profile:v baseline -level:v 4.0 \
  -pix_fmt yuv420p -r 30 -fps_mode cfr \
  -x264-params "bframes=0" \
  -movflags +faststart \
  -c:a aac -ar 48000 -b:a 128k \
  final-1080p-universal.mp4
```

Also produce a lightweight 720p preview when in-app/browser preview compatibility matters. A High/Main Profile master may be included separately, but should not be the only deliverable unless verified.
