---
id: STM32的启动模式
title: STM32 的启动模式
---

STM32 提供了 BOOT1 与 BOOT0 引脚，可以通过设置引脚的状态，以选择上电复位后的启动模式。

以下为三种启动模式：

## 1. 从主闪存存储器启动

| BOOT0 | BOOT1 |
| :---: | :---: |
|  低   | 任意  |

从片上 Flash 存储器启动（就是参数为 64K / 128K / 256K 的 Flash），一般正常情况下是这样配置的。

## 2. 从系统存储器启动

| BOOT0 | BOOT1 |
| :---: | :---: |
|  高   |  低   |

使用串口 / ISP 下载程序时，需要配置这种模式。

## 3. 从内置 SRAM 启动

| BOOT0 | BOOT1 |
| :---: | :---: |
|  高   |  高   |

从内置 SRAM 启动，用途有两个：

- 用于反复下载调试时，提高效率（因为下载到 Flash 相对慢）。需要注意的是，断电程序将丢失
- 用于解除芯片的读保护功能 / 擦除 Flash 恢复出厂

## 补充

以上图表中 `高` `低` 表示接 10K 电阻上拉 / 下拉，而非直连 VCC / GND

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200603134417.jpg)

## 参考与致谢

- [STM32 BOOT0、BOOT1 的配置](https://blog.csdn.net/Creative_Team/article/details/79315876)
- [STM32 BOOT 模式配置以及作用](https://blog.csdn.net/weixin_34349320/article/details/86231081?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

