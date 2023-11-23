# ملاحظات تعلم JavaScript

## استدعاء جافا سكريبت خارجي

```markup
<!DOCTYPE html>
<html>
    <head>
        <script src="xx1.js"></script>
    </head>
    <body>
        <script src="xx2.js"></script>
    </body>
</html>
```

## الإخراج

### عرض نافذة تحذير

```javascript
window.alert("مرحبًا");
```

### التعامل مع عناصر HTML

```markup
<!DOCTYPE html>
<html>
    <body>
        <h1>صفحتي الويب الأولى</h1>
        <p id="demo">فقرتي الأولى</p>
        <script>
            document.getElementById("demo").innerHTML = "تم تعديل الفقرة.";
        </script>
    </body>
</html>
```

## أنواع البيانات

إنشاء متغير:

```javascript
var carname = "فولفو";
```

**أنواع القيم (الأساسية):** سلسلة نصية (String)، رقم (Number)، منطقي (Boolean)، فارغ (Null)، غير معرف (Undefined)، رمز (Symbol).

**أنواع البيانات المرجعية:** كائن (Object)، مصفوفة (Array)، وظيفة (Function).

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.