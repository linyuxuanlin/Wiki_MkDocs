# Homelab - Home Assistant لخادم المنزل الذكي

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202306011647498.png)

**Home Assistant** هو خادم منزلي ذكي مفتوح المصدر يمكنه مراقبة جميع أجهزة المنزل ، ويشبه وظيفته تطبيق Mi Home ، ويتميز بواجهة مستخدم ودية وجميلة ونسبيًا سهلة التنصيب.

## التنصيب (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  homeassistant:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/home-assistant/home-assistant:${APP_VERSION}
    ports:
      - ${APP_PORT}:8123
    volumes:
      - ${STACK_DIR}:/config
      - /etc/localtime:/etc/localtime:ro
    privileged: true
    #network_mode: host
    restart: unless-stopped
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، اختر أي منفذ غير مستخدم
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الإعداد.

## شرح التكوين

يمكن استخدام تطبيق Home Assistant الرسمي على الهاتف المحمول مباشرةً.

## المراجع والشكر

- [الموقع الرسمي](https://www.home-assistant.io/)
- [الوثائق](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [مستودع GitHub](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [موقع العرض التوضيحي](https://demo.home-assistant.io/#/lovelace/0)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
