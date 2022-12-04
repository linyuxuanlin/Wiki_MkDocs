---
id: RobotCtrl_Core-核心板
title: RobotCtrl_Core - 核心板
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527113423.png)

项目仓库：[**linyuxuanlin/RobotCtrl/RobotCtrl_Core**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core)

项目在线预览：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/RobotCtrl_Core.html"
></iframe>
</div>

注：项目包含于 [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6)。

## 原理图设计

RobotCtrl_Core 的主要功能如下：

- 供电稳压电路（5V 转 3.3V，引出测试点）
- 单片机最小系统
  - 电源电路（供电去耦、ADC 模拟电源）
  - 复位电路（外部复位按键）
  - 时钟电路（HSE 无源晶振）
  - 下载调试接口（SW）
  - 启动模式（选择从主闪存存储器启动）
  - USB 供电与通信电路（USB-Micro）
- B2B 连接器（引出所有 IO）
- 板载外设

### 供电电路

RobotCtrl_Core 可由 USB 接口或 B2B 连接器输入 5V 电源，并转换为 3.3V 供单片机核心及板载外设使用。稳压电路使用了 LDO（AMS1117-3.3，最大电流为 1A），附带了一颗电源指示灯，并预留了关键测试点。

LDO 的基础原理可以参考文章 [**电源拓扑 - 线性稳压**](https://wiki-power.com/%E7%94%B5%E6%BA%90%E6%8B%93%E6%89%91-%E7%BA%BF%E6%80%A7%E7%A8%B3%E5%8E%8B)。

### 单片机最小系统

单片机最小系统的设计，分为几个部分：供电、复位、下载调试、时钟、启动模式。基础知识可参考文章 [**如何设计一款单片机的最小系统**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E8%AE%BE%E8%AE%A1%E4%B8%80%E6%AC%BE%E5%8D%95%E7%89%87%E6%9C%BA%E7%9A%84%E6%9C%80%E5%B0%8F%E7%B3%BB%E7%BB%9F) 和 [**STM32F4 硬件开发**](https://wiki-power.com/STM32F4%E7%A1%AC%E4%BB%B6%E5%BC%80%E5%8F%91)。

### 电源电路

去耦电容：

- VDD：总的一个 10 μF 的陶瓷电容，外加每个 VDD 引脚旁接一个 100 nF 陶瓷电容。
- VDDA：100 nF 陶瓷电容 + 1 µF 陶瓷电容。

VCAP 电容

- 各对地接一个 2.2 µF 陶瓷电容。

### 复位电路

启用电源监控器，即 PDR_ON 通过 120Ω 电阻上拉。除此之外，也添加了复位按键，带硬件防抖。

### 时钟电路

外部高速时钟（HSE）选用村田 8M 无源晶振。

### 下载调试接口

本设计直接引出下载调试接口，不需要外部上拉／下拉电阻（因为 STM32 内部有集成）。

### 启动模式

选择从主闪存存储器启动，即 BOOT0 串接 10 K 的下拉电阻，BOOT1 任意。

### USB 供电与通信电路（USB-Micro）

STM32 有内置 USB 外设，只需要直接引出接口（在 STM32F07ZE 芯片上是 PA11 和 PA12）就可以实现 USB 通信。

USB 接口也支持了外部供电功能（VUSB）。

## B2B 连接器

B2B 连接器选用正点原子的 3710 系列，RobotCtrl_Core 核心板使用一对 3710M060037G3FT01（公座），RobotCtrl_Func 拓展板使用一对 F060037G0FR01（母座）进行配合。一对 B2B（共 120 pin）足以将 STM32F407ZE 的所有 IO 完全引出使用，最大化利用了系统资源。

B2B 连接器的相关资料请参考 [**3710F 端子资料**](http://www.openedv.com/thread-78182-1-1.html)

## 用户按键与 LED

为了能够进行简单的验证调试，RobotCtrl_Core 板载了一颗用户按键与一颗用户 LED，按键配置为 GPIO 输入模式、内部上拉，并加一个 MLCC 电容以硬件抖动。LED 配置为 GPIO 输出模式，引脚置高电平点亮，中间串联一个电阻以限流。

具体引脚请参考原理图。

## 硬件测试

电源测试需要在 USB 座子接入 5V 供电（或者通过 B2B 连接器通过外设拓展版供电），在 3.3V 的测试点测得相应电压即可。实际测试为 3.32V，验证通过。

功能测试通过烧录初始程序（用户按键控制用户 LED），测试上电及程序的烧录、复位按键与用户按键、电源 LED 与用户 LED、USB 功能。在实际的测试中，初始程序可正常通过 ST-Link 烧录进单片机核心板。复位按键可正常复位系统；在测试程序中，可以通过用户按键点亮/关闭用户 LED；上电时，电源 LED 正常亮起。USB 功能测试，使用的是 USB 虚拟串口的程序，打开串口工具（波特率任意），发送任意字符，将返回相同字符，测试通过。

## 参考与致谢

- [STM32 的 PDR_ON 引脚，比较好的解释（转载+补充）](https://blog.csdn.net/Frankenstien_/article/details/105971841)
- [正点原子【STM32-F407 探索者】第五十六章 USB 读卡器(Slave)实验](https://zhuanlan.zhihu.com/p/136163591)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

