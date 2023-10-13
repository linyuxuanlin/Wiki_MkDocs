# AD Basic Operations - Basic Knowledge

—— Altium Designer Tutorial Series

## Background

Before starting to design a PCB, it is essential to familiarize oneself with some basic knowledge of Altium Designer and circuit design.

## Library Installation

A library is a collection of schematic/PCB footprints for each discrete component (such as resistors, capacitors, etc.), making it easy to call them directly. It is not necessary to create schematic/footprint libraries for every component, but **organizing your own library is a must**. Imagine if every component in your project uses someone else's library (and different libraries have their own rules), then you will be more and more restricted. Having your own library not only facilitates migration and improves efficiency, but also helps to systematize knowledge. With your own rules and system, knowledge will grow exponentially over time. Although the growth curve is slow at the beginning, there will be no repetitive work in the later stages. All you need to do is learn new knowledge and integrate it into the system.

Friendly reminder: Try to extract all the components needed for your project from your own organized schematic/footprint library.

### Reference Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): A library I organized myself. The footprint library is complete, and the schematic library only includes the component models needed for my project. It is constantly being updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively complete library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite comprehensive library, including some MCU solution boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): A standard integrated library provided by Jia Li Chuang, including all components that can be SMT mounted by Jia Li Chuang. Using this integrated library will ensure better compatibility when making PCBs/SMT.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): A schematic/footprint library organized by Bin Ge, covering most of the components needed by the team.

How to install library files: Refer to [**Installing Library Files in Altium Designer**](https://wiki-power.com/ar/Installing Library Files in Altium Designer)

### Uncommon Components

The libraries provided above already cover more than 95% of component models on the market. If you still cannot find the required components, you can try the following methods:

AD plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This is really convenient to use.

Search engine: [**Schematic and Footprint Download · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Shortcuts

For Altium Designer, mastering commonly used shortcuts can greatly improve efficiency. The system shortcuts of Altium Designer are composed of letters with underlines in the commands under the menu. For example, the shortcut for **Place-Line** is **P-L** (press P first and then L).

### Schematic

- عرض لوحة المكتبة: **PP**
- رسم الأسلاك: **Ctrl + W**
- رسم علامات الشبكة: **PN**
- نسخ المكونات وتحديث الرقم التسلسلي تلقائيًا: **اضغط Shift + اسحب**
- ترقيم الرسم البياني: **TAT**
- ترقيم المكونات تلقائيًا: **TAA**
  - إعادة تعيين الكل: إعادة تعيين جميع أرقام المكونات لتصبح بتنسيق "حرف +؟"
  - تحديث قائمة التغييرات: تغيير أرقام المكونات في القائمة
  - قبول التغييرات (إنشاء ECO): تعني قبول تغييرات الأرقام وتنفيذ تغييرات الرسم البياني الأصلي
- إنشاء جدول BOM: **RI**
- تحديث PCB: **DU**
- محاذاة إلى اليسار (اليمين): **AL** (**AR**)

### PCB

- استيراد التغييرات من الرسم البياني إلى PCB: **DI**
- استيراد التغييرات من PCB إلى الرسم البياني: **DU**
- تبديل الوحدة (بوصة / ملم): **Q**
- تدوير المكونات (بأي زاوية): **EMO**
- وضع المكونات على الطبقة السفلية: **اسحب واضغط L**
- تخطيط تلقائي: **تحديد و TOL**
- تعيين نقطة البداية: **EOS**
- تعيين الشبكة: **G**
- توصيل تلقائي: **UAA**
- مسح التوصيل: **UUA**
- تسليط الضوء على الأسلاك: **اضغط Shift + حرك المؤشر على السلك**
- تسليط الضوء على الأسلاك المتصلة بالعقدة: **اضغط Ctrl + انقر بزر الفأرة الأيسر**
- الانعكاس الأفقي: **Ctrl + F**
- القياس: **Ctrl + M**
- تبديل العرض (2D / 3D): **2/3**
- تدوير في العرض ثلاثي الأبعاد: **اضغط Shift + اسحب**
- مسح المرشح: **Shift + C**
- تبديل العرض الأحادي / المتعدد: **Shift + S**
- غطاء الثقب (يمكن تجاهله ، يمكن اختياره مباشرة عند إنشاء اللوحة)
  1. انقر فوق ثقب معين
  2. انقر بزر الماوس الأيمن - البحث عن كائنات مماثلة
  3. حدد خاصية الحجم كـ Same ، ثم اختر جميع الثقوب
  4. في توسيع قناع اللحام في الخصائص ، حدد الطبقة العلوية والطبقة السفلية
- تعيين قواعد التوصيل
  1. **UAA**
  2. إنشاء استراتيجية وتحرير القواعد
  3. تعديل القواعد في Routing (إنشاء قواعد جديدة)
     - العرض: تعيين سمك الخط
     - Routing Via Style: تعيين قواعد الثقوب
     - التصفيح:؟

### مكتبة الرسم البياني

تحتاج إلى المزيد من المعلومات ...

### مكتبة التغليف

- قياس المسافة: **Ctrl + N**
- تبديل الوحدة (بوصة / ملم): **Q**

## العملية والمعايير

يتم تصميم لوحة الدائرة الكهربائية من الصفر ، ويتم تنفيذ العملية الأساسية على النحو التالي:

1. التهيئة
   1. إنشاء مشروع جديد
   2. إنشاء مخطط وملف PCB داخل المشروع
2. رسم المخطط
   1. التأكد من تجميع المخطط بنجاح بعد الانتهاء من الرسم
3. رسم PCB
   1. استيراد التغييرات من المخطط
   2. إخفاء علامات تحديد العناصر
      1. فتح لوحة الخصائص على اليمين
      2. النقر على العلامة المجاورة لـ "علامة التحديد" ، وسيتم إغلاقها
   3. رسم شكل اللوحة
      - تبديل الأسلاك بزاوية 90 درجة / 45 درجة (Shift + Space)
      - تعريف اللوحة بالشكل المرسوم (DSD)
      - تعيين خصائص الإطار على طبقة الميكانيكية 1
      - ثقب ثابت
        - ثقب برغي M3: داخلي 3.1 مم ، خارجي 4 مم
   4. ترتيب العناصر
      - انتقل إلى المقالة [**PCB تخطيط العناصر الكهربائية**](https://wiki-power.com/ar/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. تمديد الأسلاك
      - تعيين قواعد تمديد الأسلاك
        - انظر [**PCB قواعد تمديد الأسلاك**](https://wiki-power.com/ar/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - **لا تفعل التمديد التلقائي!**
      - **تفعيل وظيفة القطرة الدمعية**
   6. تحديد الخطوط (علامات الأقدام / حقوق النشر / النصوص المضللة)
      - وضعها على طبقة الطباعة (الطبقة العلوية / الطبقة السفلية)
      - إذا كانت على الطبقة السفلية ، يجب تعكسها أولاً
   7. تطبيق النحاس (PG)
      - انظر [**PCB قواعد تمديد الأسلاك**](https://wiki-power.com/ar/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)

4. صنع اللوحة
   1. حفظ المشروع
   2. ضغط ملف **.pcb** (إذا كان ذلك ممكنًا ، يمكن تصدير Gerber)
   3. تحميله على **JLCPCB**
   4. (اختياري SMT)

## معلومات أخرى

### خصائص العنصر

- **Designator**: رقم العنصر ، وهو معرف فريد للعنصر ، يستخدم لتحديد العناصر المختلفة في المخطط الكهربائي
  - **R**: مقاومة
  - **RN**: مقاومة متسلسلة
  - **C**: سعة
  - **J**: واجهة / كابل
  - **X**: كريستال
  - **D**: ديود
  - **Q** أو **T**: ثلاثي الأقطاب
  - **FB**: حبة مغناطيسية
  - **U**: رقاقة
  - **TP**: نقطة الاختبار
- **Comment**: معلمة حجم العنصر ، مثل قيمة المقاومة وسعة الكابل ونوع رقاقة IC
- **Description**: يستخدم لتعريف وظيفة العنصر

### إضافة الشعار

انتقل إلى المقالة [**إضافة الشعار**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/) .

### استخدام Git لإدارة المشروع

انظر [**ملاحظات استخدام Git في AD**](https://wiki-power.com/ar/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9)

## خلاصة

هذه هي المعرفة الأساسية لـ Altium Designer وتصميم الدوائر الكهربائية.  
في الفصل التالي ، سنبدأ في تصميم المخطط الكهربائي.

## المراجع والشكر

- [Altium شركة Altium Designer العمود الخاص بها](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [جياليتشوانغ SMT قائمة اللصق المتكاملة PADS \ (الإصدار الرسمي)](http://club.szlcsc.com/article/details_2757_1.html)
- [Altium Designer استخدام Git الفكرة](https://blog.csdn.net/weifengdq/article/details/78406438)
- [استخدام التحكم في الإصدارات](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.