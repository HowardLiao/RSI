/**
 * RSI Project Hive - Access Gatekeeper (BYPASSED / OPEN ACCESS)
 * All access controls, modal overlays, and locks disabled per executive instruction.
 * Allows instant, open access to all visitors across the site.
 */
(function () {
  "use strict";

  // Unlock document immediately
  try {
    document.documentElement.classList.remove("rsi-locked");
    if (document.body) {
      document.body.style.overflow = "";
      document.body.style.position = "";
    }
  } catch (e) {}

  function removeOverlays() {
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
    document.addEventListener("DOMContentLoaded", removeOverlays);
  } else {
    removeOverlays();
  }

  window.addEventListener("load", removeOverlays);

  window.RSIGatekeeper = {
    isOpen: true,
    bypassed: true,
    unlock: function () { return Promise.resolve(true); },
    verify: function () { return Promise.resolve(true); }
  };
})();
