# Differences and Connections between SWD and JTAG

As we all know, SWD and JTAG are commonly used interfaces for downloading programs and debugging microcontrollers. Their similarities are:

- **Power supply voltage range**: 1.2 V - 5.5 V
- **Clock rate**: Configurable up to 10 MHz
- **SWO trace capture**: Data rate up to 50 Mbit/s (UART/NRZ mode)
- **Isolation voltage**: 1 kV
- **Hot plug**: Supported

## JTAG

JTAG, short for Joint Test Action Group. The latest standard as of this article is IEEE Standard 1149.1-1990.

Its topology diagram (daisy chain) is as follows:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210209191921.png)

JTAG generally uses 5 pins:

- **TDI** (Test Data In): Serial input pin
- **TDO** (Test Data Out): Serial output pin
- **TCK** (Test Clock): Clock pin, generally with a 100k pull-down resistor
- **TMS** (Test Mode Select): Mode selection (control signal) pin
- **TRST** (Test Reset): Reset pin

Advantages of JTAG:

- Not limited to ARM series chips
- Has more uses for programming, debugging, and production testing

## SWD

Serial Wire Debug, specifically designed by ARM, only supports ARM (so it performs better in ARM series microcontrollers).

SWD generally uses 2 pins:

- **SWDIO** (Serial Wire Data Input Output): Serial data input and output pin
- **SWCLK** (Serial Wire Clock): Serial line clock pin

Advantages of SWD:

- Uses fewer pins, only SWDIO and SWCLK are needed
- SWD has special functions, such as printing debugging information
- Compared with JTAG, SWD has better overall performance in speed

## Compatibility between JTAG and SWD

Generally, the following burning sockets will be available on the microcontroller board, which can be compatible with both JTAG and SWD:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210210122923.jpg)

![](https://f004.backblazeb2.com/file/wiki-media/img/20210210123714.png)

- TCK is compatible with SWCLK
- TMS is compatible with SWDIO
- (TDO is compatible with SWO)

Reasons for choosing SWD instead of JTAG:

- The circuit schematic design needs to be simple enough and can be tested without JTAG functionality
- The PCB has size limitations, and SWD can save space
- The MCU no longer has extra pins for JTAG

## References and Acknowledgments

- [Difference between SWD and JTAG download and debug interface](https://mp.weixin.qq.com/s/MW57t266yvv6TOweeFEUVA)
- [Cortex JTAG, SWD Debug Port Sharing](https://southlife.tistory.com/107)
- [JTAG/SWD Interface](https://www.keil.com/support/man/docs/ulinkplus/ulinkplus_jtagswd_interface.htm)
- [JTAG](https://en.wikipedia.org/wiki/JTAG)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.