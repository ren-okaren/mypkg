from pathlib import Path

targets = list(Path(".").rglob("*.py"))
for p in targets:
    text = p.read_text(encoding="utf-8")
    lines = text.splitlines(True)  # keep \n
    changed = False

    # 先頭の SPDX 行を削除（連続しているぶん全部）
    while lines and lines[0].lstrip().startswith("# SPDX-"):
        lines.pop(0)
        changed = True

    # 先頭に空行が残ったら消す
    if changed:
        while lines and lines[0].strip() == "":
            lines.pop(0)

        p.write_text("".join(lines), encoding="utf-8")
        print("fixed:", p)
