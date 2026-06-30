# Examples

These are reference examples of the expected output quality and format. Do not copy
them verbatim; produce a fresh explanation for the actual word using `template.md`.

---

## Example A — User asks in Chinese, single word

**User:** 解释这个单词：campaign

**Assistant output (saved to `vocabulary-YYYYMMDD-HHMMSS/campaign.md`):**

```markdown
**campaign /kæmˈpeɪn/**

# 1. Meaning Summary
**Campaign** means a planned set of actions to reach a goal, like winning an
election, selling something, or helping people. It is used in both **daily talking**
and **formal talking**.
**Example:** The class started a **campaign** to keep the playground clean.

# 2. Word Building (The Pieces of the Word)
## Step 1: Camp = Camp
**(Type: Root)**
**(Origin: Latin "campus," meaning "field" or "open land")**
**Meaning of this piece**
**Camp** originally meant an open field. The core idea is a place where people
gather or work together.
**Related word example**
**Campus** = the land and buildings of a school.
**Literal meaning after combining**
**Camp** means "field" or "open place."

## Step 2: Camp + aign = Campaign
**(Type: Root + word ending)**
**(Origin: French "campagne," from Latin "campania," meaning "open country")**
...

# 4. Detailed Meanings & Examples
Meaning 1 — Noun (C): a planned set of actions to reach a goal.
- The students made a **campaign** to save water.
- Her **campaign** helped many animals.
...

# Summary
**Teacher's Tip:** Use **campaign** when people work together with a plan to win,
sell, help, or change something.
```

---

## Example B — Misspelled word

**User:** explain this word: compaign

**Assistant:** Gently notes the correct spelling is **campaign**, then explains
**campaign** using the full template, and saves to `campaign.md`.

---

## Example C — Multiple words

**User:** 解释这些单词：brave, gentle, curious

**Assistant:** Explains **brave** completely first (full template, saved to its own
file), then **gentle**, then **curious** — one fully finished before starting the next.

---

## Example D — File input, small, English only

**User:** 解释这个文件里的单词 words.txt  *(file has 8 English words)*

**Assistant:** Runs `scripts/count_words.py`, sees 8 words and no non-English content,
so proceeds directly. Creates `vocabulary-YYYYMMDD-HHMMSS/` and saves one md file per word.

---

## Example E — File input, large, with non-English content

**User:** 解释这个文件里的单词 lesson.md  *(file has 350 English words + Chinese notes)*

**Assistant:**
1. Runs `scripts/count_words.py`.
2. Warns: the file contains **350** unique words (over the 20-word threshold) AND
   contains non-English content (sample shown). Asks the user to confirm before continuing.
3. After confirmation, explains the words and saves results in batches of **200 words
   per file** (e.g. `batch-001.md`, `batch-002.md`) inside `vocabulary-YYYYMMDD-HHMMSS/`.
