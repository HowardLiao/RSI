/* ==========================================================================
   RSI 2027 Project Hive — Neon 5-Dimension Interactive Engine (v7.5.0)
   ========================================================================== */
(function () {
  'use strict';

  const FX_RATE = 31.5;
  const FINOPS_SCOPES = {
    full: {
      capUsd: 1390000,
      capNtd: 43785000,
      labelZh: '2027 全年四大主架構 (25 項 WBS 總額)',
      descZh: '基於 2027 全年 25 項 WBS 總預算 $1,390,000 USD（約 NT$ 4,378.5 萬），動態調整「空運包機防禦」與「大貨布損改善」，即時驗證現金流回本速度與 ROI。'
    },
    phase1: {
      capUsd: 640000,
      capNtd: 20160000,
      labelZh: 'Phase 1 數位底座 (Pillar I · P1-1～P1-8)',
      descZh: '基於 Phase 1 數位底座與治理預算 $640,000 USD（約 NT$ 2,016 萬，依 D04 核定），即時模擬第一階段投資回收與硬性現金流對沖效益。'
    }
  };

  let currentFinOpsScope = 'full';
  let finopsBreakevenChart = null;
  let activeWbsCategory = 'all';
  let walTickerTimer = null;
  let walCounters = { s1: 284, s2: 178, s3: 412 };
  let gateOverrideState = { active: false, timestamp: '' };

  /* ------------------------------------------------------------------------
     Dimension 1: FinOps Scope Toggle + Accurate Math + 24M Breakeven Chart
     ------------------------------------------------------------------------ */
  function setFinOpsScope(scopeKey) {
    if (!FINOPS_SCOPES[scopeKey]) return;
    currentFinOpsScope = scopeKey;
    document.querySelectorAll('.finops-scope-btn').forEach((btn) => {
      btn.classList.toggle('active', btn.dataset.scope === scopeKey);
    });
    const sc = FINOPS_SCOPES[scopeKey];
    const capValEl = document.getElementById('finopsCapBaselineVal');
    const capSubEl = document.getElementById('finopsCapBaselineSub');
    const descEl = document.getElementById('t-finopsDesc');
    if (capValEl) capValEl.textContent = 'NT$ ' + sc.capNtd.toLocaleString();
    if (capSubEl) capSubEl.textContent = '$' + sc.capUsd.toLocaleString() + ' USD · ' + sc.labelZh;
    if (descEl && (typeof currentLang === 'undefined' || currentLang === 'zh')) {
      descEl.textContent = sc.descZh;
    }
    neonUpdateFinOps();
  }

  function renderFinOpsBreakevenChart(capNtd, annualSavingsNtd, paybackMonths) {
    const canvas = document.getElementById('finopsBreakevenCanvas');
    if (!canvas || typeof Chart === 'undefined') return;

    const months = Array.from({ length: 25 }, (_, i) => (i === 0 ? 'M0' : 'M' + i));
    const monthlySave = annualSavingsNtd / 12;
    const cumSavings = months.map((_, i) => Math.round((monthlySave * i) / 10000)); // 萬 NTD
    const capLine = months.map(() => Math.round(capNtd / 10000));

    const badge = document.getElementById('finopsBreakevenBadge');
    if (badge) {
      if (annualSavingsNtd <= 0) {
        badge.textContent = '尚無硬性節省現金流';
      } else {
        const net24 = Math.round(((monthlySave * 24) - capNtd) / 10000);
        badge.textContent = `回本交叉點：第 ${paybackMonths} 個月 ｜ 24M 淨現金貢獻：${net24 >= 0 ? '+' : ''}NT$ ${net24.toLocaleString()} 萬`;
      }
    }

    if (finopsBreakevenChart) {
      finopsBreakevenChart.data.datasets[0].data = cumSavings;
      finopsBreakevenChart.data.datasets[1].data = capLine;
      finopsBreakevenChart.update('none');
      return;
    }

    finopsBreakevenChart = new Chart(canvas.getContext('2d'), {
      type: 'line',
      data: {
        labels: months,
        datasets: [
          {
            label: '累積硬性節省現金流 (萬 NTD)',
            data: cumSavings,
            borderColor: '#C2410C',
            backgroundColor: 'rgba(232, 117, 36, 0.14)',
            borderWidth: 2.5,
            fill: true,
            tension: 0.25,
            pointRadius: 2,
            pointHoverRadius: 5
          },
          {
            label: 'IT 投資總基準線 CAPEX (萬 NTD)',
            data: capLine,
            borderColor: '#1C1917',
            borderDash: [6, 4],
            borderWidth: 2,
            fill: false,
            pointRadius: 0
          }
        ]
      },
      options: {
        responsive: true,
        maintainAspectRatio: false,
        interaction: { mode: 'index', intersect: false },
        plugins: {
          legend: {
            position: 'bottom',
            labels: { boxWidth: 14, font: { family: 'Inter, Noto Sans TC, sans-serif', size: 11, weight: '600' }, color: '#332E2A' }
          },
          tooltip: {
            callbacks: {
              label: (ctx) => `${ctx.dataset.label}: NT$ ${ctx.parsed.y.toLocaleString()} 萬`
            }
          }
        },
        scales: {
          x: { grid: { display: false }, ticks: { color: '#6B635B', font: { family: 'JetBrains Mono, monospace', size: 10 }, maxTicksLimit: 13 } },
          y: {
            grid: { color: 'rgba(230, 221, 208, 0.7)' },
            ticks: { color: '#6B635B', font: { family: 'JetBrains Mono, monospace', size: 10 }, callback: (v) => v + '萬' }
          }
        }
      }
    });
  }

  function neonUpdateFinOps() {
    const airInput = document.getElementById('airSavesSlider');
    const fabricInput = document.getElementById('fabricGainSlider');
    if (!airInput || !fabricInput) return;

    const lang = typeof currentLang !== 'undefined' ? currentLang : 'zh';
    const airSaves = parseInt(airInput.value, 10) || 0;
    const fabricGain = parseFloat(fabricInput.value) || 0;

    const airSavesDisp = document.getElementById('airSavesValDisplay');
    const fabricGainDisp = document.getElementById('fabricGainValDisplay');
    if (airSavesDisp) {
      airSavesDisp.innerText = airSaves + (lang === 'en' ? ' saves' : (lang === 'vi' ? ' lần' : ' 次'));
    }
    if (fabricGainDisp) {
      fabricGainDisp.innerText = fabricGain.toFixed(1) + ' %';
    }

    const airCashSaved = airSaves * 7500000;
    const fabricCashSaved = Math.round(fabricGain * 18375000);
    const totalCashSaved = airCashSaved + fabricCashSaved;

    const totalCap = FINOPS_SCOPES[currentFinOpsScope].capNtd;
    const paybackMonths = totalCashSaved > 0 ? ((totalCap / totalCashSaved) * 12).toFixed(1) : '99+';
    const roi3yr = totalCashSaved > 0 ? ((totalCashSaved * 3) / totalCap).toFixed(2) : '0.00';
    const roi1yr = totalCashSaved > 0 ? (totalCashSaved / totalCap).toFixed(2) : '0.00';

    const setTxt = (id, val) => { const el = document.getElementById(id); if (el) el.innerText = val; };
    const subPrefix = lang === 'en' ? 'approx. $' : '約 $';
    const subSuffix = lang === 'en' ? ' USD / yr' : ' USD / 年';

    setTxt('dispAirCash', 'NT$ ' + airCashSaved.toLocaleString());
    setTxt('dispAirCashSub', subPrefix + Math.round(airCashSaved / FX_RATE).toLocaleString() + subSuffix);
    setTxt('dispFabricCash', 'NT$ ' + fabricCashSaved.toLocaleString());
    setTxt('dispFabricCashSub', subPrefix + Math.round(fabricCashSaved / FX_RATE).toLocaleString() + subSuffix);
    setTxt('dispTotalCash', 'NT$ ' + totalCashSaved.toLocaleString());
    setTxt('dispTotalCashSub', subPrefix + Math.round(totalCashSaved / FX_RATE).toLocaleString() + subSuffix);

    const unitMo = lang === 'en' ? ' Months' : (lang === 'vi' ? ' Tháng' : ' 個月');
    setTxt('dispPaybackMonths', paybackMonths + unitMo);
    setTxt(
      'dispRoiRatio',
      lang === 'en'
        ? `1-Yr ROI 1 : ${roi1yr} · 3-Yr ROI 1 : ${roi3yr}`
        : `首年 ROI 1 : ${roi1yr} ｜ 3年累積 ROI 1 : ${roi3yr}`
    );

    renderFinOpsBreakevenChart(totalCap, totalCashSaved, paybackMonths);
  }

  /* ------------------------------------------------------------------------
     Dimension 2: 4-Cluster Nav Interactions, Reading Rail & Hero Count-Up
     ------------------------------------------------------------------------ */
  function initNavDropdowns() {
    const groups = document.querySelectorAll('.neon-nav-group');
    groups.forEach((group) => {
      const btn = group.querySelector('.neon-nav-trigger');
      if (!btn) return;
      btn.addEventListener('click', (e) => {
        e.stopPropagation();
        const isOpen = group.classList.contains('open');
        groups.forEach((g) => {
          g.classList.remove('open');
          const b = g.querySelector('.neon-nav-trigger');
          if (b) b.setAttribute('aria-expanded', 'false');
        });
        if (!isOpen) {
          group.classList.add('open');
          btn.setAttribute('aria-expanded', 'true');
        }
      });
      group.querySelectorAll('.neon-nav-menu a').forEach((link) => {
        link.addEventListener('click', () => {
          group.classList.remove('open');
          btn.setAttribute('aria-expanded', 'false');
        });
      });
    });

    document.addEventListener('click', () => {
      groups.forEach((g) => {
        g.classList.remove('open');
        const b = g.querySelector('.neon-nav-trigger');
        if (b) b.setAttribute('aria-expanded', 'false');
      });
    });

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        groups.forEach((g) => g.classList.remove('open'));
      }
    });
  }

  function initReadingProgressAndRail() {
    const bar = document.createElement('div');
    bar.className = 'neon-read-progress';
    bar.setAttribute('aria-hidden', 'true');
    document.body.prepend(bar);

    const chapters = [
      { id: 'hive-pipeline', label: '蜂巢時程與閘門' },
      { id: 'hive-3d-map', label: '3D 戰略全景地圖' },
      { id: 'invest-framework', label: '投資主軸與 FinOps' },
      { id: 'visual-analytics', label: '動態視覺化圖表' },
      { id: 'factory-monitor', label: '跨國廠區邊緣遙測' },
      { id: 'pillars', label: '四大核心主架構' },
      { id: 'simulator', label: '4-Gate 產前門禁' },
      { id: 'wbs-gantt', label: '25項 WBS 與甘特' },
      { id: 'recommendations', label: '六大升級節點' }
    ].filter((c) => document.getElementById(c.id));

    const rail = document.createElement('nav');
    rail.className = 'neon-section-rail';
    rail.setAttribute('aria-label', '章節進度導航');

    const railMap = new Map();
    chapters.forEach((c) => {
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.className = 'neon-rail-item';
      btn.setAttribute('data-label', c.label);
      btn.setAttribute('aria-label', '跳至 ' + c.label);
      btn.addEventListener('click', () => {
        const target = document.getElementById(c.id);
        if (target) target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      });
      rail.appendChild(btn);
      railMap.set(c.id, btn);
    });
    document.body.appendChild(rail);

    let ticking = false;
    window.addEventListener('scroll', () => {
      if (ticking) return;
      ticking = true;
      requestAnimationFrame(() => {
        const docH = document.documentElement.scrollHeight - window.innerHeight;
        const pct = docH > 0 ? Math.min(100, Math.max(0, (window.scrollY / docH) * 100)) : 0;
        bar.style.width = pct.toFixed(1) + '%';
        ticking = false;
      });
    }, { passive: true });

    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        entries.forEach((entry) => {
          if (entry.isIntersecting) {
            railMap.forEach((b) => b.classList.remove('active'));
            const activeBtn = railMap.get(entry.target.id);
            if (activeBtn) activeBtn.classList.add('active');
          }
        });
      }, { rootMargin: '-20% 0px -65% 0px' });

      chapters.forEach((c) => {
        const el = document.getElementById(c.id);
        if (el) io.observe(el);
      });
    }
  }

  function initHeroBentoCountUp() {
    const specs = [
      { id: 'bento-val-shipment', end: 7500, fmt: (v) => Math.round(v).toLocaleString() + ' 萬件' },
      { id: 'bento-val-savings', end: 3705, fmt: (v) => 'NT$ ' + Math.round(v).toLocaleString() + ' 萬' },
      { id: 'bento-val-payback', end: 14.2, fmt: (v) => v.toFixed(1) + ' 個月' }
    ];
    const grid = document.querySelector('.hero-bento-grid');
    if (!grid) return;

    let animated = false;
    const run = () => {
      if (animated) return;
      animated = true;
      const start = performance.now();
      const duration = 900;
      function frame(now) {
        const t = Math.max(0, Math.min(1, (now - start) / duration));
        const eased = 1 - Math.pow(1 - t, 3);
        specs.forEach((s) => {
          const el = document.getElementById(s.id);
          if (el) el.textContent = s.fmt(s.end * eased);
        });
        if (t < 1) requestAnimationFrame(frame);
      }
      requestAnimationFrame(frame);
    };

    if ('IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        if (entries.some((e) => e.isIntersecting)) {
          run();
          io.disconnect();
        }
      }, { threshold: 0.25 });
      io.observe(grid);
    } else {
      run();
    }
  }

  /* ------------------------------------------------------------------------
     Dimension 4A: WBS Composable Filters + Live Subtotal Bar + Inline Gantt
     ------------------------------------------------------------------------ */
  function parseWbsUsd(text) {
    const m = (text || '').replace(/,/g, '').match(/\$\s*([\d.]+)\s*([KkMm])?/);
    if (!m) return 0;
    let val = parseFloat(m[1]) || 0;
    const unit = (m[2] || '').toUpperCase();
    if (unit === 'K') val *= 1000;
    else if (unit === 'M') val *= 1000000;
    return val;
  }

  function parseDateMs(str) {
    const m = (str || '').trim().match(/(\d{4})[\/\-](\d{1,2})[\/\-](\d{1,2})/);
    if (!m) return null;
    return new Date(parseInt(m[1], 10), parseInt(m[2], 10) - 1, parseInt(m[3], 10)).getTime();
  }

  function enhanceWbsTable() {
    const tbody = document.getElementById('wbsTableBody');
    if (!tbody) return;
    const table = tbody.closest('table');
    if (!table) return;

    // 1. Add Timeline header column
    const theadRow = table.querySelector('thead tr');
    if (theadRow && !theadRow.querySelector('.wbs-gantt-th')) {
      const th = document.createElement('th');
      th.className = 'wbs-gantt-th';
      th.style.cssText = 'padding:10px 10px; text-align:center; width:155px; color:var(--text-charcoal); font-weight:800;';
      th.innerHTML = '甘特進度軌<div class="wbs-gantt-axis"><span>26/11</span><span>27/06</span><span>27/12</span></div>';
      theadRow.appendChild(th);
    }

    // 2. Add Inline Gantt bar to each row
    const minMs = new Date(2026, 10, 1).getTime(); // 2026-11-01
    const maxMs = new Date(2027, 11, 31).getTime(); // 2027-12-31
    const spanMs = maxMs - minMs;
    const cnyLeft = ((new Date(2027, 1, 5).getTime() - minMs) / spanMs) * 100;
    const cnyWidth = ((new Date(2027, 1, 15).getTime() - new Date(2027, 1, 5).getTime()) / spanMs) * 100;

    tbody.querySelectorAll('.wbs-row').forEach((row) => {
      if (row.querySelector('.wbs-gantt-cell')) return;
      const cells = row.querySelectorAll('td');
      const startMs = parseDateMs(cells[3] ? cells[3].textContent : '');
      const endMs = parseDateMs(cells[4] ? cells[4].textContent : '');
      const cat = (row.getAttribute('data-cat') || 'Run').toLowerCase();
      const catClass = cat.includes('trans') ? 'cat-transform' : (cat.includes('grow') ? 'cat-grow' : 'cat-run');

      let leftPct = 0;
      let widthPct = 10;
      if (startMs && endMs && endMs >= startMs) {
        leftPct = Math.max(0, Math.min(96, ((startMs - minMs) / spanMs) * 100));
        widthPct = Math.max(4, Math.min(100 - leftPct, ((endMs - startMs) / spanMs) * 100));
      }

      const td = document.createElement('td');
      td.className = 'wbs-gantt-cell';
      td.innerHTML = `
        <div class="wbs-gantt-track" title="${(cells[3]?.textContent || '').trim()} → ${(cells[4]?.textContent || '').trim()}">
          <div class="wbs-gantt-freeze" style="left:${cnyLeft.toFixed(1)}%; width:${cnyWidth.toFixed(1)}%;" title="2/5-2/15 春節封網期"></div>
          <div class="wbs-gantt-bar ${catClass}" style="left:${leftPct.toFixed(1)}%; width:${widthPct.toFixed(1)}%;"></div>
        </div>
      `;
      row.appendChild(td);
    });

    // 3. Inject Live Dynamic Subtotal Bar right above the table wrapper
    const tableWrap = table.parentElement;
    if (tableWrap && !document.getElementById('wbsSubtotalBar')) {
      const bar = document.createElement('div');
      bar.id = 'wbsSubtotalBar';
      bar.className = 'wbs-subtotal-bar';
      tableWrap.parentElement.insertBefore(bar, tableWrap);
    }

    updateWbsVisibilityAndSubtotal();
  }

  function updateWbsVisibilityAndSubtotal() {
    const rows = document.querySelectorAll('.wbs-row');
    const searchInput = document.getElementById('wbsSearchInput');
    const q = searchInput ? searchInput.value.trim().toLowerCase() : '';

    let totalAllUsd = 0;
    let shownCount = 0;
    let shownUsd = 0;
    let cntRun = 0, cntGrow = 0, cntTrans = 0;

    rows.forEach((r) => {
      const cells = r.querySelectorAll('td');
      const budgetCell = cells[8]; // 9th col (index 8) is 預算規模
      const usd = parseWbsUsd(budgetCell ? budgetCell.textContent : '');
      totalAllUsd += usd;

      const pPillar = r.getAttribute('data-pillar') || '';
      const pCat = r.getAttribute('data-cat') || '';
      const catMatch =
        activeWbsCategory === 'all' ||
        pCat === activeWbsCategory ||
        pPillar.startsWith(activeWbsCategory + ' ');
      const textMatch = !q || r.textContent.toLowerCase().includes(q);

      if (catMatch && textMatch) {
        r.style.display = '';
        shownCount++;
        shownUsd += usd;
        if (pCat === 'Run') cntRun++;
        else if (pCat === 'Grow') cntGrow++;
        else cntTrans++;
      } else {
        r.style.display = 'none';
      }
    });

    const bar = document.getElementById('wbsSubtotalBar');
    if (bar) {
      const ntdWan = Math.round((shownUsd * FX_RATE) / 10000);
      const pct = totalAllUsd > 0 ? ((shownUsd / totalAllUsd) * 100).toFixed(1) : '0.0';
      bar.innerHTML = `
        <div class="wbs-subtotal-group">
          <span class="wbs-subtotal-item">篩選顯示 <span class="wbs-subtotal-val">${shownCount} / ${rows.length}</span> 項</span>
          <span class="wbs-subtotal-item">小計預算 <span class="wbs-subtotal-val">$${shownUsd.toLocaleString()} USD</span> (約 NT$ ${ntdWan.toLocaleString()} 萬 · 佔比 ${pct}%)</span>
        </div>
        <div class="wbs-subtotal-group" style="font-size:0.74rem;">
          <span style="color:var(--green-run); font-weight:700;">● Run ${cntRun}</span>
          <span style="color:var(--blue-grow); font-weight:700;">● Grow ${cntGrow}</span>
          <span style="color:var(--purple-trans); font-weight:700;">● Transform ${cntTrans}</span>
          <button type="button" class="wbs-csv-btn" onclick="window.__neonExportWbsCsv && window.__neonExportWbsCsv()" title="將目前篩選結果匯出為 Excel 相容 CSV">📥 匯出 CSV</button>
        </div>
      `;
    }
  }

  window.__neonExportWbsCsv = function () {
    const rows = Array.from(document.querySelectorAll('.wbs-row')).filter((r) => r.style.display !== 'none');
    if (!rows.length) {
      showNeonToast('⚠️ 目前無符合篩選條件的 WBS 項目');
      return;
    }
    const header = ['WBS代號', '專案名稱', '主架構範疇', '資本屬性', '開始日期', '結束日期', '實質工期', '負責團隊', '關鍵里程碑與交付成果', '預算規模(USD)'];
    const escCsv = (s) => '"' + String(s || '').replace(/\s+/g, ' ').trim().replace(/"/g, '""') + '"';
    const lines = [header.map(escCsv).join(',')];
    rows.forEach((r) => {
      const c = r.querySelectorAll('td');
      const titleDivs = c[1] ? c[1].querySelectorAll('div') : [];
      const projName = titleDivs[0] ? titleDivs[0].textContent : (c[1]?.textContent || '');
      const pillar = r.getAttribute('data-pillar') || (titleDivs[1]?.textContent || '');
      const budget = (c[8]?.textContent || '').replace(/預估參考值/g, '').trim();
      lines.push([
        c[0]?.textContent,
        projName,
        pillar,
        r.getAttribute('data-cat') || c[2]?.textContent,
        c[3]?.textContent,
        c[4]?.textContent,
        c[5]?.textContent,
        c[6]?.textContent,
        c[7]?.textContent,
        budget
      ].map(escCsv).join(','));
    });
    const blob = new Blob(['\uFEFF' + lines.join('\r\n')], { type: 'text/csv;charset=utf-8;' });
    const a = document.createElement('a');
    a.href = URL.createObjectURL(blob);
    a.download = `RSI_2027_WBS_${activeWbsCategory}_${rows.length}items.csv`;
    document.body.appendChild(a);
    a.click();
    setTimeout(() => {
      URL.revokeObjectURL(a.href);
      a.remove();
    }, 500);
    showNeonToast(`📥 已匯出 ${rows.length} 項 WBS 清單 (CSV)`);
  };

  /* ------------------------------------------------------------------------
     Dimension 4B: Ready-to-Sew 4-Gate Executive Dual-Sign Override SOP
     ------------------------------------------------------------------------ */
  function syncGateOverrideUI() {
    const resultBox = document.getElementById('simResultBox');
    if (!resultBox) return;

    const g1 = document.getElementById('gateBOM')?.checked ?? true;
    const g2 = document.getElementById('gateTechPack')?.checked ?? true;
    const g3 = document.getElementById('gateMQP')?.checked ?? false;
    const g4 = document.getElementById('gateCut')?.checked ?? true;
    const passed = [g1, g2, g3, g4].filter(Boolean).length;

    let wrap = document.getElementById('gateOverrideWrap');
    if (!wrap) {
      wrap = document.createElement('div');
      wrap.id = 'gateOverrideWrap';
      resultBox.appendChild(wrap);
    }

    if (passed === 4) {
      gateOverrideState.active = false;
      wrap.innerHTML = '';
      return;
    }

    if (gateOverrideState.active) {
      resultBox.className = 'sim-result-box override-approved';
      const icon = document.getElementById('simIcon');
      const title = document.getElementById('simTitle');
      const desc = document.getElementById('simDesc');
      if (icon) icon.textContent = '⚠️';
      if (title) title.textContent = '雙簽特許放行 · 紅色風險工單監控中 (Override Active)';
      if (desc) {
        desc.innerHTML = `已啟動 <strong>Override SOP</strong>（通過 ${passed}/4 門禁），系統自動標註為紅色風險工單並即時追蹤欠料補齊時效，防堵隱性停工。`;
      }
      wrap.innerHTML = `
        <div class="override-audit-stamp">
          AUDIT-ID: RSI-OVR-${gateOverrideState.timestamp.slice(-6)} ｜ 核准：廠長 + 周文津副總 ｜ ${gateOverrideState.timestamp}
        </div>
        <button type="button" class="gate-override-trigger" onclick="window.__neonRevokeOverride()">
          ↩ 撤銷特許放行並恢復硬性攔截
        </button>
      `;
      return;
    }

    wrap.innerHTML = `
      <button type="button" class="gate-override-trigger" onclick="window.__neonOpenOverridePanel()">
        ✍️ 申請「廠長＋副總」雙簽緊急特許通行 (Override SOP)
      </button>
      <div id="gateOverridePanel" class="gate-override-panel" style="display:none;">
        <div style="font-weight:800; color:#9A3412; margin-bottom:6px;">
          緊急特許通行電子雙簽（需確認齊套率 ≥85% 並掛載紅色風險警示）
        </div>
        <label class="gate-override-check">
          <input type="checkbox" id="ovrSignPlant" onchange="window.__neonCheckOverrideReady()">
          <span>廠長核簽：確認現場可先開前段工序，缺口件 24h 內補齊</span>
        </label>
        <label class="gate-override-check">
          <input type="checkbox" id="ovrSignVp" onchange="window.__neonCheckOverrideReady()">
          <span>副總核准（周文津）：同意掛載紅色風險工單並留存稽核軌跡</span>
        </label>
        <button type="button" id="ovrConfirmBtn" class="gate-override-confirm" disabled onclick="window.__neonApproveOverride()">
          確認雙簽並放行紅色風險工單
        </button>
      </div>
    `;
  }

  window.__neonOpenOverridePanel = function () {
    const p = document.getElementById('gateOverridePanel');
    if (p) p.style.display = p.style.display === 'none' ? 'block' : 'none';
  };
  window.__neonCheckOverrideReady = function () {
    const a = document.getElementById('ovrSignPlant')?.checked;
    const b = document.getElementById('ovrSignVp')?.checked;
    const btn = document.getElementById('ovrConfirmBtn');
    if (btn) btn.disabled = !(a && b);
  };
  window.__neonApproveOverride = function () {
    const now = new Date();
    gateOverrideState.active = true;
    gateOverrideState.timestamp = now.toISOString().replace('T', ' ').slice(0, 19);
    syncGateOverrideUI();
    showNeonToast('⚠️ 已完成廠長＋副總雙簽特許放行（稽核軌跡已記錄）');
  };
  window.__neonRevokeOverride = function () {
    gateOverrideState.active = false;
    if (typeof window.calculateGateStatus === 'function') window.calculateGateStatus();
  };

  /* ------------------------------------------------------------------------
     Dimension 4C: Live DuckDB WAL Offline Queue Ticker during Cable Cut
     ------------------------------------------------------------------------ */
  function startWalTicker() {
    stopWalTicker();
    walCounters = { s1: 284, s2: 178, s3: 412 };
    walTickerTimer = setInterval(() => {
      walCounters.s1 += Math.floor(Math.random() * 14) + 8;
      walCounters.s2 += Math.floor(Math.random() * 10) + 5;
      walCounters.s3 += Math.floor(Math.random() * 16) + 9;
      const q1 = document.getElementById('site1-queue');
      const q2 = document.getElementById('site2-queue');
      const q3 = document.getElementById('site3-queue');
      if (q1) q1.textContent = `${walCounters.s1.toLocaleString()} 件 (DuckDB WAL 寫入中)`;
      if (q2) q2.textContent = `${walCounters.s2.toLocaleString()} 件 (DuckDB WAL 寫入中)`;
      if (q3) q3.textContent = `${walCounters.s3.toLocaleString()} 件 (DuckDB WAL 寫入中)`;
    }, 1400);
  }

  function stopWalTicker() {
    if (walTickerTimer) {
      clearInterval(walTickerTimer);
      walTickerTimer = null;
    }
  }

  /* ------------------------------------------------------------------------
     Dimension 5 & 6 (v8.0): Theme Switcher, Sticky Bar, Unified FAB, SW
     ------------------------------------------------------------------------ */
  const THEME_KEY = 'rsi_neon_theme';

  function applyNeonTheme(theme, silent) {
    const t = theme === 'obsidian' ? 'obsidian' : 'milan';
    document.documentElement.setAttribute('data-theme', t);
    try { localStorage.setItem(THEME_KEY, t); } catch (e) {}

    const icon = document.getElementById('neonThemeIcon');
    const label = document.getElementById('neonThemeLabel');
    const stickyIcon = document.getElementById('neonStickyThemeBtn');
    if (icon) icon.textContent = t === 'obsidian' ? '☀️' : '🌙';
    if (label) label.textContent = t === 'obsidian' ? '米蘭暖琥珀' : '深黑曜';
    if (stickyIcon) stickyIcon.textContent = t === 'obsidian' ? '☀️' : '🌙';

    // Sync Chart.js axis & legend colors cleanly
    if (typeof Chart !== 'undefined' && Chart.instances) {
      const tickColor = t === 'obsidian' ? '#A8A097' : '#6B635B';
      const legendColor = t === 'obsidian' ? '#E7E0D8' : '#332E2A';
      const gridColor = t === 'obsidian' ? 'rgba(255,255,255,0.08)' : 'rgba(230,221,208,0.7)';
      Object.values(Chart.instances).forEach((ch) => {
        try {
          if (ch.options?.plugins?.legend?.labels) ch.options.plugins.legend.labels.color = legendColor;
          if (ch.options?.scales) {
            Object.values(ch.options.scales).forEach((sc) => {
              if (sc.ticks) sc.ticks.color = tickColor;
              if (sc.grid && sc.grid.display !== false) sc.grid.color = gridColor;
              if (sc.pointLabels) sc.pointLabels.color = legendColor;
            });
          }
          ch.update('none');
        } catch (e) {}
      });
    }

    if (!silent) {
      showNeonToast(t === 'obsidian' ? '🌙 已切換至深黑曜戰情室主題' : '☀️ 已切換至米蘭暖琥珀主題');
    }
  }

  window.__neonToggleTheme = function () {
    const cur = document.documentElement.getAttribute('data-theme') || 'milan';
    applyNeonTheme(cur === 'obsidian' ? 'milan' : 'obsidian', false);
  };

  function initStickyExecutiveBar() {
    if (document.getElementById('neonStickyBar')) return;
    const bar = document.createElement('div');
    bar.id = 'neonStickyBar';
    bar.className = 'neon-sticky-bar';
    bar.setAttribute('aria-label', '捲動快速導覽列');
    bar.innerHTML = `
      <div class="neon-sticky-inner">
        <a href="#" class="neon-sticky-brand"><span class="dot"></span><span>RSI 2027 · 蜂巢計畫</span></a>
        <div class="neon-sticky-links">
          <a href="#hive-pipeline">🐝 時程閘門</a>
          <a href="#hive-3d-map">🗺️ 3D 地圖</a>
          <a href="#invest-framework">💵 FinOps ROI</a>
          <a href="#factory-monitor">📡 邊緣遙測</a>
          <a href="#pillars">🏛️ 四大架構</a>
          <a href="#simulator">🚦 4-Gate</a>
          <a href="#wbs-gantt">📅 25項 WBS</a>
          <a href="#doc-center">📑 文檔中心</a>
        </div>
        <div class="neon-sticky-actions">
          <button type="button" class="executive-search-btn" onclick="openSearchModal()" style="padding:5px 12px; border-radius:9999px; font-size:0.74rem; font-weight:700;">🔍 ⌘K</button>
          <button type="button" id="neonStickyThemeBtn" class="neon-theme-btn" onclick="window.__neonToggleTheme()" title="切換主題" aria-label="切換主題" style="padding:5px 10px !important;">🌙</button>
        </div>
      </div>
    `;
    document.body.appendChild(bar);

    const masthead = document.querySelector('.milan-masthead');
    if (masthead && 'IntersectionObserver' in window) {
      const io = new IntersectionObserver((entries) => {
        const show = !entries[0].isIntersecting;
        bar.classList.toggle('visible', show);
      }, { threshold: 0.05 });
      io.observe(masthead);
    }
  }

  function showNeonToast(msg) {
    let t = document.getElementById('neonToast');
    if (!t) {
      t = document.createElement('div');
      t.id = 'neonToast';
      t.className = 'neon-toast';
      document.body.appendChild(t);
    }
    t.textContent = msg;
    t.classList.add('show');
    clearTimeout(t._timer);
    t._timer = setTimeout(() => t.classList.remove('show'), 2600);
  }

  function initExecutiveFab() {
    const fab = document.createElement('div');
    fab.className = 'neon-fab-group';
    fab.setAttribute('aria-label', '快速高管操作');
    fab.innerHTML = `
      <button type="button" class="neon-fab-btn fab-search" title="全站搜尋 (⌘K)" aria-label="全站搜尋" id="neonFabSearch">🔍</button>
      <button type="button" class="neon-fab-btn" title="複製本頁分享連結" aria-label="複製連結" id="neonFabCopy">🔗</button>
      <button type="button" class="neon-fab-btn" title="列印董事會紙本報告 (Cmd+P)" aria-label="列印報告" id="neonFabPrint">🖨️</button>
      <button type="button" class="neon-fab-btn fab-top-hidden" title="回到頂部" aria-label="回到頂部" id="neonFabTop">↑</button>
    `;
    document.body.appendChild(fab);

    document.getElementById('neonFabSearch')?.addEventListener('click', () => {
      if (typeof window.openSearchModal === 'function') window.openSearchModal();
    });
    document.getElementById('neonFabCopy')?.addEventListener('click', () => {
      const url = window.location.href;
      if (navigator.clipboard && navigator.clipboard.writeText) {
        navigator.clipboard.writeText(url).then(() => showNeonToast('✅ 已複製 RSI 2027 戰略網站連結'));
      } else {
        showNeonToast('🔗 ' + url);
      }
    });
    document.getElementById('neonFabPrint')?.addEventListener('click', () => window.print());
    const topBtn = document.getElementById('neonFabTop');
    topBtn?.addEventListener('click', () => window.scrollTo({ top: 0, behavior: 'smooth' }));

    window.addEventListener('scroll', () => {
      if (topBtn) topBtn.classList.toggle('fab-top-hidden', window.scrollY < 320);
    }, { passive: true });
  }

  function registerServiceWorker() {
    if ('serviceWorker' in navigator && (location.protocol === 'https:' || location.hostname === 'localhost' || location.hostname === '127.0.0.1')) {
      navigator.serviceWorker.register('./sw.js').catch(() => {});
    }
  }

  /* ------------------------------------------------------------------------
     Bootstrap & Hook Overrides
     ------------------------------------------------------------------------ */
  document.addEventListener('DOMContentLoaded', () => {
    // Restore saved theme (default: Milan Warm Amber)
    let savedTheme = 'milan';
    try { savedTheme = localStorage.getItem(THEME_KEY) || 'milan'; } catch (e) {}
    applyNeonTheme(savedTheme, true);

    // Override FinOps engine cleanly
    window.setFinOpsScope = setFinOpsScope;
    window.updateFinOpsSimulation = neonUpdateFinOps;
    setFinOpsScope('full');

    // Wrap calculateGateStatus to preserve Override SOP UI
    if (typeof window.calculateGateStatus === 'function') {
      const origGate = window.calculateGateStatus;
      window.calculateGateStatus = function () {
        gateOverrideState.active = false;
        origGate.apply(this, arguments);
        syncGateOverrideUI();
      };
      syncGateOverrideUI();
    }

    // Wrap WBS filter & search to be composable + update subtotal bar
    window.filterWbs = function (catOrPillar, btn) {
      activeWbsCategory = catOrPillar || 'all';
      document.querySelectorAll('.wbs-filter-btn').forEach((b) => {
        b.classList.remove('active');
        b.style.background = 'var(--bg-card)';
        b.style.color = 'var(--text-body)';
        b.style.borderColor = 'var(--border-subtle)';
      });
      if (btn) {
        btn.classList.add('active');
        btn.style.background = 'var(--rust-primary)';
        btn.style.color = '#fff';
        btn.style.borderColor = 'var(--rust-primary)';
      }
      updateWbsVisibilityAndSubtotal();
    };
    window.searchWbs = function () {
      updateWbsVisibilityAndSubtotal();
    };
    enhanceWbsTable();

    // Wrap toggleCableCutSimulation to drive live DuckDB WAL ticker
    if (typeof window.toggleCableCutSimulation === 'function') {
      const origCable = window.toggleCableCutSimulation;
      window.toggleCableCutSimulation = function () {
        origCable.apply(this, arguments);
        if (typeof isCableCut !== 'undefined' && isCableCut) {
          startWalTicker();
        } else {
          stopWalTicker();
        }
      };
    }

    // Upgrade Factory Monitor to Dark Obsidian-Amber Command Center Band
    const monitor = document.querySelector('.factory-edge-monitor');
    if (monitor) monitor.classList.add('neon-command-band');

    initNavDropdowns();
    initReadingProgressAndRail();
    initStickyExecutiveBar();
    initHeroBentoCountUp();
    initExecutiveFab();
    registerServiceWorker();
  });
})();
