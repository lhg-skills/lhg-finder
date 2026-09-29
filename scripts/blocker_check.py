#!/usr/bin/env python3
"""lhg-finder 冒烟脚本：校验 blocker 三件套写回文件是否齐全。

用法: python3 scripts/blocker_check.py <blocker-summary.md>
退出码 0 = 三件套齐全；1 = 缺项或为空，并打印 FAIL 原因。
判定规则（三件套缺一不可，且每件内容不能为空）：
  B1 卡在哪 / Stuck on
  B2 试过什么 / Tried so far
  B3 解开后得到什么 / What unblocking enables
"""
import re
import sys

LABELS = [
    ("B1", ["卡在哪", "stuck on"]),
    ("B2", ["试过什么", "tried so far"]),
    ("B3", ["解开后得到什么", "what unblocking enables"]),
]


def check(path: str) -> list[str]:
    with open(path, encoding="utf-8") as f:
        text = f.read()
    fails: list[str] = []
    for code, keys in LABELS:
        found = False
        for key in keys:
            m = re.search(rf"{re.escape(key)}\s*[:：]\s*(.+)", text, re.IGNORECASE)
            if m and m.group(1).strip():
                found = True
                break
        if not found:
            fails.append(f"{code} {'/'.join(keys)}缺失或为空")
    return fails


def main() -> int:
    if len(sys.argv) != 2:
        print("用法: blocker_check.py <blocker-summary.md>")
        return 2
    fails = check(sys.argv[1])
    if fails:
        print("FAIL: " + "；".join(fails))
        return 1
    print("✅ blocker 三件套齐全")
    return 0


if __name__ == "__main__":
    sys.exit(main())
