```markdown
# العمليات الأساسية في AD - إعداد البيئة

- دليل سلسلة Altium Designer

## الخلفية

تعتمد سلسلة الدروس هذه على Altium Designer 19 (متوافق أيضًا مع الإصدار 20)، وسأقوم بمتابعتها في الإصدارات اللاحقة أيضًا.

## تنزيل البرامج

يُرجى الرجوع مباشرةً إلى [**دليل تثبيت Altium Designer 2020**](https://mp.weixin.qq.com/s?__biz=MzIwMjE1MjMyMw==&mid=502718968&idx=1&sn=4c37dc403171ffad01fca95b5a537b2e&chksm=0ee141143996c8021799bb5bf5407b7b56c2d7fa5dc484bda61893efd74a06a1f6be63a7a35e&scene=20&xtrack=1&key=088e5814bbd70a9bf7fb42111d02cbb81bb55981baea77169d867e2871add46f26dccde79326a96e819591677be92412fc05ff2af437922652dfe7ae1b94dc8172f36186ba0b2b460004027131ceae2c&ascene=1&uin=MTk5MDUwOTA0Mg%3D%3D&devicetype=Windows+10+x64&version=62090523&lang=zh_CN&exportkey=AyOYwgP948kprM0EiAGMcyk%3D&pass_ticket=6jBDTE0Qqg%2BrAl1wrTIo2UeJLmUrtbfUKPpgRGdeqhwXUk8QVkc%2Fyekd3BvlvVsB) للحصول على التعليمات.

## ضبط الإعدادات

لتحقيق أداء متميز، يجب أن نبدأ بضبط الأدوات. عند فتح Altium Designer للمرة الأولى، يمكننا ضبط بعض الإعدادات لتجعل الأداة أكثر سهولة في الاستخدام. ابحث عن رمز **الترس** في الزاوية العلوية اليمنى، ثم **افتح صفحة الإعدادات** وقم باتباع الإرشادات التالية.

### تعيين اللغة الصينية

1. انقر بالتتابع على الخيارات في الجانب الأيسر لقائمة الخيارات **System - General**، وقم بتحديد خيار **Use localized resources** في القسم **Localizatioin**.
2. انقر على **تطبيق** لحفظ الإعدادات وأعد تشغيل Altium Designer.

### محرر PCB

1. انقر على الخيار **PCB Editor** في القائمة الجانبية اليسرى.
2. في الخيار **PCB Editor**، انقر على الخيار **General**، ثم حدد **Rebuild polygons after modification** في القسم **Copper Pour**. ثم حدد خياري **Disable opening old version reports** و **Disable opening new version reports** في قسم **Document Format Modification Report**. وأخيرًا، قم بتغيير نوع المؤشر إلى **Large 90** في القسم **Others**.
3. انقر على الخيار **Display**، وحدد خيار **Apply highlighting during interactive editing** في قسم **Highlight Options**.
4. انقر على الخيار **Board Insight Color Overrides**، وقم بتحديد **Solid (Overlay Color)** في قسم **Basic Styles**.
5. انقر على الخيار **DRC Violations Display**، وقم بتحديد **Solid (Overlay Color)** في قسم **Conflict Overlay Style**.
6. انقر على **تطبيق** لحفظ الإعدادات وأعد تشغيل Altium Designer.

### الألواح

1. أغلق صفحة الإعدادات واختر من القائمة الرئيسية **View - Panels**، ثم حدد بالتتابع **Components, Messages**.
2. في الزاوية العلوية اليمنى للوحة المنبثقة، انقر على أيقونة **الدبوس** لتثبيت اللوحة على الجانب الأيمن.

### تعيين الخلفية إلى الشبكة

1. افتح أي ملف PCB (إذا لم يكن لديك ملف يمكنك إنشاء واحدًا).
2. اضغط على **Ctrl + G** لفتح نافذة إعدادات الشبكة.
3. في قسم **Display**، قم بتعيين خياري **Dots** لكل من **Fine** و **Coarse** في قائمة العرض.

## التوافق مع لوحة المفاتيح

إذا لم تكن قادرًا على استخدام مفاتيح الاختصار، يُرجى التحقق مما إذا كنت قد قمت بالتبديل إلى اللغة الإنجليزية (ستظهر حالة لوح

```markdown
1. قم بفتح **لوحة التحكم** ، ثم انتقل إلى صفحة **الساعة واللغة والمنطقة - اللغة**.
2. انقر على زر **إضافة لغة** وقم بإضافة **الإنجليزية** واختر **الإنجليزية (الولايات المتحدة)**.
3. يمكنك التبديل بين أنظمة الإدخال في شريط المهام على سطح المكتب.

## تلخيص

في هذا الفصل، قمنا بإعداد بيئة Altium Designer بشكل أساسي، ويمكننا الآن البدء في رسم الدوائر بسعادة :smiley:

## الإشارات والشكر

- [المقالة عن Altium Designer من شركة Altium](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.