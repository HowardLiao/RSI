/**
 * RSI Project Hive - Site Navigation & Analytics Engine (GA4)
 * Open-access mode: no overlays, zero barrier.
 * Automatically captures visitor paths, scroll depth, and file downloads.
 */
(function () {
  "use strict";

  // === 1. GA4 Configuration ===
  // Replace with your GA4 Measurement ID (e.g. "G-XXXXXXXXXX")
  const GA_MEASUREMENT_ID = window.RSI_GA_ID || "G-PLACEHOLDER";

  // Clean up any legacy modal overlays
  try {
    document.documentElement.classList.remove("rsi-locked");
    if (document.body) {
      document.body.style.overflow = "";
      document.body.style.position = "";
    }
  } catch (e) {}

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

  // === 2. Dynamic GA4 Loader ===
  function initGA4() {
    if (!GA_MEASUREMENT_ID || GA_MEASUREMENT_ID === "G-PLACEHOLDER") {
      console.log("[RSI Analytics] Waiting for GA4 Measurement ID. Set window.RSI_GA_ID or update assets/rsi-gatekeeper.js.");
      return;
    }

    // Prevent duplicate injection
    if (document.getElementById("rsi-gtag-script")) return;

    const script = document.createElement("script");
    script.id = "rsi-gtag-script";
    script.async = true;
    script.src = "https://www.googletagmanager.com/gtag/js?id=" + encodeURIComponent(GA_MEASUREMENT_ID);
    document.head.appendChild(script);

    window.dataLayer = window.dataLayer || [];
    function gtag() { window.dataLayer.push(arguments); }
    window.gtag = gtag;

    gtag("js", new Date());

    // Extract visitor identity from query params (e.g., ?u=vp_chou or ?utm_source=leo)
    const urlParams = new URLSearchParams(window.location.search);
    const visitorIdentity = urlParams.get("u") || urlParams.get("user") || urlParams.get("utm_source") || sessionStorage.getItem("rsi_visitor_id");

    const config = {
      page_title: document.title,
      page_location: window.location.href,
      page_path: window.location.pathname
    };

    if (visitorIdentity) {
      try { sessionStorage.setItem("rsi_visitor_id", visitorIdentity); } catch(e) {}
      config.user_id = visitorIdentity;
      config.visitor_name = visitorIdentity;
      gtag("set", "user_properties", { visitor_identity: visitorIdentity });
    }

    gtag("config", GA_MEASUREMENT_ID, config);
    console.log("[RSI Analytics] GA4 initialized (" + GA_MEASUREMENT_ID + ") for visitor:", visitorIdentity || "anonymous");

    // Track document downloads (docx, csv, pdf, pptx, xlsx)
    document.addEventListener("click", function(e) {
      const a = e.target.closest("a");
      if (!a || !a.href) return;
      const href = a.href;
      if (/\.(docx|csv|pdf|pptx|xlsx|zip)$/i.test(href)) {
        gtag("event", "file_download", {
          file_name: href.split("/").pop(),
          file_url: href,
          link_text: (a.innerText || "").trim(),
          page_path: window.location.pathname
        });
      }
    });
  }

  initGA4();

  window.RSIGatekeeper = {
    isOpen: true,
    bypassed: true,
    gaId: GA_MEASUREMENT_ID,
    setGA: function(id) {
      window.RSI_GA_ID = id;
      initGA4();
    }
  };
})();
