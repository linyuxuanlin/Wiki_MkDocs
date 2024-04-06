# TinyMonitor - مراقب حالة الخادم الصغير

![](https://media.wiki-power.com/img/202305261716469.jpg)

TinyMonitor هو مراقب حالة الخادم البسيط والمصغر جدًا، وهو مكون فقط من وحدة تحكم ESP32 وشاشة OLED، يمكن أن يعرض معلمات حالة الخادم في الوقت الحقيقي بسهولة للمراقبة والتصحيح.

## التحضير المبدئي

المواد العتيقة المستخدمة في هذا المشروع بسيطة للغاية، تحتاج إلى وحدة Beetle ESP32-C3 التي تحتوي على Wi-Fi و Bluetooth مدمجين، بالإضافة إلى شاشة OLED بحجم 128x64.

![](https://media.wiki-power.com/img/202305261541993.png)

تعريف أوصاف أطراف وحدة Beetle ESP32-C3 على النحو التالي.

![](https://media.wiki-power.com/img/202305261545236.png)

يمكن استخدام طريقة I2C البرمجية (أي تعريف أطراف I2C المخصصة) لتشغيل شاشة OLED، لذا قمت بتعريف أطراف Beetle ESP32-C3 بأنها SCL/SDA. بهذه الطريقة، يصبح التوصيل بسيطًا للغاية، حيث يتم توصيل الأطراف الأربعة مع بعضها البعض.

![](https://media.wiki-power.com/img/202305261546367.png)

ملاحظة: قبل تفريغ البرنامج إلى وحدة Beetle ESP32-C3، يجب إضافة ملفات باكدج ESP32 للتعرف على نموذج اللوحة بشكل صحيح. يمكنك العثور على التفاصيل في صفحتهم [**هنا**](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3) .

### تشغيل الشاشة

يمكن استخدام هذا البرنامج البسيط لاختبار ما إذا كان بإمكان الشاشة OLED عرض المعلومات بشكل صحيح:

```cpp title="OLED_SoftwareI2C_HelloWorld.ino"
#include <U8g2lib.h>

#define OLED_SDA 1
#define OLED_SCL 0

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB08_tr);
  u8g2.drawStr(0,10,"مرحبًا بالعالم!");
  u8g2.sendBuffer();
  delay(1000);
}
```

## خدمة وكيل MQTT

بروتوكول MQTT هو بروتوكول نقل الرسائل المستند إلى نمط النشر / الاشتراك بين العميل والخادم. في هذا المشروع، يعتبر MQTT جسرًا للاتصال بين الخادم ووحدة ESP32. للراحة، قمت بنشر خدمة MQTT على الخادم الذي نريد مراقبته. إذا لزم الأمر، يمكنك أيضًا نشرها على أجهزة أخرى.

### نشر خدمة Mosquitto

يعتبر Mosquitto برنامج وكيل الرسائل المفتوح المصدر الذي يدعم بروتوكول نقل الرسائل MQTT v3.1. في هذا السياق، استخدمت إصدار [**eclipse-mosquitto**](https://hub.docker.com/_/eclipse-mosquitto) الذي يتم نشره باستخدام Docker كخادم MQTT. إذا لم تكن على دراية بطريقة نشر Docker، يمكنك الرجوع إلى المقالات التالية [**دليل Docker المبسط**](https://wiki-power.com/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97/) و [**Docker Compose - طريقة أكثر أناقة للبدء**](https://wiki-power.com/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F/) إذا كنت غير ملم بكيفية القيام بذلك.

بناءً على التوجيهات الرسمية، أولاً يجب إنشاء الدلائل والملفات التالية لاستخدام Mosquitto وتخصيص الأذونات بشكل كافٍ: (يرجى استبدال `${STACK_DIR}` بمسار تخزين البيانات المحلي، مثل `/DATA/AppData/mosquitto`، كما هو مذكور فيما يلي)

```bash
mkdir -vp ${STACK_DIR}/{config,data,log} \
&& touch ${STACK_DIR}/config/mosquitto.conf \
&& chmod -R 755 ${STACK_DIR} \
&& chmod -R 777 ${STACK_DIR}/log
```

ثم، قم بكتابة المحتوى التالي في ملف `mosquitto.conf`:

```conf title="mosquitto.conf"
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log

# اغلاق الوضع المجهول
allow_anonymous false
# تحديد ملف كلمات المرور
password_file /mosquitto/config/pwfile.conf
```

استخدم طريقة `docker-compose` لنشر الحاويات:

```yaml title="compose.yaml"
version: "3"
services:
  mosquitto:
    container_name: mosquitto_app
    image: eclipse-mosquitto:1.6.14 # 2.x قد تكون غير متوافقة
    ports:
      - "1883:1883"
      - "9001:9001"
    volumes:
      - ${STACK_DIR}/config/mosquitto.conf:/mosquitto/config/mosquitto.conf
      - ${STACK_DIR}/data:/mosquitto/data
      - ${STACK_DIR}/log:/mosquitto/log
    #privileged: true
    restart: always
```

قم بالدخول إلى الحاوية وقم بتعديل كلمات المرور:

```bash
cd المسار الذي يحتوي على compose.yaml
docker compose up

docker compose ps # ابحث عن هوية الحاوية التي تعمل
docker exec -it هوية_الحاوية sh # ادخل إلى shell الحاوية

touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf

# إنشاء مستخدم وكلمة مرور، اسم المستخدم: test، كلمة المرور: 123
mosquitto_passwd -b /mosquitto/config/pwfile.conf test 123

exit # اخرج من shell الحاوية
docker restart هوية_الحاوية # أعد تشغيل الحاوية لتفعيل التغييرات
```

### اختبار توافر خادم MQTT

بعد بدء تشغيل خدمة `mosquitto` بشكل طبيعي، يمكننا اختبار توافر خادم الوكيل MQTT باستخدام [**MQTTBox**](https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG).

بعد تثبيت البرنامج، انقر فوق "إنشاء عميل MQTT" لإنشاء اتصال جديد، واملأ المعلمات كما هو موضح في الصورة أدناه:

![](https://media.wiki-power.com/img/202305261456592.png)

حيث "HOST" هو عنوان الخادم الذي توجد عليه خدمة MQTT (على سبيل المثال، إذا كان الخادم الخاص بك على نفس الشبكة المحلية، فإن العنوان يمكن أن يكون `192.168.1.2`)؛ ويجب أن تكون اسم المستخدم وكلمة المرور متطابقة مع القيم التي تم تكوينها في Mosquitto في الأعلى.

بمجرد الانتهاء، انقر على "حفظ"، وإذا رأيت "Connected" باللون الأخضر في شريط الحالة العلوي، فهذا يشير إلى أنك قد قمت بالاتصال بالخادم.

يمكننا القيام بجلب معلومات الجهاز في الوقت الفعلي وإرسالها إلى موضوعات MQTT المقابلة عن طريق تشغيل البرنامج البايثون التالي على الخادم:

أولاً، يجب تثبيت الحزم التالية باستخدام الأمر:

```bash
pip install paho-mqtt psutil
```

ثم، يجب إنشاء البرنامج البايثون التالي وتشغيله:

```python title="status-collector.py"
import paho.mqtt.client as mqtt
import psutil
import time

# الاتصال بخادم وكيل MQTT
client = mqtt.Client()
client.username_pw_set("اسم مستخدم MQTT", "كلمة مرور MQTT")
client.connect("عنوان خادم MQTT", "رقم المنفذ")
# مثال: client.connect("192.168.1.2", 1883)

# جمع حالة الخادم وإرسالها إلى موضوعات MQTT
while True:
    client.publish("USAGE_CPU", psutil.cpu_percent())
    client.publish("USAGE_MEM", psutil.virtual_memory().percent)
    client.publish("USAGE_DISK", psutil.disk_usage('/').percent)
    time.sleep(1) # نشر بيانات كل ثانية
```

بعد تشغيله بنجاح، يمكنك إضافة اشتراكات لهذه الموضوعات الثلاثة في شريط الحالة العلوي لـ MQTTBox، كما يلي:

![صورة](https://media.wiki-power.com/img/202305261513642.png)

إذا كان كل شيء على ما يرام، يجب أن ترى معلومات حالة الخادم تعود بشكل متكرر في MQTTBox.

## جهاز Arduino ESP32 للعرض

يمكنك إنشاء الشيفرة التالية في Arduino وتعديل المعلمات ومن ثم تحميلها إلى ESP32. إذا كان كل شيء على ما يرام، يجب أن ترى معلومات حالة الخادم تتحدث بشكل مستمر.

```cpp title="Received-from-MQTT-and-Display.ino"
#include <Wire.h>
#include <U8g2lib.h>
#include <WiFi.h>
#include <PubSubClient.h>

// اتصال OLED بواسطة I2C بواسطة برمجة الأسلاك
#define OLED_SDA 1
#define OLED_SCL 0

// تعريف MQTT
#define WIFI_SSID "اسم شبكة الواي فاي"
#define WIFI_PASSWORD "كلمة مرور الواي فاي"
#define MQTT_BROKER "عنوان خادم MQTT" // مثال: 192.168.31.2
#define MQTT_PORT MQTT_PORT // مثال: 1883
#define MQTT_USERNAME "اسم مستخدم MQTT" // يجب أن يتطابق مع التكوين السابق
#define MQTT_PASSWORD "كلمة مرور MQTT" // يجب أن يتطابق مع التكوين السابق
#define MQTT_TOPIC_CPU "USAGE_CPU" // الموضوع المشترك فيه
#define MQTT_TOPIC_MEM "USAGE_MEM"
#define MQTT_TOPIC_DISK "USAGE_DISK"

char msg_cpu_usage[10];
char msg_mem_usage[10];
char msg_disk_usage[10];

// تعريف كائن شاشة OLED
U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

// كائن عميل واي فاي
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);
```

```arduino
// دالة رد الاستدعاء MQTT
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  if (strcmp(topic, MQTT_TOPIC_CPU) == 0) {
    // تسجيل استخدام وحدة المعالجة المركزية
    for (int i = 0; i < length; i++)
      msg_cpu_usage[i] = (char)payload[i];
  } else if (strcmp(topic, MQTT_TOPIC_MEM) == 0) {
    // تسجيل استخدام الذاكرة
    for (int i = 0; i < length; i++)
      msg_mem_usage[i] = (char)payload[i];
  } else if (strcmp(topic, MQTT_TOPIC_DISK) == 0) {
    // تسجيل استخدام القرص
    for (int i = 0; i < length; i++)
      msg_disk_usage[i] = (char)payload[i];
  }
}

void setup() {
  u8g2.begin();  // بدء تشغيل شاشة OLED
  Wire.begin();  // بدء نقل I2C

  // الاتصال بشبكة الواي فاي
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // الاتصال بخادم وكيل MQTT
  mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
  if (mqttClient.connect("ESP32", MQTT_USERNAME, MQTT_PASSWORD)) {
    mqttClient.subscribe(MQTT_TOPIC_CPU);
    mqttClient.subscribe(MQTT_TOPIC_MEM);
    mqttClient.subscribe(MQTT_TOPIC_DISK);
  }
}

void loop() {
  mqttClient.loop();  // معالجة رسائل MQTT
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_9x15_tf);

    // عرض استخدام وحدة المعالجة المركزية
    u8g2.setCursor(0, 12);
    u8g2.print("CPU: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_cpu_usage[i]);
    u8g2.print(" %");

    // عرض استخدام الذاكرة
    u8g2.setCursor(0, 35);
    u8g2.print("Mem: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_mem_usage[i]);
    u8g2.print(" %");

    // عرض استخدام القرص
    u8g2.setCursor(0, 58);
    u8g2.print("Disk: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_disk_usage[i]);
    u8g2.print(" %");

  } while (u8g2.nextPage());
}
```

## مزيد من الأفكار للتوسيع

هناك أفكار إضافية قيد البحث:

```

- إضافة مُلحقات بطارية وغلاف بتقنية الطباعة ثلاثية الأبعاد لتصميم أدق للديكورات الصغيرة على المكتب.
- توفير إمكانية اختراق الشبكة المحلية لتحويل الجهاز إلى مراقب صغير يُمكن مراقبته حتى عن بعد حتى خارج المنزل.
- تعبئة برنامج المراقبة المكتوب بلغة Python بتقنية Docker لتسهيل التنصيب.
- تحسين تصميم واجهة المستخدم لإظهار معلومات مراقبة أكثر.
- إضافة وظيفة مراقبة حالة عدة خوادم.
- إضافة إمكانية إصدار تنبيهات عند تجاوز بعض المعلمات الحد الأقصى.

مرفق: صورة مشتركة بين Beetle ESP32-C3 وSeeed XIAO ESP32C3.

![الصورة](https://media.wiki-power.com/img/202305261719170.jpg)

## المراجع والشكر

- [DFRobot Wiki · Beetle ESP32 C3](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)
- [بناء نظام مراقبة أداء Raspberry Pi باستخدام Arduino و MQTT](https://www.zhihu.com/tardis/zm/art/463880669?source_id=1003)
- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [Docker - دليل لتثبيت ونشر خدمة Mosquitto باستخدام الحاوية (خادم MQTT)](https://www.hangge.com/blog/cache/detail_2896.html)
- [دليل سلسلة MQTT 3 (تثبيت واستخدام أداة MQTTBox للعميل)](https://www.hangge.com/blog/cache/detail_2350.html)
- [linyuxuanlin/TinyMonitor](https://github.com/linyuxuanlin/TinyMonitor)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
```
