# Auto-i18n: Using ChatGPT's Automatic Multilingual Translation Tool

Auto-i18n is a tool that leverages ChatGPT to automatically translate Markdown files into multiple languages. It achieves full automation of blog article internationalization (i18n). You only need to push your blog posts to a GitHub repository, and GitHub Actions will take care of automatically translating them into various languages. Currently, it supports English, Spanish, and Arabic, with plans to provide support for more languages in the future.

Key Features of Auto-i18n:

- **Batch Multilingual Translation**: Auto-i18n offers batch translation functionality, allowing you to translate all Markdown documents in an entire directory into multiple languages at once, significantly improving the efficiency of multilingual projects.

- **Front Matter Compatibility**: Auto-i18n is compatible with Markdown Front Matter syntax, enabling you to customize translation or replacement rules for different fields.

- **Fixed Content Replacement**: Auto-i18n also supports fixed content replacement. If you want the translations of certain repetitive fields in your documents to remain consistent, this feature can help you achieve document consistency.

- **Automation Workflow**: You can use GitHub Actions to implement an automated translation process without manual intervention. The translation work will proceed automatically and update your documents, allowing you to focus more on your content.

## Getting Started

1. Clone the repository to your local machine, rename `env_template.py` to `env.py`, and provide your ChatGPT API key. If you don't have your own API key, you can obtain a free one from [GPT_API_free](https://github.com/chatanywhere/GPT_API_free). You can also use [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) to convert the web-based ChatGPT into an API.

2. Install the required modules: `pip install -r requirements.txt`.

3. Run the command `python auto-translater.py` to execute the program. It will automatically process all Markdown files in the test directory `testdir/to-translate` and translate them into English, Spanish, and Arabic. (More language support will be added in the future).

## Detailed Description

The logic of the program `auto-translater.py` is as follows:

1. البرنامج سيتعامل تلقائيًا مع جميع ملفات التسويق الواردة في الدليل `testdir/to-translate`. يمكنك استبعاد الملفات التي لا ترغب في ترجمتها باستخدام متغير `exclude_list`.

2. سيتم تسجيل أسماء الملفات بعد المعالجة في ملف `processed_list.txt` الذي يتم إنشاؤه تلقائيًا. عند تشغيل البرنامج في المرة التالية، لن يتم ترجمة الملفات التي تم معالجتها بالفعل.

3. بالنسبة للمقالات التي كتبت أصلاً باللغة الإنجليزية، لن يتم ترجمتها مرة أخرى إلى الإنجليزية، ولن يتم ترجمتها أيضًا إلى اللغة الصينية، بل سيتم ترجمتها إلى لغة أخرى. يجب عليك إضافة النص التالي في المقالة: `> This post was originally written in English.` (يرجى ترك سطر فارغ أعلى وأسفل النص) لكي يتم التعرف عليها بواسطة البرنامج. يرجى الرجوع إلى [ملف الاختبار\_en.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_en.md).

4. إذا كنت بحاجة إلى إعادة ترجمة مقال معين (مثل ترجمة غير دقيقة أو تغيير محتوى المقال، وما إلى ذلك)، يمكنك إضافة النص `[translate]` في المقال (مع الحرص على ترك سطر فارغ أعلى وأسفل النص). سيتجاهل هذا الأمر قائمة الاستبعاد وقائمة الملفات المعالجة سابقًا وسيجبر على ترجمة المقال. يرجى الرجوع إلى [ملف الاختبار\_force-mark.md](https://github.com/linyuxuanlin/Auto-i18n/blob/main/testdir/to-translate/测试文章_force-mark.md).

5. إذا كان الملف بتنسيق Markdown يحتوي على Front Matter، سيتم التعامل معه وفقًا لقواعد البرنامج الموجودة في `front_matter_translation_rules`:

   - الترجمة التلقائية: سيتم ترجمة العناوين أو حقول الوصف باستخدام ChatGPT.
   - استبدال الحقول الثابتة: سيتم استخدام هذا للفئات أو الوسوم. مثلاً، إذا كان لديك نفس الوسم باللغة الصينية وتريد أن لا يتم ترجمته بأكواد بالإنجليزية مختلفة.
   - عدم القيام بأي معالجة: سيتم الاحتفاظ بالنص الأصلي للحقول التي لم تتم معالجتها وفقًا للقواعد السابقة، مثل التواريخ والروابط.

## دليل الأتمتة باستخدام GitHub Actions

يمكنك إنشاء ملف `.github/workflows/ci.yml` في مستودع مشروعك الخاص. عندما يتم اكتشاف تحديث في مستودع GitHub الخاص بك، سيقوم GitHub Actions بمعالجة الترجمة تلقائيًا والالتزام التلقائي بالمستودع الأصلي.

يمكنك الاستعانة بالقالب التالي لمحتوى ملف `ci.yml`: [ci_template.yml](https://github.com/linyuxuanlin/Auto-i18n/blob/main/ci_template.yml)

سيتعين عليك إضافة اثنين من الأسرار (secrets) في إعدادات مستودعك في "Settings" - "Secrets and variables" - "Repository secrets": `CHATGPT_API_BASE` و `CHATGPT_API_KEY`، وعليك أيضًا تعليق البيانات الواردة في برنامج `auto-translater.py`.

## حل المشكلات

1. إذا كنت بحاجة إلى التحقق من صلاحية مفتاح API الخاص بـ ChatGPT، يمكنك استخدام البرنامج [verify-api-key.py](https://github.com/linyuxuanlin/Auto-i18n/blob/main/Archive/verify-api-key.py) لإجراء الاختبار. إذا كنت تستخدم API الرسمي في الصين، قد تحتاج إلى استخدام وكيل محلي.

2. إذا كان Front Matter في ملف Markdown لا يتعرف عليه بشكل صحيح، يمكنك استخدام البرنامج [detect_front_matter.py](https://github.com/liny

```markdown
1. في بعض الحالات الخاصة، قد يحدث عدم دقة في الترجمة أو عدم ترجمة بعض الحقول. ننصح بالتحقق اليدوي بعد الترجمة قبل نشر المقال.
2. (تم الحل) ~~إذا كان هناك Front Matter في الـ Markdown، سيتم الاحتفاظ بالمحتوى الأصلي لـ Front Matter. تجري تطوير ميزة ترجمة معلمات Front Matter حاليًا.~~

## المساهمة

نرحب بمشاركتك في تحسين هذا المشروع! إذا كنت ترغب في المساهمة بالشفرة أو الإبلاغ عن مشكلة أو تقديم اقتراح، يُرجى الاطلاع على [دليل المساهمة](https://github.com/linyuxuanlin/Auto-i18n/blob/main/CONTRIBUTING.md).

## حقوق النشر والترخيص

يُشترط استخدام [رخصة MIT](https://github.com/linyuxuanlin/Auto-i18n/blob/main/LICENSE) لهذا المشروع.

## الأسئلة والدعم

إذا واجهتك أي مشكلة أثناء استخدام Auto-i18n أو كنت بحاجة إلى دعم تقني، فلا تتردد في [تقديم طلب مساعدة](https://github.com/linyuxuanlin/Auto-i18n/issues).

يتيح مدونتي استخدام Auto-i18n لدعم العديد من اللغات. يمكنك رؤية العرض التوضيحي على [Power's Wiki](https://wiki-power.com).

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## الشكر

- نشكر [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) على توفير مفتاح API لـ ChatGPT مجانًا.
- نشكر [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) على توفير طريقة لتحويل ChatGPT الإصدار الويب إلى واجهة برمجة التطبيقات (API).

[![مخطط تاريخ النجوم](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.