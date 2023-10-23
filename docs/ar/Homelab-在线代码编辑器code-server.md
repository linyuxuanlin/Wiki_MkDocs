# الورشة المنزلية - محرر الشيفرة code-server على الإنترنت

![](https://img.wiki-power.com/d/wiki-media/img/202304132214418.png)

**code-server** هو محرر شيفرة يمكن تشغيله في متصفح الويب. واحدة من المزايا المهمة له على سطح المكتب هي القدرة على كتابة الشيفرة عبر أي جهاز عبر الإنترنت، بما في ذلك الهواتف المحمولة والأجهزة اللوحية التي لا يمكن تثبيت VS Code مباشرة عليها.

## النشر (بواسطة Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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
    environment: # يجب تشغيلها بصلاحيات الجذر، وإلا لن تتمكن من الوصول إلى مجلدات Docker الأخرى أو مجلد الجذر على المضيف
      - PUID=0
      - PGID=0
      - TZ=Asia/Shanghai
      - PASSWORD=${APP_PASSWORD} # اختياري
      - SUDO_PASSWORD=${APP_SUDO_PASSWORD} # اختياري
      #- SUDO_PASSWORD_HASH= # اختياري
      #- PROXY_DOMAIN=code.wiki-power.com # اختياري
    restart: unless-stopped
```

(اختياري) نوصي بإنشاء ملف `.env` في نفس المجلد الرئيسي لملف `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك هناك. إذا لم ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعاملات مباشرة في ملف `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `code-server`).

```dotenv title=".env"
STACK_NAME=code-server
STACK_DIR=xxx # مسار تخزين المشروع المخصص، مثل ./code-server
DATA_DIR_LOCAL=xxx # مجلد المضيف المحلي الذي يتم توصيله يدويًا، مثل /DATA

# code-server
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك - اختر منفذًا غير مستخدم بالفعل
APP_PASSWORD=xxx # كلمة المرور لتسجيل الدخول
APP_SUDO_PASSWORD=xxx # كلمة المرور للمستخدم الجذر - اختياري

```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس المجلد الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات.

## تفسير الإعدادات

### تكوين Git

بعد الانتهاء من التثبيت، إذا كنت بحاجة إلى استخدام Git، يرجى الرجوع إلى مقالة [**مذكرات تعلم Git**](https://wiki-power.com/ar/Git%E5%AD%A6%E4%B9%A0%E7%AC%94%E8%AE%B0#%E5%AE%89%E8%A3%85%E4%B8%8E%E9%85%8D%E7%BD%AE] للحصول على إرشادات حول تكوين اسم المستخدم والبريد الإلكتروني.

### مشكلة الأذونات

إذا واجهت مشكلة "Error: EACCES: permission denied" أثناء التعامل مع الملفات، يمكنك فتح الطرفية واستخدام الأمر التالي لمنح صلاحيات المستخدم الحالي على المجلد:

```shell
sudo chown -R اسم_المستخدم مسار_المجلد
```

مثلاً، إليك كيفية منح مالك المجلد "abc" صلاحيات على المجلد الحالي:

```shell
sudo chown -R abc .
```

### تعيين كلمة مرور الجذر

إذا كنت بحاجة إلى استخدام حساب الجذر، يمكنك استخدام الأمر التالي لتعيين كلمة مرور له:

```shell
sudo passwd root
```

## المراجعة والشكر

- [الموقع الرسمي](https://coder.com/docs/code-server/latest)
- [الوثائق / مستودع GitHub](https://github.com/linuxserver/docker-code-server)
- [مركز Docker](https://hub.docker.com/r/linuxserver/code-server)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.