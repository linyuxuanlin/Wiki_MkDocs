---
id: TIC基础知识
title: TIC 基础知识
---

在半导体测试中，**TIC（Test Interface Controller，测试接口控制器）** 是一个总线主控器，它遵循的是 **AMBA（Advanced Microcontroller Bus Architecture，高级微控制器总线架构）** 规范中的 **Test Interface** 协议。AMBA 是嵌入式微控制器的片上通信标准，囊括三类总线协议：

- **AHB**（the Advanced High-performance Bus，高性能总线）
- **ASB**（the Advanced System Bus，系统总线）
- **APB**（the Advanced Peripheral Bus，外设总线）

因为 AMBA 的理念是对系统中的单个模块进行隔离测试，每个模块的测试只依赖于总线接口，所以需要有一种测试方法，对没有接到总线的外设上的输入输出进行测试。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262214877.png)

这种测试方法可通过 Test Interface 实现。它采用简单的三线握手机制，以控制 Vector 的读写；使用 **EBI（External Bus Interface，外部总线接口）** 作为数据路径，将外部的 Vector 导入内部总线。

## Test Interface 的引脚

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262225257.png)

由上图可见，Test Interface 的引脚由三个部分组成：

- 一个时钟引脚 **TCLK**
- 三个控制引脚 **TREQA**，**TREQB** 和 **TACK**
- 一个 32 位的测试总线 **TBUS[31:0]**

Test Interface 最小只需要 TREQA 和 TACK 作为 **专用引脚**，来控制测试模式的进入与退出。其他引脚都可以通过复用设备上的引脚来实现。

**TREQA/TREQB（Test Bus Request，测试总线请求）** 是 **输入** 信号。在系统正常运行其间，TREQA 用于请求进入测试模式，允许 Vector 被加载进来。在测试过程中，TREQA 与 TREQB 结合使用，以指示下一个 Cycle 将使用的 Vector 类型。

**TACK（Test Bus Acknowledge，测试总线确认）** 是一个 **输出** 信号。TACK 用于表示总线的状态，也指示一个测试项何时完成。当 TACK 输出低电平时，表示当前 Vector 需要更多时间，直到 TACK 变为高电平。只有当 TACK 为高电平时，TREQA/TREQB 才会对外部控制信号进行读取。

当系统正常运行时， TACK 与 TREQA/TREQB 的真值表如下：

| TREQA | TREQB | TACK | 状态                     |
| ----- | ----- | ---- | ------------------------ |
| 0     | 0     | 0    | 正常运行，未进入测试模式 |
| 1     | 0     | 0    | 请求进入测试模式         |
| 0     | 1     | 0    | 预留，用于外部主机请求   |
| -     | -     | 1    | 已进入测试模式           |

进入到测试模式后，三线的信号与对应的系统状态如下：

| TREQA | TREQB | TACK | 状态                              |
| ----- | ----- | ---- | --------------------------------- |
| -     | -     | 0    | 当前测试模式访问有问题            |
| 1     | 1     | 1    | Address/Control/Turnaround Vector |
| 1     | 0     | 1    | Write Vector                      |
| 0     | 1     | 1    | Read Vector                       |
| 0     | 0     | 1    | 退出测试模式                      |

**TCLK（Test Clock）** 是一个时钟信号输入。Test Interface 的测试时钟是由外部提供的。在普通模式与测试模式之间切换时，要求 TCLK 时钟不能有毛刺。

**TBUS[31:0]（Test Bus）** 是一个 32 位双向测试接口总线。当它处于输入状态时，用于应用 Vector 地址、控制和写入 Vector；当处于输出状态时，可以用来读取 Vector。当需要改变 TBUS 输入输出状态时，测试总线协议确保提供一个用于换向的 Cycle。

## Vector 的类型

在测试接口中，Vector 的类型有 5 种：

- Address Vector：声明地址的 Vector
- Write Vector：写入的 Vector（0/1）
- Read Vector：读取的 Vector（L/H）
- Control Vector：控制的 Vector
- Turnaround Vector：换向 Vector

其中，Address/Control/Turnaround Vector 均由相同的 TREQA/TREQB 共同值决定。

判断 Vector 的类型，可以参考以下的规则：

- 只出现一条 Address/Control/Turnaround Vector：它就是一条 Address Vector。
- 出现连续一串 Address/Control/Turnaround Vector：除了最后一条是 Control Vector，其他全是 Address Vector。
- 一条 / 一串 Read Vector 之后：总会跟一个 Turnaround Vector。（在 ASB 中是单个，AHB 中需要两个）

## 参考与致谢

- _IHI0011 - ARM advanced microcontroller bus architecture (AMBA) specification.Rev 2.0_

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
