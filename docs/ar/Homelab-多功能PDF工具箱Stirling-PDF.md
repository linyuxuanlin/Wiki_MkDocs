# Homelab - Stirling-PDF: مجموعة أدوات PDF متعددة الاستخدامات

![Stirling-PDF](https://media.wiki-power.com/img/20230410172939.png)

**Stirling-PDF** هو مجموعة أدوات PDF قابلة للتنفيذ ذاتية الاستضافة. تتضمن وظائف مثل تقسيم PDF، دمجه، تدويره، استخراج الصفحات، تحويل الصور، إعادة ترتيبه، إضافة / استخراج الصور، إضافة وإزالة كلمات المرور، تعيين الأذونات، إضافة العلامات المائية، تحويل ملفات أخرى إلى PDF، التعرف على النصوص بواسطة التعرف الضوئي على الأحرف (OCR)، تحرير البيانات الوصفية، ودعم وضع الظلام.

## النشر (Docker Compose)

أولاً، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

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

(اختياري) يُوصى بإنشاء ملف `.env` في نفس مجلد `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا لم تكن ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة داخل `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `s-pdf`).

```dotenv title=".env"
STACK_NAME=s-pdf
STACK_DIR=xxx # مسار تخزين المشروع المخصص، على سبيل المثال: ./s-pdf

# s-pdf
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس المجلد الذي يحتوي على `compose.yaml` لبدء تشغيل الحاويات المعدلة.

## المراجع والشكر

- [الوثائق / مستودع GitHub](https://github.com/Frooodle/Stirling-PDF)
- [مركز Docker](https://hub.docker.com/r/frooodle/s-pdf)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
