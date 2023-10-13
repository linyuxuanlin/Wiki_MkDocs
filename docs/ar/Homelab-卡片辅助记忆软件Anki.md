# Homelab - برنامج Anki للمساعدة في الذاكرة بواسطة البطاقات

![](https://img.wiki-power.com/d/wiki-media/img/202306191745527.png)

**Anki** هو تطبيق بطاقات ذاكرة مفتوح المصدر يساعد المستخدمين على تذكر مختلف نقاط المعرفة بسهولة وكفاءة، وعادة ما يستخدم لحفظ الكلمات الفردية. يتميز بطريقة استخدام منحنى نسيان الذاكرة، حيث يتم إنشاء خطة مراجعة مناسبة وفقًا لحالة التعلم، ويساعد المستخدمين على الاستفادة الكاملة من قواعد الذاكرة في الدماغ لتحقيق أفضل نتائج الذاكرة. يتميز Anki بمرونة عالية، حيث يمكنك إنشاء بطاقات دراسية خاصة بك، بما في ذلك النصوص والصور وحتى الصوت والفيديو. كما يدعم Anki استخدام متعدد المنصات.

نظرًا لأن خادم المزامنة في الخارج، قد يتعذر في بعض الأحيان المزامنة بشكل صحيح، يمكننا استخدام **anki-sync-server** لإنشاء خدمة مزامنة خاصة بنا. يستخدم البرنامج النصي التالي `johngong/anki-sync-server`، ويمكن استخدامه بشكل طبيعي، ولم يتم اختبار الإصدارات الأخرى.

## النشر (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  anki-sync-server:
    container_name: ${STACK_NAME}_app
    image: johngong/anki-sync-server:${APP_VERSION}
    ports:
      - "${APP_PORT}:27701"
    volumes:
      - ${STACK_DIR}:/config
    environment:
      - ANKI_SYNC_SERVER_USER=${APP_USERNAME}
      - ANKI_SYNC_SERVER_PASSWORD=${APP_PASSWORD}
      - UID=1000
      - GID=1000
    restart: unless-stopped
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # مسار تخزين المشروع المخصص، مثل ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر غير مستخدم فقط
APP_USERNAME=xxx@xx.com  # تخصيص اسم المستخدم الخاص بك، يجب أن يكون بتنسيق البريد الإلكتروني
APP_PASSWORD=xxxxxx # تخصيص كلمة المرور الخاصة بك
```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## تعليمات التكوين

### Windows

في Windows، استخدمت [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (تم اختبارها وتبين أن 2.1.65 لا يمكن المزامنة).

بعد التثبيت، انقر على `أدوات` - `المكونات الإضافية` في الشريط العلوي، ثم انقر على `الحصول على المكونات الإضافية`، ثم أدخل رمز المكون الإضافي `358444159` وانقر على `موافق`، ثم انقر على `الإعدادات`، وقم بتغيير العنوان إلى عنوان الخادم الذي نشرته `anki-sync-server` والمنفذ، ثم أعد تشغيل البرنامج.

بعد إعادة التشغيل، انقر فوق المزامنة في الواجهة الرئيسية، ثم أدخل عنوان البريد الإلكتروني وكلمة المرور التي قمت بإدخالها عند نشر Docker للمزامنة.

إذا لم يتمكن من المزامنة بعد ذلك، يرجى الرجوع إلى [**Setting up Anki**](https://github.com/ankicommunity/anki-sync-server/blob/develop/README.md#setting-up-anki).

### Android

يستخدم AnkiDroid على نظام Android ، ولا يلزم تثبيت أي ملحقات لتخصيص عنوان الخادم ، ولكن يجب تسجيل الدخول باستخدام https. يوصى باستخدام الوكيل العكسي (يمكن الرجوع إلى مقالة بناء خادم الوكيل العكسي لإدارة شهادات الوكيل العكسي Nginx Proxy Manager).

بعد تسجيل الدخول باستخدام https ، يمكن تكوين الخادم المخصص عن طريق الانتقال إلى "Advanced" - "Custom sync server" في الشاشة الرئيسية. يجب ملاحظة أنه يجب إضافة "/msync" بعد العنوان الأصلي في خانة "Media sync url" للمزامنة الصحيحة.

المراجع والشكر:

- الموقع الرسمي
- الوثائق
- مستودع GitHub
- Docker Hub

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
