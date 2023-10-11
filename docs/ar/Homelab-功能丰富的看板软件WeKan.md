# Homelab - برنامج WeKan لوحة المهام الغنية بالميزات

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230508175842.png)

**WeKan** هو برنامج مفتوح المصدر لوحة المهام المرنة والسهلة الاستخدام والفعالة، ويمكن استخدامه لإدارة المهام والمشاريع وسير العمل في الفريق. يوفر واجهة مستخدم بسيطة وقوية يمكن للمستخدمين من خلالها إنشاء العديد من اللوحات وإضافة القوائم والبطاقات لكل لوحة، وتعيين المهام لأعضاء مختلفين لإدارة المشروع وتتبع التقدم.

## التنصيب (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` ولصق المحتوى التالي:

```yaml title="compose.yaml"
version: "2"
services:
  wekandb:
    container_name: ${STACK_NAME}_db
    image: mongo:${DB_VERSION}
    command: mongod --logpath /dev/null --oplogSize 128 --quiet
    networks:
      - wekan-tier
    expose:
      - 27017
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - wekan-db:/data/db
      - wekan-db-dump:/dump
    restart: no
  wekan:
    container_name: ${STACK_NAME}_app
    image: quay.io/wekan/wekan:${APP_VERSION}
    user: 0:0
    networks:
      - wekan-tier
    ports:
      - ${APP_PORT}:8080
    environment:
      - WRITABLE_PATH=/data
      - MONGO_URL=mongodb://wekandb:27017/wekan
      - ROOT_URL=http://localhost
      - MAIL_URL=smtp://<mail_url>:25/?ignoreTLS=true&tls={rejectUnauthorized:false}
      - MAIL_FROM=Wekan Notifications <noreply.wekan@mydomain.com>
      - WITH_API=true
      - RICHER_CARD_COMMENT_EDITOR=false
      - CARD_OPENED_WEBHOOK_ENABLED=false
    depends_on:
      - wekandb
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - wekan-files:/data:rw
    restart: no
volumes:
  wekan-files:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-files
      o: bind
  wekan-db:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-db
      o: bind
  wekan-db-dump:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-db-dump
      o: bind
networks:
  wekan-tier:
    driver: bridge
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرةً داخل `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `wekan`).

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # مسار تخزين المشروع المخصص، مثل ./wekan

# wekandb
DB_VERSION=6

# wekan
APP_VERSION=latest
APP_PORT=xxxx # منفذ الوصول المخصص، اختر غير المستخدم لتجنب التعارض
```

ثم نقوم بتهيئة هيكل المجلدات. انتقل إلى `STACK_DIR` المخصص (مثل `./wekan`) وقم بتنفيذ الأمر لإنشاء المجلدات:

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
```

أخيرًا، يمكنك تشغيل حاويات الترتيب ببساطة باستخدام الأمر `docker compose up -d` في نفس مستوى `compose.yaml`.

## تفاصيل التكوين

تم تبسيط وتعديل `compose.yaml` المذكور أعلاه. إذا كنت ترغب في الإطلاع على النسخة الكاملة، يرجى الرجوع إلى [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml).

بعد الانتهاء من التثبيت، يتم تسجيل الحساب الأول كحساب مدير. إذا كنت تستخدمها لنفسك، فمن المستحسن إيقاف تشغيل وظيفة تسجيل المستخدمين في لوحة الإعدادات.

## المراجع والشكر

- [الموقع الرسمي](https://wekan.github.io/)
- [الوثائق](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [مستودع GitHub](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [موقع العرض التوضيحي](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
