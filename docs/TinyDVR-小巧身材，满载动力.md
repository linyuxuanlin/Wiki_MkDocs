---
id: TinyDVR-小巧身材，满载动力
title: TinyDVR - 小巧身材，满载动力
---

—— 基于 TinyDVR Master V1.1 & Slave V7.2 Release

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191345.jpg)

TinyDVR 是一款电机驱动套件，包含母板（Master）与子板（Slave），供电部分与驱动部分分离，相比前身 ZenDriver 大幅度缩减了体积，极大提升了可拓展性。你可以根据自己的需求，堆叠不同数量的子板，驱动 n 个电机。

项目仓库：[**linyuxuanlin/TinyDVR**](https://github.com/linyuxuanlin/TinyDVR)

项目在线预览：

**TinyDVR_Master**：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/TinyDVR_Master.html"
></iframe>
</div>

**TinyDVR_Slave**：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/TinyDVR_Slave.html"
></iframe>
</div>

## 基本参数

1. 输入电压：**7.2 ~ 20 V**
2. 输出电流：**0 ~ 68 A**
3. 提供 **5V / 3A** 的电源输出，可供控制器及其他模块使用
4. 保护装置：集成防反接、光耦隔离电路
5. 电机简便接插：对市面上通用的直流减速电机（带编码器），可直接用 6 pin 排线接插（免对线）
6. 可拓展：一块母板可堆叠 n 块子板，实现 n 路电机驱动

## 接口定义

### TinyDVR Master

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191439.png)

### TinyDVR Slave

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191457.png)

背面引脚详解：

- \+ ：提供 5V / 3A 的电源输出
- 1 ：IN1 端口，输入 PWM 信号 1
- 2 ：IN2 端口，输入 PWM 信号 2
- A : 编码器 A 相信号端口
- B : 编码器 B 相信号端口
- \- ：GND

## 使用指南

### 测试方法

1. 接入 **7.2 ~ 20 V** 电池供电
2. 在对应的子板处接上电机
3. 用 **5V** 供电口分别接 **IN1/ IN2** 端口，此时电机将 **正 / 反转**

### 连接单片机

4. 接入 **7.2 ~ 20 V** 电池供电
5. 在对应的子板处接上电机
6. 共地（驱动板 GND 接单片机 GND）
7. IN1，IN2 端口接单片机对应 PWM 端口（代码内设置）
8. 测试方法：请见项目仓库内的测试例程

## 花絮

早期子板：
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182442.jpg)

批量焊接：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182441.jpg)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

