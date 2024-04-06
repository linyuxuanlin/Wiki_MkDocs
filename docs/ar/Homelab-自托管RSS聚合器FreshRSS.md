# الخادم المنزلي - منصة إدارة تغذية الـ RSS المُستضافة بشكل ذاتي - FreshRSS

![صورة](https://media.wiki-power.com/img/202304102312005.png)

**FreshRSS** هي منصة إدارة تغذية RSS مُستضافة بشكل ذاتي، حيث تُمكنك من الاشتراك في عدة مصادر لتغذيات RSS وتحديثها تلقائيًا. يُمكنك أيضًا استخدام واجهة الويب للقراءة عبر الإنترنت وAPI لتطبيقات الهواتف المحمولة.

## النشر (عبر Docker Compose)

أولاً، قم بإنشاء ملف بمسمى `compose.yaml` والصق فيه المحتوى التالي:

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
      CRON_MIN: "*/60" # تحديث المقالات كل 60 دقيقة
    restart: unless-stopped
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل الذي يحتوي على ملف `compose.yaml` لتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة داخل ملف `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، مثل ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذ غير مستخدم
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس الدليل الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات.

## تفاصيل الإعداد

يُمكن الاطلاع على قائمة مواقع الويب الصينية المُوصى بها لتغذية RSS من [**rss-list**](https://github.com/saveweb/rss-list).

لتطبيقات الهواتف المحمولة، نوصي باستخدام تطبيق FeedMe (Android) أو NetNewsWire (iOS).

للمزيد من المعلومات حول تغذية RSS، يُمكنك الرجوع إلى المقالة [**تغذية RSS - وسيلة فعّالة للقراءة**](https://wiki-power.com/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/).

## المصادر والشكر

- [الموقع الرسمي](https://freshrss.org)
- [الوثائق](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [مستودع GitHub](https://github.com/FreshRSS/FreshRSS)
- [موقع Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [موقع العرض التوضيحي](https://demo.freshrss.org/i/?rid=64342708bf322)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
