(function () {
  const SCRIPT_ID = 'altium-embed-script';
  const SCRIPT_SRC = 'https://viewer.altium.com/client/static/js/embed.js';

  function loadScript() {
    if (window.AltiumViewer || document.getElementById(SCRIPT_ID)) {
      return Promise.resolve();
    }
    return new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.id = SCRIPT_ID;
      script.src = SCRIPT_SRC;
      script.async = true;
      script.crossOrigin = 'anonymous';
      script.onload = () => resolve();
      script.onerror = () => reject(new Error('Failed to load Altium viewer script.'));
      document.head.appendChild(script);
    });
  }

  function activateViewers(root) {
    const containers = root.querySelectorAll('.altium-iframe-viewer');
    if (!containers.length) {
      return;
    }

    loadScript().catch((error) => {
      console.error('[Altium] Unable to load embed script:', error);
    });
  }

  function handlePage(root) {
    const scope = root && root.querySelector ? root : document;
    activateViewers(scope);
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', () => handlePage(document));
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(() => handlePage(document));
  }
})();
