# الوصول إلى NAS Synology باستخدام frp

الوصول إلى NAS Synology باستخدام frp في أي شبكة.

## لماذا نستخدم frp للوصول إلى NAS Synology

- لا يوجد لديك عنوان IP عام
- خدمة QuickConnect بطيئة جداً
- خدمات مثل خدمة Peanut Shell تتطلب شراء حزم ترافيك منفصلة

## إعداد الخادم

يرجى الانتقال إلى المقالة [**كيفية تكوين الخادم البعيد (frp) للوصول إلى نظام التحكم عن بعد RDP عبر الإنترنت**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE). يجب أن تلاحظ أنه يجب الاحتفاظ بمعلمات `vhost_http_port` / `vhost_https_port` في ملف التكوين `frpc.ini`.

### ربط اسم النطاق

- في خدمة تحليل النطاق، قم بإضافة سجل A باستخدام عنوان الخادم
- قم بتكوين ربط النطاق في خادم السحاب

## إعداد NAS Synology

### تحرير ملف التكوين

أنشئ ملف `frpc.ini` في أي مكان وقم بإضافة المحتوى التالي:

```ini title="frpc.ini"
[common]
server_addr = عنوان الخادم
server_port = منفذ خادم frp، الافتراضي 7000
token = المفتاح، يجب أن يتطابق مع الإعدادات على الخادم

[dsm-http]
type = tcp
local_ip = localhost
local_port = منفذ DSM للوصول عبر HTTP في Synology، الافتراضي 5000
custom_domains = النطاق المرتبط
remote_port = منفذ بعيد مخصص

[dsm-https]
type = tcp
local_ip = localhost
local_port = منفذ DSM للوصول عبر HTTPS في Synology، الافتراضي 5001
custom_domains = النطاق المرتبط
remote_port = منفذ بعيد مخصص

[ssh]
type = tcp
local_ip = localhost
local_port = الافتراضي 22
custom_domains = النطاق المرتبط
remote_port = منفذ بعيد مخصص
```

### الاستخدام بواسطة الطريقة التي تعتمد على Docker

قم بتثبيت صورة `stilleshan/frpc` داخل بيئة Docker على Synology واستخدم الإعدادات التالية:

- حدد "استخدام صلاحيات عالية لتشغيل الحاوية"
- حدد "تمكين إعادة التشغيل التلقائي"
- في علامة التبويب "الحجرة"، أضف ملفًا واختر ملف `frpc.ini` المحلي، وحدد المسار المستهدف كـ `/frp/frpc.ini`
- حدد "استخدام نفس شبكة مضيف Docker"

قم بتشغيل الحاوية وانتظر لحظة واحدة، ستكون قادرًا على الوصول إلى DSM Synology عبر النطاق ومنفذ HTTP.

## المراجع والشكر

- [دليل تثبيت وتكوين frpc لاختراق الشبكة المحلية على NAS Synology باستخدام Docker](https://www.ioiox.com/archives/26.html)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.