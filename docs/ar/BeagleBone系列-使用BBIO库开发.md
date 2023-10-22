# سلسلة BeagleBone - تطوير باستخدام مكتبة BBIO

## تثبيت Adafruit-BBIO

```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO
```

## هيكل البرنامج الأساسي

```python
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

```python
import Adafruit_BBIO.GPIO as GPIO
```

### تكوين دخل / إخراج الأرجل

```python
GPIO.setup("P8_14", GPIO.OUT)
```

يمكن اختيار "دخل" أو "إخراج" من بين `GPIO.IN` / `GPIO.OUT`.

### تعيين مستوى عالي / منخفض للإخراج

```python
GPIO.output("P8_14", GPIO.HIGH)
```

"عال" أو "منخفض" يمكن اختيارها من بين `GPIO.HIGH` / `GPIO.LOW` أو `1` / `0`.

### وضع الدخل للأرجل

اعرض حالة المنفذ الداخلي:

```python
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

انتظار إشارة الدخل، مع خيارات `GPIO.RISING` / `GPIO.FALLING` / `GPIO.BOTH`:

```python
GPIO.wait_for_edge(channel, GPIO.RISING)

أو

GPIO.wait_for_edge(channel, GPIO.RISING, timeout)
```

### رصد الإدخال

```python
GPIO.add_event_detect("P9_12", GPIO.FALLING)
if GPIO.event_detected("P9_12"):
    print "الحدث تم الكشف عنه!"
```

## التأخير

تأخير لمدة 1 ثانية:

```python
import time
time.sleep(1)
```

## الإخراج بتقنية PWM

```python
import Adafruit_BBIO.PWM as PWM
#PWM.start(القناة, نسبة الواجب, التردد الافتراضي=2000, القطبية=0)
PWM.start("P9_14", 50)

# يمكنك أيضًا تحديد التردد والقطبية بنفسك
PWM.start("P9_14", 50, 1000, 1)
```

حيث يتراوح نسبة الواجب الفعّالة بين 0.0 و 100.0، تُستخدم وظيفة "start" لتنشيط الإخراج بتقنية PWM على هذه القناة.

بمجرد تشغيل PWM، يمكنك تعيين نسبة الواجب أو التردد بشكل منفصل:

```python
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

عند الانتهاء من الاستخدام، يمكنك أيضًا إيقاف إخراج PWM أو مسح المعلومات:

```python
PWM.stop("P9_14")
PWM.cleanup()
```

## إدخال ADC

في هذا الهيكل، هناك ثلاث وظائف لـ ADC: setup، read، و read_raw. قبل قراءة البيانات، يجب تنفيذ الإعداد أولاً.

على BeagleBone، يمكن استخدام الأرجل التالية للADC:

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```



تنبيه: الجهد الأقصى لـ ADC هو 1.8 فولت، والأرضي للـ ADC هو دبوس GNDA_ADC (P9_34). إذا كنت بحاجة لقياس 3.3 فولت، يمكنك استخدام مقسم الجهد باستخدام المقاومات كما هو موضح في الصورة أدناه لتحويل النطاق من 0-3.3 فولت إلى 0-1.65 فولت لقراءة القيم الأنالوجية.

### تهيئة ADC

```python
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### قراءة القيم الأنالوجية

```python
value = ADC.read("P9_40")

أو

value = ADC.read("AIN1")
```

هذا الإطار يعاني من خلل يتطلب قراءة متتالية مرتين للحصول على أحدث القيم الأنالوجية.

القيم التي تم قراءتها تكون بين 0 و1.0، يمكن ضربها في 1.8 لتحويلها إلى قيم الجهد. إذا كنت لا ترغب في هذا العناء، يمكنك استخدام `read_raw` مباشرة لقراءة الجهد الحقيقي.

## التواصل عبر I2C

للاستفادة من التواصل عبر I2C، كل ما تحتاجه هو استيراد المكتبة، تعيين عنوان I2C، واختيار الحافلة I2C المراد استخدامها (الافتراضي هو I2C-1).

```python
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

يتعين تثبيت حزمة Python المسماة `python-smbus` لاستخدام الوظائف المتعلقة بـ I2C، ولكن في الوقت الحالي، تلك الحزمة متوافقة فقط مع Python 2. يمكن استخدام [**smbus2**](https://pypi.org/project/smbus2/) كبديل لها.

## التواصل عبر SPI

استيراد مكتبة SPI كما يلي:

```python
from Adafruit_BBIO.SPI import SPI
```

## ملاحظات أخرى

إذا فشل تثبيت Adafruit-BBIO بشكل تلقائي، يمكنك تثبيته يدويًا باستخدام الأوامر التالية:

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

ثم يمكنك ترقية Adafruit-BBIO كما يلي:

```
sudo pip3 install --upgrade Adafruit_BBIO
```

نظرًا لاعتماد python-smbus على Python 2، فإن التواصل عبر I2C متاح فقط في Python 2.

## المراجع والشكر

- [أمثلة Python Adafruit_GPIO.I2C](https://www.programcreek.com/python/example/92524/Adafruit_GPIO.I2C)
- [Adafruit-BBIO 1.2.0](https://pypi.org/project/Adafruit-BBIO/#description)
- [إعداد مكتبة IO Python على BeagleBone Black](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.