# PlatformIO - أداة تطوير مدمجة

- إنشاء بيئة تطوير مدمجة لاستبدال Keil / Arduino IDE

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531112801.png)

## الخلفية

PlatformIO هي أداة مدمجة قوية ، وهناك بعض الميزات:

- متعددة المنصات ، تحتاج فقط إلى بيئة Python (مما يعني أنه يمكن استخدامه على Windows / MacOS / Linux)
- يمكن تثبيته كإضافة داخل VSCode (يمكن التخلص من Keil أخيرًا)
- بيئة قوية:
  - [**800+ لوحة تطوير شائعة**](https://docs.platformio.org/en/latest/boards/index.html#boards) : تقريبًا كل ما يمكنك شراؤه من لوحات التطوير العامة متاح هنا
  - [**35+ منصة تطوير**](https://docs.platformio.org/en/latest/platforms/index.html#platforms) : تغطي Atmel AVR (Arduino) / ESP / NXP / 8051 / PIC32 / FPGA / FreeRTOS / ARM (STM32) وغيرها
  - [**20+ إطار عمل**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks) : Arduino / CMSIS / STM32Cube وغيرها
- يحتوي على وظائف الترميز / التنزيل / التصحيح / مراقبة المنافذ التسلسلية ، ويدعم جميع أنواع المترجمات / المصححين
- يوفر مكتبات وظائف مختلفة
- إكمال تلقائي للشفرة ، فحص الصياغة ، إدارة المشاريع المتعددة ، والتكيف مع الموضوع
- ميزة التطوير عن بعد (لم يتم تجربتها)
- اختبار الوحدة (لم يتم تجربتها)
- يوجد بيئة سطر الأوامر والواجهة الرسومية

على العموم ، حان الوقت للتخلص من جميع بيئات التطوير (مثل Arduino IDE / Keil / IAR) والاستمتاع بخدمة واحدة.

## التنزيل والتثبيت

أولاً ، تأكد من وجود VSCode على جهاز الكمبيوتر الخاص بك (يمكنك الانتقال إلى [**هذه المقالة**](https://wiki-power.com/ar/ دليل إنتاجية VSCode - تكوين البيئة)

ابحث وقم بتثبيت `Python` و `PlatformIO IDE` داخل `الملحقات` (`Ctrl + Shift + X`).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531113916.png)

بعد تثبيت الإضافة بنجاح ، انقر فوق `إعادة تحميل` لتشغيل الإضافة ، ثم اصنع فنجانًا من القهوة وانتظر حتى يتم تثبيت مكونات النواة الأساسية `platformIO-core` تلقائيًا (قد يستغرق الأمر وقتًا طويلاً في المرة الأولى).

بعد الانتهاء من التثبيت ، انقر فوق الأزرار ذات الصلة في الشريط الجانبي لتشغيل PlatformIO.

## المراجع والشكر

- [PlatformIO](https://platformio.org/)
- [PlatformIO Docs](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [استخدام VS Code كمنصة تطوير STM32 (platformIO)](https://www.jianshu.com/p/49cfa03d6164)
- [PlatformIO IDE (VSCode) - مشروع إطار stm32cube](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
