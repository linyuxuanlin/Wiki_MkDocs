# Homelab - محرر الكود عبر الإنترنت code-server

![](https://f004.backblazeb2.com/file/wiki-media/img/202304132214418.png)

**code-server** هو برنامج يمكن تشغيله في المتصفح ويعمل على نفس نظام VS Code. وبالمقارنة مع الإصدار السطحي ، يمكنك كتابة الشفرة عبر الإنترنت باستخدام أي جهاز ، بما في ذلك الهواتف المحمولة والأجهزة اللوحية التي لا يمكن تثبيت VS Code مباشرة عليها.

## التنصيب (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` ولصق المحتوى التالي:

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
    environment: # يجب تشغيله بصلاحيات root ، وإلا فلن يتمكن من قراءة أي دليل آخر لـ docker أو دليل root لجهاز الاستضافة
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} #optional
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} #optional
      #- SUDO_PASSWORD_HASH= #optional
      #- PROXY_DOMAIN=code.wiki-power.com #optional
    restart: unless-stopped
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، فيمكنك تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./code-server
DATA_DIR_LOCAL=xxx # مسار الدليل المحلي المراد تعليقه ، على سبيل المثال /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # منفذ الوصول المخصص ، اختر أي منفذ غير مستخدم بالفعل
APP_PASSWORD=xxx # كلمة المرور لتسجيل الدخول
APP_SUDO_PASSWORD=xxx # كلمة مرور المستخدم الجذرية

```

أخيرًا ، يمكنك تشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## تعليمات التكوين

### تكوين git

بعد التثبيت ، إذا كنت ترغب في استخدام Git ، فيجب تهيئة اسم المستخدم والبريد الإلكتروني ، يرجى الرجوع إلى المقالة [**Git 学习笔记**](https://wiki-power.com/ar/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE).

### مشكلة الصلاحيات للقراءة والكتابة

إذا واجهت خطأ `Error: EACCES: permission denied` أثناء عملية الملف ، يمكنك فتح الطرفية وإدخال الأمر التالي لمنح المستخدم الحالي الحقوق الكاملة:

```shell
sudo chown -R اسم_المستخدم مسار_المجلد
```

على سبيل المثال ، هذا هو كيفية منح المستخدم `abc` الحقوق الكاملة للمجلد الحالي:

```shell
sudo chown -R abc .
```

### تعيين كلمة مرور حساب root

إذا كنت بحاجة إلى استخدام حساب root ، فيمكنك استخدام الأمر التالي لتهيئة كلمة مروره:

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