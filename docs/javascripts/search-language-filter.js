// Locale-aware search result filter for MkDocs Material
(function () {
    'use strict';

    var SUPPORTED_LOCALES = ['zh', 'en', 'es', 'ar'];
    var DEFAULT_LOCALE = 'zh';
    var LOCALE_PREFIXES = {
        zh: ['/', '/zh/'],
        en: ['/en/'],
        es: ['/es/'],
        ar: ['/ar/']
    };

    var listObserver = null;

    function getCurrentLocale() {
        var htmlLang = (document.documentElement.getAttribute('lang') || '').trim().toLowerCase();
        if (SUPPORTED_LOCALES.indexOf(htmlLang) !== -1) {
            return htmlLang;
        }
        var pathMatch = window.location.pathname.match(/^\/(zh|en|es|ar)\//);
        if (pathMatch) {
            return pathMatch[1];
        }
        return DEFAULT_LOCALE;
    }

    function startsWithAny(pathname, prefixes) {
        for (var i = 0; i < prefixes.length; i += 1) {
            var prefix = prefixes[i];
            if (prefix && pathname.indexOf(prefix) === 0) {
                return true;
            }
        }
        return false;
    }

    function isAllowedPath(locale, pathname) {
        var prefixes = LOCALE_PREFIXES[locale] || ['/' + locale + '/'];
        var otherPrefixes = SUPPORTED_LOCALES.filter(function (code) {
            return code !== locale;
        }).map(function (code) {
            return '/' + code + '/';
        });

        for (var i = 0; i < prefixes.length; i += 1) {
            var prefix = prefixes[i];
            if (!prefix) {
                continue;
            }
            if (prefix === '/' && locale === DEFAULT_LOCALE) {
                if (pathname === '/' || !startsWithAny(pathname, otherPrefixes)) {
                    return true;
                }
            } else if (pathname === prefix || pathname.indexOf(prefix) === 0) {
                return true;
            }
        }
        return false;
    }

    function filterSearchResults() {
        var locale = getCurrentLocale();
        var links = document.querySelectorAll('.md-search-result__link[href]');
        if (!links.length) {
            return;
        }

        Array.prototype.forEach.call(links, function (link) {
            var href = link.getAttribute('href');
            if (!href) {
                return;
            }
            var resolved;
            try {
                resolved = new URL(href, window.location.origin);
            } catch (error) {
                return;
            }
            var pathname = resolved.pathname;
            var listItem = link.closest('.md-search-result__item') || link.parentElement;
            if (!listItem) {
                return;
            }

            if (isAllowedPath(locale, pathname)) {
                listItem.style.display = '';
                listItem.removeAttribute('aria-hidden');
                listItem.classList.remove('is-filtered-out');
            } else {
                listItem.style.display = 'none';
                listItem.setAttribute('aria-hidden', 'true');
                listItem.classList.add('is-filtered-out');
            }
        });
    }

    function attachObserverToList(list) {
        if (listObserver) {
            listObserver.disconnect();
        }
        listObserver = new MutationObserver(filterSearchResults);
        listObserver.observe(list, { childList: true });
        filterSearchResults();
    }

    function watchForResultList() {
        var list = document.querySelector('.md-search-result__list');
        if (!list) {
            return false;
        }
        attachObserverToList(list);
        return true;
    }

    function initialise() {
        if (watchForResultList()) {
            return;
        }
        var attempts = 0;
        var maxAttempts = 40;
        var timer = window.setInterval(function () {
            attempts += 1;
            if (watchForResultList() || attempts >= maxAttempts) {
                window.clearInterval(timer);
            }
        }, 250);
    }

    document.addEventListener('DOMContentLoaded', function () {
        initialise();
    });

    if (window.document$ && typeof window.document$.subscribe === 'function') {
        window.document$.subscribe(function () {
            initialise();
        });
    }

    document.addEventListener('input', function (event) {
        var target = event.target;
        if (target && target.getAttribute('data-md-component') === 'search-query') {
            window.requestAnimationFrame(filterSearchResults);
        }
    });
})();
