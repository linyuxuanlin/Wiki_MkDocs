# هوملاب - خادم إدارة الكتب الإلكترونية calibre-web

![](https://img.wiki-power.com/d/wiki-media/img/20210429125418.png)

**calibre-web** هو حلاً شاملاً للكتب الإلكترونية، يستند إلى Calibre ويتيح قراءة الكتب الإلكترونية عبر الويب. يتميز بخدمة calibre-server المدمجة وأداة تحويل تنسيقات الكتب الإلكترونية.

## النشر (Docker Compose)

أولاً، أنشئ ملف `compose.yaml` وقم بلصق المحتوى التالي:

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

(اختياري) يُفضل إنشاء ملف `.env` في نفس مستوى ملف `compose.yaml` وتخصيص المتغيرات البيئية الخاصة بك فيه. إذا كنت لا ترغب في استخدام المتغيرات البيئية، يمكنك أيضاً تخصيص المعلمات مباشرة في ملف `compose.yaml` (على سبيل المثال، استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # حدد مسار تخزين المشروع الخاص بك، على سبيل المثال، ./calibre-web
DATA_DIR=xxx # حدد مسار تخزين الكتب الخاص بك، على سبيل المثال، ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # حدد منفذ واجهة المستخدم عبر الويب الخاص بك، اختر منفذ غير مستخدم بالفعل
APP_PORT_SERVER=xxxx # حدد منفذ الوصول إلى calibre-server الخاص بك، اختر منفذ غير مستخدم بالفعل
```

إذا كان لديك NAS، يمكنك أيضًا توصيل مساحة التخزين على NAS باستخدام بروتوكول NFS. يمكنك تخزين الكتب الصوتية على NAS لتوفير مساحة الخادم. لمزيد من التفاصيل، يُرجى الرجوع إلى [**توسيع مساحة القرص الصلب NAS من Synology على نظام Linux (NFS)**](https://to_be_replace[3]Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9C%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) للمزيد من المعلومات.

أخيرًا، قم بتنفيذ الأمر `docker compose up -d` في نفس دليل ملف `compose.yaml` لبدء تشغيل الحاويات المكونة.

## توضيحات التكوين

اسم المستخدم الافتراضي هو `admin`، وكلمة المرور هي `admin123`.

### وظيفة تحميل الكتب

النظام ليس لديه وظيفة تحميل الكتب افتراضيًا، يجب النقر على "صلاحيات الإدارة" في الزاوية العلوية اليمنى ثم "تحرير الإعدادات الأساسية" وتمكين خيار "تمكين التحميل" لتمكين وظيفة تحميل الكتب.

### الاستخدام على الأجهزة المحمولة

يمكن استخدامه على نظام Android باستخدام تطبيق Librera والاتصال بـ calibre-web عبر بروتوكول OPDS. يجب إضافة عنوان URL لمكتبة الكتب الإلكترونية عبر إضافة "/opds" إلى عنوان URL الأصلي، على سبيل المثال: `calibre.xxx.com/opds`.

### نسيت كلمة المرور

إذا نسيت كلمة المرور، يمكنك تنزيل قاعدة بيانات `app.db` من `calibre-web` واستخدام مشاهد SQLite لعرض البيانات (أو استخدام أدوات مشاهدة SQLite عبر الإنترنت مثل [**Sqlite Viewer | Modifier**](https://www.lzltool.com/sqlite-viewer))، ثم تنفيذ الاستعلامات التالية:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- يمكن أيضًا التبديل يدويًا إلى الجدول الذي يسمى "user"
``

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- Replace 'xxx' with your current username

Replace the modified `app.db` with the original one, and then log in using the new password 'hello'.

## References and Acknowledgments

- [GitHub repository](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```


> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.