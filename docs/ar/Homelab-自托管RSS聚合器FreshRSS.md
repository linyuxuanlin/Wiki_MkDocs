# Homelab - تشغيل مجمّع RSS FreshRSS على خادم شخصي

![](https://f004.backblazeb2.com/file/wiki-media/img/202304102312005.png)

**FreshRSS** هو مجمّع RSS مستضاف يدعم الاشتراك في عدة مصادر RSS ويقوم بالتحديث التلقائي. يوفر قراءة عبر الويب وواجهة برمجة تطبيقات (API) للاستخدام على التطبيقات المحمولة.

## التثبيت (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "2.4"
services:
  freshrss:
    container_name: ${STACK_NAME}_app
    image: freshrss/freshrss:${APP_VERSION}
    hostname: freshrss
    logging:
      options:
        max-size: 10m
    ports:
      - "${APP_PORT}:80"
    volumes:
      - ${STACK_DIR}/data:/var/www/FreshRSS/data
      - ${STACK_DIR}/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: "*/60" # استدعاء تحديث المقالات كل 60 دقيقة
    restart: unless-stopped
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، فيمكنك تخصيص المعلمات مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # تخصيص مسار حفظ المشروع، مثل ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول، يمكن اختيار أي منفذ غير مستخدم
```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## شرح التكوين

يمكن الاطلاع على قائمة مدونات RSS الصينية الموصى بها من saveweb [**rss-list**](https://github.com/saveweb/rss-list).

يوصى باستخدام تطبيقات FeedMe (Android) و NetNewsWire (iOS) على الأجهزة المحمولة.

يمكن الاطلاع على المزيد من المحتوى المتعلق بـ RSS في المقال [**RSS - طريقة قراءة فعالة**](https://wiki-power.com/ar/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/) (باللغة الصينية).

## المراجع والشكر

- [الموقع الرسمي](https://freshrss.org)
- [الوثائق](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [مستودع GitHub](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [موقع العرض التوضيحي](https://demo.freshrss.org/i/?rid=64342708bf322)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.