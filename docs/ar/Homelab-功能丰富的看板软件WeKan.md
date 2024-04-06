# Homelab - برنامج لوحة الأعمال WeKan الغني بالميزات

![صورة](https://media.wiki-power.com/img/20230508175842.png)

**WeKan** هو برنامج لوحة الأعمال مفتوح المصدر مرن وسهل الاستخدام وفعال يساعد الفرق في إدارة المهام والمشاريع وسير العمل. يوفر واجهة مستخدم بسيطة وقوية تسمح للمستخدمين بإنشاء لوحات متعددة بسهولة، وإضافة قوائم وبطاقات لكل لوحة، وتخصيص المهام لأعضاء مختلفين، مما يساعد على إدارة المشروع بشكل أفضل وتتبع التقدم.

## النشر (Docker Compose)

أولاً، أنشئ ملف `compose.yaml` وقم بلصق المحتوى التالي:

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

(اختياري) يُوصى بإنشاء ملف `.env` في نفس الدليل مع `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `wekan`).

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # مسار تخزين المشروع المخصص، على سبيل المثال ./wekan

# wekandb
DB_VERSION=6

# wekan
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم
```

بعد ذلك، سنقوم ببنية الهيكل الدليلي. انتقل إلى الدليل المخصص الخاص بك (`STACK_DIR` على سبيل المثال `./wekan`) وقم بتنفيذ الأمر التالي لإنشاء المجلدات:

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
```

أخيرًا، في نفس الدليل مع `compose.yaml`، قم بتنفيذ الأمر `docker compose up -d` لتشغيل حاويات الإعداد.

## توجيهات التكوين

تم تبسيط وتعديل `compose.yaml` المذكور أعلاه. إذا كنت تحتاج إلى الإصدار الكامل، يُرجى الرجوع إلى [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml).

بعد الانتهاء من النشر، سيتم إنشاء حساب مسؤول للتسجيل الأولي. إذا كنت تستخدمها لنفسك، نوصي بإلغاء تفعيل وظيفة تسجيل المستخدمين من خلال لوحة الإعداد.

## مراجع وشكر

- [الموقع الرسمي](https://wekan.github.io/)
- [الوثائق](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [مستودع GitHub](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [موقع العرض التوضيحي](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
