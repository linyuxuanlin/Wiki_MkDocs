# ملاحظات تطوير مكتبة HAL - إعداد البيئة

ملاحظة: يتم تنفيذ هذا البرنامج التعليمي باستخدام لوحة STM32F429IGT6 من منتج Reverse 客.

## تثبيت البرامج

### Keil MDK

يرجى الرجوع إلى المقالة [**دليل تكوين Keil MDK**](https://wiki-power.com/KeilMDK%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97) للحصول على التفاصيل.

### بيئة تشغيل جافا

هذه هي بيئة جافا المطلوبة لتشغيل STM32CubeMX. يمكنك تنزيلها وتثبيتها من [**الرابط الرسمي**](https://www.java.com/en/download/).

### STM32CubeMX

قم بتنزيل وتثبيت STM32CubeMX من [**الرابط الرسمي**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## إعداد المشروع

### البداية

ابدأ بإنشاء مشروع جديد وحفظه بعد اختيار الشرائح.

### تكوين SYS

`Pinout & Configurations` - `System Core` - `SYS`

قم بتغيير خيار `Debug` إلى `Serial Wire` (يرجى الرجوع إلى المقالة [**استدراجات CubeMX و CubeIDE**](https://wiki-power.com/CubeMX与CubeIDE避坑) للتفاصيل).

### تكوين RCC

`Pinout & Configurations` - `System Core` - `RCC`

قم بتكوينه وفقًا للوضعية الخاصة باللوحة.

على سبيل المثال، استنادًا إلى الرسم البياني للوحة:

![](https://media.wiki-power.com/img/20210205205030.png)

قم بتعيين خيارات `HSE` و `LSE` على أن تكون كلاهما خارجيتين فقط:

![](https://media.wiki-power.com/img/20210205205140.png)

### تكوين شجرة الساعة

قم بتكوينها في واجهة `Clock Configuration`.

![](https://media.wiki-power.com/img/20210205205550.png)

اتبع الخطوات كما هو موضح في الصورة أعلاه:

1. استنادًا إلى معلومات الكريستال الخارجي على لوحتك، قم بإدخال القيم في أول اثنين من الأعمدة اليسرى.
2. حدد خيار `HSE`، لأن تردد الكريستال الخارجي أعلى ودقته أفضل من التردد الداخلي.
3. حدد خيار `PLLCLK` لاستخدام PLL (التضاعف التسلسلي للتردد) للحصول على تردد عالٍ.
4. أدخل قيمة `HCKL`، عادة استنادًا إلى أعلى تردد محدد في القسم السفلي، ثم اضغط على Enter لحساب تلقائي للمضاعفات والتقسيمات.

### تكوين خيارات إدارة المشروع

![](https://media.wiki-power.com/img/20210130095224.png)

![](https://media.wiki-power.com/img/20210130095239.png)

## الفروق بين مكتبة HAL والمكتبة القياسية

من أجل زيادة النقلية، تتضمن مكتبة HAL وظائف إضافية مثل **المقابض، وظائف MSP، وظائف الاستدعاء**. يمكن الرجوع إلى المراجع المذكورة في الروابط في نهاية هذا النص لمزيد من التفاصيل.

## المراجع والشكر

- [**تفصيل RCC لساعة النظام في STM32**](https://blog.csdn.net/as480133937/article/details/98845509)
- [**طريقة وعملية تكوين شجرة الساعة RCC لبدء تشغيل اللوحة**](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [**ملخص شامل لمعرفة كل شيء عن STM32 HAL**](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [**أصبحت أمورًا واضحة أكثر، ملخص شامل لمعرفة كل شيء عن STM32 HAL**](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
