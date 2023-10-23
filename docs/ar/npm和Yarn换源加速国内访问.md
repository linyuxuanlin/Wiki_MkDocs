```markdown
# تغيير مصدر npm و Yarn لتسريع الوصول في الصين

## الخلفية

مصادر npm و Yarn الافتراضية في الخارج، وتواجه صعوبات في الوصول إليها في الصين.  
يمكنك التحقق من مصدر المرآة الحالي باستخدام الأمر التالي:

```shell
yarn config get registry
```

## الحل

استخدام البرنامج المساعد cgr للتبديل بسرعة بين مصادر المرآة لـ npm و Yarn.

### تثبيت cgr

```shell
npm install -g cgr
```

### عرض الأمثلة الحالية المتاحة

```
cgr ls
```

### اختيار مصدر المرآة للتبديل إليه (مثلاً مرآة Taobao)

```
cgr use taobao
```

### اختبار سرعة الوصول

```
cgr test taobao
```

## المراجع والشكر

- [تسريع Yarn في الصين وتعديل مصدر المرآة](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr -- تغيير مسجل | إدارة مسجل yarn و npm](https://www.npmjs.com/package/cgr)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.