# Homelab - أداة مذكرات ملاحظات الحطام memos

![](https://f004.backblazeb2.com/file/wiki-media/img/202304111548420.png)

**memos** هي أداة مذكرات ملاحظات مفتوحة المصدر وذاتية الاستضافة. تدعم بناء الجمل Markdown والمشاركة العامة وتضمين iframe وإدارة العلامات وعرض التقويم ونقل البيانات والنسخ الاحتياطي البسيط.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3.0"
services:
  memos:
    container_name: ${STACK_NAME}_app
    image: neosmemo/memos:${APP_VERSION}
    ports:
      - ${APP_PORT}:5230
    volumes:
      - ${STACK_DIR}:/var/opt/memos
    restart: always
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص متغيرات البيئة الخاصة بك. إذا لم ترغب في استخدام المتغيرات البيئية ، يمكنك تخصيص المعلمات الخاصة بك مباشرة في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `memos`).

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # تخصيص منفذ الوصول الخاص بك ، اختر غير مستخدم فقط
```

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## توضيحات التكوين

تطبيق الجوال iOS / Android: [**Moe Memos**](https://memos.moe/) . هناك المزيد من العملاء الجانب الثالث (مثل برنامج WeChat Mini ، وامتداد المتصفح ، و Telegram Bot ، إلخ) ، يرجى الرجوع إلى وثائق [**contribution·memos**](https://github.com/usememos/memos#contribution) .

يمكن استخدام إضافة VS Code [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite) لتصدير واستيراد بيانات المستخدم ، وتنزيل وفتح `memos_prod.db` في `${DIR}` لإجراء عمليات الإضافة والحذف والتعديل والبحث والنسخ الاحتياطي والاستيراد. تنبيه ، سيتم تحديث ملف `memos_prod.db` فقط عند إغلاق / إعادة تشغيل حاويات Docker.

## المراجع والشكر

- [الموقع الرسمي](https://usememos.com/)
- [الوثائق](https://usememos.com/docs/install#docker-compose)
- [مستودع GitHub](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [موقع العرض التوضيحي](https://demo.usememos.com/)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.