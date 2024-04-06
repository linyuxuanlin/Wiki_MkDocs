# Homelab - إدارة خادم الكتب الإلكترونية calibre-web

![](https://media.wiki-power.com/img/20210429125418.png)

**calibre-web** هو حلاً شاملاً للكتب الإلكترونية، وهو مبني على Calibre، ويتيح قراءة الكتب الإلكترونية عبر الويب، ويدمج خدمة calibre-server وأداة تحويل الكتب الإلكترونية.

## النشر (Docker Compose)

قم أولاً بإنشاء ملف `compose.yaml` والصق فيه المحتوى التالي:

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

(اختياري) يُفضل إنشاء ملف `.env` في نفس الدليل الذي يحتوي على ملف `compose.yaml` وقم بتخصيص المتغيرات البيئية الخاصة بك. إذا لم تكن ترغب في استخدام المتغيرات البيئية، يمكنك أيضًا تخصيص المعلمات مباشرة في ملف `compose.yaml` (مثل استبدال `${STACK_NAME}` بـ `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=calibre-web
STACK_DIR=xxx # قم بتخصيص مسار تخزين المشروع الخاص بك، مثل ./calibre-web
DATA_DIR=xxx # قم بتخصيص مسار تخزين المكتبة الخاص بك، مثل ./book

# calibre-web
APP_VERSION=latest
APP_PORT_WEB=xxxx # قم بتخصيص منفذ واجهة المستخدم الويب الخاص بك، اختر منفذًا غير مستخدم بالفعل
APP_PORT_SERVER=xxxx # قم بتخصيص منفذ الوصول إلى خادم calibre-server الخاص بك، اختر منفذًا غير مستخدم بالفعل
```

إذا كان لديك جهاز تخزين NAS، يمكنك أيضًا ربطه بالخادم باستخدام بروتوكول NFS لتوفير مساحة تخزين الكتب وتوفير مساحة الخادم. لمزيد من التفاصيل، يُرجى الرجوع إلى [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

أخيرًا، يمكنك تشغيل الحاويات بنجاح بتنفيذ الأمر `docker compose up -d` في نفس الدليل الذي يحتوي على ملف `compose.yaml`.

## تعليمات التكوين

اسم المستخدم وكلمة المرور الافتراضية هما `admin` و`admin123`.

### وظيفة تحميل الكتب

بشكل افتراضي، لا تكون وظيفة تحميل الكتب ممكنة. يجب النقر على الحق في الزاوية العليا اليمنى ومن ثم `مجلد التحكم` - `تحرير الإعدادات الأساسية` - `تمكين التحميل` لتمكين وظيفة تحميل الكتب.

### الاستخدام على الأجهزة المحمولة

يمكن استخدام تطبيق Librera على نظام Android، حيث يمكنك الاتصال بـ calibre-web من خلال بروتوكول OPDS. قم بإضافة عنوان URL الخاص بالمكتبة عبر إضافة `/opds` إلى العنوان الأصلي، مثل `calibre.xxx.com/opds`.

### نسيت كلمة المرور

إذا نسيت كلمة المرور، يمكنك تنزيل قاعدة البيانات `app.db` من داخل تطبيق `calibre-web` واستخدام مستعرض SQLite لعرضه (أو استخدام أداة عبر الإنترنت مثل [**Sqlite 查看器 | 修改器**](https://www.lzltool.com/sqlite-viewer))، ثم قم بتنفيذ الاستعلامات التالية:

```sql
SELECT * FROM 'user' LIMIT 0,30 -- يمكن أيضًا التبديل يدويًا إلى الجدول المسمى "user"
```

```sql
UPDATE user SET password='pbkdf2:sha256:150000$ODedbYPS$4d1bd12adb1eb63f78e49873cbfc731e35af178cb9eb6b8b62c09dcf8db76670' WHERE name='xxx'; -- Please replace 'xxx' with your current username

Replace the modified `app.db` with the original one, and then log in using the new password 'hello'.

## References and Acknowledgments

- [GitHub repo](https://github.com/janeczku/calibre-web)
- [Docker Hub](https://registry.hub.docker.com/r/johngong/calibre-web)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
