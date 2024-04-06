# دليل إنتاجية VS Code - إعداد البيئة

—— كيفية استخدام VS Code لبناء أداة إنتاجية فعّالة.

![](https://media.wiki-power.com/img/20200319135609.png)

## الخلفية

> "العدول عن أفعالك وجعلها أفضل هو الغاية الحقيقية. الإبداع شيء جميل، وإذا تم دعمه بأدوات جيدة، سيصبح هذا العمل أكثر راحة."

### لماذا نختار استخدام VS Code؟

- مفتوح المصدر ومجاني، وأنيق المظهر.
- ميزات تحرير متقدمة (إكمال ذاتي، تمييز القواعد اللغوية، وما إلى ذلك).
- القدرة على تصحيح الشفرة مباشرة في المحرر.
- دمج Git.
- دعم مكملات متنوعة وإمكانية تخصيص البيئة.

## تثبيت البرامج

يمكنك تنزيل أحدث نسخة من VS Code من الموقع الرسمي: <https://code.visualstudio.com/>

عادةً ما نختار تنزيل الإصدار "المستقر". إذا كنت غير متضايق من وجود أخطاء وترغب في تجربة أحدث الميزات، يمكنك أيضًا جرب الإصدار "المتداول".

بعد الانتهاء من التثبيت، ستظهر لنا الشاشة الافتتاحية أولًا:

![](https://media.wiki-power.com/img/20200318224855.png)

## تثبيت المكملات

لتقليل حجم تثبيت VS Code، تأتي البرنامج افتراضيًا مع الوظائف الأساسية فقط. ومع ذلك، إذا كنت ترغب في زيادة الإنتاجية، لن تكون هذه الوظائف كافية.  
لحسن الحظ، يمكنك الاستفادة من مجموعة متنوعة من المكملات من طرف ثالث لتلبية احتياجاتك.

نقترح بعض المكملات المفيدة (يمكنك النقر مباشرة على الروابط للتثبيت):

### الأساسية

- [**حزمة اللغة الصينية (المبسطة)**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans): تضيف الدعم للغة الصينية (المبسطة) إلى VS Code.
- [**مزامنة الإعدادات**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync): تمكين مزامنة إعداداتك والمكملات عبر عدة أجهزة.
  - **الإعدادات**: قم بتكوين "معرف GitHub Gist" و "رمز الوصول إلى GitHub".
  - **الاستخدام**: استخدم "Shift + Alt + U" للتحميل و "Shift + Alt + D" للتنزيل.
  - (من المهم ملاحظة أن VS Code الأحدث يدعم ميزة المزامنة بشكل مدمج، لكن هذا المكمل مفيد إذا كنت بحاجة لإدارة إصدارات مخصصة).

### تنسيق Markdown

- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one): تقدم دعمًا أقوى للتنسيقات المختلفة في Markdown.
- [**Markdown Paste Image**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus): تسمح بلصق الصور في ملفات Markdown ونسخها إلى المجلد /res.
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown): تحسين تنسيق النص في Markdown (إضافة مسافات بين النصوص الصينية والإنجليزية، وتبديل علامات الترقيم بتنسيق قياسي).
  - **الإعدادات**: قم بتمكين التنسيق التلقائي عند حفظ الملف.
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc): توفير دعم لتصدير الملفات Markdown إلى تنسيقات مثل PDF وWord وHTML.
  - **الإعدادات**: تأكد من تثبيت [Pandoc](https://pandoc.org/installing.html) أولاً.

### تحسين المظهر

- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator): يسلط الضوء على عمق التنسيق في الشفرة
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): يضيف رموزًا جذابة لتنسيق ملفات مختلفة

### لغات البرمجة

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### تطوير الواجهة الأمامية

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): أداة تنسيق تلقائية للغات مثل HTML/CSS/JavaScript وغيرها
  - **الاستخدام**: `Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager): معاينة مباشرة للألوان المقابلة للقيم اللونية
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): تشغيل صفحات الويب المحلية داخل VS Code

### أدوات أخرى

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate): توفير خدمة الترجمة داخل VS Code
  - **الاستخدام**: `Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash): إضافة الوحدة النمطية "bash" إلى محطة الأوامر في VS Code
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng): ضغط الصور
  - **الإعدادات**: قم بتعيين "TinyPNG API Key" الصحيح
  - **الاستخدام**: انقر بزر الماوس الأيمن على الصورة داخل شجرة الملفات - `TinyPNG: ضغط`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu): ضروري لتصفح جريدة Zhihu داخل VS Code
- [**محفز كون كون**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk): بمجرد البرمجة المتواصلة لمدة ساعة، ستحصل على تذكير برقصة سلة حصرية لـ Cai Xukun لتذكيرك بأهمية الاستراحة

## السمات

يمكنك اختيار سمة تناسب ذوقك الخاص من خلال الانتقال إلى "ملف - تفضيلات - سمات الألوان". على سبيل المثال، اخترت سمة "Monokai Dimmed" كما هو موضح أدناه:

![](https://media.wiki-power.com/img/20200319132727.png)

إذا شعرت أن السمات الافتراضية المقدمة غير كافية، يمكنك أيضًا البحث وتنزيل سمات أخرى تناسب ذوقك من داخل متجر الإضافات باستخدام الكلمة الرئيسية "theme".

## الإعدادات الشائعة

عند استخدام VS Code لأول مرة، يمكنك تعديل بعض الإعدادات الشائعة لجعل البرنامج يعمل بشكل أفضل. يمكنك الوصول إلى صفحة الإعدادات من خلال "ملف - تفضيلات - الإعدادات".

### الحفظ التلقائي

يُمكن تعيين `Files: Auto Save` على أي إعداد غير `إيقاف` الثلاثة الأخرى. في الاستخدام اليومي، الحفظ التلقائي ضروري.

### الخطوط

الخطوط الثابتة ضرورية عند كتابة الشيفرة. أنصح شخصياً بخط [**Microsoft YaHei Mono**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf).

بمجرد تنزيل ملف الخط .ttf، قم بتثبيته وأعد تشغيل VS Code، ثم انتقل إلى `الإعدادات - محرر النصوص - الخط - Font Family` وأضف `'Microsoft YaHei Mono'` إلى الجزء العلوي. ستتمكن من استخدام الخط بنجاح.

## اختصارات شائعة

|        الإجراء         |          الاختصار          |
| :--------------------: | :------------------------: |
|      لوحة الأوامر      | `F1` أو `Ctrl + Shift + P` |
|         الطرف          | <code>Ctrl + &#96;</code>  |
|      مدير الملفات      |     `Ctrl + Shift + E`     |
|      البحث الشامل      |     `Ctrl + Shift + F`     |
|      مدير الشيفرة      |     `Ctrl + Shift + G`     |
|        التشغيل         |     `Ctrl + Shift + D`     |
|     إدارة الإضافات     |     `Ctrl + Shift + X`     |
| التبديل السريع للملفات |         `Ctrl + D`         |

## مراقبة الشيفرة المصدرية

هل تحتاج دائمًا إلى إدخال اسم المستخدم وكلمة المرور عند التوصيل بـ Github؟
استخدم الأمر التالي:

```shell
git config --global credential.helper store
```

أعد تشغيل VS Code وستكون جاهزًا.

## تلخيص

هذا هو تكوين بيئة VS Code الأساسي. في المقالة التالية، سنتناول بالتفصيل Git، Jupyter Notebook، وطرق إنشاء قواعد الشيفرة الخاصة بالمستخدم وغيرها من الإجراءات. ترقبوا ذلك!

### روابط مرجعية

- [المستندات · Visual Studio Code](https://code.visualstudio.com/docs)
- [لماذا اخترت استخدام VS Code لتطوير الواجهة الأمامية؟](https://zhuanlan.zhihu.com/p/28631442)
- [VS Code دائمًا يطلب إدخال اسم المستخدم وكلمة المرور](https://www.jianshu.com/p/8854713433c5)
- [كيفية تحرير أكواد الـ markdown في Visual Studio Code](https://www.jianshu.com/p/a87e9ca2d208)
- [إضافة مقاطع الشيفرة المخصصة في Visual Studio Code](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
