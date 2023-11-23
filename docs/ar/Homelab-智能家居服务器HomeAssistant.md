# الهوم لاب - خادم المنزل الذكي هوم أسيستانت

![Home Assistant](https://img.wiki-power.com/d/wiki-media/img/202306011647498.png)

**هوم أسيستانت** هو خادم منزلي ذكي مفتوح المصدر يمكنه مراقبة جميع الأجهزة في منزلك. إنه مشابه لـ Mi Home من ناحية الوظائف ويتميز بواجهة مستخدم ودية وجذابة، ويمكن نشره بسهولة نسبية.

## النشر (Docker Compose)

أولاً، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يُوصى بإنشاء ملف `.env` في نفس الدليل الرئيسي لـ `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا لم ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعاملات مباشرة داخل `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # تخصيص مسار تخزين المشروع الخاص بك، على سبيل المثال: ./homeassistant

# هوم أسيستانت
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر أحدًا غير مستخدم بالفعل
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس الدليل الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات المجمعة.

## توجيهات التكوين

يمكن استخدام تطبيق هوم أسيستانت الرسمي مباشرة على الهواتف النقالة.

## المراجع والشكر

- [الموقع الرسمي](https://www.home-assistant.io/)
- [الوثائق](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [مستودع GitHub](https://github.com/home-assistant)
- [مستودع Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [موقع العرض التوضيحي](https://demo.home-assistant.io/#/lovelace/0)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.