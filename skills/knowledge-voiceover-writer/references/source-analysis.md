# Source Analysis

This skill was distilled from user-provided Chinese SRT transcripts. Treat them as style and structure sources, not factual authority.

## Sources

1. `Google AI 课程 Day 4+5 解析，怎么放心让 AI 上正式环境？`
   - Type: production-risk explainer.
   - Main pattern: incident hook -> trust gap -> spec / boundary / eval -> human bottleneck -> craft reframe.

2. `Skill 实战教学，从制作到维护的完整指南`
   - Type: practical skill-making tutorial.
   - Main pattern: why skill-making is hard -> anatomy -> when to make one -> two creation paths -> common pitfalls -> maintenance as compound interest.

3. `15 分钟学完 CLAUDE.md：从入门到精通`
   - Type: beginner-to-mastery tutorial.
   - Main pattern: ROI hook -> beginner/advanced promise -> concept/scope -> first version -> subtract/add -> route overflow -> maintain and prune.

4. `Codex 新手教学，非技术人员也能上手的 AI Agent 新手指南`
   - Type: nontechnical agent onboarding.
   - Main pattern: relatable nontechnical user -> chatbot vs agent contrast -> interface orientation -> project / permission / context / rules file -> daily workflow -> skills / plugins / automation -> agent as tutor.

5. `700 万人下载的 /grill-me，Matt Pocock 到底写了什么？`
   - Type: project teardown.
   - Main pattern: social proof + author authority -> central mystery -> ordinary AI failure -> project mechanism -> concrete examples -> human control reframe.
   - Useful for GitHub/skill videos because it turns a repo into a story about controlling AI behavior.

## Cross-Source Mental Models

### 1. Consequence Before Concept

Strong scripts avoid dry definitions at the start. They first establish a consequence:

- Production AI can take unauthorized action.
- A poorly written skill may not trigger or may become unmaintainable.
- A bloated rules file wastes instruction budget.
- Treating Codex like ChatGPT wastes its core value.
- A persona prompt can produce confident style imitation without grounded judgment.

Use this model to make dry topics watchable.

### 2. Audience Ladder

The scripts often serve beginners and advanced users in the same video:

- Beginners get what the object is, where it lives, and how to start.
- Advanced users get best practices, pruning, maintenance, and reliability tradeoffs.

This keeps basic explanations from feeling shallow.

### 3. Failure Mode First

The strongest sections introduce a failure:

- AI guesses when spec is incomplete.
- AI overreaches without sandbox and checkpoints.
- Skills fail when descriptions do not match user trigger language.
- Rules files rot when old model patches remain forever.
- Persona prompts create fluent but unfaithful imitation.

Then the mechanism becomes the solution.

### 4. Subtract Before Add

The CLAUDE.md and skill tutorials both teach subtraction:

- remove facts the agent can discover;
- remove rules only needed in one folder;
- move long workflows to skills;
- move deterministic work to scripts;
- remove old model patches after upgrades.

This style feels expert because it warns against over-instruction.

### 5. Container Routing

The scripts repeatedly ask: where should this knowledge live?

- AGENTS.md / CLAUDE.md for always-needed project rules.
- Nested files for folder-specific rules.
- Skills for reusable but conditional workflows.
- Scripts for deterministic operations.
- Hooks for forbidden actions.
- Evals/tests for verification.
- Human review for high-risk judgment.

This provides a reusable decision tree for many AI workflow topics.

### 6. Evidence-Bound Judgment

The project-teardown style is strongest when it distinguishes:

- verified facts;
- source-supported interpretation;
- illustrative examples;
- speculative but plausible implications.

For GitHub projects, use current metrics and author context as heat, but make the video about the mechanism, not the numbers.

### 7. Maintenance And Becoming

The best endings turn maintenance into a philosophy:

- rules files are gardens;
- skills compound through use and revision;
- AI systems improve when failures are written back into the harness;
- codebases and models evolve, so instructions must evolve too;
- knowledge artifacts are not static docs, but living control surfaces.

## Expression DNA

- Mostly short spoken clauses.
- Frequent direct address: "如果你...", "你可能会问...", "注意".
- Strong contrasts: chatbot vs agent, safety vs quality, style imitation vs grounded judgment.
- Concrete analogies: Tesla as radio, sandbox as disposable room, game save point, garden.
- Practical examples before abstractions: event planning, weekly report, login spec, API key hook, persona skill critique.
- Endings summarize and then lift into a larger idea.
- Human presenter presence: "我仔细看了", "我认为可惜", "打开会发现", "你看懂差别了吗". The speaker is not invisible.
- The best drafts often sound like discovery: mild skepticism first, then a concrete example, then the mechanism.

## Nuwa Style Iteration Note

In the Nuwa Skill teardown iteration, the more effective version did not change the facts much. It changed the speaking posture:

- It stopped opening with "一个 29,480 star 的 skill..." and started with "最近我翻到一个很有意思的 skill...但我一开始有点皱眉."
- It moved metrics after the speaker's first human reaction.
- It reduced "第一道闸门 / 第二道闸门" framing and let questions move the script.
- It used "我这次翻 Nuwa，最想看的其实不是..." to give the presenter a reason to be there.
- It explained "三重验证" as three plain questions before treating it as a framework.
- It kept punchlines, but broke up overly symmetrical AI-sounding lines with concrete explanation.

Reusable rule: if a draft feels like an analysis report split into subtitle lines, rewrite it as a researched person's walkthrough.

## Comparison Checklist

Use this only after an independent draft exists:

- Does the opening combine heat with a mystery, instead of merely announcing the topic?
- Does the opening sound like a human observation rather than a metric template?
- Does the first minute preview the route when the video is a longer teardown?
- Is the presenter visible through research actions, doubt, surprise, or judgment?
- For a tool/skill/repo, does the script clearly answer why it is good, how to use it, and how it is designed or implemented?
- Is there one clear enemy: a common failure mode, misconception, or risk?
- Does each chapter begin with a new problem?
- Is there a concrete running example that makes the mechanism visible?
- Does the script show the bad version before explaining the good mechanism?
- Are transitions causal rather than list-like?
- Are lists converted into why-driven explanations where possible?
- Are framework names introduced after the problem, not before it?
- Are repeated symmetric punchlines used sparingly?
- Are judgments vivid but supportable?
- Does the ending lift from the project to AI collaboration, verification, or knowledge transfer?
- Does the draft avoid copying reference wording?
- For a tool/skill/repo, can the viewer actually try it after watching?

## Anti-Patterns Observed By Contrast

Avoid:

- pure feature tours;
- long definitions before viewer payoff;
- overusing technical acronyms before plain examples;
- overusing tidy framework labels that make the speaker disappear;
- leaving viewers without an immediate action or changed mental model;
- treating AI output as magic instead of a system that needs boundaries and verification;
- reading reference SRTs before generating a supposedly independent draft.
