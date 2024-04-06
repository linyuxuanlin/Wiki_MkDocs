# الورشة المنزلية - تطبيق Anki لمساعدة الذاكرة بواسطة البطاقات

![](https://media.wiki-power.com/img/202306191745527.png)

**Anki** هو تطبيق مفتوح المصدر يستخدم لتسهيل عملية حفظ مجموعة متنوعة من المعلومات بكفاءة، ويُستخدم عادة لحفظ الكلمات والمصطلحات. يتميز Anki بالعمل بناءً على منحنى نسيان الذاكرة، حيث يُنشئ خطة مراجعة مناسبة استنادًا إلى تقدم عملية التعلم. يساعد هذا المنهج الطلاب على الاستفادة القصوى من نمط الذاكرة في أدمغتهم لتحقيق أفضل أداء في عملية الحفظ. يتيح Anki أيضًا للمستخدمين إمكانية تخصيص عالية، حيث يمكنهم إنشاء بطاقات دراسية خاصة بهم تحتوي على نصوص وصور وحتى ملفات صوتية وفيديو. ويمكن استخدام Anki على عدة منصات.

نظرًا لأن خادم المزامنة موجود في الخارج في بعض الأحيان، قد يكون هناك مشكلات في عملية المزامنة. لذلك يمكننا استخدام **anki-sync-server** لإعداد خادم المزامنة بأنفسنا. فيما يلي الإرشادات باستخدام صورة `johngong/anki-sync-server` التي تم اختبارها والتي يمكن استخدامها بشكل طبيعي.

## النشر باستخدام Docker Compose

أولاً، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يُوصى بإنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك فيه. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في ملف `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `anki-sync-server`).

```dotenv title=".env"
STACK_NAME=anki-sync-server
STACK_DIR=/DATA/AppData/anki-sync-server # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال: ./anki-sync-server

# anki-sync-server
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك - اختر منفذًا غير مستخدم مسبقًا
APP_USERNAME=xxx@xx.com  # قم بتخصيص اسم المستخدم - يجب أن يكون بتنسيق البريد الإلكتروني
APP_PASSWORD=xxxxxx # حدد كلمة المرور الخاصة بك
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس دليل `compose.yaml` لبدء تشغيل الحاويات.

## تعليمات التكوين

### نظام التشغيل Windows

على نظام التشغيل Windows، تم اختبار استخدام [**Anki 2.1.28**](https://github.com/ankitects/anki/releases/download/2.1.28/anki-2.1.28-windows.exe) (تم اختباره على أنه لا يمكن المزامنة بنجاح باستخدام الإصدار 2.1.65).

بعد التثبيت، انتقل إلى الشريط العلوي وانقر على "أدوات"، ثم انتقل إلى "الملحقات" ومن ثم انقر على "الحصول على ملحق"، ثم قم بإدخال رمز الملحق "358444159" وانقر على "موافق". بعد ذلك، انتقل إلى "الإعدادات" وقم بتغيير عنوان الخادم الذي نصبت فيه "anki-sync-server" ومنفذه إلى عنوان ومنفذ الخادم الخاص بك. أخيرًا، قم بإعادة تشغيل البرنامج.

بعد إعادة التشغيل، انتقل إلى الشاشة الرئي

### أندرويد

في الجانب الخاص بنظام Android، يتم استخدام تطبيق AnkiDroid. يمكنك تخصيص عنوان الخادم بدون الحاجة إلى تثبيت إضافات، ولكن يجب أن يكون لديك اتصال HTTPS. يُفضل استخدام خادم الوكيل العكسي لتحقيق ذلك (يمكنك الرجوع إلى مقال [Homelab - لوحة إدارة شهادات خادم الوكيل العكسي Nginx Proxy Manager](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/) لمعرفة كيفية إعداد خادم الوكيل العكسي).

بعد تسجيل الدخول باستخدام اتصال HTTPS، يُمكنك تكوين الخادم الخاص بك من خلال الانتقال إلى القسم الرئيسي واختيار `Advanced` - `Custom sync server`. يجب ملاحظة أنه يجب إضافة `/msync` إلى عنوان الوسائط الأصلي في خانة `Media sync URL` لضمان التزامن الصحيح.

## مراجع وشكر

- [الموقع الرسمي](https://apps.ankiweb.net/)
- [الوثائق](https://www.navidrome.org/docs/installation/docker/)
- [مستودع GitHub](https://github.com/ankicommunity/anki-sync-server)
- [Docker Hub](https://hub.docker.com/r/johngong/anki-sync-server)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
