(function () {
  function setDialogLabel(doc) {
    var dialog = doc.querySelector('.md-search[data-md-component="search"]');
    if (!dialog) {
      return;
    }
    var existing = dialog.getAttribute('aria-label');
    if (existing && existing.trim()) {
      return;
    }
    var input = dialog.querySelector('input[aria-label], input[placeholder]');
    var label = '';
    if (input) {
      label = (input.getAttribute('aria-label') || input.getAttribute('placeholder') || '').trim();
    }
    if (!label) {
      label = 'Search';
    }
    dialog.setAttribute('aria-label', label);
  }

  function init() {
    setDialogLabel(document);
    if (window.document$ && typeof window.document$.subscribe === 'function') {
      window.document$.subscribe(function () {
        setDialogLabel(document);
      });
    }
  }

  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', init);
  } else {
    init();
  }
})();
