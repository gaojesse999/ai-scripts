# Migration from v1

1. Keep approved evidence, brief, script, voice, and subtitle artifacts.
2. Add `motion/` and create `motion-plan.yaml` from final audio timing.
3. Convert sentence-level scene cuts into states inside longer stable scenes.
4. Replace raw `fade/slide/zoom` directions with semantic actions.
5. Mark previous items dormant instead of removing them.
6. Add style tokens and reduce dashboard-style containers.
7. Re-render text natively at target FPS and target/supersampled resolution.
8. Deliver a Baseline-compatible 1080p file and a 720p preview.
