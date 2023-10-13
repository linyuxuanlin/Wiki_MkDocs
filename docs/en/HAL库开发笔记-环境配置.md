# HAL Library Development Notes - Environment Configuration

Note: This tutorial is based on the Reverse Customer's STM32F429IGT6 board.

## Software Installation

### Keil MDK

Refer to the article [**Keil MDK Configuration Guide**](https://wiki-power.com/en/KeilMDK%E9%85%8D%E7%BD%AE%E6%8C%87%E5%8D%97)

### Java Runtime Environment

This is the Java environment required by STM32CubeMX. Download and install it from the [**official website link**](https://www.java.com/en/download/).

### STM32CubeMX

Download and install STM32CubeMX from the [**official website link**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## Project Configuration

### Initialization

Create a new project and save it after selecting the chip.

### Configure SYS

`Pinout & Configurations` - `System Core` - `SYS`

Change the `Debug` option to `Serial Wire` (see the article [**CubeMX and CubeIDE Pitfalls**](https://wiki-power.com/en/CubeMX与CubeIDE避坑) for details).

### Configure RCC

`Pinout & Configurations` - `System Core` - `RCC`

Set it according to the board situation.

For example, referring to the board schematic:

![](https://img.wiki-power.com/d/wiki-media/img/20210205205030.png)

Set both `HSE` and `LSE` options to external crystal.

### Configuring the Clock Tree

Configure in the `Clock Configuration` interface.

![](https://img.wiki-power.com/d/wiki-media/img/20210205205550.png)

Follow the steps in the above figure:

1. Fill in the values of the two leftmost frequencies according to the parameters of the onboard external crystal oscillator.
2. Check `HSE` because the external crystal oscillator has higher frequency and accuracy than the internal one.
3. Check `PLLCLK` to obtain a high frequency using PLL phase-locked loop multiplication.
4. Fill in the value of `HCKL`, generally based on the maximum frequency indicated below, and press enter. The division and multiplication factors will be automatically calculated.

### Configuring Project Management Options

![](https://img.wiki-power.com/d/wiki-media/img/20210130095224.png)

![](https://img.wiki-power.com/d/wiki-media/img/20210130095239.png)

## Differences between HAL Library and Standard Library

To increase portability, the HAL library has three additional features compared to the standard library: **handle, MSP function, and callback function**. For details, please refer to the content in the reference links at the end of the article.

## References and Acknowledgements

- [STM32 System Clock RCC Detailed Explanation](https://blog.csdn.net/as480133937/article/details/98845509)
- [Board Initialization, RCC Clock Tree Complete Configuration Method and Detailed Process](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [A Comprehensive Summary of STM32 HAL Knowledge](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [Clearer, A Comprehensive Summary of STM32 HAL Knowledge](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

Sorry, there is no Chinese article provided for translation. Please provide the article to be translated.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
