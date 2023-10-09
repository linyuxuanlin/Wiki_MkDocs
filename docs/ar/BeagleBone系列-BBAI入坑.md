# سلسلة BeagleBone - BBAI

## التهيئة الأولية

أولاً ، قم بتوصيل مدخل طاقة Cape بقوة 12 فولت ، واستخدم وحدة تحويل USB إلى سلك تسلسلي لتوصيل السلك التسلسلي المدمج (يمكن استخدام منفذ J3 للتصحيح):

![](https://f004.backblazeb2.com/file/wiki-media/img/20211027164010.png)

تأكد من تثبيت برنامج التشغيل لوحدة تحويل USB إلى سلك تسلسلي (استخدمت وحدة FTDI وكان عنوان تنزيل برنامج التشغيل هو <https://ftdichip.com/drivers/vcp-drivers/>).

استخدم أداة سطر الأوامر لتوصيل السلك التسلسلي (استخدمت MobaXterm) وضبط سرعة البت على 115200.

## تثبيت حزمة التصحيح

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

قم بتغيير الاسم إلى `k3-j721e-beagleboneai64.dtb` ، وانقله إلى المسار `/boot` واستبدل الملف الأصلي. (قمت بتحميل الملف إلى مستودع GitHub واستخدمت الأمر `wget` للحصول عليه. قد يتطلب تعديل مضيف GitHub للتنزيل بشكل صحيح)

يمكن أيضًا استخدام sftp لنقل الملف.

## أداة evtest

أداة اختبار الحدث هي أداة لطباعة أحداث kernel evdev ، وهي تقرأ مباشرةً من جهاز kernel وتطبع الحدث الذي يحتوي على قيمة واسم رمزي للجهاز ، ويمكن استخدامها لتصحيح أجهزة الإدخال مثل الماوس ولوحة المفاتيح ولوحة اللمس.

تنزيل أداة evtest:

```shell
sudo apt install evtest
```

استخدام الأداة:

```shell
sudo evtest /dev/input/eventｘ（ｘ هو رقم الحدث）
```

## الأزرار

```shell
debian@BeagleBone:~$ evtest
No device specified, trying to scan all of /dev/input/event*
Available devices:
/dev/input/event0:      gpio-keys
Select the device event number [0-0]: 0
Input driver version is 1.0.1
Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
Input device name: "gpio-keys"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 256 (BTN_0)
    Event code 257 (BTN_1)
    Event code 258 (BTN_2)
Key repeat handling:
  Repeat type 20 (EV_REP)
    Repeat code 0 (REP_DELAY)
      Value    250
    Repeat code 1 (REP_PERIOD)
      Value     33
Properties:
Testing ... (interrupt to exit)
Event: time 1634868166.060258, type 1 (EV_KEY), code 257 (BTN_1), value 1
Event: time 1634868166.060258, -------------- SYN_REPORT ------------
Event: time 1634868166.284257, type 1 (EV_KEY), code 257 (BTN_1), value 0
Event: time 1634868166.284257, -------------- SYN_REPORT ------------
```

## أجهزة SPI

- Barometer - BMP280
- 6-DOF - LSM6DS3TR
- Compass - BMM150

```shell
cd /sys/bus/iio/devices && ls -l
```

## اسم الجهاز

```shell
cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## BeagleConnect الاتصال

```shell
# BC_RST
cd /sys/class/gpio
echo 326 > export
echo out > gpio326/direction
echo 0 > gpio326/value
echo 1 > gpio326/value


# Uart2
root@BeagleBone:/sys/class/tty# ls -l
lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS4 -> ../../devices/platform/bus@100000/2820000.serial/tty/ttyS4

sudo apt-get install minicom
sudo minicom -D /dev/ttyS4

Welcome to minicom 2.8
OPTIONS: I18n
Port /dev/ttyS4, 10:57:41
Press CTRL-A Z for help on special keys

hello
```

لا يوجد اختبار ناجح ، لم يتم استلام أو إرسال البيانات.

## الصمامات

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightnessb

echo 0 > beaglebone:green:cape1/brightness # لا يمكن إيقافه
```

## ماسح الليزر

إذا تم الإشارة إلى عدم وجود الأذونات ، يرجى الرجوع إلى [**تمكين حساب root مع ssh**](https://wiki-power.com/ar/BeagleBone%E7%B3%BB%E5%88%97-%E5%9F%BA%E6%9C%AC%E5%8F%82%E6%95%B0%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E5%90%AF%E7%94%A8-ssh-%E7%9A%84-root-%E5%B8%90%E6%88%B7) ، واستخدام صلاحيات root.

أولاً ، قم بتشغيل مخرج GPIO لتشغيل ماسح الليزر.

```shell
cd /sys/class/gpio
echo 306 > export
echo 374 > export
echo out > gpio306/direction
echo out > gpio374/direction
echo 0 > gpio374/value
echo 1 > gpio306/value
```

echo 1 > gpio374/value
echo 0 > gpio306/value

تأكد من الواجهة:

```shell
ls -l /sys/class/tty/

lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

تنزيل SDK الأحدث: <https://github.com/Slamtec/rplidar_sdk/releases>

قم بتعديل ملف `/sdk/sdk/src/hal/event.h` للترميز الصحيح:

```shell
enum
     {
         EVENT_OK = 1,
-        EVENT_TIMEOUT = -1,
+        EVENT_TIMEOUT = 2,
         EVENT_FAILED = 0,
     };
```

انتقل إلى الدليل `/sdk` واستخدم أمر `make` للترميز ، وسيتم ترميز الملفات في الدليل `/sdk/output`.

## التبديل إلى المسار `/sdk/output/Linux/Release` واستخدام الأمر التالي لتشغيل برنامج الاختبار:

```shell
./ultra_simple /dev/ttyS0
```

## المراجع والشكر

- [مخطط الدائرة الكهربائية](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [صورة النظام](https://rcn-ee.net/rootfs/debian-arm64/)
- [كود الاختبار](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [مشكلة الـ Cape](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [ليزر الرادار](https://github.com/Slamtec/rplidar_sdk)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.