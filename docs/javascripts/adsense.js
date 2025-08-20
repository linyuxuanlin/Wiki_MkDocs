// AdSense广告插入脚本
(function() {
    'use strict';
    
    // 等待DOM加载完成
    document.addEventListener('DOMContentLoaded', function() {
        // 检查是否为首页（通过URL路径或页面标题判断）
        const isHomePage = window.location.pathname === '/' || 
                          window.location.pathname === '/zh/' || 
                          window.location.pathname === '/en/' ||
                          window.location.pathname === '/es/' ||
                          window.location.pathname === '/ar/' ||
                          document.title === 'Home' ||
                          document.title === 'Power\'s Wiki';
        
        // 如果不是首页，则插入广告
        if (!isHomePage) {
            // 延迟插入广告，确保页面完全加载
            setTimeout(insertAdsenseAd, 1000);
        }
    });
    
    function insertAdsenseAd() {
        // 查找文章内容区域
        const articleContent = document.querySelector('.md-content__inner');
        
        if (articleContent) {
            // 检查是否已经插入了广告
            if (articleContent.querySelector('.adsense-container')) {
                return;
            }
            
            // 创建广告容器
            const adContainer = document.createElement('div');
            adContainer.className = 'adsense-container';
            adContainer.innerHTML = `
                <div class="adsense-ad" id="adsense-ad">
                    <div class="adsense-label">广告</div>
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-client="ca-pub-3052781953929851"
                         data-ad-slot="auto"
                         data-ad-format="auto"
                         data-full-width-responsive="true"></ins>
                </div>
            `;
            
            // 在文章末尾插入广告
            articleContent.appendChild(adContainer);
            
            // 加载AdSense广告
            loadAdsenseAd();
        }
    }
    
    function loadAdsenseAd() {
        // 检查AdSense是否已加载
        if (typeof adsbygoogle === 'undefined') {
            // 如果AdSense未加载，创建script标签
            const script = document.createElement('script');
            script.src = 'https://pagead2.googlesyndication.com/pagead/js/adsbygoogle.js';
            script.async = true;
            script.crossOrigin = 'anonymous';
            
            script.onload = function() {
                // AdSense加载完成后，初始化广告
                initAdsenseAd();
            };
            
            script.onerror = function() {
                // 加载失败时的处理
                handleAdsenseError();
            };
            
            document.head.appendChild(script);
        } else {
            // AdSense已加载，直接初始化
            initAdsenseAd();
        }
    }
    
    function initAdsenseAd() {
        try {
            // 初始化AdSense广告
            (adsbygoogle = window.adsbygoogle || []).push({});
            
            // 监听广告加载状态
            const adElement = document.querySelector('.adsense-ad ins.adsbygoogle');
            if (adElement) {
                // 添加加载完成的类
                setTimeout(() => {
                    const adContainer = document.querySelector('.adsense-ad');
                    if (adContainer) {
                        adContainer.classList.add('ads-loaded');
                    }
                }, 2000);
            }
        } catch (error) {
            console.warn('AdSense初始化失败:', error);
            handleAdsenseError();
        }
    }
    
    function handleAdsenseError() {
        // 广告加载失败时的处理
        const adContainer = document.querySelector('.adsense-ad');
        if (adContainer) {
            adContainer.classList.add('error');
            adContainer.innerHTML = `
                <div class="adsense-label">广告</div>
                <div style="padding: 2rem; text-align: center; color: var(--md-default-fg-color--light);">
                    <p>广告加载中...</p>
                    <small>如果广告无法显示，请刷新页面或稍后再试</small>
                </div>
            `;
        }
    }
    
    // 页面可见性变化时重新加载广告
    document.addEventListener('visibilitychange', function() {
        if (!document.hidden) {
            // 页面变为可见时，检查广告是否需要重新加载
            const adContainer = document.querySelector('.adsense-container');
            if (adContainer && !adContainer.querySelector('ins.adsbygoogle iframe')) {
                // 如果广告没有正确加载，重新初始化
                setTimeout(loadAdsenseAd, 1000);
            }
        }
    });
})();
