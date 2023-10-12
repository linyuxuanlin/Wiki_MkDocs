# TinyMonitor - مراقب حالة الخادم الصغير

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261716469.jpg)

TinyMonitor هو مراقب حالة الخادم الصغير والبسيط للغاية ، وهو يتكون فقط من ESP32 الرئيسي وشاشة OLED ، ويمكنه عرض معلمات حالة الخادم الحية لتسهيل المراقبة والتصحيح.

## التحضيرات الأولية

المواد الأولية المستخدمة في هذا المشروع بسيطة للغاية ، وهي Beetle ESP32-C3 الذي يحتوي على Wi-Fi و Bluetooth مدمجين ، بالإضافة إلى شاشة OLED بحجم 128x64.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261541993.png)

تعريف دبوس Beetle ESP32-C3 كما يلي.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261545236.png)

نظرًا لأنه يمكن استخدام طريقة I2C البرمجية (أي تعريف دبوس I2C المخصص) لتشغيل شاشة OLED ، فقد قمت بتعريف دبوس `0` / `1` لـ Beetle ESP32-C3 كـ `SCL` / `SDA`. بالتالي ، يكون التوصيل بسيطًا للغاية ، حيث يتم لصق 4 دبابيس معًا.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261546367.png)

ملاحظة: قبل تفريغ برنامج على Beetle ESP32-C3 ، يجب إضافة حزمة ESP32 للتعرف على نموذج اللوحة بشكل صحيح. انظر صفحة [**Wiki**](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3) للحصول على التفاصيل.

### تشغيل الشاشة

يمكن استخدام هذا البرنامج البسيط لاختبار ما إذا كان بإمكانك عرض المعلومات بشكل صحيح على OLED:

```cpp title="OLED_SoftwareI2C_HelloWorld.ino"
#include <U8g2lib.h>

#define OLED_SDA 1
#define OLED_SCL 0

U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2,  OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

void setup(void) {
  u8g2.begin();
}

void loop(void) {
  u8g2.clearBuffer();
  u8g2.setFont(u8g2_font_ncenB08_tr);
  u8g2.drawStr(0,10,"Hello World!");
  u8g2.sendBuffer();
  delay(1000);
}
```

## خدمة وكيل MQTT

MQTT هو بروتوكول نقل الرسائل الذي يعتمد على عميل - خادم. في هذا المشروع ، يعد MQTT جسرًا للاتصال بين الخادم و ESP32. للراحة ، قمت بنشر خدمة MQTT على الخادم الذي يجب مراقبته. إذا لزم الأمر ، يمكنك أيضًا نشره على أجهزة أخرى.

### نشر خدمة Mosquitto

Mosquitto هو برنامج وكيل رسائل مفتوح المصدر يدعم بروتوكول نشر الرسائل MQTT v3.1. في هذا المثال ، استخدمت [**eclipse-mosquitto**](https://hub.docker.com/_/eclipse-mosquitto) المنشورة باستخدام Docker كخادم وكيل MQTT. إذا لم تكن ملمًا بطريقة نشر Docker ، فيمكنك الرجوع إلى المقالات [**Docker الدليل البسيط**](https://wiki-power.com/ar/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97/) و [**Docker Compose - طريقة أكثر أناقة للفتح**](https://wiki-power.com/ar/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F/) للمزيد من المعلومات.

وفقًا للشرح الرسمي ، يجب أولاً إنشاء المجلدات والملفات التالية للاستخدام بواسطة Mosquitto وتخصيص الأذونات الكافية: (يرجى تعديل `${STACK_DIR}` إلى مسار تخزين البيانات المحلي ، مثل `/ DATA / AppData / mosquitto` ، كما هو موضح في النص التالي)

```bash
mkdir -vp ${STACK_DIR}/{config,data,log} \
&& touch ${STACK_DIR}/config/mosquitto.conf \
&& chmod -R 755 ${STACK_DIR} \
&& chmod -R 777 ${STACK_DIR}/log \
```

ثم ، اكتب المحتوى التالي في ملف `mosquitto.conf`:

```conf title="mosquitto.conf"
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log

# إيقاف تشغيل الوضع المجهول
allow_anonymous false
# تحديد ملف كلمة المرور
password_file /mosquitto/config/pwfile.conf
```

استخدم طريقة `docker-compose` لنشر الحاويات:

```yaml title="compose.yaml"
version: "3"
services:
  mosquitto:
    container_name: mosquitto_app
    image: eclipse-mosquitto:1.6.14 # 2.x قد لا يكون لها توافق جيد
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

ادخل الحاوية وقم بتغيير كلمة المرور:

```bash
cd مسار حفظ compose.yaml
docker compose up

docker compose ps # العثور على معرف الحاوية التي تعمل
docker exec -it معرف الحاوية sh # الدخول إلى shell الحاوية

touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf

# إنشاء اسم المستخدم وكلمة المرور ، اسم المستخدم: test ، كلمة المرور: 123
mosquitto_passwd -b /mosquitto/config/pwfile.conf test 123

exit # الخروج من shell الحاوية
docker restart معرف الحاوية # إعادة تشغيل الحاوية للتطبيق
```

### اختبار توافر خادم MQTT

بعد تشغيل خدمة `mosquitto` بشكل طبيعي ، يمكننا استخدام [**MQTTBox**](https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG) لاختبار توافر خادم وكيل MQTT.

بعد تثبيت البرنامج ، انقر فوق `Create MQTT Client` لإنشاء اتصال جديد ، وفقًا للمعلمات ذات الصلة الموضحة في الشكل التالي:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261456592.png)

حيث `HOST` هو عنوان خادم MQTT (على سبيل المثال ، يكون عنوان خادمي في الشبكة المحلية `192.168.1.2`) ؛ يجب أن تتطابق اسم المستخدم وكلمة المرور مع القيم التي تم تعيينها عند تكوين Mosquitto.

بعد النقر فوق `Save` ، إذا رأينا `Connected` الأخضر في شريط الحالة العلوي ، فهذا يعني أننا قد اتصلنا بالخادم بنجاح.

## نصيحة لمراقبة الخادم

يمكننا تنفيذ جمع المعلومات في الوقت الحقيقي عن الجهاز وإرسالها إلى موضوع MQTT المناسب عن طريق تشغيل البرنامج النصي Python التالي على الخادم. يتطلب ذلك تثبيت الحزم التالية أولاً:

```bash
pip install paho-mqtt psutil
```

أنشئ وشغل برنامج Python التالي:

```python title="status-collector.py"
import paho.mqtt.client as mqtt
import psutil
import time

# اتصل بخادم وكيل MQTT
client = mqtt.Client()
client.username_pw_set("MQTTاسم المستخدم", "MQTTكلمة المرور")
client.connect("عنوان خادم MQTT", رقم المنفذ)
# مثال: client.connect("192.168.1.2", 1883)

# جمع حالة الخادم وإرسالها إلى موضوع MQTT
while True:
    client.publish("USAGE_CPU", psutil.cpu_percent())
    client.publish("USAGE_MEM", psutil.virtual_memory().percent)
    client.publish("USAGE_DISK", psutil.disk_usage('/').percent)
    time.sleep(1) # نشر كل ثانية واحدة
```

بعد تشغيل البرنامج بنجاح ، يمكننا النقر فوق `Add subscriber` في شريط الحالة العلوي لـ MQTTBox لإضافة اشتراك لهذه الثلاثة موضوعات ، على سبيل المثال:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261513642.png)

إذا كان كل شيء على ما يرام ، يجب أن تتمكن من رؤية معلومات حالة الخادم المستمرة في MQTTBox.

## جهاز Arduino ESP32 عرض النهاية

أنشئ الكود Arduino التالي ، وقم بتعديل المعلمات وحرقها على ESP32. إذا كان كل شيء على ما يرام ، يجب أن تتمكن من رؤية معلومات الحالة المستمرة.

```cpp title="Received-from-MQTT-and-Display.ino"
#include <Wire.h>
#include <U8g2lib.h>
#include <WiFi.h>
#include <PubSubClient.h>

// استخدام I2C البرمجي لتوصيل OLED ، إعادة تعريف دبوس
#define OLED_SDA 1
#define OLED_SCL 0

// MQTT تعريف
#define WIFI_SSID "اسم شبكة الواي فاي"
#define WIFI_PASSWORD "كلمة مرور شبكة الواي فاي"
#define MQTT_BROKER "عنوان خادم MQTT" // مثال: 192.168.31.2
#define MQTT_PORT رقم المنفذ MQTT // مثال: 1883
#define MQTT_USERNAME "MQTTاسم المستخدم" //test ، يجب أن يتطابق مع التكوين المذكور أعلاه
#define MQTT_PASSWORD "MQTTكلمة المرور" //123 ، يجب أن يتطابق مع التكوين المذكور أعلاه
#define MQTT_TOPIC_CPU "USAGE_CPU" // الموضوع المشترك
#define MQTT_TOPIC_MEM "USAGE_MEM"
#define MQTT_TOPIC_DISK "USAGE_DISK"

char msg_cpu_usage[10];
char msg_mem_usage[10];
char msg_disk_usage[10];

// تعريف كائن الشاشة OLED
U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

// كائن عميل WIFI
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);
```

// دالة استدعاء MQTT
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
    // تسجيل استخدام القرص الصلب
    for (int i = 0; i < length; i++)
      msg_disk_usage[i] = (char)payload[i];
  }
}

void setup() {
  u8g2.begin();  // تهيئة شاشة OLED
  Wire.begin();  // بدء نقل I2C

  // الاتصال بشبكة الواي فاي
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // الاتصال بخادم وسيط MQTT
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

    // عرض استخدام القرص الصلب
    u8g2.setCursor(0, 58);
    u8g2.print("Disk: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_disk_usage[i]);
    u8g2.print(" %");

  } while (u8g2.nextPage());
}
```

## مزيد من الأفكار للتوسع

الأفكار التالية تحتاج إلى التنفيذ:

- زيادة البطارية والغلاف المطبوع ثلاثي الأبعاد لصنع أدوات مكتبية صغيرة أكثر دقة
- إضافة الاتصال الداخلي لجعلها معلقة صغيرة يمكن مراقبة حالة الخادم حتى عندما لا تكون في المنزل
- تغليف برنامج المراقبة باستخدام Python كطريقة لنشر Docker
- تحسين تخطيط واجهة المستخدم لمراقبة المزيد من المعلمات
- إضافة ميزة مراقبة حالة الخادم لعدة خوادم
- إضافة ميزة تنبيه عند تجاوز بعض المعلمات الحد الأقصى

ملاحظة: صورة Beetle ESP32-C3 و Seeed XIAO ESP32C3.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261719170.jpg)

## المراجع والشكر

- [DFRobot Wiki · Beetle ESP32 C3](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)
- [إنشاء نظام مراقبة أداء Raspberry Pi باستخدام Arduino و MQTT](https://www.zhihu.com/tardis/zm/art/463880669?source_id=1003)
- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [Docker - تثبيت ونشر خدمة Mosquitto عبر الحاويات (خادم MQTT)](https://www.hangge.com/blog/cache/detail_2896.html)
- [MQTT سلسلة دروس 3 (تثبيت واستخدام أداة MQTTBox للعميل)](https://www.hangge.com/blog/cache/detail_2350.html)
- [linyuxuanlin/TinyMonitor](https://github.com/linyuxuanlin/TinyMonitor)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.