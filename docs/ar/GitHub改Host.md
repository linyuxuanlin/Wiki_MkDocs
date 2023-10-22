# تعديل GitHub Host

## المشكلة

خطأ: `curl: (7) فشل الاتصال بـ raw.githubusercontent.com على المنفذ 443: تم رفض الاتصال`

## السبب

تلوث DNS في البلاد.

## الحل

أضف السطور التالية إلى ملف host الخاص بجهاز الكمبيوتر:

```
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

مسار ملف Host:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

إليك بعض الخطوات للقيام بذلك في نظام Linux:

1. افتح الطرفية (الترمينال).
2. أدخل الأمر: `vi /etc/hosts`
3. اضغط `A` للانتقال إلى وضع التحرير.
4. قم بإضافة السطور السابقة إلى نهاية الملف.
5. اضغط `Esc` للخروج من وضع التحرير، ثم اكتب `:wq` واضغط Enter لحفظ التغييرات والخروج.

## توسيع

### البحث عن عنوان IP للمضيف

استخدم [**IPAddress**](https://www.ipaddress.com/)

## المراجع والشكر

- [إضافة Host لتسريع الوصول إلى GitHub](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> كاتب المقال: **باور لين**
> عنوان المقال الأصلي: <https://wiki-power.com>
> إخلاء المسؤولية: يتم ترخيص المقال بموجب [رخصة CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.