# lhg-finder · 找 Skill 的质检门

> **一句话**：安装任何第三方 skill 之前的质检门：blocker 三件套检查 + 六维评分卡，两道确认门，永远不自动安装。
>
> **一键安装**：`npx skills add lhg-skills/lhg-finder`


卡住时帮你找"能解当前困境"的 skill：**先提炼 blocker 三件套并暂停确认，再用多维评分卡筛候选**（lhg-skills 出品，流程借鉴 Emily27-alt/find-skill（MIT），文本独立重写）。

**流程**：第 1 道确认门（blocker 三件套：卡在哪 / 试过什么 / 解开后得到什么，确认前不搜索；前置诚实判断：是 code bug 就明说"skill 修不好 bug"）→ 阶段 1 本地优先（本地够用就明说，不硬推全网）→ 阶段 2 全网检索（中文关键词 + 英文技术词并行，候选上限 5 个）→ 阶段 3 多维评分卡（license 一票否决 / SKILL.md 结构完整性 / 维护活跃度 / 安全披露 / 去重检查，star 只作热度分项；结论分直接推荐 / 备选 / 排除三档；找过即记留档）→ 第 2 道确认门（装前预览 SKILL.md 全文 + 安全披露逐项清单，确认才装）→ 诚实兜底（搜不到直说、是 bug 明说、本地够用明说）。

**触发**：用户说"有没有 skill 能帮我做… / 卡住了找个 skill / 推荐个 skill"时使用——先确认卡点，再找 skill，而不是直接搜。

## 安装

一键安装：`npx skills add lhg-skills/lhg-finder`

- 通用：将本仓库放到各平台的 skill 目录（如 `~/.agents/skills/lhg-finder/`，注意 SKILL.md 须在目录根）。
- Coze：在扣子编程（code.coze.cn）→ 导入项目 → 本地上传本仓库 zip 包，平台会识别为 skill 类型。
- Trae：设置 → 技能 → 上传技能，选择本仓库 zip 包（或把目录放到 `~/.trae-cn/skills/`，国区版注意路径）。
- 平台无关：本 skill 写法平台中立（联网搜索/抓取全文/只读子 agent/任务清单/文件搜索/编辑），不依赖任何单一生态的专有工具名。

## 自检与反馈

本 skill 每次执行后自动做一次轻量自检（对照两道确认门/评分卡六维度/诚实兜底）；只有发现疑似自身缺陷时，才运行 `references/smoke-test.md` 标准用例并输出质检报告。报告经你确认后，可一键向 GitHub 提交 `[QC]` issue（模板见 `.github/ISSUE_TEMPLATE/qc-report.md`）。

## 版本

- 1.0.0（2026-09-29）：首版。blocker 三件套 + 两道确认门 + 本地优先 + 多维评分卡（license 一票否决/结构完整性/维护活跃度/安全披露/去重检查，star 仅作热度分项）+ 找过即记 + 诚实兜底；流程借鉴 Emily27-alt/find-skill（MIT）。

## 什么时候用 / 什么时候不用

**用它，当你**：
- 从网上找 skill，装进自己的 Agent 之前先验货
- 给团队引入外部 skill，需要安全与质量把关

**别用它，当你**：
- 只用官方 skill（anthropics/vercel-labs），不需要质检
- 个人尝鲜，不在乎风险

---

## lhg-skills 矩阵

刘洪光出品的中文 Agent Skills，全开源：

| Skill | 名称 | 一句话 |
|---|---|---|
| `lhg-writing` | 中文写作 | 风格指纹 → Orwell 六规则 → AI 味诊断，写出有人味的中文 |
| `lhg-slides` | HTML 演示文稿 | 大纲/文档一键生成可编辑的单文件 HTML slides |
| `lhg-trend` | 近30天热点扫描 | 话题火不火、为什么火、还能不能追 |
| `lhg-deep-research` | 深度调研 | 多源检索 → 结构化中文调研报告 |
| `lhg-benchmark-topic-factory` | 对标拆解选题工厂 | 找对标 → 逆向 100 条选题库 → 口播文案 |
| `lhg-net` | 互联网能力层 | 中文优先多平台取数，取不到诚实说 |
| `lhg-craft` | AI 编程工程规范 | 分级澄清 → TDD → 独立评审 → 证据门禁 |
| `lhg-debug` | 系统化调试 | 复现 → 定位 → 修复 → 验证 |
| `lhg-secure` | 代码安全审计 | 九维度扫描 + 对抗验证，分级风险清单 |
| `lhg-finder` | 找 skill 质检门 | 装第三方 skill 前的 blocker 检查 + 六维评分 |

安装任意一个：`npx skills add lhg-skills/<上表 slug>`

---

## 出品：刘洪光

本 skill 由真人出镜 IP「刘洪光」（安徽合肥）出品，归属 [lhg-skills](https://github.com/lhg-skills)。

- GitHub 主页：https://github.com/lhg-skills —— 全部 skill 开源在此，欢迎 star
- 视频号：搜「刘洪光实名上网」
- 微信：lhgsmsw
