# تغيير Host في GitHub

## المشكلة

خطأ: `curl: (7) Failed to connect to raw.githubusercontent.com port 443: Connection refused `

## السبب

تلوث DNS في الصين.

## الحل

أضف الآتي إلى ملف host على جهازك:

```
199.232.68.133 raw.githubusercontent.com
199.232.68.133 user-images.githubusercontent.com
199.232.68.133 avatars2.githubusercontent.com
199.232.68.133 avatars1.githubusercontent.com
```

مسار host:

- Windows: `C:\Windows\System32\drivers\etc`
- Linux: `/etc/hosts`

إليك بعض طرق التعامل مع Linux:

1. افتح الطرفية
2. أدخل الأمر: `vi /etc/hosts`
3. اضغط على `A` للتبديل إلى وضع التحرير
4. أضف الآتي إلى نهاية Host
5. اضغط على `Esc` للخروج من وضع التحرير، ثم اضغط على `:wq` للحفظ والخروج

## توسيع

### البحث عن عنوان IP لاسم النطاق

استخدم [**IPAddress**](https://www.ipaddress.com/)

## المراجع والشكر

- [إضافة Host لتسريع الوصول إلى GitHub](https://yangshun.win/blogs/2b7abf4f/#%E4%BF%AE%E6%94%B9-host)

> مؤلف المقال: **Power Lin**
> الرابط الأصلي للمقال: <https://wiki-power.com>
> بيان حقوق النشر: يتم ترخيص المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يرجى الإشارة إلى المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.