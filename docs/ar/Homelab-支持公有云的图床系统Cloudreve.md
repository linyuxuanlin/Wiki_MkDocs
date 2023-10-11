# Homelab - نظام Cloudreve لدعم الخدمات السحابية العامة للصور

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195423.png)

**Cloudreve** هو نظام ملفات سحابي يدعم العديد من محركات التخزين السحابية العامة، ويدعم استخدام الأجهزة المحلية والفرعية والسحابية العامة مثل Qiniu و Alibaba Cloud OSS و Tencent Cloud COS و Upyun و OneDrive و S3 كنهاية تخزين، ويمكنه الاتصال بـ Aria2 للتنزيل الغير متصل بالإنترنت، ويدعم العديد من المستخدمين والتحميل بالسحب والإفلات والإدارة، والمعاينة والتحرير عبر الإنترنت، و WebDAV وغيرها. وهو يستخدم عادة كمخزن للصور الشخصية أو إدارة ملفات السحابة.

## التنصيب (Docker Compose)

أولاً، نحتاج إلى إنشاء هيكل المجلدات. قم بالتبديل إلى المجلد الذي يحتوي على Cloudreve (مثال: `/DATA/AppData/cloudreve`) وقم بتنفيذ الأمر التالي:

```shell
mkdir -vp cloudreve/{uploads,avatar,data} \
&& touch cloudreve/conf.ini \
&& touch cloudreve/cloudreve.db \
&& mkdir -p aria2/config \
&& mkdir -p cloudreve/data/aria2 \
&& chmod -R 777 cloudreve/data/aria2 \
&& mkdir data
```

أولاً، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.8"
services:
  cloudreve:
    container_name: ${STACK_NAME}_app
    image: cloudreve/cloudreve:${APP_VERSION}
    ports:
      - "${APP_PORT}:5212"
    volumes:
      - temp_data:/data
      - ${STACK_DIR}/cloudreve/uploads:/cloudreve/uploads
      - ${STACK_DIR}/cloudreve/conf.ini:/cloudreve/conf.ini
      - ${STACK_DIR}/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - ${STACK_DIR}/cloudreve/avatar:/cloudreve/avatar
    restart: unless-stopped
    depends_on:
      - aria2
  aria2:
    container_name: ${STACK_NAME}_aria2
    image: p3terx/aria2-pro:${ARIA2_VERSION}
    volumes:
      - ${STACK_DIR}/aria2/config:/config
      - ${STACK_DIR}/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
    environment:
      - RPC_SECRET=${ARIA2_RPC_SECRET}
      - RPC_PORT=${ARIA2_RPC_PORT}
    restart: unless-stopped
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/temp_data
      o: bind
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مجلد `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `cloudreve`).

```dotenv title=".env"
STACK_NAME=cloudreve
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./cloudreve

# cloudreve
APP_VERSION=latest
APP_PORT=xxxx # منفذ الوصول المخصص ، اختر غير المستخدمة فقط

# aria2
ARIA2_VERSION=latest
ARIA2_RPC_SECRET=xxx # كلمة مرور ARIA2
ARIA2_RPC_PORT=6800
```

أخيرًا ، يمكن تشغيل حاويات الترتيب باستخدام الأمر `docker compose up -d` في نفس دليل `compose.yaml`.

## تعليمات التكوين

عند التشغيل لأول مرة ، سيتم إنشاء حساب المسؤول الأولي تلقائيًا ، ويمكن العثور عليه في السجل. إذا فاتتك ، فيرجى حذف cloudreve.db في الدليل وإعادة تشغيل البرنامج الرئيسي لتهيئة حساب المسؤول الجديد.

أنا استخدمت قاعدة تسمية الصور التالية: `{year}{month}{day}{hour}{minute}{second}{ext}`.

## المراجع والشكر

- [الموقع الرسمي](https://docs.cloudreve.org/)
- [الوثائق](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [المنتدى](https://forum.cloudreve.org/)
- [مستودع GitHub](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [موقع العرض التوضيحي](https://demo.cloudreve.org/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
