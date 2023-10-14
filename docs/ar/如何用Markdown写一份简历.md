# كيفية كتابة سيرة ذاتية باستخدام Markdown

![](https://img.wiki-power.com/d/wiki-media/img/20210318220041.png)

استخدم Markdown لكتابة سيرة ذاتية يمكن معاينتها عبر الإنترنت وتصديرها إلى PDF.

**رابط المعاينة**: [**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**كيفية تصدير إلى PDF**: استخدم اختصارات لوحة المفاتيح `Ctrl` + `P` لفتح واجهة الطباعة على الموقع، ثم حدد `Microsoft Print to PDF` كطابعة هدف لتصدير السيرة الذاتية إلى PDF.

## طريقة الاستخدام

افتح المشروع [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site)، ثم انقر على الزر الأخضر `Use this template` لإنشاء مستودع خاص بك.

افتح [**Vercel**](https://vercel.com/)، ثم انقر على `New Project` واستورد المستودع الذي أنشأته في GitHub، وحدد الإعدادات التالية:

- `FRAMEWORK PRESET`: اختر `Other`
- `BUILD COMMAND`: اكتب `npm run build`
- `OUTPUT DIRECTORY`: اكتب `dist`

انقر على الخطوة التالية، وانتظر بضع ثوانٍ حتى يتم إنشاء الموقع.

إذا كنت ترغب في تعديل محتوى السيرة الذاتية، فعليك تحرير الملفات `_config.yml` و `markdown/resume-template.md` في الدليل الرئيسي، ثم تحميل التغييرات إلى مستودع GitHub الخاص بك، وسيتم تشغيل بناء Vercel تلقائيًا.

## المراجع والشكر

يستند هذا المشروع إلى [**BigLiao/markCV**](https://github.com/BigLiao/markCV)، وقد تم تبسيط وتحسين بعض عناصر واجهة المستخدم. تم استخدام قالب السيرة الذاتية الافتراضي من [**لينغ زينغ سيرة ذاتية**](https://cv.ftqq.com/).

- [كيفية كتابة سيرة ذاتية؟](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.