# الرئيسية - لوحة إدارة شهادة الاستضافة المعكوسة Nginx Proxy Manager

![صورة](https://media.wiki-power.com/img/20230408182138.png)

**Nginx Proxy Manager** هو لوحة تحكم رسومية لـ Nginx، تمكّن المستخدمين من تكوين الاستضافة المعكوسة بسهولة وطلب شهادات SSL للمواقع عبر واجهة الويب دون الحاجة إلى معرفة تفاصيل داخلية متعلقة بـ Nginx أو Let's Encrypt.

## النشر (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` وقم بلصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  nginx-proxy-manager:
    container_name: ${STACK_NAME}_app
    image: "jc21/nginx-proxy-manager:${APP_VERSION}"
    ports:
      - "${APP_PORT}:81" # عنوان اللوحة
      - "80:80"
      - "443:443"
    volumes:
      - ${STACK_DIR}/data:/data
      - ${STACK_DIR}/letsencrypt:/etc/letsencrypt
    restart: unless-stopped
```

(اختياري) يُفضل إنشاء ملف `.env` في نفس المجلد مع `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا لم تكن ترغب في استخدام المتغيرات البيئية، يمكنك أيضاً تخصيص المعلمات مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `nginx-proxy-manager`).

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، مثل ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # الافتراضي 81، يمكنك تغييره وفقًا للوثائق
```

أخيرًا، يمكنك تشغيل الحاويات المكونة عن طريق تنفيذ الأمر `docker-compose up -d` في نفس المجلد الذي يحتوي على ملف `compose.yaml`.

## توضيحات التكوين

اسم المستخدم وكلمة المرور الافتراضيين:

- البريد الإلكتروني: `admin@example.com`
- كلمة المرور: `changeme`

للحصول على عنوان IP لـ Docker:

```shell
ip addr show docker0
```

ملحوظة: من الأفضل استخدام الخدمات الذاتية الاستضافة عبر الاستضافة المعكوسة باستخدام اتصال فرعي للنطاق (المنافذ 80/443) وإغلاق المنافذ الأخرى في جدران الجدران على لوحة تحكم الخادم العام على الإنترنت لزيادة مستوى الأمان.

## المراجع والشكر

- [الموقع الرسمي](https://nginxproxymanager.com)
- [الوثائق](https://nginxproxymanager.com/guide)
- [مستودع GitHub](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
