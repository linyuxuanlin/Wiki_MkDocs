# Homelab - أداة جلب رمز موقع favicon iconserver

![](https://img.wiki-power.com/d/wiki-media/img/20230304195157.png)

**iconserver** هي أداة جلب رمز موقع favicon. تدعم جلب `favicon.ico` و `apple-touch-icon.png` ، وتحتوي على واجهة برمجة تطبيقات URL وصفحة عمليات ويب بسيطة. إذا فشل جلب الرمز ، فسيتم إنشاء رمز بحرف أول.

## التنصيب (docker-compose)

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

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `iconserver`).

```dotenv title=".env"
STACK_NAME=iconserver

# iconserver
APP_VERSION=latest
APP_PORT=xxxx # اختر منفذًا مخصصًا للوصول إليه ، واختر أي منفذ غير مستخدم
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## المراجع والشكر

- [الوثائق](https://github.com/mat/besticon#docker)
- [مستودع GitHub](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [موقع العرض التوضيحي](https://besticon-demo.herokuapp.com/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
