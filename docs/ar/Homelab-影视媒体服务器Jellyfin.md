# هوملاب - خادم وسائط الفيديو والأفلام Jellyfin

![صورة](https://media.wiki-power.com/img/20230531213856.png)

**Jellyfin** هو خادم وسائط مفتوح المصدر يستخدم لإدارة الأفلام والبرامج التلفزيونية ومشاهدتها على أجهزة متعددة. يُعتبر بديلاً للبرامج الخاصة Emby وPlex.

## النشر (Docker Compose)

أولاً، أنشئ ملف "compose.yaml" والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.5"
services:
  jellyfin:
    container_name: ${STACK_NAME}_app
    image: jellyfin/jellyfin:${APP_VERSION}
    #user: uid:gid
    #network_mode: 'host'
    ports:
      - ${APP_PORT}:8096
    volumes:
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/cache:/cache
      - ${DATA_DIR}:/media
    restart: "unless-stopped"
    # اختياري - عنوان بديل يُستخدم للعثور التلقائي
    #environment:
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # اختياري - قد يكون ضروريًا لاجتياز فحص صحة Docker إذا تم التشغيل في وضع الشبكة المضيفة
    #extra_hosts:
    #  - "host.docker.internal:host-gateway"
```

(اختياري) يُفضل إنشاء ملف ".env" في نفس الدليل الرئيسي الذي يحتوي على ملف "compose.yaml" وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة في "compose.yaml" (مثل استبدال "${STACK_NAME}" بـ "jellyfin").

```dotenv title=".env"
STACK_NAME=jellyfin
STACK_DIR=xxx # مسار تخزين المشروع المخصص، على سبيل المثال: ./jellyfin
DATA_DIR=xxx # مسار تخزين الفيديو المخصص، على سبيل المثال: ./video

# jellyfin
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم بالفعل
```

إذا كنت تمتلك NAS، يمكنك أيضًا استخدام بروتوكول NFS لربط مساحة التخزين على NAS وتخزين الموسيقى على NAS لتوفير مساحة الخادم. لمزيد من التفاصيل، يُرجى الرجوع إلى [**ربط أقراص الـ NAS من سينولوجي على نظام لينكس (NFS)**](https://wiki-power.com/ar/(https://example.com).

أخيرًا، يمكنك تشغيل الحاويات المُنسقة بتنفيذ الأمر "docker compose up -d" في الدليل الذي يحتوي على ملف "compose.yaml".

## توجيهات التكوين

يمكنك استخدام تطبيق Jellyfin الرسمي المتاح لأجهزة الجوال.

## المراجع والشكر

- [الموقع الرسمي](https://jellyfin.org/)
- [الوثائق](https://jellyfin.org/docs/general/installation/container#using-docker-compose)
- [مستودع GitHub](https://github.com/jellyfin/jellyfin)
- [مستودع Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin)
- [موقع العرض التوضيحي](https://demo.jellyfin.org/stable)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
