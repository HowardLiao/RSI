/**
 * RSI Project Hive - Enterprise Visitor Identity & Email Telemetry Engine
 * Features:
 * 1. Automatic Email registration modal for first-time visitors (Zero password friction).
 * 2. Persistent identity stored in localStorage (remembers visitor forever on their device).
 * 3. Real-time beacon to ntfy / LINE on email registration, page views, and file downloads.
 * 4. Backward-compatible with ?email=... and ?u=... query parameters.
 * 5. Exempts admin pages (visitor_log.html).
 */
(function () {
  "use strict";

  const AUDIT_TOPIC = "howard_rsi_audit_log";
  const BEACON_URL = "https://ntfy.sh/" + AUDIT_TOPIC;
  const STORAGE_KEY = "rsi_visitor_email";

  // Check if current page is admin dashboard (exempt)
  const isDashboard = window.location.pathname.includes("visitor_log.html");

  // Device & Environment fingerprinting
  function getDeviceSummary() {
    const ua = navigator.userAgent || "";
    let os = "PC / 桌面電腦";
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

  // Dispatch event beacon
  function sendAuditBeacon(title, body, tags) {
    try {
      const payload = body || "";
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
    } catch (err) {}
  }

  // Strict email validation helper (prevents DOM-XSS from query params)
  const EMAIL_REGEX = /^[^\s@<>'"]+@[^\s@<>'"]+\.[^\s@<>'"]+$/;

  // Check URL query parameters (?email=... or ?u=...)
  const urlParams = new URLSearchParams(window.location.search);
  const rawParamEmail = (urlParams.get("email") || urlParams.get("u") || urlParams.get("user") || "").trim().toLowerCase();
  if (rawParamEmail && EMAIL_REGEX.test(rawParamEmail) && rawParamEmail.length <= 160) {
    try {
      localStorage.setItem(STORAGE_KEY, rawParamEmail);
    } catch (e) {}
  }

  let currentEmail = "";
  try {
    const stored = (localStorage.getItem(STORAGE_KEY) || "").trim().toLowerCase();
    if (stored && EMAIL_REGEX.test(stored)) {
      currentEmail = stored;
    } else if (stored) {
      localStorage.removeItem(STORAGE_KEY);
    }
  } catch (e) {}

  // Log page visit
  function logPageVisit(email) {
    if (!email) return;
    const timeStr = getTaipeiTimeString();
    const pageTitle = document.title || "RSI 蜂巢計畫頁面";
    const path = window.location.pathname || "/";
    const ref = document.referrer ? (new URL(document.referrer, window.location.origin).hostname || "外部推薦") : "直接點擊造訪";
    const dev = getDeviceSummary();

    const title = "[RSI 訪客] " + email + " 造訪";
    const body = "訪客身分: " + email + "\n" +
                 "行為動作: 頁面造訪\n" +
                 "造訪頁面: " + pageTitle + "\n" +
                 "路徑: " + path + "\n" +
                 "時間: " + timeStr + "\n" +
                 "設備: " + dev + "\n" +
                 "來源: " + ref;

    sendAuditBeacon(title, body, "eyes,bell");
    console.log("[RSI Telemetry] Visit logged for:", email);
  }

  // Log email registration
  function logRegistration(email) {
    const timeStr = getTaipeiTimeString();
    const pageTitle = document.title || "RSI 蜂巢計畫頁面";
    const path = window.location.pathname || "/";
    const dev = getDeviceSummary();

    const title = "[RSI 身分登記] " + email;
    const body = "訪客身分: " + email + "\n" +
                 "行為動作: 輸入 Email 登記進入\n" +
                 "造訪頁面: " + pageTitle + "\n" +
                 "路徑: " + path + "\n" +
                 "時間: " + timeStr + "\n" +
                 "設備: " + dev;

    sendAuditBeacon(title, body, "email,white_check_mark");
    logPageVisit(email);
  }

  // Inject compact collapsible floating identity badge at bottom left (XSS-safe textContent)
  function renderIdentityBadge(email) {
    let existing = document.getElementById("rsi-identity-badge");
    if (existing) existing.remove();

    const isMob = window.innerWidth <= 768;
    const badge = document.createElement("div");
    badge.id = "rsi-identity-badge";
    badge.setAttribute("role", "status");
    badge.setAttribute("aria-label", "已識別訪客身份");

    const row = document.createElement("div");
    row.style.cssText = "display:flex;align-items:center;gap:6px;font-family:system-ui,-apple-system,sans-serif;font-size:11px;";

    const dot = document.createElement("span");
    dot.style.cssText = "display:inline-block;width:7px;height:7px;border-radius:50%;background:#10B981;box-shadow:0 0 6px #10B981;flex-shrink:0;";

    const details = document.createElement("span");
    details.style.cssText = "display:inline-flex;align-items:center;gap:5px;";

    const emailEl = document.createElement("strong");
    emailEl.style.cssText = `color:#F1F5F9;max-width:${isMob ? "105px" : "150px"};overflow:hidden;text-overflow:ellipsis;white-space:nowrap;font-weight:600;`;
    emailEl.textContent = email;

    const switchBtn = document.createElement("button");
    switchBtn.type = "button";
    switchBtn.id = "rsi-switch-identity-btn";
    switchBtn.textContent = "切換";
    switchBtn.style.cssText = "background:none;border:none;border-bottom:1px dotted #F59E0B;color:#F59E0B;cursor:pointer;font-size:11px;padding:0;margin-left:2px;";

    const collapseBtn = document.createElement("button");
    collapseBtn.type = "button";
    collapseBtn.setAttribute("aria-label", "收合或展開訪客徽章");
    collapseBtn.title = "收合／展開";
    collapseBtn.textContent = "×";
    collapseBtn.style.cssText = "background:none;border:none;color:#94A3B8;cursor:pointer;font-size:13px;line-height:1;padding:0 2px;margin-left:2px;";

    details.appendChild(emailEl);
    details.appendChild(switchBtn);
    row.appendChild(dot);
    row.appendChild(details);
    row.appendChild(collapseBtn);
    badge.appendChild(row);

    badge.style.cssText = `position:fixed;bottom:${isMob ? "76px" : "14px"};left:${isMob ? "10px" : "14px"};right:auto;z-index:9400;background:rgba(21,19,17,0.84);backdrop-filter:blur(10px);-webkit-backdrop-filter:blur(10px);border:1px solid rgba(245,158,11,0.3);border-radius:9999px;padding:4px 10px;box-shadow:0 6px 18px rgba(0,0,0,0.28);opacity:0.78;transition:opacity 0.2s ease,padding 0.2s ease;`;
    badge.addEventListener("mouseenter", function () { badge.style.opacity = "1"; });
    badge.addEventListener("mouseleave", function () { badge.style.opacity = "0.78"; });

    let collapsed = isMob;
    const syncCollapsed = () => {
      details.style.display = collapsed ? "none" : "inline-flex";
      collapseBtn.textContent = collapsed ? "ID" : "×";
      collapseBtn.style.fontSize = collapsed ? "10px" : "13px";
      badge.style.padding = collapsed ? "4px 8px" : "4px 10px";
    };
    syncCollapsed();

    collapseBtn.addEventListener("click", function () {
      collapsed = !collapsed;
      syncCollapsed();
    });

    switchBtn.addEventListener("click", function () {
      localStorage.removeItem(STORAGE_KEY);
      badge.remove();
      showEmailModal();
    });

    document.body.appendChild(badge);
  }

  // Show Email input modal
  function showEmailModal() {
    if (document.getElementById("rsi-email-modal-overlay")) return;

    // Inject styles
    if (!document.getElementById("rsi-email-modal-styles")) {
      const style = document.createElement("style");
      style.id = "rsi-email-modal-styles";
      style.textContent = `
        #rsi-email-modal-overlay {
          position: fixed;
          top: 0; left: 0; right: 0; bottom: 0;
          background: rgba(8, 12, 22, 0.88);
          backdrop-filter: blur(14px);
          -webkit-backdrop-filter: blur(14px);
          z-index: 9999999;
          display: flex;
          align-items: center;
          justify-content: center;
          padding: 20px;
          animation: rsiFadeIn 0.35s cubic-bezier(0.16, 1, 0.3, 1);
        }
        @keyframes rsiFadeIn {
          from { opacity: 0; }
          to { opacity: 1; }
        }
        .rsi-email-card {
          width: 100%;
          max-width: 440px;
          background: #0F172A;
          border: 1px solid rgba(245, 158, 11, 0.4);
          border-radius: 18px;
          padding: 32px 28px;
          box-shadow: 0 25px 60px -15px rgba(0, 0, 0, 0.9), 0 0 35px rgba(245, 158, 11, 0.12);
          color: #F8FAFC;
          font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
          position: relative;
        }
        .rsi-email-badge {
          display: inline-flex;
          align-items: center;
          gap: 6px;
          font-size: 11px;
          font-weight: 700;
          letter-spacing: 0.08em;
          color: #F59E0B;
          background: rgba(245, 158, 11, 0.12);
          border: 1px solid rgba(245, 158, 11, 0.3);
          border-radius: 9999px;
          padding: 4px 12px;
          margin-bottom: 14px;
          text-transform: uppercase;
        }
        .rsi-email-title {
          font-size: 20px;
          font-weight: 700;
          color: #FFFFFF;
          margin: 0 0 8px 0;
          line-height: 1.3;
        }
        .rsi-email-desc {
          font-size: 13.5px;
          line-height: 1.55;
          color: #94A3B8;
          margin-bottom: 22px;
        }
        .rsi-input-group {
          margin-bottom: 16px;
        }
        .rsi-email-input {
          width: 100%;
          box-sizing: border-box;
          padding: 13px 16px;
          background: #020617;
          border: 1.5px solid #334155;
          border-radius: 10px;
          color: #F8FAFC;
          font-size: 15px;
          outline: none;
          transition: all 0.2s ease;
        }
        .rsi-email-input:focus {
          border-color: #F59E0B;
          box-shadow: 0 0 0 3px rgba(245, 158, 11, 0.2);
        }
        .rsi-email-btn {
          width: 100%;
          padding: 13px;
          background: linear-gradient(135deg, #F59E0B 0%, #D97706 100%);
          border: none;
          border-radius: 10px;
          color: #0F172A;
          font-size: 15px;
          font-weight: 700;
          cursor: pointer;
          transition: all 0.2s ease;
          display: flex;
          align-items: center;
          justify-content: center;
          gap: 8px;
        }
        .rsi-email-btn:hover {
          filter: brightness(1.1);
          transform: translateY(-1px);
          box-shadow: 0 8px 20px rgba(245, 158, 11, 0.3);
        }
        .rsi-email-footer {
          margin-top: 18px;
          font-size: 12px;
          color: #64748B;
          text-align: center;
          line-height: 1.5;
        }
        .rsi-error-msg {
          color: #EF4444;
          font-size: 12px;
          margin-top: 6px;
          display: none;
        }
      `;
      document.head.appendChild(style);
    }

    const overlay = document.createElement("div");
    overlay.id = "rsi-email-modal-overlay";
    overlay.setAttribute("role", "dialog");
    overlay.setAttribute("aria-modal", "true");
    overlay.setAttribute("aria-labelledby", "rsi-email-modal-title");
    overlay.innerHTML = `
      <div class="rsi-email-card">
        <div class="rsi-email-badge">
          <span>🏛️</span> RSI Group · 企業架構審閱
        </div>
        <h2 class="rsi-email-title" id="rsi-email-modal-title">閱讀存取確認</h2>
        <p class="rsi-email-desc">本專案包含 2027 IT 營運藍圖與核心投資評估報告。請輸入您的公司 Email 即可開始閱讀：</p>
        
        <form id="rsi-email-form" novalidate>
          <div class="rsi-input-group">
            <label for="rsi-email-input-field" style="display:block;font-size:12px;color:#CBD5E1;margin-bottom:6px;">公司或聯絡 Email（例如：user@rsiglobal.com）</label>
            <input type="email" id="rsi-email-input-field" class="rsi-email-input" style="font-size:16px;" placeholder="name@company.com" required autocomplete="email" inputmode="email" />
            <div id="rsi-email-error" class="rsi-error-msg" role="alert">請輸入有效的 Email 地址</div>
          </div>
          <button type="submit" class="rsi-email-btn" id="rsi-submit-btn">
            <span>開始查閱完整報告</span>
            <span>→</span>
          </button>
        </form>

        <div class="rsi-email-footer">
          🔒 免密碼驗證 · 一次登記本機永久記憶 · 動態自動通報至管理團隊
        </div>
      </div>
    `;
    document.body.appendChild(overlay);

    const input = document.getElementById("rsi-email-input-field");
    const form = document.getElementById("rsi-email-form");
    const errorEl = document.getElementById("rsi-email-error");

    setTimeout(() => {
      if (input) input.focus();
    }, 100);

    form.addEventListener("submit", function (e) {
      e.preventDefault();
      const val = (input.value || "").trim().toLowerCase();
      const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
      if (!val || !emailRegex.test(val)) {
        errorEl.style.display = "block";
        input.focus();
        return;
      }
      errorEl.style.display = "none";

      try {
        localStorage.setItem(STORAGE_KEY, val);
      } catch (err) {}

      currentEmail = val;

      // Animate out
      overlay.style.transition = "opacity 0.3s ease";
      overlay.style.opacity = "0";
      setTimeout(() => {
        overlay.remove();
      }, 300);

      // Send telemetry
      logRegistration(val);
      renderIdentityBadge(val);
    });
  }

  // Document & File Download Tracker
  document.addEventListener("click", function (e) {
    const a = e.target.closest("a");
    if (!a || !a.href) return;
    const href = a.href;
    if (/\.(docx|csv|pdf|pptx|xlsx|zip)$/i.test(href)) {
      const fileName = href.split("/").pop();
      const timeStr = getTaipeiTimeString();
      const user = currentEmail || "未具名訪客";
      const title = "[RSI 文件下載] " + user;
      const body = "訪客身分: " + user + "\n" +
                   "下載檔案: " + fileName + "\n" +
                   "所在頁面: " + (document.title || window.location.pathname) + "\n" +
                   "時間: " + timeStr;
      sendAuditBeacon(title, body, "floppy_disk,inbox_tray");
    }
  });

  // Init logic on DOM Ready
  function init() {
    if (isDashboard) {
      console.log("[RSI Telemetry] Dashboard mode: Email gate exempt.");
      return;
    }

    if (currentEmail) {
      logPageVisit(currentEmail);
      renderIdentityBadge(currentEmail);
    } else {
      showEmailModal();
    }
  }

  if (document.readyState === "complete" || document.readyState === "interactive") {
    init();
  } else {
    window.addEventListener("DOMContentLoaded", init);
  }

  // Global helper API
  window.RSITelemetry = {
    getEmail: function () { return currentEmail; },
    resetEmail: function () {
      localStorage.removeItem(STORAGE_KEY);
      window.location.reload();
    }
  };
})();
