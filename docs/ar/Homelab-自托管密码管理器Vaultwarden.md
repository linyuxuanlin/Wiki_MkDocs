# Homelab - خادم إدارة كلمات المرور Vaultwarden المستضاف ذاتيًا

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195414.jpg)

**Vaultwarden** هو خادم Bitwarden المستضاف ذاتيًا من طرف ثالث ، يحمي كلمات المرور لمختلف المواقع ويديرها بواسطة كلمة مرور رئيسية ، ويمكنه إنشاء كلمات مرور عشوائية للاستخدام في مواقع مختلفة.

## التنصيب (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  vaultwarden:
    container_name: ${STACK_NAME}_app
    image: vaultwarden/server:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}:/data/
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، اختر غير مستخدم فقط
```

أخيرًا ، يمكنك تشغيل الحاويات المرتبطة عن طريق تنفيذ الأمر `docker compose up -d` في نفس مستوى `compose.yaml`.

## تعليمات التكوين

يتطلب Vaultwarden الوصول عبر HTTPS بشكل افتراضي ، ويوصى باستخدام الوكيل العكسي (يمكن الرجوع إلى مقالة **Homelab - لوحة إدارة شهادات الوكيل العكسي Nginx Proxy Manager** لمعرفة كيفية إعداد الخادم العكسي).

عند استخدام الامتدادات المتصفح وتطبيقات سطح المكتب والجوال ، يجب النقر على الإعدادات في صفحة تسجيل الدخول وتكوين عنوان URL للخادم لاستخدام الخدمة المستضافة ذاتيًا بشكل صحيح.

علاوة على ذلك ، لا يتوافق إضافة المتصفح القديمة (الإصدارات الأقل من 1.27.0) من Vaultwarden و Bitwarden ، مما يؤدي إلى عدم القدرة على تسجيل الدخول. انظر المسألة: [**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082).

نظرًا لأنها خدمة مستضافة ذاتيًا ، يجب الانتباه إلى أمان البيانات. تذكر نسخ قاعدة بيانات كلمات المرور بانتظام.

## المراجع والشكر

- [الموقع الرسمي](https://github.com/dani-garcia/vaultwarden/wiki)
- [الوثائق](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [مستودع GitHub](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
