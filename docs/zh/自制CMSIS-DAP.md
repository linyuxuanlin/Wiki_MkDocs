---
id: 自制CMSIS-DAP
title: 自制 CMSIS-DAP 🚧
---

CMSIS DAP 是 ARM 官方推出的开源仿真器，支持所有的 Cortex - ARM 器件，支持 JTAG / SWD 接口，在最新的固件版本中，还支持单线 SWO 接口，可以直接在程序里把相应的数据通过 SWO 接口输出到调试窗口，起到类似串口调试的目的。DAP 主要有以下特点：

1. 完全开源，没有版权限制，所以相应的价格会很便宜
2. 无须驱动，即插即用
3. 在新版本的 DAP 里集成了串口，除了下载调试外还能充当 USB 转串口模块，一机两用
4. 性能方面已经可以满足一般用户的需求

（未完成）

GitHub 仓库：[**linyuxuanlin/DashDAP**](https://github.com/linyuxuanlin/DashDAP)

## 参考与致谢

- [x893/CMSIS-DAP](https://github.com/x893/CMSIS-DAP)
- [ARM 官网的 DAP 介绍](http://www.keil.com/pack/doc/cmsis/DAP/html/index.html)
- [电子屌丝的的情怀：CMSIS DAP 仿真器](http://www.stmcu.org.cn/module/forum/thread-610968-1-2.html)
- [CMSIS DAP 仿真器](https://item.taobao.com/item.htm?spm=a1z10.1-c.w5003-21405148310.36.78726a3dta5ieC&id=550828063764&scene=taobao_shop)
- [konosubakonoakua/Various_MCU_Debugger_DIY](https://github.com/konosubakonoakua/Various_MCU_Debugger_DIY)

---

`2.0 版本编辑中`

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200613154907.jpg)

项目在线预览：

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/DashDAP/raw/master/Hardware/DashDAP.zip"
  ></div>
</div>

## 背景

CMSIS-DAP / DAP-Link 相比 J-Link / ST-Link 有以下优势：

- 完全开源，无法律风险
- 支持虚拟串口
- 免驱
- DAPLink 是 CMSIS-DAP，支持 U 盘拖拽烧录 / 固件升级

## 硬件部分

### MCU

#### 晶振

选用村田 8MHz 无源晶振，型号为 CSTCE8M00G53-R0，封装为 3213，电容为 15pF. 为什么选用这个呢？是因为它体积相对小，并且把两个起振电容整合进去了，硬件设计上能省很多事。至于村田晶振型号的命名方式，可以参考下表：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200612143451.jpg)

### 电源

### 功能模块

## 软件部分

### 驱动

在 Win10 / MacOS / Linux 不需要手动安装驱动；Win8 及更老的系统需要手动安装驱动。

### 拖拽式下载（MSC）

讲编译生成的 `.hex` 或 `.bin` 文件直接拖进 DAPLink 的虚拟 U 盘，即可完成烧录。如果发生错误，错误的信息就会存放在 `FAIL.txt` 中。

### 虚拟串口（CDC）

CDC 虚拟串口功能具备一般的串口功能，允许双向通信，允许发送中断命令来重置目标板。

## 参考与致谢

- [JLink、STLink、DAPLink、CMSIS DAP 使用区别](https://blog.csdn.net/zhouml_msn/article/details/105298776)
- [技新 · DAPLink 仿真器](https://www.jixin.pro/bbs/topic/4187)
- [wuxx / nanoDAP](https://github.com/wuxx/nanoDAP)
- [LGG001 / DAPLink-Brochure](https://github.com/LGG001/DAPLink-Brochure)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
