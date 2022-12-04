---
id: SWD与JTAG的区别与联系
title: SWD 与 JTAG 的区别与联系
---


众所周知，SWD 和 JTAG 是单片机下载程序与调试的常用接口。其共同之处：

- **供电电压范围**: 1.2 V - 5.5 V
- **时钟速率**: 可配置高达 10 MHz
- **SWO 跟踪捕获**: 数据速率高达 50 Mbit/s（UART/NRZ 模式）
- **隔离电压**: 1 kV
- **热插拔**：支持

## JTAG

JTAG，全名为 Joint Test Action Group（联合测试行动小组）。截至本文最新的标准为 IEEE Standard 1149.1-1990.

其拓扑图（菊花链）如下：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210209191921.png)

JTAG 一般使用 5 个引脚：

- **TDI**（Test Data In）：串行输入引脚
- **TDO**（Test Data Out）：串行输出引脚
- **TCK**（Test Clock）：时钟引脚，一般附加 100k 下拉电阻
- **TMS**（Test Mode Select）：模式选择（控制信号）引脚
- **TRST**（Test Reset）：复位引脚


JTAG 的优势：

- 不限于 ARM 系列芯片
- 具有更多用于编程，调试和生产测试的用途

## SWD

全称为 Serial Wire Debug（串行线调试），是 ARM 专门设计的协议，仅支持 ARM（所以在 ARM 系列单片机中性能表现较佳）。

SWD 一般使用 2 个引脚：

- **SWDIO**（Serial Wire Data Input Output）：串行数据输入输出引脚
- **SWCLK**（Serial Wire Clock）：串行线时钟引脚

SWD 的优势：

- 使用引脚更少，只需 SWDIO 和 SWCLK 两个引脚
- SWD 具有特殊功能，例如打印调试信息
- 与 JTAG 相比，SWD 在速度上具有更好的整体性能

## JTAG 与 SWD 的兼容性

一般来说，单片机板子上会有以下这些烧录座，可同时兼容 JTAG 与 SWD：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210210122923.jpg)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210210123714.png)

- TCK 兼容 SWCLK
- TMS 兼容 SWDIO
- （TDO 兼容 SWO）

选用 SWD 而非 JTAG 的理由：

- 电路原理图设计需要足够简单，且可以在没有 JTAG 功能的情况下进行测试
- PCB 在尺寸方面有限制，SWD 可以节省空间
- MCU 已经没有多余的引脚给 JTAG 用了

## 参考与致谢 

- [下载调试接口 SWD 和 JTAG 的区别](https://mp.weixin.qq.com/s/MW57t266yvv6TOweeFEUVA)
- [Cortex JTAG，SWD Debug Port Sharing](https://southlife.tistory.com/107)
- [JTAG/SWD Interface](https://www.keil.com/support/man/docs/ulinkplus/ulinkplus_jtagswd_interface.htm)
- [JTAG](https://en.wikipedia.org/wiki/JTAG)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

