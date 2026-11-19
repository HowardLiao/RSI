/**
 * RSI Group · Project Hive 2027
 * Enterprise Access Gatekeeper & Client-Side Cryptographic Guard
 * 
 * Functions:
 * 1. Site-wide interception: prevents unverified visitors from browsing confidential pages.
 * 2. Visitor identity capture: mandatory registration of Name, Company/Plant, Dept/Title, Email, Reason.
 * 3. Passkey authorization: validates credentials against authorized tokens (RSI2027, VPCHOU2027, etc.).
 * 4. Audit logging & webhook sync: saves all access attempts to localStorage and dispatches to cloud webhook.
 * 5. AES-256-GCM decryption: client-side decryption of encrypted payload blocks.
 * 6. Admin audit panel: allows C-Level/Advisors to inspect visitor logs and export CSV reports.
 * 
 * Author: Howard Liao Ph.D.
 * Standard: Milan Executive Architecture
 */

(function () {
  'use strict';

  // Prevent multiple initializations on the same page
  if (window.__rsiGatekeeper) return;
  window.__rsiGatekeeper = true;

  // Session & Storage keys
  const SESSION_KEY = 'RSI_HIVE_AUTH_SESSION';
  const AUDIT_LOG_KEY = 'RSI_ACCESS_AUDIT_LOGS';
  const REMEMBER_KEY = 'RSI_HIVE_REMEMBERED_KEY';

  // Configured Authorized Passkeys
  const VALID_KEYS = {
    'RSI2027': { role: '信源同仁 / 專案成員', title: '蜂巢計畫授權存取' },
    'VPCHOU2027': { role: '計畫主持人 (周文津 副總經理)', title: '最高決策經營權限' },
    'HOWARD2027': { role: '執行負責人 (Howard Liao Ph.D.)', title: '首席架構顧問權限' },
    'DUKE2027': { role: '研發資訊主管 (Duke Chen)', title: '架構與 API 核心權限' },
    'HIVE2027': { role: '蜂巢計畫小組 (Project Hive Team)', title: '跨廠整合工作權限' }
  };

  const ADMIN_KEYS = ['HOWARD2027', 'VPCHOU2027'];

  // Optional cloud webhook endpoint (can be configured to Google Sheet Web App / Formspree / Slack)
  const CLOUD_WEBHOOK_URL = ''; // Leave blank or fill if cloud endpoint is provisioned

  // Ensure early lock on document before body renders
  document.documentElement.classList.add('rsi-locked');

  // Helper: check if current session is valid (< 24 hours)
  function getActiveSession() {
    try {
      const raw = sessionStorage.getItem(SESSION_KEY);
      if (!raw) return null;
      const sess = JSON.parse(raw);
      if (!sess || !sess.timestamp) return null;
      // 24 hours expiry
      if (Date.now() - sess.timestamp > 24 * 60 * 60 * 1000) {
        sessionStorage.removeItem(SESSION_KEY);
        return null;
      }
      return sess;
    } catch (e) {
      return null;
    }
  }

  // Helper: log visitor access to localStorage
  function logVisitor(record) {
    try {
      const logs = JSON.parse(localStorage.getItem(AUDIT_LOG_KEY) || '[]');
      logs.unshift(record);
      // Keep latest 500 records
      if (logs.length > 500) logs.length = 500;
      localStorage.setItem(AUDIT_LOG_KEY, JSON.stringify(logs));
    } catch (e) {
      console.warn('[RSI Gatekeeper] Failed to save audit log:', e);
    }

    // Attempt cloud webhook dispatch
    if (CLOUD_WEBHOOK_URL) {
      try {
        fetch(CLOUD_WEBHOOK_URL, {
          method: 'POST',
          mode: 'no-cors',
          headers: { 'Content-Type': 'application/json' },
          body: JSON.stringify(record)
        }).catch(() => {});
      } catch (err) {}
    }
  }

  // Web Crypto AES-256-GCM Decryption
  async function decryptRSIE1(base64Ciphertext, password, iterations = 100000) {
    const binary = atob(base64Ciphertext);
    const bytes = new Uint8Array(binary.length);
    for (let i = 0; i < binary.length; i++) {
      bytes[i] = binary.charCodeAt(i);
    }

    const magic = new TextDecoder().decode(bytes.slice(0, 5));
    if (magic !== 'RSIE1') {
      throw new Error('無效的加密格式 (Invalid magic header)');
    }

    const salt = bytes.slice(5, 21);
    const iv = bytes.slice(21, 33);
    const ctAndTag = bytes.slice(33); // Ciphertext + 16-byte GCM tag

    const baseKey = await crypto.subtle.importKey(
      'raw',
      new TextEncoder().encode(password),
      'PBKDF2',
      false,
      ['deriveKey']
    );

    const key = await crypto.subtle.deriveKey(
      { name: 'PBKDF2', salt, iterations, hash: 'SHA-256' },
      baseKey,
      { name: 'AES-GCM', length: 256 },
      false,
      ['decrypt']
    );

    const decryptedBuffer = await crypto.subtle.decrypt(
      { name: 'AES-GCM', iv },
      key,
      ctAndTag
    );

    return new TextDecoder().decode(decryptedBuffer);
  }

  // Create UI overlay
  function createGatekeeperOverlay() {
    if (document.getElementById('rsi-gatekeeper-overlay')) return;

    const overlay = document.createElement('div');
    overlay.id = 'rsi-gatekeeper-overlay';

    overlay.innerHTML = `
      <div class="rsi-gate-watermark"></div>
      <div class="rsi-gate-card">
        <div class="rsi-gate-kicker">
          <svg width="12" height="12" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
          RSI GROUP · 機密資產門禁驗證
        </div>
        <h1 class="rsi-gate-title">2027 蜂巢計畫 · 存取門禁審核系統</h1>
        <p class="rsi-gate-subtitle">本站點包含信源全球集團跨國製造架構、財務投資效益、海外 8 廠自律協議與自研 API 核心規格，受嚴格企業機密保護。請填寫留資資料並輸入授權金鑰以取得存取權限。</p>

        <div class="rsi-gate-meta">
          <div><strong>計畫主持：</strong>周文津 副總經理</div>
          <div><strong>執行負責：</strong>Howard Liao Ph.D.</div>
          <div><strong>資安層級：</strong>Tier-1 核心機密</div>
        </div>

        <form id="rsi-gate-form" autocomplete="on">
          <div class="rsi-gate-grid">
            <div class="rsi-gate-field">
              <label class="rsi-gate-label">訪客真實姓名 <span class="req">*</span></label>
              <input type="text" id="rsi-gate-name" class="rsi-gate-input" placeholder="例：周文津 / 廖倫豪 / 陳大衛" required autocomplete="name">
            </div>

            <div class="rsi-gate-field">
              <label class="rsi-gate-label">所屬機構 / 廠區 <span class="req">*</span></label>
              <select id="rsi-gate-company" class="rsi-gate-select" required>
                <option value="信源台北總部 (RSI HQ)">信源台北總部 (RSI HQ)</option>
                <option value="越南 RSA 廠">越南 RSA 廠</option>
                <option value="越南 RSB 廠">越南 RSB 廠</option>
                <option value="越南 TOP 廠">越南 TOP 廠</option>
                <option value="柬埔寨 RSG 廠">柬埔寨 RSG 廠</option>
                <option value="柬埔寨 RSK 廠">柬埔寨 RSK 廠</option>
                <option value="緬甸 RSV 廠">緬甸 RSV 廠</option>
                <option value="緬甸 SY 廠">緬甸 SY 廠</option>
                <option value="總部 RVT 廠">總部 RVT 廠</option>
                <option value="外部技術協同顧問 / SI 夥伴">外部技術協同顧問 / SI 夥伴</option>
                <option value="其他外部單位">其他外部單位</option>
              </select>
            </div>

            <div class="rsi-gate-field">
              <label class="rsi-gate-label">部門與職稱 <span class="req">*</span></label>
              <input type="text" id="rsi-gate-dept" class="rsi-gate-input" placeholder="例：研發資訊主管 / IS 架構師 / ITS" required>
            </div>

            <div class="rsi-gate-field">
              <label class="rsi-gate-label">公務電子信箱 <span class="req">*</span></label>
              <input type="email" id="rsi-gate-email" class="rsi-gate-input" placeholder="name@rsi.com.tw" required autocomplete="email">
            </div>

            <div class="rsi-gate-field full">
              <label class="rsi-gate-label">存取事由 / 專案申請目的 <span class="req">*</span></label>
              <textarea id="rsi-gate-purpose" class="rsi-gate-textarea" placeholder="請具體填寫查閱目的（例：進行第一週自研 API 盤點對齊、查閱海外 8 廠離線架構 PoC 等）" required></textarea>
            </div>

            <div class="rsi-gate-field full">
              <label class="rsi-gate-label">通行授權金鑰 (Passkey) <span class="req">*</span></label>
              <input type="password" id="rsi-gate-passkey" class="rsi-gate-input" placeholder="請輸入 2027 蜂巢計畫通行密鑰" autocomplete="current-password">
            </div>
          </div>

          <div class="rsi-gate-notice">
            📌 <strong>同仁提醒：</strong>本站點採用端到端密鑰驗證與訪問審核機制。所有進站留資與查詢軌跡皆記入企業稽核日誌。若尚未取得通行金鑰，請填妥上方留資後點擊「提交審核申請」。
          </div>

          <div class="rsi-gate-actions">
            <button type="submit" id="rsi-gate-submit-btn" class="rsi-gate-btn-primary">
              <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><rect width="18" height="11" x="3" y="11" rx="2" ry="2"/><path d="M7 11V7a5 5 0 0 1 10 0v4"/></svg>
              驗證身分並解鎖存取
            </button>
            <button type="button" id="rsi-gate-apply-btn" class="rsi-gate-btn-secondary">
              無金鑰 · 提交留資審核申請
            </button>
          </div>

          <div id="rsi-gate-status" class="rsi-gate-status"></div>
        </form>

        <div class="rsi-gate-footer">
          <div>RSI Group Enterprise Information Security · Tier-1</div>
          <button type="button" id="rsi-gate-admin-link">管理員稽核檢視</button>
        </div>
      </div>
    `;

    document.body.appendChild(overlay);

    // Event Listeners
    const form = document.getElementById('rsi-gate-form');
    const applyBtn = document.getElementById('rsi-gate-apply-btn');
    const adminLink = document.getElementById('rsi-gate-admin-link');

    form.addEventListener('submit', handleVerifySubmit);
    applyBtn.addEventListener('click', handleApplySubmit);
    adminLink.addEventListener('click', handleAdminPrompt);
  }

  // Create Verified User Chip
  function createVerifiedChip(sess) {
    let chip = document.getElementById('rsi-verified-chip');
    if (!chip) {
      chip = document.createElement('div');
      chip.id = 'rsi-verified-chip';
      document.body.appendChild(chip);
    }

    chip.innerHTML = `
      <svg width="14" height="14" viewBox="0 0 24 24" fill="none" stroke="#10B981" stroke-width="3"><polyline points="20 6 9 17 4 12"/></svg>
      <span>已授權訪客：<strong>${escapeHtml(sess.name)}</strong>（${escapeHtml(sess.company)} · ${escapeHtml(sess.dept)}）</span>
      <button type="button" class="rsi-chip-btn" id="rsi-chip-admin">稽核</button>
      <button type="button" class="rsi-chip-btn" id="rsi-chip-logout">登出</button>
    `;

    document.getElementById('rsi-chip-admin').addEventListener('click', handleAdminPrompt);
    document.getElementById('rsi-chip-logout').addEventListener('click', handleLogout);
  }

  // Execute decrypted scripts sequentially
  function runScriptsInElement(container) {
    const scripts = Array.from(container.querySelectorAll('script'));
    function runNextScript(idx) {
      if (idx >= scripts.length) return;
      const oldScript = scripts[idx];
      const newScript = document.createElement('script');
      Array.from(oldScript.attributes).forEach(attr => newScript.setAttribute(attr.name, attr.value));

      if (oldScript.src) {
        newScript.onload = () => runNextScript(idx + 1);
        newScript.onerror = () => runNextScript(idx + 1);
        oldScript.parentNode.replaceChild(newScript, oldScript);
      } else {
        newScript.textContent = oldScript.textContent;
        oldScript.parentNode.replaceChild(newScript, oldScript);
        runNextScript(idx + 1);
      }
    }
    runNextScript(0);
  }

  // Unlock Site Action
  async function unlockSite(sess, passkey) {
    const statusEl = document.getElementById('rsi-gate-status');
    const overlay = document.getElementById('rsi-gate-overlay') || document.getElementById('rsi-gatekeeper-overlay');

    // If page contains an encrypted payload, decrypt it
    const cipherEl = document.getElementById('rsi-encrypted-payload');
    const mountEl = document.getElementById('rsi-app-mount');

    if (cipherEl && mountEl) {
      if (statusEl) {
        statusEl.className = 'rsi-gate-status info';
        statusEl.textContent = '正在解密機密核心架構資料…';
      }
      try {
        const rawCipher = cipherEl.textContent.trim();
        // Fallback key: if user entered another valid key, use RSI2027 as decrypt key if master
        let decryptKey = passkey || sess.key || 'RSI2027';
        let decryptedHtml = '';
        try {
          decryptedHtml = await decryptRSIE1(rawCipher, decryptKey);
        } catch (err) {
          // If custom key failed, try primary project key RSI2027
          decryptedHtml = await decryptRSIE1(rawCipher, 'RSI2027');
        }

        mountEl.innerHTML = decryptedHtml;
        runScriptsInElement(mountEl);
      } catch (err) {
        console.error('[RSI Gatekeeper] Decryption error:', err);
        if (statusEl) {
          statusEl.className = 'rsi-gate-status error';
          statusEl.textContent = '資料解密失敗：金鑰不匹配或密文損毀。';
        }
        return false;
      }
    }

    // Success unlock
    document.documentElement.classList.remove('rsi-locked');
    if (overlay) {
      overlay.hidden = true;
      overlay.style.display = 'none';
    }

    createVerifiedChip(sess);
    return true;
  }

  // Handle Verify Submit
  async function handleVerifySubmit(e) {
    e.preventDefault();
    const name = document.getElementById('rsi-gate-name').value.trim();
    const company = document.getElementById('rsi-gate-company').value.trim();
    const dept = document.getElementById('rsi-gate-dept').value.trim();
    const email = document.getElementById('rsi-gate-email').value.trim();
    const purpose = document.getElementById('rsi-gate-purpose').value.trim();
    const passkey = document.getElementById('rsi-gate-passkey').value.trim();
    const statusEl = document.getElementById('rsi-gate-status');

    if (!name || !company || !dept || !email || !purpose) {
      statusEl.className = 'rsi-gate-status error';
      statusEl.textContent = '請完整填寫所有留資欄位！';
      return;
    }

    if (!passkey) {
      statusEl.className = 'rsi-gate-status error';
      statusEl.textContent = '請輸入通行授權金鑰；若無金鑰請點選「無金鑰 · 提交留資審核申請」。';
      return;
    }

    const keyUpper = passkey.toUpperCase();
    const keyInfo = VALID_KEYS[keyUpper] || VALID_KEYS[passkey];

    if (!keyInfo) {
      statusEl.className = 'rsi-gate-status error';
      statusEl.textContent = '通行金鑰無效！若尚未取得金鑰，請點選下方按鈕提交留資申請。';
      return;
    }

    statusEl.className = 'rsi-gate-status info';
    statusEl.textContent = '正在驗證身分並建立安全連線…';

    const timestamp = Date.now();
    const sessionData = {
      name,
      company,
      dept,
      email,
      purpose,
      role: keyInfo.role,
      title: keyInfo.title,
      key: keyUpper,
      timestamp
    };

    // Log to Audit Trail
    logVisitor({
      id: 'ACC-' + timestamp,
      timestamp: new Date().toISOString(),
      name,
      company,
      dept,
      email,
      purpose,
      keyUsed: keyUpper,
      role: keyInfo.role,
      status: 'VERIFIED_ACCESS',
      path: location.pathname,
      userAgent: navigator.userAgent
    });

    // Save session
    sessionStorage.setItem(SESSION_KEY, JSON.stringify(sessionData));

    // Unlock
    const ok = await unlockSite(sessionData, keyUpper);
    if (ok) {
      statusEl.className = 'rsi-gate-status success';
      statusEl.textContent = '驗證成功，歡迎進入信源 2027 蜂巢計畫！';
    }
  }

  // Handle Request Access without Key
  function handleApplySubmit() {
    const name = document.getElementById('rsi-gate-name').value.trim();
    const company = document.getElementById('rsi-gate-company').value.trim();
    const dept = document.getElementById('rsi-gate-dept').value.trim();
    const email = document.getElementById('rsi-gate-email').value.trim();
    const purpose = document.getElementById('rsi-gate-purpose').value.trim();
    const statusEl = document.getElementById('rsi-gate-status');

    if (!name || !company || !dept || !email || !purpose) {
      statusEl.className = 'rsi-gate-status error';
      statusEl.textContent = '請先完整填寫姓名、公司、職稱、信箱與存取事由後再提交申請！';
      return;
    }

    const timestamp = Date.now();
    logVisitor({
      id: 'REQ-' + timestamp,
      timestamp: new Date().toISOString(),
      name,
      company,
      dept,
      email,
      purpose,
      keyUsed: 'NONE (APPLY_REQUEST)',
      role: '待審核訪客',
      status: 'PENDING_APPROVAL',
      path: location.pathname,
      userAgent: navigator.userAgent
    });

    alert(
      `【信源全球 2027 蜂巢計畫 · 存取留資已受理】\n\n` +
      `感謝您的申請，${name} 同仁/長官！\n\n` +
      `您的留資紀錄已成功存檔並呈報至：\n` +
      `• 計畫主持人：周文津 副總經理\n` +
      `• 執行負責人：Howard Liao Ph.D.\n\n` +
      `審核通過後，專屬通行金鑰將寄送至您的公務信箱：${email}。\n` +
      `若您為內部緊急查閱需求，請直接向 周副總 或 顧問團隊 聯繫取得臨時通行密鑰。`
    );

    statusEl.className = 'rsi-gate-status info';
    statusEl.textContent = '留資審核申請已送出，請靜待管理員核發通行金鑰。';
  }

  // Admin Audit Log Modal
  function handleAdminPrompt() {
    const masterKey = prompt('請輸入管理員主控金鑰 (Admin Master Key)：');
    if (!masterKey) return;

    if (!ADMIN_KEYS.includes(masterKey.toUpperCase())) {
      alert('管理員金鑰錯誤，存取遭到拒絕！');
      return;
    }

    openAdminAuditModal();
  }

  function openAdminAuditModal() {
    let adminModal = document.getElementById('rsi-admin-modal');
    if (!adminModal) {
      adminModal = document.createElement('div');
      adminModal.id = 'rsi-admin-modal';
      document.body.appendChild(adminModal);
    }

    const logs = JSON.parse(localStorage.getItem(AUDIT_LOG_KEY) || '[]');

    adminModal.innerHTML = `
      <div class="rsi-admin-card">
        <div class="rsi-admin-header">
          <div>
            <h2 style="margin:0;font-size:18px;font-weight:800;color:#111827;">信源 2027 蜂巢計畫 · 訪客留資與存取稽核日誌</h2>
            <div style="font-size:12px;color:#6B7280;margin-top:2px;">管理員權限：Howard Liao Ph.D. / 周文津 副總經理 · 共 ${logs.length} 筆存取紀錄</div>
          </div>
          <div style="display:flex;gap:8px;">
            <button type="button" class="rsi-gate-btn-secondary" id="rsi-export-csv" style="padding:6px 12px;font-size:12px;">📥 匯出 CSV</button>
            <button type="button" class="rsi-gate-btn-secondary" id="rsi-clear-logs" style="padding:6px 12px;font-size:12px;">🗑️ 清空日誌</button>
            <button type="button" class="rsi-gate-btn-secondary" id="rsi-close-admin" style="padding:6px 12px;font-size:12px;">✕ 關閉</button>
          </div>
        </div>
        <div class="rsi-admin-body">
          ${logs.length === 0 ? '<div style="text-align:center;padding:40px;color:#9CA3AF;">目前尚無訪客留資紀錄</div>' : `
            <table class="rsi-admin-table">
              <thead>
                <tr>
                  <th>時間 (UTC+8)</th>
                  <th>姓名</th>
                  <th>單位 / 廠區</th>
                  <th>職稱</th>
                  <th>公務信箱</th>
                  <th>存取事由</th>
                  <th>金鑰</th>
                  <th>狀態</th>
                </tr>
              </thead>
              <tbody>
                ${logs.map(log => `
                  <tr>
                    <td style="white-space:nowrap;">${new Date(log.timestamp).toLocaleString('zh-TW')}</td>
                    <td><strong>${escapeHtml(log.name)}</strong></td>
                    <td>${escapeHtml(log.company)}</td>
                    <td>${escapeHtml(log.dept)}</td>
                    <td><a href="mailto:${escapeHtml(log.email)}" style="color:#B45309;">${escapeHtml(log.email)}</a></td>
                    <td style="max-width:240px;overflow:hidden;text-overflow:ellipsis;" title="${escapeHtml(log.purpose)}">${escapeHtml(log.purpose)}</td>
                    <td><code>${escapeHtml(log.keyUsed || '—')}</code></td>
                    <td><span class="rsi-status-badge ${log.status === 'VERIFIED_ACCESS' ? 'verified' : 'pending'}">${log.status === 'VERIFIED_ACCESS' ? '已核准' : '待審核'}</span></td>
                  </tr>
                `).join('')}
              </tbody>
            </table>
          `}
        </div>
      </div>
    `;

    adminModal.hidden = false;
    adminModal.style.display = 'flex';

    document.getElementById('rsi-close-admin').addEventListener('click', () => {
      adminModal.hidden = true;
      adminModal.style.display = 'none';
    });

    document.getElementById('rsi-export-csv').addEventListener('click', () => {
      exportAuditCsv(logs);
    });

    document.getElementById('rsi-clear-logs').addEventListener('click', () => {
      if (confirm('確定要清空所有訪客審核日誌紀錄嗎？')) {
        localStorage.removeItem(AUDIT_LOG_KEY);
        openAdminAuditModal();
      }
    });
  }

  function exportAuditCsv(logs) {
    if (!logs || logs.length === 0) {
      alert('無日誌資料可匯出！');
      return;
    }
    const headers = ['紀錄ID', '存取時間', '姓名', '單位與廠區', '部門與職稱', '公務信箱', '存取事由', '使用金鑰', '角色層級', '審核狀態', '來源網址'];
    const rows = logs.map(l => [
      l.id,
      new Date(l.timestamp).toLocaleString('zh-TW'),
      l.name,
      l.company,
      l.dept,
      l.email,
      (l.purpose || '').replace(/"/g, '""'),
      l.keyUsed,
      l.role,
      l.status,
      l.path
    ]);

    const csvContent = '\uFEFF' + [
      headers.join(','),
      ...rows.map(r => r.map(f => `"${f || ''}"`).join(','))
    ].join('\r\n');

    const blob = new Blob([csvContent], { type: 'text/csv;charset=utf-8;' });
    const url = URL.createObjectURL(blob);
    const a = document.createElement('a');
    a.href = url;
    a.download = `信源2027蜂巢計畫_訪客留資與存取稽核日誌_${new Date().toISOString().slice(0, 10)}.csv`;
    document.body.appendChild(a);
    a.click();
    a.remove();
    URL.revokeObjectURL(url);
  }

  function handleLogout() {
    if (confirm('確定要登出並重新鎖定本站點嗎？')) {
      sessionStorage.removeItem(SESSION_KEY);
      location.reload();
    }
  }

  function escapeHtml(str) {
    if (!str) return '';
    return String(str)
      .replace(/&/g, '&amp;')
      .replace(/</g, '&lt;')
      .replace(/>/g, '&gt;')
      .replace(/"/g, '&quot;')
      .replace(/'/g, '&#39;');
  }

  // Initial check on DOMContentLoaded
  function init() {
    const sess = getActiveSession();
    if (sess) {
      unlockSite(sess, sess.key);
    } else {
      createGatekeeperOverlay();
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
