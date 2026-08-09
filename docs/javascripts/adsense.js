// AdSense placement and loader for content pages.
(function () {
    'use strict';

    var AD_CLIENT = 'ca-pub-4776987651904746';
    var AD_SLOT = window.ADSENSE_SLOT_ID || window.ADSENSE_SLOT || '7746286479';
    var HOME_PATHS = new Set(['/', '/zh/', '/en/', '/es/', '/ar/']);
    var ADSENSE_SCRIPT_SELECTOR = 'script[src*="pagead/js/adsbygoogle.js"]';
    var MIN_TEXT_LENGTH = 800;
    var LONG_ARTICLE_TEXT_LENGTH = 2600;
    var lastInitializedUrl = '';

    if (!AD_SLOT) {
        console.warn('[AdSense] Missing data-ad-slot id.');
        return;
    }

    onReady(initAds);

    // Also works if Material instant navigation is enabled in the future.
    if (window.document$ && typeof window.document$.subscribe === 'function') {
        window.document$.subscribe(initAds);
    }

    function onReady(callback) {
        if (document.readyState === 'loading') {
            document.addEventListener('DOMContentLoaded', callback, { once: true });
        } else {
            callback();
        }
    }

    function initAds() {
        if (shouldSkipPage()) {
            return;
        }

        var article = document.querySelector('.md-content__inner');
        if (!article) {
            return;
        }

        var currentUrl = window.location.href;
        if (lastInitializedUrl === currentUrl && article.querySelector('.adsense-container')) {
            return;
        }

        // Avoid monetizing very short / low-value pages.
        var textLength = (article.innerText || article.textContent || '')
            .replace(/\s+/g, ' ')
            .trim().length;
        if (textLength < MIN_TEXT_LENGTH) {
            return;
        }

        article.querySelectorAll('.adsense-container').forEach(function (element) {
            element.remove();
        });

        var adUnits = [];

        if (textLength >= LONG_ARTICLE_TEXT_LENGTH) {
            var midpoint = findMidpointTarget(article);
            if (midpoint) {
                var midAd = createAdUnit('mid');
                midpoint.insertAdjacentElement('afterend', midAd.container);
                adUnits.push(midAd);
            }
        }

        var endAd = createAdUnit('end');
        article.appendChild(endAd.container);
        adUnits.push(endAd);
        lastInitializedUrl = currentUrl;

        ensureAdsenseScript(function () {
            adUnits.forEach(renderAd);
        }, function () {
            adUnits.forEach(function (unit) {
                unit.container.remove();
            });
        });
    }

    function shouldSkipPage() {
        var path = window.location.pathname;
        var title = document.title || '';
        var robots = document.querySelector('meta[name="robots"]');
        var robotsContent = robots ? (robots.getAttribute('content') || '').toLowerCase() : '';

        return HOME_PATHS.has(path) ||
            path === '/404.html' ||
            /(^|\s)404(\s|$)/.test(title) ||
            /(^|,)\s*noindex\s*(,|$)/.test(robotsContent) ||
            hasDifferentCanonical();
    }

    function hasDifferentCanonical() {
        var canonicalLink = document.querySelector('link[rel="canonical"]');
        if (!canonicalLink || !canonicalLink.getAttribute('href')) {
            return false;
        }

        try {
            var canonical = new URL(canonicalLink.getAttribute('href'), window.location.href);
            var current = new URL(window.location.href);

            return canonical.origin !== current.origin ||
                normalizePath(canonical.pathname) !== normalizePath(current.pathname);
        } catch (error) {
            return false;
        }
    }

    function normalizePath(path) {
        if (!path || path === '/') {
            return '/';
        }
        return path.replace(/\/+$/, '');
    }

    function findMidpointTarget(article) {
        var candidates = Array.prototype.filter.call(article.children, function (element) {
            if (!/^(P|UL|OL|PRE|TABLE|BLOCKQUOTE|DIV)$/.test(element.tagName)) {
                return false;
            }

            var text = (element.innerText || element.textContent || '').trim();
            return text.length >= 80 && !element.closest('.adsense-container');
        });

        if (candidates.length < 6) {
            return null;
        }

        return candidates[Math.floor(candidates.length * 0.55)];
    }

    function createAdUnit(position) {
        var container = document.createElement('div');
        container.className = 'adsense-container adsense-container--' + position;
        container.setAttribute('aria-label', 'Advertisement');
        container.setAttribute('data-adsense-position', position);

        var ad = document.createElement('ins');
        ad.className = 'adsbygoogle';
        ad.style.display = 'block';
        ad.setAttribute('data-ad-client', AD_CLIENT);
        ad.setAttribute('data-ad-slot', AD_SLOT);
        ad.setAttribute('data-ad-format', 'auto');
        ad.setAttribute('data-full-width-responsive', 'true');

        observeAdStatus(ad, container);
        container.appendChild(ad);

        return { container: container, ad: ad };
    }

    function observeAdStatus(ad, container) {
        if (typeof MutationObserver !== 'function') {
            return;
        }

        var observer = new MutationObserver(function () {
            var status = ad.getAttribute('data-ad-status');
            container.classList.toggle('is-unfilled', status === 'unfilled');

            if (status === 'filled' || status === 'unfilled') {
                observer.disconnect();
            }
        });

        observer.observe(ad, { attributes: true, attributeFilter: ['data-ad-status'] });
    }

    function ensureAdsenseScript(onLoad, onError) {
        if (window.adsbygoogle && typeof window.adsbygoogle.push === 'function') {
            onLoad();
            return;
        }

        var existingScript = document.getElementById('adsense-loader') ||
            document.querySelector(ADSENSE_SCRIPT_SELECTOR);

        if (existingScript) {
            existingScript.addEventListener('load', onLoad, { once: true });
            existingScript.addEventListener('error', onError, { once: true });
            return;
        }

        var script = document.createElement('script');
        script.id = 'adsense-loader';
        script.async = true;
        script.crossOrigin = 'anonymous';
        script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js?client=' +
            encodeURIComponent(AD_CLIENT);
        script.addEventListener('load', onLoad, { once: true });
        script.addEventListener('error', onError, { once: true });
        document.head.appendChild(script);
    }

    function renderAd(unit) {
        if (unit.ad.getAttribute('data-adsbygoogle-status')) {
            return;
        }

        try {
            (window.adsbygoogle = window.adsbygoogle || []).push({});
        } catch (error) {
            unit.container.remove();
            console.error('[AdSense] Failed to render ad:', error);
        }
    }
})();
