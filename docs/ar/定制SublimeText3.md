# تخصيص SublimeText3

## الخلفية

**Sublime Text** هو محرر نصي قوي جداً. بسبب دورتي الدراسية القادمة في الفصل القادم المتعلقة بلغة Python، وبما أن واجهة استخدام أدوات مثل PyCharm قد تكون غير جذابة بالنسبة لي، أرغب في تجربة تخصيص Sublime Text لتحويله إلى أداة تطوير Python قوية.

صورة توضيحية للتخصيص:
![](https://media.wiki-power.com/img/ST3效果.png)

## [النشر البسيط](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. حمل خط "Consolas-with-Yahei" وقم بفك الضغط ثم قم بتثبيته.
2. حمل [**Sublime Text 3** المخصص من قِبلي](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB) (التحديث غير مضمون).
3. قم بتشغيل ملف ".exe" مباشرةً. لمزيد من التكوينات المفصلة، يُرجى الاطلاع على الجزء التالي.

## تكوين مفصل

### تنزيل وتثبيت البرنامج

يمكن تنزيل Sublime Text 3 من [الموقع الرسمي](http://www.sublimetext.com/) (يُفضل تنزيل [**الإصدار القابل للتثبيت بدون تثبيت**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip)) والبرنامج مجاني للاستخدام، ولكن في بعض الأحيان قد تظهر نوافذ دفع. بناءً على طلب، تمت إزالة الكود التسلسلي من المقالة. إذا كنت بحاجة إليه، فلا تتردد في الاتصال بي.

### مدير الحزم وتثبيت الإضافات

لتثبيت مدير الحزم: اذهب إلى "Preferences" ثم اختر "Install Package Control". بعد ذلك، يُمكن الوصول إلى واجهة مدير الحزم بسرعة باستخدام اختصار لوحة المفاتيح "Ctrl + Shift + P".

لتثبيت الإضافات: قم بفتح واجهة مدير الحزم باستخدام "Package Control" ثم اكتب "Install Package" واضغط على Enter. انتظر بصبر حتى تظهر الإضافات المطلوبة في الواجهة التي ستظهر بعد ذلك. بالنسبة للإضافات غير المنشورة، يُمكنك ببساطة اختيار "Preference -> Browser packages" وفتح مجلد تخزين الإضافات، ثم قم بإضافة الإضافات مباشرةً.

### الدعم للغة الصينية

1. الترجمة إلى اللغة الصينية: استخدم "Package Control" للبحث عن "ChineseLocalizations" ثم قم بتثبيته.
2. مشكلة إدخال النص باللغة الصينية: قم بتنزيل [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip)، ثم قم بفك الضغط على الملفات في مجلد تثبيت الإضافات. أعد تشغيل Sublime لحل مشكلة عدم متابعة إطار الإدخال عند إدخال نص باللغة الصينية.
3. الخطوط الصينية: قم بتنزيل الخط "Consolas-with-Yahei" وقم بتثبيته، ثم استبدل الإعدادات الخطوط في إعدادات المستخدم بالآتي: `"font_face": "Consolas-with-Yahei",`.

### تصميم الواجهة

الثيم الداكن الذي أستخدمه: استخدم "Package Control" للبحث عن "Spacegray" و "Afterglow" ثم استبدل الإعدادات في إعدادات المستخدم بالآتي:

```
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
"theme": "Afterglow-green.sublime-theme"
```

### تعديلات دقيقة

يمكنك إضافة الأكواد التالية في إعدادات المستخدم:

````
"word_wrap": "true", // التفاف النص عندما يتم تجاوز الشاشة
"fold_buttons": true, // تفعيل طي الأكواد
"fade_fold_buttons": true, // إخفاء أزرار الطي تلقائيًا
"tab_size": 4, // عدد الفراغات في التباعد
"margin": 4, // المساف

يمكن تثبيت الإضافات التالية مباشرةً باستخدام `Package Control`.

- **StyleToken**: يعرض الألوان (RGB) التي يُمثلها الشيفرة.

- **FileHeader**: يمكنك تخصيص قوالب الملفات. اذهب إلى `Preferences -> Package Settings -> FileHeader -> Settings - User`، وانسخ محتوى القالب الافتراضي (`Default`) إلى القالب الخاص بالمستخدم (`User`) وعدل المعلومات الشخصية كالتالي:

```json
{
    "Default": {
        "author": "linyuxuanlin",
        "email": "824676271@qq.com",
        "website": "yxrct.com"
    }
}
````

بعد ذلك، يمكنك تخصيص محتوى القالب في `Preferences -> Browse Packages... -> FileHeader -> template -> header أو body`.

**مثال على النتيجة:**  
![نموذج FileHeader](https://media.wiki-power.com/img/ST3 模板效果.png)

### تشغيل Python

نظرًا لعدم وجود مُدمج للإدخالات من المستخدم في الكود الخاص بـ Sublime Text، يلزم تثبيت إضافة `SublimeREPL` باستخدام `Package Control`. بعد التثبيت، قم بإضافة اختصار لتشغيله في `Preferences —> Key Buildings -> User` كالتالي:

```json
[
  {
    "keys": ["f5"],
    "caption": "SublimeREPL:Python",
    "command": "run_existing_window_command",
    "args": {
      "id": "repl_python_run",
      "file": "config/Python/Main.sublime-menu"
    }
  }
]
```

بعد ذلك، يمكنك تشغيل الكود Python مباشرةً باستخدام `F5`.

### تنسيق الشيفرة تلقائيًا

يمكنك تثبيت إضافة `Python PEP8 Autoformat` وإضافة اختصار لتنسيق شيفرة Python باستخدام `Alt + R` كالتالي:

```json
{ "keys": ["alt+r"], "command": "pep8_autoformat" }
```

## الاستنتاج

المظهر يعكس الإنتاجية. Sublime Text ليس مقتصرًا على دعم Python فقط، بل يمكن استخدامه لفتح وتحرير معظم تنسيقات الملفات. عند استخدامه بذكاء، يمكن أن يكون البرمجة في واجهة بسيطة وقوية أمرًا رائعًا.

## المراجع والشكر

- [Sublime Text 3 تعديل أداة الإنتاج الشخصية (الجزء الأول)](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [استخدام إضافة FileHeader لتوليد رأس الملف ومعلومات حقوق الطبع والنشر في Sublime Text](https://blog.csdn.net/afei__/article/details/82890493)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
