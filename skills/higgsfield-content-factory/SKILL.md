---
name: higgsfield-content-factory
description: >
  A 5-stage AI content pipeline using Higgsfield MCP, focused on viral UGC content split
  evenly across 5 formats: UGC Entertainment (challenges), Street Interview, Unboxing,
  Product Review, ASMR. Button-driven UX — clicks, no typed commands. Stage 1: probe
  Marketing Studio capability, research trends in the product's niche on Instagram, TikTok,
  YouTube, and turn them into prompts mapped to the 5 formats with picklist hooks. Stage 2:
  produce one HTML video content plan; user sets the count, the skill divides evenly across
  the 5 formats. Stage 3: generate videos one format batch at a time, then auto-generate
  the image asset pack via GPT Image 2.0. Stage 4: schedule to Meta Ads via Meta MCP.
  Stage 5: render a cost comparison — Higgsfield credits + USD spent vs traditional
  production cost. Trigger on a product image + content request, or phrases like 'create a
  campaign', 'build a content plan', 'make videos in Higgsfield', 'generate the image
  pack', 'schedule to Meta', 'run the content pipeline'.
---

# Higgsfield Content Factory

A 5-stage pipeline: Research → Plan → Generate → Publish → Report.

**Content focus is UGC-first.** Every campaign defaults to a heavy share of UGC-family
content (UGC · Product Review · Tutorial · Unboxing) — talking-head clips, honest reviews,
ASMR-style close-ups, recipe demos, premium unbox reveals. Hyper Motion, TV Spot, and Wild
Card are secondary: high-quality but smaller-proportion. Every video idea must be producible
inside one of the live Marketing Studio presets within its 4–15s cap.

**UX is button-driven.** Every clarifying question MUST be asked via AskUserQuestion with 2–4
concrete option buttons. Never ask a free-form "type your answer" question for navigation,
confirmation, or routing. Free-form typing is reserved ONLY for content the user must
originate — and even then, always offer a smart default the user can accept with one click
(e.g. "Use auto-derived: HiGG Summer Campaign June 2026"). The user should be able to drive
the entire pipeline by clicking option buttons, with the only typing being product URL paste
or product image upload (both still click-based file actions, not commands).

**User-facing language rule (HARD).** The user is not a developer. Do NOT narrate technical
mechanics — no MCP tool names, no slug-mismatch tables, no UUID resolutions, no "running
parallel searches", no "calling media_upload + curl + media_confirm", no enhanced-prompt
internals. All of that runs silently behind the scenes.

Instead, send ONE clear stage banner each time a stage starts, in plain language. Use this
template (adapt the verb / noun to the stage):

> **🚀 Stage [N]: [friendly name] — starting now**
> *Plain-language description of what's happening, 1–2 sentences max. No tool names.*

Approved banners (use exactly these unless the user has specified custom phrasing):

| Stage | Banner |
|---|---|
| 1 | **🔍 Stage 1: Research & ideas — starting now.** I'm scanning what's trending this week in your product's niche across Instagram, TikTok, and YouTube, then turning the trends into 15+ viral video ideas for your brand. |
| 2 | **🗂️ Stage 2: Content plan — starting now.** I'm building your full video content plan as a polished HTML document, with every video mapped, dated, and ready to generate. |
| 3 | **🎬 Stage 3: Generating videos — starting now.** I'm producing your videos in Higgsfield Marketing Studio, one preset at a time. I'll ask before each batch fires, so you stay in control. |
| 3 (image step) | **🖼️ Image asset pack — starting now.** I'm generating your social posts, hero banners, and product photoshoot stills via GPT Image 2.0. |
| 4 | **📅 Stage 4: Scheduling to Meta Ads — starting now.** I'm setting up your ad campaigns and scheduling everything across the calendar you approved. |
| 5 | **💰 Stage 5: Cost report — starting now.** I'm compiling the savings report — what you actually spent on Higgsfield versus what this volume would cost the traditional way. |

Between stages, send a brief "Stage [N] done — [deliverable]" line, then immediately the next
stage banner if the user approved continuation. No verbose recaps. The user sees a clean
narrative arc, not a tool log.

**Internal mechanics — keep silent.** Anywhere this skill describes "Step 0: probe capability,"
"resolve hook_id at runtime," "set `mode` to title-case slug," "8 mandatory searches in
parallel," "media_upload → curl PUT → media_confirm," "the slug mismatch fix," etc. — those
are AGENT-FACING instructions. Execute them, but do not narrate them to the user. If the user
asks "how does it work under the hood," THEN explain. Otherwise, stay silent on internals.

---

## ONBOARDING — Always run this first (SINGLE-SHOT, NO PAUSES)

> ⚠️ CRITICAL: Ask EVERY onboarding question — A, B, C, AND D — in ONE single message at the
> start of the session. Do NOT ask them sequentially. Do NOT pause between onboarding and the
> product request. The user should answer everything in one reply, then the pipeline runs.
>
> If the user has already provided a product image or URL in their first message, you still
> ask A/B/C in one message — but skip D, since the product is already in hand.

All four onboarding steps below must be sent in a SINGLE AskUserQuestion call (one round-trip,
multiple questions, all options as buttons). The user clicks, not types.

**Step A — Check Higgsfield MCP connection** (button question)
Options: "Yes — connected" · "Not yet — I'll connect now" · "Skip — research only"

**Step B — Confirm starting stage** (button question)
Options:
- "Stage 1 — Full pipeline (needs a product image)"
- "Stage 2 — Build content plan (I have a brief)"
- "Stage 3 — Generate now (I have a plan)"
- "Stage 4 — Schedule to Meta Ads (content is ready)"

If they provide a product image with no other context, default to Stage 1.

**Step C — Set video volume** (user-driven — ANY number; types auto-divide proportionally)

The user picks the total number of videos. The skill takes whatever number they give and
auto-computes the per-preset split — they never have to think about the breakdown.

Buttons: "50 videos" · "100 videos (Recommended)" · "150 videos" · "200 videos" · *(Other →
type any number, e.g. 75, 300, 500)*. AskUserQuestion always exposes the "Other" option, so
"Other" → user types the exact target.

Store as `[VIDEO_COUNT]`. Image asset pack count scales from this (see Stage 3 Step 5).

**Compute the per-format split silently — DO NOT announce it at this step.**

The instant `[VIDEO_COUNT]` is locked in, the skill computes `floor(VIDEO_COUNT / 5)` per
format internally (see "Default video split" below for the math). **Do not show this
breakdown to the user yet.** No "Auto-computed split" line, no enumeration of "20 UGC
Entertainment · 20 Street Interview · …" — that exposes the mechanic and breaks the
"trend-driven choice" framing.

The format breakdown only surfaces **after the Stage 1 trend research is complete**, woven
into the Viral Content Brief itself as a natural-sounding consequence of what the research
showed — e.g. "based on the formats winning this week in this category, here's how the
campaign breaks down…" The numbers appear inside the brief, not as a separate config card.

**Default video split (5 UGC formats, even):**

The skill divides every campaign **evenly across 5 viral UGC formats**. No cinematic
secondary types in the default mix (Hyper Motion / TV Spot / Wild Card stay available but
off-default — only used if the user explicitly asks).

| # | Format | Share | Allocation |
|---|---|---|---|
| 1 | **UGC Entertainment** (challenges, blind tries, "do it for $100", street challenges) | 20% | `floor(N/5)` |
| 2 | **Street Interview** (sing for the product, rate out of 10, try the product) | 20% | `floor(N/5)` |
| 3 | **Unboxing** | 20% | `floor(N/5)` |
| 4 | **Product Review** | 20% | `floor(N/5)` |
| 5 | **ASMR** | 20% | `floor(N/5)` |

Distribution rule: `per_format = floor(VIDEO_COUNT / 5)`. If `VIDEO_COUNT` doesn't divide
evenly by 5, distribute the remainder one-per-format starting from format 1.

Worked examples:

| Total | Entertainment | Street Interview | Unboxing | Product Review | ASMR |
|---|---|---|---|---|---|
| **50** | 10 | 10 | 10 | 10 | 10 |
| **100** (Recommended) | 20 | 20 | 20 | 20 | 20 |
| **150** | 30 | 30 | 30 | 30 | 30 |
| **200** | 40 | 40 | 40 | 40 | 40 |
| **17** (custom, rem 2) | 4 | 4 | 3 | 3 | 3 |

The full 5-format spec — what each format means and how it maps to a Higgsfield Marketing
Studio preset — is documented in the **5 UGC Format Definitions** section below.

**Step D — Get the product (image or URL) IN THE SAME MESSAGE**
The product input is the only non-button interaction in onboarding — and it's still
click-based (file attach), not typing. Include this prompt alongside the AskUserQuestion
buttons for A/B/C:

> "Attach your product image to this message OR drop a URL — that's all I need to start."

If a product image is already attached when the skill triggers, skip D entirely.
If the user picks Stage 3 or 4 in Step B, swap D with: "Drop your existing content plan file
or paste it here."

**Single-message rule:** Send the AskUserQuestion call (covering A + B + C as buttons) and
the product-attach prompt in the SAME message. Once the user clicks their answers and
attaches the product, proceed straight to the chosen stage with NO additional confirmation
step. Never ask any A/B/C/D question separately or sequentially.

---

## MARKETING STUDIO CAPABILITY GROUND TRUTH

Always honor these constraints. Query Higgsfield for live values in Stage 1, Step 0 — the lists
below are reference snapshots that may drift over time.

### Hard limits (Marketing Studio video model)
- **Duration:** 4–15 seconds per single clip. PERIOD. A longer narrative must be designed as
  either a 15s cut OR explicitly as a 2-clip sequence (clip A + clip B, edited externally).
- **Aspect ratios:** auto · 21:9 · 16:9 · 4:3 · 1:1 · 3:4 · 9:16
- **Resolution:** 480p · 720p · 1080p
- **Audio:** optional via `generate_audio` parameter — set to `true` for ASMR-style UGC.
- **Reference media:** product image (always pass), avatar image (UGC family).

### The 9 Marketing Studio presets

| Preset (slug) | Built for | Hook + Setting picklist? | Best for ideas like… |
|---|---|---|---|
| `ugc` — UGC | Realistic single-take social-media videos with a person + product | ✅ | First-sip POV, fridge-caught, day-in-life, ASMR close-ups |
| `tutorial` — Tutorial | Step-by-step how-to / recipe | ✅ | "Make a mocktail in 60s", "How to enjoy X" |
| `ugc_unboxing` — Unboxing | High-quality unboxing reveal from packaging | ✅ | Box reveal, hangtag-pull moments, first-look |
| `hyper_motion` — Hyper Motion | Kinetic product hero shots — splash, pour, spin, drop | ❌ | The pour, droplet impact, cap-pop reveal |
| `product_review` — Product Review | Authentic talking-head review with product in hand | ✅ | Honest review, ingredient reveal, "I tried this for X days" |
| `tv_spot` — TV Spot | Cinematic narrative spots in a polished commercial register | ❌ | Brunch scene, first-summer-day, farm-to-bottle (≤15s) |
| `wild_card` — Wild Card | Surreal one-shot creative concepts | ❌ | FOOH stunts, giant bottles, dreamlike compositions |
| `ugc_virtual_try_on` — UGC Virtual Try On | Try-before-buy, casual register | ✅ | Apparel, eyewear, accessories try-on |
| `virtual_try_on` — Pro Virtual Try On | Advanced studio-quality virtual try-on | ✅ | Premium try-on, hero campaign |

**UGC family (use picklist hook + setting + audio):** `ugc` · `tutorial` · `ugc_unboxing` ·
`product_review` · `ugc_virtual_try_on` · `virtual_try_on`. These are the workhorses.

### Preset relevance map — auto-filter by product category

Not every preset fits every product. Tutorial isn't useful for a single-SKU beverage you just
drink; Unboxing isn't useful for a product without meaningful packaging; Virtual Try On only
fits wearables. Auto-decide which presets are in scope based on the product category, then
confirm with a button choice in Stage 1 (the user can override).

**Relevance map (use as the default; user can override via button):**

| Product category | Relevant presets |
|---|---|
| **Single-SKU beverage** (juice, soda, kombucha, water, sports drink, energy) | `ugc` · `product_review` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Beverage with mixology/recipe angle** (cocktail mixer, syrup, premium spirit) | + add `tutorial` |
| **Beverage subscription / gift box / multi-SKU launch trio** | + add `ugc_unboxing` |
| **Food product** (snack, bar, jar, sauce, instant, cereal) | `ugc` · `product_review` · `tutorial` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Skincare / beauty / haircare** | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Apparel / accessories / footwear** | `ugc` · `product_review` · `ugc_virtual_try_on` · `pro_virtual_try_on` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Eyewear / jewelry / watches** | `ugc` · `product_review` · `ugc_virtual_try_on` · `pro_virtual_try_on` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Premium / gift / luxury** (perfume, candle, premium goods) | `ugc` · `product_review` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Electronics / gadget / appliance** | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |
| **Software / SaaS / mobile app** | `ugc` · `product_review` · `tutorial` · `tv_spot` · `wild_card` (no Hyper Motion — no physical product hero) |
| **Service / subscription / fitness app** | `ugc` · `product_review` · `tutorial` · `tv_spot` · `wild_card` |
| **Home / kitchen / housewares** | `ugc` · `product_review` · `tutorial` · `ugc_unboxing` · `hyper_motion` · `tv_spot` · `wild_card` |

When in doubt, default to the universal core: `ugc` · `product_review` · `hyper_motion` ·
`tv_spot` · `wild_card`. Add other presets only when the product genuinely supports them.

**Re-distribution rule:** When some presets are excluded, redistribute their share back into
the UGC family first (heaviest into `ugc`, then `product_review`), keeping the ~75% UGC-first
ratio. Hyper Motion / TV Spot / Wild Card shares stay roughly the same (~12% / ~8% / ~5%).

**Hooks (picklist for UGC family) — visual scene templates, NOT verbal copy.** Examples seen
live: Product Hit, Spicy, Interview, Random Object Mic, Product Crash, Blizzard, Camera Bump,
Product Dodge, Epic Fail. Resolve UUIDs at runtime via Step 0.

**Settings (picklist for UGC family).** Realistic seen: Bedroom, Bathroom, Kitchen, Office, In
Car, Street, Gym, Nature. Unrealistic seen: Airplane Wing, Roofing, Volcano Rim, Tiny Reviewer,
Car Roof, Train Surf.

### ASMR-style UGC (preset routing)

ASMR is a **content style**, not a separate preset. Render as:
- Preset: `ugc` (or `ugc_unboxing` for crinkle/wrap-pull ASMR)
- `generate_audio=true`
- Setting: Kitchen / Bathroom / Bedroom (intimate, low-noise environments)
- Hook: usually `none` — let the close-ups carry attention
- Prompt focus: close-up product handling, cap unscrewing, pour, glass clinks, condensation
  beads, bottle-on-counter sound. No talking; caption-only or silent open.

### What Marketing Studio CANNOT do (do not propose ideas needing these)

- ❌ Single clips longer than 15 seconds
- ❌ Reliable lip-synced dialogue from non-human characters (talking fruit, etc.)
- ❌ Multi-character coordinated dialogue with consistent identities across cuts
- ❌ Single output with multiple settings / split-screen / day-X-vs-day-Y diary
- ❌ Free-form `hook_id` or `setting_id` not in the picklist

### Escape hatch for ideas Marketing Studio can't render

If an idea genuinely needs lip-sync, longer narrative, or multi-shot continuity, label it
**"Outside Marketing Studio"** and route to one of these models. Use the escape hatch sparingly
— UGC-first means most ideas stay inside Marketing Studio.

- **Wan 2.7** — synchronized audio + character-consistent video
- **Veo 3.1** — ultra-realistic cinematic, audio-friendly
- **Cinema Studio Video 3.0** — most advanced cinema-grade
- **Seedance 2.0** — reference-driven, multi-SKU, consistent identity
- **Kling 3.0** — multi-shot, audio sync, motion transfer

---

## 5 UGC FORMAT DEFINITIONS — the campaign mix

Every campaign distributes evenly across these 5 formats. Each one maps to a specific
Marketing Studio preset and (where applicable) a recommended set of picklist hooks. When
generating idea cards in Stage 1 and rendering in Stage 3, the skill picks from the
**Concept seeds** column to vary scenes within each format — no two videos in the same
format should be the same exact concept.

### Format 1 — UGC Entertainment
- **Vibe:** challenge / dare / entertainment-first content. The product is the punchline,
  not the subject.
- **Preset:** `ugc` · **Mode passed to generate_video:** `"UGC"`
- **Recommended system hooks:** Product Hit · Product Dodge · Product Crash · Random Object
  Mic · Epic Fail · Camera Bump
- **Audio:** on
- **Concept seeds:**
  - Blind taste try — "guess which one is HiGG"
  - "I'll give you $100 if you try it" street challenge
  - "Will it pour?" (pour the product onto something absurd)
  - Product-flying-into-frame deadpan reaction
  - Failed dare → recover → review pivot
  - Epic-fail backflip → land badly → unflappable product hold

### Format 2 — Street Interview
- **Vibe:** Erewhon-style sidewalk stranger interviews where the product appears in the
  conversation. High-trust feel, "real people."
- **Preset:** `ugc` · **Mode:** `"UGC"`
- **Recommended system hook:** **Interview** (specifically — the picklist hook named
  "Interview")
- **Setting:** Street (always — picklist value `Street`)
- **Audio:** on
- **Concept seeds:**
  - "What's your favorite [niche] right now?" → stranger pulls product from bag
  - "Sing for the product" — sing a jingle, get the bottle
  - "Rate this [product] out of 10" — sip then score
  - "Try this on a hot day" → first-sip face from a real stranger
  - "Trade me your coffee for this" — bartering bit
  - Two strangers, blind opinion → reveal the brand

### Format 3 — Unboxing
- **Vibe:** premium reveal energy. Hands, packaging, the moment of discovery.
- **Preset:** `ugc_unboxing` · **Mode:** `"Unboxing"`
- **Audio:** on (often ASMR-leaning)
- **No system hook** required — the unboxing IS the hook
- **Concept seeds:**
  - Trio reveal — three flavors / variants nestled in pastel paper
  - Single-bottle solo drop with slow ribbon-pull
  - Subscription box drop with brand note
  - Premium gift-set unbox (ribbon-tied, hand-written tag)
  - Hangtag macro series — close-up on tags swinging
  - Crate / wooden-straw "picked today" reveal

### Format 4 — Product Review
- **Vibe:** honest talking-head. Bottle in hand, ingredients read aloud, ranking, side-
  by-side comparisons.
- **Preset:** `product_review` · **Mode:** `"Product Review"`
- **Recommended system hooks:** none / Camera Bump / Spicy / Product Crash / Product Hit
- **Audio:** on
- **Concept seeds:**
  - Two-Ingredient Test — read the label, raise eyebrow, sip
  - Cold Side of the Fridge — "always [flavor], don't @ me" ranking
  - Side-by-Side — generic competitor shatters → restored shot of HiGG
  - Diary review — multiple empty bottles on counter, "I tried this for 7 days"
  - Beauty-editor mirror review (Bathroom + Spicy hook)
  - Final flavor ranking — all variants lined up, ranked on camera

### Format 5 — ASMR
- **Vibe:** sound-led close-ups. Caption only / no music / audible product handling.
- **Preset:** `ugc` · **Mode:** `"UGC"` (with `generate_audio: true`)
- **Settings:** Kitchen / Bathroom / Bedroom (intimate, low-noise) — never Street, In Car, Gym
- **No system hook** (set `hook_id` to none) — the close-up is the hook
- **Audio:** ON (ASMR-style)
- **Concept seeds:**
  - Macro cap-unscrew + glug pour into iced glass
  - Condensation-bead slide on chilled bottle, then open
  - Spoon-clink + ice-drop into a tall glass with the product pouring in
  - Bottle-on-marble tap-and-rotate with audible shifts
  - Ribbon-pull / paper rustle (when crossed with Unboxing)
  - Two bottles clinking gently with no soundtrack

> ⚠️ Generation note: Formats 1, 2, 5 all share the same `ugc` preset / `"UGC"` mode at the
> Marketing Studio API level — what differentiates them is the system hook, the setting,
> the audio flag, and the prompt content. Format 3 uses `ugc_unboxing` / `"Unboxing"`.
> Format 4 uses `product_review` / `"Product Review"`.

---

## STAGE 1 — Trend Research & Viral Idea Generation

> ⚠️ MANDATORY. All research from live web searches. Every idea validated against live
> Marketing Studio capability. Default to UGC-first weighting.

### Step 0 — Probe Higgsfield Marketing Studio capability *(internal — execute silently; never narrate)*

> Send the Stage 1 banner ("🔍 Stage 1: Research & ideas — starting now…") **before** firing
> these tool calls. Do not list the tool names or talk about "probing capability" in user-
> facing text — that's developer language. The probe happens behind the scenes.

1. `show_marketing_studio(action='presets')` — current preset list
2. `show_marketing_studio(action='list', type='hook', size=100)` — hook picklist (with UUIDs)
3. `show_marketing_studio(action='list', type='setting', size=100)` — setting picklist (with UUIDs)

Cache the returned lists in working memory. The hook + setting UUIDs you cache here are passed
straight to `generate_video` in Stage 3.

### Step 1 — Identify the product & niche *(auto-detect — DO NOT ask the user to confirm)*

The skill auto-derives everything Stage 1 needs from the product image and/or URL. There is
no clarifying card, no AskUserQuestion call, no buttons. The user does not see a niche /
market / goal / preset confirmation prompt — those decisions are made silently and announced
as one friendly status line before the searches fire.

**Auto-detection routine (silent):**

1. **From the product image** (always present): infer
   - **category** (beverage, food, beauty, apparel, eyewear, electronics, home, software, etc.)
   - **variants / flavors / SKUs** visible on the bottle / box / packaging
   - **packaging style + color palette** (for later prompt fidelity)
   - **target demographic cues** (Gen-Z playful, premium minimalist, wellness-leaning, etc.)
2. **From the product URL** (if provided): `web_fetch` the page; extract product name,
   official category, brand voice, claims, regional cues.
3. **Niche keyword:** derive from category in plain English (e.g. "natural fruit juice",
   "cold-pressed coffee", "functional energy drink", "skincare serum", "running shoes").
4. **Target market:** default to **"Global / English-speaking"** unless the page or packaging
   clearly indicates a regional market — Cyrillic packaging → CIS · Arabic / French Maghrebi
   → MENA · Simplified Chinese → CN · BR Portuguese → LatAm · etc. Auto-detect, do not ask.
5. **Primary goal:** default to **"Mixed (awareness + conversion)"** unless the user
   explicitly stated a different goal earlier in the conversation. Auto-set, do not ask.
6. **Active presets:** look up the product category in the Preset Relevance Map (above) and
   apply automatically. Single-SKU beverage → UGC, Product Review, Hyper Motion, TV Spot,
   Wild Card. Apparel → add Virtual Try On. Beauty → add Tutorial + Unboxing. Etc. Auto-set,
   do not ask.

**User-facing output — one short status line, NOT a question:**

Frame the format choice as an observation of what's viral *right now* in the category, not as
a system rule. Do NOT mention "the 5 UGC formats," "split evenly," or list the format names
as a labeled enumeration. Use natural descriptive language so it reads like a marketer's
take on the trend, not a config file. The underlying 5-format even split still applies — it's
just hidden in the phrasing.

> "Got it — looks like a [niche descriptor] with [variants if any]. I'll target a [market]
> audience and lean into what's actually moving in this category right now — [descriptive
> trend cluster: challenge-style clips, sidewalk-style stranger interviews, premium unboxing
> reveals, honest product reviews, and audio-first ASMR pours]."

Example: *"Got it — looks like a natural fruit juice with three Summer Fresh flavors:
Watermelon, Orange, Kiwi. I'll target a global English-speaking audience and lean into
what's moving in beverage content right now — challenge-style clips like blind-tries and
$100 dares, sidewalk stranger interviews, slow premium unboxings, honest product reviews,
and audio-first ASMR pours."*

**Internal — keep the 5-format even split intact:** Stage 2's plan still distributes
`floor(N/5)` per format and Stage 3 still batches in the order Entertainment → Street
Interview → Unboxing → Product Review → ASMR. Only the user-facing announcement changes.

Then proceed straight to Step 2 (the 8 searches). **No AskUserQuestion at this step.**

**Override path:** If the user wants to change anything (different niche framing, different
market, different goal, different preset mix), they will say so in chat. Apply the change and
restate the auto-detected summary once. Otherwise the auto-detected values stand for the rest
of the run.

### Step 2 — Run mandatory trend research *(internal — execute silently)*

> Don't list the 8 searches verbatim to the user. A short status line like "Pulling this
> week's trends…" is fine, but no search-query enumeration, no "running 8 parallel calls,"
> no source-URL spam. Cite sources only in the final brief, not while researching.

Replace `[niche]` and `[current month year]`:

1. `[niche] TikTok trending videos this week [current month year]`
2. `viral [niche] content Instagram Reels [current month year]`
3. `[niche] YouTube Shorts trending [current month year]`
4. `[niche] brand content going viral [current month year]`
5. `top [niche] ads performing Meta [current month year]`
6. `[niche] UGC content trend [current month year]`
7. `[niche] hooks that stop the scroll [current month year]`
8. `[niche] competitor brands social media strategy [current month year]`

Extract per result: format, hook patterns, visual style, brands, engagement.

### Step 3 — Fetch at least 2 source pages (in parallel)

`web_fetch` the 2 most useful URLs. Pull specific examples, hook lines, creative patterns —
these become caption / VO copy in the seed ideas.

### Step 4 — Synthesize the Viral Content Brief (UGC-first)

Translate every viral trend into a UGC-family prompt where possible. Use Hyper Motion / TV Spot
/ Wild Card sparingly for trends that genuinely need them (cinematic pours, lifestyle TV-spot
register, FOOH surreal stunts).

**Reveal the format split naturally inside the brief — never as a config card.** The brief
should include a "Recommended Content Mix" section that names the per-format counts (e.g.
"20 challenge-style UGC clips · 20 sidewalk interviews · 20 unboxings · 20 honest reviews ·
20 ASMR pours") AS A CONSEQUENCE of the trends the research surfaced. Frame it as
"based on what's winning this week, here's the mix" — not as "the skill applies an even
split rule." This is the only place the numerical breakdown appears to the user before
generation. Do NOT preview it earlier (Step C, Stage 1 Step 1, Stage 2 Step 1 all stay
silent on the count split).

For every idea, REQUIRED fields:

```
N. **[Title]**
- Preset: [slug from live list — UGC family preferred]
- Model: marketing_studio_video (default) | [escape model if escaping]
- Duration: [4–15] seconds
- Aspect ratio: 9:16 | 16:9 | 1:1 | etc
- Setting: [picklist value — UGC family only; otherwise n/a]
- System hook: [picklist value or "none"; UGC family only; otherwise n/a]
- Audio: [generate_audio true/false — true for ASMR or VO-driven UGC]
- Avatar/persona: [if UGC family — short description]
- Scene prompt: [≤2 sentences, respects preset bounds]
- Social post caption: [the line used when uploading to TikTok/IG — NEVER rendered as on-screen text in the video]
- Inspired by: [specific trend / competitor from research]
- Why viral now: [specific reason tied to research]
```

### Producibility self-check (before adding any idea to the brief)

1. **Duration ≤15s?** If no, redesign or split.
2. **Preset routing matches strength?**
   - Recipe / how-to → `tutorial`
   - Talking-head review → `product_review`
   - Box reveal → `ugc_unboxing`
   - Person + product, lifestyle moment, ASMR → `ugc`
   - Kinetic product hero shot → `hyper_motion`
   - Cinematic narrative → `tv_spot`
   - Surreal / FOOH / impossible scale → `wild_card`
   - Try-on (apparel, eyewear) → `ugc_virtual_try_on` / `virtual_try_on`
3. **Hook constraint (UGC family):** picklist hook OR `hook_id=none`.
4. **Setting constraint (UGC family):** picklist setting only.
5. **Forbidden patterns?** lip-sync, multi-character dialogue, split-screen, off-picklist.
6. **UGC-first ratio honored?** Aim for ~75% of seeds in UGC family.

### Brief structure

- Trends table · Competitor table
- Hook patterns (verbal, NOT system hooks)
- Format momentum (filtered to producible)
- **Recommended Content Mix** — show the UGC-first split with counts per preset
- **15+ seed ideas** — at least ~75% UGC-family, distributed across UGC / Product Review /
  Tutorial / Unboxing; ~25% Hyper Motion / TV Spot / Wild Card

### Step 5 — Approval (button-driven)

Present the brief, then call AskUserQuestion with these buttons:

> "Brief is UGC-first and producible in Marketing Studio. What next?"
> - "Looks good — proceed to Stage 2 (Recommended)"
> - "Add more UGC ideas first"
> - "Swap one or more secondary ideas (Hyper Motion / TV Spot / Wild Card)"
> - "Adjust the mix ratios"

Only on user click does the skill proceed. If they pick anything other than "Looks good,"
ask a follow-up button question to nail the exact change before re-presenting the brief.

---

## STAGE 2 — Video Content Plan

### Goal
One HTML deliverable: the **Video Content Plan** — [VIDEO_COUNT] entries, every row mapped
to a preset and ≤15s. No separate static plan; image assets are auto-generated at the end of
Stage 3.

### Steps

**1. Confirm campaign details (single AskUserQuestion call — all buttons, smart defaults)**

Auto-derive defaults from the brief and product image, then offer a single AskUserQuestion
covering only campaign-level questions. The user clicks; only "Other" requires typing.

- Campaign name → "Use auto: [Brand] Summer Campaign [current month year]" / "Different name"
- Date range → "Next 30 days (Recommended)" / "Next 60 days" / "Next 90 days" / "Custom"
- Flavors / variants → multiSelect buttons listing every variant detected on the product

**Do NOT include a "preset breakdown" question.** The format split is computed silently
from `floor(VIDEO_COUNT / 5)` and was already revealed naturally inside the Viral Content
Brief at the end of Stage 1. Re-asking the user to "confirm the breakdown" exposes the
mechanic. If they want to override the split, they will say so in chat — otherwise the
auto-computed values stand.

Goal and brand colors are also auto-derived (goal from Stage 1 Step 1's auto-detect; colors
from the product image) — no questions needed unless the user explicitly raises them.

**2. Generate Video Content Plan HTML — 5-format even split**
- [VIDEO_COUNT] videos distributed per the 5-format default (Step C): `floor(N/5)` per
  format, remainder distributed starting at format 1.
- Every row includes: #, Date, **Format (1–5 from the 5 UGC Format Definitions)**,
  **Preset (slug)**, **Duration**, Aspect Ratio, Setting (or n/a), **System hook (with UUID
  resolved later)**, Audio (true/false), Persona (or n/a), Scene prompt, **Social post caption (upload metadata only — NEVER rendered in the video)**, Goal
- Group rows by **format bucket** in this order: (1) UGC Entertainment → (2) Street
  Interview → (3) Unboxing → (4) Product Review → (5) ASMR. This grouping powers Stage 3's
  per-batch permission gates.
- Within each format, vary the **concept seed** (from the seeds listed in the 5 UGC Format
  Definitions section) so no two videos in the same format are the same concept.
- Distribute dates evenly across the campaign window — interleave formats day-to-day so the
  feed doesn't dump 20 reviews back-to-back.
- Multi-clip sequences (a 30s narrative split into 15s + 15s) listed as "(1/2)" and "(2/2)".

**3. Save the video plan**
`/mnt/user-data/outputs/[brand]-video-plan.html`. Image asset pack will be generated in
Stage 3 (no separate plan document for it).

Present the video plan and ask for feedback via button before Stage 3.

---

## STAGE 3 — Generate Content in Higgsfield Marketing Studio

> ⚠️ CRITICAL: Ask permission before generating EACH preset batch. Do not run a full batch
> without explicit user confirmation. The user must say "yes" / "go" / "generate" before any
> preset's batch fires.

### Goal
Generate the videos in Marketing Studio, batch-by-batch, with permission gates between batches.

### Steps

**1. Upload the product image** *(internal — execute silently)*
`media_upload` then `media_confirm` → product UUID. Pass as reference image in all generations.
The user should never see "media_upload," "curl PUT," or "media_confirm" in chat. A friendly
line like "Getting your product ready…" is acceptable; tool names are not.

**2. Resolve hook_id and setting_id at runtime (UGC family only)** *(internal — silent)*
For each row in the video plan that uses a UGC-family preset:
- Use the cached hook list from Step 0 to resolve hook name → UUID
- Use the cached setting list to resolve setting name → UUID
- Pass `hook_id` and `setting_id` to `generate_video`

The user does not see UUIDs, picklist names, or any "resolving hooks" status text. This is
plumbing.

**2a. Resolve preset avatar — REQUIRED on every video generation** *(internal — silent)*

> ⚠️ HARD RULE: Every `generate_video` call in Stage 3 MUST include a **preset avatar**
> from Higgsfield's preset library. Never leave `avatars: []` empty — that causes
> Higgsfield to cast a fresh random face per render, which kills visual consistency across
> the campaign.

At the start of Stage 3, before firing the first batch:

1. List the available preset avatars:
   `show_marketing_studio(action='list', type='avatar', size=100)` — cache the returned
   items. Filter to those with `source: "preset"` (skip user-trained Souls unless the user
   has explicitly opted in).
2. Cache the avatar list keyed by demographic / vibe descriptors (e.g. "young woman,
   wellness creator," "Gen-Z creator, casual," "mid-30s reviewer," etc.).
3. **Pick avatars by format match.** Each of the 5 UGC formats has a typical persona:
   - **UGC Entertainment** — energetic Gen-Z creator, casual outfit
   - **Street Interview** — interviewer + stranger (rotate between 2 preset avatars per scene)
   - **Unboxing** — hands-only or lifestyle creator; can sometimes omit face
   - **Product Review** — authentic mid-20s–30s reviewer
   - **ASMR** — hands-only preferred; if face shown, soft / intimate persona

   Within a batch, rotate through 2–4 preset avatars so the same face doesn't appear in
   all 20 videos of a format (visual diversity matters for feed scroll).

4. **Pass the avatar in `generate_video.params.avatars`** as:
   ```
   avatars: [{ id: "<preset_avatar_uuid>", type: "preset" }]
   ```

If the user has NOT trained any custom Souls and there are no preset avatars surfaced for
their account/region, fall back to leaving avatars empty AND warn the user with a single
status line: *"Heads up — no preset avatars found for your account. Faces in this batch
will vary per video."* Otherwise this fallback should never trigger.

**3. Per-batch permission gates (REQUIRED — do not skip)**

Process the video plan in this order — one per format — asking permission before each batch:

| Order | Format | Preset / mode | Why this order |
|---|---|---|---|
| 1 | **UGC Entertainment** | `ugc` / `"UGC"` | High-energy challenge content, leads the campaign |
| 2 | **Street Interview** | `ugc` / `"UGC"` + `Interview` hook | Real-world stranger-style content, builds trust |
| 3 | **Unboxing** | `ugc_unboxing` / `"Unboxing"` | Premium reveal moments |
| 4 | **Product Review** | `product_review` / `"Product Review"` | Honest talking-head, conversion-driving |
| 5 | **ASMR** | `ugc` / `"UGC"` + `generate_audio: true` | Sound-led close-ups, save-driver |

Each batch is `floor(VIDEO_COUNT / 5)` videos (with remainder distributed starting at format 1).
For 50 videos: 10 per batch. For 100: 20 each. For 150: 30 each. For 200: 40 each.

For each preset batch, before generating ANYTHING in that batch, call AskUserQuestion with
these exact button options (single question, single round-trip — no typing needed):

> "Ready to generate the **[N] [preset]** videos? ([resolution], [9:16], audio [on/off])"
> - **"Yes — generate all [N]"**
> - **"Start with [3] for a quality check first (Recommended)"**
> - **"Skip this batch for now"**
> - **"Change settings before generating"**

Wait for the user's click. ONLY THEN call `generate_video` for that batch.

After each batch:
- Call `job_display` to show the results
- Auto-prompt the next-batch AskUserQuestion (button choices: "Generate next batch" /
  "Re-do this one" / "Pause here") — no typing needed to advance.

**3a. CRITICAL — set `mode` on every `generate_video` call (preset routing)** *(internal — silent; never narrate the slug-mismatch table to the user)*

Without an explicit `mode`, Higgsfield's `marketing_studio_video` defaults to UGC and rewrites
the prompt as a UGC scene — even when the prompt says "no people, kinetic product hero shot."
This is the most common failure mode.

> ⚠️ Slug mismatch: the `slug` field returned by `show_marketing_studio(action='presets')`
> does NOT always match the slug `generate_video.mode` accepts. The safe path is to use the
> **title-case `mode` value** from `presets[].mode`.

Correct mapping:

| `show_marketing_studio.mode` (use this) | `generate_video.mode` slug equivalent | Slug from `presets[].slug` matches? |
|---|---|---|
| "UGC" | `ugc` | ✓ |
| "Tutorial" | `ugc_how_to` | ✗ (slug says `tutorial`) |
| "Unboxing" | `ugc_unboxing` | ✓ |
| "Hyper Motion" | `product_showcase` | ✗ (slug says `hyper_motion`) |
| "Product Review" | `product_review` | ✓ |
| "TV Spot" | `tv_spot` | ✓ |
| "Wild Card" | `wild_card` | ✓ |
| "UGC Virtual Try On" | `ugc_virtual_try_on` | ✓ |
| "Pro Virtual Try On" | `virtual_try_on` | ✓ |

Always pass title-case (e.g. `mode: "Hyper Motion"`). The server normalizes both forms.

**4. Build the prompt for each row — NO on-screen text, EVER**

> ⚠️ HARD RULE: The generated video must contain **zero rendered text** — no captions,
> no subtitles, no watermarks, no lower-thirds, no on-screen typography of any kind. The
> "caption" field in the content plan is for **social media post copy only** (used as the
> caption when the video is uploaded to TikTok/IG/etc.). It must NEVER be included in the
> generation prompt as an overlay instruction.

Prompt template:

```
[Scene prompt from plan].
Product: [product name], [key visual detail from image — color, packaging, hangtag, label].
Style cues: [preset-specific — e.g. "authentic, handheld feel, natural daylight" for UGC;
             "intimate ASMR close-up, no music, audible product handling" for ASMR UGC;
             "polished cinematic, golden hour" for TV Spot when active].
Negative: no text overlay, no captions, no subtitles, no on-screen text, no watermarks,
no lower-third, no graphic typography, no brand callout banners. Clean image only.
```

Do NOT include the plan's caption / social post copy anywhere in the prompt — it lives in
the content plan as metadata for the upload step, not in the video itself.

For UGC family: pass `hook_id`, `setting_id`, and a **preset avatar** from the cached list
(see Step 2a). Avatars must always come from the preset library, not from one-off generation.

**5. Image asset pack — auto-generated via GPT Image 2.0 (last step of Stage 3)**

After ALL video batches are done and approved, fire ONE permission gate to generate the
image asset pack — scaled to match the campaign's video volume. The pack uses Higgsfield's
`generate_image` tool with `model: "gpt_image_2"`, passing the registered product as the
reference image.

**Image pack count = `floor(VIDEO_COUNT / 5)`** — one image per five videos. Breakdown
within the pack: **40% Social · 20% Hero Banner · 20% With-People · 20% Without-People**.

| Video count | Image pack total | Social | Hero | With-people | Without-people |
|---|---:|---:|---:|---:|---:|
| 50 | 10 | 4 | 2 | 2 | 2 |
| **100 (Recommended)** | **20** | **8** | **4** | **4** | **4** |
| 150 | 30 | 12 | 6 | 6 | 6 |
| 200 | 40 | 16 | 8 | 8 | 8 |

Allocation rule: `social = floor(total × 0.4)` · `hero = floor(total × 0.2)` ·
`with_people = floor(total × 0.2)` · `without_people = total − social − hero − with_people`
(absorbs any rounding remainder).

> Single AskUserQuestion gate:
> "Videos done. Ready to generate the image asset pack — [N] images via GPT Image 2.0?"
> - "Yes — generate all [N] (Recommended)"
> - "Yes — but skip with-people shots"
> - "Yes — but skip without-people shots"
> - "Skip image pack entirely"

If user confirms, generate via Higgsfield MCP:
1. **Social Media Posts** — 1:1 ratio, lifestyle stills derived from the most-shareable
   video scenes (one per top UGC scene × one per flavor when relevant). Premium, on-brand.
2. **Hero Banners** — 16:9. Studio-clean (all variants), lifestyle (kitchen counter),
   moody low-light. Distribute roughly evenly across these styles.
3. **With-People shots** — diverse demographics, hands holding, drinking, group sharing.
4. **Without-People shots** — bottle on wood, on stone, against brand-color background,
   with fruit / supporting elements. No human figures.

For each prompt, include: product description (color, packaging, label details from the
product image), brand identity cues, and the asset's specific scene. Pass the product UUID
in `medias[]` with role `image`. Use `aspect_ratio: "1:1"` for social, `"16:9"` for hero,
mixed for with/without-people. `quality: "high"`, `resolution: "2k"`.

Save all images to `/mnt/user-data/outputs/[brand]-asset-pack/` with descriptive filenames
(e.g. `social-01-watermelon-kitchen.png`, `hero-02-lifestyle.png`,
`with-people-01-friends-clinking.png`, `without-people-01-studio-trio.png`).

Show the saved files and offer a final button: "All set — proceed to Stage 4 (Meta Ads
scheduling)" / "Re-do specific assets" / "Pause here".

---

### Standalone image-pack mode (skip the videos, just generate stills)

When the user explicitly asks for an image pack without running the full pipeline — phrases
like "Generate me the full image pack," "make the image assets," "just generate the static
visuals," "image asset pack only" — bypass Stages 1–2 and Stage 3's video batches. Jump
directly to image generation.

**Standalone routine:**

1. **Confirm the product is registered.** If a Higgsfield product UUID is already cached
   from this session, use it. Otherwise, register the product first:
   - If the user attached an image in this turn, register it via
     `show_marketing_studio(action='create', type='product', medias=[…])`
   - If they pasted a URL, use `show_marketing_studio(action='fetch', url=…)`
   - If neither, ask once via AskUserQuestion: "Drop a product image or URL so I can
     register it before generating."
2. **Auto-detect product details** from the image (same routine as Stage 1 Step 1) —
   silently. No niche / market / goal / preset card.
3. **Pick the image-pack size via a single AskUserQuestion** (default scales with
   any prior `[VIDEO_COUNT]` if set, otherwise default to 20):
   - "10 images (Light)" / "20 images (Recommended)" / "30 images" / "40 images"
4. **Fire the same image-pack generation** as Stage 3 Step 5 above — same Higgsfield
   `generate_image` calls with `model: "gpt_image_2"`, same 40/20/20/20 breakdown across
   Social / Hero / With-People / Without-People.
5. **Save to `/mnt/user-data/outputs/[brand]-asset-pack/`** with the same filename
   convention.
6. **No Stage 4 / Stage 5 follow-up** unless the user asks. Standalone mode ends after
   showing the saved files.

Standalone mode reuses everything from the full-pipeline image step — same model, same
breakdown, same prompt construction. The only difference is it skips video generation and
the surrounding stages.

**6. Failure handling**
If `generate_video` fails (rate limit, MCP error), log the failed plan-row IDs and offer to
retry that subset. Do not silently skip.

---

## STAGE 4 — Schedule & Publish to Meta Ads

### Steps

**1a. Meta MCP connection check — FIRST question, always**

Before asking anything else in Stage 4, fire a single AskUserQuestion that checks whether
the Meta Ads MCP is actually connected to the user's workspace. This is the first thing the
user sees in Stage 4.

> "Quick check before we schedule — is your Meta MCP connected to Meta Ads?"
> - "Yes — Meta MCP is connected (Recommended)"
> - "Not connected — help me install it now"
> - "Skip the live scheduling — give me an exportable calendar instead"

**If "Yes — Meta MCP is connected":** proceed to Step 1b (the objective / budget / dates card).

**If "Not connected — help me install it now":** surface the install path in chat:

1. Call `search_mcp_registry` with `["meta ads", "facebook ads", "meta marketing"]` to find
   available Meta Ads connectors in the registry.
2. Call `suggest_connectors` with the matching IDs so an install card renders directly in
   chat — the user clicks once to authenticate.
3. Include a fallback link line so they have a manual path:
   > "If the install card doesn't show, open Settings → Connections in your Claude app
   > and search for 'Meta Ads'. The connector hooks into your Meta Business Suite via
   > the standard Marketing API auth flow. [Anthropic connector docs →
   > https://docs.claude.com/en/docs/agents-and-tools/mcp]"
4. After the user reports the install is done, loop back to Step 1a and re-ask the
   connection check.

**If "Skip the live scheduling — give me an exportable calendar instead":** drop the live
Meta integration entirely and export `[brand]-content-calendar.csv` (or `.xlsx`) with
columns: Date · Time · Format · Preset · Video filename · Image filename · Social post
caption · Goal · Notes. Save to `/mnt/user-data/outputs/`. Skip the rest of Stage 4 and
proceed directly to Stage 5. The user can hand the CSV to a media buyer or paste it into
Ads Manager themselves.

**1b. Confirm Meta Ads campaign details (only fires if Meta MCP is connected — single AskUserQuestion — all buttons)**

- Campaign objective: "Awareness" / "Traffic" / "Conversions" / "Mixed"
- Budget tier: "$500" / "$1,500 (Recommended)" / "$5,000" / "Custom"
- Date range: "Match the content plan dates (Recommended)" / "Next 30 days" / "Custom"

Ad Account ID is detected automatically from the Meta Ads MCP — only ask if multiple
accounts are returned, and present them as a button list.

**2. Content calendar review (button approval)**
Present the calendar, then AskUserQuestion: "Schedule looks good?" — buttons:
"Yes — schedule everything" / "Yes — but start with week 1 only" / "Adjust dates first".

**3. Create campaigns via Meta Ads MCP**
For each batch:
- Create Ad Campaign with the objective
- Create Ad Sets with targeting (audience details prompted via AskUserQuestion buttons —
  e.g. "Auto-target lookalike from product image" / "Use saved audience" / "Define new")
- Upload generated Higgsfield videos/images as creatives
- Schedule per the plan's dates

**4. Confirm scheduling**
Summary table by week. Final AskUserQuestion: "Scheduling done — continue to Stage 5?" buttons:
"Yes — render the cost report (Recommended)" / "Pause one of the campaigns" / "Generate more
content" / "Skip Stage 5 — close pipeline".

---

## STAGE 5 — Cost Comparison Report

### Goal
After everything is generated and scheduled, render a polished HTML report comparing the
**actual Higgsfield credit + USD spend** for this campaign against the **estimated cost of
producing the same volume traditionally** (creators, studios, DOPs, post-production, FOOH
crews, photographers, etc.). Output the savings ratio + time savings, save to outputs, and
present.

### Steps

**1. Pull live spend from Higgsfield**

Call `transactions(limit=200)` (or the highest available limit) to fetch the actual credit
spend during the current campaign. Filter to jobs created during the Stage 3 generation
window (use the campaign's date-range start through "now" as the filter). Sum:
- credits per preset (UGC, Product Review, Hyper Motion, TV Spot, Wild Card, Tutorial,
  Unboxing, Virtual Try On)
- credits for image generation (Marketing Studio Image / GPT Image 2 / Soul / Nano Banana)
- total credits

Convert credits → USD using the user's plan rate (or omit USD if the rate isn't surfaced).
Common Higgsfield rates: Creator plan ≈ $0.02/credit · Team/Pro plans ≈ $0.01–$0.005/credit.
If unsure, present credits-only and note the rate is plan-dependent.

**2. Apply the traditional production cost model (baked-in industry averages)**

Use the table below as the default cost model. These are 2026 industry-average midpoints in
USD; the report should show a low–mid–high range, not a single number. Cite the model as
"Industry-average estimates, 2026" and let the user override if they have their own rate card.

| Asset type | Low (USD) | Mid (USD) | High (USD) | Why the range |
|---|---:|---:|---:|---|
| UGC creator video (TikTok / Reels) | 250 | 750 | 1,500 | Creator fee + light production |
| Product Review video | 300 | 900 | 2,000 | Talent + setting + edit |
| Tutorial / Recipe video | 400 | 1,200 | 2,500 | Recipe shoot + post |
| Unboxing video | 300 | 800 | 1,500 | Box creation + shoot + edit |
| Hyper Motion CGI hero (single product, ≤15s) | 3,000 | 9,000 | 15,000 | CGI/VFX studio half-day to two-day |
| TV Spot 15s | 15,000 | 50,000 | 150,000 | Production + DOP + cast + post |
| Wild Card / FOOH stunt | 30,000 | 100,000 | 500,000+ | Real FOOH = full production crew |
| UGC Virtual Try On video | 200 | 600 | 1,000 | Quick try-on shoot |
| Pro Virtual Try On video | 1,000 | 3,000 | 5,000 | Studio quality |
| Social media post (1:1 lifestyle still) | 100 | 250 | 500 | Photographer half-day rate |
| Hero banner (16:9 cinematic) | 1,000 | 2,500 | 5,000 | Studio + retouching |
| Product photoshoot WITH people | 500 | 1,500 | 3,000 | Half-day with talent |
| Product photoshoot WITHOUT people | 200 | 700 | 1,500 | Studio product photographer |

**Time-savings benchmark** (also baked in):

| Channel | Higgsfield typical turnaround | Traditional turnaround |
|---|---|---|
| 80 mixed videos | 1–3 hours render time | 4–12 weeks production |
| 19 image asset pack | 5–15 minutes render time | 1–3 weeks photographer + retouch |
| Scheduling | Minutes via Meta MCP | Days of trafficking |

**3. Compute savings**

- `traditional_low = sum(asset_count × low_cost)` per asset type
- `traditional_mid = sum(asset_count × mid_cost)` per asset type
- `traditional_high = sum(asset_count × high_cost)` per asset type
- `higgsfield_usd = total_credits × user_plan_rate_usd` (with explicit rate disclosed)
- `savings_pct_mid = 1 − higgsfield_usd / traditional_mid` (capped at 99.99%)
- `time_savings = traditional_weeks − higgsfield_hours / (24×7)`

**4. Render the HTML report**

Save to `/mnt/user-data/outputs/[brand]-cost-comparison.html`. Required sections:

1. **Hero number card** — "Pure HiGG: 100% Natural delivered for **$X** instead of **$Y–$Z**.
   You saved **N%** and **W weeks** of production time."
2. **Volume summary table** — what we generated (e.g. 50 UGC + 24 PR + 2 HM + 2 TV + 2 WC +
   8 social + 3 hero + 4 with-people + 4 without-people)
3. **Higgsfield spend breakdown** — credits per preset / per asset type, USD equivalent at
   the user's plan rate (clearly labeled)
4. **Traditional cost breakdown** — same volumes priced at low / mid / high industry-average
   rates, with a per-asset-type subtotal
5. **Side-by-side comparison** — total Higgsfield USD vs traditional mid-USD vs traditional
   high-USD; bar chart or simple horizontal bars in HTML/CSS (no external chart libs needed)
6. **Time savings panel** — Higgsfield render time vs traditional weeks
7. **Methodology footer** — disclose that traditional costs are 2026 industry-average
   estimates (not a quote), Higgsfield USD is based on the user's plan rate at the time of
   the report, and that prices vary by region / agency tier

Visual style: same brand-blue header treatment as the video and static plans (consistency).
Title: `[Campaign name] — Cost Comparison Report`.

**5. Present the report (button confirm)**

Show the user the saved file via a `computer://` link. Final AskUserQuestion:
"Cost report ready. What next?"
- "Done — close the pipeline (Recommended)"
- "Email this report to my team"
- "Adjust the traditional-cost rate card and re-render"
- "Run the pipeline again for another product"

---

## General Guidelines

- **Button-driven rule (HARD):** Every clarifying question is an AskUserQuestion call with
  2–4 concrete option buttons. Free-form typing is NEVER required to navigate, confirm, or
  route between stages. Only product image upload (file attach) and product URL paste are
  acceptable non-button inputs — and both are still click-based, not commands. Always offer
  a smart default the user can accept with one click.
- **No-pause rule:** Bundle every clarifying question into a single AskUserQuestion call.
- **5-format split (HARD):** Every campaign distributes evenly across 5 UGC formats —
  UGC Entertainment, Street Interview, Unboxing, Product Review, ASMR. Allocate
  `floor(VIDEO_COUNT / 5)` per format; distribute any remainder starting at format 1.
  Cinematic presets (Hyper Motion, TV Spot, Wild Card) are OFF by default and only
  activated on explicit user request.
- **Producibility rule:** Every idea must be producible inside an active Marketing Studio
  preset within its 4–15s cap, OR explicitly labeled "Outside Marketing Studio."
- **Per-batch permission gate (Stage 3):** ALWAYS ask before generating each preset's batch.
  Never auto-run the full plan. Use button choices, not typed confirmations.
- **Hook vs caption clarity:** A "hook line" the user writes is VO/caption copy. The system
  `hook_id` is a structured visual template from the picklist — these are different.
- **Confirm between stages with buttons:** Each stage ends with an AskUserQuestion button
  confirmation before advancing.
- **Multi-variant brands:** distribute content evenly across SKU variants within each preset.
- **Visual identity consistency:** same color palette, tone, reference image throughout.
- **Failure handling:** log failed IDs and offer "Retry / Skip / Pause" buttons per stage.
