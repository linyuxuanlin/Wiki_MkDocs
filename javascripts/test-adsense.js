// AdSense集成测试脚本 - 简化版
(function() {
    'use strict';

    const HOME_PATHS = new Set(['/', '/zh/', '/en/', '/es/', '/ar/']);
    const HOME_TITLES = new Set(['Home', "Power's Wiki"]);
    const DEBUG = Boolean(window.ADSENSE_TEST_DEBUG);

    function debugLog() {
        if (!DEBUG) {
            return;
        }
        console.log.apply(console, arguments);
    }

    debugLog('🔍 AdSense集成测试脚本已加载');

    function testPageDetection() {
        const path = window.location.pathname;
        const title = document.title;
        const isHomePage = HOME_PATHS.has(path) || HOME_TITLES.has(title);
        const detectionPass = !isHomePage;

        debugLog('📍 页面检测结果:', {
            pathname: path,
            title: title,
            isHomePage: isHomePage
        });

        if (detectionPass) {
            debugLog('✅ 当前页面被识别为非主页');
        } else {
            debugLog('❌ 页面被识别为主页，请确认测试URL');
        }

        return detectionPass;
    }

    function testAdInsertion() {
        const articleContent = document.querySelector('.md-content__inner');
        if (articleContent) {
            debugLog('📄 找到文章内容区域:', articleContent);

            const existingAd = articleContent.querySelector('.adsense-container');
            if (existingAd) {
                debugLog('✅ 广告容器已存在');
                return true;
            }

            debugLog('❌ 广告容器不存在');
            return false;
        }

        console.warn('❌ 未找到文章内容区域');
        return false;
    }

    function testStyles() {
        const styleSheets = Array.from(document.styleSheets);
        const adsenseStyle = styleSheets.find(sheet =>
            sheet.href && sheet.href.includes('adsense.css')
        );

        if (adsenseStyle) {
            debugLog('✅ AdSense样式已加载');
            return true;
        }

        console.warn('❌ AdSense样式未加载');
        return false;
    }

    function runTests() {
        debugLog('🧪 开始运行AdSense集成测试...');

        const tests = [
            { name: '页面检测', test: testPageDetection },
            { name: '广告插入', test: testAdInsertion },
            { name: '样式加载', test: testStyles }
        ];

        let passed = 0;
        const total = tests.length;

        tests.forEach(({ name, test }) => {
            try {
                const result = test();
                if (result) {
                    debugLog('✅ ' + name + '测试通过');
                    passed++;
                } else {
                    debugLog('❌ ' + name + '测试失败');
                }
            } catch (error) {
                console.error('❌ ' + name + '测试出错:', error);
            }
        });

        debugLog('📊 测试结果: ' + passed + '/' + total + ' 通过');

        if (passed === total) {
            debugLog('🎉 所有测试通过！AdSense集成正常工作');
        } else {
            debugLog('⚠️ 部分测试失败，请检查配置');
        }
    }

    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', runTests);
    } else {
        runTests();
    }

    window.testAdsenseIntegration = runTests;
})();
