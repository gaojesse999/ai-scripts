# 维度 6：理论时间线、智识谱系与最新动态

> 研究对象：BJ Fogg 的 Fogg Behavior Model（FBM）、Fogg Behavior Design 与 Tiny Habits  
> 截止日期：2026-09-07  
> 主语料：简体中文版《福格行为模型》（英文原书 *Tiny Habits*）全文 OCR  
> 本文是研究底稿，不是最终 `SKILL.md`。

## 0. 证据标记与结论边界

- **[事实]**：由原始论文、正式书目、出版社或可交叉核实的机构记录支持。
- **[作者自述]**：来自 Fogg 本人、其官网或其团队；可用于还原创作史，但不能自动视为独立验证。
- **[谱系推断]**：概念上存在可说明的承继或平行关系，但没有找到作者明确承认的直接影响证据。
- **可信度 A（高）**：同行评审原文、ACM/Springer/APA 等正式书目、出版社或 Stanford 官方记录。
- **可信度 B（中高）**：作者官网、自序、演讲或项目官网；对“作者如何叙述自己”很强，对普适有效性较弱。
- **可信度 C（中）**：可靠媒体、其他作者的直接陈述或二手书目；只用于交叉核对和影响史。

### 一句话总论

FBM 的核心不是“养成习惯公式”，而是一个**瞬时行为发生诊断模型**：当动机、能力和一个当下提示同时越过阈值时，目标行为发生。Tiny Habits 是 2011 年后建立在 FBM 上的**纵向习惯设计方法**，新增行为匹配、把行为缩小、锚点和即时庆祝。把二者合并成一个自 2007 年起就完整存在的理论，会抹掉重要的版本演化。

---

## 1. 压缩时间线

### 1.1 前史：说服、强化、能力与“意图—行动鸿沟”

#### 约公元前 4 世纪：亚里士多德《修辞学》

- **[作者自述]** Fogg 说自己约 35 年前在法国阅读法文版 Aristotle 的 *Rhetoric* 时意识到：计算机终将执行传统修辞所描述的说服功能；这一顿悟促使他研究 persuasive technology。[S08]
- **边界**：这是**研究议程的灵感来源**，不是 B=MAT/B=MAP 三构件的结构来源。没有证据表明亚里士多德直接给出了 Motivation–Ability–Prompt。
- **来源日期/可信度**：作者官网，无页面发布日期，检索于 2026-09-07；B。

#### 1938–1953：操作性条件作用与强化

- **[事实]** Skinner 的操作性条件作用传统把“行为后果改变行为未来概率”置于核心位置；1953 年的表述明确把后果与未来发生概率联系起来。[S27]
- **[谱系推断]** Tiny Habits 的“行为后立即庆祝，让积极情绪提高再次发生概率”与强化传统结构同源；但 Fogg 把主观“成功感/shine”置于特殊位置，并声称情绪而非重复创造习惯。这是应用性重述，不等于 Skinner 理论的直接推导。
- **来源日期/可信度**：1938、1953 原著及行为分析史回顾；A。

#### 1955：Ripple 的 Motivation–Capacity–Opportunity

- **[事实]** Lilian Ripple 在 *Social Service Review* 发表 “Motivation, Capacity, and Opportunity as Related to the Use of Casework Service”。[S18]
- **[作者自述]** Fogg 官网称这是他能找到的最早三元人类行为模型，但强调 Ripple 的术语定义与 FBM 不同。[S05]
- **[谱系推断]** 它是**词汇近邻和历史平行项**，不是已证实的直接祖先。尤其 Opportunity 与 Prompt 不同，Capacity 也不等同于 Fogg 的“在此刻做起来多容易”。
- **来源日期/可信度**：1955-06-01 同行评审论文 + 作者官网；A/B。

#### 1977：Bandura 自我效能

- **[事实]** Bandura 提出 self-efficacy 会影响行为是否启动、投入多少努力及面对阻碍时持续多久。[S19]
- **[谱系推断]** 它与 FBM 的 Ability 邻近，但不等价：自我效能是“我相信自己能做”的判断；FBM 的 Ability 在 2009 版主要被操作化为时间、金钱、体力、脑力、社会偏离和非日常性等“简易度资源”。
- **来源日期/可信度**：1977-03，*Psychological Review*；A。

#### 1985/2000：Self-Determination Theory（SDT）

- **[事实]** Deci 与 Ryan 区分内在/外在动机，并进一步区分外在动机的自主化程度，强调自主、胜任和关系需要。[S20]
- **[作者立场]** 2020 书中 Fogg 明说自己认为“内在/外在”区分在现实设计中用处不大，改用 Person–Action–Context 三种动机来源。[S01]
- **意义**：SDT 显示 FBM 的 Motivation 是刻意简化的设计变量，并没有覆盖动机质量、内化或自主性。
- **来源日期/可信度**：1985 专著传统、2000-01 综述；A；Fogg 的评价为 B。

#### 1991：计划行为理论（TPB）

- **[事实]** Ajzen 的 TPB 用态度、主观规范、知觉行为控制预测意图，再由意图与知觉控制解释行为。[S21]
- **[谱系推断]** TPB 适合预测“为什么想做”，FBM 更适合诊断“为什么此刻没做”。FBM 把 prompt 单列，正是在设计层面对意图—行动断裂的处理，但它没有 TPB 那样成熟的测量传统。
- **来源日期/可信度**：1991-12，*Organizational Behavior and Human Decision Processes*；A。

#### 1999：Implementation Intentions

- **[事实]** Gollwitzer 的 implementation intention 用 “Whenever situation X arises, I will initiate response Y” 把情境线索绑定到行动，使行动可被线索自动触发。[S22]
- **[谱系推断]** Tiny Habits 配方 “After I [Anchor], I will [Tiny Behavior]” 是它的高度相似变体：把 if/when 改成 after，把线索优先设为已有日常行为，并加上庆祝。2022 年 Tiny Habits RCT 论文也明确把 Recipe 解释为一种 implementation intention。[S34]
- **来源日期/可信度**：1999-07-01，*American Psychologist*；A。

### 1.2 Captology 阶段：从社会心理学到可设计的数字说服

#### 1997：博士论文、Captology 命名与 CHI 公开

- **[事实]** Fogg 的 Stanford 博士论文为 *Charismatic Computers: Creating More Likable and Persuasive Interactive Technologies by Leveraging Principles from Social Psychology*；研究沿用 Computers Are Social Actors（CASA）范式，实验计算机奉承、队友关系和互惠等社会心理原则。[S09]
- **[事实]** CHI 1997 extended abstract 已出现 “Captology: The Study of Computers as Persuasive Technologies”；Fogg 的论文获 Stanford Maccoby Prize。[S08][S10]
- **[谱系结论]** FBM 的直接学术土壤不是一般“习惯学”，而是 Stanford 的**社会心理学 × 人机交互 × 说服设计**传统。Fogg 列出的导师包括 Clifford Nass、Byron Reeves、Terry Winograd、Philip Zimbardo。[S08]
- **来源日期/可信度**：1997 学位论文/CHI 记录/作者履历；A/B。

#### 1998：Persuasive Computers 与 Functional Triad

- **[事实]** CHI 1998 论文定义 persuasive computer 为“有意图改变人的态度或行为”的交互技术，提出：
  1. 三种继承意图（endogenous / exogenous / autogenous）；
  2. Functional Triad（计算机作为 tool、medium、social actor）；
  3. 分析层级、设计空间和伦理问题。[S10]
- **[事实]** 论文已明确提醒：技术的说服意图可能被遮蔽，设计者与研究者承担伦理责任。
- **版本冲突**：Fogg 当前官网称实验室 1998 年创立；Stanford Lifestyle Medicine 的人物稿称 2000 年启动实验室。[S08][S07] 没有进一步档案足以消解，保留为 **1998/2000**。
- **来源日期/可信度**：1998-04 CHI 同行评审论文；A。实验室日期为 B/A（机构页面互冲突）。

#### 2002/2003：*Persuasive Technology*

- **[事实]** Morgan Kaufmann/Elsevier 官方页同时出现 “1st Edition – December 16, 2002” 与 “Published: January 4, 2003”；ISBN 978-1-55860-643-2。[S11]
- **[概念作用]** 专著系统化 captology、Functional Triad 与工具/媒介/社会行动者的说服原则，重点仍是**计算机如何改变态度和行为**，尚不是后来通用的人类行为模型。
- **版本冲突**：参考文献常写 Fogg 2003；作者与部分出版社页面写 2002。最稳妥写法是“2002 年末出版、2003 年进入流通/常见引文年”。
- **来源日期/可信度**：官方出版社；A。

#### 2007：移动说服、Facebook 课程与 FBM 的作者认定诞生年

- **[事实]** Fogg 与 Dean Eckles 编 *Mobile Persuasion: 20 Perspectives on the Future of Behavior Change*，由 Stanford Captology Media 出版，说明研究从桌面说服转向移动设备的及时触发和健康行为。[S12]
- **[作者自述]** Fogg 说自己在 2006 或 2007 年先使用 “hot trigger”，并在 2007 年“解开行为谜题”、命名 Fogg Behavior Model。[S01][S06]
- **[事实]** 2007 年 Stanford “Facebook Class”让约 75 名学生创建 31 个应用；Stanford Magazine 报道这些应用 10 周触达 1600 万用户。[S28]
- **边界**：
  - 2007 是作者回溯认定的“发现年”，现有最强同时代正式文本仍是 2009 论文。
  - Facebook 课程证明 Fogg 的说服设计教学对产品实践有扩散力，但不能证明 1600 万用户由尚未正式发表的 FBM 单独导致。
  - 中文版自序写“不到 6 个月、超过 2400 万人”；与 Stanford Magazine 的“10 周、1600 万”口径不同，应并列保留，不混算。[S01][S28]
- **来源日期/可信度**：2007 书目与 2011 Stanford 校刊回顾为 A/C；“模型发现”是 B。

### 1.3 FBM 正式化与 Behavior Design 工具体系

#### 2009-04-26：FBM 首次可核实正式发表

- **[事实]** PERSUASIVE 2009 论文 *A Behavior Model for Persuasive Design* 正式发表，DOI 10.1145/1541948.1541999。[S02]
- **2009 版构件**：
  - Behavior 发生要求 Motivation、Ability、Trigger 在**同一时刻**同时存在；
  - Motivation 与 Ability 存在补偿关系；
  - 有一条 curved “behavior activation threshold”；
  - Motivation 三对：pleasure/pain、hope/fear、social acceptance/rejection；
  - Ability/Simplicity 六因素：time、money、physical effort、brain cycles、social deviance、non-routine；
  - Trigger 三类：spark（补动机）、facilitator（补能力）、signal（只提醒）。[S02]
- **[事实]** 原文明确说纵横轴“没有单位”，模型是概念关系图，并称论文是 early way to share ideas，内容仍会演化。
- **关键边界**：论文把 FBM 定位为设计分析框架，不是已给出量表、参数和可证伪方程的数学模型；“B=MAT”是助记写法，不应读成数值乘法。
- **来源日期/可信度**：ACM 同行评审会议论文；A。

#### 2009：Behavior Grid 35 类

- **[事实]** 同届会议论文 *The Behavior Grid: 35 Ways Behavior Can Change* 将行为改变按两个维度分成 35 类，示例映射 Facebook 目标。[S13]
- **[版本演化]** Stanford 当前页面明确说 35 类方案“有弱点”，后来 15 类网格更好。[S13]
- **意义**：FBM 解释行为发生条件；Behavior Grid 先规定“你究竟想改变哪一类行为”。这标志理论由单模型走向设计工具链。
- **来源日期/可信度**：2009-04-26 ACM 论文 + Stanford 官方说明；A。

#### 2009–2010：从 Persuasive Technology 转向 Behavior Design

- **[作者自述/机构自述]** Fogg 官网说 2009 年研究兴趣从 persuasive technology 转向一般人类行为、尤其健康习惯；中文版序说 2010 年他与 Stanford 同事把新领域命名为 Behavior Design。[S06][S01]
- **[机构自述]** Stanford 实验室页则说“2009 年开始创建新的 behavior change 设计方式”。[S07]
- **结论**：将 **2009 视为转向起点、2010 视为命名年**最能兼容三份材料。
- **来源日期/可信度**：作者/机构官网与原书；B。

#### 2010：Behavior Wizard 与 15 类 Grid

- **[事实]** Fogg 与 Jason Hreha 在 PERSUASIVE 2010 发表 *Behavior Wizard: A Method for Matching Target Behaviors with Solutions*；先把目标分入 15 类，再匹配 trigger、理论与技巧。[S14]
- **[版本演化]** 15 类替代 35 类，说明“目标行为分类”本身也处于快速迭代，不能把 2009 Grid 当最终版。
- **来源日期/可信度**：2010-06-07/10 Springer LNCS 会议论文；A。

#### 约 2009–2010：Focus Mapping、Swarm of Behaviors、Golden Behavior

- **[作者自述]** 2020 原书称 Focus Mapping 是“10 年前”在 Stanford 早期研究中创建并持续改进；据此只能约定为 2009–2010，不能给出精确首发日。[S01]
- **[方法演化]** Behavior Design 逐步形成：
  1. 明确 aspiration/outcome；
  2. 生成 Swarm of Behaviors；
  3. 以影响力和可行性做 Focus Mapping；
  4. 选 Golden Behaviors；
  5. 再用 FBM 让行为容易并给出合适提示。
- **边界**：没有找到与 2009 FBM 同等强度的首发论文，年代主要依赖回忆性自述。
- **来源日期/可信度**：2020 原书；B。

### 1.4 Tiny Habits 阶段：从一次行为到习惯形成方法

#### 2011：实验室改名与 Tiny Habits 诞生

- **[作者自述]** Fogg 说 2011 年初从“每天只用牙线清洁一颗牙”开始试验微小行为；2011 年 12 月向约 60 人运行第一期免费 5 日邮件项目，下一周约 150 人，并持续迭代说明。[S15]
- **[作者/机构自述]** Persuasive Technology Lab 于 2011 年改名 Behavior Design Lab，以匹配研究方向。[S08]
- **Tiny Habits 初版结构**：
  - 选 3 个极小行为；
  - 绑定既有日常行为；
  - 周一至周五签到与教练反馈；
  - 通过做成小事学习“如何创建习惯”。[S15]
- **关键区分**：即时庆祝后来成为书中显著的 C，但 2011 首批项目公开史料更清楚地证明“小行为 + 锚点 + 反馈”；无法从现有材料证明 2011 首周就已有 2020 书中全部 ABC 术语。
- **来源日期/可信度**：Fogg 2014 年第一人称回顾、作者官网；B。

#### 2012-03-26：Motivation Wave 公开演讲

- **[事实/作者自述]** Fogg 在 Boston 健康会议 keynote 公开 “Motivation Wave”：动机高涨时完成难事或一次性环境配置，动机回落后只依靠容易行为。[S16]
- **意义**：这把 2009 版 Motivation–Ability 补偿关系转为时间维度上的实践启发式。
- **来源日期/可信度**：作者官网与演讲视频说明；B。

#### 2012：大众习惯模型并行扩散

- **[事实]** Charles Duhigg 的 *The Power of Habit* 普及 cue–routine–reward “habit loop”。[S29]
- **[谱系推断]** 它与 Tiny Habits 的 anchor–behavior–celebration 表面相似，但来源和主张不同：Duhigg 强调循环、渴求和奖励；Fogg 强调行为要足够小、行动提示与即时成功感。没有证据表明任一框架由另一框架直接派生。
- **来源日期/可信度**：2012-02 出版书目；A/C。

#### 2013–2014：从 Tiny Habits 到 *Hooked*

- **[作者自述]** Fogg 的中文版序称 James Clear 于 2013 年发现免费 Tiny Habits 课程并来信。[S01]
- **[事实]** Nir Eyal 的 *Hooked*（2013 自出版、2014-11-04 Portfolio 版）在 Action 阶段直接采用旧版 B=MAT，配套 workbook 也列出 Fogg 的动机、简易度和 trigger 分类。[S30][S31]
- **影响判断**：
  - **直接影响，证据强**：Eyal 本人网站明确称 FBM 是 behavior-tech 常用模型，且其 workbook 明列 Fogg。
  - Hook Model 增加 variable reward 与 investment，解释循环使用；它不是 FBM 的同义重写。
- **来源日期/可信度**：Eyal 官方材料 + Penguin Random House 书目；A/B。

#### 2017 年末：Trigger 改为 Prompt，B=MAT → B=MAP

- **[作者自述]** Fogg 官方 Prompt 页明确说在 **late 2017** 把 Trigger 改为 Prompt。[S04]
- **改名理由（中文版序）**：
  1. trigger 在英语中逐渐带有创伤/负面触发含义；
  2. 人们容易把 trigger 误认为“制造动机”，而第三构件本意只是“现在做”。[S01]
- **版本结论**：这是术语修订，不是三构件机制被重做。引用 2009 论文时必须保留 Trigger；描述当前模型时用 Prompt。
- **来源日期/可信度**：作者官网 + 2021 中文版序；B。

#### 2017：Growth Hacking 吸收旧版 FBM

- **[作者自述]** 中文版序说《增长黑客》引用其部分研究。[S01]
- **[二手核对]** *Hacking Growth* 的概述材料出现 motivation–ability–trigger 与 Hook Model，用于 acquisition/activation/retention 的实验设计。[S32]
- **边界**：未取得该书可核对页码或作者官网原文，因此“直接影响”可信度低于 *Hooked* 和 *Atomic Habits*，记为 C，不把它作为核心证据。

#### 2018：*Atomic Habits* 吸收 anchoring/tiny behavior

- **[事实]** *Atomic Habits* 于 2018-10-16 由 Avery 出版。[S25]
- **[直接影响]** James Clear 官网明确：
  - Tiny Habits “originally laid out many of the steps”；
  - “habit stacking”来自 Fogg 的 anchoring；
  - 他采用“正确的小行为 + 正确排序，不依靠提高动机”的思路。[S46]
- **概念再命名**：Fogg 的 anchor/anchoring → Clear 的 habit stacking。Clear 的 Four Laws 仍是自己的综合框架。
- **争议**：Fogg 认可 Clear 受其启发，但批评 *Atomic Habits* 忽略情绪的核心作用并过分强调重复。[S01] 这是原作者评价，不是已裁决的科学结论。
- **来源日期/可信度**：作者官网、出版社与 Fogg 原书；A/B。

#### 2019：首次较直接的公共健康构件检验

- **[事实]** Agha 等用 617 名巴基斯坦已婚男性的两轮 panel survey 检验安全套使用：高 Motivation + 高 Ability 组的使用 odds 约为低低组 34 倍，方向符合 FBM；prompt 的关联通过 M/A 运作。[S35]
- **边界**：这是观察性/准纵向模型应用，不是随机操纵 M、A、P 并验证 action line 形状；因此支持“构件相关方向”，不能证明 FBM 全部因果主张。
- **来源日期/可信度**：2019，*Journal of Health Communication*；A。

#### 2019-12-31 / 2020-01：*Tiny Habits* 出版

- **[事实]** Penguin UK 的电子版日期是 2019-12-31；美国版书目也常列 2019-12-31。Fogg 官网把发布叙述为 2020-01，书内版权为 ©2020。[S17][S01][S06]
- **[版本结论]** 可写“2019 年末首发，2020 年全面发行/版权年”，不要二选一抹掉版本差异。
- **2020 书把分散工具首次整合为完整 Behavior Design 系统**：
  - B=MAP 与 action line；
  - Behavior Matching / Swarm / Focus Map / Golden Behavior；
  - Tiny Habits ABC：Anchor–Behavior–Celebration；
  - Prompt PAC：Person–Action–Context；
  - Ability Chain；
  - Shine、Spectrum of Automaticity；
  - 好/坏习惯与群体行为设计。[S01]
- **来源日期/可信度**：出版社与原书；A。

#### 2021-10：简体中文版《福格行为模型》

- **[事实]** 天津科学技术出版社于 2021-10 出版简体中文版，徐毅译，ISBN 9787557696672；主语料版权页可直接确认。[S01]
- **重要翻译/定位变化**：
  - 英文题名突出 *Tiny Habits*；
  - 中文题名突出“福格行为模型”，更容易让读者误以为全书所有习惯方法都属于 2009 FBM 本体；
  - 中文版序是独有的重要版本史材料，明确解释 B=MAT → B=MAP、2007 发现年、2010 “Behavior Design”命名及作者对后继习惯书的评价。[S01]
- **来源日期/可信度**：书内版权页和中文版序；A/B。

#### 2021：Stanford 机构归属变化

- **[机构事实]** Behavior Design Lab 页面称 2021 年初迁至 Stanford Flourishing Project 下的 Division of Health and Human Performance，隶属 Stanford Medicine 与 Vaden Health Services。[S07]
- **后续页面漂移**：Fogg 当前个人页又称 Stanford home 是 Stanford Lifestyle Medicine；Lifestyle Medicine 简介称其为 Research and Implementation Specialist、Stanford Living Education Adjunct Professor。[S06][S39]
- **结论**：可确认方向从 HCI/说服技术持续转向 health/flourishing，但当前职衔与组织挂靠在不同官方页面上并不完全同步。
- **来源日期/可信度**：Stanford/作者官方页面；A/B。

### 1.5 2022–2026：开始被测量，但仍以应用性证据为主

#### 2022：跨行为关联研究

- **[事实]** Agha 等在 Nigeria、Pakistan、India 的四类行为中发现，高 M + 高 A 与疫苗、安全套、铁叶酸、现代避孕采用显著相关，odds 约为低低组的 8–35 倍。[S33]
- **作者自己的限制**：论文结论明确要求用实验或准实验数据进一步严格检验 FBM。
- **来源日期/可信度**：2022-08，*Vaccines*；A。

#### 2022：Tiny Habits for Gratitude RCT

- **[事实]** 154 名成人随机分入 gratitude Tiny Habits、一般 Tiny Habits、inactive control。干预后两个 Tiny Habits 组的 gratitude 均优于 inactive control；1 个月时 gratitude 特定组仍优于 inactive control。[S34]
- **能说明什么**：5 日项目/Recipe 可作为短期行为干预载体。
- **不能说明什么**：
  - 两个活跃组都含 Anchor、Tiny Behavior、Celebration，研究没有单独随机“庆祝 vs 不庆祝”；
  - 因而不能验证“庆祝是习惯形成的独立因果机制”；
  - 主要结局是自报 gratitude，不是长期自动性或全套 FBM action line。
- **来源日期/可信度**：2022-05-30，*Frontiers in Public Health*；A。

#### 2023：AI 时代的说服伦理重新升温

- **[事实]** 2023 年同行评审论文把 persuasive technology 延伸到 computational manipulation / hypernudging，指出 AI 画像和个性化可隐蔽利用认知弱点、损害 mental self-determination。[S38]
- **[谱系结论]** 这不是 FBM 的模型升级，而是 Captology 伦理问题在 AI 个性化条件下的放大；也是使用该 Skill 时必须加入的规范边界。
- **来源日期/可信度**：2023，*Frontiers in Artificial Intelligence*；A。

#### 2024：构件测量开始精细化

- **[事实]** 一项疫苗研究为 FBM 的 Motivation 开发 6-item index，CFA 后 baseline/endline Cronbach’s α 为 0.89/0.77；作者称 Ability 的验证指标自 2021 已可用。[S36]
- **意义**：FBM 长期缺少统一测量，这项工作说明研究界开始把宽泛构件变成领域量表。
- **边界**：这是疫苗情境中的 Motivation 指标，不是通用 FBM 量表，也没有验证 M×A×P 的普适函数形式。
- **来源日期/可信度**：2024-01，*Vaccines*；A。

#### 2025-10-14：首个聚焦 FBM 健康干预的范围综述

- **[事实]** Duarte-Anselmi 等在 *BMC Public Health* 发表 scoping review，系统检索后仅纳入 **6 项**符合条件的健康干预，领域涵盖生殖健康、疫苗、慢病、自我管理、一般健康与依从性；效果方向多为正，但差异明显。[S37]
- **综述结论**：
  - FBM 对实践者友好、在公共健康中有潜力；
  - 仍“underutilized”；
  - 需要长期随访、性别分层、结构/文化障碍处理、与其他模型的比较及更严谨方法。[S37]
- **证据读法**：到 2025 年，“大量引用”主要代表采用度，不等于核心模型已完成大规模因果验证。仅 6 项纳入研究是更有诊断价值的数字。
- **来源日期/可信度**：2025-10-14，*BMC Public Health*，DOI 10.1186/s12889-025-24525-y；A。

#### 2026：职位延续与 AI 工具化

- **[作者/机构自述]** 截至 2026-09-07，可核实公开页面仍把 Fogg 列为 Stanford 的行为设计研究/教学者，方向聚焦健康、幸福、human flourishing；各页面的具体职衔和机构归属存在上文所述漂移。[S06][S07][S39]
- **[作者自述]** Fogg 于 2026-07-30 宣布已开发一组用于 Fogg Behavior Design 的 AI tools；当前培训页也把“Behavior Design + AI tools”列为课程组成，称工具持续更新。[S40][S41]
- **最新动态判断**：
  1. 这是**方法应用与商业培训层的 AI 工具化**；
  2. 尚未找到截至截止日的同行评审论文、公开技术规格或新的 FBM 方程；
  3. 因而不能称为“FBM 2.0”或理论修订。
- **来源日期/可信度**：2026-07-30 作者 LinkedIn 与当前官网；B。

---

## 2. 概念版本对照：哪些保持不变，哪些改了名或分叉

### 2.1 核心公式

| 时期 | 写法 | 第三构件 | 状态 |
|---|---|---|---|
| 2006/2007 作者回忆 | 未找到同期正式公式；提及 hot trigger | Trigger | 发现史仅有作者自述 [S01] |
| 2009 正式论文 | 通常后世写作 B=MAT | Trigger | 原论文的正式版本 [S02] |
| 2017 年末以后 | B=MAP | Prompt | 仅改名，机制不变 [S04] |
| 2019/2020 *Tiny Habits* | B=MAP | Prompt | 纳入更大的 Behavior Design 系统 [S01] |

**冲突处理规则**：历史性描述用该年代原词；面向当前用户解释用 Prompt，并注明旧文献的 Trigger 与之等价。不要反向篡改 2009 论文题意。

### 2.2 阈值曲线

| 2009 | 2020 书 | 变化 |
|---|---|---|
| behavior activation threshold | action line（行动线） | 术语简化；均表示提示到来时 M/A 组合是否足以让行为发生 |

曲线从未被原论文参数化，轴也没有单位。它是设计诊断图，不是已估计的概率函数。[S02]

### 2.3 Motivation：至少三套切分并存

| 版本/用途 | 分类 |
|---|---|
| 2009 核心动机 | pleasure/pain；hope/fear；social acceptance/rejection [S02] |
| 当前官网标签 | Sensation；Anticipation；Belonging，各自仍对应上述两极 [S16] |
| 2020 实用来源 PAC | Person（自己想要）；Action（利益/惩罚）；Context（环境/他人）[S01] |

这不是明确宣布的“旧三对被新 PAC 废止”。更合理的读法是：前者按**动机内容**分类，后者按**动机来源**分类。Skill 不应把它们拼成一张没有证据的九宫格。

### 2.4 Ability/Simplicity：六因素变五因素

| 2009 论文六因素 | 2020 书 Ability Chain 五因素 |
|---|---|
| time | time |
| money | money |
| physical effort | physical effort |
| brain cycles | creative/mental effort |
| social deviance | **不再单列** |
| non-routine | whether it fits the current routine / schedule |

2020 版实际删除了 social deviance 这一独立链环，并把 non-routine 改写得更日常化。[S02][S01] 这是真实的版本变化，不应继续声称当前 Ability Chain 有六环。

### 2.5 Prompt：两套“三分类”是正交的

| 分类问题 | 三类 | 出处 |
|---|---|---|
| 这个提示要发挥什么功能？ | Spark / Facilitator / Signal | 2009 FBM，当前官网仍保留 [S02][S04] |
| 提示从哪里来？ | Person / Context / Action（Anchor） | 2020 Tiny Habits [S01] |

两套分类不是互相替代。例如，手机通知在来源上是 Context Prompt，在功能上可能是 Signal、Spark 或 Facilitator。很多二手解释把六个词混成一套，这是错误的。

### 2.6 Behavior Grid：35 → 15

- 2009：5 种改变颜色 × 7 种时间形态 = 35 类的早期 Grid。[S13]
- 2010：Behavior Wizard 采用 15 类目标行为。[S14]
- Stanford 当前页明确判定 35 类有弱点、15 类更好。[S13]

### 2.7 Tiny Habits 的 ABC

- **Anchor Moment**：一个稳定的既有行为或必然事件。
- **Behavior**：可在约 30 秒内完成的 tiny version。
- **Celebration**：行为中或刚结束时制造成功感。

ABC 是 2020 书的成熟表达，不应回填成 2009 FBM 的原始组成部分。[S01]

### 2.8 “情绪创造习惯”与“重复形成自动性”的冲突

- **Fogg 主张**：积极情绪尤其成功感把行为快速“写入”大脑；有些习惯一次即可形成；庆祝可人为制造 Shine。[S01]
- **主流情境—自动性证据**：
  - Wood & Neal：习惯来自反应与稳定情境特征的渐进联结，形成后由情境直接触发。[S23]
  - Lally 等：96 人 12 周研究中，自动性随重复呈渐近曲线；达到个人渐近值 95% 的时间范围 18–254 天，中位约 66 天；漏做一次无实质影响。[S24]
  - Gardner 等：临床建议是“在同一情境中反复做简单行动”，经过 initiation–learning–stability。[S26]
- **准确综合**：
  1. “66 天”不是人人固定期限，Fogg 对固定天数神话的批评成立；
  2. 但“没有研究显示重复创造习惯”表述过强；同行评审文献支持**稳定情境中的重复与自动性增长**；
  3. 积极情绪/内在奖赏可能促进重复和习惯强度，但截至截止日，尚无强证据证明 Fogg 式自我庆祝能独立取代重复；
  4. 2022 RCT 支持 Tiny Habits 项目可改善短期结果，未隔离 Celebration 机制。[S34]

---

## 3. 智识谱系图（带证据等级）

### 3.1 可确认的直接谱系

1. **社会心理学/CASA → Charismatic Computers → Captology**
   - Fogg 论文直接说明运用社会心理规则研究人对计算机的奉承、互惠、团队关系反应。[S09]

2. **Captology → Persuasive Technology 专著 → Persuasive Systems Design（PSD）**
   - Oinas-Kukkonen 与 Harjumaa 直接评价 Fogg 2003 框架对理解 persuasive technology 有用，但不足以直接指导系统开发；其 PSD 增加 persuasion context、设计过程与 28 条软件特性。[S42]

3. **FBM → Behavior Grid/Wizard → Fogg Behavior Design**
   - 发生条件、目标行为类型、解决方案匹配逐步形成一套工作流。[S02][S13][S14]

4. **FBM + 个人试验 → Tiny Habits**
   - Fogg 明确称 Tiny Habits derived from FBM；2011 牙线实验和 5 日项目是方法成形点。[S15][S34]

5. **FBM → Hook Model 的 Action 层**
   - Eyal 官方资料与 workbook 直接引用 Motivation、Ability、Trigger；再自行加 reward 和 investment。[S30]

6. **Tiny Habits anchoring → Atomic Habits habit stacking**
   - Clear 本人明确给 Fogg credit，属于证据最清楚的大众习惯书影响链。[S46]

### 3.2 高度相似但应标为平行理论

1. **Ripple M–C–O（1955）**
   - 词形相似；作者自己否认术语等价；没有直接承继记录。[S05][S18]

2. **TPB（1991）**
   - 都讨论行为控制，但 TPB 围绕信念—意图—行为预测，FBM 围绕即时设计诊断。[S21]

3. **Implementation Intentions（1999）**
   - if/then 与 after/anchor 结构高度接近；Tiny Habits 论文明确承认理论支持，但没有证据称 Fogg 最初由此直接改写。[S22][S34]

4. **COM-B/Behavior Change Wheel（2011）**
   - COM-B：Capability、Opportunity、Motivation → Behavior；FBM：Motivation、Ability、Prompt 同时汇合。
   - COM-B 明确拆分 physical/social opportunity、reflective/automatic motivation，并连接干预功能和政策层；FBM 更轻量、更适合单个“do it now”节点。[S43]
   - COM-B 论文没有把 FBM 列为直接来源，且是系统检索 19 个框架后综合形成，宜视为独立平行框架。

5. **Habit cue–response/automaticity 科学**
   - 共享“稳定线索触发行为”的核心，但主流模型把重复学习置于核心，Fogg 把设计简易度与即时情绪置于核心。[S23][S24][S26]

### 3.3 推断性深层来源

1. **行为主义/强化学习传统**
   - Celebration 定义近似“提高行为未来发生概率的即时后果”；概念关系强，但未找到 Fogg 将 Tiny Habits 明确归功于 Skinner 的原始记录。[S27]

2. **设计思维/原型迭代**
   - “不要责怪人、把生活当实验、设计—测试—修正”与 Stanford 设计文化同构；但本轮没有取得足以建立直接师承的原始来源，暂不写成事实。

3. **Kairos（适时）**
   - 2009 论文直接借古希腊 kairos 解释提示必须在 M/A 越过阈值的时刻到来。[S02] 这是修辞传统与模型结构之间少数明确的概念桥。

---

## 4. 对产品设计、行为设计与习惯写作的影响

### 4.1 产品与 UX

- **即时行为节点**：FBM 把 conversion/onboarding 中的失败归为 M、A 或 P 缺口，促使设计师优先降低步骤、认知负荷和费用，再优化 CTA 时机。[S02]
- **移动通知**：2009 论文已预测移动设备会加强 trigger–behavior coupling；后来的通知、深链和一键操作正好把提示与行为压到同一上下文。[S02]
- **PSD 学术化**：PSD 接过 Captology，但指出 Fogg 框架太有限，补足软件需求和评估分类；这也是“Fogg 奠基、后继框架工程化”的明证。[S42]
- **Hooked 商业化**：Hook Model 把一次行为条件嵌入 trigger–action–variable reward–investment 循环，扩大到留存与习惯型产品。[S30][S31]
- **伦理反作用**：
  - 2018 CHI dark-pattern 研究认为黑暗 UX 与 Fogg 的 reduction、tunneling、suggestion、surveillance、conditioning 等策略存在扭曲后的共鸣，但没有声称所有 persuasive design 都是 dark pattern。[S44]
  - Tristan Harris 自述其 Stanford Persuasive Technology Lab 经历使他担忧注意力经济，后来参与创建 Center for Humane Technology；这是一条“同一谱系内部的伦理反拨”。[S45]

### 4.2 Silicon Valley 影响的强弱分层

- **强证据**：2007 Facebook Class 确实产生大规模应用实践；16M/10 周有 Stanford 校刊支持。[S28]
- **中等证据**：Stanford Behavior Design Lab 说其学生后来共同创办 Instagram、发起 Time Well Spent/Center for Humane Technology。[S07]
- **应谨慎**：
  - Fogg 原书将 Instagram 的简洁与自己的教学连接，并称 Mike Krieger 曾上其课；公开 Stanford 页面能确认 Krieger 的 HCI 背景，但本轮未找到独立课程花名册证明具体哪门 Fogg 课程。[S01]
  - 不应写成“FBM 创造了 Instagram”或“行为设计直接导致 Instagram 成功”。

### 4.3 习惯类大众写作

- **Duhigg（2012）**：平行普及 cue–routine–reward，不宜称 Fogg 的学生或衍生框架。[S29]
- **Eyal（2013/2014）**：直接吸收 B=MAT，面向产品留存扩展。[S30][S31]
- **Clear（2013 接触课程；2018 出书）**：直接吸收 tiny behavior 与 anchoring，并改名 habit stacking。[S01][S46][S25]
- **Hacking Growth（2017）**：有使用旧版 trigger 框架的二手证据，原书页码未核，影响可信度 C。[S32]
- **Fogg 的反批评**：后继书常省略 Celebration/Shine，并把重复当习惯核心；这个批评准确描述了 Fogg 的理论差异，但不能替代对习惯科学证据的评估。[S01][S23][S24]

---

## 5. 截至 2026-09-07 的理论状态

### 5.1 已稳定的部分

- Motivation、Ability、Prompt 同时汇合的三构件框架。
- Motivation 与 Ability 的补偿关系和 action line 图。
- 设计优先级通常是让行为更容易、匹配已有动机、安排及时提示。
- Trigger 已稳定改称 Prompt，但历史文献仍广泛保留 B=MAT。
- Tiny Habits 的成熟配方是 Anchor–Behavior–Celebration。

### 5.2 仍在演化或存在歧义的部分

- Motivation 既有三对核心动机，又有 PAC 来源分类。
- Prompt 同时有“来源三类”和“功能三类”。
- Ability 从六因素缩为五因素。
- Behavior Grid 从 35 类缩为 15 类。
- 组织归属、参与人数和引用数在作者/机构页面持续变化，不宜写死成理论事实。

### 5.3 实证强度判断

- **较有支持**：
  - 简化行为、稳定线索、及时提醒与行为执行相关；
  - M/A 高组在多个公共健康行为中采用率更高；
  - Tiny Habits 5 日项目在一项 RCT 中改善短期 gratitude。
- **尚不足**：
  - action line 的精确函数形状；
  - 三构件是否对“所有年龄、文化、所有行为”普适；
  - Prompt 必须性在无显性提示/内源行为中的可操作定义；
  - Celebration/Shine 相对于无庆祝对照的独立效应；
  - “情绪而非重复创造习惯”的强因果排他表述；
  - 长期、复杂、结构性受限行为（贫困、政策、组织权力、成瘾）的充分解释。

### 5.4 2026 最新动态

- 实践侧最新变化是 Fogg 把 AI 工具加入专业 Behavior Design 培训。[S40][S41]
- 学术侧最重要的新节点仍是 2025 范围综述：应用案例增加，但严格纳入的健康干预只有 6 项。[S37]
- 未检索到 2026 年由 Fogg 正式发表的新模型论文、新公式或 Tiny Habits 大型多中心试验。
- 因此 Skill 应把 2026 AI 内容标为“最新应用动态”，而非“理论已升级”。

---

## 6. 必须保留的版本冲突清单

1. **模型诞生**：作者说 2007；正式论文是 2009。
2. **公式**：B=MAT（历史）与 B=MAP（2017 年末后）机制相同、用词不同。
3. **实验室创立**：作者页 1998；Stanford 人物稿 2000。
4. **Behavior Design 起点**：机构页 2009 开始；中文版序 2010 命名。
5. **Behavior Grid**：35 类早期版被 15 类版明确替代。
6. **Ability**：2009 六因素；2020 五因素，social deviance 不再单列。
7. **Prompt 分类**：功能三类与来源三类同时有效，不能混并。
8. ***Tiny Habits* 出版年**：2019-12-31 电子/首发；2020 版权与全面发行。
9. **项目规模**：英文版前后宣传出现 40,000、60,000；中文版推荐序写 120,000，当前官网又写 millions。口径、日期、是否“亲自 coaching”不同，不用于证明有效性。
10. **Facebook Class 成果**：中文版 24M/不足 6 月；Stanford 校刊 16M/10 周。
11. **习惯因果**：Fogg 强调 emotion，不接受 repetition 为因；主流同行评审文献支持稳定情境重复与自动性渐进增长。
12. **Stanford 当前职位**：Behavior Design Lab、Lifestyle Medicine、Living Education 页面职衔/挂靠更新不同步。

---

## 7. 来源台账（共 46 个独立来源）

> 网站无原始发布日期时，日期栏写“访问 2026-09-07”。可信度评价针对本文所用命题，不代表对整个网站的总体评价。

| ID | 来源、日期与 URL | 类型 | 可信度/用途 |
|---|---|---|---|
| S01 | Fogg, *Tiny Habits* / 简中《福格行为模型》，英文版权 2020；简中 2021-10。仓库主语料 `references/sources/books/fogg-behavior-model.txt` | 原书/中文版序 | A（版权、书内表述）/B（作者回忆与效果主张） |
| S02 | Fogg, “A Behavior Model for Persuasive Design,” 2009-04-26. https://doi.org/10.1145/1541948.1541999 | ACM 会议论文 | A；FBM 原始正式版本 |
| S03 | Fogg Behavior Model 首页，访问 2026-09-07. https://www.behaviormodel.org/ | 作者官网 | B；当前 B=MAP |
| S04 | “Prompts in the Fogg Behavior Model,” 访问 2026-09-07. https://www.behaviormodel.org/prompts | 作者官网 | B；late 2017 改名及功能三类 |
| S05 | “References to related work,” 访问 2026-09-07. https://www.behaviormodel.org/references | 作者官网 | B；作者认可的平行理论清单 |
| S06 | BJ Fogg 官网首页/履历，访问 2026-09-07. https://www.bjfogg.com/ | 作者官网 | B；2007 自述、2009 转向、当前方向 |
| S07 | Stanford Behavior Design Lab, “About Us,” 访问 2026-09-07. https://behaviordesign.stanford.edu/about-us | Stanford 机构页 | A/B；实验室沿革与机构自述 |
| S08 | Fogg, “Stanford,” 访问 2026-09-07. https://www.bjfogg.com/stanford | 作者官网 | B；Aristotle、导师、1998 建实验室、2011 改名 |
| S09 | Fogg, *Charismatic Computers*, 1997. https://dl.acm.org/citation.cfm?id=287026 | 博士论文书目/摘要 | A；社会心理学与 CASA 前史 |
| S10 | Fogg, “Persuasive Computers,” CHI 1998. https://doi.org/10.1145/274644.274677 | ACM 论文 | A；Captology、Functional Triad、伦理 |
| S11 | Elsevier, *Persuasive Technology*, 2002/2003. https://shop.elsevier.com/books/persuasive-technology/fogg/978-1-55860-643-2 | 出版社书目 | A；出版日期冲突 |
| S12 | Fogg & Eckles eds., *Mobile Persuasion*, 2007. https://cir.nii.ac.jp/crid/1970304959835554606 | 图书馆书目 | A；移动说服桥梁 |
| S13 | Fogg, “The Behavior Grid,” 2009-04-26. https://doi.org/10.1145/1541948.1542001 ；Stanford 说明 https://behaviordesign.stanford.edu/resources/fogg-behavior-grid | ACM 论文/机构页 | A；35→15 |
| S14 | Fogg & Hreha, “Behavior Wizard,” 2010. https://doi.org/10.1007/978-3-642-13226-1_13 | Springer 会议论文 | A；15 类及匹配方法 |
| S15 | Fogg, “How I Cracked the Code for Creating Habits,” 2014-12. https://www.acefitness.org/continuing-education/prosource/december-2014/5134/how-i-cracked-the-code-for-creating-habits/ | 作者第一人称文章 | B；2011 Tiny Habits 诞生史 |
| S16 | Fogg, “Motivation,” 访问 2026-09-07. https://www.behaviormodel.org/motivation | 作者官网 | B；核心动机与 2012 Motivation Wave |
| S17 | Penguin UK, *Tiny Habits*, 2019-12-31. https://www.penguin.co.uk/books/438937/tiny-habits-by-bj-fogg/9780753553251 | 出版社书目 | A；2019 首发 |
| S18 | Ripple, “Motivation, Capacity, and Opportunity…,” 1955-06-01. https://doi.org/10.1086/639813 | 同行评审论文 | A；最早三元平行模型 |
| S19 | Bandura, “Self-Efficacy…,” 1977. https://doi.org/10.1037/0033-295X.84.2.191 | 同行评审论文 | A；能力/效能平行理论 |
| S20 | Ryan & Deci, “Intrinsic and Extrinsic Motivations,” 2000-01. https://doi.org/10.1006/ceps.1999.1020 | 同行评审综述 | A；动机质量 |
| S21 | Ajzen, “The Theory of Planned Behavior,” 1991-12. https://doi.org/10.1016/0749-5978(91)90020-T | 同行评审论文 | A；意图型平行理论 |
| S22 | Gollwitzer, “Implementation Intentions,” 1999-07-01. https://doi.org/10.1037/0003-066X.54.7.493 | 同行评审综述 | A；if–then 与 anchor |
| S23 | Wood & Neal, “A New Look at Habits…,” 2007. https://doi.org/10.1037/0033-295X.114.4.843 | 同行评审理论论文 | A；情境—反应自动性 |
| S24 | Lally et al., “How Are Habits Formed,” online 2009-07-16 / issue 2010. https://doi.org/10.1002/ejsp.674 | 同行评审纵向研究 | A；18–254 天、66 天中位数 |
| S25 | Penguin Random House, *Atomic Habits*, 2018-10-16. https://www.penguinrandomhouse.com/books/543993/atomic-habits-by-james-clear/ | 出版社书目 | A；出版日期 |
| S26 | Gardner, Lally & Wardle, “Making Health Habitual,” 2012-11-27. https://doi.org/10.3399/bjgp12X659466 | 同行评审综述/实践建议 | A；重复与稳定情境 |
| S27 | Skinner, *The Behavior of Organisms*, 1938. https://www.bfskinner.org/wp-content/uploads/2016/02/BoO.pdf ；行为分析史回顾 https://doi.org/10.1901/jeab.2003.80-313 | 原著/同行评审回顾 | A；强化谱系 |
| S28 | Stanford Magazine, “It’s Who You Know (Or Don’t),” 2008/访问 2026-09-07. https://stanfordmag.org/contents/it-s-who-you-know-or-don-t | 校刊报道 | C；Facebook Class 16M/10 周 |
| S29 | Duhigg, *The Power of Habit*, 2012. APA 书目 https://psycnet.apa.org/record/2012-09134-000 | 正式书目 | A/C；平行大众习惯框架 |
| S30 | Nir Eyal, “Can Online Apps Change Real-Life Behavior?”, 访问 2026-09-07. https://www.nirandfar.com/can-online-apps-change-real-life-behavior/ 及 workbook https://www.nirandfar.com/download/hooked-workbook.pdf | 后继作者原文 | B；Hooked 直接引用 FBM |
| S31 | Penguin Random House, *Hooked*, 2014-11-04. https://www.penguinrandomhouse.com/books/317898/hooked-by-nir-eyal/ | 出版社书目 | A；正式版日期 |
| S32 | *Hacking Growth* 概述，2017. https://www.usetools.design/tools/hacking-growth-how-todays-fastest-growing-companies-drive-breakout-success | 二手概述 | C；仅辅助核对，不作关键结论 |
| S33 | Agha et al., “Use of a Practitioner-Friendly Behavior Model…,” 2022-08. https://doi.org/10.3390/vaccines10081261 | 同行评审多数据集研究 | A；跨行为 M/A 关联 |
| S34 | “Tiny Habits for Gratitude,” 2022-05-30. https://doi.org/10.3389/fpubh.2022.866992 | 同行评审 RCT | A；方法级证据，未隔离庆祝 |
| S35 | Agha et al., “Use of the Fogg Behavior Model…Condom Use,” 2019. https://doi.org/10.1080/10810730.2019.1597952 | 同行评审 panel study | A；较直接构件检验 |
| S36 | “Development and Assessment of a Six-Item Index…,” 2024-01. https://www.mdpi.com/2076-393X/12/1/6 | 同行评审量表研究 | A；Motivation 测量 |
| S37 | Duarte-Anselmi et al., “Behavioral Science Meets Public Health,” 2025-10-14. https://doi.org/10.1186/s12889-025-24525-y | 同行评审范围综述 | A；截至当前最关键证据汇总 |
| S38 | “Persuasive Technology and Computational Manipulation,” 2023. https://doi.org/10.3389/frai.2023.1216340 | 同行评审伦理论文 | A；AI/hypernudging 风险 |
| S39 | Stanford Lifestyle Medicine, “BJ Fogg, PhD,” 页面在检索时可索引、直接抓取返回 404，访问 2026-09-07. https://lifestylemedicine.stanford.edu/bio-fogg/ | Stanford 页面/缓存记录 | B；当前职衔只作冲突记录 |
| S40 | Fogg LinkedIn 帖文，2026-07-30. https://www.linkedin.com/posts/bjfogg_after-months-of-careful-work-i-now-activity-7488612996512894976-50nq | 作者动态 | B；AI 工具首发自述 |
| S41 | Fogg Behavior Design Training，访问 2026-09-07. https://www.bjfogg.com/training | 作者商业培训页 | B；AI tools 当前形态 |
| S42 | Oinas-Kukkonen & Harjumaa, “Persuasive Systems Design,” 2009. https://doi.org/10.17705/1CAIS.02428 | 同行评审理论论文 | A；Captology 的学术后继 |
| S43 | Michie, van Stralen & West, “The Behaviour Change Wheel,” 2011-04-23. https://doi.org/10.1186/1748-5908-6-42 | 同行评审系统构建论文 | A；COM-B 平行框架 |
| S44 | Gray et al., “The Dark (Patterns) Side of UX Design,” 2018. https://doi.org/10.1145/3173574.3174108 | CHI 同行评审论文 | A；伦理与 dark patterns |
| S45 | Tristan Harris / Berkeley Talks，2021-02-26. https://news.berkeley.edu/2021/02/26/berkeley-talks-transcript-tristan-harris/ | 当事人演讲/大学媒体 | C；伦理反拨影响链 |
| S46 | James Clear, “Small Habits” 与 “Habit Stacking”，访问 2026-09-07. https://jamesclear.com/small-habits ；https://jamesclear.com/habit-stacking | 后继作者原文 | B；明确给 Tiny Habits/anchoring credit |

---

## 8. 研究薄弱点与后续建议

1. **2006–2008 同期档案不足**：尚未找到可公开核验、带日期的第一张 B=MAT 图或 2007 课堂讲义；“2007 发现”主要依赖作者回忆。
2. **Focus Mapping 首发不清**：只有“约十年前创建”的书中自述，缺正式论文或课程档案。
3. **Tiny Habits 术语首现不清**：Anchor、Celebration、Shine、ABC/PAC 各自第一次公开使用的精确年份尚未逐一锁定。
4. **中文独有改写需版本校勘**：中文版序信息丰富，但部分规模数字与英文/Stanford 口径冲突；需要英文 2019/2020 首版逐页对照才能判断哪些是作者专为中国版新增。
5. **Hacking Growth 影响证据偏弱**：尚未取得原书页码，仅有 Fogg 自述与二手概述。
6. **产品影响常被因果夸大**：Facebook Class、Instagram、Clubhouse 等多为教学关系和案例叙事，缺反事实证据。
7. **核心方程未参数化**：M、A、P 没有通用量表，action line 没有正式函数；2024 疫苗动机指标只是领域化进展。
8. **庆祝机制缺拆分试验**：现有 Tiny Habits RCT 没有 Celebration-only factorial design，不能判定 Shine 的独立效应或效应量。
9. **长期和复杂行为证据薄**：公共健康综述仅纳入 6 项，结构性 Opportunity、社会规范、成瘾和权力关系常被压入过宽的 Ability/Context。
10. **2026 AI 工具不可审计**：只有作者公告和培训页，没有公开方法、版本、数据或同行评审评估。

