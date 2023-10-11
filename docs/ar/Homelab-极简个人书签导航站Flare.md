# Homelab - موقع إشارات مرجعية شخصي بسيط Flare

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410170939.png)

**Flare** هو موقع إشارات مرجعية شخصي خفيف وسريع وجميل، ولا يعتمد على أي قاعدة بيانات، ويتم فتح بيانات التطبيق بشكل كامل وشفاف، ويدعم التحرير عبر الإنترنت، ويحتوي على أكثر من 6,000 رمز Material Design Icons.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.6"

services:
  flare:
    container_name: ${STACK_NAME}_app
    image: soulteary/flare:${APP_VERSION}
    # المزيد من معلمات البدء يرجى الرجوع إلى الوثائق https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    ports:
      - ${APP_PORT}:5005
    volumes:
      - ${STACK_DIR}:/app
    command: flare --nologin=0 # تمكين وضع تسجيل الدخول للمستخدمين ، يجب تعيين معلمة البدء nologin على 0 أولاً
    environment:
      - FLARE_USER= ${APP_USER} # في حالة تمكين وضع تسجيل الدخول للمستخدمين ولم يتم تعيين FLARE_USER ، فإن المستخدم الافتراضي هو `flare`
      - FLARE_PASS= ${APP_PASS} # في حالة تمكين وضع تسجيل الدخول للمستخدمين ولم يتم تعيين FLARE_USER ، سيتم إنشاء كلمة مرور افتراضية وعرضها في سجل التشغيل التطبيق
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `flare`).

```dotenv title=".env"
STACK_NAME=flare
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./flare

# flare
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، فقط اختر غير مستخدم
APP_USER=xxxx # تخصيص اسم المستخدم الخاص بك
APP_PASS=xxxx # تخصيص كلمة المرور الخاصة بك
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الإعداد.

## تعليمات التكوين

يمكن تعديل عناوين التطبيقات والإشارات المرجعية في `${DIR}/flare`. سيتم تحديث الحاوية في الوقت الفعلي. يمكنك أيضًا إضافة المعلمات التالية إلى عنوان URL لتصحيح:

- دليل التشغيل: `/guide`
- صفحة الإعدادات: `/settings`
- التحرير عبر الإنترنت: `/editor`
- الحصول على الرموز: `/icons`
- صفحة المساعدة: `/help`

## المراجع والشكر

- [الموقع الرسمي](https://soulteary.com/2022/02/23/building-a-personal-bookmark-navigation-app-from-scratch-flare.html)
- [الوثائق / مستودع GitHub](https://github.com/soulteary/docker-flare)
- [Docker Hub](https://hub.docker.com/r/soulteary/flare/)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
