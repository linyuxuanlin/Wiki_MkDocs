# Homelab - برنامج Next Terminal للمحطات الفرعية المدعومة بعدة بروتوكولات

![](https://img.wiki-power.com/d/wiki-media/img/20230312001443.png)

يعد Next Terminal برنامجًا سهل الاستخدام للمحطات الفرعية (المحطات الأمنية)، وهو يدمج حلًا للمحطات الفرعية لبوابة سطح المكتب البعيد بدون عميل Apache Guacamole، ويدعم العديد من البروتوكولات مثل RDP و SSH و VNC و TELNET و Kubernetes، ويمكن الوصول إلى الموارد الداخلية مباشرة عبر الويب، ويتوافق مع العديد من المنصات. كما يدعم تسجيل الدخول بعوامل متعددة (MFA) ولديه وظيفة تسجيل الفيديو والتسجيلات الأخرى.

## التنصيب (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` ولصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.3"
services:
  guacd:
    container_name: ${STACK_NAME}_guacd
    image: dushixiang/guacd:${GUACD_VERSION}
    volumes:
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
  next-terminal:
    container_name: ${STACK_NAME}_app
    image: dushixiang/next-terminal:${APP_VERSION}
    environment:
      DB: sqlite
      GUACD_HOSTNAME: ${APP_GUACD_HOSTNAME}
      GUACD_PORT: ${APP_GUACD_PORT}
    ports:
      - ${APP_PORT}:8088
    volumes:
      - /etc/localtime:/etc/localtime
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `next-terminal`).

```dotenv title=".env"
STACK_NAME=next-terminal
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./next-terminal

# next-terminal
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، اختر غير مستخدم بالفعل
APP_GUACD_HOSTNAME=guacd # الافتراضي
APP_GUACD_PORT=4822 # الافتراضي

# guacd
GUACD_VERSION=latest
```

أخيرًا، يمكنك تشغيل حاويات الترتيب بتنفيذ الأمر `docker compose up -d` في نفس مستوى `compose.yaml`.

## تعليمات التكوين

اسم المستخدم / كلمة المرور الافتراضية: `admin`.

## المراجع والشكر

- [الموقع الرسمي](https://next-terminal.typesafe.cn/)
- [الوثائق](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [مستودع GitHub](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [موقع العرض التوضيحي](https://next.typesafe.cn/) (اسم المستخدم: test، كلمة المرور: test)
- [Next Terminal | بوابة دخول مفتوحة المصدر وخفيفة الوزن وبسيطة](https://blog.samliu.tech/2022/07/22/next-terminal-%D9%83%D9%88%D8%A7%D8%A8%D9%8A%D8%B3-%D8%A8%D9%88%D8%A7%D8%A8%D8%A9-%D8%AF%D8%AE%D9%88%D9%84-%D9%85%D9%81%D8%AA%D9%88%D8%AD%D8%A9-%D8%A7%D9%84%D9%85%D8%B5%D8%AF%D8%B1-%D9%88%D8%AE%D9%81%D9%8A%D9%81%D8%A9-%D8%A7%D9%84%D9%88%D8%B2%D9%86-%D9%88%D8%A8%D8%B3%D9%8A%D8%B7%D8%A9%D8%9Futm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%2592%25e6%259c%25ba)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
