# سلسلة BeagleBone - تطوير باستخدام مكتبة BBIO

## تثبيت Adafruit-BBIO

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO
```

## إطار البرنامج الأساسي

```py
import time
import Adafruit_BBIO.GPIO as GPIO

RELAY = "P9_22"            # GPIO P9_22
GPIO.setup(RELAY, GPIO.OUT)

while True:

    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(1)
```

## GPIO

استدعاء المكتبة:

```py
import Adafruit_BBIO.GPIO as GPIO
```

### تعيين دخل / إخراج الأرجل

```py
GPIO.setup("P8_14", GPIO.OUT)
```

يمكن اختيار `المدخل` / `المخرج` `GPIO.IN`/`GPIO.OUT`.

### تعيين مستوى الإخراج العالي / المنخفض

```py
GPIO.output("P8_14", GPIO.HIGH)
```

يمكن اختيار `المستوى العالي` / `المستوى المنخفض` `GPIO.HIGH`/`GPIO.LOW`، أو `1`/`0`.

### وضع الدخل الأرجل

عرض حالة المنفذ الداخلي:

```py
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

انتظار الحافة الداخلية، يوجد معلمات `GPIO.RISING`/`GPIO.FALLING`/`GPIO.BOTH`:

```py
GPIO.wait_for_edge(channel, GPIO.RISING)

أو

GPIO.wait_for_edge(channel, GPIO.RISING, timeout)
```

### رصد الدخل

```py
GPIO.add_event_detect("P9_12", GPIO.FALLING)
if GPIO.event_detected("P9_12"):
    print "event detected!"
```

## التأخير

تأخير لمدة ثانية:

```py
import time
time.sleep(1)
```

## PWM الإخراج

```py
import Adafruit_BBIO.PWM as PWM
#PWM.start(القناة, نسبة العرض, التردد الافتراضي=2000, القطبية=0)
PWM.start("P9_14", 50)

#يمكن أيضًا تحديد التردد والقطبية بشكل مستقل
PWM.start("P9_14", 50, 1000, 1)
```

حيث يكون نسبة العرض الفعالة بين 0.0-100.0، وتستخدم وظيفة start لتنشيط PWM على هذه القناة.

بعد تشغيل PWM، يمكن تعيين نسبة العرض أو التردد بشكل منفصل:

```py
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

بعد الانتهاء، يمكن إيقاف إخراج PWM، أو مسح المعلومات:

```py
PWM.stop("P9_14")
PWM.cleanup()
```

## ADC الدخل

في هذا الإطار، يوجد ثلاثة وظائف لـ ADC: setup و read و read_raw. يجب تعيين setup قبل قراءة البيانات.

يمكن استخدام المنافذ التالية لـ ADC على BeagleBone:

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```

تنبيه: الجهد الأقصى لـ ADC هو 1.8 فولت ، وأرضية ADC هي GNDA_ADC (P9_34) pin. إذا كنت بحاجة إلى قياس 3.3 فولت ، فيمكن استخدام تقسيم الجهد باستخدام مقاومة ، مثل الصورة أدناه ، لتقسيم 0-3.3 فولت إلى 0-1.65 فولت لقراءة القيم الأنالوجية.

### تهيئة ADC

```py
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### قراءة القيم الأنالوجية

```py
value = ADC.read("P9_40")

أو

value = ADC.read("AIN1")
```

هناك خطأ في هذا الإطار يتطلب قراءة متتالية مرتين للحصول على أحدث القيم الأنالوجية.

القيم المقروءة هي قيمة بين 0 و 1.0 ، يمكن ضربها بـ 1.8 لتحويلها إلى قيمة الجهد. إذا كنت لا تريد ذلك ، فيمكن استخدام read_raw لقراءة الجهد الحقيقي مباشرةً.

## تواصل I2C

للاستخدام مع I2C ، يتم تحميل المكتبة وتعيين عنوان I2C واختيار I2C المستخدم (الافتراضي هو I2C-1).

```py
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

يتطلب تشغيل I2C تثبيت حزمة python `python-smbus` ، ولكن هذه الحزمة تعمل فقط مع إصدار python 2. يمكن استخدام [**smbus2**](https://pypi.org/project/smbus2/) كبديل.

## تواصل SPI

يتم تحميل مكتبة SPI كالتالي:

```py
from Adafruit_BBIO.SPI import SPI
```

## آخر

إذا فشل تثبيت Adafruit-BBIO ، فيمكن التثبيت يدويًا:

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

تحديث Adafruit-BBIO:

```
sudo pip3 install --upgrade Adafruit_BBIO
```

بسبب اعتمادية python-smbus ، يتم استخدام I2C فقط في python2.

## المراجع والشكر

- [Python Adafruit_GPIO.I2C Examples](https://www.programcreek.com/python/example/92524/Adafruit_GPIO.I2C)
- [Adafruit-BBIO 1.2.0](https://pypi.org/project/Adafruit-BBIO/#description)
- [Setting up IO Python Library on BeagleBone Black](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.