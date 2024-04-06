````markdown
# Homelab - أداة مذكرات الـ Homelab

![](https://media.wiki-power.com/img/202304111548420.png)

**memos** هو أداة مذكرات مفتوحة المصدر قابلة للاستضافة ذات العديد من الميزات. يدعم تنسيق Markdown، مشاركة عامة، تضمين iframe، إدارة العلامات، عرض التقويم، وإمكانية نقل البيانات والنسخ الاحتياطي البسيط.

## النشر باستخدام Docker Compose

أولاً، أنشئ ملف `compose.yaml` والصق المحتوى التالي:

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
````

(اختياري) يُفضل إنشاء ملف `.env` في نفس مجلد `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة في ملف `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `memos`).

```dotenv title=".env"
STACK_NAME=memos
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، مثل ./memos

# memos
APP_VERSION=latest
APP_PORT=xxxx # قم بتخصيص منفذ الوصول الخاص بك، اختر منفذًا غير مستخدم
```

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس مجلد `compose.yaml` لبدء تشغيل الحاويات.

## توجيهات الإعداد

للوصول من الهواتف الذكية iOS/Android، يمكنك استخدام تطبيق [**Moe Memos**](https://memos.moe/)، وهناك المزيد من العملاء من جهات خارجية (مثل تطبيق WeChat Mini، إضافة متصفح، وتليغرام بوت)، يُرجى الرجوع إلى وثائق [**contribution·memos**](https://github.com/usememos/memos#contribution).

بالنسبة لاستيراد وتصدير بيانات المستخدم، يمكنك استخدام إضافة VS Code [**SQLite**](https://marketplace.visualstudio.com/items?itemName=alexcvzz.vscode-sqlite). قم بتنزيل الملف `memos_prod.db` في المجلد `${DIR}` وافتحه لإجراء الإضافة والحذف والتحديث وعمليات الاستيراد والتصدير والنسخ الاحتياطي. يُرجى ملاحظة أنه سيتم تحديث ملف `memos_prod.db` فقط عند إيقاف الحاوية Docker أو إعادة تشغيلها.

## المراجع والشكر

- [الموقع الرسمي](https://usememos.com/)
- [الوثائق](https://usememos.com/docs/install#docker-compose)
- [مستودع GitHub](https://github.com/usememos/memos)
- [مستودع Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [موقع العرض التوضيحي](https://demo.usememos.com/)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
