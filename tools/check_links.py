#!/usr/bin/env python3
"""Check that every relative Markdown link in the repo points at a file that exists.

Usage:
    python tools/check_links.py          # from the repo root; exits 1 on any broken link
"""
import pathlib
import re
import sys

ROOT = pathlib.Path(__file__).resolve().parent.parent
LINK = re.compile(r"\[[^\]]*\]\(([^)\s]+)\)")
SKIP = ("http://", "https://", "mailto:", "#")


def main():
    broken = []
    for md in sorted(ROOT.rglob("*.md")):
        if {".git", "_upcoming", "Claude outputs"} & set(md.parts):
            continue
        text = md.read_text(encoding="utf-8")
        text = re.sub(r"```.*?```", "", text, flags=re.S)  # ignore code blocks
        for target in LINK.findall(text):
            if target.startswith(SKIP):
                continue
            path = target.split("#", 1)[0]
            if path and not (md.parent / path).resolve().exists():
                broken.append(f"{md.relative_to(ROOT)} -> {target}")
    if broken:
        print("Broken links:")
        print("\n".join(f"  {b}" for b in broken))
        sys.exit(1)
    print("All relative links resolve.")


if __name__ == "__main__":
    main()
