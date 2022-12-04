---
id: RobotCtrl_Func-外设拓展板
title: RobotCtrl_Func - 外设拓展板
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527113505.png)

项目仓库：[**linyuxuanlin/RobotCtrl/RobotCtrl_Func**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func)

项目在线预览：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/RobotCtrl_Func.html"
></iframe>
</div>

注：项目包含于 [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6)。

## 原理图设计

RobotCtrl_Func 的主要功能如下：

- 12V 电源输入，5V 电源输入 / 输出，3.3V 电源输出（引出测试点）
- 5V 转 3.3V 供电稳压电路 \* 2（供传感器 / 以太网，引出测试点）
- 以太网通信电路
- CAN 通信电路 \* 2
- 串口通信电路（RS-232 与 TTL 电平）
- 蜂鸣器电路
- 用户按键 \* 2
- 用户 LED \* 3
- MPU6050 姿态传感器模块
- 红外测距传感器接口 \* 4
- 超声波接口 \* 5
- 用户 GPIO 接口 \* 6
- B2B 连接器（引出所有 IO）
- SW 下载接口

### 电源

RobotCtrl_Func 板载 2 路 LDO，原理与 RobotCtrl_Core 中相似，其中一路供外设传感器使用，另一路供以太网电路单独使用。

### 以太网通信电路

以太网通信基于以太网 PHY 芯片，使用 RMII 接口与单片机通信，通过内置隔离变压器的 RJ45 网口外接网线通信。以太网电路的时钟采用外部 25M 无源晶振，且需要独立供电以减小电源干扰，这里使用了与核心板相同的低压差线性稳压器供电方案，为以太网电路单独供电。以太网通信的原理可以参考文章 [**HAL 库开发笔记 - 以太网通信（LwIP）**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%BB%A5%E5%A4%AA%E7%BD%91%E9%80%9A%E4%BF%A1%EF%BC%88LwIP%EF%BC%89)。

### CAN 通信电路

CAN 通信电路基于 CAN 收发芯片搭建，通过 CAN 差分电平传输。CAN 协议控制器（例如单片机）通过串行线（RX/TX）连接到收发器，在收发器上转换为 CAN 信号（CANH/CANL），并通过 RS 引脚来选择高速 / 静音模式。CAN 总线上需加 120Ω 末端电阻，以匹配阻抗，减少信号的反射。CAN 通信的原理可参考文章 [**通信协议 - CAN**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-CAN) 与 [**HAL 库开发笔记 - 串口通信**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-CAN%E9%80%9A%E4%BF%A1)。

### 串口通信电路

RobotCtrl_Func 板载了 RS-232 电平的串口通信电路，并额外引出了 TTL 电平的 USART1/UART5。串口通信的原理可参考文章 [**通信协议 - 串口通信**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1) 与 [**HAL 库开发笔记 - 串口通信**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1)。

RS-232 通信电路是采用 TTL 转 232 电平的芯片，将单片机的 TTL 转换为 RS-232 电平。为提高 EMC 性能，DB9 座子外壳连接引脚可对地接 TVS 二极管，TTL 转 232 芯片需要外加电源去耦与自举电容。

### 蜂鸣器电路

蜂鸣器电路选用的是 12V 蜂鸣器，用一个三极管即可控制。

### 用户按键与 LED

用户按键与 LED 原理可参考 RobotCtrl_Core，此处不多赘述。

### 姿态传感器模块

直接贴装 MPU6050 模块使用，预留 I2C 接口与单片机进行通信。I2C 通信的原理可参考文章 [**通信协议 - I2C**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C) 与 [**HAL 库开发笔记 - I2C 通信（MPU6050）**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-I2C%E9%80%9A%E4%BF%A1%EF%BC%88MPU6050%EF%BC%89)。

### 红外测距传感器接口

四路红外测距传感器接口电路因红外传感器使用的是 12V 供电与信号（NPN 常开型），所以从 RobotCtrl_Power 引出 12V 为其供电，并加上四路光耦隔离芯片，以传输高低电平信号。光耦隔离电路的设计，需要根据电流的大小，计算限流电阻的阻值，确保在数据手册规定的触发电压范围内即可。光电耦合器的原理可以参考文章 [**基本元器件 - 光电耦合器**](https://wiki-power.com/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E5%85%89%E7%94%B5%E8%80%A6%E5%90%88%E5%99%A8)。

### 电源输入接口与 B2B 连接器

外设拓展板的电源输入接口为 4 个排针，用于与底部的电源供电板相连接。B2B 连接器用于为主控板供电及数据通信。

## 硬件测试

### 电源测试

电源输入（以下测试项目都需按照此操作连接电源）：

- VCC_12V：通过 P1 输入。
- VCC_5V：通过 P2 或 J1_1/2 输入。
- GND：通过 P3、P4、J1_31/32 或 J2_30/31 与外界共地。

5V 转 3.3V 稳压（供传感器）：

- VCC_3V3S：测量 C30 两端电压是否为 3.3V。

5V 转 3.3V 稳压（供以太网）：

- VCC_3V3E：测量 C26 两端电压是否为 3.3V。

### 板载传感器测试

用户按键：

- 配置 PE2/PE3 为 GPIO 上拉输入模式，按下按键读取到低电平，松开为高。

用户 LED：

- 配置 PC6/PC7/PC8 为 GPIO 输出模式，输出高电平，LED 依次点亮；输出低电平熄灭。

MPU6050 姿态传感器模块：

- 测量 M1 模块 1 号引脚对地是否为 VCC_3V3S 电压。
- 测试 IO 引脚连通性。

蜂鸣器：

- 测量 BUZZER1 正极对地是否为 VCC_12V 电压。
- 配置 PC9 为 GPIO 输出模式，输出高电平，蜂鸣器发出声音；输出低电平不发出声音。

串口转 RS232：

- 测量 C3 两端是否为 VCC_3V3S 电压。
- 运行测试程序，通过 PB10/PB11 引脚进行测试。

CAN 总线通信：

- 测量 C10/C13 两端是否为 VCC_5V 电压。
- 运行测试程序（回环测试），通过 PD0/PD1、PB12/PB13 引脚进行测试。

以太网通信：

- 测量 IC2_9 对地是否为 VCC_3V3S 电压。
- 测量 VDD1A/VDD2A 对地是否为 VCC_3V3E 电压。
- 运行测试程序，通过 RMII 接口对以太网通信进行测试。

### 接口测试

红外测距传感器接口：

- 分别测量 J16/J17/J18/J19 座子的 1 号引脚对地是否为 VCC_12V 电压。
- 配置 PF2/PF3/PF4/PF5 为 GPIO 下拉输入，外部使得 IR1/IR2/IR3/IR4 分别为高电平（VCC_12V），则 PF2/PF3/PF4/PF5 读取到高电平；反之为低电平。

超声波接口：

- 分别测量 J3/J4/J5/J6/J7 座子的 4 号引脚对地是否为 VCC_3V3S 电压。
- 测试 IO 引脚连通性。

用户 GPIO 接口：

- 分别测量 J9/J10/J11 座子的 4 号引脚对地是否为 VCC_3V3S 电压。
- 测试 IO 引脚连通性。

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

