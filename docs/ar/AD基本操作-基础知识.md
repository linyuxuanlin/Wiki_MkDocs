# AD Basic Operations - Fundamental Knowledge

— Altium Designer Tutorial Series

## Background

After configuring the software environment, it is essential to familiarize ourselves with some basic knowledge about Altium Designer and circuit design before we start creating PCBs.

## Library File Installation

Libraries are like encapsulations of individual components (such as resistors, capacitors, etc.) that make it easy to use them directly. Not every component's schematic or package library needs to be created from scratch, but **organizing your own library is a must**. Imagine if every component in your project is from different sources, each with its own rules; you'll find yourself restricted. Having your library not only makes migration and efficiency better but also helps organize knowledge. Adhering to your rules and system, knowledge will grow exponentially over time. Initially, the growth curve may be slow, but in the later stages, there won't be repetitive work. All you'll need to do then is learn new knowledge and integrate it into your system.

Friendly advice: Extract all the components you need for your project from your organized schematic and package libraries.

### Recommended Libraries

- [**Power_Lib_Altium**](https://github.com/linyuxuanlin/Power_Lib_Altium): My own organized library. It has comprehensive package libraries, and the schematic library only includes component models needed for my projects. Continuously updated.
- [**AltiumDesigner_PcbLibrary**](https://github.com/KitSprout/AltiumDesigner_PcbLibrary): A relatively comprehensive library.
- [**My_PCB_Library_Github**](https://github.com/Samwuzhitao/My_PCB_Library_Github): A quite comprehensive library, including some microcontroller solution boards.
- [**JLCSMT_LIB**](https://gitee.com/JLC_SMT/JLCSMT_LIB): Jialichuang's standard integrated library, containing all components that Jialichuang can SMT solder. Using this integrated library ensures good compatibility when making boards or SMT.
- [**Hare_Library**](https://github.com/linyuxuanlin/Power_Lib_Altium/tree/master/Other_Libs/Hare_Library): Bin's organized schematic and package libraries cover most components needed for the hardware team.

How to install library files: Refer to [**Altium Designer Library Installation**](https://wiki-power.com/AltiumDesigner%E5%AE%89%E8%A3%85%E5%BA%93%E6%96%87%E4%BB%B6)

### Uncommon Components

The libraries provided above already cover over 95% of the component models available in the market. If you can't find the component you need, you can try the following methods:

AD Plugins:

- [**Altium Library Loader**](https://www.samacsys.com/altium-designer-library-instructions/): This one is really convenient to use.

Search Engine: [**Schematic and Package Downloads · Power's NAV**](https://nav.wiki-power.com/#87696a153c91c609c4c595e421e880ae)

## Shortcuts

For Altium Designer, mastering common shortcuts can significantly enhance your efficiency. The system shortcuts in Altium Designer are composed of letter combinations with underscores from menu commands, e.g., the shortcut for **Place-Line** is **P-L** (press P and then L).

### Schematic

Here is the translated text in Arabic:

```markdown
- عرض لوحة المكتبة: **PP**
- رسم الأسلاك: **Ctrl + W**
- رسم علامات الشبكة: **PN**
- نسخ العناصر وتحديث الأرقام تلقائيًا: **اضغط Shift + اسحب**
- ترقيم الرسوم البيانية: **TAT**
- ترقيم العناصر تلقائيًا: **TAA**
  - إعادة تعيين الكل: إعادة تعيين جميع أرقام العناصر لتصبح "حرف + ؟" شكل
  - تحديث قائمة التغييرات: تغيير ترقيم العناصر في القائمة
  - قبول التغييرات (إنشاء ECO): القبول لتغيير ترقيم العناصر وتنفيذ التغييرات في المخطط الأصلي
- إنشاء جدول BOM: **RI**
- تحديث PCB: **DU**
- محاذاة إلى اليسار (أو اليمين): **AL** (أو **AR**)

### PCB

- استيراد التغييرات من المخطط الأصلي إلى PCB: **DI**
- استبدال التغييرات من PCB إلى المخطط الأصلي: **DU**
- تغيير الوحدات (بوصة / ملم): **Q**
- دوران العناصر (بزوايا مختلفة): **EMO**
- وضع العناصر على الطبقة السفلية: **اسحب مع الضغط على L**
- تخطيط تلقائي: **تحديد مستطيلي + TOL**
- تعيين نقطة الأصل للإحداثيات: **EOS**
- تعيين الشبكة: **G**
- تمديد التوصيل تلقائيًا: **UAA**
- مسح التوصيل: **UUA**
- تسليط الضوء على الأسلاك: **اضغط Shift + انتقل بالمؤشر إلى السلك**
- تسليط الضوء على الأسلاك المتصلة بالنقاط: **اضغط Ctrl + انقر بزر الماوس الأيسر على النقطة**
- انعكاس أفقي: **Ctrl + F**
- قياس: **Ctrl + M**
- تبديل العرض (ثنائي / ثلاثي الأبعاد): **2 / 3**
- دوران في عرض ثلاثي الأبعاد: **اضغط Shift + اسحب**
- مسح المرشحات: **Shift + C**
- تبديل عرض الطبقة (طبقة واحدة / متعددة الطبقات): **Shift + S**
- إخفاء التمرير (اختياري، يمكن اختياره أثناء تصنيع اللوحات)
  1. انقر مرة على فتحة تمرير معينة
  2. انقر بزر الماوس الأيمن - البحث عن كائن مشابه
  3. حدد الحجم كما هو مطلوب في خصائص الفتحة لتحديد جميع الفتحات المماثلة
  4. في خصائص الواقي الكيميائي، حدد الجزء العلوي والجزء السفلي
- تعيين قواعد الاتصال
  1. **UAA**
  2. إنشاء استراتيجية جديدة وتحرير القواعد
  3. تعديل القواعد في التوجيه (إنشاء قواعد جديدة)
     - العرض: تحديد عرض السلك
     - نمط الفتحة في التوجيه: تحديد قواعد الفتحة
     - التوصيل بالنحاس: ؟

### مكتبة المخطط الكهربائي

تحتاج إلى المزيد من المعلومات...

### مكتبة التعبئة والتغليف

- قياس المسافة: **Ctrl + N**
- تغيير الوحدات (بوصة / ملم): **Q**

## العمليات والمعايير

تصميم لوحة دوائر إلكترونية من البداية إلى النهاية يتضمن العمليات الأساسية التالية:
```

1. البدء
   1. إنشاء مشروع جديد
   2. إنشاء مخطط وملف PCB داخل المشروع
2. رسم المخطط
   1. تأكد من أنه بعد الانتهاء يتم الترجمة بنجاح
3. رسم PCB
   1. استيراد التغييرات من المخطط
   2. إخفاء علامة تصنيف العنصر "Designator"
      1. افتح اللوحة الجانبية "الخصائص" من الجهة اليمنى
      2. انقر على العلامة "عين" بجوار "Designator" لإيقاف تشغيلها
   3. رسم شكل اللوحة
      - تغيير زاوية الأسلاك إلى 90°/45° (Shift+Space)
      - تحديد شكل اللوحة بناءً على الشكل المرسوم (DSD)
      - تعيين خصائص اللوحة كطبقة ميكانيكية 1
      - ثقب ثابت
        - ثقب M3: داخلي بقطر 3.1 مم وخارجي بقطر 4 مم
   4. ترتيب العناصر
      - راجع [مواصفات ترتيب عناصر PCB](https://wiki-power.com/PCB%E5%85%83%E4%BB%B6%E5%B8%83%E5%B1%80%E8%A7%84%E8%8C%83)
   5. تمديد الأسلاك
      - تعيين قواعد تمديد الأسلاك
        - انظر [مواصفات تمديد الأسلاك في PCB](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
      - لا تقم بتشغيل التمديد التلقائي!
      - قم بتفعيل وظيفة التلامس (التيرمينال)
   6. تسمية الخطوط والعلامات (علامات الأقدام / حقوق النشر / نصوص ملفات مرجعية)
      - ضعها على الطبقة العلوية أو السفلية
      - إذا وُضعت على الطبقة السفلية، يجب أن تتم عملية انعكاسها أولاً
   7. تطبيق النحاس (PG)
      - انظر [مواصفات تمديد الأسلاك في PCB](https://wiki-power.com/PCB%E5%B8%83%E7%BA%BF%E8%A7%84%E8%8C%83)
4. تصنيع اللوحة
   1. احتفظ بالمشروع
   2. قم بضغط ملف PCB (.pcb) (على الأرجح، يُفضل تصدير Gerber إذا كان ذلك ممكنًا)
   3. قم بتحميل الملف المضغوط إلى مساعد الطلب في جياليتشوانغ
   4. (اختياري SMT)

## معلومات إضافية

### خصائص العناصر

- **Designator**: العلامة التجارية للعنصر، وهي تُستخدم لتمييز العناصر المختلفة في المخطط
  - **R**: المقاومة
  - **RN**: المقاومة المتعددة
  - **C**: المكثف
  - **J**: الواجهة / الربط
  - **X**: الكريستال
  - **D**: الدائيود
  - **Q** أو **T**: الثلاثيات
  - **FB**: البيضاء المغناطيسية
  - **U**: الشريحة
  - **TP**: نقطة الاختبار
- **Comment**: المعلومات الفنية للعنصر، مثل قيمة المقاومة، سعة المكثف، نموذج شريحة IC، وما إلى ذلك
- **Description**: يُستخدم لوصف وظيفة العنصر

### إضافة الشعار

راجع المقالة [إضافة الشعار](https://seujxh.wordpress.com/2018/10/03/logo%E6%B7%BB%E5%8A%A0/).

### إدارة المشروع باستخدام Git

للمزيد من التفاصيل، راجع [توجيهات استخدام Git في AD](https://wiki-power.com/AD%E4%BD%BF%E7%94%A8Git%E7%9A%84%E6%B3%A8%E6%84%8F%E4%BA%8B%E9%A1%B9).

## الختام

هذه هي المعلومات الأساسية حول Altium Designer وتصميم الدوائر الإلكترونية.  
في الفصل التالي، سنبدأ في تصميم المخطط.

- [مقالة عن شركة Altium ومنتجهم Altium Designer](https://seujxh.wordpress.com/2018/09/30/altium%e5%85%ac%e5%8f%b8altium-designer%e4%b8%93%e6%a0%8f/)
- [قائمة الأجهزة التي يمكن تثبيتها في مكونات PADS SMT من Jialichuang (الإصدار الرسمي)](http://club.szlcsc.com/article/details_2757_1.html)
- [فكرة استخدام Git مع Altium Designer](https://blog.csdn.net/weifengdq/article/details/78406438)
- [استخدام نظام التحكم في الإصدارات](https://www.altium.com/documentation/altium-designer/using-version-control-ad)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.