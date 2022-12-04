---
id: KeilMDK配置指南
title: Keil MDK 配置指南
---

## 1. 下载

**进入 Keil 官网下载页面：** [https://www.keil.com/demo/eval/arm.htm](https://www.keil.com/demo/eval/arm.htm)

**如图填写相关信息并点击 `Submit` 按钮：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564402348383.png)

**点击下载安装包：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564402469518.png)

## 2. 安装

**打开下载完成的安装包，按如下步骤操作：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405005991.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405034468.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405123578.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405166784.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405201092.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405260737.png)

**安装芯片包（我们需要 STM32 F1 和 F4 系列）：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405574756.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564405648731.png)

## 3. 破解

点击下载 [**破解器**](https://github.com/linyuxuanlin/File-host/blob/main/software/KEIL_Lic.exe)

**关闭 MDK，右键以管理员身份打开：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564406135091.png)

**打开菜单栏 - File - License Management ：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564406171844.png)

**复制这一串 `CID`：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564406230209.png)

**在破解器中粘贴，并在 `Target` 下拉框中选择 `Arm` ，然后点击 `Generate` 生成激活码：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564406292113.png)

**拷贝激活码，到 MDK 中粘贴，后点击 `Add LIC`：**

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/UTOOLS1564406431978.png)

## 参考与致谢

- [Keil 保护视力背景颜色设置](https://blog.csdn.net/w5862338/article/details/50984536)
- [keil 代码格式化](https://blog.csdn.net/sudaroot/article/details/88095269)
- [个人界面配置](https://github.com/linyuxuanlin/File-host/blob/main/software-development/global.prop)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

