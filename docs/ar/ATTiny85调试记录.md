# سجل تصحيح ATTiny85

## التشغيل

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Arduino كمبرمج ISP

|   Attiny    | Arduino |
| :---------: | :-----: |
| Pin 1 (PB5) |   D10   |
| Pin 4 (GND) |   GND   |
| Pin 5 (PB0) |   D11   |
| Pin 6 (PB1) |   D12   |
| Pin 7 (PB2) |   D13   |
| Pin 8 (VCC) |   5V    |

قم بتفليش Arduino كمبرمج ISP أولاً:

![](https://media.wiki-power.com/img/20200426144425.png)

افتح تفضيلات الـ IDE وقم بإضافة عنوان لوحة التطوير الإضافية:

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

ثم افتح مدير لوحات التطوير:

![](https://media.wiki-power.com/img/20200426144642.png)

ابحث وقم بتثبيت اللوحة (قد تحتاج إلى استخدام وسيط):

![](https://media.wiki-power.com/img/20200426144732.png)

عند تفليش الرقاقة، تأكد من اختيار نوع الرقاقة الصحيح وسرعة الساعة (Internal 16 MHz)، والمنفذ الذي توصل إليه Arduino. كما يجب اختيار "Arduino as ISP" كبرمج:

![](https://media.wiki-power.com/img/20200426144834.png)

## ختام

## المراجع والشكر

- [دليل صناعة نظام Digispark Arduino الأدنى بناءً على ATTiny85 (الجزء الأول)](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu--4)
- [دليل صناعة نظام Digispark Arduino الأدنى بناءً على ATTiny85 (الجزء الثاني)](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [ملاحظات حول استخدام لوحة تطوير Digispark USB (الجزء الأول): تعرّف على هذه اللوحة الصغيرة والمتعددة الوظائف والرخيصة المتوافقة مع Arduino](https://zhuanlan.zhihu.com/p/73336394)
- [الاتصال وبرمجة Digispark الخاص بك](http://digistump.com/wiki/digispark/tutorials/connecting)
- [حرق برنامج تشغيل Micronucleus لل Attiny85](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [صناعة جهاز ألعاب صغير بناءً على ATtiny85](https://www.jianshu.com/p/55e86b4e0194)
- [ملاحظات حول DigiSpark ATtiny85: برمجة AVR ISP بواسطة 8 دبابيس وبوتلوادر الذاكرة](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [مرجع سريع للمعلومات المطلوبة بشكل متكرر](http://digistump.com/wiki/digispark/quickref)

> المؤلف: **باور لين**
> الرابط الأصلي: <https://wiki-power.com>
> إشعار حقوق النشر: يُرجى الإشارة إلى المصدر عند إعادة النشر. ترخيص المقال: [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh).

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
