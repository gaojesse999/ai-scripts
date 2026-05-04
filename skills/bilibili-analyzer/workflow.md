# Bilibili Analyzer 工作流程

## 1. 术语表

| 缩写/术语 | 英文全称 | 中文含义 |
|-----------|---------|----------|
| **BV** | Bilibili Video (ID) | B站视频唯一标识符，如 `BV15qD8BTEsD` |
| **UGC** | User Generated Content | 用户生成内容，指 UP 主自己创作上传的视频（区别于 B站采购的番剧） |
| **UGC 合集 / UGC Season** | UGC Season | UP 主在个人空间创建的视频合集，把多个独立 BV 视频归为一组 |
| **系列 / Series** | Series | B站另一种视频分组方式，功能类似合集但更松散 |
| **分P** | Part / Page | 一个 BV 视频内的多个分段（如"第1P"、"第2P"），共享同一个 BV 号 |
| **spm_id_from** | Super Position Model ID From | B站的来源追踪参数，记录用户从哪个页面点进来，不影响功能 |
| **vd_source** | Video Source | B站的用户追踪标识，不影响功能 |
| **view API** | View API | B站获取视频信息的接口，返回标题、UP主、分P列表、合集信息等 |
| **ugc_season** | UGC Season (字段名) | view API 返回数据中的一个字段，如果该视频属于 UGC 合集则包含合集内所有视频信息 |
| **mid** | Member ID | UP 主的用户ID（数字） |
| **cid** | Content ID | 视频内容 ID，每个分P有独立的 cid |
| **season_id / sid** | Season ID | 合集/系列的唯一编号 |

### 三种"分组"概念区分

| 概念 | 说明 | URL 特征 |
|------|------|----------|
| **分P** | 同一个 BV 视频内的多个片段 | `bilibili.com/video/BVxxx?p=2` |
| **UGC 合集** | 多个**不同 BV 视频**组成的集合 | 合集页: `space.bilibili.com/{mid}/channel/collectiondetail?sid=xxx` |
| **系列** | 另一种多 BV 视频分组 | 系列页: `space.bilibili.com/{mid}/channel/seriesdetail?sid=xxx` |

### URL 类型分类

| 类型 | URL 模式 | 示例 |
|------|---------|------|
| **BV 视频链接** | `bilibili.com/video/BVxxx...` | `https://www.bilibili.com/video/BV15qD8BTEsD?p=2` |
| **合集页面链接** | `space.bilibili.com/{mid}/channel/collectiondetail?sid={id}` | `https://space.bilibili.com/476048648/channel/collectiondetail?sid=12345` |
| **系列页面链接** | `space.bilibili.com/{mid}/channel/seriesdetail?sid={id}` | `https://space.bilibili.com/476048648/channel/seriesdetail?sid=67890` |
| **短链接** | `b23.tv/xxxxx` | `https://b23.tv/AbCdEf` |

## 2. 整体流程图

```mermaid
flowchart TD
    Start([用户提供 URL 和请求]) --> CheckKeywords{用户提及<br/>合集关键词？}
    
    %% 未提及合集关键词
    CheckKeywords -->|否| CheckURLType1{URL 类型？}
    CheckURLType1 -->|BV 链接| SingleFlow[单视频流程]
    CheckURLType1 -->|space.bilibili.com<br/>合集/系列页面| CallCollection1[调用 collection.py]
    CallCollection1 --> CollectionFlow[合集流程]
    
    %% 提及合集关键词
    CheckKeywords -->|是| CheckURLType2{URL 类型？}
    CheckURLType2 -->|space.bilibili.com<br/>合集/系列页面| CallCollection2[调用 collection.py]
    CallCollection2 --> CollectionFlow
    
    CheckURLType2 -->|BV 链接| CallCollection3[调用 collection.py]
    CallCollection3 --> DetectResult{检测结果？}
    
    DetectResult -->|type=single<br/>不属于任何合集| NotifyUser1[提示用户：该视频不属于任何合集]
    NotifyUser1 --> SingleFlow
    
    DetectResult -->|type=collection<br/>source=ugc_season| CheckDual{also_in_series?}
    CheckDual -->|否| CollectionFlow
    CheckDual -->|是| NotifyDual[提示：同时属于系列，<br/>将按 UGC 合集处理]
    NotifyDual --> CollectionFlow
    
    DetectResult -->|type=collection<br/>source=series| CollectionFlow
```

## 3. 单视频流程

```mermaid
flowchart TD
    S1[Step 1: 下载视频并拆帧] --> S1Run["python scripts/prepare.py URL -o 输出目录"]
    S1Run --> S1FPS{视频时长？}
    S1FPS -->|"<10分钟"| FPS1["--fps 1"]
    S1FPS -->|"10-30分钟"| FPS05["--fps 0.5"]
    S1FPS -->|">30分钟"| FPS02["--fps 0.2"]
    FPS1 --> S2
    FPS05 --> S2
    FPS02 --> S2
    
    S2[Step 2: 分析帧图片] --> CheckSubAgent{用户指定<br/>SubAgent？}
    CheckSubAgent -->|否| Sequential[顺序分析]
    CheckSubAgent -->|是| Parallel[Task 工具并行分析]
    
    Sequential --> BatchCalc[计算分批策略]
    Parallel --> BatchCalc
    
    BatchCalc --> BatchExec[分批执行帧分析]
    BatchExec --> S3[Step 3: 生成文档]
    
    S3 --> JudgeType{视频类型？}
    JudgeType -->|实操类| Tutorial[生成实操教程]
    JudgeType -->|知识类| Knowledge[生成知识文档]
    Tutorial --> Output1["输出：视频分析.md"]
    Knowledge --> Output1
```

## 4. 合集流程

```mermaid
flowchart TD
    C1[合集 Step 1: 确认视频列表] --> ShowList[显示合集标题、视频总数、各视频标题和时长]
    ShowList --> UserConfirm{用户确认？}
    UserConfirm -->|否| Abort([结束])
    UserConfirm -->|是| C2[合集 Step 2: 逐个分析视频]
    
    C2 --> Loop[遍历合集中每个视频]
    Loop --> PerVideo["对视频 N 执行：<br/>Step 1 → Step 2 → Step 3"]
    PerVideo --> VideoOK{分析成功？}
    VideoOK -->|是| SaveResult["保存 视频分析.md"]
    VideoOK -->|否| RecordFail[记录失败信息]
    SaveResult --> HasNext{还有下一个视频？}
    RecordFail --> HasNext
    HasNext -->|是| Loop
    HasNext -->|否| C3[合集 Step 3: 合并生成合集文档]
    
    C3 --> Merge["合并操作：<br/>1. 写入合集概要<br/>2. 按顺序拼接各视频分析<br/>3. 标题降级<br/>4. 图片路径调整<br/>5. 标注失败视频"]
    Merge --> Output2["输出：合集视频分析.md"]
```

## 5. 分批策略

```mermaid
flowchart LR
    Total[总图片数] --> C1{"≤30?"}
    C1 -->|是| B1[1 批]
    C1 -->|否| C2{"≤60?"}
    C2 -->|是| B2[2 批]
    C2 -->|否| C3{"≤120?"}
    C3 -->|是| B3[3 批]
    C3 -->|否| C4{"≤200?"}
    C4 -->|是| B4[4 批]
    C4 -->|否| B5[5 批]
```

## 6. collection.py 检测逻辑

```mermaid
flowchart TD
    Input[输入 URL] --> IsShort{"b23.tv<br/>短链接？"}
    IsShort -->|是| Resolve[解析重定向获取真实 URL]
    Resolve --> IsSpace
    IsShort -->|否| IsSpace{"space.bilibili.com<br/>合集/系列页面？"}
    
    IsSpace -->|是,collectiondetail| FetchUGC["调用 seasons_archives_list API<br/>（支持分页）"]
    FetchUGC --> ReturnCollection["返回 type=collection<br/>source=collection_page"]
    
    IsSpace -->|是,seriesdetail| FetchSeries["调用 series/archives API<br/>（支持分页）"]
    FetchSeries --> ReturnSeries["返回 type=collection<br/>source=series_page"]
    
    IsSpace -->|否| ExtractBV[提取 BV 号]
    ExtractBV --> CallView["调用 view API"]
    CallView --> HasUGC{"有 ugc_season？"}
    HasUGC -->|是| ReturnUGCSeason["返回 type=collection<br/>source=ugc_season<br/>+ also_in_series 标记"]
    HasUGC -->|否| ReturnSingle["返回 type=single"]
```

## 7. 输出目录结构

### 单视频

```
<输出目录>/
├── video.mp4
├── images_raw/
├── images/
├── metadata.json
├── frames.json
└── 视频分析.md
```

### 合集

```
<合集输出目录>/
├── <视频1 BV号>/
│   ├── video.mp4
│   ├── images_raw/
│   ├── images/
│   ├── metadata.json
│   ├── frames.json
│   └── 视频分析.md
├── <视频2 BV号>/
│   └── ...
├── ...
└── 合集视频分析.md
```
