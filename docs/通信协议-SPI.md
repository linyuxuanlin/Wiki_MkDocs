---
id: 通信协议-SPI
title: 通信协议 - SPI
---

SPI（Serial Peripheral Interface）是一种 **全双工、同步、串行、主从、总线** 通信协议，其数据传输速率为 8 Mbit。SPI 只能有一个主机，可连接一个或多个从机。连接多设备时，需要用到片选引脚（chip select，CS）。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210911095950.png)

## SPI 的引脚

- **SCLK**（serial clock）：由主机驱动的方波时钟信号，从端为输入采样。SDO 和 SDI 上的信号根据 SCLK 上的时钟信号来进行锁存操作。一个时钟周期传输 1bit 数据，所以传输速率等同于主机产生的时钟频率。
- **SDI/SDO**（serial data in / serial data out）：描述了相对于主机的数据流的方向，但更多时候在板子上出现的是 MOSI（Master Out Slave In）和 MISO（Master In Slave Out）。对应地，SDO 在主机上是 MOSI，在从机上是 MISO；而 SDI 在主机上是 MISO，在从机上是 MOSI；在菊花链拓扑中，A 器件 MISO 连接到 B 器件的 MISO。
- **CS/SS**（chip select / slave select）：由主机驱动，用于仲裁 SPI 总线上通信的优先级。当 CS 线上为低电平时，就会激活 SPI 通信。CS 是低电平有效。

## SPI 数据锁存操作

- SPI 数据在 SCLK 上升或下降沿时进行锁存。
- 锁存数据的边沿称为临界边沿。
- 举个例子，以下左图表示 SDO 在上升沿锁存逻辑 `1`，右图表示在下降沿锁存逻辑 `0`。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026151750.png)

## SPI 读取句段示例

1. 临界边沿为上升沿
2. 主机输出到从机（在从机上为 SDI）
3. CS 脚被拉低为 0V，以激活 SPI
4. 数据在 SCLK 上升沿时，从高位（MSB）到低位（LSB）按顺序进行传输
5. 完成传输数据：`1011001`

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026152228.png)

## SPI 临界边沿

- $t_{SU}$（setup time）：定义在临界边沿事件发生多久前，SDI 数据就该被确定并稳定下来。
- $t_{HO}$（hold time）：定义在临界边沿事件发生后，SDI 上的数据必须保留多长时间。
- $t_{DO}$（delay time）：定义在临界边沿事件发生后，SDO 上的有效数据的延迟时间。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026160940.png)

## SPI 传输模式（4 种）

- **CPOL**（clock polarity，时钟极性）：空闲（不传输数据）时钟的极性，`0` 代表低电平，`1` 代表高电平。
- **CPHA**（clock phase，时钟相位）：定义在上升还是下降沿进行锁存。`0` 代表在第一个变化的边沿进行锁存；`1` 代表在第二个变化的边沿进行锁存。

| 模式编号 | CPOL（时钟极性） | CPHA（时钟相位）          | 锁存边沿 |
| -------- | ---------------- | ------------------------- | -------- |
| 0        | 0（低电平）      | 0（在第一个边沿进行锁存） | 上升沿   |
| 1        | 0（低电平）      | 1（在第二个边沿进行锁存） | 下降沿   |
| 2        | 1（高电平）      | 0（在第一个边沿进行锁存） | 下降沿   |
| 3        | 1（高电平）      | 1（在第二个边沿进行锁存） | 上升沿   |

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026162028.png)

## 菊花链（Daisy Chain）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026164011.png)

在普通模式下，SPI 每个从机都需要一条 CS 线。当从机一多，会占用主机过多的 IO 口。使用菊花链的拓扑连接，就可以只用一条 CS 线，驱动所有的从机。

菊花链的原理是，数据从主机传输到第一个从机，然后从第一个从机传输到第二个从机，依此下去，数据沿着线路级联，直到系列中的最后一个从机，最后的一个从机通过 SDO 将数据传送到主机。

## SPI 的优缺点

优点：

- 全双工通信
- 推挽驱动，能提供比较好的信号完整性和较高的速度
- 协议灵活，不仅限于 8-bit 一个字节
- 硬件设计简单
  - 不需要上拉电阻，因此功耗更低
  - 没有仲裁机制或相关的失效模式
  - 从机不需要时钟（由主机提供）
  - 从设备不需要单独的地址
  - 不需要收发器
  - 信号都是单向的，容易进行电流隔离
- 时钟速率没有上限

缺点：

- 用到的引脚比 I2C 多
- 从机无法进行硬件应答
- 没有错误检查机制，如 UART 中的奇偶校验位
- 只能有一个主机
- 规范不统一，无法验证一致性
- 传输距离相对比较近（相比 CAN、RS232、RS485 等）

## 参考与致谢

- 《Analog Engineer’s Pocket Reference》

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

