# Homelab - خادم وسائط الفيديو Jellyfin

![](https://f004.backblazeb2.com/file/wiki-media/img/20230531213856.png)

**Jellyfin** هو خادم وسائط الفيديو والتدفق المفتوح المصدر ، ويمكن استخدامه لإدارة الأفلام والبرامج التلفزيونية ومشاهدتها على أجهزة مختلفة. يمكن استخدامه كبديل للبرامج الخاصة Emby و Plex.

## نشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

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
    # Optional - alternative address used for autodiscovery
    #environment:
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # Optional - may be necessary for docker healthcheck to pass if running in host network mode
    #extra_hosts:
    #  - "host.docker.internal:host-gateway"
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `jellyfin`).

```dotenv title=".env"
STACK_NAME=jellyfin
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./jellyfin
DATA_DIR=xxx # مسار تخزين الفيديو المخصص ، على سبيل المثال ./video

# jellyfin
APP_VERSION=latest
APP_PORT=xxxx # منفذ الوصول المخصص ، اختر غير مستخدم فقط
```

إذا كان لديك NAS ، فيمكنك أيضًا تثبيت مساحة التخزين على NAS باستخدام بروتوكول NFS ، وتخزين الموسيقى على NAS لتوفير مساحة الخادم ، يرجى الرجوع إلى [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/ar/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) للحصول على التفاصيل.

أخيرًا ، يمكنك تشغيل حاويات الترتيب باستخدام الأمر `docker compose up -d` في نفس مستوى `compose.yaml`.

## شرح التكوين

يمكن استخدام تطبيق Jellyfin الرسمي على الهواتف المحمولة.

## المراجع والشكر

- [الموقع الرسمي](https://jellyfin.org/)
- [الوثائق](https://jellyfin.org/docs/general/installation/container#using-docker-compose)
- [مستودع GitHub](https://github.com/jellyfin/jellyfin)
- [Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin)
- [موقع العرض التوضيحي](https://demo.jellyfin.org/stable)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.