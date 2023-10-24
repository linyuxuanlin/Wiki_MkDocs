# إنشاء الشرائح باستخدام reveal.js

## اختصارات لوحة المفاتيح

- الشريحة التالية: **مسافة**
- تحديد الاتجاه للشريحة: **مفاتيح الاتجاه**
- عرض عام: **Esc**
- عرض المتحدث: **S**
- إيقاف العرض / الشاشة السوداء: **V/B/.**

## تصدير إلى PDF

أضف `?print-pdf` إلى العنوان، على سبيل المثال `http://localhost:8000/?print-pdf`

## قواعد الصياغة المرجعية

### الصور

```html
<img
  data-src=""
  style="
              width: px;
              margin: 0 auto 1rem auto;
              background: transparent;
            "
/>
```

```html
align="left"
```

### النص

```html
<p style="white-space: pre-line;"><small> </small></p>
```

### الفيديو

```html
<section
  data-transition="slide"
  data-background="#EAB547"
  data-background-transition="zoom"
>
  <video data-src=""></video>
</section>
```

## المراجع والشكر

- [reveal.js](https://revealjs.com/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.