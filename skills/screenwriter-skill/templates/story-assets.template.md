# Story Assets — <Project title>

> Registry of **story** assets: characters, locations, prop mines, mythology, causality.
> This is **not** a visual registry (image refs / palettes / shotlists are a separate pipeline, outside this file).
> This file lives in the project folder alongside `synopsis.md`, `characters.md`, `worldbuilding.md`, the treatment, and the scenes.

---

## Controlling Idea

One sentence, McKee-form:

> Life becomes **X** when the hero does **Y**, because **Z**.

(If you can't put it in one sentence — the film has no spine.)

---

## Characters

One block per significant character.

### `<NAME>`

| Field | Content |
|---|---|
| **Role** | protagonist / antagonist / mentor / shadow / herald / threshold guardian / shape-shifter / trickster |
| **Want** (external goal) | what the character consciously pursues in the film |
| **Need** (internal truth) | what they actually need (often in conflict with Want) |
| **Hamartia** (fatal flaw) | a trait that in ordinary life is a virtue, in extraordinary life — a catastrophe |
| **Arc** | `+ → –` (tragic) / `– → +` (rising) / `flat` (catalyst for others) |
| **Voice** | line length, register, slang, patterns, forms of address to other characters |
| **Recurring tic / phrase** | repeating gesture, line, or anchor object |

#### Beats by act

- **Act 1** — what the character carries in, which inciting incident hits them
- **Act 2A** — first attempt, failure
- **Midpoint** — discovery / reversal
- **Act 2B** — deepening, crisis
- **Act 3** — climax choice, resolution

---

## Locations

One block per location with a **dramatic** function (not just a backdrop).

### `<LOCATION NAME>`

| Field | Content |
|---|---|
| **Dramatic role** | which value flips here (trust → betrayal, control → chaos, etc.) |
| **Symbolic association** | old life / limbo / trial / inheritance / grave |
| **Associated character(s)** | whose "territory" this is; who owns it |
| **Scenes** | list of scenes where it appears |
| **Echo / rhyme** | if first and last scenes rhyme — note that here |

---

## Props (Mines)

Objects that "fire" — Chekhov's rule. One block per object.

### `<OBJECT>`

| Field | Content |
|---|---|
| **Dramatic function** | Chekhov's gun / recurring motif / mirror / character anchor / key to a riddle |
| **Symbolic meaning** | what the object means for the hero / for the audience |
| **Setup** (first appearance) | scene N — what is shown, what function is hinted |
| **Reload** (second appearance) | scene M — function clarified / complicated |
| **Payoff** (the firing) | scene K — the object does what it was introduced for |
| **Anti-pattern** | if shown and never fired — that's a **failure**, remove or give a function |

---

## World Rules

### Hard rules (break = world falls apart)

- ...

### Soft rules (breakable, but at a cost)

- ...

### Tech / magic limits

- what **is possible** in this universe
- what **is impossible**
- what **is costly** (requires sacrifice)

### Social norms / power structures

- hierarchies, oaths, taboos

---

## Recurring Motifs

Repeating lines, images, actions that change meaning from one appearance to the next.

| Motif | Appearances | Meaning shift |
|---|---|---|
| `<line / image>` | sc. N, sc. M, sc. K | context 1 → context 2 → irony / tragedy |

---

## Causality Audit

Scene matrix. Each row answers: "this scene happened **because**...".

| Scene | Trigger (what set it off) | What it triggers next | Value: in → out | Tag |
|---|---|---|---|---|
| 1 | — (opening) | sc. 2 | control+ → control– | ✓ |
| 2 | sc. 1 (consequence of X) | sc. 3 | ... | ⚠ [causality] / ⚠ [value] / ⚠ [bible] / ⚠ [pace] |

Tag markers:

- ⚠ **[causality]** — scene doesn't follow from the previous (chronological, not causal)
- ⚠ **[value]** — scene doesn't move value, no +/–
- ⚠ **[bible]** — conflict with character / world bible
- ⚠ **[pace]** — too slow or too fast for its function

---

## Open Questions / Decisions Pending

Park unresolved decisions here: alternative endings, contested motifs, bible amendments still under discussion.

- ...
