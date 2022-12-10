---
id: 嵌入式Linux-基础知识
title: 嵌入式 Linux - 基础知识
---

## 常用命令

- 查看 CPU 信息：`cat /proc/cpuinfo`
- 查看内核版本：`cat /proc/version`
- 查看内存使用情况：`cat /proc/meminfo`
  - 也可以使用命令 `free` 来简单了解内存使用情况
- 查看 FLASH 存储器使用情况：`cat /proc/partitions`
- 查看任务进程：`top`
- 查看支持的文件系统：`cat /proc/filesystems`（nodev 表示不需要挂载块设备）
- 查看 CPU 主频：`cat /sys/devices/system/cpu/cpu0/cpufreq/cpuinfo_cur_freq`

## Linux 的驱动

Linux 上驱动的作用，就是把硬件设备与 Linux 文件建立了映射关系。

比如，控制 LED 灯和按键时，我们不需要知道他们的具体硬件连接，只要知道哪个文件代表哪个设备，然后就可以通过文件以同样的方式操控同类设备了。

## 参考与致谢

- [[野火]i.MX Linux 开发实战指南](https://doc.embedfire.com/linux/imx6/base/zh/latest/index.html)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

