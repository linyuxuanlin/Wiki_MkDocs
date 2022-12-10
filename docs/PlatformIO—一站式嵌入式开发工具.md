---
id: PlatformIO—一站式嵌入式开发工具
title: PlatformIO — 一站式嵌入式开发工具
---

—— 搭建一站式开发环境，替代 Keil / Arduino IDE

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531112801.png)

## 背景

PlatformIO 是一个强大的一站式工具，来看看它的特点：

- 跨平台，仅需 Python 环境（意味着可以在 Windows/MacOS/Linux 上使用）
- 在 VSCode 内可作为插件安装使用（终于可以抛弃 Keil 了）
- 强大的生态：
  - [**800+ 常用的开发板**](https://docs.platformio.org/en/latest/boards/index.html#boards)：你能买到的通用开发板，这儿基本上都有
  - [**35+ 开发平台**](https://docs.platformio.org/en/latest/platforms/index.html#platforms)：覆盖 Atmel AVR（Arduino）/ ESP / NXP / 8051 / PIC32 / FPGA / FreeRTOS / ARM（STM32） 等等
  - [**20+ 框架**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks)：Arduino / CMSIS / STM32Cube 等等
- 带编译 / 下载 / 调试 / 串口监视器功能，且支持各式各样的编译器 / 调试器
- 提供各式各样的功能库
- 代码自动补全、语法检查、多项目管理、适配主题
- 远程开发功能（未尝试）
- 单元测试（未尝试）
- 命令行和 GUI 环境都有

总之，是时候抛弃各类 IDE（如 Arduino IDE / Keil / IAR），享受一条龙服务了。

## 下载安装

首先，确保你的电脑有 VSCode（VSCode 的下载安装可以跳转 [**这篇文章**](https://wiki-power.com/VSCode生产力指南-环境配置)

在 `拓展` （`Ctrl + Shift + X`） 内搜索并安装 `Python` 和 `PlatformIO IDE`.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200531113916.png)

插件安装成功后，点击 `重新加载` 启动插件，然后泡一杯咖啡，待其自动安装核心组件 `platformIO-core`（首次安装时间可能会比较长）

安装完成后，单击侧边栏相关的按钮，即可启动 PlatformIO.

## 参考与致谢

- [PlatformIO](https://platformio.org/)
- [PlatformIO Docs](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [用 VS Code 作为 STM32 开发平台（platformIO）](https://www.jianshu.com/p/49cfa03d6164)
- [PlatformIO IDE(VSCode) - stm32cube 框架的工程](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

