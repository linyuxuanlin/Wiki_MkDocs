# Homelab - لوحة تحكم خفيفة لإدارة الخوادم CasaOS

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304192541.png)

**CasaOS** هي لوحة تحكم شخصية مفتوحة المصدر بسيطة وسهلة الاستخدام وأنيقة، وتتضمن ميزات مثل مدير الملفات ومراقبة حالة الخادم والطرفية وإدارة حاويات Docker ومتجر تطبيقات Docker المدمج.

## التثبيت (شل)

```shell
curl -fsSL https://get.casaos.io | sudo bash
```

عنوان الوصول الافتراضي للوحة: <http://localhost:80>

ملاحظة: إذا تم تثبيتها على خادم لديه وكيل عكسي معين، فمن الأفضل تغيير منفذ الوصول إلى الوحة في الإعدادات الداخلية وترك المنفذ 80 لـ Nginx.

## المراجع والشكر

- [الموقع الرسمي](https://casaos.io)
- [الوثائق](https://wiki.casaos.io/en/home)
- [مستودع GitHub](https://github.com/IceWhaleTech/CasaOS)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
