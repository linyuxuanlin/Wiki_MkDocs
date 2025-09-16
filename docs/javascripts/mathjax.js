window.MathJax = {
  tex: {
    inlineMath: [["\\(", "\\)"]],
    displayMath: [["\\[", "\\]"]],
    processEscapes: true,
    processEnvironments: true
  },
  options: {
    ignoreHtmlClass: ".*|",
    processHtmlClass: "arithmatex"
  },
  chtml: {
    fontURL: 'https://cdn.jsdelivr.net/npm/mathjax@3/es5/output/chtml/fonts/woff-v2'
  }
};

document$.subscribe(() => {
  if (window.MathJax && typeof window.MathJax.typesetPromise === 'function') {
    window.MathJax.typesetPromise();
  }
  if (window.pangu && typeof window.pangu.spacingPageBody === 'function') {
    window.pangu.spacingPageBody();
  }
});
