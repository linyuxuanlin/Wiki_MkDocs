# هوملاب - خادم المنزل الذكي Home Assistant

![](https://media.wiki-power.com/img/202306011647498.png)

**Home Assistant** هو خادم منزل ذكي مفتوح المصدر يمكنه مراقبة جميع أجهزة منزلك ، ويشبه وظيفته تطبيق Mi Home ، ويتميز بواجهة مستخدم ودية وجذابة ونسبيًا سهلة التركيب.

## التركيب (Docker Compose)

أولاً ، أنشئ ملف `compose.yaml` ، والصق المحتوى التالي:

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

(اختياري) يوصى بإنشاء ملف `.env` في نفس الدليل مع `compose.yaml` وتخصيص المتغيرات المحيطة. إذا كنت لا ترغب في استخدام المتغيرات المحيطة ، فيمكنك تعديل المعلمات مباشرة في `compose.yaml` (على سبيل المثال ، استبدل `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # حدد مسار مخزن المشروع المخصص مباشرة مثل ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول المخصص واتركه غير مشغول
```

أخيرًا ، قم بتنفيذ الأمر `docker compose up -d` في نفس الدليل مع `compose.yaml` لتشغيل الحاويات المكونة.

## توضيحات التكوين

يمكن استخدام تطبيق Home Assistant الرسمي الخاص بالأجهزة المحمولة.

إذا كنت تواجه رسالة خطأ "400 Bad Request" عند الوصول من الإنترنت ، فيمكن أن تقوم بإضافة البيانات التالية إلى ملف التكوين `configuration.yaml`:

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 10.0.0.200 # عنوان IP لخادم الوكيل
    - 172.30.33.0/24 # يمكن أيضًا تقديم عنوان IP مع قناع الشبكة
```

إذا كنت لا تعلم عنوان IP لخادم الوكيل ، يمكنك محاولة الوصول إلى Home Assistant من الإنترنت وستجد رسالة الخطأ في سجل الأخطاء.

## المراجع والشكر

- [الموقع الرسمي](https://www.home-assistant.io/)
- [الوثائق](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [مستودع GitHub](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [موقع العرض التوضيحي](https://demo.home-assistant.io/#/lovelace/0)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
