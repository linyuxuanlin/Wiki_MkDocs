# الرئيسة - منصة إدارة الخدمات المنزلية

![](https://img.wiki-power.com/d/wiki-media/img/202304102312005.png)

**FreshRSS** هو منصة إدارة مصادر خدمة التجميع لتغذية RSS، حيث يمكنك الاشتراك في مصادر متعددة وتحديثها تلقائيًا. توفر واجهة ويب للقراءة عبر الإنترنت وواجهة برمجة تطبيقات للاستخدام على الهواتف المحمولة.

## النشر (Docker Compose)

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
      CRON_MIN: "*/60" # يستخدم لسحب تحديث المقالات كل 60 دقيقة
    restart: unless-stopped
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل الرئيسي لـ `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك فيه. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في ملف `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `freshrss`).

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال، ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # قم باختيار منفذ الوصول الخاص بك الذي لا يتم استخدامه بالفعل
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس الدليل الرئيسي لملف `compose.yaml` لبدء تشغيل الحاويات المكوّنة.

## تعليمات التكوين

يُوصى بشدة بمصادر RSS من [**قائمة RSS**](https://github.com/saveweb/rss-list) التي تقدمها Saveweb.

يُفضل استخدام تطبيقات FeedMe (لأنظمة Android) و NetNewsWire (لأنظمة iOS) على الهواتف المحمولة.

لمزيد من المعلومات حول خدمات RSS، يُمكنك الرجوع إلى المقالة [**RSS - طريقة فعالة للقراءة**](to_be_replace[3]).

## المراجع والشكر

- [الموقع الرسمي](https://freshrss.org)
- [الوثائق](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [مستودع GitHub](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [موقع تجريبي](https://demo.freshrss.org/i/?rid=64342708bf322)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.