# HAL Library Development Notes - Environment Setup

Note: This tutorial is based on the STM32F429IGT6 board by STM32.

## Software Installation

### Keil MDK

Refer to the article [**Keil MDK Configuration Guide**](https://wiki-power.com/KeilMDK%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97) for details.

### Java Runtime Environment

This is the Java environment required for STM32CubeMX. Download and install it from the [**official website**](https://www.java.com/en/download/).

### STM32CubeMX

Download and install STM32CubeMX from the [**official website**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## Project Configuration

### Initialization

Create a new project, select the microcontroller, and save the project.

### SYS Configuration

`Pinout & Configurations` - `System Core` - `SYS`

Change the `Debug` option to `Serial Wire` (see the article [**CubeMX and CubeIDE Pitfalls**](https://wiki-power.com/CubeMX与CubeIDE避坑) for the rationale).

### RCC Configuration

`Pinout & Configurations` - `System Core` - `RCC`

Configure it according to your board's specifications.

For example, refer to the board's schematic:

![Board Schematic](https://media.wiki-power.com/img/20210205205030.png)

Set both `HSE` and `LSE` options to use external crystal oscillators:

![Clock Settings](https://media.wiki-power.com/img/20210205205140.png)

### Clock Tree Configuration

Configure the clock settings in the `Clock Configuration` interface.

![Clock Configuration](https://media.wiki-power.com/img/20210205205550.png)

Follow these steps based on the image above:

1. Enter the values for the two leftmost frequencies based on the parameters of the onboard external crystal oscillator.
2. Check the `HSE` box since the external crystal oscillator has higher frequency and precision than the internal oscillator.
3. Check the `PLLCLK` box to use PLL (Phase-Locked Loop) multiplication for higher frequencies.
4. Enter the value for `HCKL`, usually based on the maximum recommended frequency shown below, and press Enter. It will automatically calculate the prescaler and multiplier values.

### Project Management Options Configuration

![Project Management Options](https://media.wiki-power.com/img/20210130095224.png)

![Project Management Options](https://media.wiki-power.com/img/20210130095239.png)

## Differences Between HAL Library and Standard Library

To enhance portability, the HAL library includes three additional features compared to the standard library: **handles, MSP functions, and callback functions**. For more details, refer to the content in the cited links at the end of this document.

## References and Acknowledgments

- [Explanation of the STM32 System Clock RCC](https://blog.csdn.net/as480133937/article/details/98845509)
- [Board Initialization: Complete Configuration of the RCC Clock Tree](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [Comprehensive Summary of STM32 HAL Knowledge](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [It's Clear Now: A Comprehensive Summary of STM32 HAL Knowledge](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
