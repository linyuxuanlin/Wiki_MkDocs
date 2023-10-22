# AD Basic Operations - Fundamentals

- Altium Designer Tutorial Series

## Background

After configuring the software environment, it is essential to familiarize ourselves with some basic knowledge of Altium Designer and circuit design before starting to create PCBs.

## Library File Installation

Libraries are like enclosures for each discrete component (e.g., resistors, capacitors), making them readily accessible. Not every component's schematic/library has to be created from scratch, but **organizing your own libraries is a must**. Imagine if every component in your project comes from others (and different libraries have their own rules), you will increasingly be constrained by others. Having your own library is not only convenient for migration and efficiency but also promotes systematic knowledge. According to the timeline, knowledge growth will be exponential. While the initial growth curve may be slow, later on, there won't be repetitive work. At that point, all you need to do is learn new knowledge and incorporate it into your system.

Friendly reminder: Try to extract all the components your project needs from your organized schematic/library.

### Reference Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): A library I've organized. It has comprehensive packaging libraries, and its schematic library only includes the component models required for my projects. It's continuously updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively comprehensive library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite comprehensive library, including some microcontroller solution boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): A standard integrated library provided by Jialichuang, including all the components that Jialichuang can SMT. Using this integrated library ensures good compatibility when making PCBs or SMT.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): Organized by Bin, this schematic/library covers most of the components required by the hardware team.

How to install library files: Refer to [**Altium Designer Library Installation**](https://wiki-power.com/ar/AltiumDesigner Library Installation)

### Uncommon Components

The provided libraries already cover over 95% of component models available in the market. If you can't find the component you need, you can try the following methods:

AD Plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This is incredibly convenient to use.

Search Engines: [**Schematic and Packaging Downloads · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Keyboard Shortcuts

For Altium Designer, mastering common keyboard shortcuts can significantly improve efficiency. Altium Designer's system shortcuts are composed of letter combinations with underscores based on menu command names. For example, the shortcut for **Place-Line** is **P-L** (press P first and then L).

### Schematic

Certainly, here is the text translated into Arabic while maintaining the original markdown format:

```markdown
- عرض لوحة المكتبة: **PP**
- رسم الأسلاك: **Ctrl + W**
- رسم علامات الشبكة: **PN**
- نسخ العناصر وتحديث الترقيم تلقائيًا: **اضغط Shift + اسحب**
- ترقيم الصفحة: **TAT**
- ترقيم العناصر تلقائيًا: **TAA**
  - إعادة تعيين الكل: إعادة تعيين جميع أرقام العناصر لتصبح "حرف + ؟" 
  - تحديث قائمة التغييرات: تغيير ترقيم العناصر في القائمة
  - قبول التغييرات (إنشاء تعديل هندسي): تأكيد تغييرات الترقيم وتنفيذ تعديلات على المخطط الأصلي
- إنشاء جدول مستندات القائمة (BOM): **RI**
- تحديث لوحة الدوائر المطبوعة (PCB): **DU**
- محاذاة إلى اليسار (أو اليمين): **AL** (أو **AR**)

### لوحة الدوائر المطبوعة (PCB)

- استيراد التغييرات من المخطط الأصلي إلى لوحة الدوائر المطبوعة: **DI**
- استبدال التغييرات في لوحة الدوائر المطبوعة بالمخطط الأصلي: **DU**
- تبديل وحدات القياس (بوصة/مليمتر): **Q**
- تدوير العناصر (بأي زاوية): **EMO**
- وضع العناصر في الطبقة السفلية: **اسحب مع الضغط على L**
- تخطيط تلقائي: **حدد واسحب مع الضغط على TOL**
- تحديد نقطة البداية للإحداثيات: **EOS**
- تعيين الشبكة: **G**
- توصيل التوصيلات تلقائيًا: **UAA**
- مسح التوصيلات: **UUA**
- تمييز الأسلاك: **اضغط Shift وانقر على السلك**
- تمييز الأسلاك المتصلة بالنقاط: **اضغط Ctrl وانقر بزر الفأرة الأيسر على النقطة**
- عكس الأفقي: **Ctrl + F**
- قياس: **Ctrl + M**
- تبديل العرض (ثنائي/ثلاثي الأبعاد): **2 / 3**
- تدوير في العرض ثلاثي الأبعاد: **اضغط Shift واسحب**
- مسح الفلاتر: **Shift + C**
- تبديل عرض الطبقات (طبقة واحدة/عدة طبقات): **Shift + S**
- تغطية الفتحات باللحام (يمكن تجاهلها واختيارها مباشرة أثناء الإنتاج)
  1. انقر مرتين على أي فتحة
  2. انقر بزر الماوس الأيمن - ابحث عن كائنات مماثلة
  3. حدد خاصية الحجم كـ مماثلة، وقم بتأكيد الاختيار لتحديد جميع الفتحات
  4. في خاصية التوسيع لطبقة اللحام، حدد الجزء العلوي والجزء السفلي
- تعيين قواعد التصميم
  1. **UAA**
  2. أنشئ استراتيجية جديدة وحرر القواعد
  3. تعديل قواعد التوجيه في التصميم (إنشاء قاعدة جديدة)
     - العرض: تعيين عرض السلك
     - نمط الفتحات: تعيين قواعد الفتحات
     - تصفيح: ؟

### مكتبة المخطط الكهربائي

تحتاج إلى التحقق...

### مكتبة الحاويات (الأشكال)

- قياس المسافة: **Ctrl + N**
- تبديل وحدات القياس (بوصة/مليمتر): **Q**

## العمليات والمعايير

تصميم الدوائر الإلكترونية من البداية حتى النهاية يشمل الخطوات التالية:
```

Please note that I've provided the translation in Arabic within the original markdown structure.

Here is the translated text in Arabic:

```markdown
1. البدء
   1. إنشاء مشروع جديد
   2. إنشاء رسم تخطيطي وملف PCB داخل المشروع
2. رسم الرسم التخطيطي
   1. تأكد من التحقق من البرمجة بعد الانتهاء
3. رسم PCB
   1. استيراد التغييرات من الرسم التخطيطي
   2. إخفاء علامات المرجع Designator
      1. افتح لوحة الخصائص على الجانب الأيمن **Properties**
      2. انقر على الرمز **العين** بجوار **Designator** لإيقاف التشغيل
   3. رسم شكل اللوحة
      - تبديل زوايا الأسلاك 90°/45° (**Shift+Space**)
      - تعريف اللوحة بالشكل المرسوم (**DSD**)
      - **تعيين خصائص اللوحة للطبقة الميكانيكية 1**
      - ثقب ثابت
        - ثقب M3: الداخلي **3.1** ملم، الخارجي **4** ملم
   4. ترتيب المكونات
      - انتقل إلى المقالة [**مواصفات ترتيب المكونات في PCB**](to_be_replace[3])
   5. تمرير الأسلاك
      - تعيين قواعد تمرير الأسلاك
        - انظر إلى [**مواصفات تمرير الأسلاك في PCB**](to_be_replace[3])
      - **لا تقم بتشغيل التمرير التلقائي!**
      - **قم بتشغيل ميزة البكاء (Tear Drop)**
   6. وضع العلامات بالخط (علامات دبوس / حقوق الملكية / نص مضلل)
      - ضعها في طبقة الطباعة (الجزء العلوي / الجزء السفلي)
      - إذا وُضعت في الجزء السفلي، يجب أن تكون معكوسة أولاً
   7. تطبيق التوصيلات النحاسية (**PG**)
      - انظر إلى [**مواصفات تمرير الأسلاك في PCB**](to_be_replace[3])
4. تصنيع اللوحة
   1. احتفظ بالمشروع
   2. ضغط على ملف **.pcb** (على الرغم من أن هذا قد لا يكون صحيحًا، يمكنك تصدير Gerber إذا كنت تستطيع)
   3. قم برفع الملف إلى مساعد طلبات JLCPCB
   4. (اختياري SMT)

## معلومات إضافية

### خصائص المكونات

- **Designator**: رمز المكون، وهو الرمز الفريد للمكون يُستخدم لتمييز المكونات المختلفة في الرسم التخطيطي
  - **R**: مقاومة
  - **RN**: مقاومة مصفوفة
  - **C**: مكثف
  - **J**: واجهة / ربط
  - **X**: مذبذب
  - **D**: صمام ثنائي
  - **Q** أو **T**: مكون ثلاثي
  - **FB**: حبة مغناطيسية
  - **U**: رقاقة
  - **TP**: نقطة اختبار
- **Comment**: معاملات المكونات مثل مقاومة المقاومة، سعة المكثف، ونموذج رقاقة IC
- **Description**: تُستخدم لكتابة وصف وظيفة المكون

### إضافة شعار (Logo)

انتقل إلى المقالة [**إضافة شعار (Logo)**](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/).

### إدارة المشروع باستخدام Git

راجع [**ملاحظات استخدام Git في AD**](to_be_replace[3]) للتفاصيل.

## ختاماً

هذه هي المعرفة الأساسية لبرنامج Altium Designer وتصميم الدوائر.  
في الفصل التالي، سنبدأ في تصميم الرسم التخطيطي.
```

Please note that I've retained the original markdown format while providing the translation in an elegant and professional manner.

- [Altium شركة Altium Designer قسم](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [جياليتشوانج SMT لائحة قابلة للصق لمكتبة PADS الرسمية](http://club.szlcsc.com/article/details_2757_1.html)
- [Altium Designer: استخدام Git في التصميم](https://blog.csdn.net/weifengdq/article/details/78406438)
- [استخدام التحكم في الإصدارات](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.