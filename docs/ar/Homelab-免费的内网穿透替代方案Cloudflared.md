# معمل المنزل - بديل مجاني للاتصال الداخلي عبر الإنترنت: Cloudflared

![](https://media.wiki-power.com/img/20230416143051.png)

**Cloudflared** هو حلاً مجانيًا للاتصال الداخلي عبر الإنترنت، يُستخدم للوصول من الإنترنت إلى أجهزة الخادم التي ليس لديها عنوان IP عام.

المتطلبات الأساسية:

- على الرغم من أن Cloudflared مجاني، إلا أنه يتطلب ربط ببطاقة VISA/PayPal.
- يجب أن يشير NameServer للنطاق إلى خدمة Cloudflare.
- يجب تمكين خدمة Cloudflare CDN (سرعة الوصول في الداخل تكون بطيئة).

المزايا:

- ليس هناك حاجة لخادم عام.
- ليس هناك حاجة لجدار حماية أو بروكسي عكسي.
- يمكن استخدام المنافذ 80 و443 بدون الحاجة للترخيص.
- ليس هناك حاجة لطلب شهادة SSL بنفسك.
- مجاني.

العيوب:

- سرعة الوصول في الداخل تكون بطيئة.
- يعتمد نسبيًا على منصة Cloudflare.

## النشر (Docker Compose)

ابدأ أولاً بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  cloudflared:
    container_name: ${STACK_NAME}_app
    image: cloudflare/cloudflared:${APP_VERSION}
    network_mode: host
    restart: unless-stopped
    command: tunnel run
    environment:
      - TUNNEL_TOKEN=${APP_TUNNEL_TOKEN}
```

(اختياري) يُوصى بإنشاء ملف `.env` في نفس الدليل الذي يحتوي على ملف `compose.yaml`، وقم بتخصيص متغيرات البيئة الخاصة بك فيه. إذا لم ترغب في استخدام متغيرات البيئة، يمكنك أيضًا تخصيص المعلمات مباشرة في ملف `compose.yaml` الخاص بك (على سبيل المثال، استبدال `${STACK_NAME}` بـ `cloudflared`).

```dotenv title=".env"
STACK_NAME=cloudflared

# cloudflared
APP_VERSION=latest
APP_TUNNEL_TOKEN=xxx # قم بتبديله بالرمز الخاص بك
```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس الدليل الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات الخاصة بك.

## توضيحات الإعداد

قم بزيارة [**لوحة تحكم Cloudflare Zero Trust**](https://one.dash.cloudflare.com/)، ثم اختر في القائمة الجانبية اليسرى `Access` - `Tunnels`، ثم انقر على "إنشاء نفق" لإنشاء النفق. قم بتقديم اسم للنفق (يُستخدم للتمييز بين أجهزة الخادم المختلفة) واحتفظ بالرمز الخاص به، ثم قم بإدخاله في ملف `compose.yaml`.

بعد ذلك، انتقل إلى النفق الذي أنشأته، واذهب إلى علامة التبويب "صفحة اسم الاستضافة العامة" وأضف المنافذ التي تريد تمثيلها. على سبيل المثال، إذا كنت قد قمت بربط نطاق Cloudflare الخاص بك باسم النطاق `wiki-power.com`، وكنت ترغب في تمثيل منفذ محلي بالمنفذ 80 وبروتوكول HTTP، يمكنك القيام بذلك عن طريق:

![](https://media.wiki-power.com/img/20230416183438.png)

بهذه الطريقة، يمكنك الوصول إلى المنفذ المحلي من خلال <https://dashboard.wiki-power.com>، وسيتولى النظام طلب شهادة SSL تلقائيًا لتمكين الوصول عبر الإنترنت بواسطة HTTPS.

## المراجع والشكر

- [الموقع الرسمي / الوثائق](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [مستودع GitHub](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
