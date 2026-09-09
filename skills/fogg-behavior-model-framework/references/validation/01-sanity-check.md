# Phase 4.1 已知测试：公开立场 sanity check

- 测试日期：2026-09-07
- 测试对象：`fogg-behavior-model-framework/SKILL.md`
- 测试方法：只读取 `SKILL.md` 并做三道已知问题干跑；没有读取 `references/research/07-synthesis.md` 或 `08-synthesis-review.md`，以避免复述综合稿自评。
- 对照口径：本报告只判断 Skill 是否忠实路由、是否与 BJ Fogg / *Tiny Habits* 的公开立场同向，以及证据收缩是否合理；不把作者官网、著作或访谈本身当成独立效果验证。
- 总结判定：**PASS（有 3 项非阻断性偏差/术语风险）**。

## 测试 1：高动机、低摩擦，但行为仍未发生

### 测试问题

某人非常想在每天 17:00 提交一份只需约一分钟完成的日报，工具、权限和技能也都具备，但当天仍没有提交。按照本 Skill 应如何诊断？能否直接断言是“不够自律”？

### Skill 按协议应给的核心回答

1. 先把目标锁定为：“该主体在当天 17:00 提交日报”，而不是抽象的“更负责”。
2. 用模型 1 做时点诊断：动机高是当前已知；“只需一分钟且工具可用”支持 Ability 较高，但仍要核对当天的真实时点；Prompt 是否在 17:00 出现、被注意、且明确指向“现在提交”仍待核。
3. 由于 M、A 看起来充足，首要假设是 Prompt 缺失或失效，而不是人格/意志力缺陷。首个单变量试验应是放置一个适时、可见、当时可执行的提示，例如在关机动作前出现提交入口。
4. 观察提示注意率与提示后提交率。若提示确实出现并被注意却仍不提交，再重新检查真实 Ability（表单内容是否仍需搜索、是否被会议打断）和对这个具体动作的 Motivation。
5. 不把 B=MAP 当成可计算公式，也不因一次事后解释就声称找到了唯一原因。

### 公开立场 / 来源

- BJ Fogg 的官方 Behavior Model 页面明确写道：行为发生要求 Motivation、Ability、Prompt 在同一时刻汇合；行为未发生时，三者至少缺一项。  
  来源（作者官方材料，证据层级 C，用于确认“Fogg 主张什么”）：https://www.behaviormodel.org/
- 官方 Prompt 页面明确写道：“Without a Prompt, the target behavior will not happen”，并把高 Motivation、高 Ability 情境下的适配提示称为 Signal。  
  来源（作者官方材料，C）：https://www.behaviormodel.org/prompts
- Fogg 对公开排障顺序的表述是先查 Prompt、再查 Ability、最后查 Motivation；公开报道对该顺序有直接引述。  
  来源（作者公开教学的媒体转述，C/D）：https://www.businessinsider.com/steps-to-troubleshoot-bad-behavior-design-stanford

### 方向是否一致

**一致。** Skill 的模型 1、Step 3 与 H2 都会先查 Prompt，再查 Ability，最后才碰 Motivation；这正好能通过本题的已知答案。它没有把“高动机 + 容易”误写成行为必然发生，因为 Prompt 仍是必要构件。

### 是否因证据纪律做了合理收缩

**是。** 官方页面把 FBM 表述为普适模型，而 Skill 只把完整 MAP 结构列为作者模型/实践证据 C，把行动线形状和普适性降为 D；同时要求区分已知、推断、待观察，不允许算概率或循环解释。该收缩不改变本题的操作方向，且避免把作者的强普适主张冒充独立验证事实。

## 测试 2：建立牙线 / 微小健康习惯

### 测试问题

一个愿意改善口腔护理、会刷牙但一直没有稳定使用牙线的人，怎样按本 Skill 建立一个微小健康习惯？

### Skill 按协议应给的核心回答

1. 主路由为模型 2 → 3 → 4 → 5：先确认这是本人想做且现实可行的具体行为，不把“口腔更健康”直接当作 Behavior。
2. 将最低行为缩为安全 Tiny Behavior：“清洁一颗牙”。它是启动与自动性训练基线，不等于已经完成足量口腔护理。
3. 选择同地点、同频率、同主题的稳定 Action Prompt，并尽量收紧到前序动作的末端，例如：“在我刷完牙并把牙刷放回杯中之后，我会用牙线清洁一颗牙。”
4. 可选一个真实、即时、非控制性的积极反馈，如点头或心中确认；如果尴尬、虚假或无帮助，就删除或更换。
5. 短期观察是否想起、是否执行、实际清洁牙数、是否逐渐自动，以及疼痛/出血等停止或求助信号。只有本人自然想加量且功能指标改善时才小幅扩展，低状态日仍保留安全基线。

### 公开立场 / 来源

- Tiny Habits 官方页面给出的原配方就是：“After I brush my teeth, I will floss one tooth.” 并说明 Anchor 应与新行为在频率、地点和主题上匹配。  
  来源（作者官方方法材料，C）：https://tinyhabits.com/good-spot/
- 官方 “Start Tiny” 页面说明 Fogg 把完整牙线行为缩为一颗牙，先形成自动性，后来才扩展到所有牙；同时区分 Starter Step 与 Tiny Version。  
  来源（作者官方方法材料，C）：https://tinyhabits.com/start-tiny/
- 官方 “Rewire Your Brain” 页面要求在清洁一颗牙后立即 Celebration，并以照镜子微笑、说 “Good for me!” 为例；页面还主张积极情绪会更快“wire”习惯。  
  来源（作者官方方法材料，C）：https://tinyhabits.com/rewire/

### 方向是否一致

**一致，但有一处有意降格。** “刷牙后 → 一颗牙”的 Anchor + Tiny Behavior 与 Fogg 的公开范例直接一致；Skill 把 Anchor 收紧到可感知的最后动作，也与其时序设计方向一致。差别在 Celebration：Fogg 的公开教学把它称为关键技能，Skill 则把它处理为可选积极反馈。

### 是否因证据纪律做了合理收缩

**是，而且是必要收缩。**

- Skill 没有复述“情绪创造习惯”“越强烈就越快重连大脑”等未经独立组件试验充分支持的因果强断言。
- Skill 明确说即时自我庆祝对自动性的独立增益证据弱，稳定情境中的重复与自动性增长证据更强，因此把 Celebration 降为可选放大器。
- Skill 不把清洁一颗牙等同于足量健康行为，也不保证它会自然长成完整护理；这是对健康剂量与功能结果的合理保护。

该处理不是对“原版 Tiny Habits 协议”的逐字忠实复现，但 Skill 已明确把“作者主张”与“独立证据”分开，因此属于透明、合理的证据约束版本，不构成方向性失败。

## 测试 3：处理不想要的手机行为

### 测试问题

某人工作时一看到社交媒体通知就会打开 App 并连续刷很久，想减少这一行为。按照本 Skill，应该先靠意志力克制、直接写一个 Tiny Habits 配方，还是用别的路由？

### Skill 按协议应给的核心回答

1. 先做风险分级。若是普通、非临床的不想要行为，进入模型 6；若存在严重成瘾、显著功能损害、躁狂、危机或其他临床信号，停止普通习惯自助解释并升级支持。
2. 不处理“少玩手机”这个概括标签，而拆成具体行为结，例如：“工作时看见社交媒体通知后，点开 App”与“一个视频结束后继续上滑”。
3. 先选最容易解开的具体结，并优先处理 Prompt：先测试关闭通知、工作时开启勿扰，或移除会触发点开的上下文线索。
4. 如果 Prompt 无法充分移除，再增加旧行为摩擦、降低其 Ability，例如把 App 移出首页、退出自动登录或卸载；最后才考虑 Motivation 或设计一个本人更想做、更易做的替代行为。
5. 每轮只改一个主要变量，记录提示后是否点开、使用次数/时长及负担。不能用羞辱、罚款、不可退出监控等方式“增摩擦”。

### 公开立场 / 来源

- *Popular Science* 公开刊载的内容明确标注为“excerpt adapted from Tiny Habits by BJ Fogg”。节选把过多屏幕时间/不健康饮食拆成多个具体习惯结，要求先选最容易的一结；随后按 Prompt → Ability → Motivation 的顺序逆向设计。
- 同一节选明确列出对 Prompt 的三种处理：remove、avoid、ignore；其中 remove 最简单，ignore 长期依赖意志力、通常不是最佳方案。
- 手机例子是工作时关闭社交媒体通知、开飞行模式、关机或移除 App；若仍不够，再通过复杂密码、不保存登录等方式增加时间/脑力摩擦。饮食例子包括不把冰淇淋带回家、避开会出现甜点提示的咖啡店。
- 节选也明确区分普通 Downhill Habits 与可能需要专业帮助的 Freefall Habits，并说明 Tiny Habits 不是严重成瘾的答案。  
  来源（Fogg 著作公开节选，作者立场 C）：https://www.popsci.com/story/science/tiny-habits-change/
- Fogg 的公开访谈也直接说，不想要行为不是一次“break”，而要逐结 “untangle”；移除 M、A 或 P 都可阻止行为。  
  来源（含 Fogg 逐字访谈的公开页面，C）：https://www.jordanharbinger.com/bj-fogg-tiny-habits-that-change-everything/

### 方向是否一致

**一致。** Skill 准确保留了“拆具体行为结 → 先 Prompt → 再让旧行为更难 → 最后处理 Motivation”的公开顺序，也没有把建立新习惯的 ABC 配方机械倒放成终止坏习惯的方法。手机通知与移除 App 的案例与公开节选几乎是一一对应的已知答案。

### 是否因证据纪律做了合理收缩

**是。**

- 公开节选写“my research shows there is an optimal order”，但 Skill 没有把该顺序包装为已获强独立验证的最优定律，而把逆向 MAP 列为 C，把刺激控制/增摩擦的邻近方向列为 B。
- Skill 在作者原有 Freefall/专业帮助边界上进一步明确了成瘾、进食障碍、危机、权力和零容忍安全情境的升级条件。
- Skill 限制罚款、羞辱与强制监控，避免把 Fogg 节选中“增加金钱成本”的例子无条件扩展到儿童、员工或脆弱主体。

这些收缩保留了公开方法的方向，同时降低了临床越界和伦理误用风险。

## 六模型路由冲突检查

### 结论

**未发现会让三道已知题得到相反答案的硬冲突。** 六模型整体是分层协作，而非六套竞争理论：

- 模型 1 诊断某一时点的一次行为是否发生；
- 模型 2 把愿望/成果转成具体且匹配的行为；
- 模型 3 处理 Ability/摩擦与缩小行为；
- 模型 4 处理 Prompt/锚点及时序；
- 模型 5 仅在需要重复时组装 Tiny Habits 学习配方；
- 模型 6 负责失败迭代、不想要行为的逆向解结及风险升级。

### 两处轻微路由重叠

1. **模型 1 与模型 6 都包含普通新行为失败的 P→A→M 排障。** Step 1 指示“行为没有发生”先走模型 1，但模型 6 的运行步骤 3 又处理“普通新行为失败”。这不是答案冲突，两处顺序相同；不过模型 6 到底是所有失败的治理外壳，还是只是不想要行为/高风险升级的主路由，文本可再明确。
2. **模型 2 的行为集群包含“停止/替换行为”，而 Step 1 又规定不想要行为主路由为模型 6。** 两者可以解释为模型 2 提供候选生成、模型 6 提供逆向排障与安全治理，但当前交接关系没有显式写出。

这两项属于职责边界轻微重叠，不构成 Phase 4.1 失败。

## B=MAP 与 Tiny Habits 混淆检查

### 结论

**没有错误混淆。**

Skill 做了以下关键区分：

1. 开头明确写出 `B=MAP ≠ Behavior Design ≠ Tiny Habits ≠ Behavior Change System`。
2. B=MAP 被限定为“某主体在某时点的具体行为是否发生”的诊断启发式，不负责证明长期自动性、剂量或成果。
3. Tiny Habits 只在行为已匹配、已安全缩小且需要重复时启用；ABC 配方没有被写成 B=MAP 的替代公式。
4. Anchor 被正确定位为 Action Prompt 的一种，不是所有 Prompt；Tiny Behavior 主要提高 Ability；Celebration 发生在行为之后，因此不是触发该次行为的 MAP 构件。
5. Skill 明确区分一次行为、重复、自动性与功能成果，避免用“一次清洁一颗牙”证明完整健康结果。

### 一个术语风险

Skill 使用大写 **Behavior Change System** 作为扩展流程名称，而 Fogg 在公开的 *Tiny Habits* 节选中使用的是 **Behavior Change Masterplan**。Skill 的定义内容与公开 Masterplan 大体同向，但 “Behavior Change System” 容易被读者误认为 Fogg 的正式专名。此处是命名/归属风险，不是 B=MAP 与 Tiny Habits 的机制混淆。

## 最终判定

**PASS**

三道已知题均与 BJ Fogg / *Tiny Habits* 的公开立场方向一致：

1. 高 M、高 A 仍未行动时，优先核对 Prompt；
2. 牙线习惯采用“刷牙后清洁一颗牙”的 Anchor + Tiny Behavior；
3. 不想要的手机/饮食行为先拆结，再按 Prompt → Ability → Motivation 逆向处理。

### 具体偏差

1. **Celebration 强度偏差（合理收缩）**：Fogg 公开材料把 Celebration 视为 Tiny Habits 的关键，Skill 将其降为可选反馈。该偏差有明确证据纪律支撑，且已透明标注，不判 FAIL。
2. **模型 1 / 模型 6 与模型 2 / 模型 6 的职责轻微重叠（结构性小偏差）**：不导致相反建议，但可能让执行者不清楚何时从局部诊断切到治理/升级层。
3. **Behavior Change System 命名偏差（术语风险）**：公开作者材料使用 Behavior Change Masterplan；当前名称应理解为 Skill 自己的安全扩展层，不宜无说明地归为 Fogg 的正式框架名。

未发现以下阻断性问题：把 B=MAP 写成乘法或概率公式、把 ABC 当作 B=MAP、用微行为替代足量治疗/健康剂量、让 Motivation 优先于 Prompt/Ability、或用 Tiny Habits 自助替代严重成瘾/临床支持。
