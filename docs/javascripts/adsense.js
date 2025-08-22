// AdSense广告插入脚本 - 优化版本
(function() {
    'use strict';
    
    let adContainer = null;
    let loadTimeout = null;
    let checkTimeout = null;
    
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
            adContainer = document.createElement('div');
            adContainer.className = 'adsense-container hidden'; // 初始时隐藏
            adContainer.innerHTML = `
                <div class="adsense-ad" id="adsense-ad">
                    <ins class="adsbygoogle"
                         style="display:block"
                         data-ad-client="ca-pub-2699191587499841"
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
                // 加载失败时，立即隐藏广告容器
                hideAdContainer();
            };
            
            // 设置加载超时 - 统一为3秒
            loadTimeout = setTimeout(function() {
                if (typeof adsbygoogle === 'undefined') {
                    hideAdContainer();
                }
            }, 3000);
            
            document.head.appendChild(script);
        } else {
            // AdSense已加载，直接初始化
            initAdsenseAd();
        }
    }
    
    function initAdsenseAd() {
        try {
            // 显示广告容器
            if (adContainer) {
                adContainer.classList.remove('hidden');
                adContainer.classList.add('loading');
            }
            
            // 初始化AdSense广告
            (adsbygoogle = window.adsbygoogle || []).push({});
            
            // 设置超时检查 - 统一为3秒
            checkTimeout = setTimeout(function() {
                const adElement = document.querySelector('.adsense-ad ins.adsbygoogle iframe');
                if (!adElement) {
                    hideAdContainer();
                } else {
                    // 广告加载成功，检查iframe内容
                    checkIframeContent(adElement);
                }
            }, 3000);
            
        } catch (error) {
            console.warn('AdSense初始化失败:', error);
            hideAdContainer();
        }
    }
    
    function checkIframeContent(iframe) {
        try {
            // 等待iframe加载完成
            iframe.onload = function() {
                try {
                    const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
                    const iframeBody = iframeDoc.body;
                    
                    if (iframeBody) {
                        // 检查iframe body是否有内容
                        const hasContent = iframeBody.children.length > 0 || 
                                         iframeBody.textContent.trim().length > 0 ||
                                         iframeBody.innerHTML.includes('adsbygoogle');
                        
                        if (!hasContent) {
                            // iframe没有有效内容，隐藏广告容器
                            hideAdContainer();
                        } else {
                            // 广告加载成功
                            if (adContainer) {
                                adContainer.classList.remove('loading');
                                adContainer.classList.add('loaded');
                            }
                        }
                    }
                } catch (e) {
                    // 跨域限制，无法访问iframe内容
                    // 通过其他方式检查广告是否真的加载了
                    setTimeout(() => {
                        const adRect = iframe.getBoundingClientRect();
                        if (adRect.height < 50 || adRect.width < 50) {
                            // 广告尺寸太小，可能没有真正加载
                            hideAdContainer();
                        } else {
                            // 广告加载成功
                            if (adContainer) {
                                adContainer.classList.remove('loading');
                                adContainer.classList.add('loaded');
                            }
                        }
                    }, 1000);
                }
            };
            
            // 如果iframe已经加载完成
            if (iframe.contentDocument && iframe.contentDocument.readyState === 'complete') {
                iframe.onload();
            }
            
        } catch (error) {
            console.warn('检查iframe内容失败:', error);
            // 如果无法检查iframe内容，使用尺寸检查
            setTimeout(() => {
                const adRect = iframe.getBoundingClientRect();
                if (adRect.height < 50 || adRect.width < 50) {
                    hideAdContainer();
                } else {
                    if (adContainer) {
                        adContainer.classList.remove('loading');
                        adContainer.classList.add('loaded');
                    }
                }
            }, 1000);
        }
    }
    
    function hideAdContainer() {
        // 清除所有超时
        if (loadTimeout) {
            clearTimeout(loadTimeout);
            loadTimeout = null;
        }
        if (checkTimeout) {
            clearTimeout(checkTimeout);
            checkTimeout = null;
        }
        
        // 立即隐藏广告容器
        if (adContainer) {
            // 先尝试隐藏所有相关的iframe
            const iframes = adContainer.querySelectorAll('iframe');
            iframes.forEach(iframe => {
                try {
                    // 设置iframe样式为隐藏
                    iframe.style.cssText = `
                        display: none !important;
                        width: 0 !important;
                        height: 0 !important;
                        border: none !important;
                        margin: 0 !important;
                        padding: 0 !important;
                        overflow: hidden !important;
                        position: absolute !important;
                        left: -9999px !important;
                        top: -9999px !important;
                    `;
                    
                    // 尝试访问iframe内容并隐藏
                    try {
                        const iframeDoc = iframe.contentDocument || iframe.contentWindow.document;
                        if (iframeDoc && iframeDoc.body) {
                            iframeDoc.body.style.cssText = `
                                display: none !important;
                                width: 0 !important;
                                height: 0 !important;
                                margin: 0 !important;
                                padding: 0 !important;
                                overflow: hidden !important;
                                position: absolute !important;
                                left: -9999px !important;
                                top: -9999px !important;
                            `;
                        }
                    } catch (e) {
                        // 跨域限制，无法访问iframe内容
                    }
                } catch (e) {
                    console.warn('隐藏iframe失败:', e);
                }
            });
            
            // 使用内联样式确保立即隐藏
            adContainer.style.cssText = `
                display: none !important;
                margin: 0 !important;
                padding: 0 !important;
                height: 0 !important;
                min-height: 0 !important;
                max-height: 0 !important;
                width: 0 !important;
                min-width: 0 !important;
                max-width: 0 !important;
                overflow: hidden !important;
                opacity: 0 !important;
                visibility: hidden !important;
                position: absolute !important;
                left: -9999px !important;
                top: -9999px !important;
                z-index: -9999 !important;
                pointer-events: none !important;
                user-select: none !important;
                transform: scale(0) !important;
                clip: rect(0, 0, 0, 0) !important;
            `;
            
            // 添加CSS类
            adContainer.classList.add('hidden');
            
            // 强制重排，确保样式生效
            adContainer.offsetHeight;
            
            // 立即移除，不等待延迟
            if (adContainer && adContainer.parentNode) {
                adContainer.remove();
                adContainer = null;
            }
        }
    }
    
    function removeAdContainer() {
        // 移除广告容器
        if (adContainer && adContainer.parentNode) {
            adContainer.remove();
            adContainer = null;
        }
    }
    
    // 页面可见性变化时检查广告状态
    document.addEventListener('visibilitychange', function() {
        if (!document.hidden) {
            // 页面变为可见时，检查广告是否加载成功
            if (adContainer) {
                const adElement = adContainer.querySelector('ins.adsbygoogle iframe');
                if (!adElement) {
                    // 如果广告没有加载成功，立即隐藏容器
                    hideAdContainer();
                } else {
                    // 检查iframe内容
                    checkIframeContent(adElement);
                }
            }
        }
    });
    
    // 页面卸载时清理资源
    window.addEventListener('beforeunload', function() {
        if (loadTimeout) {
            clearTimeout(loadTimeout);
        }
        if (checkTimeout) {
            clearTimeout(checkTimeout);
        }
    });
})();

