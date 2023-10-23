# ملاحظات تكوين Ubuntu

## مشكلة الوقت في نظامين مزدوجين

بعد تثبيت نظامين مزدوجين، قد تواجه مشكلة في الوقت (عدم تزامن الوقت بين Windows و Ubuntu). يمكن حلها باستخدام الأمر التالي:

```shell
timedatectl set-local-rtc 1 --adjust-system-clock
```

## تثبيت البرامج

1. Chrome
2. VS Code
3. [**Qv2ray**](https://qv2ray.net/)
4. Git
   - `sudo apt install git`
   - `git config --global user.name "John Doe"`
   - `git config --global user.email johndoe@example.com`

## النصائح

### عرض الملفات المخفية

استخدم الاختصار: `Ctrl` + `H`

### فتح الطرفية

استخدم الاختصار: `Ctrl` + `Alt` + `T`

### الأوامر

ملاحظة: `<xx>` تشير إلى إلزامي، `(xx)` تشير إلى اختياري

- cd
  - التنقل إلى مجلد العمل
  - `cd <مسار المجلد>`
- pwd
  - عرض المسار المطلق الحالي
  - `pwd`
- mkdir
  - إنشاء مجلد
  - `mkdir (الخيارات) <اسم المجلد>`
- ls
  - عرض محتويات المجلد
  - `ls (الخيارات) (اسم المجلد)`
- touch
  - تغيير وقت الملف أو المجلد
  - `touch (الخيارات) <اسم الملف>`
- mv
  - نقل
  - `mv (الخيارات) (الملف/المجلد المصدر) <الملف/المجلد الهدف>`
- cp
  - نسخ
  - `cp (الخيارات) (اسم الملف/اسم المجلد المصدر) <اسم الملف/اسم المجلد الهدف>`
- rm
  - حذف
  - `rm (الخيارات) <اسم الملف/اسم المجلد>`

## المراجع والشكر

- [دليل تثبيت ROS](https://mp.weixin.qq.com/s?__biz=MzU4Mzc1NDA5Mw==&mid=2247486645&idx=1&sn=8ba442af57060b4d608d4c24d4307921&chksm=fda504b7cad28da11a2dd782b60dce466d53ad8e260f161b1e47f24423cc1e9f9aabc486c7f3&mpshare=1&scene=1&srcid=1125YhpxcX5as5se6rsek2IS&sharer_sharetime=1606233866320&sharer_shareid=57baeb2b96d0cff9b17ac2c15b36602b&key=a402d93e91746f46ae3228f3f1014e2c74a235c331168642475573a82dabce23902b3593a2a240439e9e37cd9b2ceaeab2b3b2130d952ee61260b30c6cad24ab3f1907dd57abfae9934d0c9487ddc4364b41261c6fb7277d94de784fa9718f9f60712a15b25f505ab7105346330f16f4b659970a5143e8aa882da96dc76c0100&ascene=1&uin=MTk5MDUwOTA4Mg%3D%3D&devicetype=Windows+10+x64&version=6300002f&lang=zh_CN&exportkey=A0ZOktA1B68GOdT4vmLQPxA%3D&pass_ticket=b2tffRx7FG4vxDxfZxW7b9rGQf%2FK8YGbZtslM9VWUgnItoiwUPJYOD8ciwJbwx%2BC&wx_header=0)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.