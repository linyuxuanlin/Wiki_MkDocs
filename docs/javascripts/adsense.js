// Simplified AdSense insertion script with locale-aware home detection
(function () {
    'use strict';

    var AD_CLIENT = 'ca-pub-4776987651904746';
    var AD_SLOT = window.ADSENSE_SLOT_ID || window.ADSENSE_SLOT || '7746286479';
    var DEFAULT_LOCALE = 'zh';
    var SUPPORTED_LOCALES = ['zh', 'en', 'es', 'ar'];
    var LOCALE_PREFIXES = {
        zh: ['/', '/zh/'],
        en: ['/en/'],
        es: ['/es/'],
        ar: ['/ar/']
    };
    var ADSENSE_SCRIPT_SELECTOR = 'script[src*="pagead/js/adsbygoogle.js"]';
    var ADSENSE_STYLE_ID = 'adsense-style';
    var ADSENSE_STYLE_PATH = window.ADSENSE_STYLE_PATH || 'stylesheets/adsense.css';

    if (!AD_SLOT) {
        console.warn('[AdSense] Missing data-ad-slot id. Set window.ADSENSE_SLOT_ID before this script runs.');
        return;
    }

    function getLocale() {
        var lang = (document.documentElement.getAttribute('lang') || '').trim().toLowerCase();
        if (SUPPORTED_LOCALES.indexOf(lang) !== -1) {
            return lang;
        }
        var match = window.location.pathname.match(/^\/(zh|en|es|ar)\//);
        if (match) {
            return match[1];
        }
        return DEFAULT_LOCALE;
    }

    function normalisePath(pathname) {
        if (!pathname) {
            return '/';
        }
        if (pathname === '/') {
            return pathname;
        }
        if (pathname.endsWith('/')) {
            return pathname;
        }
        if (pathname.endsWith('/index.html')) {
            return pathname.replace(/index\.html$/, '');
        }
        return pathname;
    }

    function isHomePath(pathname, locale) {
        var prefixes = LOCALE_PREFIXES[locale] || ['/' + locale + '/'];
        var normalised = normalisePath(pathname);
        for (var i = 0; i < prefixes.length; i += 1) {
            var prefix = prefixes[i];
            if (!prefix) {
                continue;
            }
            if (prefix === '/' && locale === DEFAULT_LOCALE) {
                if (normalised === '/' || normalised === '/zh/') {
                    return true;
                }
            } else if (normalised === prefix) {
                return true;
            }
        }
        return false;
    }

    function isHomePage() {
        var locale = getLocale();
        if (isHomePath(window.location.pathname, locale)) {
            return true;
        }
        var title = (document.title || '').trim();
        return title === 'Home' || title === "Power's Wiki";
    }

    function ensureAdsenseStyles() {
        if (document.getElementById(ADSENSE_STYLE_ID)) {
            return;
        }
        var link = document.createElement('link');
        link.id = ADSENSE_STYLE_ID;
        link.rel = 'stylesheet';
        link.href = new URL(ADSENSE_STYLE_PATH, document.baseURI).href;
        link.crossOrigin = 'anonymous';
        document.head.appendChild(link);
    }

    function createAdContainer() {
        var container = document.createElement('div');
        container.className = 'adsense-container is-loading';

        var adIns = document.createElement('ins');
        adIns.className = 'adsbygoogle';
        adIns.style.display = 'block';
        adIns.setAttribute('data-ad-client', AD_CLIENT);
        adIns.setAttribute('data-ad-slot', AD_SLOT);
        adIns.setAttribute('data-ad-format', 'auto');
        adIns.setAttribute('data-full-width-responsive', 'true');

        container.appendChild(adIns);
        return container;
    }

    function removeExistingAds() {
        var containers = document.querySelectorAll('.md-content__inner .adsense-container');
        Array.prototype.forEach.call(containers, function (node) {
            node.classList.add('is-hidden');
        });
    }

    function injectAd() {
        if (isHomePage()) {
            removeExistingAds();
            return;
        }

        ensureAdsenseStyles();

        var articleContent = document.querySelector('.md-content__inner');
        if (!articleContent) {
            return;
        }

        var container = articleContent.querySelector('.adsense-container');
        if (!container) {
            container = createAdContainer();
            articleContent.appendChild(container);
        } else {
            container.classList.remove('is-hidden');
        }

        ensureAdsenseScript(function () {
            renderAd(container);
        });
    }

    function ensureAdsenseScript(callback) {
        if (window.adsbygoogle && typeof window.adsbygoogle.push === 'function') {
            callback();
            return;
        }

        var existingScript = document.getElementById('adsense-loader') || document.querySelector(ADSENSE_SCRIPT_SELECTOR);
        if (existingScript) {
            existingScript.addEventListener('load', callback, { once: true });
            return;
        }

        var script = document.createElement('script');
        script.id = 'adsense-loader';
        script.async = true;
        script.crossOrigin = 'anonymous';
        script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' + encodeURIComponent(AD_CLIENT);
        script.defer = true;
        script.addEventListener('load', callback, { once: true });
        script.addEventListener('error', function () {
            console.error('[AdSense] Failed to load Google AdSense library.');
        });
        document.head.appendChild(script);
    }

    function renderAd(container) {
        if (!container) {
            return;
        }
        container.classList.remove('is-hidden');
        container.classList.add('is-loading');
        container.classList.remove('is-loaded');

        try {
            (window.adsbygoogle = window.adsbygoogle || []).push({});
            container.classList.remove('is-loading');
            container.classList.add('is-loaded');
        } catch (error) {
            container.classList.add('is-hidden');
            container.classList.remove('is-loading');
            console.error('[AdSense] Failed to render ad:', error);
        }
    }

    function onPageReady() {
        window.requestAnimationFrame(injectAd);
    }

    document.addEventListener('DOMContentLoaded', onPageReady);

    if (window.document$ && typeof window.document$.subscribe === 'function') {
        window.document$.subscribe(onPageReady);
    }
})();