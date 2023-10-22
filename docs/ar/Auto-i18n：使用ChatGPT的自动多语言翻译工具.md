# Auto-i18n: Using ChatGPT's Automatic Multilingual Translation Tool

Auto-i18n is a tool that automatically translates Markdown files into multiple languages using ChatGPT. It achieves full automation of blog post i18n (Internationalization). All you need to do is push your blog posts to a GitHub repository, and with the help of GitHub Actions, it will automatically translate them into multiple languages. (Currently supporting English, Spanish, and Arabic, with more language support coming soon)

Key Features of Auto-i18n:

- **Batch Multilingual Translation**: Auto-i18n offers batch translation capabilities, allowing you to translate all Markdown documents in an entire directory into multiple languages at once, significantly increasing the efficiency of multilingual projects.
- **Front Matter Compatibility**: Auto-i18n is compatible with Markdown Front Matter syntax, enabling you to customize translation or replacement rules for different fields.
- **Fixed Content Replacement**: Auto-i18n also supports fixed content replacement. If you want the translation of certain repetitive fields in your documents to remain the same, this feature helps maintain consistency in your documents.
- **Automation Workflow**: You can automate the translation process using GitHub Actions. No manual intervention is required; the translation work will be carried out automatically, allowing you to focus more on the content.

## Getting Started

1. Clone the repository to your local machine, rename `env_template.py` to `env.py`, and provide your ChatGPT API key. If you don't have your own API, you can get a free one from [GPT_API_free](https://github.com/chatanywhere/GPT_API_free) or use [go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) to convert the web-based ChatGPT into an API.
2. Install the required modules: `pip install -r requirements.txt`.
3. Run the command `python auto-translater.py` to execute the program. It will automatically process all Markdown files in the test directory `testdir/to-translate` and translate them into English, Spanish, and Arabic. (More language support will be added in the future)

## Detailed Description

The logic of the `auto-translater.py` program is as follows:

1. The program will automatically process all Markdown files in the test directory `testdir/to-translate`, and you can exclude files that don't need translation in the `exclude_list` variable.
2. The processed file names will be recorded in the automatically generated `processed_list.txt`. When you run the program next time, already processed files will not be translated again.
3. For articles originally written in English, the program will not retranslate them into English or translate them back into Chinese. Instead, it will translate them into other languages. You need to add the field `> This post was originally written in English.` in the article (with a blank line above and below) for the program to recognize. Please refer to [测试文章_en.md](testdir/to-translate/测试文章_en.md).
4. If you need to retranslate a specific article (e.g., if the translation result is inaccurate or the content has changed), you can add the `[translate]` field in the article (again, with a blank line above and below). This will override the rules in `exclude_list` and `processed_list` and force a translation. Please refer to [测试文章_force-mark.md](testdir/to-translate/测试文章_force-mark.md).
5. If a Markdown file contains Front Matter, it will be processed according to the rules in `front_matter_translation_rules` within the program:
   1. Automatic Translation: Translated by ChatGPT, suitable for article titles or descriptions.
   2. Fixed Field Replacement: Suitable for categories or tags fields. For example, when you want the same Chinese tag name to remain untranslated in different English tags to avoid indexing errors.
   3. No Processing: If a field doesn't appear in the above two rules, it will preserve the original text, suitable for date, URL, etc.

## دليل أتوماتي لـ GitHub Actions

يمكنك إنشاء ملف `.github/workflows/ci.yml` في مستودع مشروعك الخاص. عند اكتشاف تحديثات في مستودع GitHub الخاص بك، يمكن استخدام GitHub Actions تلقائيًا لمعالجة الترجمة والتعهد تلقائيًا بالمستودع الأصلي.

يمكن الرجوع إلى المحتوى في `ci.yml` باستخدام القالب التالي: [ci_template.yml](ci_template.yml)

يجب عليك إضافة اثنين من الأسرار في "إعدادات" المستودع - "الأسرار والمتغيرات" - "أسرار المستودع": `CHATGPT_API_BASE` و `CHATGPT_API_KEY`. كما يجب عليك تعليق البيانات المستوردة في البرنامج `auto-translater.py`.

## حل المشكلات

1. إذا كنت بحاجة إلى التحقق من صلاحية مفتاح ChatGPT API، يمكنك استخدام البرنامج [verify-api-key.py](Archive/verify-api-key.py) لإجراء الاختبار. إذا كنت تستخدم API الرسمية في الصين، فيجب أن تكون لديك وكيل محلي.
2. إذا لم يتم التعرف بشكل صحيح على Front Matter في Markdown، يمكن استخدام البرنامج [detect_front_matter.py](Archive/detect_front_matter.py) للفحص.
3. عند واجهتك مشاكل مع GitHub Actions، يجب التحقق أولاً من صحة مراجعات المسارات (مثل `dir_to_translate` و `dir_translated_en` و `dir_translated_es` و `dir_translated_ar` و `processed_list`).

## المشكلات القادمة

1. في بعض الحالات الخاصة، قد تحدث أخطاء في الترجمة أو قد لا تتم الترجمة لبعض الحقول. نوصي بالتحقق يدويًا من الترجمة بعد ذلك قبل نشر المقال.
2. (تم حله) ~~إذا كان هناك Front Matter في Markdown، سيتم الاحتفاظ بمحتوى Front Matter الأصلي. وظيفة ترجمة معلمات Front Matter قيد التطوير.~~

## المساهمة

نرحب بمساهمتك في تحسين هذا المشروع! إذا كنت ترغب في المساهمة بالشفرة، أو تقديم تقارير عن المشكلات، أو تقديم اقتراحات، يُرجى الاطلاع على [دليل المساهمة](CONTRIBUTING.md).

## حقوق النشر والتراخيص

يتم توزيع هذا المشروع وفقًا لترخيص MIT.

## المشكلات والدعم

إذا واجهت أي مشكلة أثناء استخدام أوتو-18N، أو إذا كنت بحاجة إلى دعم تقني، فلا تتردد في [تقديم طلب](https://github.com/linyuxuanlin/Auto-i18n/issues).

مدونتي تستخدم أوتو-18N لدعم اللغات المتعددة، يمكنك زيارة [Power's Wiki](https://wiki-power.com) لرؤية الديمو.

[![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202310222223670.png)](https://wiki-power.com)

## الشكر

- نشكر [chatanywhere/GPT_API_free](https://github.com/chatanywhere/GPT_API_free) على توفير مفتاح ChatGPT API مجاني.
- نشكر [linweiyuan/go-chatgpt-api](https://github.com/linweiyuan/go-chatgpt-api) على توفير وسيلة لتحويل نسخة الويب من ChatGPT إلى واجهة برمجة التطبيقات (API).

[![Star History Chart](https://api.star-history.com/svg?repos=linyuxuanlin/Auto-i18n&type=Date)](https://star-history.com/#linyuxuanlin/Auto-i18n&Date)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.