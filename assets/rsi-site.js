/* RSI Group site layer — loaded on every page (see tools/inject_site_assets.py).
   1) Site search: button + dialog, opens with the button, "/" or Cmd/Ctrl+K.
      Reads assets/search-index.json (tools/build_search_index.py) on first open.
   2) Mobile fit (<= 768px): scrollable tables, stacked grids, fit-to-width
      fallback for fixed-width blocks, a one-row scrolling nav in tall sticky
      headers, and an 11px floor for tiny text. */
(function () {
  'use strict';
  if (window.__rsiSite) return;
  window.__rsiSite = true;

  var script = document.currentScript;
  var ROOT = new URL('..', script ? script.src : location.href); // assets/ -> site root
  var INDEX_URL = new URL('assets/search-index.json', ROOT).href;
  var mq = window.matchMedia('(max-width: 768px)');
  var isMac = /Mac|iPhone|iPad/.test(navigator.platform || navigator.userAgent);

  var ICON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><circle cx="11" cy="11" r="7"/><path d="m20 20-3.5-3.5"/></svg>';
  var SUGGEST = ['RACI', 'PoC', 'SD-WAN', 'Data Lake', '副總裁示', 'API Platform', '甘特圖', 'KPI'];

  /* ---------------- Site map: top navigation and breadcrumbs ---------------- */
  // Paths are relative to the site root. Pages not listed here get "首頁 › <page title>".
  var STRATEGY = [
    ['ceo_strategic_plan.html', 'IT 策略與投資計畫（CEO）'],
    ['roadmap_2027.html', '2025–2027 策略路線圖'],
    ['gantt_chart_2027.html', '全專案甘特圖'],
    ['vp_chou_worklist.html', '周副總交辦工作清單'],
    ['organization_resources.html', '組織職能與資源配置'],
    ['inventory_discovery.html', '職能與設備盤點手冊'],
    ['pptx_rendered_deck.html', 'IT 營運計畫簡報']
  ];
  var HIVE = [
    { label: '架構與平台', items: [
      ['Hive/platforms_architecture_showcase.html', '雙核心架構展廳'],
      ['Hive/cloud_platforms_deepdive_architecture.html', '三大雲端深度架構'],
      ['Hive/platform_tools_comparison_matrix.html', '工具選型評估'],
      ['Hive/api_platform_drawio.html', 'API Platform 架構圖'],
      ['Hive/datalake_etl_elt_drawio.html', 'Data Lake ETL/ELT 架構圖'],
      ['Hive/azure_native_architecture_showcase.html', 'Azure 原生選型報告'],
      ['Hive/platform_selection_4routes_showcase.html', '多雲選型與 MuleSoft 評估'],
      ['RSI-data-architecture.html', 'APIM＋ADF 資料整合架構'],
      ['Hive/togaf_api_quality_standards.html', 'TOGAF 與 API 品質規範'],
      ['Hive/waap_api_security_architecture.html', 'WAAP 與 API 安全架構']
    ] },
    { label: '盤點與問卷', items: [
      ['Hive/it_skills_8domains_assessment.html', '技術職能問卷'],
      ['Hive/engineer_skills_inventory.html', '高階技術評鑑表'],
      ['Hive/it_skills_questionnaire.html', '6 大領域職能盤點問卷'],
      ['Hive/modular_skills_inventory.html', '6 大領域分項盤點表'],
      ['Hive/it_infrastructure_inventory.html', '資訊基礎設施盤點表']
    ] },
    { label: '文件', items: [
      ['Hive/index.html', '蜂巢計畫實施藍圖'],
      ['Hive/download_center.html', '文檔中心']
    ] }
  ];
  var EXTRA = {
    'mobile.html': '首頁（行動版）',
    'mobile_simulator.html': '手機真機模擬',
    'index_legacy_swiss.html': '首頁（舊版）',
    'RSI-data-architecture.html': 'APIM＋ADF 資料整合架構（米蘭風格）',
    'Hive/RSI-data-architecture.html': 'APIM＋ADF 資料整合架構（米蘭風格）',
    'Hive/azure_native_architecture_showcase.html': 'Azure 原生架構選型報告',
    'Hive/platform_selection_4routes_showcase.html': '多雲選型與 MuleSoft 評估',
    'RSI-meeting-brief.html': '2026-10-16 會談備忘',
    'RSI-meeting-minutes.html': '2026-10-16 會談紀錄全文',
    'RSI-meeting-report.html': '2026-10-16 會談高階報告',
    'hive-review.html': '蜂巢計畫藍圖健檢',
    'private/index.html': '機密顧問文件庫'
  };

  var CHEVRON = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round" aria-hidden="true"><path d="m6 9 6 6 6-6"/></svg>';
  var BURGER = '<svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" aria-hidden="true"><path d="M4 7h16M4 12h16M4 17h16"/></svg>';

  function here() {
    var p = decodeURIComponent(location.pathname), r = decodeURIComponent(ROOT.pathname);
    p = p.indexOf(r) === 0 ? p.slice(r.length) : p.replace(/^\//, '');
    return p === '' || /\/$/.test(p) ? p + 'index.html' : p;
  }
  function url(p) { return new URL(p, ROOT).href; }

  function crumbsFor(cur) {
    var home = [['index.html', '首頁']], i, g;
    if (cur === 'index.html') return [];
    for (i = 0; i < STRATEGY.length; i++) if (STRATEGY[i][0] === cur) return home.concat([[null, '策略與規劃'], [cur, STRATEGY[i][1]]]);
    if (cur === 'Hive/index.html') return home.concat([[cur, '蜂巢計畫']]);
    for (g = 0; g < HIVE.length; g++) for (i = 0; i < HIVE[g].items.length; i++) {
      if (HIVE[g].items[i][0] === cur) return home.concat([['Hive/index.html', '蜂巢計畫'], [null, HIVE[g].label], [cur, HIVE[g].items[i][1]]]);
    }
    var t = EXTRA[cur] || (document.title || '').split(/[｜|]/)[0].replace(/^RSI Group\s*·\s*/, '').trim() || cur;
    return home.concat([[cur, t]]);
  }

  var top, menus = [];
  function closeMenus(except) {
    menus.forEach(function (m) { if (m !== except) { m.btn.setAttribute('aria-expanded', 'false'); m.panel.hidden = true; } });
  }
  function link(p, text, cur, cls) {
    var a = el('a', cls || null); a.href = url(p); a.textContent = text;
    if (p === cur) a.setAttribute('aria-current', 'page');
    return a;
  }
  function dropdown(label, groups, cur) {
    var wrap = el('div', 'rsi-dd'), id = 'rsi-dd-' + menus.length;
    var btn = el('button', 'rsi-dd-btn', esc(label) + CHEVRON);
    btn.type = 'button'; btn.setAttribute('aria-expanded', 'false'); btn.setAttribute('aria-controls', id);
    var panel = el('div', 'rsi-dd-panel' + (groups.length > 1 ? ' cols' : '')); panel.id = id; panel.hidden = true;
    groups.forEach(function (g) {
      var box = el('div', 'rsi-dd-group');
      if (g.label) box.appendChild(el('div', 'rsi-dd-label', esc(g.label)));
      g.items.forEach(function (it) {
        box.appendChild(link(it[0], it[1], cur));
        if (it[0] === cur) wrap.classList.add('is-current');
      });
      panel.appendChild(box);
    });
    var m = { btn: btn, panel: panel };
    menus.push(m);
    btn.addEventListener('click', function () {
      var open = btn.getAttribute('aria-expanded') !== 'true';
      closeMenus(m);
      btn.setAttribute('aria-expanded', String(open)); panel.hidden = !open;
    });
    wrap.appendChild(btn); wrap.appendChild(panel);
    return wrap;
  }

  function buildTop() {
    var cur = here();
    top = el('header', 'rsi-top');
    top.setAttribute('data-nosnippet', '');
    var inner = el('div', 'rsi-top-in');
    var brand = el('a', 'rsi-brand', '<b>RSI Group</b><span>2027 IT 營運計畫</span>');
    brand.href = url('index.html');
    var nav = el('nav', 'rsi-nav'); nav.setAttribute('aria-label', '網站導覽');
    nav.appendChild(link('index.html', '首頁', cur, 'rsi-nav-link'));
    nav.appendChild(dropdown('策略與規劃', [{ items: STRATEGY }], cur));
    var hiveCur = cur.indexOf('Hive/') === 0;
    var hive = dropdown('蜂巢計畫', HIVE, cur);
    if (hiveCur) hive.classList.add('is-current');
    nav.appendChild(hive);
    nav.appendChild(link('Hive/download_center.html', '文檔中心', cur, 'rsi-nav-link'));

    var kbd = pageOwnsShortcuts() ? '' : '<span class="rsi-kbd">' + (isMac ? '⌘K' : 'Ctrl K') + '</span>';
    var search = el('button', 'rsi-top-search', ICON + '<span class="rsi-ph">搜尋全站內容…</span>' + kbd);
    search.type = 'button'; search.setAttribute('aria-label', '全站搜尋');
    search.addEventListener('click', open);

    var burger = el('button', 'rsi-menu-btn', BURGER + '<span class="rsi-menu-txt">導覽</span>');
    burger.type = 'button'; burger.setAttribute('aria-label', '開啟網站選單'); burger.setAttribute('aria-expanded', 'false');
    burger.addEventListener('click', function () {
      var o = !top.classList.contains('is-open');
      top.classList.toggle('is-open', o);
      burger.setAttribute('aria-expanded', String(o));
      burger.setAttribute('aria-label', o ? '關閉網站選單' : '開啟網站選單');
    });

    var navBtn = el('a', 'rsi-header-nav-btn', '<span>🧭</span><span>導覽鍵</span>');
    navBtn.href = 'javascript:void(0)';
    navBtn.setAttribute('role', 'button');
    navBtn.type = 'button';
    navBtn.setAttribute('aria-label', '開啟全景導覽選單');
    navBtn.addEventListener('click', openMobileDrawer);

    inner.appendChild(brand);
    inner.appendChild(nav);
    inner.appendChild(search);
    inner.appendChild(navBtn);
    inner.appendChild(burger);
    top.appendChild(inner);

    var trail = crumbsFor(cur);
    if (trail.length) {
      var bc = el('nav', 'rsi-crumbs'); bc.setAttribute('aria-label', '麵包屑');
      var ol = el('ol');
      trail.forEach(function (c, i) {
        var li = el('li');
        if (i === trail.length - 1) { var s = el('span'); s.textContent = c[1]; s.setAttribute('aria-current', 'page'); li.appendChild(s); }
        else if (c[0]) li.appendChild(link(c[0], c[1], null));
        else li.appendChild(document.createTextNode(c[1]));
        ol.appendChild(li);
      });
      bc.appendChild(ol); top.appendChild(bc);
    }

    // Clean top bar sizing without breaking mobile viewport
    if (window.innerWidth > 768) {
      var bs = getComputedStyle(document.body);
      var pt = parseFloat(bs.paddingTop) || 0, pl = parseFloat(bs.paddingLeft) || 0, pr = parseFloat(bs.paddingRight) || 0;
      top.style.margin = (-pt) + 'px ' + (-pr) + 'px ' + pt + 'px ' + (-pl) + 'px';
      if (bs.display.indexOf('flex') >= 0 || bs.display.indexOf('grid') >= 0) { top.style.width = 'calc(100% + ' + (pl + pr) + 'px)'; top.style.gridColumn = '1 / -1'; top.style.order = '-1'; }
    } else {
      top.style.margin = '0';
      top.style.width = '100%';
      top.style.maxWidth = '100vw';
      top.style.boxSizing = 'border-box';
    }
    document.body.insertBefore(top, document.body.firstChild);

    // Mobile Bottom Floating Dock (手機專屬底部導覽列 ＋ 導覽鍵)
    try {
      var dock = el('nav', 'rsi-mobile-dock');
      dock.setAttribute('aria-label', '手機快速導覽列');
      
      var dockHome = el('a', 'rsi-dock-item', '<span class="rsi-dock-icon">🏠</span><span class="rsi-dock-label">首頁</span>');
      dockHome.href = url('index.html');
      if (cur === 'index.html') dockHome.classList.add('is-active');

      var dockHive = el('a', 'rsi-dock-item', '<span class="rsi-dock-icon">🐝</span><span class="rsi-dock-label">蜂巢</span>');
      dockHive.href = url('Hive/index.html');
      if (cur === 'Hive/index.html') dockHive.classList.add('is-active');

      var dockAzure = el('a', 'rsi-dock-item', '<span class="rsi-dock-icon">🔷</span><span class="rsi-dock-label">Azure選型</span>');
      dockAzure.href = url('Hive/azure_native_architecture_showcase.html');
      if (cur.indexOf('azure_native') >= 0) dockAzure.classList.add('is-active');

      var dockDocs = el('a', 'rsi-dock-item', '<span class="rsi-dock-icon">📑</span><span class="rsi-dock-label">文檔</span>');
      dockDocs.href = url('Hive/download_center.html');
      if (cur.indexOf('download_center') >= 0) dockDocs.classList.add('is-active');

      var dockMenu = el('a', 'rsi-dock-item rsi-dock-btn', '<span class="rsi-dock-icon">🧭</span><span class="rsi-dock-label">導覽鍵</span>');
      dockMenu.href = 'javascript:void(0)';
      dockMenu.setAttribute('role', 'button');
      dockMenu.setAttribute('aria-label', '切換導覽選單');
      dockMenu.addEventListener('click', function (e) { e.preventDefault(); openMobileDrawer(); return;
        var o = !top.classList.contains('is-open');
        top.classList.toggle('is-open', o);
        burger.setAttribute('aria-expanded', String(o));
        dockMenu.classList.toggle('is-active', o);
        if (o) window.scrollTo({ top: 0, behavior: 'smooth' });
      });

      dock.appendChild(dockHome);
      dock.appendChild(dockHive);
      dock.appendChild(dockAzure);
      dock.appendChild(dockDocs);
      dock.appendChild(dockMenu);
      document.body.appendChild(dock);
    } catch (e) {
      console.warn('Dock init:', e);
    }

    document.addEventListener('click', function (e) { if (!top.contains(e.target)) closeMenus(); });
    document.addEventListener('keydown', function (e) {
      if (e.key !== 'Escape') return;
      var openOne = menus.filter(function (m) { return !m.panel.hidden; })[0];
      if (openOne) { closeMenus(); openOne.btn.focus(); }
    });
    return search;
  }

  /* ---------------- Search ---------------- */
  var dialog, input, body, list, status, chips, fab;
  var index = null, loading = null, hits = [], active = -1, lastFocus = null, timer = 0;

  function el(tag, cls, html) { var n = document.createElement(tag); if (cls) n.className = cls; if (html != null) n.innerHTML = html; return n; }
  function esc(s) { return String(s).replace(/[&<>"']/g, function (c) { return { '&': '&amp;', '<': '&lt;', '>': '&gt;', '"': '&quot;', "'": '&#39;' }[c]; }); }
  function norm(s) { return String(s || '').normalize('NFKC').toLowerCase(); }
  function reEsc(s) { return s.replace(/[.*+?^${}()|[\]\\]/g, '\\$&'); }

  // Pages with their own in-page search (the home page) keep Cmd/Ctrl+K and "/" for it.
  function pageOwnsShortcuts() { return typeof window.openSearchModal === 'function'; }

  function buildUI() {
    var kbd = pageOwnsShortcuts() ? '' : '<span class="rsi-kbd">' + (isMac ? '⌘K' : 'Ctrl K') + '</span>';
    fab = el('button', 'rsi-search-fab', ICON + '<span class="rsi-label">全站搜尋</span>' + kbd);
    fab.type = 'button';
    fab.setAttribute('aria-label', '全站搜尋');
    fab.addEventListener('click', open);

    dialog = el('div', 'rsi-search');
    dialog.hidden = true;
    dialog.setAttribute('role', 'dialog');
    dialog.setAttribute('aria-modal', 'true');
    dialog.setAttribute('aria-label', '全站搜尋');
    dialog.innerHTML =
      '<div class="rsi-search-panel">' +
        '<div class="rsi-search-bar">' + ICON +
          '<input class="rsi-search-input" id="rsi-search-input" type="search" placeholder="搜尋全站內容，例如 RACI、PoC、SD-WAN" autocomplete="off" autocapitalize="off" spellcheck="false" enterkeyhint="search" aria-controls="rsi-search-list" aria-autocomplete="list">' +
          '<button type="button" class="rsi-search-close">關閉</button>' +
        '</div>' +
        '<div class="rsi-search-body">' +
          '<p class="rsi-search-status" role="status" aria-live="polite"></p>' +
          '<div class="rsi-search-chips"></div>' +
          '<ul class="rsi-search-list" id="rsi-search-list" role="listbox" aria-label="搜尋結果"></ul>' +
        '</div>' +
        '<div class="rsi-search-foot"><span><kbd>↑</kbd> <kbd>↓</kbd> 選擇</span><span><kbd>Enter</kbd> 開啟</span><span><kbd>Esc</kbd> 關閉</span></div>' +
      '</div>';
    input = dialog.querySelector('.rsi-search-input');
    body = dialog.querySelector('.rsi-search-body');
    list = dialog.querySelector('.rsi-search-list');
    status = dialog.querySelector('.rsi-search-status');
    chips = dialog.querySelector('.rsi-search-chips');
    SUGGEST.forEach(function (q) {
      var c = el('button', 'rsi-search-chip'); c.type = 'button'; c.textContent = q;
      c.addEventListener('click', function () { input.value = q; run(); input.focus(); });
      chips.appendChild(c);
    });
    dialog.querySelector('.rsi-search-close').addEventListener('click', close);
    dialog.addEventListener('mousedown', function (e) { if (e.target === dialog) close(); });
    input.addEventListener('input', function () { clearTimeout(timer); timer = setTimeout(run, 90); });
    input.addEventListener('keydown', onKeys);
    document.body.appendChild(fab);
    document.body.appendChild(dialog);
  }

  function loadIndex() {
    if (index) return Promise.resolve(index);
    if (loading) return loading;
    loading = fetch(INDEX_URL, { cache: 'no-cache' })
      .then(function (r) { if (!r.ok) throw new Error(r.status); return r.json(); })
      .then(function (data) {
        index = [];
        data.pages.forEach(function (p) {
          p.s.forEach(function (s) {
            index.push({ u: p.u, title: p.title, g: p.g, h: s.h, id: s.id, t: s.t, key: norm(p.title + ' ' + s.h + ' ' + s.t), nh: norm(s.h), nt: norm(p.title) });
          });
        });
        return index;
      })
      .catch(function (e) { loading = null; throw e; });
    return loading;
  }

  function open() {
    if (!dialog) return;
    lastFocus = document.activeElement;
    document.body.appendChild(dialog); // last in DOM: paints above page bars that share the max z-index
    dialog.hidden = false;
    document.documentElement.classList.add('rsi-search-open');
    input.focus();
    input.select();
    if (!input.value) idle();
    loadIndex().then(function () { if (input.value) run(); else idle(); }, function () {
      status.textContent = '搜尋資料載入失敗，請確認網路連線後重新整理頁面再試。';
    });
  }
  function close() {
    dialog.hidden = true;
    document.documentElement.classList.remove('rsi-search-open');
    if (lastFocus && lastFocus.focus) lastFocus.focus();
  }
  function idle() {
    list.innerHTML = ''; hits = []; active = -1;
    chips.hidden = false;
    status.textContent = '輸入關鍵字搜尋全站頁面，或點選常用主題：';
  }

  function run() {
    var q = input.value.trim();
    if (!q) return idle();
    if (!index) { status.textContent = '正在載入搜尋資料…'; return; }
    chips.hidden = true;
    var terms = norm(q).split(/\s+/).filter(Boolean);
    var phrase = norm(q);
    var scored = [];
    for (var i = 0; i < index.length; i++) {
      var r = index[i], ok = true, score = 0;
      for (var j = 0; j < terms.length; j++) {
        var t = terms[j];
        if (r.key.indexOf(t) < 0) { ok = false; break; }
        if (r.nh.indexOf(t) >= 0) score += 8;
        if (r.nt.indexOf(t) >= 0) score += 3;
        score += Math.min(5, r.key.split(t).length - 1);
      }
      if (!ok) continue;
      if (terms.length > 1 && r.key.indexOf(phrase) >= 0) score += 6;
      scored.push([score, i]);
    }
    scored.sort(function (a, b) { return b[0] - a[0] || a[1] - b[1]; });
    var perPage = {}, out = [];
    for (var k = 0; k < scored.length && out.length < 40; k++) {
      var e = index[scored[k][1]];
      perPage[e.u] = (perPage[e.u] || 0) + 1;
      if (perPage[e.u] <= 5) out.push(e);
    }
    hits = out; active = out.length ? 0 : -1;
    render(q, terms);
  }

  function highlight(text, terms) {
    var safe = esc(text);
    terms.forEach(function (t) {
      if (!t) return;
      safe = safe.replace(new RegExp('(' + reEsc(esc(t)) + ')', 'gi'), '\u0000$1\u0001');
    });
    return safe.replace(/\u0000/g, '<mark>').replace(/\u0001/g, '</mark>');
  }
  function snippet(text, terms) {
    var low = norm(text), at = -1;
    for (var i = 0; i < terms.length && at < 0; i++) at = low.indexOf(terms[i]);
    if (at < 0) return text.slice(0, 120);
    var start = Math.max(0, at - 40);
    return (start ? '…' : '') + text.slice(start, start + 140) + (start + 140 < text.length ? '…' : '');
  }
  function hrefFor(h) {
    var url = new URL(h.u, ROOT).href;
    if (h.h) return url + '#:~:text=' + encodeURIComponent(h.h.slice(0, 60));
    return h.id ? url + '#' + encodeURIComponent(h.id) : url;
  }

  function render(q, terms) {
    list.innerHTML = '';
    if (!hits.length) {
      status.textContent = '找不到「' + q + '」。試試較短的關鍵字，或改用英文縮寫（例如 API、ERP、KPI）。';
      return;
    }
    status.textContent = '找到 ' + hits.length + (hits.length === 40 ? '+' : '') + ' 筆結果';
    hits.forEach(function (h, i) {
      var li = el('li');
      var a = el('a', 'rsi-search-hit');
      a.href = hrefFor(h);
      a.id = 'rsi-hit-' + i;
      a.setAttribute('role', 'option');
      a.setAttribute('aria-selected', i === active ? 'true' : 'false');
      a.innerHTML =
        '<span class="rsi-hit-page">' + esc(h.g + ' · ' + h.title) + '</span>' +
        (h.h ? '<span class="rsi-hit-head">' + highlight(h.h, terms) + '</span>' : '') +
        '<span class="rsi-hit-snip">' + highlight(snippet(h.t, terms), terms) + '</span>';
      a.addEventListener('click', function () { close(); });
      li.appendChild(a);
      list.appendChild(li);
    });
    input.setAttribute('aria-activedescendant', active >= 0 ? 'rsi-hit-' + active : '');
  }

  function move(d) {
    if (!hits.length) return;
    var old = list.querySelector('[aria-selected="true"]');
    if (old) old.setAttribute('aria-selected', 'false');
    active = (active + d + hits.length) % hits.length;
    var cur = document.getElementById('rsi-hit-' + active);
    cur.setAttribute('aria-selected', 'true');
    cur.scrollIntoView({ block: 'nearest' });
    input.setAttribute('aria-activedescendant', cur.id);
  }
  function onKeys(e) {
    if (e.key === 'ArrowDown') { e.preventDefault(); move(1); }
    else if (e.key === 'ArrowUp') { e.preventDefault(); move(-1); }
    else if (e.key === 'Enter' && active >= 0) { e.preventDefault(); var a = document.getElementById('rsi-hit-' + active); close(); location.href = a.href; }
    else if (e.key === 'Escape') { e.preventDefault(); close(); }
    else if (e.key === 'Tab') { // keep focus inside the dialog
      var f = dialog.querySelectorAll('input, button:not([hidden]), a[href]');
      if (e.shiftKey && document.activeElement === f[0]) { e.preventDefault(); f[f.length - 1].focus(); }
    }
  }
  document.addEventListener('keydown', function (e) {
    if (!dialog) return;
    if (!dialog.hidden && e.key === 'Escape') { close(); return; }
    if (pageOwnsShortcuts()) return;
    var typing = /^(INPUT|TEXTAREA|SELECT)$/.test((e.target || {}).tagName) || (e.target && e.target.isContentEditable);
    if ((e.key === 'k' || e.key === 'K') && (e.metaKey || e.ctrlKey)) { e.preventDefault(); dialog.hidden ? open() : close(); }
    else if (e.key === '/' && !typing && dialog.hidden) { e.preventDefault(); open(); }
  });

  /* ---------------- Mobile fit ---------------- */
  var zoomed = [], fontFixed = [], lastWidth = 0;

  function inScroller(n) {
    for (var a = n.parentElement; a && a !== document.body; a = a.parentElement) {
      var o = getComputedStyle(a).overflowX;
      if (o === 'auto' || o === 'scroll' || o === 'hidden' || o === 'clip') return true;
    }
    return false;
  }
  function isUI(n) { return n.closest && n.closest('.rsi-search, .rsi-search-fab, .rsi-top'); }

  function resetFit() {
    zoomed.forEach(function (n) { n.style.zoom = ''; }); zoomed = [];
    fontFixed.forEach(function (n) { n.style.fontSize = ''; }); fontFixed = [];
  }

  function fitMobile() {
    var w = document.documentElement.clientWidth;
    if (w === lastWidth) return;
    lastWidth = w;
    resetFit();
    if (!mq.matches) return;
    var all = document.body.getElementsByTagName('*');

    // 1. wide tables scroll inside their own box
    Array.prototype.forEach.call(document.querySelectorAll('table'), function (t) {
      if (isUI(t) || t.parentElement.classList.contains('rsi-x-scroll') || inScroller(t)) return;
      if (t.scrollWidth <= t.parentElement.clientWidth + 1) return;
      var wrap = el('div', 'rsi-x-scroll');
      t.parentNode.insertBefore(wrap, t);
      wrap.appendChild(t);
    });

    // 2. long unbroken text may wrap; grids whose tracks overflow stack to one column; overflowing rows wrap
    for (var pass = 0; pass < 2; pass++) {
      for (var i = 0; i < all.length; i++) {
        var n = all[i];
        if (n.scrollWidth <= n.clientWidth + 2 || isUI(n)) continue;
        if (!n.childElementCount && n.textContent.trim()) { n.classList.add('rsi-break'); continue; } // long unbroken text, e.g. file names
        var cs = getComputedStyle(n);
        if (cs.display.indexOf('grid') >= 0) n.classList.add('rsi-stack');
        else if (cs.display.indexOf('flex') >= 0 && cs.flexDirection.indexOf('row') === 0 && cs.flexWrap === 'nowrap' && cs.overflowX === 'visible' && !n.closest('nav')) n.classList.add('rsi-wrap');
      }
    }

    // 3. tall sticky/fixed headers: nav links on one scrolling row
    Array.prototype.forEach.call(document.querySelectorAll('header, nav, [class*="header"], [class*="navbar"]'), function (h) {
      var cs = getComputedStyle(h);
      if ((cs.position !== 'sticky' && cs.position !== 'fixed') || h.getBoundingClientRect().height < 96) return;
      Array.prototype.forEach.call(h.querySelectorAll('*'), function (c) {
        var s = getComputedStyle(c);
        if (s.display.indexOf('flex') >= 0 && s.flexWrap === 'wrap' && c.querySelectorAll('a, button').length >= 3) c.classList.add('rsi-nav-scroll');
      });
    });

    // 4. anything still wider than the screen is scaled down to fit
    for (var j = 0; j < all.length; j++) {
      var m = all[j];
      if (isUI(m) || m.style.zoom) continue;
      var r = m.getBoundingClientRect();
      if (r.width === 0 || r.right <= w + 1) continue;
      var p = m.parentElement;
      if (!p || p.getBoundingClientRect().right > w + 1 || inScroller(m)) continue;
      var pos = getComputedStyle(m).position;
      if (pos === 'fixed' || pos === 'absolute') continue;
      var avail = p.clientWidth - parseFloat(getComputedStyle(p).paddingLeft) - parseFloat(getComputedStyle(p).paddingRight);
      var z = Math.max(0.25, Math.min(1, avail / m.offsetWidth));
      if (z < 0.98) { m.style.zoom = z.toFixed(3); zoomed.push(m); }
    }

    // 5. 11px floor for tiny text
    for (var k = 0; k < all.length && fontFixed.length < 4000; k++) {
      var t = all[k];
      if (t.childElementCount || !t.textContent.trim() || isUI(t)) continue;
      if (parseFloat(getComputedStyle(t).fontSize) < 11) { t.style.fontSize = '11px'; fontFixed.push(t); }
    }
  }

  // Keep the search button clear of the page's own fixed controls in the bottom-right
  // corner (tab bars, back-to-top buttons). Probe what sits under the corner, so
  // controls that a page adds or shows later are caught too.
  function fixedAncestor(n) {
    for (var d = 0; n && n !== document.body && d < 8; n = n.parentElement, d++) {
      if (getComputedStyle(n).position === 'fixed') return n;
    }
    return null;
  }
  function placeFab() {
    if (!fab || !document.elementsFromPoint) return;
    var H = innerHeight, W = innerWidth, seen = [], lift = 0;
    for (var y = H - 8; y > H - 260; y -= 14) {
      for (var x = W - 24; x > W - 80; x -= 24) {
        document.elementsFromPoint(x, y).forEach(function (n) {
          if (isUI(n)) return;
          var f = fixedAncestor(n);
          if (!f || seen.indexOf(f) >= 0) return;
          seen.push(f);
          var cs = getComputedStyle(f), r = f.getBoundingClientRect();
          if (cs.pointerEvents === 'none' || r.height > 220 || r.height >= H * 0.5) return;
          lift = Math.max(lift, H - r.top);
        });
      }
    }
    fab.style.bottom = lift ? 'calc(' + Math.round(lift) + 'px + 12px)' : '';
  }
  var st = 0;
  window.addEventListener('scroll', function () { if (!st) st = setTimeout(function () { st = 0; placeFab(); }, 200); }, { passive: true });

  var rt = 0;
  function scheduleFit() { clearTimeout(rt); rt = setTimeout(function () { fitMobile(); placeFab(); }, 150); }

  
  /* ---------------- Mobile Navigation Fullscreen Drawer ---------------- */
  var drawerModal = null;
  function openMobileDrawer() {
    if (!drawerModal) {
      drawerModal = el('div', 'rsi-mobile-drawer');
      drawerModal.innerHTML = 
        '<div class="rsi-drawer-sheet">' +
          '<div class="rsi-drawer-head">' +
            '<div class="rsi-drawer-title"><span>🧭</span> RSI 蜂巢計畫 · 全景導覽</div>' +
            '<button type="button" class="rsi-drawer-close">✕ 關閉</button>' +
          '</div>' +
          '<div class="rsi-drawer-body">' +
            '<div>' +
              '<div class="rsi-drawer-group-title">⭐ 核心推薦方案</div>' +
              '<a href="' + url('Hive/azure_native_architecture_showcase.html') + '" class="rsi-drawer-item is-prime">' +
                '<span class="rsi-drawer-item-icon">🏆</span>' +
                '<div class="rsi-drawer-item-text">Azure 原生架構選型報告<div class="rsi-drawer-item-sub">D365 F&O (C++) ＋ 各廠 MS SQL 雙軌合流</div></div>' +
              '</a>' +
              '<a href="' + url('Hive/platform_selection_4routes_showcase.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">⚖️</span>' +
                '<div class="rsi-drawer-item-text">4 大多雲路線 ＆ MuleSoft 評估<div class="rsi-drawer-item-sub">Azure / GCP / AWS / OpenSource 全面對標</div></div>' +
              '</a>' +
              '<a href="' + url('RSI-data-architecture.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">📊</span>' +
                '<div class="rsi-drawer-item-text">資料整合架構（APIM＋ADF）<div class="rsi-drawer-item-sub">米蘭暖琥珀風格 · 雙泳道互動圖資</div></div>' +
              '</a>' +
            '</div>' +
            '<div>' +
              '<div class="rsi-drawer-group-title">🐝 蜂巢計畫專案中心</div>' +
              '<a href="' + url('Hive/index.html') + '" class="rsi-drawer-item">' +
                '<span class="rsi-drawer-item-icon">🐝</span>' +
                '<div class="rsi-drawer-item-text">蜂巢計畫實施藍圖首頁<div class="rsi-drawer-item-sub">六大推進階段、RACI 與決策閘門</div></div>' +
              '</a>' +
              '<a href="' + url('Hive/download_center.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">📑</span>' +
                '<div class="rsi-drawer-item-text">官方文檔與出版級報表中心<div class="rsi-drawer-item-sub">11 份高畫質 PDF 線上預覽與 Draw.io 原始檔</div></div>' +
              '</a>' +
              '<a href="' + url('gantt_chart_2027.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">📅</span>' +
                '<div class="rsi-drawer-item-text">2027 全專案甘特圖與 WBS<div class="rsi-drawer-item-sub">四大主架構 25 項核心專案排程</div></div>' +
              '</a>' +
            '</div>' +
            '<div>' +
              '<div class="rsi-drawer-group-title">🏛️ 戰略藍圖與治理手冊</div>' +
              '<a href="' + url('index.html') + '" class="rsi-drawer-item">' +
                '<span class="rsi-drawer-item-icon">🏠</span>' +
                '<div class="rsi-drawer-item-text">2027 IT 營運計畫首頁</div>' +
              '</a>' +
              '<a href="' + url('ceo_strategic_plan.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">🏢</span>' +
                '<div class="rsi-drawer-item-text">CEO 戰略營運計畫白皮書</div>' +
              '</a>' +
              '<a href="' + url('vp_chou_worklist.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">📋</span>' +
                '<div class="rsi-drawer-item-text">周副總交辦工作清單</div>' +
              '</a>' +
              '<a href="' + url('organization_resources.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">👥</span>' +
                '<div class="rsi-drawer-item-text">組織職能與資源配置藍圖</div>' +
              '</a>' +
              '<a href="' + url('Hive/it_skills_8domains_assessment.html') + '" class="rsi-drawer-item" style="margin-top:6px;">' +
                '<span class="rsi-drawer-item-icon">📝</span>' +
                '<div class="rsi-drawer-item-text">內部 IT 8 大領域技術職能問卷</div>' +
              '</a>' +
            '</div>' +
          '</div>' +
        '</div>';
      
      document.body.appendChild(drawerModal);
      drawerModal.querySelector('.rsi-drawer-close').addEventListener('click', closeMobileDrawer);
      drawerModal.addEventListener('click', function(e) {
        if (e.target === drawerModal) closeMobileDrawer();
      });
    }
    document.body.style.overflow = 'hidden';
    drawerModal.removeAttribute('hidden');
    requestAnimationFrame(function() {
      drawerModal.classList.add('is-open');
    });
  }

  function closeMobileDrawer() {
    if (!drawerModal) return;
    document.body.style.overflow = '';
    drawerModal.classList.remove('is-open');
    setTimeout(function() {
      drawerModal.setAttribute('hidden', '');
    }, 280);
  }
  window.rsiOpenDrawer = openMobileDrawer;

  function start() {
    var topSearch = buildTop();
    buildUI();
    // The floating search button only appears once the top bar's search has scrolled out of view.
    if ('IntersectionObserver' in window) {
      fab.hidden = true;
      new IntersectionObserver(function (es) { fab.hidden = es[0].isIntersecting; placeFab(); }).observe(topSearch);
    }
    fitMobile();
    placeFab();
    window.addEventListener('load', function () { lastWidth = 0; fitMobile(); placeFab(); });
    window.addEventListener('resize', scheduleFit);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();