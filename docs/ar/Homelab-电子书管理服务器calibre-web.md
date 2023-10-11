# Homelab - خادم إدارة الكتب الإلكترونية calibre-web

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210429125418.png)

**calibre-web** هو حل شامل للكتب الإلكترونية ، يعتمد على Calibre ، ويمكن قراءة الكتب الإلكترونية على الويب ، ويتضمن خدمة calibre-server ، ويحتوي أيضًا على تحويل تنسيق الكتب الإلكترونية.

## النشر (Docker Compose)

أولاً ، قم بإنشاء ملف `compose.yaml` والصق المحتوى التالي:

```yaml title="compose.yaml"
version: "3"
services:
  calibre-web:
    container_name: ${STACK_NAME}_app
    image: johngong/calibre-web:${APP_VERSION}
    ports:
      - ${APP_PORT_WEB}:8083
      - ${APP_PORT_SERVER}:8080
    volumes:
      - ${STACK_DIR}:/config
      - ${DATA_DIR}:/library
      - ${DATA_DIR}/autoaddbooks:/autoaddbooks
    restart: unless-stopped
```

(اختياري) يوصى بإنشاء ملف `.env` في نفس مستوى `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك. إذا كنت لا تريد استخدام المتغيرات البيئية ، يمكنك أيضًا تخصيص المعلمات الخاصة بك مباشرةً في `compose.yaml` (على سبيل المثال ، استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # مسار تخزين المشروع المخصص ، على سبيل المثال ./calibre-web
DATA_DIR=xxx # مسار تخزين الكتب المخصص ، على سبيل المثال ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # تخصيص منفذ واجهة المستخدم الرسومية للويب ، فقط اختر منفذًا غير مستخدم
APP_PORT_SERVER=xxxx # تخصيص منفذ calibre-server ، فقط اختر منفذًا غير مستخدم
```

إذا كان لديك NAS ، يمكنك أيضًا تثبيت مساحة التخزين على NAS باستخدام بروتوكول NFS ، وتخزين الكتب على NAS لتوفير مساحة الخادم ، يرجى الرجوع إلى [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/ar/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) للحصول على التفاصيل.

أخيرًا ، قم بتشغيل الأمر `docker compose up -d` في نفس مستوى `compose.yaml` لتشغيل حاويات الترتيب.

## تعليمات التكوين

الحساب الافتراضي هو `admin` وكلمة المرور هي `admin123`.

### وظيفة تحميل الكتب

النظام لا يحتوي على وظيفة تحميل الكتب بشكل افتراضي ، يجب النقر على "أذونات الإدارة" - "تحرير التكوين الأساسي" - "تمكين التحميل" على التوالي لتمكين وظيفة تحميل الكتب.

### الاستخدام على الهواتف المحمولة

يمكن استخدام Librera على Android ، والاتصال بـ calibre-web عبر بروتوكول OPDS. يتم إضافة عنوان url للمكتبة عن طريق إضافة `/opds` في نهاية العنوان الأصلي ، على سبيل المثال `calibre.xxx.com/opds`.

### نسيت كلمة المرور

إذا نسيت كلمة المرور ، يمكن تنزيل قاعدة بيانات `app.db` من `calibre-web` واستخدام SQLite لعرض البرنامج (أو أدوات عبر الإنترنت مثل [**Sqlite Viewer | Modifier**](https://www.lzltool.com/sqlite-viewer)) وتنفيذ العبارات التالية على التوالي:

```sql
SELECT * FROM 'user' LIMIT 0,30 --يمكن أيضًا التبديل يدويًا إلى الجدول المسمى user
```

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- يجب تغيير xxx إلى اسم المستخدم الحالي الخاص بك
```

استبدل ملف `app.db` المعدل بالأصلي، ثم قم بتسجيل الدخول باستخدام كلمة المرور الجديدة `hello`.

## المراجع والشكر

- [مستودع GitHub](https://github.com/janeczku/calibre-web)
- [مستودع Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
