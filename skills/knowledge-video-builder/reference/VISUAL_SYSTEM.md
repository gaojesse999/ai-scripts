# Visual System

## Direction

Modern editorial knowledge motion, not generic dashboard UI.

## Containers

Use few containers. Prefer alignment, hierarchy, local rules, number columns, chapter tracks, and accent rails. Containers should clarify grouping.

## Controls

- thin low-contrast border;
- restrained surface difference;
- low/moderate radius;
- small local accent;
- consistent component heights and spacing;
- no large neon glow or thick active-card outline.

## Typography

- CJK: Source Han Sans / Noto Sans CJK
- Latin/numbers: Inter or compatible grotesk
- main title: semibold/bold
- body/list/subtitle: regular/medium
- do not use bold everywhere

Render text natively at target resolution or supersample down. Preserve original alpha antialiasing. Never use optical-flow interpolation for text motion.

## Semantic color

Use a small stable palette. Example:

- orange: current emphasis/action
- green: correct/success
- red: error/risk
- purple: AI/model
- neutral grays: hierarchy/context

Color meaning must remain consistent across the video.
