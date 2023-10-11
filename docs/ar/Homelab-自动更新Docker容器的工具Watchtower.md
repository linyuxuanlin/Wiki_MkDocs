# Homelab - أداة Watchtower لتحديث حاويات Docker تلقائيًا

![](https://f004.backblazeb2.com/file/wiki-media/img/202304092337531.png)

**Watchtower** هي أداة لتحديث حاويات Docker كلها أو محددة تلقائيًا.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  watchtower:
    container_name: ${STACK_NAME}_app
    image: containrrr/watchtower:${APP_VERSION}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `watchtower`).

```dotenv title=".env"
STACK_NAME=watchtower

# watchtower
APP_VERSION=latest
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل الحاويات المرتبطة.

## المراجع والشكر

- [الموقع الرسمي / الوثائق](https://containrrr.dev/watchtower)
- [مستودع GitHub](https://github.com/containrrr/watchtower/)
- [Docker Hub](https://hub.docker.com/r/containrrr/watchtower)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.