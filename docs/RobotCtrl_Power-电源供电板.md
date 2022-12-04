---
id: RobotCtrl_Power-电源供电板
title: RobotCtrl_Power - 电源供电板
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527113517.png)

项目仓库：[**linyuxuanlin/RobotCtrl/RobotCtrl_Power**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power)

项目在线预览：

<div class="iframe_viewer">
    <iframe 
    scrolling="no"
  src="https://viewer.wiki-power.com/RobotCtrl_Power.html"
></iframe>
</div>

注：项目包含于 [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6)。

## 原理图设计

RobotCtrl_Power 的主要功能如下：

- 24V 电源输入（理论可以 15-40V）
- 电池电源转 12V/5A 稳压器（带使能开关与指示灯）
- 电池电源转 5V/5A 稳压器（带使能开关与指示灯）
- 防反接保护（P-MOS）
- 过压保护（大于 30V 开始保护）
- 电池电源输出、12V 电源输出、5V 电源输出接口

### 电源输入

电源输入选用了两个 XT60PW-M 座子，做双电源备份输入（也可以作为一个输入一个输出使用），并提供两排排针供输出测试。

防反接功能使用 P-MOS 实现，虽然 XT60 是防呆设计，但还是需要防止正负电源线焊反的情况。反接时，P-MOS 不会导通，电源不会灌入系统。防反接功能的设计可参考文章 [**防反接电路的设计**](https://wiki-power.com/%E9%98%B2%E5%8F%8D%E6%8E%A5%E7%94%B5%E8%B7%AF%E7%9A%84%E8%AE%BE%E8%AE%A1)。

瞬时过压保护与 ESD 防护，使用的是 TVS 管，当接入大于 30V 时，它将分走多余的电压保护后置系统。

### 12V 与 5V 稳压电路

12V 与 5V 稳压电路选用的是两路 TI 的 LMR14050 DC-DC Buck 方案，每一路最高能带 5A 电流。具体设计可参考文章 [**电源方案（Buck）- LMR14050**](https://wiki-power.com/%E7%94%B5%E6%BA%90%E6%96%B9%E6%A1%88%EF%BC%88Buck%EF%BC%89-LMR14050)。

另外，每一路都增加了使能开关和电源指示灯。

### 电源输出端口

VBAT、12V、5V 输出各自使用一对 4pin 排针，12V 输出额外增加 KF2EDGR-3.81 座子为特殊传感器提供供电。

## PCB 设计

RobotCtrl_Power 的 PCB layout，需要注意反馈网络的上下分压电阻需要尽量靠近芯片的 FB 引脚，Vout 采样路径应尽量原理噪声产生路径（电感二极管环路），最好是通过过孔走屏蔽层后的层；电感应该靠近 SW 引脚放置，以降低磁噪声和静电噪声；二极管、输入和输出电容的接地节点应尽可能小，最好是仅在一个点连接到系统阶地层，以最大限度减少系统接地层中的传导噪声；输出电容应尽量靠近电感和二极管的节点放置，且走线尽可能短而粗，以降低传导和辐射噪声，提高效率。

RobotCtrl_Power 的 PCB 顶层和底层走信号和电源，中间插入两层地平面以增强信号与电源完整性。

## 硬件测试

- 防反接测试：输入电压反接时是否可不开启系统。
- 使能开关与电源指示灯：测试是否可以正常运行。
- 输出：测试 12V/5V 输出是否达标，以及纹波大小。

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

