# AD Basic Operations - Basic Knowledge

—— Altium Designer Tutorial Series

## Background

Before starting to design a PCB, it is necessary to familiarize ourselves with some basic knowledge of Altium Designer and circuit design.

## Library Installation

A library is a collection of schematic/PCB footprints for each discrete component (such as resistors, capacitors, etc.), making it easy to call them directly. It is not necessary to create a schematic/footprint library for every component, but **organizing your own library is a must**. Imagine that every component in your project is from someone else's library (and different libraries have their own rules), then the more you progress, the more you will be restricted. Having your own library is not only convenient for migration and efficiency improvement, but also conducive to knowledge systematization. With your own rules and system, knowledge will grow exponentially over time. Although the curve of growth is slow at the beginning, there will be no repetitive work in the later stage. At that time, all you need to do is to learn new knowledge and summarize it into the system.

Friendly reminder: Try to extract all the components required for your project from your own organized schematic/footprint library.

### Reference Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): A library I organized myself. The footprint library is complete, and the schematic library only includes the component models required for my project. It is constantly being updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively complete library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite complete library, including some MCU solution boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): A standard integrated library provided by Jia Li Chuang, including all the components that can be SMT pasted by Jia Li Chuang. Using this integrated library will have better compatibility when making PCBs/SMT.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): A schematic/footprint library organized by Bin Ge, covering most of the components required by the hardware in the team.

How to install library files: Refer to [**Installing Library Files in Altium Designer**](https://wiki-power.com/ar/Installing Library Files in Altium Designer)

### Uncommon Components

The libraries provided above already cover more than 95% of the component models on the market. If you really can't find the required components, you can try the following methods:

AD plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This is really super convenient to use.

Search engine: [**Schematic and Footprint Download · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Shortcuts

For Altium Designer, mastering commonly used shortcuts can greatly improve efficiency. The system shortcuts of Altium Designer are composed of letters with underlines in the commands under the menu, such as the shortcut for **Place-Line** is **P-L** (press P first and then L).

### Schematic

- عرض لوحة المكتبة: **PP**
- رسم الأسلاك: **Ctrl + W**
- رسم علامات الشبكة: **PN**
- نسخ المكونات وتحديث الأرقام تلقائيًا: **اضغط Shift + اسحب**
- ترقيم الرسم البياني: **TAT**
- ترقيم المكونات تلقائيًا: **TAA**
  - إعادة تعيين الكل: إعادة تعيين جميع أرقام المكونات لتصبح بتنسيق "حرف + ؟"
  - تحديث قائمة التغييرات: تغيير أرقام المكونات في القائمة
  - قبول التغييرات (إنشاء ECO): قبول تغييرات الأرقام وتنفيذ التغييرات على الرسم البياني الأصلي
- إنشاء جدول BOM: **RI**
- تحديث PCB: **DU**
- محاذاة إلى اليسار (اليمين): **AL** (**AR**)

### PCB

- استيراد التغييرات من الرسم البياني إلى PCB: **DI**
- تغطية التغييرات في PCB إلى الرسم البياني: **DU**
- تبديل الوحدات (بوصة / ملم): **Q**
- تدوير المكونات (بأي زاوية): **EMO**
- وضع المكونات في الطبقة السفلية: **اسحب واضغط L**
- تخطيط تلقائي: **تحديد بالإطار + TOL**
- تعيين نقطة البداية: **EOS**
- تعيين الشبكة: **G**
- توصيل تلقائي: **UAA**
- مسح التوصيلات: **UUA**
- تحديد الأسلاك: **اضغط Shift + حرك المؤشر على السلك**
- تحديد الأسلاك المتصلة بالعقدة: **اضغط Ctrl + انقر بزر الفأرة الأيسر**
- الانعكاس الأفقي: **Ctrl + F**
- القياس: **Ctrl + M**
- التبديل بين العرض ثنائي الأبعاد / ثلاثي الأبعاد: **2/3**
- تدوير في العرض ثلاثي الأبعاد: **اضغط Shift + اسحب**
- مسح المرشح: **Shift + C**
- تبديل عرض الطبقة الواحدة / متعددة الطبقات: **Shift + S**
- غطاء الفتحة باللحام (يمكن تجاهله، يمكن اختياره مباشرة عند الطباعة)
  1. انقر فوق فتحة معينة
  2. انقر بزر الماوس الأيمن - البحث عن كائنات مماثلة
  3. حدد خاصية الحجم بـ Same واضغط على موافق لتحديد جميع الفتحات
  4. في توسيع قناع اللحام في الخصائص ، حدد الطبقة العلوية والطبقة السفلية
- تعيين قواعد التوصيل
  1. **UAA**
  2. إنشاء استراتيجية وتحرير القواعد
  3. تعديل القواعد في Routing (إنشاء قواعد جديدة)
     - Width: تعيين سمك الخط
     - Routing Via Style: تعيين قواعد الفتحة
     - تغطية النحاس:؟

### مكتبة الرسم البياني

تحتاج إلى المزيد من المعلومات ...

### مكتبة التعبئة والتغليف

- قياس المسافة: **Ctrl + N**
- تبديل الوحدات (بوصة / ملم): **Q**

## العملية والمعايير

تصميم لوحة دائرة كهربائية من الصفر يتبع العملية الأساسية التالية:

1. البدء
   1. إنشاء مشروع جديد
   2. إنشاء مخطط و PCB داخل المشروع
2. رسم المخطط
   1. التأكد من تجميع المخطط بنجاح بعد الانتهاء من الرسم
3. رسم PCB
   1. استيراد التغييرات من المخطط
   2. إخفاء علامات Designator للعناصر
      1. فتح لوحة Properties على اليمين
      2. النقر على الرمز الذي يشبه العين بجوار Designator لإخفاءه
   3. رسم شكل اللوحة
      - تبديل الاتجاه بزاوية 90°/45° (Shift+Space)
      - تعريف اللوحة بالشكل المرسوم (DSD)
      - تعيين خصائص الإطار على طبقة الميكانيكية 1
      - ثقوب ثابتة
        - ثقوب M3: داخلي بمقاس 3.1 ملم، خارجي بمقاس 4 ملم
   4. ترتيب العناصر
      - الانتقال إلى المقالة [PCB ترتيب العناصر القياسي](](https://wiki-power.com/ar/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. توصيل الأسلاك
      - تعيين قواعد توصيل الأسلاك
        - الرجوع إلى [PCB قواعد توصيل الأسلاك القياسية](](https://wiki-power.com/ar/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - عدم تفعيل التوصيل التلقائي!
      - تفعيل خاصية القطرة المتساقطة
   6. تعليمات الخط (علامات الأقدام / حقوق النشر / النصوص المضللة)
      - وضعها على طبقة الطباعة (الطبقة العلوية / الطبقة السفلية)
      - إذا وضعت على الطبقة السفلية، يجب تعكسها أولاً
   7. تطبيق النحاس (PG)
      - الرجوع إلى [PCB قواعد توصيل الأسلاك القياسية](](https://wiki-power.com/ar/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. إنتاج اللوحة
   1. حفظ المشروع
   2. ضغط ملف .pcb (إذا كان ذلك ممكنًا، يمكن تصدير Gerber)
   3. تحميل الملف المضغوط على مساعد الطلب الخاص بـ JiaLiChuang
   4. (اختياري SMT)

## معلومات أخرى

### خصائص العنصر

- Designator: رقم العنصر، وهو علامة فريدة للعنصر يستخدم لتحديد العناصر المختلفة في المخطط
  - R: مقاومة
  - RN: مقاومة متعددة
  - C: سعة
  - J: واجهة / كابل
  - X: كريستال
  - D: ديود
  - Q أو T: ترانزستور
  - FB: حبة مغناطيسية
  - U: رقاقة
  - TP: نقطة الاختبار
- Comment: معلمة حجم العنصر، مثل قيمة المقاومة أو السعة أو نوع رقاقة IC
- Description: يستخدم لتوضيح وظيفة العنصر

### إضافة الشعار

الرجوع إلى المقالة [إضافة الشعار](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/) .

### استخدام Git لإدارة المشروع

الرجوع إلى [ملاحظات استخدام Git في AD](](https://wiki-power.com/ar/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

## الخلاصة

هذه هي المعرفة الأساسية لـ Altium Designer وتصميم الدوائر الإلكترونية.  
في الفصل التالي، سنبدأ في تصميم المخطط الأساسي.

## المراجع والشكر

Translated by: @MajdAlbukhari

- [Altium شركة Altium Designer الخاصة](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [جياليتشوانج SMT قائمة اللصق القابلة للتطبيق PADS مكتبة الدمج \ (الإصدار الرسمي)](http://club.szlcsc.com/article/details_2757_1.html)
- [Altium Designer استخدام Git الفكرة](https://blog.csdn.net/weifengdq/article/details/78406438)
- [استخدام التحكم في الإصدارات](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.