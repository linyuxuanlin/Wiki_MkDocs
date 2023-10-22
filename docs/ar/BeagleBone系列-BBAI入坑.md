# سلسلة BeagleBone - البداية في BBAI

## البداية

أولاً، قم بتوصيل مصدر الطاقة بجهاز Cape الخاص بك بجهد 12 فولت، واستخدم وحدة تحويل USB إلى منفذ التسلسل للاتصال بمنفذ السلسلة المدمج (الموجود في منفذ J3 ويمكن استخدامه لأغراض التصحيح):

![الصورة](https://img.wiki-power.com/d/wiki-media/img/20211027164010.png)

تأكد من أن وحدة تحويل USB إلى منفذ التسلسل مزودة بالتعريفات (استخدمت وحدة FTDI، يمكن العثور على التعريفات على العنوان التالي: <https://ftdichip.com/drivers/vcp-drivers/>).

استخدم أداة سطر الأوامر للاتصال بمنفذ التسلسل (استخدمت MobaXterm في حالتي) وقم بضبط معدل الباود على 115200.

## تثبيت حزم الإصلاحات

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

قم بتغيير اسم الملف إلى `k3-j721e-beagleboneai64.dtb` وانقله إلى المجلد `/boot` واستبدل الملف الأصلي. (قمت بتحميل الملف إلى مستودع GitHub الخاص بي واستخدمت الأمر `wget` للحصول عليه. قد تحتاج إلى تعديل مضيف GitHub لتمكين التنزيل الصحيح)

يمكنك أيضًا نقل الملف مباشرة باستخدام sftp.

## evtest

أداة اختبار الأحداث هي أداة تُستخدم لطباعة أحداث نواة evdev مباشرة من جهاز النواة. تقوم بقراءة الأحداث من الجهاز وطباعة الأحداث التي تحتوي على قيم وأسماء رموز مرتبطة بالجهاز، ويمكن استخدامها لتصحيح أجهزة الإدخال مثل الماوس ولوحة المفاتيح ولوحة اللمس.

قم بتنزيل أداة evtest:

```shell
sudo apt install evtest
```

استخدم الأداة كما يلي:

```shell
sudo evtest /dev/input/eventｘ (حيث x هو رقم الحدث)
```

## الأزرار

```shell
debian@BeagleBone:~$ evtest
لم يتم تحديد جهاز، حاول البحث في جميع الأحداث على /dev/input/event*
الأجهزة المتاحة:
/dev/input/event0:      gpio-keys
اختر رقم الحدث [0-0]: 0
إصدار سائق الإدخال هو 1.0.1
معرف الجهاز: الحافلة 0x19 البائع 0x1 المنتج 0x1 الإصدار 0x100
اسم الجهاز: "gpio-keys"
الأحداث المدعومة:
  نوع الحدث 0 (EV_SYN)
  نوع الحدث 1 (EV_KEY)
    رمز الحدث 256 (BTN_0)
    رمز الحدث 257 (BTN_1)
    رمز الحدث 258 (BTN_2)
معالجة تكرار الأزرار:
  نوع التكرار 20 (EV_REP)
    رمز التأخير 0 (REP_DELAY)
      القيمة    250
    رمز الفترة 1 (REP_PERIOD)
      القيمة     33
الخصائص:
جاري الاختبار... (انقر للخروج)
حدث: الزمن 1634868166.060258، النوع 1 (EV_KEY)، الرمز 257 (BTN_1)، القيمة 1
حدث: الزمن 1634868166.060258، -------------- SYN_REPORT ------------
حدث: الزمن 1634868166.284257، النوع 1 (EV_KEY)، الرمز 257 (BTN_1)، القيمة 0
حدث: الزمن 1634868166.284257، -------------- SYN_REPORT ------------
```

## الأجهزة على خط SPI

- بارومتر - BMP280
- 6-DOF - LSM6DS3TR
- بوصلة - BMM150

```markdown
```shell
cd /sys/bus/iio/devices && ls -l

cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## BeagleConnect Communication

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

The test was unsuccessful, no data was transmitted or received.

## LEDs

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightness

echo 0 > beaglebone:green:cape1/brightness # Unable to turn off
```

## Laser Radar

If you encounter permission issues, please refer to [**Enabling the Root Account with SSH**[to_be_replaced[3]]BeagleBone Series - Basic Parameters and Environment Configuration#Enabling-the-root-account-for-ssh], and execute with root privileges.

First, operate the GPIO to make the laser radar rotate.

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

Confirm the interface:

```shell
ls -l /sys/class/tty/

lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

Download the latest SDK from: <https://github.com/Slamtec/rplidar_sdk/releases>

Modify the `/sdk/sdk/src/hal/event.h` file for proper compilation:

```shell
enum
     {
         EVENT_OK = 1,
-        EVENT_TIMEOUT = -1,
+        EVENT_TIMEOUT = 2,
         EVENT_FAILED = 0,
     };
```
```

```markdown
انتقل إلى الدليل `/sdk` باستخدام الأمر `make` للترجمة. ستكون الملفات المترجمة موجودة في الدليل `/sdk/output`.

ثم، انتقل إلى الدليل `/sdk/output/Linux/Release` واستخدم الأمر التالي لتشغيل عينات الاختبار:

```shell
./ultra_simple /dev/ttyS0
```

## المراجع والشكر

- [مخطط الأساس](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [صورة النظام](https://rcn-ee.net/rootfs/debian-arm64/)
- [شفرات الاختبار](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [مشكلات Cape](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [مكتبة رادار الليزر](https://github.com/Slamtec/rplidar_sdk)

[للمرجع[1]]  
[للمرجع[2]]
```

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.