# 标准冒烟测试（skill 自检用）

> 触发时机：SKILL.md「自检与反馈」命中疑似自身缺陷时运行。
> 说明：`scripts/blocker_check.py` 校验 blocker 三件套写回是否齐全（B1 卡在哪 / B2 试过什么 / B3 解开后得到什么）；
> `scripts/scorecard.py` 按 SKILL.md「阶段 3：多维评分卡」计算候选结论档（RECOMMENDED / DEGRADED / EXCLUDED / DUPLICATE）。
> 以下全部用例已于 2026-09-29 实测通过。

## S-1 blocker 三件套齐全

- fixture：`references/fixtures/fixture-blocker-good.md`（B1/B2/B3 俱全）
- ```bash
  python3 scripts/blocker_check.py references/fixtures/fixture-blocker-good.md
  ```
  → 退出码 0，`✅ blocker 三件套齐全`

## S-2 blocker 缺"试过什么"

- fixture：`references/fixtures/fixture-blocker-no-tried.md`（无 B2）
- ```bash
  python3 scripts/blocker_check.py references/fixtures/fixture-blocker-no-tried.md
  ```
  → 退出码 1，FAIL 含 `B2 试过什么`

## S-3 高 star 但无 license → 排除（一票否决）

- fixture：`references/fixtures/fixture-candidate-no-license.json`（★5200，license 为 null）
- ```bash
  python3 scripts/scorecard.py references/fixtures/fixture-candidate-no-license.json
  ```
  → 输出含 `VERDICT: EXCLUDED` 且含 `一票否决`（star 再高也不救回来）

## S-4 高 star 但久未维护 → 降级

- fixture：`references/fixtures/fixture-candidate-stale.json`（★3100，最近提交 520 天前）
- ```bash
  python3 scripts/scorecard.py references/fixtures/fixture-candidate-stale.json
  ```
  → 输出含 `VERDICT: DEGRADED` 且含 `久未维护`

## S-5 五项全过 → 直接推荐

- fixture：`references/fixtures/fixture-candidate-good.json`（MIT 可改编、结构完整、15 天前有提交、无安全异常、无重复）
- ```bash
  python3 scripts/scorecard.py references/fixtures/fixture-candidate-good.json
  ```
  → 输出含 `VERDICT: RECOMMENDED`

## S-6 与已安装 skill 重复 → 已有平替

- fixture：`references/fixtures/fixture-candidate-duplicate.json`（与 lhg-writing 功能重复）
- ```bash
  python3 scripts/scorecard.py references/fixtures/fixture-candidate-duplicate.json
  ```
  → 输出含 `VERDICT: DUPLICATE` 且含 `已有平替`

## S-7 安全披露有未说明项 → 标异常并降级

- fixture：`references/fixtures/fixture-candidate-security.json`（安装脚本内容未说明）
- ```bash
  python3 scripts/scorecard.py references/fixtures/fixture-candidate-security.json
  ```
  → 输出含 `VERDICT: DEGRADED` 且含 `标异常`

## S-8 人工检查项（脚本扫不到的）

- [ ] 第 1 道确认门：最近一次找 skill，是否在用户确认 blocker 之前零搜索
- [ ] 第 2 道确认门：是否出现过"默认安装"/自动安装（必须零容忍）
- [ ] 诚实兜底：搜不到时是否直说、是 code bug 时是否明说"skill 修不好 bug"
- [ ] 中文检索词：检索词拆分里是否有中文关键词组
- [ ] 找过即记：本次评估的候选是否已记入 `references/evaluated.md`
- [ ] 平台中立：本次输出是否出现平台专有路径/命令名
