---
id: 电源方案（LDO）-XC6206
title: 电源方案（LDO）- XC6206
---

XC6206 系列是高精度、低功耗的三端正电压调节器，提供大电流和极小的压差电压，内部由限流电路、驱动晶体管、精密基准电压和纠错电路组成。该系列兼容低 ESR 陶瓷电容。输出电压可以在 1.2V 至 5.0V 范围内以 0.1V 为增量进行选择。

本篇选用的是 TOREX（特瑞仕）的 XC6206 系列，SOT-23 封装，其他厂商相同型号可替代，但请校对详细参数。

项目仓库： [**Collection_of_Power_Module_Design/LDO/XC6206**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/LDO/XC6206)

## 主要特性

- 最大输出电流：200mA（典型值 6.0V 下）
- 压差电压：250mV@100mA（典型值 6.0V 下）
- 最大工作电压：6.0V
- 输出电压范围：1.2V ~ 5.0V（0.1V 增量）
- 精度：当 Vout<1.5V 时，精度 ±30mV；当 Vout>1.5V 时，精度 ±2%；当 Vout>2V 时，精度 ±1%
- 低功耗：典型值 1.0uA
- 保护电路：内置限流电路
- 工作温度：-40℃~ +85℃
- 可选封装：SOT-23、SOT-89、USP-6B

## 选型说明

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420102910.png)

## 典型应用电路

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420102323.png)

## 内部功能框图

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420102514.png)

注：框图内的二极管为 ESD 或寄生二极管。

## 引脚定义

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420103005.png)

| 引脚名称 | 引脚描述 |
| -------- | -------- |
| VSS      | 地       |
| Vin      | 电源输入 |
| Vout     | 电源输出 |

## 特性描述

各型号的具体参数表：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420103738.png)

## 参考与致谢

- [XC6206_Datasheet](https://www.torexsemi.com/file/xc6206/XC6206.pdf)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

