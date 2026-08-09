// Load the Altium web viewer only on pages that actually embed a project.
(function () {
  'use strict';

  var VIEWER_SELECTOR = '.altium-ecad-viewer';
  var VIEWER_SRC = 'https://viewer.altium.com/client/static/js/embed.js';
  var loading = false;

  function loadViewerIfNeeded() {
    if (!document.querySelector(VIEWER_SELECTOR)) {
      return;
    }

    if (document.querySelector('script[src="' + VIEWER_SRC + '"]') || loading) {
      return;
    }

    loading = true;

    var script = document.createElement('script');
    script.src = VIEWER_SRC;
    script.async = true;
    script.crossOrigin = 'anonymous';
    script.addEventListener('load', function () {
      loading = false;
    }, { once: true });
    script.addEventListener('error', function () {
      loading = false;
      console.error('[Altium] Failed to load the embedded viewer.');
    }, { once: true });

    document.head.appendChild(script);
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', loadViewerIfNeeded, { once: true });
  } else {
    loadViewerIfNeeded();
  }

  if (window.document$ && typeof window.document$.subscribe === 'function') {
    window.document$.subscribe(loadViewerIfNeeded);
  }
})();
