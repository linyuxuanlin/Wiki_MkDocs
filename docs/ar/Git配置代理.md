# تكوين الوكيل لـ Git

## مصدر المشكلة

سرعة `git clone` و `git pull` في الصين بطيئة للغاية.

## الحلول

### 1. إعداد الوكيل داخل برنامج الوكيل

1. في برنامج الوكيل، حدد "السماح بالاتصالات من الشبكة المحلية".
2. اكتب رقم المنفذ (مثال: 1080).
3. قم بتمكين "الوضع العام".

### 2. تكوين الوكيل HTTP على Git على مستوى عالمي

```shell
git config --global http.proxy http://127.0.0.1:【المنفذ】
git config --global https.proxy https://127.0.0.1:【المنفذ】

# مثال:
git config --global http.proxy http://127.0.0.1:10808
git config --global https.proxy https://127.0.0.1:10808

# إذا لم يكن ذلك فعالًا، جرب استخدام منفذ socks5:
git config --global http.proxy socks5://127.0.0.1:【المنفذ】
git config --global https.proxy socks5://127.0.0.1:【المنفذ】

# إذا كنت ترغب في استخدام الوكيل فقط لـ GitHub وعدم التأثير على المستودعات المحلية (غير موصى به إذا كنت غير ملم بملفات التكوين):
git config --global http.https://github.com.proxy https://127.0.0.1:【المنفذ】
git config --global https.https://github.com.proxy https://127.0.0.1:【المنفذ】

# استخدم الوكيل فقط لـ GitLab وعدم التأثير على المستودعات المحلية (غير موصى به إذا كنت غير ملم بملفات التكوين):
git config --global https.https://https://gitlab.com.proxy https://127.0.0.1:1080
```

للتكوين على نظام Ubuntu:

```shell
git config --global http.https://github.com.proxy socks5://127.0.0.1:10808
```

### عرض مسار ملف التكوين

```
git config --list --show-origin
```

### استعادة الإعدادات الافتراضية

إذا كنت لا ترغب في استخدام الوكيل، يمكنك استخدام الأمر التالي لاستعادة الإعدادات الافتراضية:

```shell
git config --global --unset http.proxy
git config --global --unset https.proxy
```

## المراجع والشكر

- [**تغلب على بطء git clone و git pull**](https://c.lanmit.com/czxt/Linux/16965.html)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.