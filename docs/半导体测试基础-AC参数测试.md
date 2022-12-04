---
id: 半导体测试基础-AC参数测试
title: 半导体测试基础 - AC 参数测试
---

AC 测试确保 DUT 的时特性序满足其规格需求。

## 基本 AC 参数

### 建立时间（Setup Time）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094845.png)

建立时间指的是在参考信号（图中为 `WE`）发生变化（取中间值 1.5V）前，为了确保能被正确读取，数据（图中为 `DATA IN`）必须提前保持稳定不变的最短时间。在最小建立时间之前，数据可以随意变化，但如果超过了最小建立时间（保持稳定得太晚），就有可能无法被识别，导致错误。在规格书中的表示如下：

| Parameter | Description              | Min | Max | Unit |
| --------- | ------------------------ | --- | --- | ---- |
| $t_{SD}$  | Data Set-Up to Write End | 11  |     | ns   |

### 保持时间（Hold Time）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094858.png)

保持时间指的是参考信号（图中为 `WE`）发生变化（到达一定电压阈值）后，为了确保无误，数据（图中为 `DATA IN`）必须保持稳定持续的最短时间（或者说在时钟信号触发前多久要保持稳定电平）。如果保持时间太短，数据有概率不能被正确识别。在规格书中的表示如下：

| Parameter | Description              | Min | Max | Unit |
| --------- | ------------------------ | --- | --- | ---- |
| $t_{HD}$  | Data Hold from Write End | 1   |     | ns   |

### 传播时延（Propagation Delay）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094910.png)

传播时延指的是一个信号的传输和另一个相关信号的传输之间的时间间隔。大多时候测量的是输入信号（图中为 `ADDR`）发生变化，到相应输出（图中为 `DATA OUT`）反应之间的时间间隔（从输入端到输出端所需的时间）。它保证了输出信号可在输入信号出现后多久内出现。在规格书中的表示如下：

| Parameter | Description           | Min | Max | Unit |
| --------- | --------------------- | --- | --- | ---- |
| $t_{AA}$  | Address to Data Valid |     | 15  | ns   |

### 最小脉宽（Minimum Pulse Widths）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094924.png)

最小脉宽通常包含最小低脉冲宽度和最小高脉冲宽度，用于确保脉冲定时时的最小可操作的值。在规格书中的表示如下：

| Parameter | Description             | Min | Max | Unit |
| --------- | ----------------------- | --- | --- | ---- |
| $t_{WL}$  | Minimum clock low time  | 20  |     | ns   |
| $t_{WH}$  | Minimum clock high time | 25  |     | ns   |

### 最大频率（Maximum Frequency）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094934.png)

最大工作频率通俗地讲，就是设备可运行的最大速度。在规格书中的表示如下：

| Parameter | Description             | Min | Max  | Unit |
| --------- | ----------------------- | --- | ---- | ---- |
| $f_{MAX}$ | Maximum clock frequency |     | 22.2 | MHz  |

### 输出使能时间（Output Enable Time）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094941.png)

指的是引脚从高阻状态（关断失能）切换到有效驱动电平（高低电平）状态所需的时间，确保输出 Buffer 可以在规定的时间内改变引脚状态。测量时计算从控制信号发出到检测到开关输出的时间间隔。在规格书中的表示如下：

| Parameter | Description          | Min | Max | Unit |
| --------- | -------------------- | --- | --- | ---- |
| $t_{DOE}$ | OE LOW to Data Valid |     | 10  | ns   |

### 输出失能时间（Output Disable Time）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094948.png)

指的是引脚从有效驱动电平（高低电平）状态切换到高阻状态（关断失能）所需的时间，确保输出 Buffer 可以在规定的时间内改变引脚状态。测量时计算从控制信号发出到检测到开关输出的时间间隔。在规格书中的表示如下：

| Parameter  | Description           | Min | Max | Unit |
| ---------- | --------------------- | --- | --- | ---- |
| $t_{HZOE}$ | OE High to Data Valid |     | 8   | ns   |

## 时序参数

### 读取周期时序（Read Cycle Timing）

一个 256 x 4 静态 RAM 的读取周期示例：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220731190300.png)

| Parameter  | Description               | Min | Max | Unit |
| ---------- | ------------------------- | --- | --- | ---- |
| $t_{RC}$   | Read Cycle Time           | 15  |     | ns   |
| $t_{AA}$   | Address to Data Valid     |     | 15  | ns   |
| $t_{ACS}$  | Chip Select to Data Valid |     | 10  | ns   |
| $t_{DOE}$  | OE LOW to Data Valid      |     | 10  | ns   |
| $t_{HZCS}$ | Chip Select to High Z     |     | 8   | ns   |
| $t_{HZOE}$ | OE HIGH to High Z         |     | 8   | ns   |
| $t_{LZCS}$ | Chip Select to Low Z      | 2   |     | ns   |
| $t_{LZOE}$ | OE LOW to Low             | 2   |     | ns   |

1. 首先由 $t_{RC}$ 参数确定写入周期的长度。
2. 确定哪个信号控制读取的功能。在上图的示例中，RAM 的数据输出是由 OE 的下降沿控制的。

### 写入周期时序（Write Cycle Timing）

一个 256 x 4 静态 RAM 的写入周期示例：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220731190328.png)

| Parameter  | Description                   | Min | Max | Unit |
| ---------- | ----------------------------- | --- | --- | ---- |
| $t_{WC}$   | Write Cycle Time              | 15  |     | ns   |
| $t_{HZWE}$ | WE LOW to High Z              |     | 8   | ns   |
| $t_{LZWE}$ | WE HIGH to Low Z              | 2   |     | ns   |
| $t_{PWE}$  | WE Pulse Width                | 11  |     | ns   |
| $t_{SD}$   | Data Set-Up to Write End      | 11  |     | ns   |
| $t_{HD}$   | Data Hold from Write End      | 1   |     | ns   |
| $t_{SA}$   | Address Set-Up to Write Start | 2   |     | ns   |
| $t_{HA}$   | Address Hold from Write End   | 2   |     | ns   |
| $t_{SCS}$  | CS LOW to Write End           | 11  |     | ns   |
| $t_{AW}$   | Address Set-Up to Write End   | 13  |     | ns   |

1. 首先由 $t_{WC}$ 参数确定写入周期的长度。
2. 确定哪个信号控制写入的功能。在上图的示例中，RAM 的数据读入是由 WE 的上升沿控制的。

## 参考与致谢

- 《The Fundamentals Of Digital Semiconductor Testing》

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
