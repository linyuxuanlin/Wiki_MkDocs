# استخدام Watchtower لتحديث الحاويات تلقائيًا (Docker على Synology)

استخدم Watchtower لتحديث الحاويات على Synology Docker تلقائيًا.

## تنزيل الصورة داخل تطبيق Docker على Synology

افتح حزمة Docker على Synology وقم بتنزيل صورة `containrrr/watchtower`.

## تكوين Watchtower في مهمة مجدولة

افتح لوحة التحكم في Synology - جدول المهام - إضافة - مهمة مجدولة - سكربت مُعرف بالمستخدم، ثم اتبع الإعدادات التالية:

![](https://media.wiki-power.com/img/202301092319956.png)

![](https://media.wiki-power.com/img/202301092321592.png)

السكربت الذي يجب استخدامه:

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

يرجى ملاحظة أن "calibre-web freshrss code-server" في نهاية السكربت تمثل أسماء الحاويات التي ترغب في تحديثها. قم بتعديلها لتناسب الحاويات التي تريد تحديثها أو اتركها فارغة لتحديث جميع الحاويات.

قم بحفظ الإعدادات وتشغيل السكربت لتنفيذ تحديثات الحاويات بانتظام.

## المراجعة والشكر

- [كيفية تحديث حاويات Docker على Synology باستخدام أمر واحد بأناقة - دليل Watchtower](https://post.smzdm.com/p/awzggnqp/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
