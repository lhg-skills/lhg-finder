#!/usr/bin/env python3
"""lhg-finder 冒烟脚本：按 SKILL.md「阶段 3：多维评分卡」计算候选结论档。

用法: python3 scripts/scorecard.py <candidate.json>
输入 JSON 字段：
  name, stars, license (字符串或 null), license_allows_adaptation (bool),
  frontmatter: {has_name, has_description, has_version},
  platform_neutral (bool), last_commit_days_ago (int), issue_responsive (bool),
  security: [{item, disclosed, redline}], duplicates: [已安装 skill 名],
  is_skill (bool)
输出一行: VERDICT: <档> | <name> | ★<stars> | <原因>
档: RECOMMENDED / DEGRADED / EXCLUDED / DUPLICATE
退出码恒为 0（脚本跑通即成功；结论档由冒烟用例断言）。
"""
import json
import sys

STALE_DAYS = 365  # 维护活跃度通过线：12 个月


def verdict(c: dict) -> tuple[str, str]:
    reasons: list[str] = []
    name = c.get("name", "?")

    if not c.get("is_skill", True):
        return "EXCLUDED", "非 skill 仓库"

    lic = c.get("license")
    if not lic:
        return "EXCLUDED", "无 license（一票否决）"
    if not c.get("license_allows_adaptation", False):
        reasons.append(f"license {lic} 不允许改编，仅可原样使用")

    sec = c.get("security", []) or []
    redlines = [s["item"] for s in sec if s.get("redline")]
    if redlines:
        return "EXCLUDED", "安全红线：" + "、".join(redlines)
    undisclosed = [s["item"] for s in sec if not s.get("disclosed", True)]
    if undisclosed:
        reasons.append("安全披露有未说明项并标异常：" + "、".join(undisclosed))

    fm = c.get("frontmatter", {}) or {}
    if not (fm.get("has_name") and fm.get("has_description")):
        reasons.append("SKILL.md 结构缺项（frontmatter 缺 name/description）")
    if not c.get("platform_neutral", True):
        reasons.append("平台不中立（含平台专有路径/命令）")

    days = c.get("last_commit_days_ago")
    if isinstance(days, int) and days > STALE_DAYS:
        reasons.append(f"久未维护（最近提交 {days} 天前）")

    dups = c.get("duplicates", []) or []
    if dups:
        note = "已有平替：" + "、".join(dups)
        if reasons:
            note += "；另有降级项：" + "；".join(reasons)
        return "DUPLICATE", note

    if reasons:
        return "DEGRADED", "；".join(reasons)
    extra = "；issue 有响应" if c.get("issue_responsive") else ""
    return "RECOMMENDED", f"五项全过{extra}"


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: scorecard.py <candidate.json>")
        return 2
    with open(sys.argv[1], encoding="utf-8") as f:
        c = json.load(f)
    tier, reason = verdict(c)
    print(f"VERDICT: {tier} | {c.get('name', '?')} | ★{c.get('stars', 0)} | {reason}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
