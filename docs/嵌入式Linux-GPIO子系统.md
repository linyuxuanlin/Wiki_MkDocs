---
id: 嵌入式Linux-GPIO子系统
title: 嵌入式 Linux - GPIO 子系统
---

## 参考与致谢

- [8. 控制蜂鸣器（GPIO 子系统）](https://doc.embedfire.com/linux/stm32mp1/linux_base/zh/latest/linux_app/gpio_subsystem/gpio_subsystem.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。


## GPIO 子系统简介

GPIO（General Purpose I/O）即通用输入输出端口。这些引脚通常有多种功能，最基本的是高低电平输入检测和输出，部分引脚还会与主控器的片上外设绑定，可作为串口、I2C、网络、电压检测等的通信引脚。

与 LED 子系统类似，Linux 提供了 GPIO 子系统驱动框架，使用该驱动框架将 CPU 的 GPIO 引脚导出到用户空间，我们通过访问 `/sys` 文件系统进行控制。GPIO 子系统支持把引脚用于基本的输入输出功能，其中输入功能支持中断检测。（在 Linux 内核源码 `Documentation/gpio` 目录可找到关于 GPIO 子系统更详细的说明）

## GPIO 设备目录

GPIO 驱动子系统导出到用户空间的目录是 `/sys/class/gpio`，使用如下的命令查看：

