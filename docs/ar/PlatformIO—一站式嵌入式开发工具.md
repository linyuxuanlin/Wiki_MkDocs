# PlatformIO — أداة تطوير مدمجة

—— إنشاء بيئة تطوير مدمجة تحل محل Keil / Arduino IDE

![PlatformIO](https://media.wiki-power.com/img/20200531112801.png)

## الخلفية

PlatformIO هو أداة مدمجة قوية. دعونا نلقي نظرة على ميزاته:

- متعددة المنصات، تعمل فقط ببيئة Python (مما يعني أنها يمكن استخدامها على نظام Windows / MacOS / Linux)
- يمكن تثبيتها كإضافة داخل Visual Studio Code (لنتخلص أخيرًا من Keil)
- بيئة قوية تشمل:
  - [**800+ لوحة تطوير شائعة**](https://docs.platformio.org/en/latest/boards/index.html#boards): تجد هنا معظم لوحات التطوير العامة
  - [**35+ منصة تطوير**](https://docs.platformio.org/en/latest/platforms/index.html#platforms): تغطي Atmel AVR (Arduino) / ESP / NXP / 8051 / PIC32 / FPGA / FreeRTOS / ARM (STM32) والمزيد
  - [**20+ إطار عمل**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks): Arduino / CMSIS / STM32Cube وغيرها
- ميزات البناء والتحميل والتصحيح ومراقبة المنفذ الرسلي، ودعم متنوع لمحركات البناء وأدوات التصحيح
- مكتبات وظائف متنوعة
- إكمال تلقائي للشيفرة وفحص الصيغة وإدارة المشاريع المتعددة ودعم السمات
- ميزة التطوير عن بعد (لم يتم التجربة)
- اختبار وحدة (لم يتم التجربة)
- وجود واجهة سطر الأوامر وواجهة المستخدم الرسومية

ببساطة، حان الوقت للتخلي عن جميع بيئات التطوير المختلفة مثل Arduino IDE / Keil / IAR والاستفادة من هذه الخدمة المتكاملة.

## التنزيل والتثبيت

أولاً، تأكد من وجود برنامج Visual Studio Code على حاسوبك (يمكنك الانتقال إلى [**هذا المقال**](https://wiki-power.com/VSCode生产力指南-环境配置) لتنزيله وتثبيته).

ثم قم بالبحث داخل الإضافات (Ctrl + Shift + X) وقم بتثبيت الإضافات التالية: `Python` و `PlatformIO IDE`.

![PlatformIO Plugins](https://media.wiki-power.com/img/20200531113916.png)

بمجرد أن تكون الإضافات مثبتة بنجاح، انقر على "إعادة تحميل" لتشغيل الإضافات. بعد ذلك، استمتع بكوب من القهوة في انتظار تثبيت المكون الأساسي "platformIO-core" تلقائيًا (قد يستغرق وقتًا أطول أثناء التثبيت الأولي).

عند الانتهاء من التثبيت، يمكنك بدء PlatformIO عن طريق النقر على الأزرار ذات الصلة في الشريط الجانبي.

## المراجع والشكر

- [PlatformIO](https://platformio.org/)
- [PlatformIO Docs](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [استخدام Visual Studio Code كبيئة تطوير STM32 (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)
- [مشروع PlatformIO IDE(VSCode) - إطار STM32Cube](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
