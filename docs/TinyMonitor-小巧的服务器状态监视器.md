---
id: TinyMonitor-小巧的服务器状态监视器
title: TinyMonitor - 小巧的服务器状态监视器
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261716469.jpg)

TinyMonitor 是一个小巧极简的服务器状态监视终端，它仅由一个 ESP32 主控加上 OLED 显示屏，就可以将服务器的实时状态参数展示出来，方便观察调试。

## 前期准备

本项目用到的硬件物料非常简单，一个自带 Wi-Fi 蓝牙的 Beetle ESP32-C3，还有一块 128x64 的 OLED 屏。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261541993.png)

Beetle ESP32-C3 的引脚定义如下。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261545236.png)

因为可以使用软件 I2C 的方式（即自定义 I2C 引脚）驱动 OLED 屏，所以我将 Beetle ESP32-C3 的 `0`/`1` 引脚定义为 `SCL`/`SDA` 功能。这样一来，接线十分简单，相互贴着把 4 个引脚焊上就完成了。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261546367.png)

注：给 Beetle ESP32-C3 烧录程序前，需要先添加 ESP32 的包，以正常识别板子型号。详见其 [**Wiki 页面**](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)。

### 点亮屏幕

可以使用这个简单的程序，测试能否在 OLED 上正常显示信息：

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

## MQTT 代理服务

MQTT 是一种基于客户端 - 服务器的消息发布 / 订阅传输协议。在本项目中，MQTT 是服务器与 ESP32 通信的桥梁，为了方便，我将 MQTT 服务部署在需要监控的服务器上；如果有需要，你也可以部署在其他的机器上。

### 部署 Mosquitto 服务

Mosquitto 是一款实现了消息推送协议 MQTT v3.1 的开源消息代理软件，在这里我用的是 Docker 方式部署的 [**eclipse-mosquitto**](https://hub.docker.com/_/eclipse-mosquitto) 作为 MQTT 代理服务器。如果不熟悉 Docker 部署的方式，可以参考文章 [**Docker 简易指南**](https://wiki-power.com/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97/) 与 [**Docker Compose - 更优雅的打开方式**](https://wiki-power.com/DockerCompose-%E6%9B%B4%E4%BC%98%E9%9B%85%E7%9A%84%E6%89%93%E5%BC%80%E6%96%B9%E5%BC%8F/)。

根据官方的说明，首先需要创建以下目录和文件供 Mosquitto 使用，并赋予足够的权限：（请将 `${STACK_DIR}` 修改为本地存放数据的路径，例如 `/DATA/AppData/mosquitto`，下文同）

```bash
mkdir -vp ${STACK_DIR}/{config,data,log} \
&& touch ${STACK_DIR}/config/mosquitto.conf \
&& chmod -R 755 ${STACK_DIR} \
&& chmod -R 777 ${STACK_DIR}/log \
```

随后，在 `mosquitto.conf` 文件中写入以下内容：

```conf title="mosquitto.conf"
persistence true
persistence_location /mosquitto/data
log_dest file /mosquitto/log/mosquitto.log

# 关闭匿名模式
allow_anonymous false
# 指定密码文件
password_file /mosquitto/config/pwfile.conf
```

使用 `docker-compose` 方式部署容器：

```yaml title="compose.yaml"
version: "3"
services:
  mosquitto:
    container_name: mosquitto_app
    image: eclipse-mosquitto:1.6.14 # 2.x 版本可能兼容性不佳
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

进入容器并修改密码：

```bash
cd 存放compose.yaml的路径
docker compose up

docker compose ps # 找到运行的容器的ID
docker exec -it 容器ID sh # 进入容器 shell

touch /mosquitto/config/pwfile.conf
chmod -R 755 /mosquitto/config/pwfile.conf

# 创建用户与密码，用户名：test，密码：123
mosquitto_passwd -b /mosquitto/config/pwfile.conf test 123

exit # 退出容器 shell
docker restart 容器ID # 重启容器生效
```

### 测试 MQTT 服务器的可用性

正常启动了 `mosquitto` 服务后，我们可以使用 [**MQTTBox**](https://apps.microsoft.com/store/detail/mqttbox/9NBLGGH55JZG) 测试 MQTT 代理服务器的可用性。

安装软件后，点击 `Create MQTT Client` 新建连接，按照下图填写相关参数：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261456592.png)

其中，`HOST` 为 MQTT 服务所在的服务器的地址（例如，我的服务器在局域网内的地址是 `192.168.1.2`)；用户名和密码需要与上文配置 Mosquitto 时设置的值对应。

点击 `Save` 保存后，如果在顶部状态栏看到绿色的 `Connected`，则表示已经连接上服务器。

## 服务端监控脚本

我们可通过在服务端运行以下 Python 程序，实现对设备实时信息的抓取，并推送到 MQTT 服务器的相应主题上。首先需要安装以下依赖包：

```bash
pip install paho-mqtt psutil
```

创建并运行 Python 程序：

```python title="status-collector.py"
import paho.mqtt.client as mqtt
import psutil
import time

# 连接到 MQTT 代理服务器
client = mqtt.Client()
client.username_pw_set("MQTT用户名", "MQTT密码")
client.connect("MQTT服务器地址", 端口号)
# 例：client.connect("192.168.1.2", 1883)

# 收集服务器状态并发送到 MQTT 主题
while True:
    client.publish("USAGE_CPU", psutil.cpu_percent())
    client.publish("USAGE_MEM", psutil.virtual_memory().percent)
    client.publish("USAGE_DISK", psutil.disk_usage('/').percent)
    time.sleep(1) # 每隔一秒发布一次
```

成功运行后，我们可以在 MQTTBox 顶部状态栏上点击 `Add subscriber` 添加对这三个主题的订阅，例如：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261513642.png)

如果一切正常的话，应该可以在 MQTTBox 中看到不断回传的服务器的状态信息。

## Arduino ESP32 显示端

创建以下 Arduino 代码，修改其中的参数，并烧录进 ESP32。如果一切正常的话，应该可以看到不断更新的状态信息。

```cpp title="Received-from-MQTT-and-Display.ino"
#include <Wire.h>
#include <U8g2lib.h>
#include <WiFi.h>
#include <PubSubClient.h>

// 使用软件 I2C 方式连接 OLED，重新定义引脚
#define OLED_SDA 1
#define OLED_SCL 0

// MQTT 定义
#define WIFI_SSID "Wi-Fi名称"
#define WIFI_PASSWORD "Wi-Fi密码"
#define MQTT_BROKER "MQTT服务器地址" // 例如 192.168.31.2
#define MQTT_PORT MQTT端口 //例如 1883
#define MQTT_USERNAME "MQTT用户名" //test，应与上文配置对应
#define MQTT_PASSWORD "MQTT密码" //123，应与上文配置对应
#define MQTT_TOPIC_CPU "USAGE_CPU" //订阅的主题
#define MQTT_TOPIC_MEM "USAGE_MEM"
#define MQTT_TOPIC_DISK "USAGE_DISK"

char msg_cpu_usage[10];
char msg_mem_usage[10];
char msg_disk_usage[10];

// 定义 OLED 屏幕对象
U8G2_SSD1306_128X64_NONAME_F_SW_I2C u8g2(U8G2_R2, OLED_SCL, OLED_SDA, U8X8_PIN_NONE);

// WIFI 客户端对象
WiFiClient wifiClient;
PubSubClient mqttClient(wifiClient);

// MQTT 回调函数
void mqttCallback(char* topic, byte* payload, unsigned int length) {
  if (strcmp(topic, MQTT_TOPIC_CPU) == 0) {
    // 记录 CPU 使用率
    for (int i = 0; i < length; i++)
      msg_cpu_usage[i] = (char)payload[i];
  } else if (strcmp(topic, MQTT_TOPIC_MEM) == 0) {
    // 记录内存使用率
    for (int i = 0; i < length; i++)
      msg_mem_usage[i] = (char)payload[i];
  } else if (strcmp(topic, MQTT_TOPIC_DISK) == 0) {
    // 记录磁盘使用率
    for (int i = 0; i < length; i++)
      msg_disk_usage[i] = (char)payload[i];
  }
}

void setup() {
  u8g2.begin();  // 初始化 OLED 屏幕
  Wire.begin();  // 开始 I2C 传输

  // 连接 WIFI
  WiFi.begin(WIFI_SSID, WIFI_PASSWORD);
  while (WiFi.status() != WL_CONNECTED) {
    delay(1000);
  }

  // 连接 MQTT 代理服务器
  mqttClient.setServer(MQTT_BROKER, MQTT_PORT);
  mqttClient.setCallback(mqttCallback);
  if (mqttClient.connect("ESP32", MQTT_USERNAME, MQTT_PASSWORD)) {
    mqttClient.subscribe(MQTT_TOPIC_CPU);
    mqttClient.subscribe(MQTT_TOPIC_MEM);
    mqttClient.subscribe(MQTT_TOPIC_DISK);
  }
}

void loop() {
  mqttClient.loop();  // 处理 MQTT 消息
  u8g2.firstPage();
  do {
    u8g2.setFont(u8g2_font_9x15_tf);

    // 显示 CPU 使用率
    u8g2.setCursor(0, 12);
    u8g2.print("CPU: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_cpu_usage[i]);
    u8g2.print(" %");

    // 显示内存使用率
    u8g2.setCursor(0, 35);
    u8g2.print("Mem: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_mem_usage[i]);
    u8g2.print(" %");

    // 显示磁盘使用率
    u8g2.setCursor(0, 58);
    u8g2.print("Disk: ");
    for (int i = 0; i < 9; i++)
      u8g2.print(msg_disk_usage[i]);
    u8g2.print(" %");

  } while (u8g2.nextPage());
}
```

## 更多扩展玩法

以下的想法有待实现：

- 增加电池和 3D 打印的外壳，做成更精致的桌面小摆件
- 增加内网穿透，打造为小挂件，不在家也可观察服务器状态
- 将 Python 监测程序封装为 Docker 方式部署
- 优化 UI 布局，实现更多参数监控
- 增加多服务器状态监控功能
- 增加某些参数超出阈值报警的功能

附：Beetle ESP32-C3 与 Seeed XIAO ESP32C3 的合照。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202305261719170.jpg)

## 参考与致谢

- [DFRobot Wiki · Beetle ESP32 C3](https://wiki.dfrobot.com.cn/_SKU_DFR0868_Beetle_ESP32_C3)
- [基于 Arduino 和 MQTT 打造一款树莓派性能监控系统](https://www.zhihu.com/tardis/zm/art/463880669?source_id=1003)
- [eclipse-mosquitto](https://hub.docker.com/_/eclipse-mosquitto)
- [Docker - 通过容器安装部署 Mosquitto 服务教程（MQTT 服务器）](https://www.hangge.com/blog/cache/detail_2896.html)
- [MQTT 系列教程 3（客户端工具 MQTTBox 的安装和使用）](https://www.hangge.com/blog/cache/detail_2350.html)
- [linyuxuanlin/TinyMonitor](https://github.com/linyuxuanlin/TinyMonitor)


> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
