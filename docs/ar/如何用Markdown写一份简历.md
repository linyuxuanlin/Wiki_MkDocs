# كيفية كتابة سيرة ذاتية باستخدام Markdown

![](https://media.wiki-power.com/img/20210318220041.png)

استخدم Markdown لكتابة سيرة ذاتية يمكن معاينتها عبر الإنترنت وتصديرها كملف PDF.

**رابط المعاينة**: [**cv-template.wiki-power.com**](https://cv-template.wiki-power.com/)

**كيفية تصدير كملف PDF**: استخدم اختصار لوحة المفاتيح `Ctrl` + `P` لفتح واجهة الطباعة على الصفحة، ثم حدد `Microsoft Print to PDF` كطابعة الهدف لتصدير السيرة الذاتية كملف PDF.

## طريقة الاستخدام

افتح المشروع [**linyuxuanlin/Markdown-CV-Site**](https://github.com/linyuxuanlin/Markdown-CV-Site) وانقر على الزر الأخضر "استخدم هذا القالب" لإنشاء مستودع خاص بك.

افتح [**Vercel**](https://vercel.com/) وانقر على "مشروع جديد" ، ثم استورد مستودع GitHub الذي تم إنشاؤه للتو وقم بتعيين المعلمات التالية:

- `FRAMEWORK PRESET`: اختر `Other`
- `BUILD COMMAND`: أدخل `npm run build`
- `OUTPUT DIRECTORY`: أدخل `dist`

انقر على الخطوة التالية وانتظر بضع ثوانٍ ، وسيتم إنشاء الموقع.

إذا كنت ترغب في تعديل محتوى السيرة الذاتية ، يرجى تحرير الملفات `_config.yml` و `markdown/resume-template.md` في الدليل الرئيسي ، وبعد الدفع إلى مستودع GitHub ، ستتم مباشرةً عملية البناء في Vercel.

## المراجع والشكر

يستند هذا المشروع إلى [**BigLiao/markCV**](https://github.com/BigLiao/markCV) ، وقد تم إجراء بعض التبسيط والتحسينات على واجهة المستخدم. تم استخدام قالب السيرة الذاتية من [**لانغ زي**](https://cv.ftqq.com/) كمحتوى افتراضي.

- [كيفية كتابة سيرة ذاتية؟](https://mp.weixin.qq.com/s/P64bm-SBYXyQymfHAR1rqA)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
