# الوحدة المنزلية - Next Terminal: الجهاز الحصني الذي يدعم العديد من البروتوكولات

![صورة](https://media.wiki-power.com/img/20230312001443.png)

**Next Terminal** هو جهاز الوصول البسيط والممتع الذي يضم بوابة سطح المكتب عن بعد بدون عميل مدمجة باستخدام Apache Guacamole. يقدم هذا الجهاز حلاً للجهاز الحصني الذي يدعم العديد من البروتوكولات مثل RDP و SSH و VNC و TELNET و Kubernetes. يمكن الوصول إلى الموارد الداخلية مباشرة عبر الويب وهو متوافق مع مختلف منصات التشغيل. يدعم أيضًا ميزة التحقق المتعدد العوامل (MFA) للدخول، بالإضافة إلى تسجيل الجلسات وميزات أخرى.

## نصائح للتنفيذ (Docker Compose)

أولاً، يجب عليك إنشاء ملف `compose.yaml` ولصق المحتوى التالي:

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

(اختياري) نوصي بإنشاء ملف `.env` في نفس مجلد `compose.yaml` وتخصيص المتغيرات البيئية وفقًا لاحتياجاتك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `next-terminal`).

```dotenv title=".env"
STACK_NAME=next-terminal
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال: ./next-terminal

# next-terminal
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم مسبقًا
APP_GUACD_HOSTNAME=guacd # الافتراضي
APP_GUACD_PORT=4822 # الافتراضي

# guacd
GUACD_VERSION=latest
```

أخيرًا، يمكنك تشغيل الحاويات المعدة باستخدام الأمر `docker compose up -d` في نفس مجلد `compose.yaml`.

## تعليمات التكوين

اسم المستخدم / كلمة المرور الافتراضيين: `admin`.

## الإشارة والشكر

- [الموقع الرسمي](https://next-terminal.typesafe.cn/)
- [الوثائق](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [مستودع GitHub](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [موقع العرض التجريبي](https://next.typesafe.cn/) (اسم المستخدم: test، كلمة المرور: test)
- [Next Terminal | منصة بوابة الوصول المفتوحة المصدر | خفيفة وبسيطة](https://blog.samliu.tech/2022/07/22/next-terminal-%E5%BC%80%E6%BA%90-%E8%BD%BB%E9%87%8F-%E7%AE%80%E5%8D%95%E7%9A%84%E5%A0%A1%E5%9E%92%E6%9C%BA/?utm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%2592%25e6%259c%25ba)

[ليتم الاستبدال[1]]
[ليتم الاستبدال[2]]

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
