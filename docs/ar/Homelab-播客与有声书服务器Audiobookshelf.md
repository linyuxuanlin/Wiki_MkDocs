# Homelab - خادم البودكاست والكتب الصوتية Audiobookshelf

![صورة](https://img.wiki-power.com/d/wiki-media/img/20230531204505.png)

**Audiobookshelf** هو خادم ذاتي الاستضافة للبودكاست والكتب الصوتية يمكنه بسهولة البحث في البودكاست والكتب الصوتية، واكتشاف التحديثات تلقائيًا وتنزيلها، وتنظيمها تلقائيًا.

## النشر (Docker Compose)

قم أولاً بإنشاء ملف `compose.yaml` ولصق المحتوى التالي:

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

(اختياري) يُفضل إنشاء ملف `.env` في نفس دليل `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا لم ترغب في استخدام المتغيرات البيئية، يمكنك أيضاً تخصيص المعاملات مباشرة داخل `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال ./audiobookshelf
DATA_DIR=xxx # حدد مسار تخزين البودكاست الخاص بك، على سبيل المثال ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذ غير مستخدم بالفعل
```

إذا كان لديك جهاز تخزين NAS، يمكنك أيضًا استخدام بروتوكول NFS لربط مساحة التخزين على NAS وحفظ البودكاست عليه لتوفير مساحة الخادم. لمزيد من التفاصيل، راجع [**كيفية ربط قرص الشبكة (NFS) من Synology NAS تحت نظام Linux لزيادة المساحة**](to_be_replace[3]).

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس دليل `compose.yaml` لبدء تشغيل الحاويات المنسقة.

## توجيهات التكوين

تطبيق الهاتف المحمول: يتوفر تطبيق رسمي لأنظمة iOS و Android يمكن استخدامه مباشرة.

## المراجعة والشكر

- [الموقع الرسمي](https://www.audiobookshelf.org/)
- [الوثائق](https://www.audiobookshelf.org/docs#docker-compose-install)
- [مستودع GitHub](https://github.com/advplyr/audiobookshelf)
- [موقع Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.