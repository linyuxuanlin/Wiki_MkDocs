# دليل إنتاجية VS Code - Jupyter Notebook

استخدم VS Code لإنشاء أدوات إنتاجية فعالة.

![](https://img.wiki-power.com/d/wiki-media/img/20200323155728.png)

يعد Jupyter Notebook أداة قوية للغاية، حيث يتيح لنا كتابة الشفرة وتشغيلها وعرض النتائج وتصور البيانات وعرض النتائج في بيئة واحدة ... بشكل عام، يجعل كتابة المستندات التي تحتوي على الشفرة أسهل بكثير.

في المقالة السابقة، قمنا بإعداد بيئة VS Code الأساسية. في هذه المقالة، سأشرح Jupyter with VS Code بالتفصيل.

## إعداد البيئة

كما هو معروف، يعتمد Jupyter Notebooks على بيئة Python.  
للتحقق مما إذا كان لديك بيئة Python، اكتب **Python: Select Interpreter** في لوحة الأوامر في VS Code (`Ctrl + Shift + P`)، إذا رأيت إصدارات Python التي يمكنك اختيارها، فلا يوجد مشكلة.

إذا لم يكن لديك بيئة Python، يمكنك تثبيتها باستخدام الطريقة التالية:

1. قم بتنزيل حزمة التثبيت الأحدث من [**موقع Python الرسمي**](https://www.python.org/) (حاول اختيار إصدار `web-based installer` إذا أمكن)

بعد إعداد بيئة Python المحلية، ستحتاج أيضًا إلى تثبيت إضافة [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python) داخل VS Code. في تحديث مؤخر، تم تضمين Jupyter Notebooks في هذه الإضافة، لذلك لا يلزم تثبيتها بشكل منفصل.

## إنشاء دفتر

بعد إعداد البيئة، يمكننا إنشاء دفتر Jupyter فارغ (ملف `.ipynb`) باستخدام لوحة الأوامر في VS Code (`Ctrl + Shift + P`) وكتابة **Python: Create Blank New Jupyter**. كما هو موضح في الصورة التالية:

![](https://img.wiki-power.com/d/wiki-media/img/20200323153020.png)

يمكن رؤية أن الشفرة تعمل بشكل صحيح.

## العمليات الأساسية

يستخدم Jupyter Notebook شفرات الأكواد الفردية (code cells) لإنشاء وتحرير وتشغيل الشفرة.

![](https://img.wiki-power.com/d/wiki-media/img/20200323153717.png)

### إضافة شفرات الأكواد

![](https://img.wiki-power.com/d/wiki-media/img/20200323153850.png)

### تشغيل شفرة واحدة

![](https://img.wiki-power.com/d/wiki-media/img/20200323153939.png)

### تشغيل شفرات متعددة

![](https://img.wiki-power.com/d/wiki-media/img/20200323154005.png)

### نقل شفرة

![](https://img.wiki-power.com/d/wiki-media/img/20200323154059.png)

### حذف شفرة

![](https://img.wiki-power.com/d/wiki-media/img/20200323154148.png)

### التبديل بين الشفرة و Markdown



### مشاهد الرسم البياني

من خلال مشاهد الرسم البياني ، يمكنك بسهولة عرض الرسوم البيانية التي تم إخراجها من الكود ، كما يمكنك تصدير الرسوم البيانية إلى صور بتنسيقات مختلفة:

![](https://img.wiki-power.com/d/wiki-media/img/20200323154555.png)

### مشاهد البيانات والمتغيرات

يمكنك عرض نوع وكمية وقيمة المتغيرات في الوقت الحقيقي من خلال مشاهد المتغيرات:

![](https://img.wiki-power.com/d/wiki-media/img/20200323154758.png)

كما يمكنك تصفح البيانات الأكثر تفصيلاً من خلال مشاهد البيانات:

![](https://img.wiki-power.com/d/wiki-media/img/20200323154832.png)

## المراجع والشكر

- [العمل مع دفاتر Jupyter في Visual Studio Code](https://code.visualstudio.com/docs/python/jupyter-support)
- [VS Code Python الإصدار الجديد! دعم Jupyter Notebook الأصلي أخيرًا هنا!](https://zhuanlan.zhihu.com/p/85445777)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.