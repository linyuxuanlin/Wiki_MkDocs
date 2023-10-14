# Homelab - أداة frp للاتصال بالشبكة الداخلية

**frp** هي طريقة للاتصال بالشبكة الداخلية. يمكنك عرض منافذ جهاز الشبكة الداخلية على الإنترنت من خلال خادم يحتوي على عنوان IP عام. يدعم frp العديد من البروتوكولات مثل TCP و UDP و HTTP و HTTPS.

## تثبيت الخادم frps (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  frps:
    container_name: ${STACK_NAME}_app
    image: snowdreamtech/frps:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frps.ini:/etc/frp/frps.ini
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، مثل ./frps

# frps
APP_VERSION=latest
```

أضف ملف تكوين `frps.ini` إلى مسار تخزين المشروع `${STACK_DIR}`:

```ini title="frps.ini"
[common]
bind_port = 7000 # منفذ الاتصال بين العميل والخادم ، سيتم استخدامه في تكوين العميل لاحقًا.
dashboard_port = 7500 # منفذ لوحة القيادة للخادم
token = ${TOKEN-FRPS} # كلمة مرور الاتصال بين العميل والخادم ، يرجى تعيينها بنفسك.
dashboard_user = ${USERNAME-FRPS} # اسم المستخدم
dashboard_pwd = ${PASSWORD-FRPS} # كلمة المرور
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

إذا كنت لا تستخدم Docker ، فيمكنك الرجوع إلى هذه المقالة: [**تكوين الخادم · كيفية تحقيق التحكم عن بعد في RDP عبر الإنترنت (frp)**](https://wiki-power.com/ar/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2).

## تثبيت العميل frpc (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.3"
services:
  frpc:
    container_name: ${STACK_NAME}_app
    image: stilleshan/frpc:${APP_VERSION}
    network_mode: "host"
    volumes:
      - ${STACK_DIR}/frpc.ini:/frp/frpc.ini
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `replace`).

```dotenv title=".env"
STACK_NAME=replace
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، مثل ./replace

```

أضف ملف تكوين `frpc.ini` إلى مسار تخزين المشروع `${STACK_DIR}`:

```ini title="frpc.ini"
[common]
server_addr = ${SERVER_ADDR} # عنوان IP للخادم الذي يحتوي على frps
server_port = 7000 # منفذ الاتصال بين العميل والخادم ، يجب أن يتطابق مع bind_port في frps.ini
token = ${TOKEN-FRPC} # كلمة مرور الاتصال بين العميل والخادم ، يجب أن تتطابق مع token في frps.ini
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

# replace
APP_VERSION=latest
```

أضف ملف تكوين `frps.ini` إلى مسار تخزين مشروعك `${STACK_DIR}`:

```ini title="frpc.ini"
[common]
server_addr = xx.xx.xx.xx # عنوان IP العام للخادم
server_port = 7000 # يجب أن يتطابق مع منفذ الخادم
tls_enable = true
token = ${TOKEN-FRPS} # يجب أن يتطابق مع رمز الخادم

[xxx]
type = tcp
remote_port = xx # رقم المنفذ الذي يمكن الوصول إليه عبر الإنترنت
local_ip = localhost
local_port = xx # رقم المنفذ الداخلي
```

أخيرًا ، قم بتشغيل حاويات الترتيب الخاصة بك بتنفيذ الأمر `docker compose up -d` في نفس دليل `compose.yaml`.

## المراجع والشكر

- [مستودع GitHub · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [مستودع GitHub · stilleshan/frpc
  ](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [كيفية تنفيذ التحكم عن بعد RDP عبر الإنترنت (frp) ](https://wiki-power.com/ar/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [استخدام frp للوصول إلى NAS الجماعية ](https://wiki-power.com/ar/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.