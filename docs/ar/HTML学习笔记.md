# ملاحظات دراسة HTML

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

يمكن فتح ملف `.html` وكتابة `html:5` مباشرة لإظهاره.

## البيانات

بعض المعايير:

1. استخدام الأحرف الصغيرة للعلامات، ويجب إغلاق العناصر.
2. يجب إضافة شرطة مائلة للعناصر الفارغة لإغلاقها، على سبيل المثال `<br />`.
3. عدم استخدام الدلالة الدلالية، ويتم تخزين جميع الأنماط في CSS، ويجب فصل المحتوى عن الأنماط.

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
    <h1>العنوان الأول</h1>
    <h2>العنوان الثاني</h2>
    <p>فقرة</p>

    <!-- فاصل السطر -->
    <br />
    <!-- خط الفاصل -->
    <hr />

    <!-- القوائم، يمكن تضمينها -->
    <!-- القائمة المرتبة -->
    <ol>
        <li>العنصر الأول</li>
        <li>العنصر الثاني</li>
    </ol>
    <!-- القائمة غير المرتبة -->
    <ul>
        <li>العنصر الأول</li>
        <li>العنصر الثاني</li>
    </ul>

    <!-- الروابط -->
    <a href="https://www.google.com/">نص الرابط</a>
    <!-- الربط إلى موقع محدد، باستخدام معرف ID -->
    <a href="#top">العودة إلى الأعلى</a>
    <p id="top">الأعلى</p>
    <!-- الربط إلى موقع آخر محدد -->
    <a href="http://wiki-power.com/#top">الانتقال إلى موقع آخر</a>

    <!-- الصور -->
    <img src="/xx.png" alt="نص الوصف عند عدم التحميل" />

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
            <th scope="row">الكمية</th>
            <td>120</td>
            <td>135</td>
        </tr>
        <!-- الصف الثالث -->
        <tr>
            <th scope="row">الأرباح</th>
            <!-- العمود العريض colspan، الصف العريض rowspan -->
            <td colspan="2">500</td>
        </tr>
    </table>

<!--النموذج، قيد الإكمال-->
<!--الإطار، قيد الإكمال-->
<!--فلاش/فيديو/صوت، قيد الإكمال-->

</body>

</html>
```

## المراجع والشكر

- [دليل HTML | تعلم البرمجة](http://www.runoob.com/html/html-tutorial.html)
- [تعلم HTML في 30 دقيقة](http://deerchao.net/tutorials/html/html.htm)
- [HTML - تحليل رأس الصفحة](https://www.tielemao.com/831.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.