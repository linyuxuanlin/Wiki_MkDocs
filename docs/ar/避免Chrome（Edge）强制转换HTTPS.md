# تجنب تحويل Chrome (Edge) إلى HTTPS بشكل قسري

بعض المواقع يمكن الوصول إليها فقط عبر بروتوكول HTTP ، ولكن في بعض الأحيان يقوم المتصفح بتحويلها بشكل قسري إلى HTTPS ، مما يؤدي إلى حدوث أخطاء في الوصول. ستوضح الخطوات التالية كيفية تعطيل التحويل التلقائي في المتصفح.

## الخطوات

أدخل الرابط في شريط العنوان واضغط على Enter:

- Chrome: `chrome://net-internals/#hsts`
- Edge: `edge://net-internals/#hsts`

في حقل "حذف سياسات أمان النطاق" ، قم بإدخال الروابط التي لا ترغب في تحويلها تلقائيًا. على سبيل المثال ، إذا كنت ترغب في منع تحويل `wiki-power.com` إلى الوصول عبر HTTPS ، قم بإدخال `wiki-power.com` وانقر على "حذف".

ثم أدخل الرابط في شريط العنوان واضغط على Enter:

- Chrome: `chrome://flags/#edge-automatic-https`
- Edge: `edge://flags/#edge-automatic-https`

قم بتغيير الخيار "HTTPS التلقائي" من "الافتراضي" إلى "معطل" ، ثم أعد تشغيل المتصفح.

## المراجع والشكر

- [Edge أو متصفح Chrome يقوم بتحويل عناوين الويب HTTP إلى HTTPS بشكل قسري ، ولا يمكن تغييرها يدويًا إلى HTTP](https://blog.csdn.net/Thinker001/article/details/117717690)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.