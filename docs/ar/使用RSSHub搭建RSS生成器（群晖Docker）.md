# استخدام RSSHub لإنشاء مولد RSS (Docker Synology)

تثبيت خدمة RSSHub على Docker Synology لإنشاء مصادر اشتراك RSS لجميع أنواع المحتويات الغريبة والعجيبة.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504105215.png)

## تثبيت على Docker Synology

افتح حزمة Docker Synology وقم بتنزيل صورة `diygod/rsshub` ، ثم انقر نقرًا مزدوجًا للتشغيل وحدد "تمكين إعادة التشغيل التلقائي" ، ثم انتقل إلى "الإعدادات المتقدمة".

في صفحة "إعدادات المنفذ" ، قم بتعيين المنفذ المحلي الذي يتوافق مع منفذ الحاوية 1200 يدويًا (على سبيل المثال ، قمت بتعيينه على "8004"):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504085806.png)

ثم اكمل الإعدادات وابدأ تشغيل الحاوية. إذا كنت تستطيع رؤية صفحة RSSHub على عنوان IP المحلي لـ Synology والمنفذ 8004 ، فقد نجحت في التثبيت.

## خطوات الاستخدام

يرجى الرجوع إلى [**المستندات الرسمية لـ RSSHub**](https://docs.rsshub.app/) للحصول على تفاصيل الاستخدام.

على سبيل المثال ، يمكن العثور على طريقة إنشاء مصدر RSS لـ "الأفلام الجارية" على موقع Douban في المستندات الرسمية كما هو موضح أدناه:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210504104630.png)

بالتالي ، يمكن استخدام `yourdomain/douban/movie/playing` لإنشاء مصدر RSS الخاص بك باستخدام خادمك الخاص.

يوصى باستخدام الوكيل العكسي المدمج في نظام Synology لتحقيق الوصول المشفر HTTPS. يمكن الرجوع إلى المقالة [**استخدام الوكيل العكسي المدمج في Synology للوصول إلى HTTPS**](https://wiki-power.com/ar/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE) للحصول على تفاصيل الإعداد.

## استخدام RSSHub Radar للكشف التلقائي عن المسارات

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) هو إضافة متصفح يمكنها مساعدتك في العثور والاشتراك بسرعة في RSS و RSSHub الحاليين.

يمكن استخدامه بعد إدخال عنوان مخصص في صفحة الإعدادات.

## المراجع والشكر

- [المستندات الرسمية لـ RSSHub](https://docs.rsshub.app/)
- [تثبيت RSSHub على Synology باستخدام Docker](https://immwind.com/use-docker-install-rsshub-in-synology)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.