# PlatformIO — An All-in-One Embedded Development Tool

— Building an all-in-one development environment, replacing Keil / Arduino IDE

![PlatformIO](https://media.wiki-power.com/img/20200531112801.png)

## Background

PlatformIO is a robust all-in-one tool. Let's take a look at its features:

- Cross-platform, requires only a Python environment (meaning it can be used on Windows/MacOS/Linux)
- Can be used as a plugin within VSCode (finally, you can say goodbye to Keil)
- Robust ecosystem:
  - [**800+ commonly used development boards**](https://docs.platformio.org/en/latest/boards/index.html#boards): Virtually all the popular development boards you can find are supported here
  - [**35+ development platforms**](https://docs.platformio.org/en/latest/platforms/index.html#platforms): Covering Atmel AVR (Arduino) / ESP / NXP / 8051 / PIC32 / FPGA / FreeRTOS / ARM (STM32), and more
  - [**20+ frameworks**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks): Arduino / CMSIS / STM32Cube, and others
- Comes with compilation, download, debugging, and serial monitoring functions, supporting a variety of compilers and debuggers
- Provides a wide range of libraries
- Features code auto-completion, syntax checking, multi-project management, and theme customization
- Remote development capabilities (untested)
- Unit testing (untested)
- Available in both command-line and GUI environments

In short, it's time to bid farewell to various IDEs like Arduino IDE, Keil, and IAR, and enjoy a one-stop service.

## Download and Installation

First, make sure you have VSCode installed (you can refer to [**this article**](https://wiki-power.com/VSCode%E7%94%9F%E4%BA%A7%E5%8A%9B%E6%8C%87%E5%8D%97-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) for VSCode download and installation).

In the `Extensions` (press `Ctrl + Shift + X`) section, search for and install `Python` and `PlatformIO IDE`.

![PlatformIO Installation](https://media.wiki-power.com/img/20200531113916.png)

After the successful installation of the plugins, click on `Reload` to start the plugin. Then, grab a cup of coffee and wait for the automatic installation of the core component, `platformIO-core` (initial installation may take some time).

Once the installation is complete, click on the relevant button in the sidebar to launch PlatformIO.

## References and Acknowledgments

- [PlatformIO](https://platformio.org/)
- [PlatformIO Docs](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [Using VS Code as an STM32 Development Platform (PlatformIO)](https://www.jianshu.com/p/49cfa03d6164)
- [PlatformIO IDE (VSCode) - stm32cube Framework Projects](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
