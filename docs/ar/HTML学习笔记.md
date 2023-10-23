# مذكرات تعلم HTML

## الإطار الأساسي

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>العنوان</title>
</head>
<body>

</body>
</html>
```

يمكن فتح ملف `.html` مباشرة وإدخال `html:5` لاستدعائه.

## البيانات

بعض الإرشادات:

1. استخدم الأوامر بأحرف صغيرة وتأكد من إغلاق العناصر.
2. يجب إضافة شرطة مائلة (/) لإغلاق العناصر الفارغة، على سبيل المثال: `<br />`.
3. لا تستخدم تشدد الدلالة، يجب وضع جميع الأنماط في ورقة الأنماط (CSS) والاحتفاظ بالمحتوى منفصلًا عن الأنماط.

```markup
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="X-UA-Compatible" content="ie=edge">
    <title>العنوان</title>
</head>
<body>
    <h1>عنوان من المستوى الأول</h1>
    <h2>عنوان من المستوى الثاني</h2>
    <p>فقرة</p>

    <!-- فاصل السطر -->
    <br />
    <!-- خط الفصل -->
    <hr />

    <!-- القوائم، قد تكون متداخلة -->
    <!-- قائمة مرتبة -->
    <ol>
        <li>العنصر الأول</li>
        <li>العنصر الثاني</li>
    </ol>
    <!-- قائمة غير مرتبة -->
    <ul>
        <li>العنصر الأول</li>
        <li>العنصر الثاني</li>
    </ul>

    <!-- الروابط -->
    <a href="https://www.google.com/">النص المعروض للرابط</a>
    <!-- الارتباط بموقع معين على الصفحة باستخدام معرف ID -->
    <a href="#top">العودة للأعلى</a>
    <p id="top">أعلى الصفحة</p>
    <!-- الارتباط بموقع معين على صفحة أخرى -->
    <a href="http://wiki-power.com/#top">الانتقال إلى مكان محدد على صفحة خارجية</a>

    <!-- الصور -->
    <img src="/xx.png" alt="نص البديل في حالة عدم التمكن من تحميل الصورة" />

    <!-- الجداول -->
    <table>
        <!-- الصف الأول -->
        <tr>
            <!-- العمود الأول -->
            <th></th>
            <!-- العمود الثاني -->
            <th scope="col">السبت</th>
            <!-- العمود الثالث -->
            <th scope="col">الأحد</th>
        </tr>
        <!-- الصف الثاني -->
        <tr>
            <th scope="row">العدد</th>
            <td>120</td>
            <td>135</td>
        </tr>
        <!-- الصف الثالث -->
        <tr>
            <th scope="row">الإيراد</th>
            <!-- الاندماج عبر الأعمدة colspan، والاندماج عبر الصفوف rowspan -->
            <td colspan="2">500</td>
        </tr>
    </table>


Here's the translation of the provided text into Arabic:

```html
<!-- نموذج، تحتاج للتعبئة -->
<!-- إطار، تحتاج للتعبئة -->
<!-- فلاش/فيديو/صوت، تحتاج للتعبئة -->

</body>

</html>
```

## مراجع وشكر خاص

- [HTML Tutorial | تعليم HTML - موقع نيوب التعليمي](http://www.runoob.com/html/html-tutorial.html)
- [دورة تعليم HTML في 30 دقيقة](http://deerchao.net/tutorials/html/html.htm)
- [HTML - تحليل الرأس (head) - تيليماو](https://www.tielemao.com/831.html)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.