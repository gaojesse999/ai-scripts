# 盲测结果 — renzhi-juexing-drive-not-against

- **方法**: 独立 sub-agent，只给 10 个 skill 的 name+description 与用户 prompt，不给 type / expected / notes。
- **日期**: 2026-08-17
- **通过率**: 6/6 = **100%**（诱饵 2/2，容错 0）

| id | type | 盲测 primary | would_trigger | 判定 |
|---|---|---|---|---|
| should-trigger-01 | should_trigger | renzhi-juexing-drive-not-against | yes | PASS |
| should-trigger-02 | should_trigger | renzhi-juexing-drive-not-against | yes | PASS |
| should-trigger-03 | should_trigger | renzhi-juexing-drive-not-against | yes | PASS |
| should-not-trigger-01 | should_not_trigger | NONE | no | PASS |
| should-not-trigger-02 | should_not_trigger | renzhi-juexing-feedback-over-checkin | no | PASS |
| edge-01 | edge_case | NONE（ADHD 临床排除） | no | PASS |

无失败。
