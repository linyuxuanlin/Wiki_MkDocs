---
id: ZenDriver-高性能的电机驱动
title: ZenDriver - 高性能的电机驱动
---

—— 基于 V5.1 Release 版本

项目仓库：[**linyuxuanlin/ZenDriver**](https://github.com/linyuxuanlin/ZenDriver)

## 基本参数

1. 输入电压：**7.2 ~ 20 V**
2. 输出电流：**0 ~ 68 A**
3. 提供 **5V 1.5A** 的电源输出，可供控制器使用
4. 保护装置：集成防反接、光耦隔离电路

## 接口定义

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125192433.png)

**电机端** 从左到右依次为：**M-，5V，编码器 A，编码器 B，GND，M+** ，对应电机引脚，可以直接怼电机上去。

**信号端** 从右到左依次为：**GND，编码器 B，编码器 A，IN2，IN1，5V** 。注意：5V 端口 **可提供电源给单片机用** （最大 1.5 A）。

**电源输入端** 三个接口通用，一般建议中间的接电池，旁边的两个接口用于拓展电源给其他的驱动板。

## 使用指南

### 直接供电测试

1. 接入 **7.2 ~ 20 V** 电池供电
2. 接上电机
3. 用 **信号端** 上的 **5V** 分别接 **IN1，IN2**，此时电机将正、反转

### 连接单片机测试

1. 接入 **7.2 ~ 20 V** 电池供电
2. 接上电机
3. **信号端 GND** 接 **单片机 GND**，**5V 端口** 接 **单片机** **5V**
4. 引脚 **IN1，IN2** 接单片机 PWM 端口
5. 用代码调试

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125192734.png)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

