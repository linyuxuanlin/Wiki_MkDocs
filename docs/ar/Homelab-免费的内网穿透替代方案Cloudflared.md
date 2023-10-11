# Homelab - بديل مجاني للاتصال بالشبكة الداخلية: Cloudflared

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

**Cloudflared** هو بديل مجاني للاتصال بالشبكة الداخلية، ويستخدم للوصول إلى الخوادم التي لا تملك عنوان IP العام.

المتطلبات الأساسية:

- على الرغم من أن Cloudflared مجاني، إلا أنه يتطلب تسجيل حساب VISA/PayPal.
- يجب أن يشير NameServer إلى Cloudflare.
- يجب تمكين CDN Cloudflare (بطيء في الوصول من داخل الصين).

المزايا:

- لا يتطلب وجود خادم بعنوان IP العام.
- لا يتطلب جدار حماية أو خادم وكيل عكسي.
- يمكن استخدام منافذ 80 و 443 دون الحاجة إلى ترخيص.
- لا يتطلب الحصول على شهادة SSL.
- مجاني.

العيوب:

- بطيء في الوصول من داخل الصين.
- يعتمد نسبيًا على منصة Cloudflare.

## التثبيت (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `cloudflared`).

```dotenv title=".env"
STACK_NAME=cloudflared

# cloudflared
APP_VERSION=latest
APP_TUNNEL_TOKEN=xxx # استبدله برمز الوصول الخاص بك
```

أخيرًا، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الإعداد.

## تفاصيل التكوين

قم بزيارة لوحة [**Cloudflare Zero Trust**](https://one.dash.cloudflare.com/)، واختر `Access` - `Tunnels` في الشريط الجانبي الأيسر، ثم انقر على `Create a tunnel` لإنشاء نفق، وأدخل اسم النفق (للتمييز بين الأجهزة المختلفة) ثم احفظه. ثم احتفظ برمز الوصول وأدخله في `compose.yaml`.

ثم انتقل إلى النفق الذي أنشأته، وفي علامة التبويب `Public Hostname Page`، أضف منفذ الوكيل. على سبيل المثال، إذا كان اسم النطاق المرتبط بـ Cloudflare هو `wiki-power.com`، وكان منفذ الخدمة المحلية هو `80` وبروتوكول `HTTP`، فما عليك سوى إدخال البيانات التالية:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416183438.png)

يمكنك الآن الوصول إلى منفذ محلي عن طريق <https://dashboard.wiki-power.com>، وسيتم تلقائيًا تطبيق شهادة SSL للوصول عبر HTTPS.

## المراجع والشكر

- [الموقع الرسمي / الوثائق](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [مستودع GitHub](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
