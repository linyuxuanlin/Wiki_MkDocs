# Homelab - أداة مزامنة عبر الأجهزة Syncthing

![صورة](https://media.wiki-power.com/img/202304111529987.png)

**Syncthing** هو تطبيق مجاني ومفتوح المصدر لمزامنة الملفات، ويمكن استخدامه لمزامنة الملفات والمجلدات عبر عدة أجهزة، ويدعم المزامنة التدريجية. استخدمه لنسخ البيانات من الخادم إلى جهاز التخزين NAS لإدارة البيانات بشكل موحد.

## النشر (Docker Compose)

قم أولاً بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    environment: # يجب تشغيله بأمتيازات المستخدم الجذري، وإلا لن يتمكن من قراءة مجلدات Docker الأخرى أو مجلد الجذر على الجهاز المضيف
      - PUID=0
      - PGID=0
    volumes:
      - ${APP_SYNC_DIR}:/DATA
      - ${STACK_DIR}/config:/var/syncthing/config/
    ports:
      - ${APP_PORT}:8384 # واجهة المستخدم على الويب
      - 22000:22000/tcp # نقل الملفات عبر TCP
      - 22000:22000/udp # نقل الملفات عبر QUIC
      - 21027:21027/udp # استقبال البث المحلي للاكتشاف
    restart: unless-stopped
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `syncthing`).

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # تخصيص مسار تخزين المشروع الخاص بك، مثل ./syncthing

# syncthing
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر أحد الذي لا يتم استخدامه بالفعل
APP_SYNC_DIR=xxxx # تخصيص المسار الذي ترغب في مزامنته، مثل /DATA
```

أخيراً، قم بتشغيل الحاويات المُنفذة باستخدام الأمر `docker compose up -d` في نفس مجلد `compose.yaml`.

## تعليمات التكوين

إذا تم عرض رسالة تحذير حول عدم وجود الأذونات، يمكنك محاولة تغيير قيم `PUID` و `PGID` لتكون كلاهما `0` لبدء التشغيل بصلاحيات المستخدم الجذري.

## المراجعة والشكر

- [الموقع الرسمي](https://syncthing.net/)
- [الوثائق](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [المنتدى](https://forum.syncthing.net/)
- [مستودع GitHub](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
