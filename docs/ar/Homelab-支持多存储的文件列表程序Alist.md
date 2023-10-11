# Homelab - برنامج Alist لقائمة الملفات المدعومة بالتخزين المتعدد

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304141808001.png)

**Alist** هو برنامج لقائمة الملفات يدعم العديد من طرق التخزين مثل المحلي وسحابة Alibaba و OneDrive و GoogleDrive و Baidu و KuaiPan و LanZou و S3 و FTP / SFTP وغيرها، ويحتوي على مشغل فيديو عبر الإنترنت ومعاينة ملفات مختلفة (متوافق مع Office و PDF و Markdown وغيرها)، بالإضافة إلى وظيفة التنزيل غير المتصل بالإنترنت.

## التنفيذ (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` ولصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.3"
services:
  alist:
    container_name: ${STACK_NAME}_app
    image: "xhofe/alist:${APP_VERSION}"
    volumes:
      - ${STACK_DIR}:/opt/alist/data
    ports:
      - ${APP_PORT}:5244
    environment: # يجب تشغيله بصلاحيات root، وإلا لن يتمكن من قراءة مجلدات Docker الأخرى أو مجلد root على المضيف
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مجلد `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية، يمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `alist`).

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # مسار تخزين المشروع المخصص، مثل ./alist

# alist
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر أي منفذ غير مستخدم
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس مجلد `compose.yaml` لتشغيل حاويات الترتيب.

## تفاصيل الإعداد

طرق الوصول إلى مختلف أنواع السحابات موضحة بشكل مفصل في الوثائق الرسمية.

## المراجع والشكر

- [الموقع الرسمي](https://alist.nn.ci/)
- [الوثائق](https://alist.nn.ci/guide/install/docker.html#release-version)
- [مستودع GitHub](https://github.com/alist-org/alist)
- [Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [موقع العرض التوضيحي](https://al.nn.ci/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
