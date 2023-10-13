# سجل تصحيح ATTiny85

## برنامج التمهيد

```shell
P:\Arduino\hardware\tools\avr/bin/avrdude -C "P:\Arduino\hardware\tools\avr/etc/avrdude.conf" -v -pattiny85 -carduino -PCOM4 -b119200 -Uflash:w:D:\t85_default.hex:i -U lfuse:w:0xE1:m -U hfuse:w:0xDD:m -U efuse:w:0xFE:m
```

## Arduino كمنزلق تحميل

|    Attiny     | Arduino |
| :-----------: | :-----: |
| Pin 1（PB5）  |   D10   |
| Pin 4 （GND） |   GND   |
| Pin 5 （PB0） |   D11   |
| Pin 6 （PB1） |   D12   |
| Pin 7 （PB2） |   D13   |
| Pin 8 （VCC） |   5V    |

أولاً ، حرق برنامج ISP على Arduino:

![](https://img.wiki-power.com/d/wiki-media/img/20200426144425.png)

افتح تفضيلات IDE واملأ عنوان لوحة التطوير الإضافية:

```
https://raw.githubusercontent.com/damellis/attiny/ide-1.6.x-boards-manager/package_damellis_attiny_index.json
```

افتح مدير لوحة التطوير:

![](https://img.wiki-power.com/d/wiki-media/img/20200426144642.png)

ابحث وقم بتثبيت (قد يحتاج إلى وكيل):

![](https://img.wiki-power.com/d/wiki-media/img/20200426144732.png)

عند الحرق ، تأكد من اختيار نوع الرقاقة الصحيح وسرعة الساعة (16 ميجاهرتز داخليًا) ومنفذ Arduino ، وتأكد من اختيار برنامج الترميز "Arduino as ISP":

![](https://img.wiki-power.com/d/wiki-media/img/20200426144834.png)

## استنتاج

## المراجع والشكر

- [دليل صنع أصغر نظام ديجيسبارك أردوينو باستخدام ATTiny85 (الجزء الأول)](https://blog.csdn.net/Argon_Ghost/article/details/103637870?depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4&utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromBaidu-4)
- [دليل صنع أصغر نظام ديجيسبارك أردوينو باستخدام ATTiny85 (الجزء الثاني)](https://blog.csdn.net/Argon_Ghost/article/details/103859931)
- [ملاحظات حول لوحة تطوير Digispark USB (الجزء الأول): تعرف على هذه اللوحة الصغيرة والرخيصة والمتعددة الوظائف للأردوينو المتوافقة](https://zhuanlan.zhihu.com/p/73336394)
- [الاتصال وبرمجة ديجيسبارك الخاص بك](http://digistump.com/wiki/digispark/tutorials/connecting)
- [حرق برنامج Micronucleus bootloader على Attiny85](http://iremo-tw.blogspot.com/2018/03/attiny85-micronucleus-bootloader.html)
- [صنع جهاز ألعاب صغير باستخدام ATtiny85](https://www.jianshu.com/p/55e86b4e0194)
- [DigiSpark ATtiny85 8 طرفًا لبرمجة AVR ISP للأردوينو BootLoader والصمامات الذائبة](http://blog.sina.com.cn/s/blog_6566538d0102w6qk.html)
- [Quick Reference Frequently requested info](http://digistump.com/wiki/digispark/quickref)

> المؤلف: **Power Lin**
> المصدر الأصلي: <https://wiki-power.com>
> بروتوكول حقوق النشر: يتم استخدام بروتوكول [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) لهذه المقالة، يرجى الإشارة إلى المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
