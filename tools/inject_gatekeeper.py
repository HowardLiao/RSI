#!/usr/bin/env python3
"""Inject RSI Gatekeeper CSS and JS into all HTML pages in the repository."""

import os
import subprocess

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MARK = "<!-- rsi-gatekeeper -->"

def main():
    out = subprocess.run(["git", "ls-files", "-z", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout
    changed = 0
    all_files = sorted(p for p in out.split("\0") if p)

    for rel in all_files:
        if rel in ["index_raw_backup.html", "index_encrypted_test.html"]:
            continue
        path = os.path.join(ROOT, rel)
        if not os.path.isfile(path):
            continue
        s = open(path, encoding="utf-8").read()
        if MARK in s or "</head>" not in s or "</body>" not in s:
            continue

        prefix = "../" * rel.count("/")
        css_tag = f'  {MARK}\n  <link rel="stylesheet" href="{prefix}assets/rsi-gatekeeper.css">\n</head>'
        js_tag = f'  <script src="{prefix}assets/rsi-gatekeeper.js"></script>\n</body>'

        s = s.replace("</head>", css_tag, 1)
        # Use rfind for </body>
        last_body = s.rfind("</body>")
        if last_body != -1:
            s = s[:last_body] + f'  <script src="{prefix}assets/rsi-gatekeeper.js"></script>\n' + s[last_body:]
            open(path, "w", encoding="utf-8").write(s)
            changed += 1

    print(f"Total HTML files processed. Pages updated: {changed}")

if __name__ == "__main__":
    main()
