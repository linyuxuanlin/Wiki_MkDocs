# استخدام PlatformIO مع CubeMX

## الخلفية

في المقالة السابقة [**PlatformIO - أداة تطوير مدمجة**](https://wiki-power.com/ar/PlatformIO—一站式嵌入式开发工具)، يمكننا أن نرى أن استخدام PlatformIO أكثر أناقة من Keil.  
كما هو معروف، تكون مكتبة HAL أكثر سهولة ويسرًا في طريقة فتح STM32 (بالتعاون مع أداة CubeMX)، ولكن التوافق الرسمي لـ PlatformIO مع CubeMX ليس مثاليًا تمامًا (يتطلب تحويل الكود من خلال وسيط Python).

في هذه المقالة، سأقدم طريقة فريدة من نوعها لجعل استخدام PlatformIO مع CubeMX أكثر لذة.

## تهيئة المشروع

لا تريد القراءة الطويلة: لقد وضعت مجلد المشروع الذي تم إنشاؤه بعد الخطوات التالية في [**هذا المستودع**](https://github.com/linyuxuanlin/Template_of_PlatformIO_with_CubeMX)، يمكنك استنساخه مباشرة.

### تهيئة CubeMX

1. إنشاء مشروع جديد
2. حدد نوع MCU
3. تكوين Pinout & Configuration
   1. تكوين RCC (اختيار الساعة الخارجية / الداخلية ، يمكن تجاهلها في بعض الحالات)
   2. تكوين SYS (تغيير خيار DEBUG من `No Debug` إلى `Serial Wire`)
4. تكوين Clock Configuration
5. تكوين Project Manager
   1. صفحة المشروع
      1. اكتب اسم المشروع (Project Name) على سبيل المثال `Template_of_PlatformIO_with_CubeMX`
      2. تغيير مسار المشروع (Project Location) على سبيل المثال `D:/Desktop`
      3. قم بتغيير سلسلة الأدوات (Toolchain / IDE) إلى `Other Toolchains`
   2. صفحة Code Generator
      1. حدد خيار حزمة البرامج الثابتة (STM32Cube Firmware Library Package) كـ `Copy only the necessary library files`
      2. حدد `Generate peripheral initialization as a pair of '.c/.h' files per peripheral` في خيارات إنشاء الملفات (Generated files)

أخيرًا، بعد الانتهاء من التكوين، انقر فوق `Generate Code` في الزاوية العلوية اليمنى لتوليد الكود.

### تهيئة PlatformIO

1. افتح صفحة PlatformIO
2. انقر فوق `New Project` لإنشاء مشروع جديد
   1. اكتب اسم المشروع. تنبيه: يجب أن يتطابق بالضبط مع الاسم الذي تم تكوينه في CubeMX! (على سبيل المثال `Template_of_PlatformIO_with_CubeMX`)
   2. حدد لوحة / نوع MCU. يمكنك اختيار نوع MCU مباشرةً (على سبيل المثال STM32F103C8) أو اختيار النموذج (على سبيل المثال BluePill F103C8). تنبيه: يجب أن يتطابق بالضبط مع الاسم الذي تم تكوينه في CubeMX!
   3. اختر Framework `STM32Cube`
   4. قم بإلغاء تحديد `Use default location` في المسار `Location` ، واختر مسارًا مخصصًا. تنبيه: يجب أن يتطابق بالضبط مع الاسم الذي تم تكوينه في CubeMX! (على سبيل المثال `D:/Desktop`)
3. افتح ملف `platformio.ini` في المشروع وأضف الأسطر التالية:

   ```ini
   [platformio]
   include_dir=Inc
   src_dir=Src
   ```

   هنا يتم تحديد مسار الملفات الذي يختلف بين PlatformIO و CubeMX. لتحقيق التوافقية، نحن نتبع CubeMX.

4. يمكنك حذف مجلد `include` من المشروع. ونظرًا لأن أسماء ملفات Windows لا تفرق بين الحروف الكبيرة والصغيرة، فإن مجلد `src` يتحول بشكل طبيعي إلى `Src`.

### استمتع بالاستخدام!



في المشروع، يتم وضع الملفات ذات الامتداد `.c` في مجلد `Src`، والملفات ذات الامتداد `.h` في مجلد `Inc`.  
يتم الاحتفاظ بأي كود يتم وضعه بين `/* USER CODE BEGIN */` و `/* USER CODE END */`، ولن يتم استبداله خلال عملية التوليد التي تتم بعد ذلك باستخدام CubeMX.

يمكن استخدام PlatformIO للترجمة باستخدام اختصارات لوحة المفاتيح `Ctrl + Alt + B`، وللترجمة والتحميل باستخدام `Ctrl + Alt + U`، ولبدء التصحيح باستخدام `F5`.

الخطوة التالية هي دراسة مكتبة HAL. تابع...

## المراجع والشكر

- [STM32CubeMX 系列教程 03\_创建并生成代码工程](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B03_%E5%88%9B%E5%BB%BA%E5%B9%B6%E7%94%9F%E6%88%90%E4%BB%A3%E7%A0%81%E5%B7%A5%E7%A8%8B.html)
- [STM32CubeMX 系列教程 06_Project Manager 工程管理器详细说明](https://www.strongerhuang.com/STM32Cube/STM32CubeMX/STM32CubeMX%E7%B3%BB%E5%88%97%E6%95%99%E7%A8%8B06_Project%20Manager%E5%B7%A5%E7%A8%8B%E7%AE%A1%E7%90%86%E5%99%A8%E8%AF%A6%E7%BB%86%E8%AF%B4%E6%98%8E.html)
- [用 VS Code 作为 STM32 开发平台（PlatformIO）](https://www.jianshu.com/p/49cfa03d6164)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.