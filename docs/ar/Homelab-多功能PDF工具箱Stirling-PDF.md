# Homelab - صندوق أدوات PDF متعدد الوظائف Stirling-PDF

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410172939.png)

**Stirling-PDF** هو حزمة أدوات PDF ذاتية الاستضافة، تتضمن وظائف مثل تقسيم ودمج وتدوير واستخراج الصفحات وتحويل الصور وإعادة الترتيب وإضافة / استخراج الصور وإضافة وحذف كلمات المرور وتعيين الأذونات وإضافة العلامات المائية وتحويل الملفات الأخرى إلى PDF وتعرفة النصوص الضوئية وتحرير البيانات الوصفية، ويدعم الوضع الليلي.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.3"
services:
  s-pdf:
    container_name: ${STACK_NAME}_app
    image: frooodle/s-pdf:${APP_VERSION}
    ports:
      - ${APP_PORT}:8080
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `s-pdf`).

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، فقط اختر غير مستخدم
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## المراجع والشكر

- [المستندات / مستودع GitHub](https://github.com/Frooodle/Stirling-PDF)
- [Docker Hub](https://hub.docker.com/r/frooodle/s-pdf)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
