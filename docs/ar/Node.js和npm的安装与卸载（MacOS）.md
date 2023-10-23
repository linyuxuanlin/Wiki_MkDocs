# تثبيت وإزالة Node.js و npm (MacOS)

## التثبيت

[http://nodejs.cn/download/](http://nodejs.cn/download/)

## الإزالة

لمن قاموا بالتثبيت باستخدام `homebrew`:

```shell
brew uninstall node
```

لمن قاموا بالتثبيت باستخدام حزمة `.pkg`:

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## حل المشكلات

س: بعد تغيير اسم المستخدم في MacOS، تظهر رسالة بأن الإذن غير كافٍ: `EACCES: permission denied`
ج: قم بتشغيل الأمر التالي بوضع غير آمن: `sudo npm install -g appium --unsafe-perm=true --allow-root`

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.