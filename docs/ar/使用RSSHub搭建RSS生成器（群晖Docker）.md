```markdown
# إنشاء مُنتج RSS باستخدام RSSHub (Docker على Synology)

قم بإعداد خدمة RSSHub على Synology Docker لإنشاء مصادر الاشتراك بالـ RSS لأنواع متنوعة من المحتوى الغريب.

![صورة](https://media.wiki-power.com/img/20210504105215.png)

## نصبه على Synology Docker

افتح حزمة Docker على Synology، قم بتنزيل صورة `diygod/rsshub`، ثم قم بالنقر نقرًا مزدوجًا لبدء التشغيل. حدد "تمكين إعادة التشغيل التلقائي" وانتقل إلى "إعدادات متقدمة".

في صفحة "إعدادات المنفذ"، قم بتعيين يدوياً منفذ الحاوية المقابل لمنفذ 1200 (على سبيل المثال، قمت بتعيينه كـ `8004`):

![صورة](https://media.wiki-power.com/img/20210504085806.png)

بعد ذلك، أكمل الإعدادات وابدأ تشغيل الحاوية. إذا تمكنت من رؤية صفحة RSSHub عبر عنوان IP المحلي لـ Synology على المنفذ 8004، فذلك يعني أن التثبيت تم بنجاح.

## خطوات الاستخدام

لمزيد من التفاصيل حول كيفية الاستخدام، يرجى الرجوع إلى [**وثائق RSSHub الرسمية**](https://docs.rsshub.app/)

على سبيل المثال البسيط، يمكنك العثور على كيفية إنشاء مصدر RSS لـ "أفلام يعرضها دور السينما" من خلال موقع دوبان في وثائق الرسمية:

![صورة](https://media.wiki-power.com/img/20210504104630.png)

بذلك، يمكنك استخدام خادمك الخاص من خلال الرابط `نطاقك/douban/movie/playing`.

ننصح باستخدام خدمة البروكسي العكسي المدمجة في نظام Synology لتمكين الوصول بواسطة HTTPS. يمكنك الرجوع إلى المقالة [**استخدام البروكسي العكسي المدمج في Synology للوصول عبر HTTPS**](https://wiki-power.com/%E7%94%A8%E7%BE%A4%E6%99%96%E8%87%AA%E5%B8%A6%E5%8F%8D%E5%90%91%E4%BB%A3%E7%90%86%E5%AE%9E%E7%8E%B0HTTPS%E8%AE%BF%E9%97%AE) لمزيد من التفاصيل.

## استخدام مُنتج RSSHub Radar للكشف التلقائي عن المسارات

[**RSSHub Radar**](https://github.com/DIYgod/RSSHub-Radar) هو امتداد متصفح يساعدك على اكتشاف والاشتراك بسرعة في مصادر RSS الحالية وموقع RSSHub.

ما عليك سوى إدخال العنوان المخصص في صفحة الإعدادات.

## المراجع والشكر

- [وثائق RSSHub الرسمية](https://docs.rsshub.app/)
- [تثبيت RSSHub على Synology باستخدام Docker](https://immwind.com/use-docker-install-rsshub-in-synology)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
