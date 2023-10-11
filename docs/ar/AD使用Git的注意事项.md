# ملاحظات حول استخدام Git في AD

## إدارة المشروع باستخدام Git

يدعم Altium Designer استخدام Git/SVN للتحكم في الإصدارات. إذا كنت تستخدم Git، يمكنك إنشاء مستودع Git مباشرة في مسار المشروع. بعد إعادة تشغيل Altium Designer، سترى حالة الإصدارات بجانب شجرة الملفات:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200421100348.png)

تعني الرموز التوضيحية ما يلي:
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200421101221.png)

يمكنك القيام بعمليات Git مباشرة من القائمة "المشروع (C) - التحكم في الإصدارات (E)"، ويمكنك حتى إرسال التعديلات مباشرة إلى GitHub.

## ملف .gitignore

عند استخدام Altium Designer، يقوم البرنامج بإنشاء بعض الملفات المؤقتة (مثل مجلد "History")، وهذه الملفات لا تؤثر فقط على سرعة الإرسال، بل تلوث أيضًا سجل الإرسال. في هذه الحالة، يجب استخدام ملف `.gitignore` لتجاهل هذه الملفات المؤقتة.

يحتوي ملف `.gitignore` المناسب لـ Altium Designer على المحتويات التالية:

```gitignore
# ============================= Projects =============================
*.DesWrk
# Altium Workspace

*.DsnWrk
# Altium Project Group

!*.LibPkg
# Altium Inegrated Library Package

*.PrjGrp
# Altium Project Group

!*.PrjMbd
# Altium Muti-board Design Project

!*.PrjPcb
# Altium PCB Project

*.PrjScr
# Altium Script Project

*.PrjPCBStructure

# ============================= Schematic =============================
*.Dot
# Altium Schematic Template

!*.MbsDoc
# Altium Multi-board Schematic

!*.Sch
# Altium Schematic Document

!*.SchDoc
# Altium Schematic Document

*.SchDot
# Altium Schematic Template

!*.SchLib
# Altium Schematic Library

# ============================= PCB =============================
!*.MbaDoc
# Altium Multi-board Assembly

!*.Pcb
# Protel PCB Document

!*.PcbDoc
# Altium PCB Document

!*.PcbLib
# Altium PCB Library

# ============================= Libraries =============================
*.CmpLib
# Altium Component Library

!*.IntLib
# Altium Compiled Library

!*.Lib
# Altium Library

*.PvLib
# Altium Pad Via Library

# ============================= CAMtastic =============================
*.Apr
# CAMtastic Aperture Data

*.Apt
# CAMtastic Aperture Data

*.Cam
# Altium CAMtastic Document

*.Drl
# CAMtastic NC Drill Binary Data
```

# ============================= جيربر =============================

\*.G[1-30]

# بيانات جيربر لطبقة CAMtastic 1-30

# ============================= المخرجات =============================

\*.Drc

# تقرير فحص القواعد التصميمية

\*.Drr

# ملف تقرير الحفر NC لبرنامج Altium

\*.Net

# ملف قائمة الشبكات لبرنامج Altium

\*.Nsx

# مستند قائمة الشبكات للمحاكاة

\*.OutJob

# ملف وظيفة الإخراج لبرنامج Altium

\*.Rep

# ملف تقرير

\*.Rpt

# ملف تقرير

# ============================= النصوص البرمجية =============================

\*.Bas

# مستند نص برمجي لبرنامج Altium

\*.SrcDoc

# مستند نص برمجي لبرنامج Altium

\*.Tcl

# مستند نص برمجي لبرنامج Altium

# ============================= المحاكاة =============================

\*.Ckt

# دائرة فرعية للمحاكاة

\*.LaxAn

# ملف تحليل منطقي تناظري

\*.LaxDig

# ملف تحليل منطقي رقمي

\*.Mdl

# نموذج المحاكاة

\*.Pld

# ملف CUPL PLD

\*.Pwl

# وصف خطي قطعي للمحاكاة

\*.Sdf

# ملف بيانات المحاكاة لبرنامج Altium

\*.Si

# ملف إدخال المحاكاة CUPL

\*.So

# ملف موجات رقمية

# ============================= المجلدات =============================

\_\_Previews/

History/

Project Logs for \*/

# ============================= أخرى =============================

\*.BomDoc

# مستند BOM

\*.DBLib

# ملف مكتبة قاعدة البيانات لبرنامج Altium

\*.DBLink

# ملف رابط قاعدة البيانات لبرنامج Altium

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
