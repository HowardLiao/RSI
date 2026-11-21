/* RSI 2027 Project Hive — Offline-Resilient Service Worker (v8.7.0-refined) */
const CACHE_NAME = 'rsi-2027-hive-v8-7';
const PRECACHE_URLS = [
  './',
  './index.html',
  './manifest.json',
  './rsi_logo_transparent.png',
  './rsi_logo_opt.png',
  './assets/rsi-core.css?v=8.6.0',
  './assets/rsi-site.css?v=d8c3ab7bca',
  './assets/rsi-neon-milan.css?v=8.7.0',
  './assets/rsi-gatekeeper.css?v=2.0',
  './assets/rsi-neon-refine.js?v=8.6.1',
  './assets/rsi-fluid-engine.js?v=8.7.0',
  './assets/rsi-site.js?v=52cc3a28d3',
  './assets/rsi-gatekeeper.js?v=2.2'
];

self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open(CACHE_NAME)
      .then((cache) => cache.addAll(PRECACHE_URLS).catch(() => {}))
      .then(() => self.skipWaiting())
  );
});

self.addEventListener('activate', (event) => {
  event.waitUntil(
    caches.keys().then((keys) =>
      Promise.all(keys.filter((k) => k !== CACHE_NAME).map((k) => caches.delete(k)))
    ).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', (event) => {
  const req = event.request;
  if (req.method !== 'GET') return;
  const url = new URL(req.url);

  // Never intercept telemetry, analytics, or external API beacons
  if (url.hostname.includes('ntfy.sh') || url.hostname.includes('google-analytics') || url.hostname.includes('googletagmanager')) {
    return;
  }

  // Network-first for HTML navigation so executive updates always arrive fresh
  if (req.mode === 'navigate' || (req.headers.get('accept') || '').includes('text/html')) {
    event.respondWith(
      fetch(req)
        .then((res) => {
          if (res && res.ok) {
            const copy = res.clone();
            caches.open(CACHE_NAME).then((c) => c.put(req, copy)).catch(() => {});
          }
          return res;
        })
        .catch(() => caches.match(req).then((r) => r || caches.match('./index.html')))
    );
    return;
  }

  // Stale-while-revalidate for same-origin static assets
  if (url.origin === self.location.origin) {
    event.respondWith(
      caches.match(req).then((cached) => {
        const fetched = fetch(req).then((res) => {
          if (res && res.ok) {
            const copy = res.clone();
            caches.open(CACHE_NAME).then((c) => c.put(req, copy)).catch(() => {});
          }
          return res;
        }).catch(() => cached);
        return cached || fetched;
      })
    );
  }
});
