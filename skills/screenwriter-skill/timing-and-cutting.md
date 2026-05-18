# Screen-time math + cutting

The "1 page = 1 minute" rule is a starting hypothesis. Calibrate it for the type of scene.

---

## Scene types and their pacing

| Scene type | Pages → minutes | Why |
|---|---|---|
| **Static dialogue** (2 people, one location) | 1.0–1.2 | Reading speed ≈ playing speed |
| **Action / fight** | 0.6–0.8 | A scripted line "He hits, dodges, hits again" plays for 5+ seconds on screen |
| **Chase** | 0.4–0.6 | Edits, multiple angles, geographic transitions |
| **Montage** | 0.3–0.5 | Many separate shots condensed |
| **Silent / atmospheric scene** | 1.5–2.0 | A single line of action ("He looks at the rain") plays for half a minute |
| **Crowd scene** | 0.7–0.9 | Coverage, group reactions |

---

## Screen-time calculation algorithm

1. Open the treatment.
2. For each scene, classify it by type (above).
3. Apply the multiplier.
4. Sum.
5. Add ≈8% for credits (opening + closing).
6. Get a final number.

**Example:**
- 18 dialogue scenes × 2 pages × 1.1 = 39.6 minutes
- 4 action scenes × 1 page × 0.7 = 2.8 minutes
- 2 chase scenes × 0.5 page × 0.5 = 0.5 minutes
- 6 silent scenes × 0.5 page × 1.7 = 5.1 minutes
- Subtotal: 48 minutes
- + 8% credits: 51.8 minutes

---

## When the user asks "how many minutes will this be"

Show the breakdown as a table:

```
Scene 1 — int. apartment — dialogue       2pp × 1.1 = 2.2 min
Scene 2 — ext. street — action            1pp × 0.7 = 0.7 min
Scene 3 — int. car — silence              0.5pp × 1.8 = 0.9 min
...
TOTAL: 51.8 min (with credits)
```

---

## When the user asks to cut for length

### Algorithm

1. **Calculate the current screen time.**
2. **Get the target.** (Producer wants 90? Festival format 75? Pilot 50?)
3. **Find the cut delta.** (e.g., "current 105, need 90 → cut 15 minutes.")
4. **Find low-stakes cut points** in this order:

   - ✂ Scenes that don't move a value. (`⚠ [VALUE]` audits.)
   - ✂ Repeats. Two scenes do the same dramatic work — cut one.
   - ✂ "Breathing" scenes that are too long. Trim them down.
   - ✂ Pre-established information. If the audience already knows X, no need to repeat it.
   - ✂ Long monologues. Boil them down to action.
   - ✂ Internal montages and "passage of time" scenes. Replace with a slug-line transition.
   - ✂ Slow scene openings (the first 30 seconds of a scene are often skippable — cut into the middle).

5. **Give a concrete plan with numbers:**

   ```
   Target: 90 min. Current: 105. Delta: 15.

   sc. 7 — drop entirely (repeats sc. 5)        : −3 min
   sc. 12 — trim opening 40 sec                 : −0.7 min
   sc. 18 — replace monologue with object       : −2 min
   sc. 23-25 — fold three into two              : −4 min
   sc. 31 — drop establishing shots             : −1.3 min
   ...
   = −15 min ✓
   ```

---

## When the user is over-budget by very little (1-2 minutes)

Don't cut whole scenes. Trim **micro-pauses**:

- The first 5 seconds of every scene before the first action.
- Long pauses between lines.
- "Lookings" — characters looking at each other for 5 seconds. Cut to 2.

A film of 91 minutes can almost always be trimmed to 89 by tightening the cut, without losing a single scene.

---

## When the user is over-budget heavily (10+ minutes)

A subplot or a character must be cut. Painful, but unavoidable. Find the **lowest-stakes character** — one whose removal least affects the controlling idea — and propose them as the cut candidate. Show what scenes go with them.

---

## When the user is UNDER-budget

A film at 75 minutes when you need 90 is more dangerous than 105 when you need 90. The plot may be skeletal.

Diagnose:
- Are there enough **value reversals** (peripeteia)?
- Is the **hamartia visible** from the first scene?
- Are there enough **stakes** at midpoint?
- Is the climax loud enough?

Propose adding 1-2 reversals or expanding the climax — not just inserting "filler."

---

## Important reminder

A page-count number is always **approximate**. The real screen time is known only after the film is shot and edited. But for the screenwriter — a 5-10% accuracy is good enough to plan structure.
