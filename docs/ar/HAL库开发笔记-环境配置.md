# ملاحظات تطوير مكتبة HAL - إعداد البيئة

ملاحظة: يستند هذا البرنامج التعليمي إلى لوحة STM32F429IGT6 من عكس الضيف.

## تثبيت البرامج اللازمة

### Keil MDK

انظر المقال [**دليل تكوين Keil MDK**](https://wiki-power.com/ar/KeilMDK%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97) للحصول على مزيد من المعلومات.

### بيئة تشغيل Java

هذه هي بيئة Java التي يحتاجها STM32CubeMX. يمكن تنزيلها وتثبيتها من [**رابط الموقع الرسمي**](https://www.java.com/en/download/).

### STM32CubeMX

يمكن تنزيل وتثبيت STM32CubeMX من [**رابط الموقع الرسمي**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## تكوين المشروع

### البدء

أنشئ مشروعًا واختر الشريحة ثم احفظها أولاً.

### تكوين SYS

`Pinout & Configurations` - `System Core` - `SYS`

قم بتغيير خيار `Debug` إلى `Serial Wire` (لمزيد من التفاصيل ، انظر المقال [**CubeMX و CubeIDE تجنب المشاكل**](https://wiki-power.com/ar/CubeMXوCubeIDEتجنبالمشاكل)).

### تكوين RCC

`Pinout & Configurations` - `System Core` - `RCC`

قم بتعيينها وفقًا لحالة اللوحة.

على سبيل المثال ، استنادًا إلى مخطط اللوحة:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205205030.png)

يمكنك تعيين خيارات `HSE` و `LSE` على التوالي على الكريستال الخارجي:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205205140.png)

### تكوين شجرة الساعة

يتم التكوين في واجهة `Clock Configuration`.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205205550.png)

وفقًا للخطوات في الصورة أعلاه:

1. استنادًا إلى معلمات الكريستال الخارجي الموجود على اللوحة ، املأ قيم التردد الأوليين على اليسار.
2. حدد `HSE` ، لأن تردد الكريستال الخارجي ودقته أعلى من الداخلية.
3. حدد `PLLCLK` ، واستخدم تضاعف تردد PLL للحصول على تردد عالي.
4. املأ قيمة `HCKL` ، وعادة ما يتم ملء القيمة وفقًا لأقصى تردد موضح في الأسفل ، وبعد الانتهاء من الملء ، يتم حساب مضاعف التقسيم تلقائيًا.

### تكوين خيارات إدارة المشروع

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210130095224.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210130095239.png)

## الفرق بين مكتبة HAL والمكتبة القياسية

لزيادة النقلية ، تحتوي مكتبة HAL على ثلاث وظائف إضافية: **المقبض ودوال MSP ودوال Callback**. يمكن الرجوع إلى المحتوى الموجود في الروابط المرجعية في نهاية المقال.

## المراجع والشكر

- [تفسير RCC لنظام STM32 بالتفصيل](https://blog.csdn.net/as480133937/article/details/98845509)
- [طريقة تكوين شجرة RCC الكاملة لتهيئة اللوحة](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [ملخص شامل لمكتبة STM32 HAL](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [ملخص شامل وواضح لمكتبة STM32 HAL](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
