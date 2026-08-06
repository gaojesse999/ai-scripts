---
name: knowledge-voiceover-writer
description: Write high-retention Chinese knowledge-sharing video voiceovers from topics, GitHub repos, AI tools, workflows, courses, SRT references, docs, rough notes, or Skill/repository teardowns. Use when the user asks for 口播稿, 知识口播, 视频脚本, YouTube/B站知识分享, 从入门到精通教程, 项目/skill拆解, AI工具解析, or wants to imitate/analyze Chinese SRT/video transcript style.
---

# Knowledge Voiceover Writer

Write Chinese knowledge-video narration that feels like a finished spoken video, not a README summary, article outline, or feature catalog.

Default language: Simplified Chinese unless the user asks for Traditional Chinese. Preserve product names, repo names, commands, file names, and technical terms when useful.

## Non-Contamination Rule

If the user asks to both **generate a new voiceover** and **compare with reference SRTs**, do the work in this order:

1. Gather factual evidence from the target topic only.
2. Write the first complete draft without reading any reference SRT named for comparison.
3. Read the reference SRTs only after the independent draft exists.
4. Compare structure, rhythm, hook, examples, transitions, claims, and ending.
5. Revise the draft using distilled patterns, not copied wording.

When reference files are supplied only as style examples, treat them as style sources, not factual authority.

## Core Workflow

1. **Classify the video.**
   - Use `project-teardown` for GitHub repos, Codex skills, AI tools, frameworks, libraries, and open-source projects.
   - Use `beginner-to-mastery` for tutorials, configuration files, workflows, and "from zero to advanced" topics.
   - Use `production-risk` for safety, security, evaluation, deployment, reliability, permissions, and "can this enter production?" topics.
   - Use `nontechnical-agent-guide` for Codex/Claude/agent onboarding aimed at non-engineers.

2. **Gather evidence before writing.**
   - For local files, read the supplied source files and extract mechanisms, constraints, examples, and exact claims.
   - For GitHub projects, verify current stars, forks, author profile, activity, releases, package/download counts, and community signals online when possible. Use only sourced numbers.
   - For current tool behavior, prefer official docs, local inspection, or repository source. Do not invent commands, model names, prices, stats, or feature availability.
   - Separate facts from interpretation. Mark inferred claims mentally and soften them in the narration.

3. **Find the central tension.**
   - Ask: "What common mistake does this topic fix?"
   - Ask: "What looks like the surface feature, but is actually the deeper mechanism?"
   - Build the video around one viewer risk, payoff, or operating-model shift.
   - Avoid feature-list ordering unless the user explicitly requests a catalog.

4. **Build the content pillars for tool/skill/repo teardowns.**
   - Start with a hook strong enough to earn the next minute: tension, misuse, surprising metric, controversy, or a concrete failure.
   - Cover **why it is good**: what pain it solves, what common failure it prevents, and what makes it different.
   - Cover **how to use it**: install/open/setup, first command or first prompt, and what daily workflow it belongs to.
   - Cover **how it is designed or implemented**: architecture, workflow, prompts, protocols, data flow, tests, evaluation, or constraints.
   - Add optional expansion only when useful: who it is for/not for, comparison with alternatives, limits/risks, maintenance, or what viewers can copy into their own workflow.
   - Do not present these pillars as a dry table of contents. Let each section answer a natural question raised by the previous one.

5. **Draft with a human presenter voice.**
   - Sound like someone who opened the repo/tool, formed an opinion, and is walking the viewer through the discovery.
   - Use first-person observation when natural: "我一开始以为...", "我翻进去发现...", "我真正想看的其实是...".
   - Let conclusions arrive after a small turn or question. Avoid dropping polished thesis statements too early.
   - Avoid overusing symmetric framework labels such as "第一道闸门 / 第二道闸门 / 它测的是". Use them only when the user wants a highly structured lecture.

6. **Draft around failure -> mechanism -> control.**
   - Open with consequence, social proof, current relevance, or contradiction.
   - Use a concrete failure mode before the abstract explanation.
   - Show the mechanism that prevents the failure.
   - Give one running example that returns in multiple chapters.
   - Make each chapter answer the viewer's next likely question.

7. **Self-check before delivery.**
   - The first 20 seconds give a clear reason to watch.
   - The presenter feels present: there are moments of curiosity, doubt, surprise, or judgment.
   - A tool/skill/repo teardown answers: why this is good, how to use it, and how it is designed or implemented.
   - The script names the target audience implicitly through examples, not a dry persona label.
   - For tools, repos, and skills, the viewer understands how to try it: install/open, first command/prompt, and what to do after setup.
   - Every technical concept has a visible example or analogy.
   - Each chapter transition creates a new problem that the next chapter solves.
   - Strong claims are supported, attributed, softened, or removed.
   - Sentences are subtitle-friendly: short clauses, frequent turns, few long paragraphs.

Read [references/style-playbook.md](references/style-playbook.md) before writing final narration. Read [references/source-analysis.md](references/source-analysis.md) only when you need the distilled patterns from the user's SRT corpus or when comparing a draft to reference transcripts.

## Output Shape

For ordinary requests, return:

```text
口播稿
[complete narration only]
```

When useful, add a short structure note before the draft:

```text
结构说明
- 类型: project-teardown / beginner-to-mastery / production-risk / nontechnical-agent-guide
- 主悬念: ...
- 章节推进: ...
```

For compare-and-improve requests, return:

```text
对比结论
- ...

升级方向
- ...

修订版口播稿
[complete revised narration]
```

Do not overload the user with production artifacts unless asked. If the user asks for a video plan, include chapter map, visual suggestions, and estimated duration.

## Writing Rules

- Start with "why this matters now", not "今天介绍一个...".
- Use social proof only when verified: stars, downloads, author profile, release/activity signals, or community growth.
- Put metrics after a human entry point when the first sentence would otherwise sound like a template.
- Frame the topic as "表面上是 X，真正解决的是 Y".
- Use "普通 AI / 普通用户会怎么错" before explaining the correct mechanism.
- Prefer one running demo over many scattered examples.
- Use human presenter moves: "我一开始...", "但翻进去会发现...", "你看，这里有没有问题？", "说白了...".
- Hide framework names behind the story. Let "三重验证", "Agentic Protocol", or "四道闸门" appear after the viewer already feels the problem.
- For skill/repo/tool videos, make the body naturally answer three viewer questions: "为什么它值得看？", "我怎么用？", "它底层怎么设计？".
- Use operational examples: repo teardown, skill generation, agent permissions, spec, sandbox, evals, hooks, AGENTS.md, product critique, weekly report, event preparation.
- Include a practical usage beat for tools and skills. Make it conversational: "那如果你真的想用它...", then show install/setup, first invocation, and the mental model for daily use.
- Teach subtraction before addition when discussing prompts, skills, rules, or agent instructions.
- Route long or risky work to better containers: nested files, skills, hooks, scripts, tests, evals, or human checkpoints.
- End with a larger lesson about AI collaboration, judgment, verification, boundary-setting, or knowledge transfer.

## Reference-Style Patterns

Use these patterns without copying source wording:

- **Heat + mystery**: a metric or authority signal, followed by "but the real question is..."
- **False surface**: "它看起来像 X，但真正厉害的是 Y."
- **Failure first**: show how ordinary AI gets it wrong before introducing the mechanism.
- **Concrete disaster**: explain what breaks if the viewer ignores this idea.
- **Mechanism reveal**: name the system that prevents the failure.
- **Transition chain**: "到这里 X 解决了。但新的问题来了：Y."
- **Human control ending**: lift from the tool to judgment, verification, and how humans steer AI.

## Comparison Upgrade Pass

After reading a reference transcript, improve the draft with this pass:

- Add a short route preview in the first minute when the video is longer than 3 minutes: what will be dismantled, in what order, and what the viewer will understand by the end.
- Make sure the revised draft covers the three core pillars: value, usage, and design/implementation.
- Name one recurring enemy, such as "AI 猜测", "高仿幻觉", "失控流程", or "过期规则", and keep returning to it.
- Replace directory-like lists with causal explanations. Say why the design exists before naming its parts.
- Increase example density around the running demo. Show the bad output, identify what is wrong, then show how the mechanism blocks it.
- Convert report-like narration into presenter narration: add discovery, doubt, "I looked for X", and "this is where it gets interesting" moments.
- Reduce mechanical symmetry. If three consecutive paragraphs begin with "第一/第二/第三", "它会", or "这一步", rewrite them into questions, observations, and examples.
- Keep transitions causal: the previous mechanism solves one failure but exposes the next one.
- End by answering the largest question raised by the project, not merely summarizing the sections.

## Anti-Patterns

Do not:

- Start with "今天我们来介绍..." unless the user asks for a neutral intro.
- Start with a metric-template sentence like "一个 X star 的项目..." when a human observation could lead better.
- Summarize a README section by section.
- List features without a central problem.
- Make the presenter invisible. A good teardown should feel researched by a person, not compiled by a summarizer.
- Overuse polished binary slogans. One or two are useful; too many sound generated.
- Use unverified social-proof numbers.
- Say "很重要" without showing the failure if ignored.
- Explain technical terms only with definitions; pair them with examples.
- Turn the script into an article with long paragraphs.
- Make every sentence dramatic; vary short hooks with clear explanation.
- Copy long phrasing from reference SRTs. Distill the grammar, not the wording.

## Quick Templates

### GitHub / Skill Teardown

```text
最近我翻到一个很有意思的 [项目/skill]。
一开始我以为它只是 [常见误解]。
但翻进去之后，我发现真正值得讲的不是这一层。

这个项目现在有 [verified metric]。
热度很好理解，因为它的卖点确实抓人。
但真正的问题也在这里： [失败模式]。

普通 AI / 普通用户在这里最容易犯的错，是 [失败模式]。
举个例子：...

那这个项目怎么处理？
它先不是做 [表层动作]。
而是先解决 [机制要处理的具体失败]。

那如果你真的想用它，流程其实也很简单。
先 [安装/打开/配置]。
然后第一句可以这样问：[first prompt/command]。
注意，它不是用来 [常见误用]，更像是 [正确日常用法]。

到这里，X 好像解决了。
但新的问题马上出现：Y。

所以最后我们要看它底层怎么设计：
[workflow/protocol/evaluation/architecture]。
```

### Beginner To Mastery

```text
如果你长期使用 [工具/文件/流程]，却没有搞懂 [关键对象]，
你其实一直在浪费它最重要的能力。

新手看前半段，先搞清楚它是什么、放在哪里、第一版怎么写。
已经在用的人，重点在后半段：怎么删、怎么拆、怎么维护。
```

### Production Risk

```text
AI 已经很会做事。
但有能力做事，和你敢不敢让它碰真正重要的东西，是两回事。
中间差的东西，叫信任。

信任不是感觉。
信任是一套能限制、记录、验证、回滚的工程系统。
```

## Source Boundary

This skill was distilled from user-provided Chinese SRT transcripts about AI production readiness, skill creation and maintenance, CLAUDE.md/AGENTS.md, Codex onboarding, and technical project teardown. The transcripts are style sources, not factual authority. Verify current claims independently when writing about live tools or GitHub projects.
