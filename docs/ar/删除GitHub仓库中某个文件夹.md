# حذف مجلد معين من مستودع GitHub

## مصدر المشكلة

عندما تم رفع المستودع المحلي إلى GitHub ، تم نسيان تجاهل مجلد معين وتم دفعه مباشرةً إلى المستودع البعيد.  
كيف يمكن حذف المجلد من مستودع GitHub والاحتفاظ بالمجلد المحلي؟

## الحل

```shell
git pull origin master        # اسحب المشروع من المستودع البعيد أولاً
dir                           # اعرض المجلدات الموجودة
git rm -r --cached target     # حذف المجلد الذي يحمل الاسم target
git commit -m 'حذف target'  # أضف شرحًا للعملية وقم بالتأكيد على الإرسال
```

## المراجع والشكر

- [حذف مجلد معين من GitHub](https://blog.csdn.net/wudinaniya/article/details/77508229)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.