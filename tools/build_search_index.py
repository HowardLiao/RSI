#!/usr/bin/env python3
"""Build assets/search-index.json for the site-wide search (assets/rsi-site.js).

Run from the repo root after editing any page:
    python3 tools/build_search_index.py

Each page is split into sections at h1/h2/h3. Navigation, header, footer,
scripts and styles are skipped so shared chrome does not flood the results.
"""
import json
import os
import re
import subprocess
from html.parser import HTMLParser

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "assets", "search-index.json")

# Duplicates or tooling pages that would only repeat other results.
SKIP = {"mobile.html", "index_legacy_swiss.html", "mobile_simulator.html",
        "Hive/RSI_Group_會議紀錄_2026-10-16.html"}  # password-protected; kept out of public search
SKIP_TAGS = {"script", "style", "noscript", "template", "svg", "nav", "header", "footer", "select", "option", "button"}
VOID = {"area", "base", "br", "col", "embed", "hr", "img", "input", "link", "meta", "source", "track", "wbr"}
HEADINGS = {"h1", "h2", "h3", "h4"}
# Many pages use styled divs as headings, e.g. class="section-h2" or "decision-title".
HEADING_CLASS = re.compile(r"(^|[-_ ])(h[1-4]|title|heading|headline)($|[-_ ])", re.I)
CHUNK = 300          # characters per search entry
MAX_SECTION_TEXT = 6000


class PageParser(HTMLParser):
    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.title = ""
        self.in_title = False
        self.skip_depth = 0
        self.stack = []
        self.heading = None  # (tag, id, [text])
        self.sections = []
        self.current = {"h": "", "id": "", "t": []}
        self.last_id = ""

    def handle_starttag(self, tag, attrs):
        a = dict(attrs)
        if tag == "title":
            self.in_title = True
        if tag in VOID:
            return
        self.stack.append(tag)
        if self.skip_depth or tag in SKIP_TAGS or a.get("aria-hidden") == "true" or "hidden" in a:
            self.skip_depth += 1
            return
        if a.get("id"):
            self.last_id = a["id"]
        if self.heading is None and (tag in HEADINGS or (tag in ("div", "span", "p", "strong") and HEADING_CLASS.search(a.get("class") or ""))):
            self.heading = (tag, a.get("id") or "", [], len(self.stack))

    def handle_endtag(self, tag):
        if tag == "title":
            self.in_title = False
        if tag in VOID or tag not in self.stack:
            return
        while self.stack:
            t = self.stack.pop()
            if self.skip_depth:
                self.skip_depth -= 1
                if t == tag:
                    return
                continue
            if self.heading and self.heading[0] == t and len(self.stack) + 1 == self.heading[3]:
                text = squash("".join(self.heading[2]))
                if text and len(text) > 120:  # not really a heading; keep it as body text
                    self.current["t"].append(" " + text + " ")
                    text = ""
                if text:
                    self.flush()
                    self.current = {"h": text, "id": self.heading[1] or self.last_id, "t": []}
                self.heading = None
            if t == tag:
                return

    def handle_data(self, data):
        if self.in_title:
            self.title += data
            return
        if self.skip_depth:
            return
        if self.heading:
            self.heading[2].append(data)
        else:
            self.current["t"].append(data)

    def flush(self):
        text = squash(" ".join(self.current["t"]))[:MAX_SECTION_TEXT]
        if not (self.current["h"] or text):
            return
        chunks = chunk(text) or [""]
        for c in chunks:
            self.sections.append({"h": self.current["h"], "id": self.current["id"], "t": c})


def squash(s):
    return re.sub(r"\s+", " ", s).strip()


def chunk(text):
    """Split long text near sentence ends so each search hit shows a readable snippet."""
    out, buf = [], ""
    for part in re.split(r"(?<=[。；！？.!?])\s*", text):
        if len(buf) + len(part) > CHUNK and buf:
            out.append(buf.strip())
            buf = ""
        buf += part
        while len(buf) > CHUNK * 1.5:
            out.append(buf[:CHUNK].strip())
            buf = buf[CHUNK:]
    if buf.strip():
        out.append(buf.strip())
    return out


def pages():
    out = subprocess.run(["git", "ls-files", "-z", "*.html"], cwd=ROOT, capture_output=True, text=True).stdout
    return sorted(p for p in out.split("\0") if p and p not in SKIP)


def main():
    index = []
    for rel in pages():
        with open(os.path.join(ROOT, rel), encoding="utf-8") as f:
            html = f.read()
        p = PageParser()
        p.feed(html)
        p.flush()
        title = squash(p.title) or rel
        sections = [s for s in p.sections if len(s["t"]) > 20 or (s["h"] and not s["t"])]
        index.append({"u": rel, "title": title, "g": "蜂巢計畫 Hive" if rel.startswith("Hive/") else "RSI 2027 IT 營運計畫", "s": sections})
    os.makedirs(os.path.dirname(OUT), exist_ok=True)
    with open(OUT, "w", encoding="utf-8") as f:
        json.dump({"v": 1, "pages": index}, f, ensure_ascii=False, separators=(",", ":"))
    n = sum(len(p["s"]) for p in index)
    print(f"{len(index)} pages, {n} sections -> {os.path.relpath(OUT, ROOT)} ({os.path.getsize(OUT)//1024} KB)")


if __name__ == "__main__":
    main()
