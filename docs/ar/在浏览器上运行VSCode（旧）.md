````markdown
# تشغيل VS Code على المتصفح (الإصدار القديم)

ملاحظة: لنسخة code-server v3.8.0 أو أعلى، يُفضل الرجوع إلى [**كيفية تشغيل VS Code على iPad**](https://wiki-power.com/如何在iPad上运行VSCode) للحصول على وسيلة أبسط للنشر.

## الخلفية

من المعروف أنَّ VS Code هو محرر قوي للغاية. إذا كنا قادرين على استخدامه على منصات خفيفة مثل الآيباد (حيث دعم iPadOS للفأرة ولوحة المفاتيح قد يكون مماثلًا لأنظمة سطح المكتب)، فسيكون بإمكاننا العمل في أي وقت وفي أي مكان.

يوفر code-server خدمة تشغيل VS Code على الخادم بعد النشر، ويمكن الوصول إليها من خلال المتصفح. ببساطة، بمجرد توفر اتصال بالإنترنت، يمكن لأي جهاز الوصول بسهولة إلى VS Code.

## إعداد البيئة

سيرفر يعمل بنظام Linux (قمت باستخدام خادم الطلاب الأدنى المواصفات المقدمة من Alibaba Cloud).

المتطلبات الرسمية كالتالي:

> - مضيف بنية 64 بت.
> - على الأقل 1 غيغابايت من الذاكرة العشوائية (RAM).
> - يُفضل وجود معالج بـ 2 أو أكثر من نوى (يعمل المعالج بنواة واحدة ولكن بأداء أقل).
> - اتصال آمن عبر HTTPS أو localhost (مطلوب لخدمة الأعمال ودعم الحافظة).
> - بالنسبة لنظام Linux: GLIBC 2.17 أو أحدث وGLIBCXX 3.4.15 أو أحدث.

## عملية التثبيت

### 1. التنزيل

```shell
wget https://github.com/cdr/code-server/releases/download/3.1.0/code-server-3.1.0-linux-x86_64.tar.gz # تنزيل code-server
```
````

لا تقم بنسخ الأمر كما هو. يُفضل نسخ رابط أحدث إصدار من [**صفحة الإصدارات**](https://github.com/cdr/code-server/releases) لـ code-server (اعتمادًا على هندسة الخادم) واستخدام أمر `wget` أو `SFTP` لتنزيله/نقله إلى الخادم.

إذا كانت سرعة التنزيل بطيئة، يمكنك نسخ الرابط واستخدام موقع [**تسريع ملفات GitHub**](https://gh.api.99988866.xyz/) للحصول على رابط تنزيل مُسرع في الصين.

```shell
tar -xvf code-server-3.1.0-linux-x86_64.tar.gz # فك الضغط
```

### 2. التثبيت

```shell
cd code-server
export PASSWORD="كلمة_المرور"
./code-server --port 8888 --host 0.0.0.0
```

- قم بتغيير "كلمة_المرور" إلى كلمة المرور التي تفضلها، وإلا ستتم إنشاء كلمة مرور عشوائية.
- `--port 8888` تعني تحديد منفذ التشغيل، يمكنك تعيينه إلى المنفذ 80 (بروتوكول HTTP) حتى لا تحتاج إلى إضافة رقم المنفذ عند الوصول إليه.
- `--host 0.0.0.0` يتيح الخدمة الوصول عبر الإنترنت. القيمة الافتراضية `127.0.0.1` تسمح فقط بالوصول المحلي.
- إذا لم تكن بحاجة إلى التحقق من كلمة المرور، يمكنك إضافة `--auth none`.
- إذا لم يتم بدء الخدمة بنجاح، فقد يكون السبب في اختيار **إصدار هندسة المعالج** خاطئ، في هذه الحالة قم باختيار إصدار آخر.

### 3. تكوين التشغيل في الخلفية

بشكل افتراضي، عند تشغيل الخدمة مباشرة، يتم إيقافها عند فصل الاتصال بـ SSH. لجعلها قائمة بالتشغيل في الخلفية، يمكنك استخدام `screen`:

```shell
yum install screen
أو
apt-get install screen
```

````shell
screen -S VSCode-online # VS Code-online هو اسم يمكنك اختياره بنفسك

إذا كنت بحاجة إلى إيقاف تشغيل خدمة الشاشة في الخلفية:

```shell
screen -ls # عرض معرف الخدمة التي تعمل بالفعل
screen -X -S id quit # استبدال id بالمعرف الصحيح
````

للخروج من الشاشة: `Ctrl + A + D`

### 4. الاستخدام السهل

قم بفتح متصفح الويب وادخل `http://عنوان الخادم الخاص بك` للاستمتاع بـ VS Code عبر الإنترنت.

![صورة](https://media.wiki-power.com/img/20200413181001.jpg)

لتكوين الوصول عبر النطاق: `تحتاج إلى البحث والاستكشاف...`

## المشكلات الحالية

- عدد الإضافات التي يمكن تنزيلها مباشرة محدود، وتثبيت الإضافات يتطلب جهدًا يدويًا ولا يتم مزامنتها تلقائيًا مع إعدادات المستخدم، ومن المفترض أن تتم تحديثات لحل هذه المشكلة في الإصدارات المستقبلية.

## المراجع والشكر

- [تشغيل VS Code في المتصفح باستخدام code-server (خادم Alibaba Cloud)](https://copyfuture.com/blogs-details/20200405045150018h4edt0f4q8486jq)
- [تشغيل VS Code في المتصفح باستخدام code-server](https://segmentfault.com/a/1190000022267386)
- [أداة VS Code عبر الإنترنت الموصى بها - تثبيت واستخدام code-server على خادم السحابة مع حلول المشكلات الشائعة (تفصيل مفصل)](https://blog.csdn.net/Granery/article/details/90415636)
- [بيئة تعلم البرمجة على iPad - إعداد إصدار VS Code عبر الويب](https://blog.icodef.com/2019/11/17/1670)

> مؤلف المقال: **Power Lin**
> العنوان الأصلي: <https://wiki-power.com>
> إعلان حقوق النشر: يُسمح بإعادة النشر بموجب ترخيص [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يرجى ذكر المصدر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
