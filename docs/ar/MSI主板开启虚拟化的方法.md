# طريقة تمكين الافتراضي للوحة الأم MSI

## إعادة التشغيل والدخول إلى BIOS

```cmd
shutdown.exe /r /o
```

بعد إعادة التشغيل ، انقر فوق `حل المشكلات (Troubleshoot)` - `خيارات متقدمة (Advanced options)` - `إعدادات البرنامج الثابت UEFI (UEFI Firmware Settings)` للدخول إلى BIOS لوحة الأم.

## العثور على الإعدادات ذات الصلة

1. الضغط على `F7` للدخول إلى الخيارات المتقدمة
2. النقر على `OC` - `ميزات المعالج (CPU Features)` بالترتيب
3. العثور على `SVM Mode / Intel Virtualization (يعتمد على المعالج)`

## تعديل الإعدادات

قم بتغيير `Disabled (معطل)` إلى `Enabled (ممكّن)`

## حفظ والخروج

اضغط على `F10` للحفظ والخروج

## المراجع والشكر

- [كيفية الدخول إلى BIOS؟](https://zhuanlan.zhihu.com/p/34223088)
- [طريقة تمكين VT لجهاز الكمبيوتر ولوحة الأم MSI](http://mumu.163.com/20181108/25905_784199.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.