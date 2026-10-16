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
  function isUI(n) { return n.closest && n.closest('.rsi-search, .rsi-search-fab'); }

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

  function start() {
    buildUI();
    fitMobile();
    placeFab();
    window.addEventListener('load', function () { lastWidth = 0; fitMobile(); placeFab(); });
    window.addEventListener('resize', scheduleFit);
  }
  if (document.readyState === 'loading') document.addEventListener('DOMContentLoaded', start);
  else start();
})();
