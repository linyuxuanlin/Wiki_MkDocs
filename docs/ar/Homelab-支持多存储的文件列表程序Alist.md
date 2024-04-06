````markdown
# الوسط المحلي - برنامج قائمة الملفات Alist الذي يدعم التخزين المتعدد

![صورة](https://media.wiki-power.com/img/202304141808001.png)

**Alist** هو برنامج قائمة الملفات الذي يدعم أنواعًا متعددة من التخزين مثل التخزين المحلي وسحابة Alibaba وOneDrive وGoogleDrive وBaidu وKuaipan وLanzou وS3 وFTP / SFTP، مزود بمشغل فيديو عبر الإنترنت ومعاينة ملفات متنوعة (متوافق مع Office وPDF وMarkdown وغيرها)، بالإضافة إلى وظيفة التنزيل الغير متصل.

## النشر (Docker Compose)

أولاً، قم بإنشاء ملف `compose.yaml` وألصق فيه المحتوى التالي:

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
    environment: # يجب تشغيله بصلاحيات root، وإلا لن تكون قادرًا على الوصول إلى المجلدات الأخرى داخل حاويات Docker أو مجلد الجذر على الخادم المضيف
      - PUID=0
      - PGID=0
      - UMASK=022
    restart: always
```
````

(اختياري) يُوصى بإنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك فيه. إذا كنت لا ترغب في استخدام متغيرات البيئة، فيمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدل `${STACK_NAME}` بـ `alist`).

```dotenv title=".env"
STACK_NAME=alist
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، مثل ./alist

# alist
APP_VERSION=latest
APP_PORT=xxxx # حدد منفذ الوصول الخاص بك، اختر منفذ غير مستخدم مسبقًا
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس المجلد الذي يحتوي على ملف `compose.yaml` لبدء تشغيل الحاويات الخاصة بك.

## توضيحات حول التكوين

طرق الانضمام إلى مختلف أنواع التخزين موضحة بشكل مفصل في الوثائق الرسمية. كل ما عليك فعله هو اتباع التكوين الذي تم وصفه خطوة بخطوة.

## المراجع والشكر

- [الموقع الرسمي](https://alist.nn.ci/)
- [الوثائق](https://alist.nn.ci/guide/install/docker.html#release-version)
- [مستودع GitHub](https://github.com/alist-org/alist)
- [مستودع Docker Hub](https://hub.docker.com/r/xhofe/alist)
- [موقع العرض التجريبي](https://al.nn.ci/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
