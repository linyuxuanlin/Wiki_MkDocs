# Homelab - خادم البودكاست والكتب الصوتية Audiobookshelf

![](https://f004.backblazeb2.com/file/wiki-media/img/20230531204505.png)

**Audiobookshelf** هو خادم بودكاست وكتب صوتية يتم استضافته ذاتيًا، ويمكن البحث عن البودكاست بسهولة والكشف التلقائي عن التحديثات وتنزيلها وتنظيمها تلقائيًا.

## التنصيب (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./audiobookshelf
DATA_DIR=xxx # مسار تخزين البودكاست المخصص ، على سبيل المثال ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، اختر غير مستخدم فقط
```

إذا كان لديك NAS ، فيمكنك أيضًا تثبيت مساحة التخزين على NAS باستخدام بروتوكول NFS ، وتخزين البودكاست على NAS لتوفير مساحة الخادم. لمزيد من التفاصيل ، يرجى الرجوع إلى [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/ar/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/)。

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## تعليمات التكوين

تطبيق الجوال: يتوفر تطبيق رسمي لـ iOS و Android ، ويمكن استخدامه مباشرةً.

## المراجع والشكر

- [الموقع الرسمي](https://www.audiobookshelf.org/)
- [الوثائق](https://www.audiobookshelf.org/docs#docker-compose-install)
- [مستودع GitHub](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.