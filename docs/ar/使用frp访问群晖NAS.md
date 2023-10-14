# استخدام frp للوصول إلى NAS من Synology

استخدام frp للوصول إلى NAS من Synology في أي شبكة.

## لماذا يجب استخدام frp للوصول إلى NAS من Synology

- لا يوجد عنوان IP العام
- خدمة QuickConnect بطيئة جدًا
- يتطلب Peanut Shell وغيرها من الخدمات شراء حركة المرور بشكل منفصل

## تكوين الخادم

انتقل إلى المقالة [**كيفية تحقيق التحكم عن بعد في RDP عبر الإنترنت (frp) · تكوين الخادم**](https://wiki-power.com/ar/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#%E6%9C%8D%E5%8A%A1%E7%AB%AF%E9%85%8D%E7%BD%AE). يجب الانتباه إلى أن المعلمات `vhost_http_port` / `vhost_https_port` في ملف التكوين `frpc.ini` يجب الاحتفاظ بها.

### ربط النطاق

- في تحليل النطاق ، أضف سجل A باستخدام عنوان IP للخادم
- في خادم السحابة ، قم بتكوين ربط النطاق

## تكوين NAS من Synology

### تحرير ملف التكوين

أنشئ ملف `frpc.ini` في أي مكان وأدخل المحتوى التالي:

```ini title="frpc.ini"
[common]
server_addr = عنوان IP للخادم
server_port = منفذ frp للخادم ، الافتراضي هو 7000
token = المفتاح السري ، يجب أن يكون مطابقًا لتكوين الخادم

[dsm-http]
type = tcp
local_ip = localhost
local_port = منفذ DSM http لـ Synology ، الافتراضي هو 5000
custom_domains = النطاق المرتبط
remote_port = منفذ عن بعد مخصص

[dsm-https]
type = tcp
local_ip = localhost
local_port = منفذ DSM https لـ Synology ، الافتراضي هو 5001
custom_domains = النطاق المرتبط
remote_port = منفذ عن بعد مخصص

[ssh]
type = tcp
local_ip = localhost
local_port = الافتراضي هو 22
custom_domains = النطاق المرتبط
remote_port = منفذ عن بعد مخصص
```

### استخدام طريقة Docker

في داخل Docker من Synology ، قم بتثبيت الصورة `stilleshan/frpc` واستخدم المعلمات التالية لتهيئة الحاوية:

- حدد "استخدام تنفيذ الحاوية بأذونات عالية"
- حدد "تمكين إعادة التشغيل التلقائي"
- في علامة التبويب "الحجم" ، أضف ملفًا واختر ملف `frpc.ini` المحلي ، ويجب أن يكون المسار المحمل `/frp/frpc.ini`
- حدد "استخدام نفس شبكة Docker Host"

قم بتشغيل الحاوية وانتظر قليلاً ، ثم يمكنك الوصول إلى DSM من Synology عبر النطاق + رقم المنفذ http.

## المراجع والشكر

- [دليل تثبيت وتكوين frpc للوصول إلى الشبكة الداخلية من Synology NAS باستخدام Docker](https://www.ioiox.com/archives/26.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.