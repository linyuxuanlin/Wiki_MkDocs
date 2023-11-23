```markdown
# حذف مجلد معين في مستودع GitHub

## مصدر المشكلة

عند رفع مستودع محلي إلى GitHub ، نسيت تجاهل مجلد معين وقمت بدفعه مباشرة إلى المستودع عن بُعد.  
كيف يمكنني حذف المجلد في مستودع GitHub مع الاحتفاظ بنسخة المجلد المحلي؟

## طريقة الحل

```shell
git pull origin master        # ابدأ بجلب المشروع من المستودع البعيد
dir                           # قم بفحص المجلدات المتاحة
git rm -r --cached target     # حذف المجلد بالاسم "target"
git commit -m 'حذف المجلد target'  # أضف توضيحًا للإجراء وقُم بالتأكيد
```

## المراجعة والشكر

- [حذف مجلد معين في GitHub](https://blog.csdn.net/wudinaniya/article/details/77508229)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.