# Homelab - محرر الشفرة عبر الإنترنت code-server

![](https://media.wiki-power.com/img/202304132214418.png)

**code-server** هو برنامج يمكن تشغيله في المتصفح كـ VS Code. بالمقارنة مع الإصدار السطحي، يمكنك كتابة الشفرة عبر الإنترنت باستخدام أي جهاز، بما في ذلك الهواتف المحمولة والأجهزة اللوحية التي لا يمكن تثبيت VS Code عليها مباشرة.

## التنصيب (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` ولصق المحتوى التالي فيه:

```yaml title="compose.yaml"
version: "2.1"
services:
  code-server:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/linuxserver/code-server:${APP_VERSION}
    ports:
      - ${APP_PORT}:8443
    volumes:
      - ${STACK_DIR}/config:/config
      - ${DATA_DIR_LOCAL}:/DATA
    environment: # يجب تشغيله بصلاحيات root، وإلا لن يتمكن من قراءة الدلائل الأخرى لـ Docker أو دليل root على المضيف
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #optional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #optional
      #- SUDO_PASSWORD_HASH= #optional
      #- PROXY_DOMAIN=code.wiki-power.com #optional
      #- DOCKER_MODS=linuxserver/mods:code-server-python3 #optional, if you want to add a python environment
    restart: unless-stopped
```

(اختياري) يُوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # مسار تخزين المشروع المخصص، مثل ./code-server
DATA_DIR_LOCAL=xxx # مسار التوصيل المحلي المخصص، مثل /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # منفذ الوصول المخصص، اختر منفذًا غير مستخدم بالفعل
APP_PASSWORD=xxx # كلمة المرور للتسجيل
APP_SUDO_PASSWORD=xxx # كلمة مرور المستخدم الجذر
```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس مجلد `compose.yaml` لبدء تشغيل الحاوية المُرتبة.

## تعليمات التكوين

### تكوين Git

بعد التثبيت، إذا كنت بحاجة إلى استخدام Git وتهيئة اسم المستخدم والبريد الإلكتروني، يُرجى الاطلاع على المقالة [**ملاحظات تعلم Git**](https://wiki-power.com/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE).

### مشكلة إذن القراءة والكتابة

إذا واجهتك خطأ "Error: EACCES: permission denied" أثناء التعامل مع الملفات، يمكنك فتح الطرفية وإدخال الأمر التالي لمنح المستخدم الحالي حقوق الملكية:

```shell
sudo chown -R اسم_المستخدم مسار_المجلد
```

على سبيل المثال، هذا هو الأمر الذي يمنح المستخدم "abc" حقوق الملكية على المجلد الحالي:

```shell
sudo chown -R abc .
```

### تعيين كلمة مرور حساب root

إذا كنت بحاجة إلى استخدام حساب root ، فيمكنك استخدام الأمر التالي لتهيئة كلمة المرور الخاصة به:

```shell
sudo passwd root
```

## المراجع والشكر

- [الموقع الرسمي](https://coder.com/docs/code-server/latest)
- [الوثائق / مستودع GitHub](https://github.com/linuxserver/docker-code-server)
- [Docker Hub](https://hub.docker.com/r/linuxserver/code-server)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
