# Homelab - أداة مراقبة حالة الموقع Uptime Kuma

![](https://f004.backblazeb2.com/file/wiki-media/img/20230410160253.jpg)

**Uptime Kuma** هي أداة مراقبة حالة تدعم العديد من بروتوكولات الشبكة ، والتي يمكنها مراقبة حالة الوقت الفعلي ومدة الاستجابة وصلاحية الشهادة لعدة مواقع مخصصة ، وتوفير العديد من طرق الإشعار.

## نشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  uptime-kuma:
    container_name: ${STACK_NAME}_app
    image: louislam/uptime-kuma:${APP_VERSION}
    ports:
      - ${APP_PORT}:3001
    volumes:
      - ${STACK_DIR}:/app/data
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `uptime-kuma`).

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، اختر غير مستخدم فقط
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الإعداد.

## تفاصيل الإعداد

ملاحظة: إذا كنت تستخدم خادم وكيل عكسي ، فيرجى تمكين خاصية `Websockets Support`.

## المراجع والشكر

- [الموقع الرسمي](https://uptime.kuma.pet/)
- [الوثائق](https://github.com/louislam/uptime-kuma/wiki)
- [مستودع GitHub](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.