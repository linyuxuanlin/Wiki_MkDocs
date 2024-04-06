# Homelab - Wiki.js: نظام ويكي قوي

![](https://media.wiki-power.com/img/20230304195348.png)

**Wiki.js** هو أداة وثائق ويكي تأتي مع محرر خلفي وصفحات إدارة، بما في ذلك إدارة الصلاحيات للمستخدمين المتعددين، ودعم Markdown، ووسائل تخزين متعددة (مثل مزامنة Git)، وغير ذلك.

## النشر (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  wikijs:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/requarks/wiki:${APP_VERSION}
    depends_on:
      - db
    environment:
      DB_TYPE: ${APP_DB_TYPE}
      DB_HOST: ${APP_DB_HOST}
      DB_PORT: ${APP_DB_PORT}
      DB_USER: ${APP_DB_USER}
      DB_PASS: ${APP_DB_PASS}
      DB_NAME: ${APP_DB_NAME}
    restart: unless-stopped
    ports:
      - "${APP_PORT}:3000"
  db:
    container_name: ${STACK_NAME}_db
    image: postgres:${DB_VERSION}
    environment:
      POSTGRES_DB: ${DB_POSTGRES_DB}
      POSTGRES_PASSWORD: ${DB_POSTGRES_PASSWORD}
      POSTGRES_USER: ${DB_POSTGRES_USER}
    logging:
      driver: "none"
    volumes:
      - ${STACK_DIR}/postgres/db-data:/var/lib/postgresql/data
    restart: unless-stopped
volumes:
  db-data:
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `wikijs`).

```dotenv title=".env"
STACK_NAME=wikijs
STACK_DIR=xxx # مسار تخزين المشروع الخاص بك، مثل ./wikijs

# wikijs
APP_VERSION=2
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم بالفعل
APP_DB_TYPE=postgres
APP_DB_HOST=db
APP_DB_PORT=5432 # منفذ قاعدة البيانات الافتراضي الداخلي
APP_DB_USER=xxx # اسم المستخدم لقاعدة البيانات
APP_DB_PASS=xxx # كلمة المرور لقاعدة البيانات
APP_DB_NAME=wikijs # اسم قاعدة البيانات

# db
DB_VERSION=10-alpine
DB_POSTGRES_DB=wikijs # اسم قاعدة البيانات، يجب أن يتطابق مع الإعداد أعلاه
DB_POSTGRES_PASSWORD=xxx # كلمة مرور قاعدة البيانات، يجب أن يتطابق مع الإعداد أعلاه
DB_POSTGRES_USER=xxx # اسم المستخدم لقاعدة البيانات، يجب أن يتطابق مع الإعداد أعلاه
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس المجلد الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات المُعدة.

## توجيهات التكوين

لمزيد من التفاصيل حول مزامنة مستودع Git، يُرجى الرجوع إلى: <https://docs.requarks.io/storage/git>

## المراجعة والشكر

- [الموقع الرسمي](https://js.wiki)
- [الوثائق](https://docs.requarks.io/install/docker)
- [مستودع GitHub](https://github.com/requarks/wiki)
- [مستودع Docker Hub](https://hub.docker.com/r/requarks/wiki)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
