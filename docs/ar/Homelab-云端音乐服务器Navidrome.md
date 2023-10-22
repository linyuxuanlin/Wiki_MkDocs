# Homelab - مختبر منزلي - خادم موسيقى سحابي Navidrome

![صورة](https://img.wiki-power.com/d/wiki-media/img/20230531212854.png)

**Navidrome** هو خادم موسيقى مفتوح المصدر قائم على الويب وخدمة بث يمكنك استخدامها لتخزين موسيقاك الخاصة والاستماع إليها عبر عدة عملاء.

## النشر (باستخدام Docker Compose)

أولاً، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # في حالة حدوث مشكلات في الأذونات، يمكنك محاولة النشر باستخدام الجذر (0:0)
    ports:
      - "${APP_PORT}:4533"
    environment:
      # اختياري: ضع خيارات تخصيص تكوينك هنا. أمثلة:
      ND_SCANSCHEDULE: 24h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
    volumes:
      - ${STACK_DIR}:/data
      - ${DATA_DIR}:/music:ro
    restart: unless-stopped
```

(اختياري) يُوصى بإنشاء ملف `.env` في نفس دليل `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا لم ترغب في استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `navidrome`).

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، مثل ./navidrome
DATA_DIR=xxx # حدد مسار تخزين الموسيقى الخاص بك، مثل ./music

# navidrome
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم بالفعل
```

إذا كان لديك NAS، يمكنك أيضًا تثبيت مساحة تخزين من NAS باستخدام بروتوكول NFS، وهذا يمكنك من تخزين الموسيقى على NAS لتوفير مساحة الخادم. لمزيد من التفاصيل، راجع [**كيفية تثبيت محرك الأقراص الصلبة من Synology NAS على نظام Linux باستخدام NFS**](https://www.navidrome.org/docs/installation/docker/) (يرجى استبدال النص في الرابط).

أخيرًا، قم بتشغيل الحاويات المكوّنة باستخدام الأمر `docker compose up -d` في نفس دليل `compose.yaml`.

## تعليمات التكوين

هناك العديد من خيارات التطبيقات المحمولة المتاحة. على Android، تجربتي الشخصية تظهر أن Substreamer هو أفضل تطبيق للاستخدام. لمزيد من الخيارات، يمكنك الرجوع إلى القائمة الرسمية [**التطبيقات**](https://www.navidrome.org/docs/overview/#apps).

## المراجعة والشكر

- [الموقع الرسمي](https://www.navidrome.org/)
- [الوثائق](https://www.navidrome.org/docs/installation/docker/)
- [مستودع GitHub](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [موقع العرض التوضيحي](https://demo.navidrome.org/app/) (اسم المستخدم وكلمة المرور هما demo)

Sure, here is the translated text in Arabic:

```
[يتم الاستبدال[1]]
[يتم الاستبدال[2]]
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.