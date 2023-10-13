# دليل إنتاجية VS Code - إعداد البيئة

- كيفية استخدام VS Code لإنشاء أدوات إنتاجية فعالة.

![](https://img.wiki-power.com/d/wiki-media/img/20200319135609.png)

## الخلفية

> لتكون جيدًا في العمل ، يجب أن تكون الأدوات جيدة. الإبداع هو شيء جميل ، وإذا كان لديك أدوات جيدة ، فسيصبح هذا العمل أكثر راحة.

### لماذا تستخدم VS Code؟

- مفتوح المصدر ومجاني وجميل المظهر
- ميزات تحرير متكاملة (إكمال تلقائي ، تمييز الصيغ ، إلخ)
- يمكن تصحيح الأخطاء مباشرة في محرر النصوص
- دمج Git
- دعم مكونات إضافية وخيارات تخصيص غنية

## تثبيت البرنامج

يمكنك تنزيل أحدث إصدار من موقع VS Code الرسمي: <https://code.visualstudio.com/>

عادةً ما نختار تنزيل الإصدار الثابت. إذا كنت لا تخاف من الأخطاء وتريد تجربة أحدث الميزات ، فيمكنك أيضًا تجربة إصدار Insiders.

بعد تنزيل وتثبيت البرنامج ، نفتحه ، وأول شيء نراه هو صفحة البدء:

![](https://img.wiki-power.com/d/wiki-media/img/20200318224855.png)

## تثبيت المكونات الإضافية

لتقليل حجم البرنامج ، يحتفظ VS Code فقط ببعض الوظائف الأساسية. ومع ذلك ، إذا كنت ترغب في زيادة الإنتاجية ، فلن تكون هذه الوظائف كافية.  
ولحسن الحظ ، يوجد العديد من المكونات الإضافية الخارجية المختلفة في VS Code التي يمكن استخدامها حسب الحاجة.

فيما يلي بعض المكونات الإضافية الجيدة (يمكن النقر مباشرةً على الروابط للتثبيت):

### الأساسية

- [**Chinese (Simplified) Language Pack**](https://marketplace.visualstudio.com/items?itemName=MS-CEINTL.vscode-language-pack-zh-hans)：تحويل VS Code إلى اللغة الصينية
- [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync)：نسخ احتياطي للإعدادات والمكونات الإضافية ، ومزامنتها عبر الأجهزة المختلفة
  - **الإعدادات**：تكوين معرف GitHub Gist ورمز الوصول إلى GitHub المناسب
  - **الاستخدام**：`Shift + Alt + U` للتحميل ، `Shift + Alt + D` للتنزيل
  - (تحتوي أحدث إصدارات VS Code على ميزة المزامنة الخاصة بها ، ولكن إذا كنت بحاجة إلى إدارة الإصدارات ، فيمكنك استخدام هذا المكون الإضافي)

### Markdown

- [**Markdown All in One**](https://marketplace.visualstudio.com/items?itemName=yzhang.markdown-all-in-one)：توفير دعم أقوى لصيغ Markdown
- [**Markdown Paste Image**](https://marketplace.visualstudio.com/items?itemName=onesdev.vscode-paste-image-plus)：لصق الصور في Markdown ونسخها إلى مجلد /res
- [**Pangu-Markdown**](https://marketplace.visualstudio.com/items?itemName=xlthu.Pangu-Markdown)：تنسيق صيغ Markdown (إضافة مسافات بين النصوص الصينية والإنجليزية ، واستبدال علامات الترقيم بالأشكال القياسية ، إلخ)
  - **الإعدادات**：تمكين التنسيق التلقائي عند الحفظ
- [**vscode-pandoc**](https://marketplace.visualstudio.com/items?itemName=DougFinke.vscode-pandoc)：زيادة دعم Pandoc ، وتصدير Markdown إلى صيغ PDF / Word / HTML ، إلخ.
  - **الإعدادات**：تأكد من تثبيت [Pandoc](https://pandoc.org/installing.html) أولاً

### التجميل



- [**Indenticator**](https://marketplace.visualstudio.com/items?itemName=SirTori.indenticator): يظهر عمق المسافات في الكود بألوان مختلفة
- [**vscode-icons**](https://marketplace.visualstudio.com/items?itemName=vscode-icons-team.vscode-icons): يضيف أيقونات جميلة لملفات مختلفة

### لغات البرمجة

- [**C/C++**](https://marketplace.visualstudio.com/items?itemName=ms-vscode.cpptools)
- [**Python**](https://marketplace.visualstudio.com/items?itemName=ms-python.python)

### تطوير الواجهة الأمامية

- [**Prettier - Code formatter**](https://marketplace.visualstudio.com/items?itemName=esbenp.prettier-vscode): أداة تنسيق تلقائي للغات الواجهة الأمامية مثل HTML/CSS/JavaScript
  - **الاستخدام**: `Ctrl + Shift + P`
- [**Color Manager**](https://marketplace.visualstudio.com/items?itemName=RoyAction.color-manager): يعرض اللون المقابل لقيمة اللون مباشرةً
- [**Live Server**](https://marketplace.visualstudio.com/items?itemName=ritwickdey.LiveServer): يشغل صفحات الويب المحلية داخل VS Code

### غيرها

- [**Google Translate**](https://marketplace.visualstudio.com/items?itemName=hancel.google-translate): يوفر خدمة الترجمة داخل VS Code
  - **الاستخدام**: `Ctrl + Alt + T`
- [**Start git-bash**](https://marketplace.visualstudio.com/items?itemName=McCarter.start-git-bash): يضيف `bash` إلى الطرفية الخاصة بـ VS Code
- [**TinyPNG**](https://marketplace.visualstudio.com/items?itemName=andi1984.tinypng): يضغط الصور
  - **الإعدادات**: تعيين مفتاح `TinyPNG API Key` الصحيح
  - **الاستخدام**: انقر بزر الماوس الأيمن على الصورة في شجرة الملفات - `TinyPNG:Compress`
- [**Zhihu Daily**](https://marketplace.visualstudio.com/items?itemName=YRM.zhihu): يمكنك تصفح صفحة الأخبار اليومية في Zhihu داخل VS Code
- [**坤坤鼓励师**](https://marketplace.visualstudio.com/items?itemName=sakura1357.cxk): يذكرك بأداء رقصة كرة السلة الخاصة بـ Cai Xukun بعد العمل لمدة ساعة

## السمات

يمكنك اختيار سمة تناسبك من خلال `ملف - التفضيلات - السمات اللونية`، على سبيل المثال، اخترت سمة `Monokai Dimmed`:

![](https://img.wiki-power.com/d/wiki-media/img/20200319132727.png)

إذا كنت ترى أن السمات الافتراضية غير كافية، يمكنك البحث عن سمات أخرى في متجر الإضافات باستخدام الكلمات الرئيسية `theme`.

## الإعدادات الشائعة

يمكنك تغيير بعض الإعدادات الشائعة لجعل استخدام VS Code أكثر سلاسة. يمكن الوصول إلى صفحة الإعدادات من خلال `ملف - التفضيلات - الإعدادات`.

### الحفظ التلقائي

```json
"files.autoSave": "onFocusChange"
```

يمكنك تعيين الحفظ التلقائي لتحفظ التغييرات تلقائيًا عند تغيير التركيز من ملف إلى آخر.

يمكن تعيين "Files: Auto Save" على 3 خيارات بخلاف "إيقاف"، ويعتبر الحفظ التلقائي ضروريًا في الاستخدام اليومي.

### الخطوط

الخط الثابت ضروري لكتابة الشفرات، وأنصح بشخصيًا بخط [**Microsoft YaHei Mono**](https://github.com/linyuxuanlin/File-host/blob/main/software-development/Microsoft-YaHei-Mono.ttf).

بعد تنزيل ملف الخط .ttf وتثبيته، أعد تشغيل VS Code وأضف `'Microsoft YaHei Mono'` إلى الجزء العلوي من خيار `Settings - Text Editor - Font - Font Family` لتمكين الخط.

## الاختصارات الشائعة

| العملية | الاختصار |
| :----------: | :------------------------: |
|   لوحة الأوامر   | `F1` أو `Ctrl + Shift + P` |
|     الطرفية     | <code>Ctrl + &#96;</code>  |
|  مدير الملفات  |     `Ctrl + Shift + E`     |
|   البحث الشامل   |     `Ctrl + Shift + F`     |
| مدير الشفرات المصدرية |     `Ctrl + Shift + G`     |
|     التشغيل     |     `Ctrl + Shift + D`     |
|   مدير المكونات الإضافية   |     `Ctrl + Shift + X`     |
| التبديل السريع بين الملفات |         `Ctrl + D`         |

## التحكم في الشفرات المصدرية

هل تحتاج إلى إدخال اسم المستخدم وكلمة المرور في Github في كل مرة تقوم بالتحميل؟
أدخل الأمر:

```shell
git config --global credential.helper store
```

وأعد تشغيل VS Code.

## الخلاصة

هذه هي الإعدادات الأساسية لـ VS Code، وسيتم مناقشة Git و Jupyter NoteBook وشفرات المستخدمين في المقالة القادمة، فترقبوها.

### الروابط المرجعية

- [Docs · Visual Studio Code](https://code.visualstudio.com/docs)
- [Why I Switched From Sublime Text To Visual Studio Code](https://hackernoon.com/why-i-switched-from-sublime-text-to-visual-studio-code-d4c9f3cba6df)
- [vscode git 提交总让输入用户名及密码](https://www.jianshu.com/p/8854713433c5)
- [Vscode 编辑 markdown 代码块（snippets）](https://www.jianshu.com/p/a87e9ca2d208)
- [在 Visual Studio Code 中添加自定义的代码片段](https://blog.walterlv.com/post/add-custom-code-snippet-for-vscode.html##%E5%85%B3%E4%BA%8E%E6%96%87%E4%BB%B6%E5%90%8D%E7%A7%B0)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.