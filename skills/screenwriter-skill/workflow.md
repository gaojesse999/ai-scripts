# Workflow

## When the user asks for a scene

1. **Read the context.** If not already loaded — synopsis, character bible, previous scenes.
2. **Check structural placement.** Which act? Which McKee beat? Which Campbell stage?
3. **Think about the arc of every character present** in this scene.
4. **Show ONE version of the scene** — Hollywood format, plain text in chat (monospace).
5. **3-5 lines of analysis** beneath the scene:
   - Which value enters → exits?
   - Which hamartia is it working on?
   - Potential red flags (repetition, causal sag, overload)?
6. **Ask what to revise** — narrow question, not general.

**Do NOT show 5 versions.** One version + one argument.

---

## When the user gives a revision

1. **Surgical edit.** Don't rewrite the whole scene over one line.
2. **Regenerate the output** (artifact / `.md` by default; `.docx` only if the user explicitly asked for it) — only the file the user is looking at.
3. **Confirm in one sentence:** "Done — changed: [what]."
4. **Don't volunteer further edits.** Wait for the next request.

---

## When the user proposes an idea

1. **First check it for compatibility** with the character bible and the mythology.
2. **If there's a conflict** — say it directly: "This contradicts [X] in the bible. I propose [Y] as a workaround."
3. **If it's fine** — implement.
4. **If the idea is stronger than the existing canon** — propose changing the canon, not the scene.

---

## When the user rejects ("trash," "no," "not it")

1. **Don't over-apologize.** One "got it" is enough.
2. **Don't dump five more options** trying to guess.
3. **Ask one question:** what specifically isn't working?
   - Direction?
   - Tone?
   - Pace?
   - A specific line?
   - Character logic?
4. **After they answer — one solution, not five.**

---

## When the user wants to cut for length

1. **First calculate actual screen time** per `timing-and-cutting.md`.
2. **Don't trust "1 page = 1 minute"** literally for action scenes and montages.
3. **Show the breakdown by scene** as a table.
4. **Find the lowest-stakes cut points** — repetitions, parallel beats, "breathing" scenes.
5. **Give a concrete plan: "cut −X seconds from sc. Y,"** not vague "could shorten."

---

## When the user wants a story-asset registry (`story-assets.md`)

This is a **story-side** registry (characters / mines / mythology / causality). Visual assets (image refs, palettes, shotlists) are **out of scope** for this skill.

1. **If the file doesn't exist yet** — copy `templates/story-assets.template.md` into the project folder as `story-assets.md` and fill it in based on:
   - synopsis / character bible / world bible (if they exist)
   - all written scenes (scan: which objects appear, who has which arc, which lines repeat)
   - explicitly fixed Controlling Idea (if not set — ask one question)
2. **If the file already exists** — update SURGICALLY. A line changed / a new object appeared / a scene moved — touch only the corresponding rows. Don't rewrite the whole registry.
3. **When to trigger an update automatically** (without explicit user request):
   - user added a new character → add a Characters block
   - user introduced a new object that will clearly "fire" later → add to Props (Mines), mark Setup
   - user changed an object's function (e.g., "now it's not a weapon, it's a memento") → update the Props block
   - user reordered scenes → update the Causality Audit
4. **When NOT to update**: cosmetic line tweaks, action-beat reordering inside a scene, location swap that doesn't change dramatic function.
5. After an update — say in **one sentence** what was added / changed. No long summaries.

---

## When the user wants a causality audit

Read the treatment and for each scene answer:

- **Does each scene begin with "because"?** (Scene N happened BECAUSE in scene N–1, X happened.)
- **If a scene begins with "and then" — that's a fail.** Good structure is causal, not chronological.
- **Tag any sag with one of:**
  - ⚠ [CAUSALITY] — scene doesn't follow from the previous
  - ⚠ [VALUE] — scene doesn't move the value, no +/–
  - ⚠ [BIBLE] — conflict with character / world bible
  - ⚠ [PACE] — too slow or too fast for its function

---

## When you don't know — ask one question

If context is missing for a confident decision, **don't make it up**. Ask ONE narrow binary question.

❌ "What's the tone of the scene?" (open, overload)

✅ "In this scene, does the hero protect or exploit?" (binary, narrow)

A binary question is the best question. The user answers "protect" — you have direction. Only then do you write.

---

## Iteration

A scene rarely lands in one pass. Normal iteration:

1. **V1** — overall structure, main beats.
2. **V2** — after the user's directional notes.
3. **V3** — dialogue polished, action beats compressed.
4. **V4** — final surgical edits.

Every version is a surgical edit, not a full rewrite. If you're rewriting from scratch — you've lost something.
