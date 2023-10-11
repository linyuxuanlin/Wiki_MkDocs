# تكوين ونصائح OrCAD

ملاحظة: يستند هذا المقال إلى Cadence OrCAD Capture CIS.

## الأساسيات

يتم استخدام OrCAD Capture CIS لرسم الرسم التخطيطي (القائمة البدء - Cadence - Capture CIS)  
يتم استخدام Allegro PCB Designer لرسم PCB (القائمة البدء - Cadence - PCB Editor)

عمومًا ، يمكن استخدام ملف `.DSN` واحد لتغطية المشروع بأكمله ، وسيتم إنشاء ملفات الرسم التخطيطي `.opj` تلقائيًا عند الفتح. إذا تم استخدام Git لإدارة الإصدارات ، فيمكن إضافة gitignore التالي:

```gitignore
# From original gitignore 

#############
## Allegro
#############

# Ignore log file
*.log
*.log,1
*.log,2
*.log,3

*.dml
*.lst

#ignore 记录操作allegro的事件
*.jrl
*.jrl,1

*.tag

#报告文件
*.rpt

#报告文件
*.cfg
*.cfg,1

*.lck

#报表文件
*.txt
*.txt,1
*.txt,2

#XY数据除外
!place_txt.txt

#DXF导入文件
*.cnv

#Gerber param file除外
!art_param.txt

#Folder
#过滤整个文件夹
/signoise.run/ 

#############
## OrCAD
#############
*.dbk
*.opj
*.DRC
*.DSNlck

#ignore netlist
allegro/ 
```

## بعض الإعدادات

إعدادات DRC:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134720.png)

إعادة تسمية تلقائية للرقم المرجعي عند نسخ المكون:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134747.png)

تحريك النص بالقرب من الشبكة:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210810134758.png)

الفخ: عند استخدام مكتبة CIP ، عندما يتم عرض `not found in the configured librarie lists` ، يجب التحقق من ترميز المسافات في المسار.

- **تكبير / تصغير عجلة الماوس**:`Options` - `Preferences…` - `Pan and Zoom` - تعيين العاملين `Zoom Factor` إلى 1.1 مرة
- **تحديث الرسم التخطيطي عند وضع المكونات**:`Options` - `Preferences…` - `Miscellaneous` - `Place Part` - تحديد `Refresh part on selection`
- **تعيين حجم الشبكة**:`Options` - `Preferences…` - `Grid Display` - `Grid Spacing` - تعيينها على 1/2

## اختصارات لوحة المفاتيح

- سحب الخط: `W`
- إلغاء: `ESC`
- سحب الأسلاك: `F4`
- وضع علامة شبكية: `N`
- تدوير / انعكاس أفقي / انعكاس عمودي للمكون: `R` / `H` / `V`
- فتح لوحة CIS: `Z`
- وضع الطاقة / الأرض: `F` / `G`
- عدم الاتصال: `X`
- مرشح: `Ctrl` + `I`
- تحديد عناصر متعددة: اضغط على `Ctrl` للتحديد
- نسخ وزيادة تلقائية للرقم المرجعي: اضغط على `Ctrl` واسحب المكون
- نقل الرسم التخطيطي حول نقطة التوازن: اضغط على `C` واسحب الماوس
- وضع الحافلة: `E`
- وضع النص: `T`

## الأخطاء والحلول

- لا يمكن سحب المكون: عمومًا ، يمكن حل المشكلة بإعادة التشغيل.

## الحيل

### الفرق بين off-page و port

يستخدم off-page عمومًا في الرسم التخطيطي المسطح ، بينما يستخدم port عمومًا في الرسم التخطيطي الهرمي.

### فحص DRC

1. انقر فوق المشروع بالكامل في شجرة الملفات
2. انقر فوق شريط الأدوات `Tools` - `Design Rules Check...`
3. حدد `Run Physical Rules` و `View Output`
4. انقر فوق موافق ، وسيتم إنشاء تقرير وفتحه تلقائيًا

## المراجع والشكر

- [【دليل سريع لـ Cadence】الإصدار الشامل للمقالة](https://blog.csdn.net/ReCclay/article/details/101225359)
- [دليل OrCAD Capture](https://resources.orcad.com/orcad-capture-tutorials)
- [حل مشكلة ضبابية الخط في برنامج Cadence على شاشات الحواسيب المحمولة عالية الدقة](https://blog.csdn.net/qq_34338527/article/details/108846792)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
