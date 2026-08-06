# Popular Knowledge Script Style

Use this reference when the user asks for a knowledge-sharing video, YouTube-style explainer, viral breakdown, creator-style narration, or provides an SRT/reference script with a high-retention educational tone. Treat the reference as a writing grammar, not a factual source.

## Core Shape

A popular knowledge script should feel like a guided teardown, not a repository tour or README summary.

When this reference is used inside Knowledge Video Builder, treat narration quality as the first draft target. Write the complete voiceover so it can stand alone as a good spoken script before turning it into storyboard, screen text, and scene-plan data. The production artifacts should preserve the voiceover's hook, rhythm, examples, and ending instead of making the narration serve a visual checklist.

Default teardown structure:

1. Open with social proof, current relevance, or a sharp contradiction.
2. Name the central mystery: what does this tool reveal, solve, or control?
3. State the video route in plain language.
4. For each chapter, start from the failure mode or common misconception.
5. Introduce the tool/rule as the mechanism that prevents that failure.
6. Explain the underlying principle with a concrete example.
7. Escalate to the next problem created by the previous solution.
8. End by reframing the subject into a larger lesson.

For "from beginner to mastery" tutorials, use a learning ladder instead of a teardown:

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

## Style Match Checklist

Before presenting the narration gate, check:

- Does the first 20 seconds give a clear reason to keep watching?
- For GitHub projects, did you verify current project/author/social-proof signals online before using any numbers?
- Is the video organized around a central mystery or thesis?
- Does each chapter start from an AI failure mode, not a feature list?
- Is every abstract concept explained with a concrete scene, analogy, or example?
- Are sentences subtitle-friendly and mostly short?
- Does the script escalate from one problem to the next instead of reading a catalog?
- Does the ending reframe the subject into a larger lesson?
- Are all numeric/social-proof claims supported by evidence or removed?
- For beginner-to-advanced tutorials, does the script serve both audiences: first-use clarity for beginners and pruning/maintenance judgment for advanced users?
