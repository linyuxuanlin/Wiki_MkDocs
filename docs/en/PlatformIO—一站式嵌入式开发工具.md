# PlatformIO - An All-in-One Embedded Development Tool

- Building an all-in-one development environment to replace Keil/Arduino IDE

![](https://f004.backblazeb2.com/file/wiki-media/img/20200531112801.png)

## Background

PlatformIO is a powerful all-in-one tool with the following features:

- Cross-platform, only requires a Python environment (meaning it can be used on Windows/MacOS/Linux)
- Can be installed as a plugin in VSCode (finally, Keil can be abandoned)
- Powerful ecosystem:
  - [**800+ commonly used development boards**](https://docs.platformio.org/en/latest/boards/index.html#boards): Almost all commonly used development boards can be found here
  - [**35+ development platforms**](https://docs.platformio.org/en/latest/platforms/index.html#platforms): Covers Atmel AVR (Arduino)/ESP/NXP/8051/PIC32/FPGA/FreeRTOS/ARM (STM32), etc.
  - [**20+ frameworks**](https://docs.platformio.org/en/latest/frameworks/index.html#frameworks): Arduino/CMSIS/STM32Cube, etc.
- Comes with compile/download/debug/serial monitor functions and supports various compilers/debuggers
- Provides various functional libraries
- Code auto-completion, syntax checking, multi-project management, theme adaptation
- Remote development function (not tried)
- Unit testing (not tried)
- Both command line and GUI environments are available

In short, it's time to abandon various IDEs (such as Arduino IDE/Keil/IAR) and enjoy one-stop service.

## Download and Installation

First, make sure you have VSCode installed (you can jump to [**this article**](https://wiki-power.com/en/VSCode生产力指南-环境配置) for VSCode download and installation).

Search and install Python and PlatformIO IDE in the `Extensions` (`Ctrl + Shift + X`) section.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200531113916.png)

After successful installation of the plugins, click on `Reload` to start the plugin and then make a cup of coffee while it automatically installs the core component `platformIO-core` (initial installation may take some time).

Once the installation is complete, click on the relevant button in the sidebar to start PlatformIO.

## References and Acknowledgements

- [PlatformIO](https://platformio.org/)
- [PlatformIO Docs](https://docs.platformio.org/en/latest/index.html)
- [ussserrr/stm32pio](https://github.com/ussserrr/stm32pio#requirements)
- [Using VS Code as an STM32 development platform (platformIO)](https://www.jianshu.com/p/49cfa03d6164)
- [PlatformIO IDE (VSCode) - stm32cube framework project](https://www.smslit.top/2019/08/24/platformio-stm32-cubemx/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.