# T-Clock ساعة مكتبية صغيرة

## المواد المطلوبة

1. **NodeMCU**: مبني على ESP8266
2. **OLED**: دقة 128x64، واجهة I2C (SPI يرجى الرجوع إلى الروابط المرجعية)

## التوصيل

| OLED | NodeMCU |
| :--: | :-----: |
| GND  |   GND   |
| VCC  |  3.3V   |
| SCL  |   D1    |
| SDA  |   D2    |

## مثال

### تكوين API

1. سجل حسابًا في [**Seniverse**](https://www.seniverse.com/)
2. أضف منتجًا جديدًا في لوحة التحكم (يمكنك اختيار الإصدار المجاني)
3. انسخ المفتاح الخاص بالواجهة

### ملفات المكتبة المضمنة

- [**Adafruit_SSD1306.h**](https://github.com/adafruit/Adafruit_SSD1306)

### المثال النهائي

- [**T-Clock/Software/Codes/Weather_Clock_OLED_I2C**](https://github.com/linyuxuanlin/T-Clock/tree/master/Software/Codes/Weather_Clock_OLED_I2C)

ملاحظة: يجب تغيير اسم شبكة WiFi وكلمة المرور والمدينة والمفتاح الخاص بك.  
إذا ظهر خطأ أثناء الترجمة وتم تحديد رسالة الخطأ في `#error("Height incorrect, please fix Adafruit_SSD1306.h!");`، فيجب فتح ملف المكتبة `Adafruit_SSD1306.h` وتغيير `#define SSD1306_128_32` إلى `#define SSD1306_128_64`.

ملاحظة: المشروع المخصص للأجهزة قيد التطوير!

## المراجع والشكر

- [T-Clock ساعة مكتبية صغيرة (قديم)](https://wiki-power.com/ar/unlist/T-Clockساعة مكتبية صغيرة (قديم))
- [Seniverse](https://www.seniverse.com/)
- [ESP8266 يتصل بواجهة Seniverse API【البرنامج + شرح مفصل】](https://www.bilibili.com/video/av89935868/?spm_id_from=333.788.b_636f6d6d656e74.4)
- [ESP8266 + OLED = ساعة شبكية وتوقعات الطقس للأيام الثلاثة القادمة](https://www.bilibili.com/video/av88920975/)
- [My_ESP8266/Seniverse](https://gitee.com/young_people_only_love_her/My_ESP8266/tree/master/%E5%BF%83%E7%9F%A5%E5%A4%A9%E6%B0%94)
- [توصيل شاشة OLED الرسومية مع NodeMCU](https://www.electronicwings.com/nodemcu/oled-graphic-display-interfacing-with-nodemcu)
- [adafruit/Adafruit_SSD1306](https://github.com/adafruit/Adafruit_SSD1306)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.