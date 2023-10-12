# TinyDVR - صغير الحجم ومحمل بالقوة

- استنادًا إلى TinyDVR Master V1.1 & Slave V7.2 Release

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191345.jpg)

TinyDVR هو مجموعة تشغيل محركات كهربائية تحتوي على لوحة أم (Master) ولوحة فرعية (Slave) ، حيث يتم فصل جزء التشغيل عن جزء الطاقة ، ويتم تقليل الحجم بشكل كبير مقارنةً بالسابق ZenDriver ، مما يزيد من قابلية التوسع. يمكنك تراكم عدد مختلف من اللوحات الفرعية وتشغيل n محركات وفقًا لاحتياجاتك.

مستودع المشروع: [**linyuxuanlin/TinyDVR**](https://github.com/linyuxuanlin/TinyDVR)

معاينة المشروع عبر الإنترنت:

**TinyDVR_Master**:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Master.zip"
  ></div>
</div>

**TinyDVR_Slave**:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Slave.zip"
  ></div>
</div>

## المعلمات الأساسية

1. الجهد المدخل: **7.2 ~ 20 V**
2. تيار الإخراج: **0 ~ 68 A**
3. يوفر مخرج طاقة **5V / 3A** لتشغيل المتحكمات والوحدات الأخرى
4. جهاز حماية: دوائر حماية مدمجة للحماية من الانعكاس والعزل الضوئي
5. توصيل محركات كهربائية بسيط: يمكن توصيل محركات التروس المباشرة الشائعة في السوق (مع محرك الترميز) مباشرةً باستخدام كابلات الربط ذات 6 دبابيس (دون الحاجة إلى توصيل الأسلاك)
6. قابل للتوسع: يمكن تراكم لوحة أم واحدة مع n لوحات فرعية لتشغيل n محركات كهربائية

## تعريف الواجهة

### TinyDVR Master

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191439.png)

### TinyDVR Slave

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191457.png)

تفسير دبوس الخلفية:

- \+ : يوفر مخرج طاقة 5V / 3A
- 1: منفذ IN1 ، يدخل إشارة PWM 1
- 2: منفذ IN2 ، يدخل إشارة PWM 2
- A: منفذ إشارة المرحلة A لمحرك الترميز
- B: منفذ إشارة المرحلة B لمحرك الترميز
- \- : GND

## دليل الاستخدام

### طريقة الاختبار

1. توصيل الطاقة من البطارية **7.2 ~ 20 V**
2. توصيل المحرك في اللوحة الفرعية المناسبة
3. توصيل مخرج الطاقة **5V** بمنافذ **IN1 / IN2** على التوالي ، وسيتم تشغيل المحرك بالترتيب **إيجابي / عكسي**

### توصيل الميكروكنترولر

4. توصيل الطاقة من البطارية **7.2 ~ 20 V**
5. توصيل المحرك في اللوحة الفرعية المناسبة
6. توصيل الأرضي المشترك (توصيل GND لوحة التشغيل بـ GND الميكروكنترولر)
7. توصيل منافذ IN1 و IN2 بمنافذ PWM المناسبة في الميكروكنترولر (تعيين الكود)
8. طريقة الاختبار: يرجى الرجوع إلى مثال الاختبار في مستودع المشروع

## خلف الكواليس

لوحة فرعية في وقت سابق:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182442.jpg)

لحام الكميات الكبيرة:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182441.jpg)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.