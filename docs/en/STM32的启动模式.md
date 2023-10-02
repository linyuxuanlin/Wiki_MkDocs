# STM32 Boot Modes

STM32 provides BOOT0 and BOOT1 pins, which can be used to select the boot mode after power-on reset by setting the status of these pins.

There are three boot modes:

## 1. Boot from Main Flash Memory

| BOOT0 | BOOT1 |
| :---: | :---: |
|  Low  |  Any  |

This is the default configuration for booting from the on-chip flash memory (i.e. the flash memory with parameters of 64K/128K/256K).

## 2. Boot from System Memory

| BOOT0 | BOOT1 |
| :---: | :---: |
| High  |  Low  |

This mode is used when downloading programs via serial port/ISP.

## 3. Boot from Internal SRAM

| BOOT0 | BOOT1 |
| :---: | :---: |
| High  | High  |

There are two uses for booting from internal SRAM:

- To improve efficiency when repeatedly downloading and debugging (because downloading to flash is relatively slow). Note that the program will be lost after power-off.
- To release the chip's read protection function/erase flash to restore factory settings.

## Supplement

In the above table, "High" and "Low" indicate connection to a 10K resistor pull-up/pull-down, not directly to VCC/GND.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200603134417.jpg)

## Reference and Acknowledgement

- [Configuration of STM32 BOOT0 and BOOT1](https://blog.csdn.net/Creative_Team/article/details/79315876)
- [Configuration and Function of STM32 BOOT Mode](https://blog.csdn.net/weixin_34349320/article/details/86231081?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.nonecase)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.