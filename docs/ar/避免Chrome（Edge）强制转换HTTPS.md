# تجنب تحويل HTTPS القسري في Chrome (Edge)

يمكن أن يتم الوصول إلى بعض المواقع فقط عبر HTTP ، ولكن في بعض الأحيان يتم تحويلها بشكل قسري إلى HTTPS ، مما يؤدي إلى حدوث أخطاء في الوصول إليها. ستوضح الخطوات التالية كيفية تعطيل التحويل التلقائي للمتصفح.

## خطوات العمل

أدخل الرابط في شريط العنوان واضغط على Enter:

- Chrome: `chrome://net-internals/#hsts`
- Edge: `edge://net-internals/#hsts`

في قائمة "حذف سياسات أمان النطاق" ، اكتب الروابط التي لا تريد تحويلها تلقائيًا. على سبيل المثال ، إذا كنت تريد منع `wiki-power.com` من التحويل القسري إلى HTTPS ، فأدخل `wiki-power.com` وانقر على "حذف".

ثم أدخل الرابط في شريط العنوان واضغط على Enter:

- Chrome: `chrome://flags/#edge-automatic-https`
- Edge: `edge://flags/#edge-automatic-https`

قم بتغيير الخيار "HTTPS التلقائي" من "الافتراضي" إلى "معطل" ، ثم أعد تشغيل المتصفح.

## المراجع والشكر

- [Edge أو Google Chrome يحولان عنوان URL الذي يتم إدخاله يدويًا إلى HTTPS ولا يمكن تغييره إلى HTTP](https://blog.csdn.net/Thinker001/article/details/117717690)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.