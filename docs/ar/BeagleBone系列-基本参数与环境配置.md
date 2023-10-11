# سلسلة BeagleBone - المعلومات الأساسية وإعداد البيئة

## الموارد الأساسية

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211008090724.png)

- USB Type-A: يستخدم كوضع USB العبد (Host)
- USB Micro: يستخدم لتزويد اللوحة بالطاقة وكوضع العبد
- LEDs
  - D2: يومض كضوء نبضي عند البدء
  - D3: يضيء عند قراءة أو كتابة بيانات SD كارد
  - D4: يضيء عندما يكون المعالج نشطًا
  - D5: يضيء عند قراءة أو كتابة eMMC
- Boot/User Button: بغض النظر عن الضغط أو عدم الضغط، إذا كان هناك بطاقة SD، فسيتم البدء من بطاقة SD بشكل افتراضي (نفس النتيجة)، وعند البدء، يعمل كزر عادي ويتصل بـ GPIO_72
- واجهة I2C Grove: متصلة بـ I2C2
- واجهة Uart Grove: متصلة بـ UART2
- Serial Debug: متصل بـ UART0، والدبابيس القريبة من USB هي الدبابيس 1، ومن الدبابيس 1 إلى 6 هي: GND، NC، NC، RX، TX، NC

## إعداد البيئة

### مشكلة تثبيت التعريف

في نظام Windows 10 والإصدارات الأحدث، يتم استخدام برنامج تشغيل التوقيع القوي افتراضيًا، وهذا قد يكون سببًا في فشل تثبيت التعريف.

الحل:

- اضغط على `shift` وانقر فوق إعادة التشغيل
- انتقل إلى `خيارات متقدمة` - `إعدادات الإقلاع` وانقر على `إعادة التشغيل`
- بعد الإعادة التشغيل، اتبع التعليمات الموجودة على الصفحة واضغط على الزر `7` على لوحة المفاتيح لتعطيل برنامج تشغيل التوقيع القوي
- بعد التشغيل، يمكنك تثبيت برنامج تشغيل BeagleBone بشكل طبيعي

### تحميل الصورة وحرقها

عنوان تحميل الصورة الرسمية: https://beagleboard.org/latest-images  
أداة الحرق: https://sourceforge.net/projects/win32diskimager/files/latest/download

قم بحرق الصورة على بطاقة SD وأدخلها في BeagleBone، وسيتم تشغيل النظام من بطاقة SD في المرة القادمة.

## الوصول إلى أدوات سطر الأوامر

### الوصول عبر المنفذ التسلسلي

قم بتوصيل المنفذ التسلسلي المدمج في اللوحة باستخدام USB إلى الكمبيوتر وافتح أداة المنفذ التسلسلي (مثل WindTerm) للاتصال. (اسم المستخدم وكلمة المرور الافتراضية هما `root`)

معدل البت هو 115200!

### الوصول عبر Ethernet

استخدم الأمر `ifconfig` داخل المنفذ التسلسلي للعثور على عنوان Ethernet والاتصال به. اسم المستخدم هو `debian` وكلمة المرور هي `temppwd`.

### الوصول عبر USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

استخدم الوصول عبر SSH، اسم المستخدم هو `debian` وكلمة المرور هي `temppwd`.

## تمكين حساب root الخاص بـ ssh

```shell
vi /etc/ssh/sshd_config
```

قم بتعديل `#PermitRootLogin prohibit-password` إلى `PermitRootLogin yes`.

## تعريف OLED Seeed (SSD1306، I2C، 12864)

استخدم pip3 لتنزيل حزمة smbus2:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

استخدم البرنامج المرجعي [**Grove - OLED Display 0.96 inch**](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green).

## المراجع والشكر

- [مشاكل تصحيح Beaglebone black 4G](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [المشروع](https://beagleboard.org/p)
- [ترقية البرامج على Beagle الخاص بك](https://beagleboard.org/upgrade#connect)
- [اختبار البرامج الثابتة](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
