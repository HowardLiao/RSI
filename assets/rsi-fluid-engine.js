/* ==========================================================================
   RSI 2027 Project Hive — Neon v8.5.0 Fluid Dynamics & Hyper-Interactive Engine
   1. Ambient Hydrodynamic Curl-Flow & Pointer Vortex Canvas (#neonFluidAmbientCanvas)
   2. Interactive Liquid-Surface Wave Coupling (Pointer-reactive Fluid Waves)
   3. Liquid Glass 3D Spring Tilt + Specular Cursor Highlight on Executive Cards
   4. Magnetic Fluid Buttons + Viscous Click Ripples
   5. Scroll Velocity Fluid Glow + Staggered Spring Reveal
   6. Interactive WBS Row Click -> Fluid Slide-Over Executive Detail Drawer
   7. Live Fluid Energy Mode Switcher (Standard / Turbo Vortex / Calm)
   ========================================================================== */
(function () {
  'use strict';

  const FLUID_MODE_KEY = 'rsi_neon_fluid_mode'; // 'calm' | 'standard' | 'turbo'
  const REDUCED_MOTION = window.matchMedia && window.matchMedia('(prefers-reduced-motion: reduce)').matches;
  const IS_TOUCH = window.matchMedia && window.matchMedia('(pointer: coarse)').matches;

  // Default to calm executive mode (zero background particle distraction unless opted in)
  let fluidMode = 'calm';
  if (!REDUCED_MOTION) {
    try {
      const saved = localStorage.getItem(FLUID_MODE_KEY);
      if (saved === 'standard' || saved === 'turbo' || saved === 'calm') {
        fluidMode = saved;
      }
    } catch (e) {}
  }

  /* ------------------------------------------------------------------------
     1. Ambient Hydrodynamic Fluid Field Canvas (Curl-Noise + Vortex Ripples)
     ------------------------------------------------------------------------ */
  class AmbientFluidField {
    constructor() {
      this.canvas = document.createElement('canvas');
      this.canvas.id = 'neonFluidAmbientCanvas';
      this.canvas.setAttribute('aria-hidden', 'true');
      document.body.prepend(this.canvas);
      this.ctx = this.canvas.getContext('2d');

      this.dpr = Math.min(window.devicePixelRatio || 1, 2);
      this.width = 0;
      this.height = 0;
      this.particles = [];
      this.ripples = [];
      this.pointer = { x: -9999, y: -9999, vx: 0, vy: 0, active: false };
      this.lastScrollY = window.scrollY || 0;
      this.scrollVel = 0;
      this.time = 0;
      this.rafId = null;

      this.resize();
      this.initParticles();
      this.bindEvents();
      this.start();
    }

    getPalette() {
      const isDark = document.documentElement.getAttribute('data-theme') === 'obsidian';
      if (isDark) {
        return {
          fade: 'rgba(14, 13, 12, 0.12)',
          streams: ['rgba(245, 158, 11, 0.42)', 'rgba(232, 117, 36, 0.34)', 'rgba(252, 211, 77, 0.28)', 'rgba(56, 189, 248, 0.20)'],
          ripple: 'rgba(245, 158, 11, 0.45)',
          glow: 'rgba(245, 158, 11, 0.14)'
        };
      }
      return {
        fade: 'rgba(247, 244, 239, 0.14)',
        streams: ['rgba(194, 65, 12, 0.22)', 'rgba(232, 117, 36, 0.24)', 'rgba(217, 119, 6, 0.20)', 'rgba(21, 128, 61, 0.12)'],
        ripple: 'rgba(194, 65, 12, 0.30)',
        glow: 'rgba(232, 117, 36, 0.10)'
      };
    }

    resize() {
      this.width = window.innerWidth;
      this.height = window.innerHeight;
      this.canvas.width = Math.floor(this.width * this.dpr);
      this.canvas.height = Math.floor(this.height * this.dpr);
      this.canvas.style.width = this.width + 'px';
      this.canvas.style.height = this.height + 'px';
      this.ctx.setTransform(this.dpr, 0, 0, this.dpr, 0, 0);
    }

    initParticles() {
      const baseCount = this.width < 768 ? 24 : 52;
      const count = fluidMode === 'turbo' ? Math.round(baseCount * 1.45) : baseCount;
      this.particles = [];
      for (let i = 0; i < count; i++) {
        this.particles.push(this.spawnParticle(true));
      }
    }

    spawnParticle(randomPos) {
      const x = randomPos ? Math.random() * this.width : (Math.random() < 0.5 ? 0 : Math.random() * this.width);
      const y = randomPos ? Math.random() * this.height : (Math.random() < 0.5 ? Math.random() * this.height : this.height);
      return {
        x, y,
        px: x, py: y,
        vx: (Math.random() - 0.5) * 0.6,
        vy: (Math.random() - 0.5) * 0.6,
        life: 60 + Math.random() * 180,
        maxLife: 240,
        radius: 1.1 + Math.random() * 2.1,
        colorIdx: Math.floor(Math.random() * 4),
        phase: Math.random() * Math.PI * 2
      };
    }

    addRipple(x, y, strength) {
      if (fluidMode === 'calm') return;
      this.ripples.push({
        x, y,
        r: 6,
        maxR: (strength || 1) * (fluidMode === 'turbo' ? 210 : 145),
        alpha: 0.55,
        lineWidth: 2.2
      });
      if (this.ripples.length > 10) this.ripples.shift();
    }

    bindEvents() {
      let resizeTimer = null;
      window.addEventListener('resize', () => {
        clearTimeout(resizeTimer);
        resizeTimer = setTimeout(() => {
          this.resize();
          this.initParticles();
        }, 150);
      }, { passive: true });

      window.addEventListener('pointermove', (e) => {
        if (fluidMode === 'calm') return;
        const nx = e.clientX;
        const ny = e.clientY;
        if (this.pointer.active) {
          this.pointer.vx = (nx - this.pointer.x) * 0.35;
          this.pointer.vy = (ny - this.pointer.y) * 0.35;
        }
        this.pointer.x = nx;
        this.pointer.y = ny;
        this.pointer.active = true;
      }, { passive: true });

      window.addEventListener('pointerleave', () => {
        this.pointer.active = false;
      }, { passive: true });

      window.addEventListener('pointerdown', (e) => {
        this.addRipple(e.clientX, e.clientY, 1.0);
      }, { passive: true });

      window.addEventListener('scroll', () => {
        const y = window.scrollY || 0;
        const delta = y - this.lastScrollY;
        this.lastScrollY = y;
        this.scrollVel = Math.max(-35, Math.min(35, this.scrollVel * 0.5 + delta * 0.25));
      }, { passive: true });
    }

    // Smooth analytic curl-like vector field (divergence-free feel)
    fieldAngle(x, y, t) {
      const s = 0.0024;
      const a = Math.sin(x * s + t * 0.55) + Math.cos(y * s - t * 0.42);
      const b = Math.sin((x + y) * s * 0.72 - t * 0.31);
      return (a + b) * Math.PI * 0.85;
    }

    step() {
      if (document.hidden || fluidMode === 'calm') {
        this.ctx.clearRect(0, 0, this.width, this.height);
        this.rafId = null;
        return;
      }

      const pal = this.getPalette();
      const ctx = this.ctx;
      const energy = fluidMode === 'turbo' ? 1.55 : 1.0;

      this.time += 0.0085 * energy;
      this.scrollVel *= 0.90;
      this.pointer.vx *= 0.88;
      this.pointer.vy *= 0.88;

      // Translucent trail clear for viscous ribbon look
      ctx.globalCompositeOperation = 'source-over';
      ctx.fillStyle = pal.fade;
      ctx.fillRect(0, 0, this.width, this.height);

      // Soft hydrodynamic aura following pointer
      if (this.pointer.active) {
        const auraR = fluidMode === 'turbo' ? 190 : 140;
        const grad = ctx.createRadialGradient(this.pointer.x, this.pointer.y, 4, this.pointer.x, this.pointer.y, auraR);
        grad.addColorStop(0, pal.glow);
        grad.addColorStop(1, 'rgba(0,0,0,0)');
        ctx.fillStyle = grad;
        ctx.beginPath();
        ctx.arc(this.pointer.x, this.pointer.y, auraR, 0, Math.PI * 2);
        ctx.fill();
      }

      // Update & draw fluid streamlines
      for (let i = 0; i < this.particles.length; i++) {
        const p = this.particles[i];
        p.px = p.x;
        p.py = p.y;

        const angle = this.fieldAngle(p.x, p.y, this.time + p.phase * 0.12);
        const speed = (0.72 + 0.35 * Math.sin(this.time + p.phase)) * energy;

        p.vx = p.vx * 0.86 + Math.cos(angle) * speed * 0.24;
        p.vy = p.vy * 0.86 + Math.sin(angle) * speed * 0.24 - this.scrollVel * 0.045;

        // Pointer viscous vortex coupling
        if (this.pointer.active) {
          const dx = p.x - this.pointer.x;
          const dy = p.y - this.pointer.y;
          const distSq = dx * dx + dy * dy;
          const influenceR = fluidMode === 'turbo' ? 220 : 165;
          if (distSq > 9 && distSq < influenceR * influenceR) {
            const dist = Math.sqrt(distSq);
            const force = (1 - dist / influenceR) * 0.55 * energy;
            // Tangential swirl + pointer drag
            p.vx += (-dy / dist) * force * 0.9 + this.pointer.vx * force * 0.16;
            p.vy += (dx / dist) * force * 0.9 + this.pointer.vy * force * 0.16;
          }
        }

        p.x += p.vx * 2.1;
        p.y += p.vy * 2.1;
        p.life -= 1;

        const outOfBounds = p.x < -30 || p.x > this.width + 30 || p.y < -30 || p.y > this.height + 30;
        if (p.life <= 0 || outOfBounds) {
          const np = this.spawnParticle(true);
          p.x = p.px = np.x;
          p.y = p.py = np.y;
          p.vx = np.vx;
          p.vy = np.vy;
          p.life = np.life;
          continue;
        }

        ctx.strokeStyle = pal.streams[p.colorIdx];
        ctx.lineWidth = p.radius;
        ctx.lineCap = 'round';
        ctx.beginPath();
        ctx.moveTo(p.px, p.py);
        ctx.lineTo(p.x, p.y);
        ctx.stroke();
      }

      // Draw expanding liquid ripples
      for (let i = this.ripples.length - 1; i >= 0; i--) {
        const rp = this.ripples[i];
        rp.r += (rp.maxR - rp.r) * 0.095 + 1.4;
        rp.alpha *= 0.92;
        if (rp.alpha < 0.02 || rp.r >= rp.maxR) {
          this.ripples.splice(i, 1);
          continue;
        }
        ctx.save();
        ctx.globalAlpha = rp.alpha;
        ctx.strokeStyle = pal.ripple;
        ctx.lineWidth = rp.lineWidth;
        ctx.beginPath();
        ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
        ctx.stroke();
        ctx.restore();
      }

      this.rafId = requestAnimationFrame(() => this.step());
    }

    start() {
      if (fluidMode === 'calm') {
        this.ctx.clearRect(0, 0, this.width, this.height);
        return;
      }
      if (!this.rafId) {
        this.ctx.clearRect(0, 0, this.width, this.height);
        this.rafId = requestAnimationFrame(() => this.step());
      }
    }

    syncMode() {
      if (fluidMode === 'calm') {
        if (this.rafId) cancelAnimationFrame(this.rafId);
        this.rafId = null;
        this.ctx.clearRect(0, 0, this.width, this.height);
      } else {
        this.initParticles();
        this.start();
      }
    }
  }

  /* ------------------------------------------------------------------------
     2. Liquid Glass 3D Spring Tilt & Specular Cursor Glow
     ------------------------------------------------------------------------ */
  function initLiquidGlassCards() {
    if (IS_TOUCH) return;
    const selector = [
      '.hero-bento-grid .bento-card',
      '.pillar-card',
      '.chart-card',
      '.doc-card',
      '.rec-card',
      '.author-dossier-card',
      '.finops-kpi-card',
      '.sim-gate-card'
    ].join(', ');

    const cards = document.querySelectorAll(selector);
    cards.forEach((card) => {
      if (card.dataset.fluidTiltBound) return;
      card.dataset.fluidTiltBound = '1';
      card.classList.add('fluid-glass-card');

      let raf = null;
      let targetRx = 0, targetRy = 0;

      card.addEventListener('pointermove', (e) => {
        if (fluidMode === 'calm') return;
        const rect = card.getBoundingClientRect();
        const px = (e.clientX - rect.left) / rect.width;
        const py = (e.clientY - rect.top) / rect.height;

        card.style.setProperty('--mx', (px * 100).toFixed(1) + '%');
        card.style.setProperty('--my', (py * 100).toFixed(1) + '%');

        const maxTilt = fluidMode === 'turbo' ? 6.2 : 3.6;
        targetRy = (px - 0.5) * maxTilt * 2;
        targetRx = (0.5 - py) * maxTilt * 2;

        if (!raf) {
          raf = requestAnimationFrame(() => {
            card.style.transform = `perspective(950px) rotateX(${targetRx.toFixed(2)}deg) rotateY(${targetRy.toFixed(2)}deg) translateY(-3px)`;
            raf = null;
          });
        }
      }, { passive: true });

      card.addEventListener('pointerleave', () => {
        if (raf) { cancelAnimationFrame(raf); raf = null; }
        card.style.transform = '';
      }, { passive: true });
    });
  }

  /* ------------------------------------------------------------------------
     3. Magnetic Fluid Buttons & Viscous Click Ripples
     ------------------------------------------------------------------------ */
  function initMagneticButtonsAndRipples() {
    const magneticSelectors = [
      '.neon-fab-btn',
      '.hero-cta-strip a',
      '.finops-scope-btn',
      '.wbs-csv-btn',
      '.neon-theme-btn',
      '.neon-util-cta',
      '.wbs-filter-btn'
    ].join(', ');

    const bindMagnetic = (el) => {
      if (el.dataset.fluidMagBound) return;
      el.dataset.fluidMagBound = '1';
      el.classList.add('fluid-magnetic');

      if (!IS_TOUCH) {
        el.addEventListener('pointermove', (e) => {
          if (fluidMode === 'calm') return;
          const r = el.getBoundingClientRect();
          const dx = (e.clientX - (r.left + r.width / 2)) / (r.width / 2);
          const dy = (e.clientY - (r.top + r.height / 2)) / (r.height / 2);
          const pull = fluidMode === 'turbo' ? 7 : 4.2;
          el.style.transform = `translate3d(${(dx * pull).toFixed(1)}px, ${(dy * pull).toFixed(1)}px, 0)`;
        }, { passive: true });

        el.addEventListener('pointerleave', () => {
          el.style.transform = '';
        }, { passive: true });
      }

      el.addEventListener('pointerdown', (e) => {
        if (fluidMode === 'calm') return;
        const r = el.getBoundingClientRect();
        const ripple = document.createElement('span');
        ripple.className = 'fluid-btn-ripple';
        const size = Math.max(r.width, r.height) * 1.9;
        ripple.style.width = ripple.style.height = size + 'px';
        ripple.style.left = (e.clientX - r.left - size / 2) + 'px';
        ripple.style.top = (e.clientY - r.top - size / 2) + 'px';
        el.appendChild(ripple);
        setTimeout(() => ripple.remove(), 620);
      }, { passive: true });
    };

    document.querySelectorAll(magneticSelectors).forEach(bindMagnetic);

    // Also attach ripple/magnetic to dynamically added buttons (e.g. .wbs-csv-btn)
    const mo = new MutationObserver(() => {
      document.querySelectorAll(magneticSelectors).forEach(bindMagnetic);
    });
    mo.observe(document.body, { childList: true, subtree: true });
    setTimeout(() => mo.disconnect(), 8000);
  }

  /* ------------------------------------------------------------------------
     4. Interactive Coupling on Existing Fluid Wave Canvases
     ------------------------------------------------------------------------ */
  function initWaveCanvasInteraction() {
    document.querySelectorAll('.fluid-wave-canvas-wrap').forEach((wrap) => {
      wrap.classList.add('fluid-wave-interactive');
      wrap.addEventListener('pointermove', (e) => {
        if (fluidMode === 'calm') return;
        const r = wrap.getBoundingClientRect();
        const pct = ((e.clientX - r.left) / r.width) * 100;
        wrap.style.setProperty('--wave-x', pct.toFixed(1) + '%');
      }, { passive: true });

      wrap.addEventListener('pointerenter', () => {
        if (fluidMode === 'calm') return;
        if (window.valueChainWave && typeof window.valueChainWave.surge === 'function') {
          window.valueChainWave.surge();
        }
        if (window.gateWave && typeof window.gateWave.surge === 'function') {
          window.gateWave.surge();
        }
      }, { passive: true });
    });
  }

  /* ------------------------------------------------------------------------
     5. Scroll-Velocity Liquid Progress & Staggered Fluid Reveal
     ------------------------------------------------------------------------ */
  function initFluidScrollEffects() {
    const progressBar = document.querySelector('.neon-read-progress');
    let lastY = window.scrollY || 0;
    let decayTimer = null;

    if (progressBar) {
      window.addEventListener('scroll', () => {
        const y = window.scrollY || 0;
        const speed = Math.min(1, Math.abs(y - lastY) / 90);
        lastY = y;
        progressBar.style.setProperty('--scroll-glow', (0.35 + speed * 0.65).toFixed(2));
        progressBar.classList.add('is-flowing');
        clearTimeout(decayTimer);
        decayTimer = setTimeout(() => progressBar.classList.remove('is-flowing'), 240);
      }, { passive: true });
    }

    if (!('IntersectionObserver' in window) || REDUCED_MOTION) return;

    const revealTargets = document.querySelectorAll(
      'section[id], .chart-card, .pillar-card, .doc-card, .rec-card, .wbs-container, .dynamic-simulator-box'
    );
    const io = new IntersectionObserver((entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('fluid-revealed');
          io.unobserve(entry.target);
        }
      });
    }, { threshold: 0.04, rootMargin: '0px 0px -30px 0px' });

    revealTargets.forEach((el) => {
      const rect = el.getBoundingClientRect();
      // Never hide elements already in or above the initial viewport
      if (rect.top > window.innerHeight * 1.05) {
        el.classList.add('fluid-reveal-pending');
        io.observe(el);
      }
    });
  }

  /* ------------------------------------------------------------------------
     6. Interactive WBS Slide-Over Executive Detail Drawer
     ------------------------------------------------------------------------ */
  function initWbsInteractiveDrawer() {
    const rows = document.querySelectorAll('.wbs-row');
    if (!rows.length) return;

    const backdrop = document.createElement('div');
    backdrop.id = 'neonWbsDrawerBackdrop';
    backdrop.className = 'fluid-drawer-backdrop';
    backdrop.setAttribute('aria-hidden', 'true');
    backdrop.innerHTML = `
      <aside class="fluid-drawer-panel" role="dialog" aria-modal="true" aria-labelledby="fluidDrawerTitle">
        <div class="fluid-drawer-head">
          <div>
            <div class="fluid-drawer-eyebrow" id="fluidDrawerCode">WBS DETAIL</div>
            <h3 class="fluid-drawer-title" id="fluidDrawerTitle">專案明細</h3>
          </div>
          <button type="button" class="fluid-drawer-close" id="fluidDrawerClose" aria-label="關閉">✕</button>
        </div>
        <div class="fluid-drawer-body" id="fluidDrawerBody"></div>
        <div class="fluid-drawer-foot">
          <button type="button" class="fluid-drawer-btn primary" id="fluidDrawerCopyBtn">📋 複製此項摘要</button>
          <a href="#invest-framework" class="fluid-drawer-btn" id="fluidDrawerFinOpsLink">💵 模擬 FinOps ROI</a>
        </div>
      </aside>
    `;
    document.body.appendChild(backdrop);

    let activeSummaryText = '';
    let lastFocusedBeforeDrawer = null;

    const closeDrawer = () => {
      backdrop.classList.remove('open');
      backdrop.setAttribute('aria-hidden', 'true');
      document.body.classList.remove('fluid-drawer-open');
      if (lastFocusedBeforeDrawer && typeof lastFocusedBeforeDrawer.focus === 'function') {
        lastFocusedBeforeDrawer.focus();
      }
    };

    backdrop.addEventListener('click', (e) => {
      if (e.target === backdrop) closeDrawer();
    });
    document.getElementById('fluidDrawerClose')?.addEventListener('click', closeDrawer);
    document.getElementById('fluidDrawerFinOpsLink')?.addEventListener('click', closeDrawer);
    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape' && backdrop.classList.contains('open')) closeDrawer();
    });

    document.getElementById('fluidDrawerCopyBtn')?.addEventListener('click', () => {
      if (navigator.clipboard && navigator.clipboard.writeText && activeSummaryText) {
        navigator.clipboard.writeText(activeSummaryText).then(() => {
          const btn = document.getElementById('fluidDrawerCopyBtn');
          if (btn) {
            const orig = btn.textContent;
            btn.textContent = '✅ 已複製到剪貼簿';
            setTimeout(() => { btn.textContent = orig; }, 1800);
          }
        });
      }
    });

    rows.forEach((row) => {
      row.classList.add('fluid-wbs-clickable');
      row.setAttribute('title', '點擊展開 WBS 專案戰情詳情抽屜');

      row.addEventListener('click', () => {
        const tds = Array.from(row.querySelectorAll('td'));
        const cells = tds.map((td) => td.innerText.trim().replace(/\s+/g, ' '));
        const code = cells[0] || row.dataset.id || 'WBS';
        const titleEl = tds[1] ? tds[1].querySelector('div') : null;
        const title = titleEl ? titleEl.innerText.trim() : (cells[1] || '專案工作包');
        const pillar = row.dataset.pillar || '2027 戰略主軸';
        const rawCat = (row.dataset.cat || cells[2] || 'run').toLowerCase();
        const startDate = cells[3] || '—';
        const endDate = cells[4] || '—';
        const duration = cells[5] || '—';
        const owner = cells[6] || 'RSI IT PMO';
        const milestone = cells[7] || '依 4-Gate 雙簽與季度里程碑交付';
        const budgetRaw = cells[8] || cells.find((c) => /\$|USD/i.test(c)) || '—';
        const usdMatch = budgetRaw.replace(/,/g, '').match(/(\d+(?:\.\d+)?)/);
        const usdVal = usdMatch ? parseFloat(usdMatch[1]) : 0;
        const ntdWan = usdVal > 0 ? Math.round((usdVal * 31.5) / 10000) : 0;
        const sharePct = usdVal > 0 ? ((usdVal / 1390000) * 100).toFixed(1) : '0.0';
        const schedule = `${startDate} → ${endDate}（${duration}）`;

        const isGrow = rawCat.includes('grow');
        const isTrans = rawCat.includes('trans');
        const catClass = isGrow ? 'cat-grow' : (isTrans ? 'cat-trans' : 'cat-run');
        const catLabel = isGrow ? 'Grow 成長擴張' : (isTrans ? 'Transform 轉型創新' : 'Run 穩健營運');

        document.getElementById('fluidDrawerCode').textContent = `${code} · ${pillar}`;
        document.getElementById('fluidDrawerTitle').textContent = title;
        document.getElementById('fluidDrawerBody').innerHTML = `
          <div class="fluid-drawer-badges">
            <span class="cat-badge ${catClass}">${catLabel}</span>
            <span class="fluid-drawer-pill">📅 ${schedule}</span>
          </div>
          <div class="fluid-drawer-metrics">
            <div class="fd-metric">
              <div class="fd-label">核定預算 (USD)</div>
              <div class="fd-val">${usdVal > 0 ? '$' + usdVal.toLocaleString() : budgetRaw}</div>
            </div>
            <div class="fd-metric">
              <div class="fd-label">約當台幣 (NT$ 萬)</div>
              <div class="fd-val">${ntdWan > 0 ? 'NT$ ' + ntdWan.toLocaleString() + ' 萬' : '—'}</div>
            </div>
          </div>
          <div class="fluid-drawer-share">
            <div class="fd-share-head">
              <span>佔 2027 全年 IT 總預算 ($1,390K) 比重</span>
              <strong>${sharePct}%</strong>
            </div>
            <div class="fd-share-track"><div class="fd-share-fill" style="width:${Math.min(100, parseFloat(sharePct) * 3.5)}%"></div></div>
          </div>
          <div class="fluid-drawer-kv">
            <div><span>主責單位</span><strong>${owner}</strong></div>
            <div><span>關鍵里程碑與交付物</span><strong>${milestone}</strong></div>
            <div><span>治理口徑</span><strong>${isTrans ? 'AI 決策賦能 / 商業模式升級' : (isGrow ? '產能擴張 / 跨廠資料貫通' : '零中斷防禦 / SLA 99.95%')}</strong></div>
            <div><span>門禁稽核狀態</span><strong>納入 4-Gate 雙簽與季度 FinOps 覆核</strong></div>
          </div>
        `;

        activeSummaryText = `[RSI 2027 WBS] ${code} ${title} (${pillar}) | 分類: ${catLabel} | 主責: ${owner} | 預算: $${usdVal.toLocaleString()} USD (約 NT$ ${ntdWan} 萬, 佔總額 ${sharePct}%) | 時程: ${schedule} | 里程碑: ${milestone}`;
        lastFocusedBeforeDrawer = document.activeElement;
        backdrop.setAttribute('aria-hidden', 'false');
        backdrop.classList.add('open');
        document.body.classList.add('fluid-drawer-open');
        setTimeout(() => { document.getElementById('fluidDrawerClose')?.focus(); }, 60);
      });
    });
  }

  /* ------------------------------------------------------------------------
     7. Live Fluid Energy Mode Toggle in FAB Group
     ------------------------------------------------------------------------ */
  function initFluidModeToggle(ambient) {
    const applyMode = (mode, announce) => {
      fluidMode = mode;
      document.documentElement.setAttribute('data-fluid', mode);
      try { localStorage.setItem(FLUID_MODE_KEY, mode); } catch (e) {}
      if (ambient) ambient.syncMode();

      const btn = document.getElementById('neonFabFluid');
      if (btn) {
        btn.textContent = mode === 'turbo' ? '🌀' : (mode === 'calm' ? '🧊' : '🌊');
        btn.title = mode === 'turbo'
          ? '流體力學模式：高動能渦流（點擊切換極簡靜態）'
          : (mode === 'calm' ? '流體力學模式：極簡靜態（點擊開啟標準流體）' : '流體力學模式：標準流體（點擊開啟高動能渦流）');
      }

      if (announce) {
        const msg = mode === 'turbo'
          ? '🌀 流體力學：高動能渦流模式（強化流場與 3D 液態阻尼）'
          : (mode === 'calm' ? '🧊 流體力學：極簡靜態模式（低耗電簡報模式）' : '🌊 流體力學：標準流體動能模式');
        let t = document.getElementById('neonToast');
        if (t) {
          t.textContent = msg;
          t.classList.add('show');
          clearTimeout(t._timer);
          t._timer = setTimeout(() => t.classList.remove('show'), 2500);
        }
      }
    };

    const mountBtn = () => {
      const fab = document.querySelector('.neon-fab-group');
      if (!fab || document.getElementById('neonFabFluid')) return;
      const btn = document.createElement('button');
      btn.type = 'button';
      btn.id = 'neonFabFluid';
      btn.className = 'neon-fab-btn fab-fluid';
      btn.setAttribute('aria-label', '切換流體力學動效強度');
      btn.addEventListener('click', () => {
        const next = fluidMode === 'standard' ? 'turbo' : (fluidMode === 'turbo' ? 'calm' : 'standard');
        applyMode(next, true);
      });
      // Insert right after search FAB
      fab.insertBefore(btn, fab.children[1] || null);
      applyMode(fluidMode, false);
    };

    mountBtn();
    setTimeout(mountBtn, 300);

    window.__neonSetFluidMode = (m) => applyMode(m, true);
    document.addEventListener('visibilitychange', () => {
      if (!document.hidden && ambient && fluidMode !== 'calm') ambient.start();
    });
  }

  /* ------------------------------------------------------------------------
     Bootstrap
     ------------------------------------------------------------------------ */
  function bootstrapFluidEngine() {
    document.documentElement.setAttribute('data-fluid', fluidMode);
    const ambient = new AmbientFluidField();
    initLiquidGlassCards();
    initMagneticButtonsAndRipples();
    initWaveCanvasInteraction();
    initFluidScrollEffects();
    initWbsInteractiveDrawer();
    initFluidModeToggle(ambient);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', bootstrapFluidEngine);
  } else {
    bootstrapFluidEngine();
  }
})();
