# 盲测结果 — renzhi-juexing-mental-bandwidth

- **方法**: 独立 sub-agent 盲测；失败 case 修 A2 后再测
- **日期**: 2026-08-17
- **通过率**: 首轮 5/6；补测后 **6/6 = 100%**（诱饵 2/2）

| id | type | 盲测 primary | would_trigger | 判定 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | renzhi-juexing-mental-bandwidth | yes | PASS |
| should-trigger-02 | should_trigger | renzhi-juexing-mental-bandwidth | yes | PASS |
| should-trigger-03 | should_trigger | 首轮 renzhi-juexing-metacognition-meta-time → 补测 renzhi-juexing-mental-bandwidth | 补测 yes | PASS（补测） |
| should-not-trigger-01 | should_not_trigger | NONE | no | PASS |
| should-not-trigger-02 | should_not_trigger | renzhi-juexing-stretch-zone-matching | no | PASS |
| edge-01 | edge_case | NONE（拒把照护/缺钱翻译成不够觉知） | no | PASS |

## 失败分析与补测

should-trigger-03「刚吵完要辞职并卖股票」：首轮判成元时间。收窄双方 description 后，补测改判带宽冻结；对照题「群里回击」仍走元时间。
