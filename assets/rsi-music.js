/* RSI background music — Erik Satie, Gymnopédie No. 1 (1888, public domain composition).
   Synthesised live with the Web Audio API: no audio file, no recording, no third-party rights.
   Starts only when the viewer presses the ♪ button (browsers block autoplay). */
(function () {
  if (window.__rsiMusic) return;
  window.__rsiMusic = true;

  var BPM = 72, BEAT = 60 / BPM;
  var A4 = 440;
  var NOTE = { C: -9, "C#": -8, D: -7, "D#": -6, E: -5, F: -4, "F#": -3, G: -2, "G#": -1, A: 0, "A#": 1, B: 2 };
  function hz(n) { var m = n.match(/^([A-G]#?)(\d)$/); return A4 * Math.pow(2, (NOTE[m[1]] + (m[2] - 4) * 12) / 12); }

  // Left hand: alternating Gmaj7 / Dmaj7 — bass on beat 1, chord on beat 2 held to bar end.
  var LH = [["G2", ["B3", "D4", "F#4"]], ["D2", ["A3", "C#4", "F#4"]]];
  // Melody (beat offset within the 3/4 bar, note, length in beats); 16-bar loop starting at bar 5.
  var MEL = [
    [4, 1, "F#5", 1], [4, 2, "A5", 1],
    [5, 0, "G5", 1], [5, 1, "F#5", 1], [5, 2, "C#5", 1],
    [6, 0, "B4", 1], [6, 1, "C#5", 1], [6, 2, "D5", 1],
    [7, 0, "A4", 3],
    [8, 0, "F#4", 3], [9, 0, "F#4", 3], [10, 0, "F#4", 3], [11, 0, "F#4", 3],
    [12, 1, "F#5", 1], [12, 2, "A5", 1],
    [13, 0, "G5", 1], [13, 1, "F#5", 1], [13, 2, "C#5", 1],
    [14, 0, "B4", 1], [14, 1, "C#5", 1], [14, 2, "D5", 1],
    [15, 0, "A4", 3],
    [16, 0, "C#5", 3], [17, 0, "F#5", 3], [18, 0, "E4", 3], [19, 0, "E4", 3],
  ];
  var BARS = 20;

  var ctx, master, verb, playing = false, timer = null, nextBar = 0, barTime = 0;

  function setup() {
    ctx = new (window.AudioContext || window.webkitAudioContext)();
    master = ctx.createGain(); master.gain.value = 0;
    var lp = ctx.createBiquadFilter(); lp.type = "lowpass"; lp.frequency.value = 2600;
    // soft room: two feedback delays
    verb = ctx.createGain(); verb.gain.value = 0.28;
    [0.137, 0.211].forEach(function (t) {
      var d = ctx.createDelay(1); d.delayTime.value = t;
      var fb = ctx.createGain(); fb.gain.value = 0.42;
      var f = ctx.createBiquadFilter(); f.type = "lowpass"; f.frequency.value = 1800;
      verb.connect(d); d.connect(f); f.connect(fb); fb.connect(d); f.connect(lp);
    });
    master.connect(lp); master.connect(verb); lp.connect(ctx.destination);
  }

  // piano-like voice: sine + quiet triangle partial, quick attack, long exponential decay
  function voice(freq, t, dur, vel) {
    var g = ctx.createGain();
    g.gain.setValueAtTime(0.0001, t);
    g.gain.exponentialRampToValueAtTime(vel, t + 0.012);
    g.gain.exponentialRampToValueAtTime(vel * 0.35, t + 0.5);
    g.gain.exponentialRampToValueAtTime(0.0001, t + Math.max(dur, 0.6) + 1.2);
    [[1, "sine", 1], [2, "triangle", 0.18], [3, "sine", 0.06]].forEach(function (p) {
      var o = ctx.createOscillator(); o.type = p[1]; o.frequency.value = freq * p[0];
      var pg = ctx.createGain(); pg.gain.value = p[2];
      o.connect(pg); pg.connect(g); o.start(t); o.stop(t + Math.max(dur, 0.6) + 1.3);
    });
    g.connect(master);
  }

  function scheduleBar(bar, t) {
    var lh = LH[bar % 2];
    voice(hz(lh[0]), t, BEAT * 3, 0.22);
    lh[1].forEach(function (n) { voice(hz(n), t + BEAT, BEAT * 2, 0.07); });
    MEL.forEach(function (m) { if (m[0] === bar) voice(hz(m[2]), t + m[1] * BEAT, m[3] * BEAT, 0.16); });
  }

  function tick() {
    while (barTime < ctx.currentTime + 1.5) {
      scheduleBar(nextBar, barTime);
      barTime += BEAT * 3;
      nextBar = (nextBar + 1) % BARS;
    }
  }

  function start() {
    if (!ctx) setup();
    ctx.resume();
    nextBar = 0; barTime = ctx.currentTime + 0.1;
    master.gain.cancelScheduledValues(ctx.currentTime);
    master.gain.setTargetAtTime(0.55, ctx.currentTime, 0.6);
    tick(); timer = setInterval(tick, 400); playing = true;
  }
  function stop() {
    playing = false; clearInterval(timer);
    master.gain.cancelScheduledValues(ctx.currentTime);
    master.gain.setTargetAtTime(0, ctx.currentTime, 0.25);
    setTimeout(function () { if (!playing && ctx) ctx.suspend(); }, 1500);
  }

  function ui() {
    var css = document.createElement("style");
    css.textContent =
      ".rsi-music{position:fixed;left:16px;bottom:16px;z-index:2147483000;display:flex;align-items:center;gap:8px;" +
      "padding:9px 14px;border-radius:999px;border:1px solid #A83212;background:#FFFFFF;color:#A83212;" +
      "font:600 13px/1 'Microsoft JhengHei','PingFang TC',system-ui,sans-serif;cursor:pointer;box-shadow:0 4px 14px rgba(45,55,72,.12)}" +
      ".rsi-music[aria-pressed=true]{background:#A83212;color:#FFFFFF}" +
      ".rsi-music .n{font-size:15px}.rsi-music .t{font-family:Cambria,Georgia,serif;font-style:italic;font-weight:400}" +
      "@media print{.rsi-music{display:none}}";
    document.head.appendChild(css);
    var b = document.createElement("button");
    b.type = "button"; b.className = "rsi-music"; b.setAttribute("aria-pressed", "false");
    b.title = "背景音樂：Erik Satie《Gymnopédie No. 1》（公共領域樂曲，瀏覽器即時合成）";
    b.innerHTML = '<span class="n">♪</span><span class="l">背景音樂</span><span class="t">Satie</span>';
    b.addEventListener("click", function () {
      if (playing) stop(); else start();
      b.setAttribute("aria-pressed", String(playing));
      b.querySelector(".l").textContent = playing ? "暫停音樂" : "背景音樂";
    });
    document.body.appendChild(b);
  }
  if (document.readyState === "loading") document.addEventListener("DOMContentLoaded", ui); else ui();
})();
