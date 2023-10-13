# تخصيص SublimeText3

## الخلفية

**Sublime Text** هو محرر نصوص قوي للغاية. بسبب وجود دورة دراسية ذات صلة بـ Python في الفصل الدراسي القادم ، ولأن واجهة المستخدم لأدوات مثل Pycharm قبيحة إلى حد ما ، أردت تجربة تحويل Sublime Text إلى أداة تطوير Python.

صورة للتخصيص بعد التطبيق:
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/ST3效果.png)

## [نشر بسيط](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB)

1. قم بتنزيل خط `Consolas-with-Yahei` وقم بتثبيته بعد فك الضغط.
2. قم بتنزيل [**Sublime Text 3**](https://www.jianguoyun.com/p/Da9TMr0Q-OOjBxif86sB) المخصص من قبلي (لا يتم ضمان التحديثات).
3. قم بتشغيل ملف `.exe` مباشرةً ، لمزيد من التفاصيل حول تكوين المعلمات ، يرجى الرجوع إلى النص أدناه.

## تكوين مفصل

### تنزيل وتثبيت البرنامج

يمكن تنزيل Sublime Text 3 من [الموقع الرسمي](http://www.sublimetext.com/) (يوصى بتنزيل [**الإصدار القابل للتثبيت**](https://download.sublimetext.com/Sublime%20Text%20Build%203176%20x64.zip)). يمكن استخدام البرنامج مجانًا ، ولكن في بعض الأحيان يمكن أن تظهر رسائل تذكيرية بالدفع. بعد التذكير ، تم حذف الرقم التسلسلي من المقالة. يرجى الاتصال بي إذا كنت بحاجة إليه.

### تثبيت مدير الحزم والإضافات

تثبيت مدير الحزم: `Preferences -> Install Package Control` ، بعد ذلك يمكن استخدام اختصار لوحة المفاتيح `Ctrl + Shift + P` لسرعة استدعاء واجهة مدير الحزم.

تثبيت الإضافات: استدعاء واجهة `Package Control` ، ثم اكتب `Install Package` ، ثم اضغط على Enter ، وانتظر بصبر ، ثم ابحث في الواجهة التي ستظهر لاحقًا عن الإضافة المطلوبة وانقر فوق تثبيت. بالنسبة للإضافات غير المنشورة ، يمكنك ببساطة اختيار `Preference -> Browser packages` ، وفتح مجلد الإضافات ، ووضع الإضافة مباشرةً فيه.

إلغاء تثبيت الإضافات: استدعاء واجهة `Package Control` ، ثم اكتب `remove package`.

### التكيف مع اللغة الصينية

1. التعريب: ابحث عن `ChineseLocalizations` باستخدام `Package Control` وانقر على تثبيت.
2. مشكلة الإدخال الصيني: قم بتنزيل [IMESupport](https://github.com/zcodes/IMESupport/archive/master.zip) ، وفك الضغط في مجلد التثبيت الإضافي ، وأعد تشغيل Sublime ، لحل مشكلة عدم متابعة مربع الإدخال عند إدخال النص الصيني.
3. الخط الصيني: قم بتنزيل `Consolas-with-Yahei` ، وفك الضغط وقم بتثبيته ، ثم استبدل `"font_face": "Consolas-with-Yahei",` في إعدادات المستخدم.

   **الموضوع**

الموضوع الداكن الذي استخدمته: ابحث عن `Spacegray` و `Afterglow` باستخدام `Package Control` ، واستبدله في إعدادات المستخدم بـ:

```
"color_scheme": "Packages/Theme - Spacegray/base16-ocean.dark.tmTheme",
"theme": "Afterglow-green.sublime-theme"
```

### تعديلات الأدق

يمكن إضافة الكود التالي في إعدادات المستخدم:

```
"word_wrap": "true", // السطور الطويلة تلتف تلقائيًا
"fold_buttons": true, // تمكين طي الكود
"fade_fold_buttons": true, // إخفاء أزرار الطي تلقائيًا
"tab_size": 4, // عدد المسافات المستخدمة للتباعد
"margin": 4, // المسافة بين النص والحافة
"tabs_small": true, // تصغير شريط التبويب
"trim_trailing_white_space_on_save": true, // إزالة المسافات الزائدة في نهاية السطر تلقائيًا
"ensure_newline_at_eof_on_save": true, // حفظ سطر فارغ في نهاية الملف ، يمكن استخدامه في لغة C
```

### الإضافات الموصى بها



يمكن تثبيت الإضافات التالية مباشرةً باستخدام `Package Control`.

**StyleToken**: يعرض اللون (RGB) الذي يمثله الكود. **FileHeader**: يخصص قالب الملف. افتح `Preferences -> Package Settings -> FileHeader -> Settings - User` ، انسخ محتويات `Default` إلى `User` وقم بتعديل المعلومات الشخصية مثل:

```
{
    "Default": {
        "author": "linyuxuanlin",
        "email": "824676271@qq.com",
        "website": "yxrct.com"
    }
}
```

قم بتعديل محتويات القالب في `Preferences -> Browse Packages... -> FileHeader -> template -> header أو body`. النتيجة:  
 ![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/ST3 模板效果。png)

### تشغيل Python

نظرًا لعدم وجود مدخلات المستخدم في المترجم المضمَّن، يلزم استخدام الإضافة التالية: `SublimeREPL`. يمكن تثبيتها مباشرةً باستخدام `Package Control` وإضافة اختصار لوحة المفاتيح في `Preferences —> Key Buildings -> User`:

```
[
    { "keys": ["f5"], "caption": "SublimeREPL:Python",
                      "command": "run_existing_window_command", "args":
                      {
                           "id": "repl_python_run",
                           "file": "config/Python/Main.sublime-menu"
                      }
    },
]
```

بعد ذلك، يمكن تشغيل الكود Python مباشرةً باستخدام `F5`.

### تنسيق الكود تلقائيًا

يمكن تثبيت الإضافة `Python PEP8 Autoformat` وإضافة اختصار لوحة المفاتيح في `Key Buildings`:

```
{ "keys": ["alt+r"], "command": "pep8_autoformat" },
```

يمكن استخدام `Alt + R` لتنسيق كود Python.

## الخلاصة

الجمال يعني الإنتاجية. لا يدعم Sublime Text فقط Python، بل يمكن استخدامه لتحرير معظم صيغ الملفات. إذا تم ضبطه بشكل صحيح، يمكن البرمجة في واجهة بسيطة وقوية، وهذا يعد شيئًا رومانسيًا.

## المراجع والشكر

- [Sublime Text 3 调教你的私人利器（上）](https://www.sheyilin.com/2015/05/sublime_text_3_tiao_jiao_ni_de_si_ren_li_qi_1/)
- [Sublime Text 自动生成文件头部注释（版权信息）：FileHeader 插件的使用](https://blog.csdn.net/afei__/article/details/82890493)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.