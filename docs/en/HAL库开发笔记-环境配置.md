# HAL Library Development Notes - Environment Configuration

Note: This tutorial is based on the STM32F429IGT6 board from STMicroelectronics.

## Software Installation

### Keil MDK

For detailed instructions, refer to the article [**Keil MDK Configuration Guide**](to_be_replaced[3]).

### Java Runtime Environment

This is the Java environment required for STM32CubeMX. Download and install it from the [**official website**](https://www.java.com/en/download/).

### STM32CubeMX

Download and install STM32CubeMX from the [**official website**](https://my.st.com/content/my_st_com/zh/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-configurators-and-code-generators/stm32cubemx.license=1611899126599.product=STM32CubeMX.version=6.1.1.html).

## Project Configuration

### Initialization

Create a new project and save it after selecting the microcontroller.

### SYS Configuration

`Pinout & Configurations` - `System Core` - `SYS`

Change the `Debug` option to `Serial Wire` (for detailed reasons, see the article [**Avoiding Pitfalls with CubeMX and CubeIDE**](to_be_replaced[3])).

### RCC Configuration

`Pinout & Configurations` - `System Core` - `RCC`

Configure it according to your board's specifications.

For example, referencing the board's schematic:

![Board Schematic](https://img.wiki-power.com/d/wiki-media/img/20210205205030.png)

Set both `HSE` and `LSE` options to use external crystal oscillators:

![Clock Configuration](https://img.wiki-power.com/d/wiki-media/img/20210205205140.png)

### Clock Tree Configuration

Configure the clock settings in the `Clock Configuration` interface.

![Clock Configuration](https://img.wiki-power.com/d/wiki-media/img/20210205205550.png)

Follow the steps below according to the above image:

1. Enter the values for the leftmost two frequencies based on the parameters of the onboard external crystal oscillator.
2. Check `HSE` because external crystal oscillators offer higher frequency and accuracy than internal ones.
3. Check `PLLCLK` to obtain a higher frequency using PLL multiplication.
4. Enter the value for `HCKL`, generally based on the maximum frequency suggested below. After inputting the value and pressing Enter, the system will automatically calculate the division and multiplication factors.

### Project Management Options Configuration

![Project Management Options](https://img.wiki-power.com/d/wiki-media/img/20210130095224.png)

![Project Management Options](https://img.wiki-power.com/d/wiki-media/img/20210130095239.png)

## Differences Between HAL Library and Standard Library

To enhance portability, the HAL library includes three additional features compared to the standard library: **Handles, MSP Functions, and Callback Functions**. For more details, refer to the content in the referenced links at the end of the document.

## References and Acknowledgments

- [**In-Depth Explanation of STM32 System Clock RCC**](https://blog.csdn.net/as480133937/article/details/98845509)
- [**Board Initialization: Complete Configuration of RCC Clock Tree**](https://www.notion.so/2-RCC-770c0c454f954408a3956257aa0fb523)
- [**Comprehensive Summary of STM32 HAL Knowledge**](https://mp.weixin.qq.com/s/ffcjKtl7JdRibLRNGquGXA)
- [**Clearly Understanding: A Comprehensive Summary of STM32 HAL Knowledge**](https://mp.weixin.qq.com/s/qkj0fQS5NrCXmbppKEhaAg)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.