#!/usr/bin/env python3
"""Stamp every page's links to the shared assets with a content hash (?v=...).

GitHub Pages lets browsers cache files for 10 minutes. Without a version in the
URL a visitor can get a new rsi-site.js with an old rsi-site.css, and the top bar
renders unstyled. Run from the repo root after editing anything in assets/:

    python3 tools/stamp_assets.py
"""
import hashlib
import os
import re
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
ASSETS = ["rsi-site.css", "rsi-site.js", "rsi-music.js"]


def main():
    ver = {}
    for name in ASSETS:
        with open(os.path.join(ROOT, "assets", name), "rb") as f:
            ver[name] = hashlib.sha256(f.read()).hexdigest()[:10]
    pat = re.compile(r'(assets/(' + "|".join(re.escape(a) for a in ASSETS) + r'))(\?v=[0-9a-f]+)?"')
    out = subprocess.run(["git", "ls-files", "-z", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout
    changed = 0
    for rel in sorted(p for p in out.split("\0") if p):
        path = os.path.join(ROOT, rel)
        s = open(path, encoding="utf-8").read()
        t = pat.sub(lambda m: f'{m.group(1)}?v={ver[m.group(2)]}"', s)
        if t != s:
            open(path, "w", encoding="utf-8").write(t)
            changed += 1
    print("versions:", ", ".join(f"{k}={v}" for k, v in ver.items()), "| pages updated:", changed)


if __name__ == "__main__":
    main()
