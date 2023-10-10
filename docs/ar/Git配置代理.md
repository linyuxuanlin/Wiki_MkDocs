# تكوين الوكيل لـ Git

## مصدر المشكلة

بطء سرعة `git clone` و `git pull` في الصين.

## الحل

### 1. تكوين الوكيل في البرنامج المساند

1. تحقق من تحديد "السماح بالاتصالات من الشبكة المحلية".
2. اكتب رقم المنفذ (على سبيل المثال: 1080).
3. تفعيل "الوضع العالمي".

### 2. تكوين الوكيل العالمي لـ Git

```shell
git config --global http.proxy http://127.0.0.1:【端口号】
git config --global https.proxy https://127.0.0.1:【端口号】

# مثال:
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# إذا لم يعمل الأمر أعلاه، جرب استخدام منفذ socks5:
git config --global http.proxy socks5://127.0.0.1:【端口号】
git config --global https.proxy socks5://127.0.0.1:【端口号】

# إذا كنت تريد استخدام الوكيل فقط لـ GitHub ولا تؤثر على المستودعات المحلية (لا يوصى باستخدام المستخدمين الجدد):
git config --global http.https://github.com.proxy https://127.0.0.1:【端口号】
git config --global https.https://github.com.proxy https://127.0.0.1:【端口号】

# إذا كنت تريد استخدام الوكيل فقط لـ GitLab ولا تؤثر على المستودعات المحلية (لا يوصى باستخدام المستخدمين الجدد):
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

تكوين Ubuntu:

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### عرض مسار ملف التكوين

```
git config –list –show-origin
```

### استعادة

إذا كنت لا تريد استخدام الوكيل، يمكنك استخدام الطريقة التالية لاستعادة الإعدادات الافتراضية:

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## المراجع والشكر

- [**التغلب على بطء git clone و git pull**](https://c.lanmit.com/czxt/Linux/16965.html)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.