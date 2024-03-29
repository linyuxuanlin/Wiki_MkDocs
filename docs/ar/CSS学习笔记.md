# مذكرات دراسة CSS

## استدعاء

قم بإضافة ورقة أنماط خارجية في العنصر `<head>` من الصفحة HTML:

```html
<link rel="stylesheet" href="xxx.css">
```

حيث `xxx.css` هو ملف CSS في نفس الدليل.  
ملاحظة: حاول دائمًا استخدام **ورقة أنماط خارجية مرتبطة** (كما هو موضح أعلاه).

## محددات

### الصيغة الأساسية

```css
المحدد {
  الخاصية: القيمة;
}
```

### مقارنة بين بعض المحددات

| المحدد   | التعريف                       | الاستدعاء                     | الأسبقية |
| :--------- | :----------------------------- | :----------------------- | :----- |
| محدد الوسم | p {...}                        | &lt;p&gt; ... &lt;/p&gt; | منخفضة     |
| محدد الفئة   | .carrot {...} / p.carrot {...} | class = "carrot"         | متوسطة     |
| محدد الهوية  | \#first {...}                  | id = "first"             | عالية     |

### مجموعة من المحددات

استخدم نفس الأنماط لتعريف عناصر مختلفة.

```css
h1,
h2,
h3 {
  اللون: البحري;
}
```

## الألوان

```css
/* لون النص */
اللون: #56a455;

/* لون الخلفية */
لون الخلفية: أزرق;

/* الشفافية */
/* القيمة تتراوح بين 0.0 و 1.0 */
الشفافية: 0.5;
```

## النص

### حجم الخط

| النمط | النسبة | قيمة EM   |
| :--- | :----- | :------ |
| h1   | 200%   | 2em     |
| h2   | 150%   | 1.5em   |
| h3   | 133%   | 1.125em |
| الجسم | 100%   | 1em     |

```css
/* حجم الخط */
حجم الخط: 200%;
```

### اختيار الخط

ملاحظة: يجب وضع علامات تنص على الخطوط المكونة من كلمات متعددة بين علامتي اقتباس، على سبيل المثال 'Courier New'.

```css
/* اختيار الخط */
/* محلي */
اختيار الخط: "Courier New", Courier, monospace, اسم الخط الخارجي;

/* خارجي */
@font-face {
  اختيار الخط: اسم الخط الخارجي;
  src: url("عنوان الخط الخارجي");
}
```

### تنسيق النص

القيمة الافتراضية هي "عادي".

```css
/* العريض */
سمك الخط: سميك;

/* المائل */
نمط الخط: مائل;

/* حالة الحروف */
/* uppercase، lowercase، capitalize (البداية بحرف كبير) */
تحويل النص: uppercase;

/* تحت الخط */
تزيين النص: underline;

/* خط الوسط */
تزيين النص: line-through;

/* تباعد الأسطر */
تباعد الأسطر: 1.4em;

/* محاذاة */
/* left، right، center، justify (محاذاة النص بالتساوي) */
محاذاة النص: left;
```

### الصفات الوهمية

```css
/* الروابط غير المزورة */
a:link {
  اللون: #ff0000;
}

/* الروابط المزورة */
a:visited {
  اللون: #00ff00;
}

/* تمرير المؤشر على الروابط */
a:hover {
  اللون: #ff00ff;
}

/* الروابط المحددة */
a:active {
  اللون: #0000ff;
}
```

## الصناديق

## القوائم، الجداول والنماذج

تحتاج إلى مزيد من المعلومات

## التخطيط

تحتاج إلى مزيد من المعلومات

## المواصفات

### ترتيب الخصائص

- طريقة العرض والتخطيط
- التموضع
- نموذج الصندوق
  - الهوامش الخارجية
  - الحواف
  - الهوامش الداخلية
- الأبعاد
- أسلوب النص
  - الخطوط
  - النص
  - لون النص
- الخلفية
- التفاصيل
- الشفافية والظل
- الحركة
  - التحولات
  - الرسوم المتحركة
- متفرقات
  - الأصناف الزائفة والعناصر الزائفة
  - الاستشهاد
  - استعلامات الوسائط

### قائمة ترتيب الخصائص

Here's the translated text in Arabic:

```css
[
  [
    "العرض",
    "الرؤية",
    "التعويم",
    "المسح",
    "تدفق",
    "تدفق-أفقي",
    "تدفق-عمودي",
    "القص",
    "التكبير"
  ],
  [
    "تخطيط-الجدول",
    "خلايا-فارغة",
    "موقع-التسمية",
    "تباعد-الحدود",
    "انهيار-الحدود",
    "نوع-أسلوب-القائمة",
    "موقع-أسلوب-القائمة",
    "نوع-أسلوب-القائمة",
    "صورة-أسلوب-القائمة"
  ],
  [
    "الموقع",
    "أعلى",
    "يمين",
    "أسفل",
    "يسار",
    "فهرس-Z"
  ],
  [
    "الهامش",
    "هامش-أعلى",
    "هامش-يمين",
    "هامش-أسفل",
    "هامش-يسار",
    "نمط-صندوق",
    "الحدود",
    "عرض-الحدود",
    "نمط-الحدود",
    "لون-الحدود",
    "حدود-الأعلى",
    "عرض-الحدود-الأعلى",
    "نمط-الحدود-الأعلى",
    "لون-الحدود-الأعلى",
    "حدود-اليمين",
    "عرض-الحدود-اليمين",
    "نمط-الحدود-اليمين",
    "لون-الحدود-اليمين",
    "حدود-الأسفل",
    "عرض-الحدود-الأسفل",
    "نمط-الحدود-الأسفل",
    "لون-الحدود-الأسفل",
    "حدود-اليسار",
    "عرض-الحدود-اليسار",
    "نمط-الحدود-اليسار",
    "لون-الحدود-اليسار",
    "نصف-القطر-للحدود",
    "نصف-القطر-الأعلى-الأيسر",
    "نصف-القطر-الأعلى-الأيمن",
    "نصف-القطر-الأسفل-الأيمن",
    "نصف-القطر-الأسفل-الأيسر",
    "صورة-الحدود",
    "مصدر-صورة-الحدود",
    "تقسيم-صورة-الحدود",
    "عرض-صورة-الحدود",
    "بداية-صورة-الحدود",
    "تحويل",
    "نقطة-الأصل-للتحويل",
    "رسوم-متحركة",
    "اسم-الرسوم-المتحركة",
    "مدة-الرسوم-المتحركة",
    "حالة-تشغيل-الرسوم-المتحركة",
    "دالة-التوقيت-للرسوم-المتحركة",
    "تأخير-الرسوم-المتحركة",
    "عدد-تكرار-الرسوم-المتحركة",
    "اتجاه-الرسوم-المتحركة"
  ],
  [
    "المحتوى",
    "اقتباسات",
    "إعادة-العد",
    "زيادة-العد",
    "تغيير-الحجم",
    "مؤشر-المؤشر",
    "تحديد-المستخدم",
    "فهرس-الملاحة",
    "التنقل-أعلى",
    "التنقل-يمين",
    "التنقل-أسفل",
    "التنقل-يسار",
    "حجم-علامة-الجدول",
    "الكسر",
    "أحداث-المؤشر"
  ]
]
```


## المراجع والشكر

- [دليل مقدمة لـ CSS](https://developer.mozilla.org/zh-CN/docs/Web/Guide/CSS/Getting_started)
- [دورة تعلم CSS3 "CSS3 Tutorial"](https://waylau.gitbooks.io/css3-tutorial/content/)
- [معيار ترتيب خصائص CSS](https://wiki.zthxxx.me/wiki/程序语言/CSS/CSS%20属性声明顺序规范/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.