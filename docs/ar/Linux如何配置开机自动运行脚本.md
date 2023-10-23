# كيفية تكوين تشغيل السيناريو تلقائيًا عند بدء تشغيل Linux

## لأنظمة تشغيل SysV init

**ملاحظة:** الأساليب التالية تنطبق على توزيعات Linux التي تستخدم نظام SysV init (مثل Ubuntu 18.04 والإصدارات الأحدث، أو Debian). بالنسبة لتلك التي تستخدم نظام Systemd (مثل Ubuntu 18.04 والإصدارات الأحدث)، يُفضل استخدام الأمر `systemctl` لإدارة خدمات البدء.

فيما يلي كيفية تكوين تشغيل السيناريو `xxx.sh` تلقائيًا عند بدء تشغيل النظام. أولاً، أنشئ سيناريو لبدء التشغيل في المجلد `/etc/init.d`، وقم بتسميته `autorun.sh` على سبيل المثال:

```shell
sudo nano /etc/init.d/autorun.sh
```

قم بإضافة السيناريو الذي ترغب في تنفيذه تلقائيًا:

```bash title="autorun.sh"
#!/bin/bash
/path/to/xxx.sh  # قم بتغيير المسار إلى المسار الفعلي
```

أضف السيناريو `autorun.sh` إلى خدمات بدء التشغيل في النظام:

```shell
sudo update-rc.d autorun.sh defaults
```

قم بتمكين تشغيل `autorun.sh` عند بدء التشغيل:

```shell
sudo update-rc.d autorun.sh enable
```

بهذه الطريقة، سيتم تشغيل السيناريو `autorun.sh` تلقائيًا بعد إعادة تشغيل النظام.

## لأنظمة تشغيل Systemd

إذا كانت توزيعة Linux الخاصة بك تستخدم نظام Systemd كإدارة بدء التشغيل (مثل Ubuntu 18.04 والإصدارات الأحدث)، يمكنك استخدام الأمر `systemctl` لضبط التشغيل التلقائي.

إذا كنت بحاجة إلى تكوين تشغيل السيناريو `xxx.sh` عند بدء تشغيل النظام، ابدأ بإنشاء ملف وحدة يصف الخدمة التي ترغب في تشغيلها تلقائيًا، مثل `autorun.service`:

```shell
sudo nano /etc/systemd/system/autorun.service
```

ضمن ملف الوحدة، قم بتعريف إعدادات الخدمة. هذا مثال لملف الوحدة:

```service title="autorun.service"
[Unit]
Description=My Service
After=network.target
[Service]
ExecStart=/path/to/xxx.sh
[Install]
WantedBy=default.target
```

المعلمات في الملف هي كالتالي:

- `Description`: وصف لخدمتك.
- `After`: تحديد متى تبدأ خدمتك بعد بدء تشغيل خدمات أخرى. على سبيل المثال، `network.target` تشير إلى بدء التشغيل بعد بدء خدمات الشبكة.
- `ExecStart`: تحديد الملف أو الأمر الذي ترغب في تنفيذه.
- `WantedBy`: تحديد الهدف الذي تجب أن تبدأ فيه خدمتك. `default.target` تعني البدء بعد تحميل الهدف الافتراضي.

بعد حفظ وإغلاق الملف، قم بإعادة تحميل تكوين Systemd كالتالي:

```shell
sudo systemctl daemon-reload
```

من ثم، قم بتمكين خدمتك بالتشغيل التلقائي:

```shell
sudo systemctl enable autorun.service
```

أخيرًا، قم بالبدء بالخدمة كالتالي:

```shell
sudo systemctl start autorun.service
```

الآن، تم تكوين الخدمة للتشغيل تلقائيًا عند بدء تشغيل النظام. يمكنك إعادة تشغيل النظام للتحقق من تشغيل الخدمة بنجاح.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.