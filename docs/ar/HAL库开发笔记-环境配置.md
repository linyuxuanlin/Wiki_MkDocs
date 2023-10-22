# مذكرات تطوير مكتبة HAL - إعداد البيئة

ملاحظة: يتم استناد هذا البرنامج التعليمي إلى لوحة STM32F429IGT6 من STMicroelectronics.

## تثبيت البرامج

### Keil MDK

للحصول على التفاصيل، يُرجى رؤية المقالة [**دليل تكوين Keil MDK**](to_be_replace[3]).

### بيئة تشغيل Java

هذه بيئة Java المطلوبة لتشغيل STM32CubeMX. يمكنك تنزيلها وتثبيتها من [**الرابط الرسمي**](https://www.java.com/en/download/).

### STM32CubeMX

يمكنك تنزيل وتثبيت STM32CubeMX من [**الرابط الرسمي**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## تكوين المشروع

### البدء

ابدأ بإنشاء مشروع جديد واختر الرقاقة المستخدمة ثم احفظ المشروع.

### تكوين النظام

`توصيل الأرجل والتكوينات` - `نواة النظام` - `النظام`

قم بتغيير خيار `Debug` إلى `Serial Wire` (يرجى الرجوع إلى المقالة [**تفادي مشاكل CubeMX و CubeIDE**](to_be_replace[3]) لمزيد من التفاصيل).

### تكوين RCC

`توصيل الأرجل والتكوينات` - `نواة النظام` - `RCC`

قم بتكوينه وفقًا لحالة اللوحة.

على سبيل المثال، استنادًا إلى رسم الدائرة الكهربائية للوحة:

![](https://img.wiki-power.com/d/wiki-media/img/20210205205030.png)

فقط قم بتعيين خيارات `HSE` و `LSE` على أن تكون كلتاهما كمراوح الكريستال الخارجية:

![](https://img.wiki-power.com/d/wiki-media/img/20210205205140.png)

### تكوين شجرة الساعة

تكوين شجرة الساعة في واجهة `تكوين الساعة`.

وفقًا للخطوات الموجودة في الصورة أعلاه:

1. استنادًا إلى معلومات المروحة الخارجية المضمنة على اللوحة، قم بإدخال القيم للترددين الأيمنين.
2. حدد خيار `HSE`، لأن تردد المروحة الخارجية ودقتها أعلى من المروحة الداخلية.
3. حدد `PLLCLK`، لاستخدام تضاعف النسق بواسطة الدائرة المتكافئة PLL للحصول على تردد عالٍ.
4. قم بإدخال القيمة المطلوبة لـ `HCKL`، وعادة ما يتم استنادها إلى أقصى تردد موجود في الأسفل، بمجرد إدخال القيمة، سيتم حساب القيم الترددية وعوامل التضاعف تلقائيًا.

### تكوين خيارات إدارة المشروع

![](https://img.wiki-power.com/d/wiki-media/img/20210130095224.png)

![](https://img.wiki-power.com/d/wiki-media/img/20210130095239.png)

## الفروق بين مكتبة HAL والمكتبة القياسية

من أجل زيادة النقلية، تحتوي مكتبة HAL على ثلاث ميزات إضافية مقارنة بالمكتبة القياسية وهي **مقبض، وظيفة MSP، ووظيفة الاستدعاء**. يمكن الاطلاع على التفاصيل في الروابط المرجعية في نهاية الوثيقة.

## المراجع والشكر

Here is the provided text translated into Arabic:

- [【STM32】 تفصيل مختصر عن ساعة النظام RCC](https://blog.csdn.net/as480133937/article/details/98845509)
- [طريقة وعملية تهيئة شجرة الساعة RCC لبدء تشغيل اللوحة](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [ملخص شامل لمعرفة STM32 HAL](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [واضح الآن، ملخص شامل لمعرفة STM32 HAL](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.