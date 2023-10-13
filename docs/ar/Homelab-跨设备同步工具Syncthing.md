# Homelab - أداة مزامنة الملفات Syncthing عبر الأجهزة

![](https://img.wiki-power.com/d/wiki-media/img/202304111529987.png)

**Syncthing** هي أداة مجانية ومفتوحة المصدر لمزامنة الملفات بين الأجهزة المختلفة، وتدعم المزامنة التدريجية. استخدمتها لنسخ احتياطي لبيانات الخادم على NAS لإدارتها بشكل موحد.

## التنصيب (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    environment: # يجب تشغيلها بصلاحيات root، وإلا لن تتمكن من قراءة أي من دلائل docker الأخرى أو دليل root على المضيف
      - PUID=0
      - PGID=0
    volumes:
      - ${APP_SYNC_DIR}:/DATA
      - ${STACK_DIR}/config:/var/syncthing/config/
    ports:
      - ${APP_PORT}:8384 # واجهة المستخدم عبر الويب
      - 22000:22000/tcp # نقل الملفات عبر TCP
      - 22000:22000/udp # نقل الملفات عبر QUIC
      - 21027:21027/udp # استقبال البث المحلي للاكتشاف
    restart: unless-stopped
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `syncthing`).

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # مسار تخزين المشروع المخصص، مثل ./syncthing

# syncthing
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر أي منفذ غير مستخدم
APP_SYNC_DIR=xxxx # تخصيص المسار الذي تريد مزامنته، مثل /DATA
```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الإعداد.

## تفاصيل التكوين

إذا كانت هناك رسالة خطأ بسبب الصلاحيات، يمكنك محاولة تغيير قيم `PUID` و `PGID` إلى `0` وتشغيلها بصلاحيات root.

## المراجع والشكر

- [الموقع الرسمي](https://syncthing.net/)
- [الوثائق](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [المنتدى](https://forum.syncthing.net/)
- [مستودع GitHub](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
