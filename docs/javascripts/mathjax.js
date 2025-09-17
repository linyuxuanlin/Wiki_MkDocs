(function () {
  const MATHJAX_SRC = 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/tex-mml-chtml.js';
  const PANGU_SRC = (typeof document !== 'undefined') ? new URL('javascripts/pangu.min.js', document.baseURI).href : '/javascripts/pangu.min.js';
  const pendingScripts = new Map();
  let mathjaxReady;

  window.MathJax = {
    tex: {
      inlineMath: [["\(", "\)"]],
      displayMath: [["\[", "\]"]],
      processEscapes: true,
      processEnvironments: true
    },
    options: {
      ignoreHtmlClass: ".*|",
      processHtmlClass: "arithmatex"
    },
    chtml: {
      fontURL: 'https://cdnjs.cloudflare.com/ajax/libs/mathjax/3.2.2/es5/output/chtml/fonts/woff-v2'
    }
  };

  function loadScript(id, src, attrs) {
    if (pendingScripts.has(id)) {
      return pendingScripts.get(id);
    }

    if (document.getElementById(id)) {
      return Promise.resolve();
    }

    const promise = new Promise((resolve, reject) => {
      const script = document.createElement('script');
      script.id = id;
      script.src = src;
      script.async = true;

      if (attrs) {
        Object.keys(attrs).forEach((key) => {
          if (key === 'defer' || key === 'async') {
            script[key] = Boolean(attrs[key]);
          } else {
            script.setAttribute(key, attrs[key]);
          }
        });
      }

      script.onload = () => resolve();
      script.onerror = () => reject(new Error('Failed to load script: ' + src));
      document.head.appendChild(script);
    });

    pendingScripts.set(id, promise);
    return promise;
  }

  function ensureMathJax(root) {
    if (!root.querySelector('.arithmatex')) {
      return;
    }

    if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
      window.MathJax.typesetPromise();
      return;
    }

    if (!mathjaxReady) {
      mathjaxReady = loadScript('mathjax-cdn-script', MATHJAX_SRC, { defer: true, crossorigin: 'anonymous' })
        .then(() => {
          if (window.MathJax && window.MathJax.startup && window.MathJax.startup.promise) {
            return window.MathJax.startup.promise;
          }
          return undefined;
        })
        .catch((error) => {
          console.error('[MathJax] Unable to load:', error);
        });
    }

    mathjaxReady?.then(() => {
      if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
        window.MathJax.typesetPromise();
      }
    });
  }

  function applyPangu(root) {
    const target = root.querySelector('.md-content');
    if (!target || !window.pangu) {
      return;
    }

    if (typeof window.pangu.spacingElement === 'function') {
      window.pangu.spacingElement(target);
    } else if (typeof window.pangu.spacingPageBody === 'function') {
      window.pangu.spacingPageBody();
    }
  }

  let panguLoading;

  function ensurePangu(root) {
    if (document.documentElement && document.documentElement.lang && document.documentElement.lang.indexOf('zh') !== 0) {
      return;
    }

    if (!root.querySelector('.md-content')) {
      return;
    }

    if (window.pangu) {
      applyPangu(root);
      return;
    }

    if (!panguLoading) {
      panguLoading = loadScript('pangu-script', PANGU_SRC, { defer: true })
        .catch((error) => {
          console.error('[Pangu] Unable to load:', error);
        });
    }

    panguLoading?.then(() => applyPangu(root));
  }

  function handlePage() {
    const root = document;
    ensureMathJax(root);
    ensurePangu(root);
  }

  if (typeof document !== 'undefined') {
    document.addEventListener('DOMContentLoaded', handlePage);
  }

  if (typeof document$ !== 'undefined') {
    document$.subscribe(handlePage);
  }
})();
