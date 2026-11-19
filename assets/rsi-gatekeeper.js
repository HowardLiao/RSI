/**
 * RSI Project Hive - Automated Visitor Analytics & Telemetry Engine
 * 100% Autonomous: Zero-barrier open access, real-time telemetry beacon.
 * Automatically tracks visitor identity (?u=...), pages viewed, and file downloads.
 */
(function () {
  "use strict";

  // Clean up any legacy modal overlays
  function removeLegacyOverlays() {
    try {
      document.documentElement.classList.remove("rsi-locked");
      const overlays = document.querySelectorAll(
        "#rsi-gatekeeper-overlay, #rsi-gate-overlay, #rsi-admin-modal, #rsi-verified-chip, .rsi-gate-backdrop, .rsi-admin-overlay"
      );
      overlays.forEach(function (el) {
        try { el.remove(); } catch (err) {}
      });
      if (document.body) {
        document.body.style.overflow = "";
        document.body.style.position = "";
      }
    } catch (e) {}
  }

  if (document.readyState === "loading") {
    document.addEventListener("DOMContentLoaded", removeLegacyOverlays);
  } else {
    removeLegacyOverlays();
  }

  // === Visitor Telemetry Beacon ===
  const AUDIT_TOPIC = "howard_rsi_audit_log";
  const BEACON_URL = "https://ntfy.sh/" + AUDIT_TOPIC;

  // Extract visitor identity from query params or session cache
  const urlParams = new URLSearchParams(window.location.search);
  let visitor = urlParams.get("u") || urlParams.get("user") || urlParams.get("name") || urlParams.get("utm_source");

  if (visitor) {
    try {
      sessionStorage.setItem("rsi_visitor_name", visitor);
    } catch (e) {}
  } else {
    try {
      visitor = sessionStorage.getItem("rsi_visitor_name") || "外部訪客 / 匿名主管";
    } catch (e) {
      visitor = "外部訪客 / 匿名主管";
    }
  }

  // Device & Environment fingerprinting
  function getDeviceSummary() {
    const ua = navigator.userAgent || "";
    let os = "PC / Desktop";
    if (/iPhone/i.test(ua)) os = "iPhone (iOS)";
    else if (/iPad/i.test(ua)) os = "iPad (iPadOS)";
    else if (/Android/i.test(ua)) os = "Android 裝置";
    else if (/Macintosh/i.test(ua)) os = "Mac (macOS)";
    else if (/Windows/i.test(ua)) os = "Windows PC";

    let browser = "瀏覽器";
    if (/Line/i.test(ua)) browser = "LINE 內建瀏覽器";
    else if (/MicroMessenger/i.test(ua)) browser = "WeChat 內建瀏覽器";
    else if (/Chrome/i.test(ua)) browser = "Chrome";
    else if (/Safari/i.test(ua)) browser = "Safari";
    else if (/Firefox/i.test(ua)) browser = "Firefox";

    return os + " · " + browser;
  }

  // Dispatch event beacon
  function sendAuditBeacon(title, body, tags) {
    try {
      const payload = body || "";
      if (navigator.sendBeacon) {
        const headers = {
          type: "text/plain; charset=utf-8"
        };
        const blob = new Blob([payload], headers);
        // Note: fetch with headers allows setting Title and Tags for ntfy
        fetch(BEACON_URL, {
          method: "POST",
          headers: {
            "Title": title,
            "Tags": tags || "eyes",
            "Priority": "default"
          },
          body: payload,
          mode: "no-cors"
        }).catch(function () {});
      } else {
        fetch(BEACON_URL, {
          method: "POST",
          headers: {
            "Title": title,
            "Tags": tags || "eyes"
          },
          body: payload,
          mode: "no-cors"
        }).catch(function () {});
      }
    } catch (err) {}
  }

  // Format timestamp (Taipei Time UTC+8)
  function getTaipeiTimeString() {
    try {
      return new Intl.DateTimeFormat("zh-TW", {
        timeZone: "Asia/Taipei",
        year: "numeric",
        month: "2-digit",
        day: "2-digit",
        hour: "2-digit",
        minute: "2-digit",
        second: "2-digit",
        hour12: false
      }).format(new Date());
    } catch (e) {
      return new Date().toISOString();
    }
  }

  // 1. Record Page Visit
  function recordPageVisit() {
    const timeStr = getTaipeiTimeString();
    const pageTitle = document.title || "RSI 蜂巢計畫頁面";
    const path = window.location.pathname || "/";
    const ref = document.referrer ? (new URL(document.referrer, window.location.origin).hostname || "外部推薦") : "直接點擊造訪";
    const dev = getDeviceSummary();

    const title = "[RSI 訪客] " + visitor + " 造訪";
    const body = "訪客身分: " + visitor + "\n" +
                 "造訪頁面: " + pageTitle + "\n" +
                 "路徑: " + path + "\n" +
                 "時間: " + timeStr + "\n" +
                 "設備: " + dev + "\n" +
                 "來源: " + ref;

    sendAuditBeacon(title, body, "eyes,bell");
    console.log("[RSI Telemetry] Logged visit for:", visitor, "on", path);
  }

  // Run on initial load
  if (document.readyState === "complete" || document.readyState === "interactive") {
    recordPageVisit();
  } else {
    window.addEventListener("DOMContentLoaded", recordPageVisit);
  }

  // 2. Record Document & Report Downloads
  document.addEventListener("click", function (e) {
    const a = e.target.closest("a");
    if (!a || !a.href) return;
    const href = a.href;
    if (/\\.(docx|csv|pdf|pptx|xlsx|zip)$/i.test(href)) {
      const fileName = href.split("/").pop();
      const timeStr = getTaipeiTimeString();
      const title = "[RSI 文件下載] " + visitor;
      const body = "訪客身分: " + visitor + "\n" +
                   "下載檔案: " + fileName + "\n" +
                   "所在頁面: " + (document.title || window.location.pathname) + "\n" +
                   "時間: " + timeStr;
      sendAuditBeacon(title, body, "floppy_disk,inbox_tray");
    }
  });

  // Global handle for dashboard or manual queries
  window.RSITelemetry = {
    visitor: visitor,
    channel: AUDIT_TOPIC,
    setIdentity: function (name) {
      sessionStorage.setItem("rsi_visitor_name", name);
      window.location.reload();
    }
  };
})();
