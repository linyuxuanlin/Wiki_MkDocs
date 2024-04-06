# الخادم المنزلي - موقع العلامات التجارية الشخصي بسيط جداً Flare

![صورة](https://media.wiki-power.com/img/20230410170939.png)

**Flare** هو موقع للعلامات التجارية الشخصي بسيط، سريع وجذاب، بدون الحاجة إلى قاعدة بيانات، وبيانات التطبيق مفتوحة بالكامل وشفافة، ويدعم التحرير عبر الإنترنت، ويحتوي على أكثر من 6,000 أيقونة من Material Design.

## التثبيت (Docker Compose)

أولاً، أنشئ ملف "compose.yaml" وألصق فيه المحتوى التالي:

```yaml title="compose.yaml"
version: "3.6"

services:
  flare:
    container_name: ${STACK_NAME}_app
    image: soulteary/flare:${APP_VERSION}
    # لمزيد من معلومات حول معلمات البدء، يُرجى الرجوع إلى الوثائق التالية: https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    ports:
      - ${APP_PORT}:5005
    volumes:
      - ${STACK_DIR}:/app
    command: flare --nologin=0 # لتمكين وضع تسجيل الدخول للمستخدمين، يجب تعيين معلمة "nologin" إلى "0" أولاً
    environment:
      - FLARE_USER= ${APP_USER} # في حالة تمكين وضع تسجيل الدخول للمستخدمين وعدم تعيين FLARE_USER، سيتم افتراض المستخدم كـ "flare"
      - FLARE_PASS= ${APP_PASS} # في حالة تمكين وضع تسجيل الدخول للمستخدمين وعدم تعيين FLARE_USER، سيتم إنشاء كلمة مرور افتراضية وعرضها في سجل بدء التطبيق
    restart: always
```

(اختياري) نوصي بإنشاء ملف ".env" في نفس مستوى ملف "compose.yaml" وتخصيص المتغيرات البيئية الخاصة بك فيه. إذا لم ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل "compose.yaml" (على سبيل المثال، استبدل "${STACK_NAME}" بـ "flare").

```dotenv title=".env"
STACK_NAME=flare
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال: ./flare

# flare
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذ غير مستخدم مسبقاً
APP_USER=xxxx # حدد اسم المستخدم الخاص بك
APP_PASS=xxxx # حدد كلمة المرور الخاصة بك
```

أخيراً، يمكنك تشغيل الحاويات بواسطة تنفيذ الأمر "docker compose up -d" في نفس المجلد الذي يحتوي على ملف "compose.yaml".

## توجيهات التكوين

يمكنك تعديل عناوين التطبيقات والعلامات التجارية في الملفات "apps.yml" و"bookmarks.yml" داخل "${DIR}/flare". سيتم تحديث الحاوية تلقائياً. يمكنك أيضاً إجراء عمليات تصحيح بإضافة المعلمات التالية إلى عنوان URL:

- للتوجيه: "/guide"
- لصفحة الإعدادات: "/settings"
- للتحرير عبر الإنترنت: "/editor"
- للحصول على الأيقونات: "/icons"
- لصفحة المساعدة: "/help"

## المراجع والشكر

- [الموقع الرسمي](https://soulteary.com/2022/02/23/building-a-personal-bookmark-navigation-app-from-scratch-flare.html)
- [الوثائق / مستودع GitHub](https://github.com/soulteary/docker-flare)
- [Docker Hub](https://hub.docker.com/r/soulteary/flare/)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
