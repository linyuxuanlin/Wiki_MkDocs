# TinyMonitor - A Compact Server Status Monitor

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261716469.jpg)

TinyMonitor is a compact and minimalist server status monitoring terminal. It consists of only an ESP32 controller and an OLED display screen, which can display real-time status parameters of the server for easy observation and debugging.

## Preparation

The hardware materials used in this project are very simple, a Beetle ESP32-C3 with built-in Wi-Fi and Bluetooth, and a 128x64 OLED screen.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261541993.png)

The pin definitions of Beetle ESP32-C3 are as follows.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261545236.png)

Because the OLED screen can be driven by software I2C (i.e. custom I2C pins), I defined the `0`/`1` pins of Beetle ESP32-C3 as `SCL`/`SDA` functions. In this way, the wiring is very simple, just solder the 4 pins together.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261546367.png)

Note: Before burning the program to Beetle ESP32-C3, you need to add the ESP32 package to recognize the board model normally. See its [**Wiki page**](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3) for details.

### Light up the screen

You can use this simple program to test whether information can be displayed normally on the OLED:

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

## MQTT Proxy Service

MQTT is a message publishing/subscribing transmission protocol based on client-server architecture. In this project, MQTT is the bridge for communication between the server and ESP32. For convenience, I deployed the MQTT service on the server that needs to be monitored; if necessary, you can also deploy it on other machines.

### Deploy Mosquitto Service

Mosquitto is an open-source message broker software that implements the MQTT v3.1 messaging protocol. Here, I am using the Docker deployment method of [**eclipse-mosquitto**](https://hub.docker.com/_/eclipse-mosquitto) as the MQTT broker server. If you are not familiar with Docker deployment, you can refer to the articles [**Docker Simple Guide**](https://wiki-power.com/en/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97/) and [**Docker Compose - A More Elegant Way to Open**](https://wiki-power.com/en/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F/).

According to the official instructions, you first need to create the following directories and files for Mosquitto to use, and give them sufficient permissions: (please modify `${STACK_DIR}` to the local data storage path, such as `/DATA/AppData/mosquitto`, the same below)

```bash
mkdir -vp ${STACK_DIR}/{config,data,log} \
&& touch ${STACK_DIR}/config/mosquitto.conf \
&& chmod -R 755 ${STACK_DIR} \
&& chmod -R 777 ${STACK_DIR}/log \
```

Then, write the following content into the `mosquitto.conf` file:

```conf title="mosquitto.conf"
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log

# Disable anonymous mode
allow_anonymous false
# Specify password file
password_file /mosquitto/config/pwfile.conf
```

Deploy the container using the `docker-compose` method:

```yaml title="compose.yaml"
version: "3"
services:
  mosquitto:
    container_name: mosquitto_app
    image: eclipse-mosquitto:1.6.14 # 2.x versions may have compatibility issues
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

Enter the container and change the password:

```bash
cd path where compose.yaml is located
docker compose up

docker compose ps # Find the ID of the running container
docker exec -it containerID sh # Enter the container shell

touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf

# Create a user and password, username: test, password: 123
mosquitto_passwd -b /mosquitto/config/pwfile.conf test 123

exit # Exit the container shell
docker restart containerID # Restart the container to take effect
```

### Test the availability of the MQTT server

After starting the `mosquitto` service normally, we can use [**MQTTBox**](https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG) to test the availability of the MQTT proxy server.

After installing the software, click `Create MQTT Client` to create a new connection and fill in the relevant parameters according to the following figure:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261456592.png)

Among them, `HOST` is the address of the server where the MQTT service is located (for example, the address of my server in the local area network is `192.168.1.2`); the username and password need to correspond to the values set when configuring Mosquitto in the previous section.

After clicking `Save`, if you see a green `Connected` in the top status bar, it means that the server has been connected.

## Server Monitoring Script

We can use the following Python program to collect real-time information of the device on the server and push it to the corresponding topic on the MQTT server. First, you need to install the following dependent packages:

```bash
pip install paho-mqtt psutil
```

Create and run the Python program:

```python title="status-collector.py"
import paho.mqtt.client as mqtt
import psutil
import time

# Connect to the MQTT proxy server
client = mqtt.Client()
client.username_pw_set("MQTT username", "MQTT password")
client.connect("MQTT server address", port number)
# Example: client.connect("192.168.1.2", 1883)

# Collect server status and send it to MQTT topic
while True:
    client.publish("USAGE_CPU", psutil.cpu_percent())
    client.publish("USAGE_MEM", psutil.virtual_memory().percent)
    client.publish("USAGE_DISK", psutil.disk_usage('/').percent)
    time.sleep(1) # Publish once every second
```

After running successfully, we can click `Add subscriber` on the top status bar of MQTTBox to subscribe to these three topics, for example:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261513642.png)

If everything is normal, you should be able to see the constantly returned server status information in MQTTBox.

## Arduino ESP32 Display End

Create the following Arduino code, modify the parameters, and burn it into ESP32. If everything is normal, you should be able to see the constantly updated status information.

```cpp title="Received-from-MQTT-and-Display.ino"
#include <Wire.h>
#include <U8g2lib.h>
#include <WiFi.h>
#include <PubSubClient.h>

// Use software I2C to connect OLED, redefine pins
#define OLED_SDA 1
#define OLED_SCL 0

```

// MQTT Definition
#define WIFI_SSID "Wi-Fi Name"
#define WIFI_PASSWORD "Wi-Fi Password"
#define MQTT_BROKER "MQTT Server Address" // e.g. 192.168.31.2
#define MQTT_PORT MQTT Port // e.g. 1883
#define MQTT_USERNAME "MQTT Username" // test, should correspond to the configuration above
#define MQTT_PASSWORD "MQTT Password" // 123, should correspond to the configuration above
#define MQTT_TOPIC_CPU "USAGE_CPU" // subscribed topic
#define MQTT_TOPIC_MEM "USAGE_MEM"
#define MQTT_TOPIC_DISK "USAGE_DISK"

char msg_cpu_usage[10];
char msg_mem_usage[10];
char msg_disk_usage[10];

// Define OLED screen object
U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

// WIFI client object
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

// MQTT callback function
void mqttCallback(char* topic, byte* payload, unsigned int length) {
if (strcmp(topic, MQTT_TOPIC_CPU) == 0) {
// Record CPU usage
for (int i = 0; i < length; i++)
msg_cpu_usage[i] = (char)payload[i];
} else if (strcmp(topic, MQTT_TOPIC_MEM) == 0) {
// Record memory usage
for (int i = 0; i < length; i++)
msg_mem_usage[i] = (char)payload[i];
} else if (strcmp(topic, MQTT_TOPIC_DISK) == 0) {
// Record disk usage
for (int i = 0; i < length; i++)
msg_disk_usage[i] = (char)payload[i];
}
}

void setup() {
u8g2.begin(); // Initialize OLED screen
Wire.begin(); // Start I2C transmission

// Connect to WIFI
WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
while (WiFi.status() != WL_CONNECTED) {
delay(1000);
}

// Connect to MQTT broker server
mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
mqttClient.setCallback(mqttCallback);
if (mqttClient.connect("ESP32", MQTT_USERNAME, MQTT_PASSWORD)) {
mqttClient.subscribe(MQTT_TOPIC_CPU);
mqttClient.subscribe(MQTT_TOPIC_MEM);
mqttClient.subscribe(MQTT_TOPIC_DISK);
}
}

void loop() {
mqttClient.loop(); // Handle MQTT messages
u8g2.firstPage();
do {
u8g2.setFont(u8g2_font_9x15_tf);

// Display CPU usage
u8g2.setCursor(0, 12);
u8g2.print("CPU: ");
for (int i = 0; i < 9; i++)
u8g2.print(msg_cpu_usage[i]);
u8g2.print(" %");

// Display memory usage
u8g2.setCursor(0, 35);
u8g2.print("Mem: ");
for (int i = 0; i < 9; i++)
u8g2.print(msg_mem_usage[i]);
u8g2.print(" %");

// Display disk usage
u8g2.setCursor(0, 58);
u8g2.print("Disk: ");
for (int i = 0; i < 9; i++)
u8g2.print(msg_disk_usage[i]);
u8g2.print(" %");

} while (u8g2.nextPage());
}

## More Extension Ideas

The following ideas are waiting to be implemented:

- Add a battery and a 3D printed case to create a more exquisite desktop gadget
- Add LAN penetration to make it a small gadget that can be used to observe server status even when not at home
- Package the Python monitoring program for deployment in Docker mode
- Optimize UI layout to achieve more parameter monitoring
- Add multi-server status monitoring function
- Add function to alert when certain parameters exceed the threshold

Attachment: Photo of Beetle ESP32-C3 and Seeed XIAO ESP32C3.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261719170.jpg)

## References and Acknowledgments

- [DFRobot Wiki · Beetle ESP32 C3](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)
- [Building a Raspberry Pi Performance Monitoring System with Arduino and MQTT](https://www.zhihu.com/tardis/zm/art/463880669?source_id=1003)
- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [Docker - Installing and Deploying Mosquitto Service through Containers (MQTT Server) Tutorial](https://www.hangge.com/blog/cache/detail_2896.html)
- [MQTT Series Tutorial 3 (Installation and Use of Client Tool MQTTBox)](https://www.hangge.com/blog/cache/detail_2350.html)
- [linyuxuanlin/TinyMonitor](https://github.com/linyuxuanlin/TinyMonitor)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
