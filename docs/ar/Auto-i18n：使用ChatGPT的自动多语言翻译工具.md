# Auto-i18n: أداة ترجمة تلقائية للعديد من اللغات باستخدام ChatGPT

Auto-i18n هي أداة تستخدم ChatGPT لترجمة ملفات Markdown بشكل تلقائي إلى العديد من اللغات.

تم تحقيق ترجمة المقالات الدولية بشكل كامل. يمكنك ببساطة دفع المقالة إلى مستودع GitHub واستخدام GitHub Actions لترجمتها تلقائيًا إلى العديد من اللغات. (يدعم الإنجليزية والإسبانية والعربية حاليًا ، وسيتم توفير دعم للغات أخرى في المستقبل)

**عنوان المشروع**: [**linyuxuanlin/Auto-i18n**](https://github.com/linyuxuanlin/Auto-i18n)

نتيجة تطبيق i18n على مدونتي:

![](https://img.wiki-power.com/d/wiki-media/img/202310151317234.png)

## البدء السريع

1. أولاً ، انسخ المستودع إلى جهاز الكمبيوتر الخاص بك.
2. قم بإعادة تسمية `env_template.py` إلى `env.py` واملأ معلومات API الخاصة بـ ChatGPT. يمكنك الحصول على مفتاح API مجاني من مشروع [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free).
3. تشغيل `pip install openai` لتثبيت التبعيات اللازمة.
4. تشغيل برنامج `auto-translater` ، وسيتم ترجمة جميع ملفات Markdown في دليل الاختبار `testdir/to-translate` تلقائيًا إلى الإنجليزية والإسبانية والعربية.

## الوصف التفصيلي

يتم تشغيل برنامج `auto-translater.py` بمنطق التشغيل التالي:

1. سيتم ترجمة جميع ملفات Markdown في دليل الاختبار `testdir/to-translate` تلقائيًا. يمكنك استبعاد الملفات التي لا تحتاج إلى الترجمة في متغير `exclude_list`.
2. سيتم تسجيل اسم الملف المعالج في `processed_list.txt` الذي يتم إنشاؤه تلقائيًا. عند تشغيل البرنامج في المرة القادمة ، لن يتم ترجمة الملفات التي تم معالجتها بالفعل.
3. بالنسبة للمقالات التي كتبت باللغة الإنجليزية ، لن يتم ترجمتها مرة أخرى إلى اللغة الإنجليزية ، ولن يتم ترجمتها إلى الصينية ، وسيتم ترجمتها إلى لغات أخرى. يجب عليك إضافة الحقل `> This post was originally written in English.` (لاحظ ترك سطر فارغ في الأعلى والأسفل) في المقالة لتعريف البرنامج. يرجى الرجوع إلى [مقالة الاختبار\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md).
4. إذا كنت بحاجة إلى إعادة ترجمة مقالة معينة (على سبيل المثال ، إذا كانت نتائج الترجمة غير دقيقة أو تغير محتوى المقالة إلخ) ، فيمكنك إضافة الحقل `[translate]` في المقالة (يجب ترك سطر فارغ في الأعلى والأسفل). سيتم تجاهل قواعد `exclude_list` و `processed_list` ، وسيتم إجبار المعالجة على الترجمة. يرجى الرجوع إلى [مقالة الاختبار\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md).

## دليل GitHub Actions التلقائي

يمكنك إنشاء `.github/workflows/ci.yml` في مستودع المشروع الخاص بك. عند الكشف عن تحديث في مستودع GitHub ، يمكن استخدام GitHub Actions لترجمتها تلقائيًا إلى العديد من اللغات وإعادة الالتزام بالمستودع الأصلي.

يمكن الاطلاع على محتوى `ci.yml` في القالب: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

يجب إضافة مفتاحين سريين: `CHATGPT_API_BASE` و `CHATGPT_API_KEY` في `Settings` - `Secrets and variables` - `Repository secrets` في المستودع الخاص بك ، وتعليق عبارة `import env` في برنامج `auto-translater.py`.

## تصحيح الأخطاء

1. إذا كنت ترغب في التحقق من صلاحية مفتاح API ChatGPT ، فيمكنك الاطلاع على البرنامج [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py).
2. عند استخدام GitHub Actions وواجهت مشكلة ، يرجى التحقق أولاً من صحة مسار الإشارة (على سبيل المثال `dir_to_translate` `dir_translated_en` `dir_translated_es` `dir_translated_ar` `processed_list`).

## المشاكل التي يجب حلها

1. إذا كان ملف Markdown يحتوي على Front Matter ، فقد يتم معالجته أيضًا للترجمة ويتسبب في مشكلة. طريقتي للتعامل مع هذه المشكلة هي عدم استخدام Front Matter ، واستخدام العنوان الرئيسي كعنوان للمقالة.
2. إذا كان المقال غير كامل ، فقد يتم ترجمته بواسطة ChatGPT واستكماله تلقائيًا (غامض).
3. في بعض الحالات الخاصة ، قد يحدث عدم دقة في الترجمة أو عدم ترجمة بعض الحقول ، وبعد الترجمة يتعين التحقق والتعديل اليدوي.

## المساهمة

نرحب بمشاركتك في تحسين هذا المشروع! إذا كنت ترغب في المساهمة بالشفرة أو تقديم تقرير عن مشكلة أو اقتراح ، يرجى الاطلاع على [دليل المساهمة](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## حقوق النشر والترخيص

يتم تطبيق [رخصة MIT](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE) على هذا المشروع.

## المشاكل والدعم

إذا واجهت أي مشكلة أثناء استخدام Auto-i18n ، أو إذا كنت بحاجة إلى الدعم الفني ، يرجى [تقديم طلب](https://github.com/linyuxuanlin/Auto-i18n/issues).

## المراجع والشكر

نشكر [**chatanywhere/GPT_API_free**](https://github.com/chatanywhere/GPT_API_free) على توفير مفتاح API ChatGPT المجاني.

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.