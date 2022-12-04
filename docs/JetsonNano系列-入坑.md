---
id: JetsonNano系列-入坑
title: Jetson Nano系列 - 入坑
---

## 参考与致谢

- [Jetson Nano 开发者套件入门](https://developer.nvidia.com/embedded/learn/get-started-jetson-nano-devkit)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。


## 下载镜像并烧录 SD 卡

下载 [J**etson Nano 开发者套件 SD 卡镜像**]( Jetson Nano 开发者套件 SD 卡镜像)，使用 Etcher 之类的工具烧录进 SD 卡。

## 启动系统

Micro-USB 接入 5V，至少 2A 的电源。或者使用 DC 口接入 5V，至少 2A 的电源（需要用跳线短接 J48 端子）。

如果启动不成功，则用 USB 转串口模块连接板载 DEBUG 端口，看串口打印的错误信息（波特率为 115200）。
