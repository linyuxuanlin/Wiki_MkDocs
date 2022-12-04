---
id: T-Clock桌上小钟
title: T-Clock 桌上小钟
---

## 准备材料

1. **NodeMCU**：基于 ESP8266
2. **OLED**：128x64 分辨率，I2C 接口（SPI 请见参考链接）

## 接线

| OLED | NodeMCU |
| :--: | :-----: |
| GND  |   GND   |
| VCC  |  3.3V   |
| SCL  |   D1    |
| SDA  |   D2    |

## 例程

### API 配置

1. 在 [**心知天气**](https://www.seniverse.com/) 注册账户
2. 在控制台内添加新产品（选择免费版即可）
3. 复制 API 私钥

### 包含库文件

- [**Adafruit_SSD1306.h**](https://github.com/adafruit/Adafruit_SSD1306)

### 最终例程

- [**T-Clock/Software/Codes/Weather_Clock_OLED_I2C**](https://github.com/linyuxuanlin/T-Clock/tree/master/Software/Codes/Weather_Clock_OLED_I2C)

注：需将 WiFi 名称及密码、城市、私钥改为你自己的。  
如果编译出现错误，且错误信息定位在 `#error("Height incorrect, please fix Adafruit_SSD1306.h!");`，则需打开库文件 `Adafruit_SSD1306.h`，将 `#define SSD1306_128_32` 改为 `#define SSD1306_128_64`。

注：定制硬件项目正在路上~

## 参考与致谢

- [T-Clock 桌上小钟（旧）](https://wiki-power.com/unlist/T-Clock桌上小钟（旧）)
- [心知天气](https://www.seniverse.com/)
- [ESP8266 接入心知天气 API【程序＋详细讲解】](https://www.bilibili.com/video/av89935868/?spm_id_from=333.788.b_636f6d6d656e74.4)
- [ESP8266 ＋ OLED = 网络时钟和未来 3 日天气预报](https://www.bilibili.com/video/av88920975/)
- [My_ESP8266/心知天气](https://gitee.com/young_people_only_love_her/My_ESP8266/tree/master/%E5%BF%83%E7%9F%A5%E5%A4%A9%E6%B0%94)
- [OLED Graphic Display Interfacing with NodeMCU](https://www.electronicwings.com/nodemcu/oled-graphic-display-interfacing-with-nodemcu)
- [adafruit/Adafruit_SSD1306](https://github.com/adafruit/Adafruit_SSD1306)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

