# سلسلة BeagleBone - المعلمات الأساسية وإعداد البيئة

## موارد الأجهزة

![صورة](https://media.wiki-power.com/img/20211008090724.png)

- USB Type-A: يُستخدم في وضع USB العبد (Host)
- USB Micro: لتوصيل اللوحة بالكهرباء واستخدامها كجهاز عبد
- LEDs
  - D2: يتم توهجه عند بدء التشغيل
  - D3: يضيء عند قراءة أو كتابة بيانات على بطاقة SD
  - D4: يضيء عندما تكون وحدة المعالجة المركزية نشطة
  - D5: يضيء عند قراءة أو كتابة على eMMC
- زر Boot/User: بغض النظر عما إذا تم الضغط عليه أم لا، سيتم الافتراض بدء التشغيل من بطاقة SD (الطريق نفسه)، وبعد البدء يصبح زرًا عاديًا يتصل بـ GPIO_72
- واجهة I2C Grove: متصلة بـ I2C2
- واجهة UART Grove: متصلة بـ UART2
- Serial Debug: متصلة بـ UART0، حيث يكون الدبوس الأقرب إلى USB هو الدبوس رقم 1، ومن الدبوس 1 إلى الدبوس 6 على التوالي: GND، NC، NC، RX، TX، NC

## إعداد البيئة

### مشكلة تثبيت التعريف

في أنظمة Windows 10 وما فوق، يتم استخدام توقيع التعريف الإجباري افتراضيًا، وهذا قد يكون سببًا لفشل تثبيت التعريف.

الحلا:

- اضغط باستمرار على `shift` ثم انقر على إعادة تشغيل الكمبيوتر.
- انتقل إلى `استكشاف مشكلة` - `خيارات متقدمة` - `إعدادات البدء`، وانقر على `إعادة التشغيل`.
- بعد إعادة التشغيل، اتبع التعليمات على الشاشة واضغط على الزر `7` من لوحة المفاتيح لتعطيل توقيع التعريف الإجباري.
- بعد الإقلاع، يمكنك الآن تثبيت تعريف BeagleBone بشكل طبيعي.

### تنزيل وحرق الصورة

عنوان تنزيل الصورة الرسمية: https://beagleboard.org/latest-images  
أداة الحرق: https://sourceforge.net/projects/win32diskimager/files/latest/download

قم بحرق الصورة على بطاقة SD، ومن ثم قم بإيقاف التشغيل وإدخالها في BeagleBone، وعند تشغيله مرة أخرى، سيتم بدء التشغيل من بطاقة SD.

## الوصول عبر أدوات سطر الأوامر

### الوصول عبر المنفذ التسلسلي

قم بتوصيل اللوحة بجهاز الكمبيوتر باستخدام USB إلى منفذ سلسلي، ثم افتح أداة المنفذ التسلسلي على الكمبيوتر (مثل WindTerm) للاتصال. (اسم المستخدم وكلمة المرور الافتراضية هما "root").

معدل الباود هو 115200!

### الوصول عبر الشبكة

ضمن اتصال المنفذ التسلسلي، استخدم الأمر `ifconfig` للعثور على عنوان الشبكة الخاص بالإيثرنت، ثم قم بالاتصال باستخدام هذا العنوان. اسم المستخدم هو "debian"، وكلمة المرور هي "temppwd".

### الوصول عبر USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

استخدم الوصول عبر SSH، واسم المستخدم هو "debian"، وكلمة المرور هي "temppwd".

## تمكين حساب المستخدم الجذر لبروتوكول SSH

```shell
vi /etc/ssh/sshd_config
```

قم بتعديل `#PermitRootLogin prohibit-password` إلى `PermitRootLogin yes` لتمكين الوصول باستخدام الحساب الجذر.

## تثبيت تعريف Seeed OLED (SSD1306، I2C، 12864)

استخدم pip3 لتثبيت حزمة smbus2:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

لمزيد من المعلومات، انظر إلى البرنامج

- [مشكلات تصحيح Beaglebone Black 4G](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [المشروع](https://beagleboard.org/p)
- [ترقية البرنامج على Beagle الخاص بك](https://beagleboard.org/upgrade#connect)
- [اختبار البرامج الثابتة](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
