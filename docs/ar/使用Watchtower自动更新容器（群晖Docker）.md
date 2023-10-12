# استخدام Watchtower لتحديث حاويات Docker (Synology Docker)

استخدام Watchtower لتحديث حاويات Synology Docker تلقائيًا.

## تنزيل الصورة في تطبيق Synology Docker

افتح حزمة Synology Docker وقم بتنزيل صورة `containrrr/watchtower`.

## تكوين Watchtower في المهام المجدولة

افتح "لوحة التحكم" في Synology - "المهام المجدولة" - "جديد" - "مهمة مجدولة" - "نص مخصص للمستخدم" ، ثم قم بملء التكوين كما هو موضح في الصور التالية:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202301092319956.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202301092321592.png)

البرنامج النصي هو:

```shell
docker run --rm --name watchtower -v /var/run/docker.sock:/var/run/docker.sock containrrr/watchtower --cleanup --run-once calibre-web freshrss code-server
```

يرجى ملاحظة أن اسماء الحاويات التي تحتاج إلى التحديث في نهاية البرنامج النصي `calibre-web freshrss code-server` يجب استبدالها بالحاويات التي تريد تحديثها ؛ أو يمكن تركها فارغة لتحديث جميع الحاويات.

حفظ التكوين وتشغيل البرنامج النصي لتحديث حاويات Docker بشكل دوري.

## المراجع والشكر

- [كيفية استخدام Watchtower بشكل أنيق لتحديث حاويات Synology Docker - دليل Watchtower](https://post.smzdm.com/p/awzggnqp/) 

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.