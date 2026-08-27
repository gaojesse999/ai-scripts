# Popular Knowledge Script Style

Use this reference when the user asks for a knowledge-sharing video, YouTube-style explainer, viral breakdown, creator-style narration, or provides an SRT/reference script with a high-retention educational tone. Treat the reference as a writing grammar, not a factual source.

## Core Shape

A popular knowledge script should feel like a guided teardown, not a repository tour or README summary.

When this reference is used inside Knowledge Video Builder, treat narration quality as the first draft target. Write the complete voiceover so it can stand alone as a good spoken script before turning it into storyboard, screen text, and scene-plan data. The production artifacts should preserve the voiceover's hook, rhythm, examples, and ending instead of making the narration serve a visual checklist.

Three skeletons cover most knowledge videos. Pick by what the subject is: the five-stage frame for a mechanism or method, the teardown for a tool or repository, the ladder for a tutorial. All three are **content stages, not a slide count** — a stage that enumerates may span several scenes while a single-claim stage stays one.

### Default five-stage frame: 解决什么问题 → 原理 → 怎么做 → 举例 → 总结

This is the default in Knowledge Video Builder and the right choice whenever the viewer's own behaviour, not a product, is the subject: a cognitive trap, a habit, a mechanism, a working method.

1. **解决什么问题** — Open on a situation the viewer recognizes in themselves, name what it costs, then state the route in one line.
2. **原理** — Name the one mechanism that explains it, and mark its limits in the same breath.
3. **怎么做** — Turn the principle into a small ordered set of steps that can be started today.
4. **举例** — Replay those steps inside concrete scenes, ideally two mirrored cases where the same mechanism produces opposite failures.
5. **总结** — Compress the method into one repeatable sentence, then close with exactly one interaction line, which must be a **two-option A/B multiple-choice question (选择题)**. See [Closing Interaction](#closing-interaction).

```text
你有没有过这种情况：重要的事草草交差，不重要的事却死磕很久。
其实这不是你分不清轻重，而是「想赶紧收尾」这件事在起作用。
应对办法分三步：标记、设规则、回顾。
放进两个场景看：年度报告结束得太早，游戏关卡结束得太晚。
所以，不是所有任务都值得同一种完成方式。
你更常是哪一种？A，该停的时候停不下来；B，该继续的时候草草收尾。
```

What each stage is most likely to get wrong:

- **解决什么问题** must be universal before it is specific. State the pattern in a form every viewer recognizes, *then* land it on one or two named examples. Opening on the example first makes the video look like it is about 年度报告 rather than about the mechanism.
- **原理** carries the credibility risk. Introduce one concept, not a survey, and keep the honest boundary in the spoken line — "这个说法并不能解释所有的赶工和沉迷". A mechanism claimed too widely is the fastest way to lose the viewers most likely to share the video. When the concept comes from research, say what it does explain rather than restating the study.
- **怎么做** should be the shortest chapter, and its steps must be sequential rather than a checklist of tips. Three is usually right; resist a fourth.
- **举例** is where retention is won, so it must not degrade into a recap of 怎么做. Give each case its own stakes, show the wrong path first, then apply the rule. Two opposite cases prove the mechanism generalizes in a way one case never can.
- **总结** repeats the rules from 怎么做 in compressed form and nothing new. If the ending introduces a fresh idea, that idea belonged in 原理. It ends on the interaction line, not on the reframe.

### Teardown structure

For tools, repositories, and frameworks:

1. Open with social proof, current relevance, or a sharp contradiction.
2. Name the central mystery: what does this tool reveal, solve, or control?
3. State the video route in plain language.
4. For each chapter, start from the failure mode or common misconception.
5. Introduce the tool/rule as the mechanism that prevents that failure.
6. Explain the underlying principle with a concrete example.
7. Escalate to the next problem created by the previous solution.
8. End by reframing the subject into a larger lesson.

### Learning ladder

For "from beginner to mastery" tutorials, use a ladder instead of a teardown:

1. State who must care and the payoff of learning this now.
2. Split the audience: beginners will learn the concept and first setup; advanced users will learn best practices and iteration.
3. Define the object in simple terms.
4. Explain where it lives, what scope each location controls, and how rules layer.
5. Show the easiest starting command or first artifact.
6. Reveal why the automatic/default version is not enough.
7. Teach subtraction first: what to delete, move, or avoid.
8. Teach addition second: what hidden knowledge, process rules, completion checks, and source pointers belong there.
9. Route overflow to better containers: nested files, skills, hooks, scripts, docs, or tests.
10. Teach maintenance: how to add from repeated failures and prune obsolete rules.
11. End with a larger operating principle, such as "the system is always becoming."

Prefer this pattern:

```text
AI 的坏习惯是什么
普通人为什么会踩坑
这个 skill 怎么拦住它
背后的工程思想是什么
用一个具体例子讲透
```

Avoid this pattern:

```text
这个仓库有 A
这个仓库有 B
这个仓库有 C
所以它很有用
```

## Opening

Open with the most clickable, counterintuitive, or consequential claim that is supported by evidence.

For GitHub projects, actively verify usable social proof online before writing the hook when web access is available:

- current stars, forks, contributors, releases, and recent commit activity from GitHub;
- star growth from star-history or an equivalent public tracker when relevant;
- package/download counts only from the package registry or official distribution surface, not from unsourced README claims;
- author background from the author's GitHub profile, official site, X/Twitter, LinkedIn, or project-linked bio;
- notable community signals such as trending status, discussion volume, public endorsements, or issue/PR activity only when directly observed.

Use these signals to answer: "Why should the viewer care now?" Do not invent or round up numbers. If a statistic is unavailable or unverifiable, omit it or phrase it qualitatively.

Good openings:

- "一个教 AI 写代码的 skill，最重要的规则，居然是先不准写代码。"
- "这个被几百万人下载的 skill，核心内容只有几行字。问题是：为什么这几行字能改变 AI 写代码的方式？"
- "Matt Pocock 真正开源的，不是几个提示词，而是一套控制 AI 随机性的工程系统。"

Weak openings:

- "今天介绍一个开源项目。"
- "这个仓库包含很多有用的 skill。"
- "随着 AI 编程的发展，工程流程变得越来越重要。"

## Chapter Engine

Each chapter should be driven by a problem, not by a feature name.

Use:

```text
现在你已经解决了 X。
但新的问题马上出现了：Y。
所以生产线的下一站，是 Z。
```

For technical tools, explain the chapter in this order:

1. Describe the naive AI behavior.
2. Show why it fails in production.
3. Name the skill/rule.
4. Show the exact constraint it imposes.
5. Translate the engineering principle into a simple metaphor or worked example.
6. State the control gained by the human.

For practical tutorials, use a "what it is → where it applies → first version → why it breaks → how to refine → how to maintain" progression. Each chapter should answer the viewer's next likely operational question:

```text
现在你知道 X 是什么。
下一个问题是：它应该放在哪里？
现在你知道放在哪里。
下一个问题是：第一版怎么生成？
现在你有第一版。
真正的问题来了：哪些内容不该留在里面？
```

This creates progression without needing artificial drama.

## Voice And Sentence Rhythm

Write for subtitles and spoken delivery.

- Use short clauses and frequent line breaks.
- Prefer 1-3 second spoken units.
- Mix quick questions, short turns, and longer explanatory beats.
- Use "为什么？", "什么意思？", "你看懂差别了吗？", and "问题来了" sparingly to reset attention.
- Avoid long paragraph blocks that read like an article.
- Prefer the voiceover-writer posture: first make the judgment clear, then attach evidence and visuals. If a line sounds like a storyboard note, rewrite it as something a creator would say aloud.

Use compact causal links:

```text
这不是停顿。
这是边界。
因为现在继续写，AI 就会开始替你做决定。
```

## Concrete Examples

Every abstract principle needs a visible example.

Examples by concept:

- Misalignment: "帮我做结账页" becomes questions about empty carts, failed coupons, payment states, and order status.
- Vertical slicing: an ecommerce site split into login, cart, and checkout slices, each with database, backend, UI, and tests.
- TDD: "满 1000 减 100" must be written as a failing test before the discount code exists.
- Code smells: Shotgun Surgery is "改一个按钮颜色却要打开十几个文件"; Data Clumps is "姓名、电话、地址总是一起出现"; Feature Envy is "订单逻辑总跑去库存文件里拿数据".
- Deep modules: a house with many rooms but no front door is a shallow module; a simple front door hiding complex rooms is a deep module.
- Configuration scope: user-level rules are personal habits, project-level rules are team standards, nested rules are folder-specific constraints.
- Instruction budget: a long config file is not just "background"; every line forces the model to spend attention deciding whether it applies.
- Maintenance: a config file is a garden; add rules from repeated failures, prune rules made obsolete by stronger models or changed code.

When a source lacks an example, create a clearly labeled illustrative example that does not invent product capabilities.

## Tone

Use confident, creator-style explanation:

- Prefer "这个设计真正厉害的地方是..." over "它还提供了..."
- Prefer "这会把决策权交还给人类" over "它可以提高对齐度"
- Prefer "AI 会在这里开始瞎猜" over "模型可能产生不确定行为"

Keep claims evidence-grounded. Strong language can dramatize implications, but it must not invent stars, download counts, prices, authorship, versions, or usage data.

For tutorial videos, use authority carefully: official docs, release notes, model prompting guides, and observed local behavior can support "latest best practices." Verify current tool behavior before claiming that a command, file name, model, or official recommendation exists.

## Reframing Ending

End by lifting the video above the tool list.

Good endings:

- "Matt 真正开源的，不是几个 skill，而是一套用工程经验驾驭 AI 的方法。"
- "AI 越强，越不是让人类放弃专业判断；恰恰相反，只有你有足够深的领域语言，才真的能控制它。"
- "不要只给 AI 一个任务。给它一套工作方式。"
- "不要把这份文件当成写完就封存的规格书。你的代码在变，模型在变，它也应该跟着变。"

### Closing Interaction

For 解决问题-type scripts (the five-stage frame), the reframe is not the last thing the viewer hears. Add exactly one interaction line after it. The reframe carries the meaning; the interaction line collects the reply. Never let the interaction line replace the reframe, and never stack two of them.

**The interaction line is always a two-option A/B multiple-choice question (选择题). This is fixed — do not choose a form.**

Rationale: a single-letter answer is the lowest-cost reply that still forces a commitment, and picking a side is an identity statement rather than a task, which is what actually produces replies. Open-ended prompts ("留下你的例子") ask the viewer to compose a sentence and expose personal detail for no return, and reliably produce the lowest reply volume.

### Required shape

Ask the question first, then hand over the two labelled options separated by a semicolon, all in one spoken breath.

```text
你更常是哪一种？A，该停的时候停不下来；B，该继续的时候草草收尾。
```

More examples:

```text
你是哪一种？A，任务太大不敢开始；B，明明很小还是拖着。
你更像哪一种？A，环境一乱就写不出来；B，多乱都能照写。
你卡在哪一头？A，想不清楚所以不动；B，想清楚了还是不动。
```

### Rules

- **Exactly two options, labelled A and B.** Never three, never unlabelled, never open-ended.
- **Both options must be equally respectable.** If one option is obviously the "right answer", the question becomes a quiz and nobody picks the other one — which kills the reply volume the format exists for. The viewer should be choosing an identity, not passing a test.
- **The two options must be mutually exclusive and jointly cover the common cases**, so almost every viewer can find themselves in one of them.
- **Prefer reusing the two mirrored cases from 举例.** If 举例 already showed the same mechanism producing opposite failures, those two failures are the ready-made A and B, and the choice lands with no extra setup.
- **Ask about the mechanism just taught**, so answering rehearses the lesson instead of changing the subject.
- **The viewer must be able to answer from their own life at a glance**, with a single letter, without rewatching or expertise.
- **One spoken breath**, and reuse the exact same wording as the end-card screen text.
- Do not substitute 点赞、关注、收藏 requests, and do not settle for "你怎么看" — that is not a question, it is filler.

### Anti-patterns

```text
你觉得这个方法有用吗？A，有用；B，没用。
```
One option is the obvious right answer, so B is dead and nobody replies.

```text
你最近一次「明明可以停，却还是硬做完」的事，是什么？
```
Open-ended: requires composing a sentence and disclosing a real task. Lowest reply volume.

```text
你更倾向哪一种？A，拆解任务；B，降低难度；C，换个时间。
```
Three options, and they are methods rather than identities. The viewer has to evaluate instead of recognise.

```text
你是 A 还是 B？
```
Options were never named. The viewer cannot answer without rewatching.

## Style Match Checklist

Before presenting the narration gate, check:

- Does the first 20 seconds give a clear reason to keep watching?
- For GitHub projects, did you verify current project/author/social-proof signals online before using any numbers?
- Is the video organized around a central mystery or thesis?
- Did you pick the skeleton that matches the subject, and can you point to where each of its stages starts?
- For the five-stage frame: does 解决什么问题 open on a universal pattern before naming examples, does 原理 state its own limits, does 怎么做 stay sequential and short, does 举例 add new scenes instead of recapping, and does 总结 introduce nothing new?
- Does each chapter start from an AI failure mode, not a feature list?
- Is every abstract concept explained with a concrete scene, analogy, or example?
- Are sentences subtitle-friendly and mostly short?
- Does the script escalate from one problem to the next instead of reading a catalog?
- Does the ending reframe the subject into a larger lesson?
- For 解决问题 scripts, does the script close on exactly one interaction line, placed after the reframe rather than instead of it, and is it a two-option A/B 选择题 — question first, two labelled options separated by a semicolon, answerable at a glance with a single letter?
- Are both A and B equally respectable identities rather than one obvious right answer, and do they reuse the two mirrored cases from 举例 where possible?
- Are all numeric/social-proof claims supported by evidence or removed?
- For beginner-to-advanced tutorials, does the script serve both audiences: first-use clarity for beginners and pruning/maintenance judgment for advanced users?
