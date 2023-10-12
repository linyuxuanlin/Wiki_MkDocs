# نصائح Vue.js الصغيرة

## إزالة `#` من عنوان URL

**المشكلة**: يتضمن عنوان URL لمشروع Vue.js علامة `#`، مما يؤثر على المظهر العام.

**الحل**: 

1. ابحث عن الدالة `const router = new VueRouter({})` في المشروع بأكمله.
2. أضف العبارة `mode: 'history'` داخل الدالة.

## المراجع والشكر

- [كيفية إزالة علامة # من مشروع Vue - وضع التاريخ](https://www.cnblogs.com/zhuzhenwei918/p/6892066.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.