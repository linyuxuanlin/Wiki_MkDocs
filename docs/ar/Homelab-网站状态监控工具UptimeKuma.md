# Homelab - أداة مراقبة حالة الموقع وتعقب الوقت الفعّال - Uptime Kuma

![صورة](https://media.wiki-power.com/img/20230410160253.jpg)

**Uptime Kuma** هو أداة مراقبة حالة تدعم العديد من بروتوكولات الشبكة وتمكّن من مراقبة الحالة الفعلية وزمن الاستجابة وصلاحية الشهادات للعديد من المواقع المخصصة، بالإضافة إلى توفير وسائل متعددة للإشعار.

## النشر (Docker Compose)

قم أولاً بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) نوصي بإنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك هناك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تعديل المعاملات المبيّنة مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `uptime-kuma`).

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال، ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # قم بتخصيص منفذ الوصول الخاص بك، اختر منفذ غير مستخدم مسبقًا
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس المجلّد الذي يحتوي على ملف `compose.yaml` لتشغيل الحاويات المنتجة.

## توجيهات التكوين

ملحوظة: إذا كنت تستخدم وكيلًا عكسيًا (Reverse Proxy)، يُفضل تفعيل خاصية "Websockets Support".

## المراجع والشكر

- [الموقع الرسمي](https://uptime.kuma.pet/)
- [الوثائق](https://github.com/louislam/uptime-kuma/wiki)
- [مستودع GitHub](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
