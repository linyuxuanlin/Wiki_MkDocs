# استخدام VS Code للتطوير عن بُعد

—— استخدام VS Code كأداة SSH للاتصال بخادم عن بُعد والقيام بعمليات التطوير.

## الخلفية

بعد تجربة مجموعة متنوعة من أدوات SSH، عدت في النهاية إلى استخدام VS Code بواجهته الجميلة والقوية.  
تسجل هذه المقالة فقط للاستعراض المستقبلي، ولم يتم توضيح بعض الأجزاء بالتفصيل. لمزيد من البرامج التعليمية، يُرجى الرجوع إلى الروابط في نهاية المقال.

قسم تهيئة VS Code الأساسية: [**دليل إنتاجية VS Code - تكوين البيئة**](https://wiki-power.com/VSCode生产力指南-环境配置)

## تهيئة الامتدادات

انقر لتثبيت الامتداد: [**Remote - SSH**](https://marketplace.visualstudio.com/items?itemName=ms-vscode-remote.remote-ssh)

اضغط على زر "Remote" في الزاوية السفلية اليسرى للاستخدام.

## تهيئة أخرى

### VS Code غير قادر على مراقبة تغييرات الملفات في مساحة عمل كبيرة

قم بتشغيل الأمر التالي لعرض القيود الحالية:

```shell
cat /proc/sys/fs/inotify/max_user_watches
```

قم بتحرير ملف `/etc/sysctl.conf`:

```shell
sudo vim /etc/sysctl.conf
```

أضف الكود التالي لزيادة الحد إلى الحد الأقصى:

```shell
fs.inotify.max_user_watches=524288
```

احفظ، ثم فعل الإعداد:

```shell
sudo sysctl -p
```

### غير قادر على تسجيل الدخول باستخدام اسم مستخدم مخصص

ابحث في إعدادات VS Code عن `Remote.SSH: Config File`، واملأ القيمة المغطاة بـ `C:\Users\اسم_المستخدم_المطلوب\.ssh\config`، ثم قم بإنشاء ملف الضبط المناسب محليًا.

### فشل الاتصال، ولكن يمكن الاتصال باستخدام عميل SSH آخر

قد يكون سببه إصدار خادم SSH البعيد الخاص بك أقل من 7.6.0 ويفتقد إلى ميزة عرض منفذ الشبكة البعيدة. لحل هذه المشكلة، يجب تحديث إصدار خادم SSH:

- بالنسبة لـ Debian أو Ubuntu: `sudo apt-get update && sudo apt-get install openssh-server`
- بالنسبة لـ Red Hat أو CentOS: `sudo yum update openssh-server`

قد يكون سببه أيضًا إعدادات الوكيل، جرب تبديلها أو إيقافها.

## الإشارات والإعترافات

- [تجربة الـ VSCode Remote | تطوير بيئة Linux عن بُعد شيق جدًا](https://zhuanlan.zhihu.com/p/64849549)
- [معالجة تقارير الخطأ في VSCode: لا يمكن لـ VisualStudioCode مراقبة تغييرات ملفات هذه المساحة الكبيرة للعمل](http://www.deadnine.com/somehow/2019/0208/1481.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.