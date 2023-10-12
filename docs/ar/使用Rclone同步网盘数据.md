# استخدام Rclone لمزامنة بيانات السحابة

Rclone هي أداة سطر الأوامر المستخدمة لإدارة ملفات السحابة، وتدعم أكثر من 40 نوعًا من السحابات (بما في ذلك S3). كما يوجد برنامج RcloneBrowser الرسومي المشتق منه، والذي يسهل استخدامه للمستخدمين العاديين. يتم في هذا المقال شرح كيفية مزامنة تخزين الكائنات السحابية على Tencent Cloud باستخدام Rclone.

## تثبيت البرامج

- [**Rclone**](https://rclone.org/downloads/) : بعد التنزيل، قم بفك الضغط عن الملف `.exe` وتدوين المسار.
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases) : أداة واجهة المستخدم الرسومية. بعد التثبيت، حدد مسار Rclone.
- ([**WinFsp**](http://www.secfs.net/winfsp/rel/): مكتبة الاعتماد، إذا كنت تريد تثبيت القرص الظاهري)

## عملية التكوين

افتح RcloneBrowser وانقر على `Config...` في الزاوية السفلى اليسرى، ثم اتبع التعليمات التالية:

أدخل `n` لإنشاء اتصال عن بعد جديد:

```shell
Name                 Type
====                 ====
rclone config        s3
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config

e/n/d/r/c/s/q> n
```

قم بتسمية الاتصال البعيد (مثل `test`):

```shell
name> test
```

حدد مزود الخدمة (في هذا المثال، سنستخدم Tencent Cloud COS ونختار `4`):

```shell
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS
   \ "s3"
...

Storage> 4
```

```shell
Choose a number from below, or type in your own value
 1 / Amazon Web Services (AWS) S3
   \ "AWS"
 2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
   \ "Alibaba"
 3 / Ceph Object Storage
   \ "Ceph"
 4 / Digital Ocean Spaces
   \ "DigitalOcean"
 5 / Dreamhost DreamObjects
   \ "Dreamhost"
 6 / IBM COS S3
   \ "IBMCOS"
 7 / Minio Object Storage
   \ "Minio"
 8 / Netease Object Storage (NOS)
   \ "Netease"
 9 / Scaleway Object Storage
   \ "Scaleway"
10 / StackPath Object Storage
   \ "StackPath"
11 / Tencent Cloud Object Storage (COS)
   \ "TencentCOS"
12 / Wasabi Object Storage
   \ "Wasabi"
13 / Any other S3 compatible provider
   \ "Other"

Arabic:

```

اختر نوع المصادقة. نظرًا لأننا نقوم بالتكوين للمرة الأولى ، فسنختار `1`:

```shell
اختر رقمًا من الأسفل ، أو اكتب قيمتك الخاصة
 1 / أدخل بيانات اعتماد AWS في الخطوة التالية
   \ "false"
 2 / الحصول على بيانات اعتماد AWS من البيئة (متغيرات env أو IAM)
   \ "true"

env_auth> 1
```

أدخل حساب خدمة السحابة ، وهذا يعادل SecretId لـ Tencent Cloud COS:

```shell
معرف مفتاح الوصول إلى AWS.

access_key_id> ******
```

أدخل كلمة المرور ، وهذا يعادل SecretKey:

```shell
AWS Secret Access Key (password)

secret_access_key> ******
```

اختر منطقة خدمة السحابة:

```shell
نقطة النهاية لواجهة برمجة تطبيقات Tencent COS.
 1 / منطقة بكين.
   \ "cos.ap-beijing.myqcloud.com"
 2 / منطقة نانجينغ.
   \ "cos.ap-nanjing.myqcloud.com"
 3 / منطقة شنغهاي.
   \ "cos.ap-shanghai.myqcloud.com"
 4 / منطقة قوانغتشو.
   \ "cos.ap-guangzhou.myqcloud.com"
...

endpoint> 4
```

اختر نوع القراءة / الكتابة ، حيث يكون القراءة عامة والكتابة خاصة في حالة الصور:

```shell
Canned ACL used when creating buckets and storing or copying objects.
 1 / Owner gets Full_CONTROL. No one else has access rights (default).
   \ "default"
 2 / Owner gets FULL_CONTROL. The AllUsers group gets READ access.
   \ "public-read"
   / Owner gets FULL_CONTROL. The AllUsers group gets READ and WRITE access.
...

acl> 2
```

اختر نوع التخزين (يمكنك اختيار الافتراضي `1`):

```shell
The storage class to use when storing new objects in Tencent COS.
 1 / Default
   \ ""
 2 / Standard storage class
   \ "STANDARD"
 3 / Archive storage mode.
   \ "ARCHIVE"
 4 / Infrequent access storage mode.
   \ "STANDARD_IA"

storage_class> 1
```

هل تريد تحرير الإعدادات المتقدمة (اختر `n` لا):

```shell
Edit advanced config? (y/n)
y) Yes
n) No (default)

y/n> n
```

أخيرًا ، تأكد من الإعدادات وأدخل `y`:

```shell
Confirm settings:
provider: Tencent Cloud COS
access_key_id: ******
secret_access_key: ******
endpoint: cos.ap-guangzhou.myqcloud.com
acl: public-read
storage_class: Default
Edit advanced config? (y/n): n
```

y
```

تكوين عن بعد
--------------------
[Txcos]
type = s3
provider = TencentCOS
env_auth = false
access_key_id = 我是马赛克
secret_access_key = 我是马赛克
endpoint = cos.ap-guangzhou.myqcloud.com
acl = public-read
--------------------
y) نعم هذا موافق (الافتراضي)
e) تحرير هذا النظام البعيد
d) حذف هذا النظام البعيد
y/e/d> y
```

أدخل `q` للخروج:

```shell
النظم البعيدة الحالية:

Name                 Type
====                 ====
Txcos                 s3

e) تحرير النظام البعيد الحالي
n) نظام بعيد جديد
d) حذف النظام البعيد
r) إعادة تسمية النظام البعيد
c) نسخ النظام البعيد
s) تعيين كلمة مرور التكوين
q) الخروج من التكوين
e/n/d/r/c/s/q> q
```

بعد ذلك ، انقر نقرًا مزدوجًا لفتح الاتصال البعيد المكون ، حدد المجلد وانقر فوق `تنزيل` لتنزيله على الجهاز المحلي ، ثم حدد التكوين التالي في النافذة المنبثقة:

- حدد الوضع `نسخ` (مزامنة من السحابة إلى الجهاز المحلي في اتجاه واحد) ، وقم بنسخ الملفات الجديدة والمتغيرة فقط ، واستخدمها للنسخ الاحتياطي.
- حدد `تخطي جميع الملفات الموجودة` في منطقة تخطي الملفات لتجنب تكرار التنزيل واستنفاد البيانات.
- أدخل اسم المهمة في منطقة وصف المهمة لسهولة الاستخدام في المرة القادمة.

بعد الانتهاء من التكوين ، انتقل إلى علامة التبويب المهام ، حدد المهمة المناسبة ، وانقر فوق `تشغيل` لبدء التنزيل.

## تكوين على NAS Synology

ملاحظة: يوصى باستخدام CloudSync على Synology ، وعدم تعديل الشفرة الأساسية.

الإعدادات اللازمة:

- تمكين ssh
- تمكين مجلد المستخدم (homes)
- إنشاء مجلد للمزامنة (مثل /volume1/wiki-media)

تثبيت Rclone:

```shell
curl https://rclone.org/install.sh | sudo bash
```

تكوين الخدمة:

```shell
rclone config
```

اتبع الخطوات المذكورة أعلاه.

أمر المزامنة:

```shell
# من الجهاز المحلي إلى السحابة
rclone [خيارات الوظيفة] <المسار المحلي> <اسم السحابة: المسار> [معلمات] [معلمات] ...

# من السحابة إلى الجهاز المحلي
rclone [خيارات الوظيفة] <اسم السحابة: المسار> <المسار المحلي> [معلمات] [معلمات] ...

# من السحابة إلى السحابة
rclone [خيارات الوظيفة] <اسم السحابة: المسار> <اسم السحابة: المسار> [معلمات] [معلمات] ...
```

على سبيل المثال ، أنا:

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

أنشئ ملف نصي تلقائيًا في المسار المحدد (مثل `rclone-sync.sh`) وضع الأمر أعلاه في ملف النص.

في `لوحة التحكم` - `مهام المجدولة` - `إضافة` - `مهمة مجدولة` - `نص محدد من قبل المستخدم` ، قم بتكوين وقت التشغيل الدوري ومسار البرنامج النصي.

1. في `لوحة التحكم` - `مهام المجدولة` - `إضافة` - `مهمة مجدولة` - `نص محدد من قبل المستخدم` ، قم بتكوين وقت التشغيل الدوري وأمر تشغيل البرنامج النصي (مثل `bash /volume1/stash/permanent/rclone-sync.sh`).
2. يمكن تكوين نتائج الإخراج في `الإعدادات` ، ثم حدد المهمة وانقر فوق `تشغيل` لاختبار التشغيل ، ويمكن فتح مسار الإخراج المكون للاطلاع على نتائج التشغيل. 

## المراجع والشكر

المصدر:

- [دليل تثبيت وتكوين واستخدام Rclone، مع شرح مفصل للمعلمات الشائعة في Rclone](https://www.wazhuji.com/jiaocheng/17.html)
- [إنشاء سحابة خاصة كاملة الميزات بتكلفة منخفضة باستخدام [تخزين الكائنات]](https://zhuanlan.zhihu.com/p/104628740)
- [تثبيت محرك أقراص Aliyun OSS / Tencent Cloud COS على نظام Windows باستخدام Rclone و WinFsp](https://www.boxmoe.com/486.html)
- [تثبيت محرك أقراص Google الشخصي / الفريقي باستخدام Rclone على نظام Windows](https://blog.rhilip.info/archives/874/)
- [نسخ احتياطي يومي بتوقيت محدد لمحتوى موقع Typecho وقاعدة بيانات MySQL إلى Google Drive / Onedrive وغيرها من خدمات التخزين السحابي باستخدام Rclone](https://omo.moe/archives/616/)'

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.