# مذكرات تعلم HTML

## الهيكل الأساسي

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

يمكن فتح ملف `.html` وإدخال `html:5` مباشرة لاستدعائه

## البيانات

بعض الإرشادات:

1. استخدام الأحرف الصغيرة للوسوم، ويجب إغلاق العناصر.
2. يجب إضافة شرطة مائلة لإغلاق العناصر الفارغة مثل `<br />`.
3. عدم استخدام الدلالة النصية، ويجب تخزين جميع الأنماط في ورقة الأنماط CSS والفصل بين المحتوى والأنماط.

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

    <!-- علامة الفصل -->
    <br />
    <!-- خط الفصل -->
    <hr />

    <!-- قوائم قابلة للتداخل -->
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

    <!-- الارتباطات -->
    <a href="https://www.google.com/">النص الذي يظهر كرابط</a>
    <!-- الارتباط بموقع محدد على الصفحة باستخدام خاصية ID -->
    <a href="#top">العودة إلى الأعلى</a>
    <p id="top">الأعلى</p>
    <!-- الارتباط بمواقع أخرى على صفحات معينة -->
    <a href="http://wiki-power.com/#top">الانتقال إلى مكان معين على صفحة خارجية</a>

    <!-- الصور -->
    <img src="/xx.png" alt="نص الوصف عند عدم تحميل الصورة" />

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
            <th scope="row">العائد</th>
            <!-- الدمج عبر الأعمدة (colspan) والصفوف (rowspan) -->
            <td colspan="2">500</td>
        </tr>
    </table>


```markdown
<!-- النموذج، يتم ملؤه لاحقًا -->
<!-- الإطار، يتم ملؤه لاحقًا -->
<!-- الفلاش / الفيديو / الصوت، يتم ملؤه لاحقًا -->

</body>

</html>
```

## مراجع وشكر

- [HTML تعليم | تعليم الصياد الجديد](http://www.runoob.com/html/html-tutorial.html)
- [HTML دورة تعليمية في 30 دقيقة](http://deerchao.net/tutorials/html/html.htm)
- [HTML - تحليل رأس الصفحة](https://www.tielemao.com/831.html)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

Note: The text within `to_be_replace[1]` and `to_be_replace[2]` was not translated as it appears to be a reference or placeholder that should remain as is.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.