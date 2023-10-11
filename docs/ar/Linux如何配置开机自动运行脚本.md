# كيفية تكوين تشغيل النظام التلقائي للبرنامج النصي في Linux

## لأنظمة SysV init

ملاحظة: تنطبق الطريقة التالية على توزيعات Linux التي تستخدم نظام SysV init (مثل Ubuntu 18.04 والإصدارات الأحدث أو Debian). بالنسبة لتوزيعات تستخدم Systemd (مثل Ubuntu 18.04 والإصدارات الأحدث) ، يرجى استخدام طريقة `systemctl` لإدارة خدمات البدء.

إذا كان البرنامج النصي الذي نريد تشغيله تلقائيًا عند بدء التشغيل هو `xxx.sh` ، فيجب علينا أولاً إنشاء برنامج نصي للتشغيل في الدليل `/etc/init.d` ، مثل `autorun.sh`:

```shell
sudo nano /etc/init.d/autorun.sh
```

ثم يتم إضافة البرنامج النصي الذي نريد تشغيله تلقائيًا عند بدء التشغيل:

```bash title="autorun.sh"
#!/bin/bash
/path/to/xxx.sh  # تعديل المسار الفعلي
```

ثم يتم إضافة برنامج `autorun.sh` إلى خدمة البدء في النظام:

```shell
sudo update-rc.d autorun.sh defaults
```

ثم يتم تعيين برنامج `autorun.sh` للتشغيل التلقائي عند بدء التشغيل:

```shell
sudo update-rc.d autorun.sh enable
```

بهذه الطريقة ، سيتم تشغيل برنامج `autorun.sh` تلقائيًا عند إعادة التشغيل.

## لأنظمة Systemd

إذا كانت توزيعة Linux الخاصة بك تستخدم Systemd كمدير بدء التشغيل (مثل Ubuntu 18.04 والإصدارات الأحدث) ، فيمكنك استخدام أمر `systemctl` لتعيين التشغيل التلقائي.

إذا كان البرنامج النصي الذي نريد تشغيله تلقائيًا عند بدء التشغيل هو `xxx.sh` ، فيجب علينا أولاً إنشاء ملف وحدة يصف الخدمة التي نريد تشغيلها تلقائيًا ، مثل `autorun.service`:

```shell
sudo nano /etc/systemd/system/autorun.service
```

ثم يتم تحديد تكوين الخدمة الخاصة بك في ملف الوحدة. هنا مثال:

```service title="autorun.service"
[Unit]
Description=My Service
After=network.target
[Service]
ExecStart=/path/to/xxx.sh
[Install]
WantedBy=default.target
```

حيث:

- `Description`: وصف الخدمة الخاصة بك.
- `After`: تحديد الخدمات الأخرى التي يجب تشغيلها قبل الخدمة الخاصة بك. على سبيل المثال ، يعني `network.target` تشغيل خدمة الشبكة قبل تشغيل الخدمة الخاصة بك.
- `ExecStart`: تحديد مسار البرنامج النصي أو الأمر الذي تريد تشغيله.
- `WantedBy`: تحديد الهدف الذي يجب تشغيل الخدمة الخاصة بك عند بدء التشغيل. يعني `default.target` تشغيل الخدمة الخاصة بك عند بدء التشغيل الافتراضي.

بعد حفظ وإغلاق الملف ، يتم إعادة تحميل تكوين systemd باستخدام الأمر التالي:

```shell
sudo systemctl daemon-reload
```

ثم يتم تمكين الخدمة الخاصة بك باستخدام الأمر التالي:

```shell
sudo systemctl enable autorun.service
```

أخيرًا ، يتم تشغيل الخدمة الخاصة بك باستخدام الأمر التالي:

```shell
sudo systemctl start autorun.service
```

الآن ، تم تعيين الخدمة الخاصة بك للتشغيل التلقائي عند بدء التشغيل. يمكنك إعادة تشغيل النظام للتحقق مما إذا كانت الخدمة تعمل بشكل صحيح.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.