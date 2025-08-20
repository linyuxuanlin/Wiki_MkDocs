// AdSense集成测试脚本 - 简化版本
(function() {
    'use strict';
    
    console.log('🔍 AdSense集成测试脚本已加载');
    
    // 测试页面检测功能
    function testPageDetection() {
        const isHomePage = window.location.pathname === '/' || 
                          window.location.pathname === '/zh/' || 
                          window.location.pathname === '/en/' ||
                          window.location.pathname === '/es/' ||
                          window.location.pathname === '/ar/' ||
                          document.title === 'Home' ||
                          document.title === 'Power\'s Wiki';
        
        console.log('📍 页面检测结果:', {
            pathname: window.location.pathname,
            title: document.title,
            isHomePage: isHomePage
        });
        
        return isHomePage;
    }
    
    // 测试广告插入功能
    function testAdInsertion() {
        const articleContent = document.querySelector('.md-content__inner');
        if (articleContent) {
            console.log('📄 找到文章内容区域:', articleContent);
            
            // 检查是否已有广告
            const existingAd = articleContent.querySelector('.adsense-container');
            if (existingAd) {
                console.log('✅ 广告容器已存在');
                return true;
            } else {
                console.log('❌ 广告容器不存在');
                return false;
            }
        } else {
            console.log('❌ 未找到文章内容区域');
            return false;
        }
    }
    
    // 测试样式加载
    function testStyles() {
        const styleSheets = Array.from(document.styleSheets);
        const adsenseStyle = styleSheets.find(sheet => 
            sheet.href && sheet.href.includes('adsense.css')
        );
        
        if (adsenseStyle) {
            console.log('✅ AdSense样式已加载');
            return true;
        } else {
            console.log('❌ AdSense样式未加载');
            return false;
        }
    }
    
    // 运行所有测试
    function runTests() {
        console.log('🧪 开始运行AdSense集成测试...');
        
        const tests = [
            { name: '页面检测', test: testPageDetection },
            { name: '广告插入', test: testAdInsertion },
            { name: '样式加载', test: testStyles }
        ];
        
        let passed = 0;
        let total = tests.length;
        
        tests.forEach(({ name, test }) => {
            try {
                const result = test();
                if (result !== false) {
                    console.log(`✅ ${name}测试通过`);
                    passed++;
                } else {
                    console.log(`❌ ${name}测试失败`);
                }
            } catch (error) {
                console.error(`❌ ${name}测试出错:`, error);
            }
        });
        
        console.log(`📊 测试结果: ${passed}/${total} 通过`);
        
        if (passed === total) {
            console.log('🎉 所有测试通过！AdSense集成正常工作');
        } else {
            console.log('⚠️ 部分测试失败，请检查配置');
        }
    }
    
    // 等待页面加载完成后运行测试
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', runTests);
    } else {
        runTests();
    }
    
    // 导出测试函数供手动调用
    window.testAdsenseIntegration = runTests;
    
})();
