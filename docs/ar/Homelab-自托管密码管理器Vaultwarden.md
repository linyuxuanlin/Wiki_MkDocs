# Homelab - مدير كلمات المرور المستضاف ذاتيًا Vaultwarden

![](https://media.wiki-power.com/img/20230304195414.jpg)

**Vaultwarden** هو خادم Bitwarden المستضاف ذاتيًا من طرف ثالث يسمح بحماية وإدارة كلمات المرور لمواقع الويب المختلفة من خلال كلمة مرور رئيسية ويمكنه توليد كلمات مرور عشوائية للاستخدام في مواقع الويب المختلفة.

## النشر (Docker Compose)

أولاً ، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك أيضًا تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # منفذ الوصول المخصص ، اختر منفذًا غير مستخدم
```

أخيرًا ، قم بتنفيذ الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات النشر.

## تعليمات التكوين

يتطلب Vaultwarden الوصول عبر HTTPS افتراضيًا ، ويوصى باستخدام خادم بروكسي عكسي (يمكن الاطلاع على مقالة **Homelab - لوحة إدارة شهادات الوكالة العكسية Nginx Proxy Manager** للحصول على معلومات حول إعداد خادم بروكسي عكسي).

عند استخدام الامتدادات المتصفح وتطبيقات سطح المكتب والجوال ، يجب النقر على الإعدادات في صفحة تسجيل الدخول وتكوين عنوان URL للخادم لاستخدام الخدمة المستضافة ذاتيًا بشكل صحيح.

علاوة على ذلك ، لا يتوافق إصدار Vaultwarden القديم (أقل من 1.27.0) مع امتدادات المتصفح لـ Bitwarden ، مما يؤدي إلى عدم القدرة على تسجيل الدخول. راجع المشكلة: [**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082).

نظرًا لأنها خدمة مستضافة ذاتيًا ، يجب أن تهتم بأمان البيانات بنفسك. تذكر أن تقوم بنسخ احتياطي لقاعدة بيانات كلمات المرور بانتظام.

## المراجع والشكر

- [الموقع الرسمي](https://github.com/dani-garcia/vaultwarden/wiki)
- [الوثائق](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [مستودع GitHub](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
