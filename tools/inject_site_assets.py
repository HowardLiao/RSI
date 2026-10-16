#!/usr/bin/env python3
"""Add the shared site layer (assets/rsi-site.css + assets/rsi-site.js) to every page.

Idempotent: pages that already carry the <!-- rsi-site --> marker are skipped.
Run from the repo root:  python3 tools/inject_site_assets.py
"""
import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARK = "<!-- rsi-site -->"
VIEWPORT = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'


def main():
    out = subprocess.run(["git", "ls-files", "-z", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout
    changed = 0
    for rel in sorted(p for p in out.split("\0") if p):
        path = os.path.join(ROOT, rel)
        s = open(path, encoding="utf-8").read()
        if MARK in s or "</head>" not in s or "</body>" not in s:
            continue
        prefix = "../" * rel.count("/")
        if 'name="viewport"' not in s:
            s = s.replace("</head>", f"  {VIEWPORT}\n</head>", 1)
        s = s.replace("</head>", f'  {MARK}\n  <link rel="stylesheet" href="{prefix}assets/rsi-site.css">\n</head>', 1)
        i = s.rfind("</body>")
        s = s[:i] + f'  <script src="{prefix}assets/rsi-site.js" defer></script>\n' + s[i:]
        open(path, "w", encoding="utf-8").write(s)
        changed += 1
    print("pages updated:", changed)


if __name__ == "__main__":
    main()
