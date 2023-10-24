# استخدام VS Code للتطوير عن بُعد

- استخدام VS Code كأداة SSH للاتصال بخادم عن بُعد للتطوير.

## الخلفية

لقد قمت بتجربة مجموعة متنوعة من أدوات SSH، ولكن في النهاية عدت إلى استخدام VS Code بسبب واجهته الجميلة وقوته.
يتم توثيق هذا المقال فقط للاستفادة في المستقبل وقد لا يتم شرح بعض الأمور بالتفصيل. لمزيد من الدروس، يرجى الرجوع إلى الروابط في النهاية.

دليل إعداد VS Code: [**دليل إنتاجية VS Code - إعداد البيئة**](https://wiki-power.com/دليل-إنتاجية-VSCode-إعداد-البيئة)

## إعداد الامتدادات

انقر لتثبيت الامتداد: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

انقر على الزر "Remote" في الزاوية السفلية اليسرى للبدء.

## إعدادات إضافية

### لا يمكن لـ VS Code مراقبة تغييرات الملفات في مساحة العمل الكبيرة

قم بتشغيل هذا الأمر لعرض القيود الحالية:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

قم بتحرير ملف `/etc/sysctl.conf`:

```shell
sudo vim /etc/sysctl.conf
```

أضف الكود التالي لزيادة هذا الحد إلى الحد الأقصى:

```shell
fs.inotify.max_user_watches=524288
```

احفظ القيم وقم بتفعيلها:

```shell
sudo sysctl -p
```

### لا يمكن استخدام اسم مستخدم مخصص للتسجيل

في إعدادات VS Code، ابحث عن `Remote.SSH: Config File` واملأ القيمة المستبدلة بـ `C:\Users\اسم المستخدم الذي تحتاجه\.ssh\config`، وقم بإنشاء ملف تكوين مماثل في جهاز الكمبيوتر المحلي.

### الاتصال فاشل، ولكن يمكن الاتصال باستخدام عميل SSH آخر

قد يكون السبب في ذلك هو أن إصدار sshd على الخادم عن بُعد يقل عن 7.6.0 ويفتقر إلى ميزة عرض منفذ الاتصال البعيد. لحل هذه المشكلة، يجب تحديث إصدار sshd:

- بالنسبة لـ Debian أو Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- بالنسبة لـ Red Hat أو CentOS: `sudo yum update openssh-server`

## المراجع والشكر

- [تجربة استخدام VSCode Remote | تطوير بيئة لينكس عن بُعد حقًا لذيذ](https://zhuanlan.zhihu.com/p/64849549)
- [معالجة تنبيهات VSCode: لا يمكن لـ VisualStudioCode مراقبة تغييرات الملفات في هذه مساحة العمل الكبيرة](http://www.deadnine.com/somehow/2019/0208/1481.html)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.