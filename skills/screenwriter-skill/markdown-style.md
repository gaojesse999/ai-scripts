# Markdown Hollywood style (default output)

Once a scene is locked in chat, the final version is saved into the project's `.md` file.
Markdown preserves the Hollywood-format skeleton without going to a binary `.docx`.

The `.docx` builders in `tools/` remain as **legacy** and are used only when the user explicitly asks for `.docx`.

---

## Hollywood ↔ Markdown mapping

| Hollywood element | Markdown |
|---|---|
| Slug-line (ALL CAPS bold, left margin) | `## N  INT./EXT. LOCATION — TIME OF DAY` (h2 with scene number) |
| Action (left margin, present tense) | plain paragraph, separated by blank lines |
| Character cue (ALL CAPS, indent ~2.2") | `### NAME` (h3) |
| Parenthetical (indent ~1.6", italic) | a line `(content)` or `（content）` placed under `###` |
| Dialogue (indent ~1") | plain paragraph under the parenthetical / character cue |
| Transition (right margin, ALL CAPS) | `**CUT TO:**` / `**HARD CUT:**` / `**硬切：**` on its own line |
| Match cut, fade out, etc. | same form — `**MATCH CUT:**`, `**FADE OUT.**` |

---

## Scene skeleton

```markdown
## 1  EXT. LOCATION — TIME OF DAY

Action. Verbs only.

Another action.

### HERO

(quietly)

Hero's line.

### SECOND

Second character's line.

**CUT TO:**
```

### Spacing rules

- Between any two screenplay "elements" — **one blank line**.
- Between `### NAME` and the line / parenthetical — a blank line is mandatory (otherwise the h3 visually eats the next paragraph).
- Do not use hard breaks (`<br>`) or HTML — only blank-line separators.

---

## Bilingual

A bilingual scene lays the dialogue out like this: the primary line on its own line, the translation directly below it in italic parentheses.

```markdown
### HERO

I'm going.

*（我走了）*
```

Action and slug-lines stay in a single language (chosen at the start of the project). Dialogue translation is the only bilingual block.

For Chinese-primary projects, swap the order — Chinese on top, English in italic parentheses below:

```markdown
### 主角

我走了。

*(I'm going.)*
```

---

## Treatment

A treatment is a list of scenes. Each scene: `## N  LOCATION — TIME OF DAY` + 3-5 sentences in a plain paragraph.

```markdown
## 1  EXT. LOCATION — TIME

Brief description of the scene: what enters, what changes, what exits. The scene's value and its causal link to the previous scene. 3-5 sentences max.

## 2  INT. ANOTHER LOCATION — LATER

...
```

---

## Notes

- The Hollywood "1 page ≈ 1 minute" rule **does not work** directly on `.md`. For screen-time estimates, always go back to `timing-and-cutting.md` and count by beats within the scene.
- When you make a surgical edit — touch **only** the block the user pointed at; don't "harmonize" the neighbors.
- Store all script versions inside the user's project folder. (No need to cross-link from here — this file is a tool of the skill, not material of the story.)
- If the user was working in `.docx` and asks to move to `.md` — convert once, then only edit the `.md`. The `.docx` stays as a backup.
