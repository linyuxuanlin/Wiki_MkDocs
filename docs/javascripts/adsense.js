// Simplified AdSense insertion script
(function() {
    'use strict';

    var AD_CLIENT = 'ca-pub-4776987651904746';
    var AD_SLOT = window.ADSENSE_SLOT_ID || window.ADSENSE_SLOT || '7746286479';
    var HOME_PATHS = new Set(['/', '/zh/', '/en/', '/es/', '/ar/']);
    var HOME_TITLES = new Set(['Home', "Power's Wiki"]);
    var ADSENSE_SCRIPT_SELECTOR = 'script[src*="pagead/js/adsbygoogle.js"]';

    if (!AD_SLOT) {
        console.warn('[AdSense] Missing data-ad-slot id. Set window.ADSENSE_SLOT_ID before this script runs.');
        return;
    }

    document.addEventListener('DOMContentLoaded', function() {
        if (isHomePage()) {
            return;
        }

        var articleContent = document.querySelector('.md-content__inner');
        if (!articleContent) {
            return;
        }

        if (articleContent.querySelector('.adsense-container')) {
            pushAds();
            return;
        }

        var adContainer = document.createElement('div');
        adContainer.className = 'adsense-container';

        var adIns = document.createElement('ins');
        adIns.className = 'adsbygoogle';
        adIns.style.display = 'block';
        adIns.setAttribute('data-ad-client', AD_CLIENT);
        adIns.setAttribute('data-ad-slot', AD_SLOT);
        adIns.setAttribute('data-ad-format', 'auto');
        adIns.setAttribute('data-full-width-responsive', 'true');

        adContainer.appendChild(adIns);
        articleContent.appendChild(adContainer);

        ensureAdsenseScript(pushAds);
    });

    function isHomePage() {
        var path = window.location.pathname;
        if (HOME_PATHS.has(path)) {
            return true;
        }
        return HOME_TITLES.has(document.title);
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
        script.addEventListener('load', callback, { once: true });
        script.addEventListener('error', function() {
            console.error('[AdSense] Failed to load Google AdSense library.');
        });
        document.head.appendChild(script);
    }

    function pushAds() {
        try {
            (window.adsbygoogle = window.adsbygoogle || []).push({});
        } catch (error) {
            console.error('[AdSense] Failed to render ad:', error);
        }
    }
})();
