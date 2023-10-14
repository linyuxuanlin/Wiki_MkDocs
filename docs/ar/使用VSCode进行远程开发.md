# استخدام VS Code للتطوير عن بعد

- استخدام VS Code كأداة SSH للاتصال بخادم عن بعد للتطوير.

## الخلفية

بعد تجربة جميع أدوات SSH المتاحة، عدت أخيرًا إلى VS Code الذي يتميز بواجهة جميلة وقوية.  
يتم توثيق هذه المقالة فقط للاستشارة في المستقبل، ولم يتم شرح بعض المحتويات بالتفصيل. لمزيد من الدروس، يرجى الرجوع إلى الروابط في نهاية المقالة.

دليل تكوين VS Code: [**دليل إنتاجية VS Code - تكوين البيئة**](](https://wiki-power.com/ar/VSCode生产力指南-环境配置)

## تكوين الامتداد

انقر لتثبيت الامتداد: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

انقر على زر `Remote` في الزاوية السفلية اليسرى للبدء.

## تكوينات أخرى

### لا يمكن لـ VS Code مراقبة تغييرات ملفات مساحة العمل الكبيرة

قم بتشغيل هذا الأمر لعرض القيود الحالية:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

تحرير ملف `/etc/sysctl.conf`:

```shell
sudo vim /etc/sysctl.conf
```

أضف الكود التالي لزيادة هذا الحد إلى الحد الأقصى:

```shell
fs.inotify.max_user_watches=524288
```

حفظ وتمكين الإعدادات:

```shell
sudo sysctl -p
```

### لا يمكن استخدام اسم مستخدم مخصص لتسجيل الدخول

ابحث في إعدادات VS Code عن `Remote.SSH: Config File`، واملأ القيمة المغطاة بـ `C:\Users\اسم المستخدم الذي تحتاجه\.ssh\config`، وأنشئ ملف التكوين المناسب محليًا.

### فشل الاتصال، ولكن يمكن الاتصال باستخدام عميل SSH آخر

قد يكون ذلك بسبب إصدار sshd على الخادم البعيد الذي يقل عن 7.6.0، والذي يفتقر إلى ميزة عرض منفذ الجهاز البعيد. لحل هذه المشكلة، يجب تحديث إصدار sshd:

- لـ Debian أو Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- لـ Red Hat أو CentOS: `sudo yum update openssh-server`

## المراجع والشكر

- [تجربة Remote VSCode | تطوير بيئة Linux عن بعد](https://zhuanlan.zhihu.com/p/64849549)
- [معالجة إنذار VSCode: لا يمكن لـ VisualStudioCode مراقبة تغييرات مساحة العمل الكبيرة هذه](http://www.deadnine.com/somehow/2019/0208/1481.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.