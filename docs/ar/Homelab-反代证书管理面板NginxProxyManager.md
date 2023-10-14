# Homelab - لوحة إدارة شهادات الوكيل العكسي Nginx Proxy Manager

![](https://img.wiki-power.com/d/wiki-media/img/20230408182138.png)

**Nginx Proxy Manager** هو لوحة تحكم رسومية لـ Nginx ، والتي تتيح للمستخدمين تكوين الوكيل العكسي وطلب شهادة SSL للمواقع على واجهة الويب بسهولة ، دون الحاجة إلى معرفة الكثير من تفاصيل Nginx / Letsencrypt.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `nginx-proxy-manager`).

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # الافتراضي هو 81 ، يرجى الرجوع إلى الوثائق للتغيير
```

أخيرًا ، يمكنك تشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## تعليمات التكوين

اسم المستخدم وكلمة المرور الافتراضية:

- البريد الإلكتروني: `admin@example.com`
- كلمة المرور: `changeme`

الحصول على عنوان IP لـ Docker:

```shell
ip addr show docker0
```

ملاحظة: يرجى استخدام الوكيل العكسي للخدمات الذاتية الاستضافة عن طريق ربط النطاقات الفرعية (80/443 منافذ) وإغلاق المنافذ الأخرى في لوحة التحكم العامة للخادم على الإنترنت لزيادة الأمان.

## المراجع والشكر

- [الموقع الرسمي](https://nginxproxymanager.com)
- [الوثائق](https://nginxproxymanager.com/guide)
- [مستودع GitHub](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
