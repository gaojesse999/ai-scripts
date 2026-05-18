# Screenwriter Skill — quick start

A general-purpose skill-tool for screenwriters. Story-agnostic. Drop the folder into Claude / Cowork / Claude Code as a skill folder.

---

## What's inside

- **`SKILL.md`** — main skill description (read first).
- **`methodology.md`** — McKee + Campbell + Aristotle.
- **`style-rules.md`** — Hollywood-format writing rules.
- **`workflow.md`** — how the skill works with you.
- **`timing-and-cutting.md`** — screen-time estimation and length cutting.
- **`markdown-style.md`** — Hollywood style in Markdown (default output).
- **`templates/`** — empty templates: synopsis, character bible, world / mythology, treatment, story-asset registry.
- **`tools/`** — *(legacy)* `.docx` builders (screenplay, bilingual, treatment).

---

## Language behavior

- The skill **talks to you** in Chinese by default. Switch to English by writing in English.
- The skill **writes screenplay** in the same language as your source material (Chinese, English, or bilingual). If unclear at the start, you'll get one question.
- All instruction files in this folder are in English — they are not user-facing output.

---

## How to start

### Step 1. Install

Copy the `screenwriter-skill/` folder anywhere convenient: inside a Claude Code project, as a user-skill in Cowork (`~/.claude/skills/screenwriter/`), or simply next to your working files.

### Step 2. Tell Claude

> "Load the screenwriter skill — let's start."

Claude will read SKILL.md, methodology, writing rules, and workflow.

### Step 3. Bring material

Pick one:

**A. You already have a synopsis / treatment / draft scenes.**
Drop the files in — Claude reads and asks where you want to start.

**B. You have only an idea.**
Describe it in 1-2 paragraphs. Claude asks questions, helps you tighten the synopsis first, then the treatment, then the scenes.

**C. You have only a title and a genre.**
Fill in `templates/synopsis.template.md` and `templates/characters.template.md`. From there — iterative work.

### Step 4. Work scene by scene

Standard cycle:
1. You request a scene from the treatment.
2. Claude gives ONE version + an argument.
3. You give notes.
4. Claude makes a surgical edit.
5. When the scene is final — the `.md` Hollywood file is updated. (`.docx` only on explicit request, via `tools/build_screenplay.js`.)

---

## Legacy `.docx` exporters

Use **only** if you explicitly want a binary `.docx`. Default output is `.md`.

### Screenplay (Hollywood format)
```bash
cp tools/build_screenplay.js my_scene.js
# open my_scene.js, fill in the `screenplay` array via slug/action/character/dial helpers
NODE_PATH=/usr/local/lib/node_modules_global/lib/node_modules node my_scene.js
# you get screenplay.docx
```

### Bilingual (dialogue + translation)
```bash
cp tools/build_bilingual.js my_bilingual.js
# fill in via ...dialB("Main lang", "Translation")
node my_bilingual.js
# you get screenplay-bilingual.docx
```

### Treatment
```bash
cp tools/build_treatment.js my_treatment.js
# fill in via scene("Title", "Body", "[opt.] audit-tag")
node my_treatment.js
# you get treatment.docx
```

---

## Typical requests to the skill

| Request | What Claude does |
|---|---|
| "Write scene 5" | Reads the treatment → writes one version + an argument |
| "This isn't working" | Asks one narrow binary question → new version |
| "Make it bilingual" | Uses `markdown-style.md` Bilingual section (or `tools/build_bilingual.js` if you asked for `.docx`) |
| "Run a causality audit" | Walks through the treatment with ⚠ tags |
| "How many minutes will this be?" | Calculates by scene type (see `timing-and-cutting.md`) |
| "Cut it to X minutes" | Gives a concrete cut plan with numbers |
| "Make character Y's voice distinct from X's" | Compares lines, proposes changes |
| "Build me a story-asset registry" | Generates `story-assets.md` from `templates/story-assets.template.md` |

---

## Three things Claude does NOT do

1. **Doesn't write 5 versions** — gives ONE + an argument.
2. **Doesn't "improve" neighboring lines** — changes only what you asked for.
3. **Doesn't describe emotions** — only action verbs.

If Claude breaks one of these — say "One version, not five" or "Change only X."

---

## Personalizing the skill

If you write many films in the same genre — fork this skill and add:

- **`reference-films.md`** — list of reference films with scene breakdowns.
- **`my-style.md`** — your personal style preferences (e.g., "no flashbacks," "always end on silence").
- **`recurring-tropes.md`** — your recurring techniques.

The skill becomes yours, not generic.
