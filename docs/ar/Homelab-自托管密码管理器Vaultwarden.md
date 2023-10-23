# الوكالة المنزلية - مدير كلمات المرور Vaultwarden ذات الاستضافة الذاتية

![](https://img.wiki-power.com/d/wiki-media/img/20230304195414.jpg)

**Vaultwarden** هو خادم Bitwarden الذي يتمتع بالاستضافة الذاتية والذي يسمح لك بحماية وإدارة كلمات المرور الخاصة بالمواقع المختلفة باستخدام كلمة مرور رئيسية ويمكن أيضًا توليد كلمات مرور عشوائية للاستخدام على المواقع المختلفة.

## النشر (باستخدام Docker Compose)

أولًا، قم بإنشاء ملف `compose.yaml` وقم بلصق المحتوى التالي:

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

(اختياري) يُوصى بإنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا لم تكن ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة في ملف `compose.yaml` الخاص بك (على سبيل المثال، استبدال `${STACK_NAME}` بـ `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، مثل ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # قم بتخصيص منفذ الوصول الخاص بك، اختر منفذ غير مستخدم مسبقًا
```

أخيرًا، يمكنك ببساطة تشغيل الحاويات المكونة عن طريق تنفيذ الأمر `docker-compose up -d` في نفس دليل ملف `compose.yaml`.

## توجيهات الضبط

يتطلب Vaultwarden افتراضيًا استخدام اتصال HTTPS، ويُوصى بشدة باستخدام خادم بروكسي عكسي (Reverse Proxy) (يمكنك الرجوع إلى مقال [**Homelab - إدارة الشهادات لوحة البروكسي Nginx Proxy Manager**](https://to_be_replace[3]) لبناء خادم بروكسي عكسي).

عند استخدام الامتدادات للمتصفح وتطبيقات سطح المكتب والهواتف المحمولة، يجب عليك النقر على الإعدادات على صفحة تسجيل الدخول وتكوين عنوان URL للخادم حتى تتمكن من استخدام خدمة الاستضافة الذاتية بشكل صحيح.

بالإضافة إلى ذلك، الإصدارات القديمة (أقل من 1.27.0) من Vaultwarden غير متوافقة مع ملحقات المتصفح الخاصة بـ Bitwarden، وهذا قد يؤدي إلى عدم القدرة على تسجيل الدخول. للمزيد من التفاصيل، انظر إلى المشكلة: [**فشل العميل في الاتصال أو تسجيل الدخول**](https://github.com/dani-garcia/vaultwarden/issues/3082).

نظرًا لأنها خدمة تتيح لك الاستضافة الذاتية، يجب عليك أن تتابع أمان البيانات بنفسك. لا تنس تنفيذ نسخ احتياطية من قاعدة بيانات كلمات المرور بانتظام.

## المراجع والشكر

- [الموقع الرسمي](https://github.com/dani-garcia/vaultwarden/wiki)
- [الوثائق](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [مستودع GitHub](https://github.com/dani-garcia/vaultwarden)
- [مستودع Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.