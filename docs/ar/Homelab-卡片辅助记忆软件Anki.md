# هوملاب - برنامج Anki لمساعدة الذاكرة باستخدام بطاقات

![صورة](https://img.wiki-power.com/d/wiki-media/img/202306191745527.png)

**Anki** هو تطبيق بطاقات الذاكرة مفتوح المصدر يساعد المستخدمين على حفظ مجموعة متنوعة من المعرفة بكفاءة وبسهولة، وعادة ما يُستخدم لحفظ الكلمات. يتميز بإستخدام منحنى النسيان في الذاكرة وإنشاء خطة مراجعة مناسبة وفقًا لأداء الدراسة، مما يساعد المستخدمين على الاستفادة القصوى من قوانين الذاكرة في الدماغ وتحقيق أفضل أداء للحفظ. يمتاز Anki بإمكانية التخصيص العالية حيث يمكنك إنشاء بطاقات دراسية خاصة بك تحتوي على نصوص وصور وحتى ملفات صوتية وفيديو. Anki متوافق أيضًا مع متعدد الأنظمة.

نظرًا لأن خادم المزامنة موجود في الخارج، قد يكون هناك أوقات يصعب فيها الوصول إلى الخادم بشكل طبيعي. يمكننا بناء خدمة المزامنة الخاصة باستخدام **anki-sync-server**. فيما يلي شرح استخدام صورة الـ Docker المُستخدمة هنا: `johngong/anki-sync-server` والتي تم اختبارها بنجاح.

## التكوين (Docker Compose)

أولاً، يجب عليك إنشاء ملف `compose.yaml` ولصق المحتوى التالي:

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

(اختياري) نوصي بإنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك فيه. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # قم بتخصيص مسار تخزين المشروع الخاص بك هنا، مثل: ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # قم بتخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم بالفعل
APP_USERNAME=xxx@xx.com # قم بتخصيص اسم المستخدم بتنسيق البريد الإلكتروني
APP_PASSWORD=xxxxxx # قم بتخصيص كلمة المرور الخاصة بك
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس المجلد الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات المُنسقة.

## توضيحات عن الإعداد

### نظام Windows

في نظام Windows، استخدمت نسخة [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (لم يتم اختبار الإصدار 2.1.65 وظهرت مشكلات في المزامنة).

بعد التثبيت، انقر على التوالي فوق "أدوات" ثم "الإضافات" في الشريط العلوي، ثم انقر على "الحصول على إضافة"، وأدخل رمز الإضافة `358444159` ثم انقر على "موافق"، ثم انقر على "الإعدادات" وقم بتعديل عنوان الخادم الذي قمت بنشر `anki-sync-server` عليه ومنفذه، ثم أعد تشغيل البرنامج.

بعد إعادة التشغيل، انتقل إلى الشاشة الرئيسية وانقر على "المزامنة"، وأدخل عنوان البريد الإلكتروني وكلمة المرور التي قمت بإدخالها عند

### الأندرويد

في جهاز Android ، نستخدم تطبيق AnkiDroid، والذي لا يتطلب تثبيت إضافات ويمكنك تخصيص عنوان الخادم بدون مشاكل. ومع ذلك، يتطلب تسجيل الدخول باستخدام HTTPS. يُفضل استخدام الوكيل العكسي لهذا الغرض (يمكنك الاطلاع على كيفية إعداد خادم الوكيل العكسي من خلال المقالة [**Homelab - إدارة شهادات الوكيل العكسي Nginx Proxy Manager**](to_be_replace[3])).

بعد تسجيل الدخول باستخدام HTTPS، يمكنك تكوين الخادم المخصص عند اختيار `Advanced` ثم `Custom sync server` في الشاشة الرئيسية. يُرجى ملاحظة أنه يجب إضافة "/msync" إلى نهاية عنوان الوسائط في خانة "Media sync url" للمزامنة بنجاح.

## مراجع وشكر

- [الموقع الرسمي](https://apps.ankiweb.net/)
- [الوثائق](https://www.navidrome.org/docs/installation/docker/)
- [مستودع GitHub](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.