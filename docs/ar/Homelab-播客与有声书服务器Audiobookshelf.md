# Homelab - خادم البودكاست والكتب الصوتية Audiobookshelf

![صورة](https://media.wiki-power.com/img/20230531204505.png)

**Audiobookshelf** هو خادم مدار بنفسك للبودكاست والكتب الصوتية، والذي يتيح البحث السهل عن البودكاست، والكشف التلقائي عن التحديثات وتنزيلها، وترتيبها تلقائيًا.

## النشر (Docker Compose)

قم أولاً بإنشاء ملف `compose.yaml` وقم بلصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.7"
services:
  audiobookshelf:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/advplyr/audiobookshelf:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}/audiobooks:/audiobooks
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/metadata:/metadata
      - ${DATA_DIR}:/podcasts
    restart: unless-stopped
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل الرئيسي الذي يحتوي على ملف `compose.yaml` وقم بتخصيص متغيرات البيئة الخاصة بك. إذا كنت لا ترغب في استخدام متغيرات البيئة، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال، ./audiobookshelf
DATA_DIR=xxx # حدد مسار تخزين البودكاست الخاص بك، على سبيل المثال، ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم مسبقًا
```

إذا كان لديك جهاز NAS، يمكنك أيضًا استخدام بروتوكول NFS لتثبيت مساحة التخزين على جهاز NAS وتخزين البودكاست على الجهاز NAS لتوفير مساحة الخادم، للمزيد من التفاصيل، يُرجى الرجوع إلى [**تثبيت الأقراص الصلبة لـ NAS من Synology على نظام Linux (NFS)**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

أخيرًا، قم بتشغيل الحاويات من خلال تنفيذ الأمر `docker compose up -d` في نفس دليل `compose.yaml`.

## توجيهات الإعداد

تطبيق الهاتف المحمول: هناك تطبيقات رسمية لنظامي iOS و Android يمكن استخدامها مباشرة.

## المراجعة والشكر

- [الموقع الرسمي](https://www.audiobookshelf.org/)
- [الوثائق](https://www.audiobookshelf.org/docs#docker-compose-install)
- [مستودع GitHub](https://github.com/advplyr/audiobookshelf)
- [مستودع Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
