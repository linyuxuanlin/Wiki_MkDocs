# استخدام Rclone لمزامنة بيانات السحابة

Rclone هي أداة سطر الأوامر المستخدمة لإدارة ملفات السحابة، وتدعم أكثر من 40 نوعًا من الخدمات السحابية (بما في ذلك S3). يوجد أيضًا نسخة من Rclone بواجهة رسومية تسمى RcloneBrowser، والتي تسهل استخدامها للمستخدمين العامين. في هذه المقالة، سنتعرف على كيفية مزامنة بيانات Tencent Cloud Object Storage باستخدام Rclone.

## تثبيت البرامج

- [**Rclone**](https://rclone.org/downloads/) : قم بتنزيل الملف المضغوط وقم بفك الضغط عنه، واحفظ مسار التثبيت.
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases) : أداة واجهة رسومية لـ Rclone. بعد التثبيت، حدد مسار تثبيت Rclone.
- (اختياري) [**WinFsp**](http://www.secfs.net/winfsp/rel/) : مكتبة مطلوبة إذا كنت ترغب في تركيب قرص افتراضي.

## إعداد الاتصال

افتح RcloneBrowser وانقر على `Config...` في الزاوية السفلى اليسرى، ثم اتبع التعليمات التالية:

أدخل `n` لإنشاء اتصال جديد:

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

قم بتسمية الاتصال البعيد (مثال: `test`):

```shell
name> test
```

اختر مزود الخدمة (في هذا المثال، سنستخدم Tencent Cloud Object Storage)، اختر `4`:

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
```

مزود> 11
```

اختر نوع التوثيق. نظرًا لأننا نقوم بالتكوين للمرة الأولى ، فقم بتحديد `1`:

```shell
اختر رقمًا من الأرقام التالية ، أو اكتب القيمة الخاصة بك
 1 / أدخل بيانات اعتماد AWS في الخطوة التالية
   \ "false"
 2 / احصل على بيانات اعتماد AWS من البيئة (متغيرات البيئة أو IAM)
   \ "true"

env_auth> 1
```

أدخل حساب خدمة السحابة ، هنا يعتبر ما يعادل SecretId لـ Tencent COS:

```shell
معرف مفتاح الوصول لـ AWS.

access_key_id> ******
```

أدخل كلمة المرور ، وهي ما يعادل SecretKey:

```shell
مفتاح الوصول السري لـ AWS (كلمة المرور)

secret_access_key> ******
```

اختر منطقة خدمة السحابة:

```shell
نقطة نهاية لواجهة برمجة تطبيقات Tencent COS.
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

اختر نوع القراءة والكتابة ، حيث يكون الرفع العام والكتابة الخاصة هي الأكثر شيوعًا:

```shell
ACL المعتمدة عند إنشاء الحاويات وتخزين أو نسخ الكائنات.
 1 / المالك يحصل على السيطرة الكاملة. لا يمتلك أي شخص حقوق الوصول (الافتراضي).
   \ "default"
 2 / المالك يحصل على السيطرة الكاملة. يحصل مجموعة AllUsers على حق القراءة.
   \ "public-read"
   / المالك يحصل على السيطرة الكاملة. يحصل مجموعة AllUsers على حق القراءة والكتابة.
...

acl> 2
```

اختر نوع التخزين (اختر `1` كافتراضيًا):

```shell
فئة التخزين المستخدمة عند تخزين كائنات جديدة في Tencent COS.
 1 / الافتراضي
   \ ""
 2 / فئة التخزين القياسية
   \ "STANDARD"
 3 / وضع التخزين الأرشيفي.
   \ "ARCHIVE"
 4 / وضع التخزين ذو الوصول النادر.
   \ "STANDARD_IA"

storage_class> 1
```

هل ترغب في تحرير الإعدادات المتقدمة (اختر `n` لا):

```shell
تحرير التكوين المتقدم؟ (نعم / لا)
نعم) نعم
لا) لا (الافتراضي)

y/n> n
```

أكد في النهاية ، وبعد التحقق من الصحة ، أدخل `y`:

```shell
التكوين البعيد

[Txcos]
النوع = s3
المزود = TencentCOS
env_auth = false
access_key_id = xxx
secret_access_key = xxx
endpoint = cos.ap-guangzhou.myqcloud.com
acl = public-read

y) نعم ، هذا صحيح (الافتراضي)
e) تحرير هذا النظام البعيد
d) حذف هذا النظام البعيد
y/e/d> y
```

أدخل `q` للخروج:

```shell
المستودعات الحالية:

الاسم                 النوع
====                 ====
Txcos                 s3

e) تعديل المستودع الحالي
n) مستودع جديد
d) حذف المستودع
r) إعادة تسمية المستودع
c) نسخ المستودع
s) تعيين كلمة مرور التكوين
q) الخروج من التكوين
e/n/d/r/c/s/q> q
```

ثم، انقر مرتين لفتح الاتصال عن بُعد المكوّن مسبقًا، حدد المجلد وانقر على `تنزيل` لتنزيله محليًا. في النافذة المنبثقة، حدد التكوينات التالية:

- اختر وضع `نسخ` (مزامنة من السحابة إلى المحلي باتجاه واحد فقط)، وقم بنسخ الملفات الجديدة والمتغيرة فقط للاحتياط.
- حدد "تخطي الملفات الموجودة" في منطقة تخطي الملفات لتجنب تكرار التنزيل واستهلاك البيانات.
- أدخل اسم المهمة في منطقة وصف المهمة لسهولة الاستخدام في المزامنة المقبلة.

بمجرد الانتهاء من التكوين، انتقل إلى علامة التبويب "المهام"، حدد المهمة المناسبة، وانقر على `تشغيل` لبدء التنزيل.

## تكوين على NAS Synology

ملاحظة: يُوصى باستخدام CloudSync على NAS Synology وعدم تعديل الشفرة الأساسية.

الإعدادات الأولية:

- تمكين SSH
- تمكين مجلد المستخدم (homes)
- إنشاء مجلد للمزامنة (على سبيل المثال، `/volume1/wiki-media`)

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
# من المحلي إلى السحابة
rclone [خيارات الوظيفة] <المسار المحلي> <اسم السحابة:المسار> [معلمات] [معلمات] ...

# من السحابة إلى المحلي
rclone [خيارات الوظيفة] <اسم السحابة:المسار> <المسار المحلي> [معلمات] [معلمات] ...

# من السحابة إلى السحابة
rclone [خيارات الوظيفة] <اسم السحابة:المسار> <اسم السحابة:المسار> [معلمات] [معلمات] ...
```

على سبيل المثال،

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

قم بإنشاء نصي تلقائي في المسار المحدد (مثل `rclone-sync.sh`) وضع الأمر أعلاه في ملف النصي.

في "لوحة التحكم" - "مهام المجدولة" - "إضافة" - "مهمة مجدولة" - "نص محدد من قبل المستخدم"، قم بتكوين وقت التشغيل الدوري ومسار النص المشغل (مثل `bash /volume1/stash/permanent/rclone-sync.sh`).

يمكنك تكوين نتائج الإخراج في "الإعدادات"، ثم حدد المهمة وانقر على `تشغيل` لاختبار التشغيل وفتح مسار الإخراج المكون لعرض نتائج التشغيل.

## المراجعة والشكر
```

- [دليل تثبيت وتكوين واستخدام Rclone ، مع شرح مفصل للمعلمات الأكثر استخدامًا](https://www.wazhuji.com/jiaocheng/17.html)
- [إنشاء سحابة خاصة متكاملة بتكلفة منخفضة بناءً على [تخزين الكائنات]](https://zhuanlan.zhihu.com/p/104628740)
- [تعليق تخزين الأجهزة السحابية على ويندوز باستخدام Rclone و WinFsp لتحويل خدمات تخزين الأجهزة السحابية على Alibaba Cloud OSS / Tencent Cloud COS إلى أقراص ويندوز](https://www.boxmoe.com/486.html)
- [تعليق تثبيت خدمة تخزين السحابة الشخصية / الفريقية من Google باستخدام Rclone على نظام التشغيل ويندوز](https://blog.rhilip.info/archives/874/)
- [جدولة نسخ احتياطي يومي باستخدام Rclone لمحتوى موقع Typecho وقاعدة بيانات MySQL إلى Google Drive / Onedrive وغيرها من خدمات التخزين السحابي](https://omo.moe/archives/616/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.