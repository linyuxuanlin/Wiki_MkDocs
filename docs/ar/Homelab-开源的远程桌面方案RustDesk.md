# Homelab - حل سطح المكتب عن بُعد مفتوح المصدر RustDesk

![](https://media.wiki-power.com/img/20230531212854.png)

**RustDesk** هو حلاً مفتوح المصدر لسطح المكتب عن بُعد، يمكنك استخدام العملاء على مختلف الأنظمة مباشرة في الشبكة الداخلية للوصول عن بُعد. تتناول هذه المقالة بصفة رئيسية كيفية إعداد الخادم الخاص بك في الشبكة العامة.

## النشر (Docker Compose)

أولاً، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"

networks:
  rustdesk-net:
    external: false

services:
  hbbs:
    container_name: ${STACK_NAME}_hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbs -r ${STACK_DOMAIN}:21117 -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: ${STACK_NAME}_hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbr -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

في هذا تكوين دوكر كومبوز، يتم تنظيم خدمتين:

- hbbs: خادم تسجيل RustDesk ID
- hbbr: خادم وسيط RustDesk

(اختياري) نوصي بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا لم تكن ترغب في استخدام متغيرات البيئة، يمكنك أيضًا تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `rustdesk-server`).

```dotenv title=".env"
STACK_NAME=rustdesk-server
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، مثل ./rustdesk-server
STACK_DOMAIN=xxx # اسم النطاق أو عنوان IP لخادم RustDesk

# rustdesk-server
APP_VERSION=latest
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس الدليل الذي يحتوي على `compose.yaml` لتشغيل الحاويات المُنظمة.

## شرح التكوين

إذا واجهت خطأ "Registered email required (-m option). Please pay and register on https://rustdesk.com/server..."، فهذا يعني أنك ربما قمت بتنزيل إصدار غير أحدث من الحزمة. يمكنك حل هذه المشكلة كالتالي:

1. اعثر على رقم الإصدار الأحدث DIGEST (مثل `83e259792b50`) على <https://hub.docker.com/r/rustdesk/rustdesk-server/tags>.
2. قم بتنزيل الحزمة الأحدث محليًا باستخدام الأمر التالي `docker image pull rustdesk/rustdesk-server:latest@sha256:83e259792b50`، تأكد من استبدال الحروف النهائية ببياناتك الخاصة.

## المراجع والشكر

- [الموقع الرسمي](https://rustdesk.com/)
- [الوثائق](https://rustdesk.com/docs/en/self-host/)
- [مستودع GitHub](https://github.com/rustdesk/rustdesk)
- [Docker Hub](https://hub.docker.com/r/rustdesk/rustdesk-server)
- [استخدام دوكر لإنشاء خادم RustDesk الخاص](https://developer.aliyun.com/article/1299504)
- [الاستضافة الذاتية](https://rustdesk.com/docs/zh-cn/self-host/rustdesk-server-oss/install/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.  

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.