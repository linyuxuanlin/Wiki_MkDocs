# ملاحظات تعلم Linux - عمليات المستخدمين

## العمليات الأساسية

### إضافة مستخدم

```shell
useradd -m اسم_المستخدم
```

### تعيين كلمة مرور

```shell
passwd اسم_المستخدم
```

### حذف مستخدم

```shell
userdel -r اسم_المستخدم
```

### حذف دليل المستخدم

```shell
rm -rf اسم_المستخدم
```

### تبديل المستخدم الحالي

```shell
su اسم_المستخدم
```

## المراجع والشكر

- [إنشاء مستخدمين في Linux وتعيين كلمات مرور](https://blog.csdn.net/li_101357/article/details/69367457)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.