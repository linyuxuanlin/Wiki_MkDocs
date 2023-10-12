# تسريع الوصول لـ npm و Yarn في الصين عن طريق تغيير المصدر

## الخلفية

توجد مصادر npm و Yarn الافتراضية في الخارج، مما يؤدي إلى بطء الوصول لها في الصين.  
يمكنك استخدام الأمر التالي لمعرفة المصدر الحالي:

```shell
yarn config get registry
```

## الحل

استخدم برنامج cgr لتغيير مصدر npm و Yarn بسرعة.

### تثبيت cgr

```shell
npm install -g cgr
```

### عرض المصادر المتاحة حاليًا

```
cgr ls
```

### اختيار مصدر واحد للتغيير (Taobao)

```
cgr use taobao
```

### اختبار سرعة الوصول

```
cgr test taobao
```

## المراجع والشكر

- [yarn 国内加速，修改镜像源](https://learnku.com/articles/15976/yarn-accelerate-and-modify-mirror-source-in-china)
- [cgr -- change registry | yarn & npm registry manager](https://www.npmjs.com/package/cgr)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.