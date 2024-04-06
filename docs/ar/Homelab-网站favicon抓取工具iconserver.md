# Homelab - أداة استخراج رمز موقع الويب favicon iconserver

![الرمز](https://media.wiki-power.com/img/20230304195157.png)

**iconserver** هي أداة استخراج رمز موقع الويب favicon. تدعم استخراج `favicon.ico` و
`apple-touch-icon.png` ، وتتيح واجهة برمجة تطبيق (API) بسيطة للاستخدام مع صفحة واجهة الويب. إذا فشلت عملية الاستخراج ، ستقوم بإنشاء رمز favicon يبدأ بالحرف الأول للموقع.

## نشر (docker-compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  iconserver:
    container_name: ${STACK_NAME}_app
    image: matthiasluedtke/iconserver:${APP_VERSION}
    ports:
      - ${APP_PORT}:8080
    restart: always
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل الرئيسي لـ `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام متغيرات البيئة ، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `iconserver`).

```dotenv title=".env"
STACK_NAME=iconserver

# iconserver
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك - اختر منفذًا غير مستخدم بالفعل
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس الدليل الرئيسي لـ `compose.yaml` لبدء تشغيل الحاويات المكونة.

## المراجعة والشكر

- [الوثائق](https://github.com/mat/besticon#docker)
- [مستودع GitHub](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [موقع العرض التوضيحي](https://besticon-demo.herokuapp.com/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
