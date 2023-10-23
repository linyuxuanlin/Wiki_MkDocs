# استخدام PlatformIO بالاشتراك مع CubeMX

## الخلفية

في المقالة السابقة، يمكننا أن نرى أن PlatformIO أكثر أناقة من Keil في الاستخدام. من المعروف أن مكتبة HAL أكثر سهولة وفعالية في استخدام وضبط المتحكمات STM32 مقارنة بالمكتبة القياسية (بالتعاون مع أداة CubeMX). ومع ذلك، التوافق الرسمي لـ CubeMX مع PlatformIO ليس مثاليًا (يتطلب استخدام وسيط Python لتحويل الشيفرة).

في هذا المقال، سأقدم طريقة فريدة لجعل استخدام PlatformIO مع CubeMX أكثر لذة.

## تهيئة المشروع

إليك الخطوات الرئيسية للمشروع:

### تهيئة CubeMX

1. إنشاء مشروع جديد.
2. اختيار نوع المتحكم (MCU).
3. تكوين Pinout & Configuration
   1. تكوين RCC (اختيار الساعة الخارجية / الساعة الداخلية حسب الحاجة).
   2. تكوين SYS (تغيير خيار DEBUG من "No Debug" إلى "Serial Wire").
4. تكوين Clock Configuration.
5. تكوين Project Manager
   1. صفحة المشروع (Project)
      1. تعبئة اسم المشروع (Project Name) مثل "Template_of_PlatformIO_with_CubeMX".
      2. تغيير موقع المشروع (Project Location) مثل "D:/Desktop".
      3. تغيير مشددات الأدوات (Toolchain / IDE) إلى "Other Toolchains".
   2. صفحة مولد الشيفرة (Code Generator)
      1. اختيار خيار حزمة مكتبات STM32Cube (STM32Cube Firmware Library Package) "Copy only the necessary library files".
      2. تحديد توليف الملفات المولدة (Generated files) لإنشاء ملفات ".c/.h" لكل واجهة.

بعد الانتهاء من التكوين، قم بالنقر على "Generate Code" في الزاوية العليا اليمنى لإنشاء الشيفرة.

### تهيئة PlatformIO

1. افتح الصفحة الرئيسية لـ PlatformIO.
2. انقر فوق "New Project" لإنشاء مشروع جديد.
   1. قم بتعبئة اسم المشروع. انتبه: يجب أن يكون مطابقًا لتكوين CubeMX (على سبيل المثال "Template_of_PlatformIO_with_CubeMX").
   2. اختر اللوحة / نوع المتحكم. يمكنك اختيار مباشرة نوع المتحكم (على سبيل المثال STM32F103C8) أو اختيار اللوحة مباشرة (على سبيل المثال BluePill F103C8). تأكد من تطابقه مع تكوين CubeMX.
   3. اختر الإطار البرمجي (Framework) "STM32Cube".
   4. قم بإلغاء تحديد "استخدام الموقع الافتراضي" في القسم "الموقع" وقم بتحديد مسار مخصص. يجب أن يكون مطابقًا لتكوين CubeMX (على سبيل المثال "D:/Desktop").

3. افتح ملف platformio.ini في المشروع وأضف السطور التالية:

   ```ini
   [platformio]
   include_dir=Inc
   src_dir=Src
   ```

   هذا لأن PlatformIO و CubeMX يولدان فولدرات إطار الشيفرة بشكل مختلف افترضت توافقًا لذا نتبع تكوين CubeMX.

4. يمكنك حذف مجلد "include" في المشروع. ونظرًا لأن أسماء الملفات في Windows غير حساسة لحالة الأحرف، ستتغير المجلد "src" تلقائيًا إلى "Src".

الآن، استمتع بالاستفادة من المشروع!

في المشروع، يتم وضع ملفات الـ `.c` في مجلد `Src` وملفات الـ `.h` في مجلد `Inc`.  
بمجرد وجود الشفرة بين `/* USER CODE BEGIN */` و `/* USER CODE END */`, سيتم الاحتفاظ بها بعد عملية توليف CubeMX ولن تتم كتابتها من جديد.

يمكن استخدام PlatformIO للترجمة باستخدام الاختصار `Ctrl + Alt + B`, وللترجمة والرفع باستخدام `Ctrl + Alt + U`, ولبدء التصحيح باستخدام `F5`.

الخطوة التالية ستتضمن دراسة مكتبة HAL. تابعوا المزيد!

## مراجع وشكر

- [STM32CubeMX سلسلة الدروس 03_إنشاء وتوليف مشروع الشفرة](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B03_%E5%88%9B%E5%BB%BA%E5%B9%B6%E7%94%9F%E6%88%90%E4%BB%A3%E7%A0%81%E5%B7%A5%E7%A8%8B.html)
- [STM32CubeMX سلسلة الدروس 06_مدير المشروع - شرح مفصل](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B06_Project%20Manager%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.html)
- [استخدام VS Code كبيئة تطوير STM32 (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.