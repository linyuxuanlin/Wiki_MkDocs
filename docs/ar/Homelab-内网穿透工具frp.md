# اللاب المنزلي - أداة اختراق الشبكة الداخلية frp

![صورة](https://media.wiki-power.com/img/20230304195137.png)

**frp** هو أسلوب لاختراق الشبكة الداخلية. يمكنك تعريض منفذ الجهاز المضيف في الشبكة الداخلية للإنترنت عن طريق خادم لديه عنوان IP عام. يدعم frp العديد من البروتوكولات مثل TCP وUDP وHTTP وHTTPS وغيرها.

## نشر الخادم frps (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل مع `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `frps`).

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # مسار تخزين المشروع الخاص بك، على سبيل المثال ./frps

# frps
APP_VERSION=latest
```

قم بإضافة ملف تكوين `frps.ini` في مسار تخزين المشروع `${STACK_DIR}` الخاص بك:

```ini title="frps.ini"
[common]
bind_port = 7000 # منفذ الاتصال بين العميل والخادم، سيتم استخدامه لاحقًا أثناء إعداد العميل.
dashboard_port = 7500 # منفذ لوحة القيادة للخادم
token = ${TOKEN-FRPS} # كلمة المرور لاتصال العميل والخادم، يُفضل تخصيصها بنفسك.
dashboard_user = ${USERNAME-FRPS} # اسم المستخدم
dashboard_pwd = ${PASSWORD-FRPS} # كلمة المرور
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس الدليل مع ملف `compose.yaml` لبدء تشغيل الحاويات.

إذا كنت لا تستخدم Docker، يمكنك أيضًا الرجوع إلى هذا المقال: [**تكوين الخادم·كيفية تنفيذ التحكم عن بعد عبر الإنترنت (frp)**](https://wiki-power.com/ar/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2) لمزيد من المعلومات.

## نشر العميل frpc (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) نوصي بإنشاء ملف `.env` في نفس الدليل مع `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `replace`).

````dotenv title=".env"
STACK_NAME=replace
STACK_DIR=xxx # مسار تخزين المشروع الخاص بك، على سبيل المثال ./replace


```markdown
# استبدال
APP_VERSION=latest
````

في مسار تخزين مشروعك `${STACK_DIR}`, أضف ملف تكوين بالاسم `frps.ini`:

```ini title="frpc.ini"
[common]
server_addr = xx.xx.xx.xx # عنوان الآي بي العام للخادم
server_port = 7000 # قم بتطابقه مع منفذ الخادم
tls_enable = true
token = ${TOKEN-FRPS} # قم بتطابقه مع الرمز الخاص بالخادم

[xxx]
type = tcp
remote_port = xx # رقم المنفذ الذي يمكن الوصول إليه عبر الإنترنت
local_ip = localhost
local_port = xx # رقم المنفذ داخل الشبكة المحلية
```

أخيرًا، يمكنك تشغيل حاويات النظم المعدة ببساطة عبر تنفيذ الأمر `docker compose up -d` في الدليل الرئيسي لملف `compose.yaml`.

## المراجع والشكر

- [مستودع GitHub · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [مستودع GitHub · stilleshan/frpc](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [كيفية تنفيذ التحكم عن بعد لديك RDP عبر الإنترنت (frp) [للإشارة[3]]%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [الوصول إلى NAS من سينولوجي باستخدام frp [للإشارة[3]]%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

[للإشارة[1]]
[للإشارة[2]]

```

Note: I have translated the text into Arabic while preserving the original markdown format.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
