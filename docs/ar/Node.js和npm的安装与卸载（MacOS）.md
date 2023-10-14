# تثبيت وإزالة Node.js و npm (MacOS)

## التثبيت

[http://nodejs.cn/download/](http://nodejs.cn/download/)

## الإزالة

للحذف عن طريق `homebrew`:

```shell
brew uninstall node
```

للحذف عن طريق حزمة التثبيت `.pkg`:

```shell
sudo rm -rf /usr/local/{bin/{node,npm},lib/node_modules/npm,lib/node,share/man/*/node.*}
```

## الأسئلة الشائعة

س: بعد تغيير اسم المستخدم في MacOS ، يتم عرض رسالة الخطأ "EACCES: permission denied"؟
ج: `sudo npm install -g appium --unsafe-perm=true --allow-root`، تشغيل بدون الأمان. 

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.