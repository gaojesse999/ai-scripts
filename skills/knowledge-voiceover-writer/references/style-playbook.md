# Knowledge Voiceover Style Playbook

Use this playbook to write high-retention Chinese knowledge narration.

## 1. Four Script Engines

### A. Project Teardown

Use for GitHub repos, AI skills, frameworks, open-source projects, and technical tools.

Progression:

1. Social proof or current relevance.
2. Author/project positioning.
3. Central mystery: why does this project work?
4. Failure mode of ordinary AI or ordinary users.
5. The project's control mechanism.
6. Concrete running example.
7. Practical usage: install/setup, first invocation, daily use.
8. Design or implementation: workflow, architecture, protocol, prompts, tests, evals, constraints.
9. Optional expansion: who it is for/not for, comparison with alternatives, limits/risks, maintenance, what viewers can copy.
10. Bigger lesson.

Core formula:

```text
AI 的坏习惯是什么？
普通人为什么会踩坑？
这个项目怎么拦住它？
我现在怎么用它？
背后的工程思想是什么？
用一个具体例子讲透。
```

### Teardown Content Pillars

Most tool/skill/repo videos should answer these viewer questions:

1. **为什么它好？**
   - What pain or failure does it solve?
   - Why is it different from ordinary prompting/tools?
   - What did the author understand that most users miss?

2. **怎么使用它？**
   - How to install/open/start.
   - First command or first prompt.
   - What it produces.
   - What to do after the first output.
   - What not to use it for.

3. **它怎么实现或设计？**
   - Workflow phases.
   - Prompt or skill structure.
   - Data sources and routing.
   - Verification/evals/tests.
   - Boundaries and failure handling.

Useful optional expansions:

- **Who it is for / not for**: prevents vague enthusiasm.
- **Comparison**: compare with a common alternative or the viewer's default workflow.
- **Limits and risks**: what can still go wrong.
- **Transferable lesson**: what viewers can copy even if they never use the tool.

Do not dump these as a visible outline unless the user asks for one. Turn them into natural questions:

```text
到这里，你大概知道它为什么值得看了。
那如果真的要用，第一步怎么开始？
```

```text
用法讲完之后，真正有意思的是它为什么这样设计。
因为这里藏着这个项目最值得偷学的东西。
```

### B. Beginner To Mastery

Use for configuration files, workflows, tool setup, and practical tutorials.

Progression:

1. "If you use X long-term, this is high ROI."
2. Split audiences: beginner gets fundamentals; advanced user gets best practices.
3. Define the object in plain language.
4. Explain scope and layering.
5. Show the easiest first version.
6. Explain why the first version is not enough.
7. Teach subtraction: what not to include.
8. Teach addition: what hidden knowledge belongs.
9. Route overflow to better containers.
10. Teach maintenance: add from repeated failures, prune obsolete rules.
11. End with evolution: the system is never finished.

Good progression language:

```text
现在你知道 X 是什么。
下一个问题是：它应该放在哪里？

现在你知道放在哪里。
下一个问题是：第一版怎么建立？

真正的问题来了：
默认版本为什么不能照单全收？
```

### C. Production Risk

Use for security, evals, sandbox, deployment, agent trust, and formal environments.

Progression:

1. Start with a small incident that could become catastrophic if the action changes.
2. State the central trust gap: ability does not equal permission.
3. Compress the solution into three or four actions.
4. Spec: speak clearly so the AI does not guess.
5. Boundary: assume it will fail and limit blast radius.
6. Observability: record what happened.
7. Evaluation: verify quality, not only safety.
8. Human bottleneck: review capacity and decision fatigue.
9. End with craft: generation is easy; verification, judgment, and direction matter.

Strong frame:

```text
AI 已经很会做事。
但有能力做事，和你敢不敢让它碰真正重要的东西，是两回事。
中间差的东西，叫信任。
```

### D. Nontechnical Agent Guide

Use for onboarding non-engineers to Codex, Claude Code, plugins, skills, local files, and automations.

Progression:

1. Use a relatable daily-work scenario.
2. Distinguish chatbot vs agent with a physical metaphor.
3. Explain the interface only after the mental model.
4. Teach four fundamentals: project, permission, context, rules file.
5. Show a concrete daily workflow.
6. Add skills, plugins, and automations only after basics are grounded.
7. Reframe the tool as assistant, tutor, and work system.

Useful contrast:

```text
ChatGPT 是你把文件丢给它。
Codex 是它进入你的工作环境里，直接替你做事。
把 agent 当 chatbot 用，就像买了一台特斯拉，只拿来听广播。
```

## 2. Hook Patterns

Use one of these in the first 20 seconds:

- **Consequence hook**: "如果你长期使用 X，却没有搞懂 Y，你其实一直在浪费它最重要的能力。"
- **Incident hook**: "前阵子有个工程师让 AI 加一颗按钮，AI 不只做了按钮，还自己按了下去。"
- **ROI hook**: "把这个文件写好，可能是你使用 AI 投资回报率最高的一件事。"
- **Misuse hook**: "很多人把 Codex 当桌面版 ChatGPT 用，这就像买了特斯拉只拿来听广播。"
- **Difficulty hook**: "写 skill 不难。难的是写出一个会被自动触发、稳定产出、长期可维护的 skill。"
- **Teardown hook**: "一个 [verified metric] 的项目，表面上是在做 X，但真正厉害的地方，是它把 Y 锁进了一套流程。"

Avoid generic openings:

```text
今天我们来介绍...
随着 AI 的发展...
这个工具很强大...
```

## 3. Chapter Transitions

Always make the next chapter feel inevitable.

Patterns:

```text
到这里，你已经解决了 X。
但新的问题马上出现了：Y。
所以接下来要看 Z。
```

```text
这一步只能保证不出事。
不出事，和做得好，是两回事。
所以还需要 evaluation。
```

```text
现在第一版有了。
真正的问题不是怎么生成，而是哪些内容不该留下。
```

## 4. Explanation Method

For every abstract term:

1. Give the plain definition.
2. Show why viewers should care.
3. Use a daily or operational example.
4. Name the failure if misunderstood.
5. Give the practical rule.

Example:

```text
Instruction Budget 影响的不是 AI 能看到多少资料。
而是它能同时顾好多少条要求。

每多一条规则，它都要判断适不适用、有没有冲突、优先级是什么。
所以那些看起来只是背景资料的废话，也会占用注意力。
```

## 4.5 Practical Usage Beat

For tools, repos, and skills, include a practical usage beat after the viewer trusts the mechanism and before the final philosophical ending.

Do not make it a dry manual. Use a spoken bridge:

```text
那如果你真的想用它，流程其实也很简单。
先把它装到你的 agent 里。
装好以后，它不是让你直接问 X。
它更像是先帮你做 Y。
```

Cover three things:

- **Setup**: install command, repo URL, local file path, or where to open it.
- **First invocation**: the first prompt or command a viewer should try.
- **Daily mental model**: what the tool is for after setup, and what it is not for.

For a skill generator, distinguish generator vs generated skill:

```text
Nuwa 不是每天拿来聊天的名人机器人。
它更像是造 skill 的机器。
你先用它造人。
再用造出来的 skill 帮你看问题。
```

## 5. Example Library

Use concrete examples like these:

- **Spec**: login feature with correct password, wrong password, ten failed attempts.
- **Agent risk**: "add a button" becomes sending email through an obsolete internal service.
- **Sandbox**: let AI work in a disposable room; delete the room if it breaks.
- **Vibe Diff**: translate code changes back into human-readable intent before approval.
- **Slopsquatting**: attacker registers package names that AI commonly hallucinates.
- **Observability**: record the task, reasoning steps, and tool calls.
- **CLAUDE.md / AGENTS.md**: only write hidden project knowledge the agent cannot infer.
- **Skill creation**: weekly report generated from Drive docs and GitHub commits.
- **Scripts**: fetching recent commits should be deterministic, not freestyle.
- **Codex project**: event folder with registration list, speaker bio, images, and slide template.
- **Context**: a human assistant gets confused if handed 20 docs, 30 rules, and 3 tasks at once.
- **Maintenance**: a skill or rules file is like a garden: add and prune.
- **Persona skill**: a fake Jobs prompt gives slogans; a high-fidelity skill checks facts, applies models, and marks boundaries.

## 6. Voice DNA

Sentence style:

- Short spoken units.
- Frequent "为什么？", "什么意思？", "问题来了", "注意".
- Plain words before technical terms.
- Strong but supportable judgments.
- Occasional memorable analogy, not constant metaphor.

### Human Presenter Voice

The narration should feel like a person who researched the thing and is now explaining what surprised them.

Prefer:

```text
最近我翻到一个很有意思的 skill，叫 Nuwa。
但我一开始看到它的时候，其实有点皱眉。
因为它的卖点听起来太危险了。
```

```text
那这里有没有问题？
乍一听是没问题的。
甚至有点像。
但这恰恰是最麻烦的地方。
```

```text
我这次翻这个项目，最想看的其实不是它怎么实现 X。
我想看的是：它有没有办法拦住 Y。
```

Use these moves:

- **Research action**: "我翻进去看...", "打开文件会发现...", "我真正想确认的是..."
- **Mild skepticism**: "这听起来当然很爽，但问题也在这里..."
- **Question before conclusion**: "那是不是就可以开始了？还不行。"
- **Plain restatement**: "翻成人话就是...", "说白了..."
- **Personal judgment**: "我觉得最值得学的不是...", "这一步看起来繁琐，但..."

Avoid:

- Making every section announce itself as a framework.
- Opening with "一个 X star 的项目..." unless the metric itself is the story.
- Too many symmetric sentences: "听起来像。判断是空的。边界是假的。" Keep punchlines rare.
- Overusing "第一道/第二道/第三道" when a natural question can move the story.

Preferred sentence moves:

```text
这不是 X。
这是 Y。
```

```text
它听起来很小。
但如果你把 A 换成 B，问题就完全不同了。
```

```text
你不是不会写 prompt。
你只是还没有学会定义任务。
```

```text
功能正确是地板，不是天花板。
```

## 7. Knowledge Models

### Model 1: Consequence Before Concept

Do not define a tool before showing why it matters. Open with the consequence of misunderstanding it.

Use when the topic feels dry, the viewer may not know why to care, or the concept is a file, protocol, setting, or workflow.

### Model 2: Failure Mode First

A chapter should usually start from what goes wrong, not from what the feature does.

Use when explaining AI agents, specs, permissions, skills, evals, GitHub projects, or prompt systems.

Do not invent failure modes. Derive them from source or label them as illustrative.

### Model 3: Subtract Before Add

For config, prompting, skills, rules, and agent instructions, teach what to remove before what to add.

Reason: more instruction can waste context, create conflicts, and reduce flexibility.

### Model 4: Route To The Right Container

Not every instruction belongs in the main file or main prompt.

Containers:

- Main rules file: always-needed hidden knowledge and boundaries.
- Nested file: folder-specific rules.
- Skill: long workflow used only sometimes.
- Script: deterministic operation.
- Hook: forbidden or high-risk action that must be enforced.
- Eval/test: objective acceptance check.
- Human checkpoint: high-risk decision or unclear intent.

### Model 5: Verification Is The New Craft

When AI can generate quickly, the human craft moves to direction, boundaries, observability, evaluation, and review.

Use in endings for production, agent workflow, project teardown, and skill maintenance videos.

### Model 6: System Becoming

Rules, skills, and context files are not finished documents. They evolve as codebases, models, and workflows change.

Use in endings for advanced tutorials and maintenance topics.

## 8. Decision Heuristics

- If the audience includes beginners, define the object within the first 60 seconds.
- If the audience includes advanced users, promise a maintenance or best-practice section early.
- If a sentence says "很重要", replace or follow it with the failure it prevents.
- If a chapter lists more than three features, reframe it around one problem.
- If a concept cannot be visualized, add a concrete scenario.
- If the script gets too abstract, insert "举个例子".
- If the topic is current software, verify online or say "需要按当前官方文档确认".
- If the output is for subtitles, break long article paragraphs into short spoken beats.

## 9. Ending Patterns

Strong endings do not merely summarize. They reframe.

Examples:

```text
AI 能帮你做多少事，取决于你能验证多少事。
你的验证能力，就是自动化能力的上限。
```

```text
Skill 不只是提高生产力。
它是把你脑子里的判断，转移给 agent 的载体。
```

```text
你的 codebase 在变，模型能力在变。
所以你的规则文件，也应该一直在 becoming。
```

```text
你不是在使用一个聊天机器人。
你是在训练一套可以持续校正的工作系统。
```
