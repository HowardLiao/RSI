#!/usr/bin/env python3
import os
import sys
import time
import json
import csv
import urllib.request
from datetime import datetime

LOG_DIR = "/Users/howard/Desktop/HermesAgent/PortFilio/RSI/logs"
CSV_FILE = os.path.join(LOG_DIR, "visitor_audit.csv")
STATE_FILE = os.path.expanduser("~/.hermes/rsi_visitor_state.json")
NTFY_URL = "https://ntfy.sh/howard_rsi_audit_log/json?poll=1"

env_file = os.path.expanduser("~/.hermes/.env")
line_token = None
line_user = None

if os.path.exists(env_file):
    with open(env_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if line and not line.startswith("#") and "=" in line:
                k, v = line.split("=", 1)
                k = k.strip()
                v = v.strip("\"'")
                if k == "LINE_CHANNEL_ACCESS_TOKEN":
                    line_token = v
                elif k == "LINE_ALLOWED_USERS":
                    line_user = v

def load_processed_ids():
    if os.path.exists(STATE_FILE):
        try:
            with open(STATE_FILE, "r", encoding="utf-8") as f:
                return set(json.load(f))
        except Exception:
            return set()
    return set()

def save_processed_ids(ids):
    try:
        recent = list(ids)[-2000:]
        with open(STATE_FILE, "w", encoding="utf-8") as f:
            json.dump(recent, f)
    except Exception as e:
        print(f"[Error saving state]: {e}", file=sys.stderr)

def init_csv():
    os.makedirs(LOG_DIR, exist_ok=True)
    if not os.path.exists(CSV_FILE):
        with open(CSV_FILE, "w", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(["存取時間", "訪客姓名/身分", "行為動作", "造訪頁面或檔案", "裝置與瀏覽器", "來源管道", "原始訊息ID"])

def append_to_csv(row):
    try:
        init_csv()
        with open(CSV_FILE, "a", newline="", encoding="utf-8-sig") as f:
            writer = csv.writer(f)
            writer.writerow(row)
    except Exception as e:
        print(f"[Error writing CSV]: {e}", file=sys.stderr)

def send_line_push(text):
    if not line_token or not line_user:
        return
    url = "https://api.line.me/v2/bot/message/push"
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {line_token}"
    }
    payload = {
        "to": line_user,
        "messages": [
            {
                "type": "text",
                "text": text
            }
        ]
    }
    try:
        req = urllib.request.Request(url, data=json.dumps(payload).encode("utf-8"), headers=headers)
        with urllib.request.urlopen(req, timeout=10) as resp:
            pass
    except Exception as e:
        print(f"[Error sending LINE push]: {e}", file=sys.stderr)

def parse_msg(raw):
    res = {}
    for line in (raw or "").splitlines():
        if ":" in line:
            k, v = line.split(":", 1)
            res[k.strip()] = v.strip()
    return res

def poll_once(processed_ids):
    try:
        req = urllib.request.Request(NTFY_URL, headers={"User-Agent": "RSI-Monitor"})
        with urllib.request.urlopen(req, timeout=10) as resp:
            content = resp.read().decode("utf-8")
        
        lines = [l for l in content.strip().splitlines() if l.strip()]
        new_count = 0

        for line in lines:
            try:
                item = json.loads(line)
                if item.get("event") != "message":
                    continue
                msg_id = item.get("id")
                if not msg_id or msg_id in processed_ids:
                    continue

                processed_ids.add(msg_id)
                new_count += 1

                title = item.get("title", "")
                raw_msg = item.get("message", "")
                fields = parse_msg(raw_msg)

                is_download = "下載" in title
                action = fields.get("行為動作") or ("重要文件下載" if is_download else "頁面造訪")
                visitor = fields.get("訪客身分", title.replace("[RSI 訪客]", "").replace("造訪", "").strip() or "外部訪客")
                target = fields.get("下載檔案") if is_download else (fields.get("造訪頁面") or fields.get("路徑") or "首頁")
                time_str = fields.get("時間", datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                device = fields.get("設備", "未知設備")
                ref = fields.get("來源", "直接造訪")

                # 1. Write to local CSV
                append_to_csv([time_str, visitor, action, target, device, ref, msg_id])

                # 2. Push to LINE
                line_text = (
                    f"🔔 [RSI 蜂巢計畫 · 訪客動態]\n"
                    f"👤 訪客：{visitor}\n"
                    f"⚡️ 行為：{action}\n"
                    f"📄 目標：{target}\n"
                    f"📱 設備：{device}\n"
                    f"⏱ 時間：{time_str}"
                )
                send_line_push(line_text)
                print(f"[RSI Monitor] Processed: {visitor} -> {action}: {target}")

            except Exception as e:
                print(f"[Error processing message]: {e}", file=sys.stderr)

        if new_count > 0:
            save_processed_ids(processed_ids)

    except Exception as e:
        print(f"[Error polling ntfy]: {e}", file=sys.stderr)

def main():
    print("[RSI Monitor] Daemon started...")
    init_csv()
    processed = load_processed_ids()
    while True:
        poll_once(processed)
        time.sleep(10)

if __name__ == "__main__":
    main()
