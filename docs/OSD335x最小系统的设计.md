---
id: OSD335x最小系统的设计
title: OSD335x 最小系统的设计
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012144907.png)

TI 的 OSD335x-SM 芯片，是一颗将 Cortex-A8 AM335x 处理器、DDR3 内存、TPS65217C PMIC（电源管理芯片）、TL5209 LDO、所需的被动器件、以及 4KB 的 EEPROM 集成在 BGA 封装内的 SIP（System-in-Package）模组。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012153036.png)

OSD335x 的最小系统包括 4 个部分：电源、时钟、复位、烧录调试接口。为了让其更易于使用，还可以加上一对按钮、几颗 LED 和一些外设排针。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012155857.png)

## 电源

### 输入

- VIN_AC：主电源输入（DC5V@2A），根据需要加保险丝、磁珠、二级管、输入保护等。
- VIN_USB：USB 电源输入（DC5V@0.5A，通过内部 PMIC 可提高至 1.3A），也作为 USB 2.0 host 的参考电压电流
- VIN_BAT：可作为电池输入（使用电池电源，2.75-5.5V）或输出（为电池充电），不可作为事件输入。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012173057.png)

### 输出

- SYS_VOUT：等于输入 PMIC 的电压，要注意接在这个引脚上的元器件是能在 3-5V 区间内使用的，因为当电池充电的时候，PMIC 切换不同的电源输入。
- SYS_VDD1_3P3V：3.3V 输出，由 TL5209 LDO 提供，并由 PMIC 的 LDO4 使能，作为主电源输出。
- SYS_VDD2_3P3V：3.3V 输出，由 PMIC 的 LDO2 提供。
- SYS_RTC_1P8V：1.8V 输出，由 PMIC 的 LDO1 提供，也用于驱动 AM335x 内部 RTC。
- SYS_VDD_1P8V：1.8V 输出，由 PMIC 的 LDO3 提供。
- SYS_ADC_1P8V：1.8V 输出，由 PMIC 的 LDO3 提供，为模拟应用做了滤波，在内部也为 AM335x ADC 供电。

推荐为所有电源输出添加测试点，方便调试。

还有一些为内部供电的引脚：VDDSHV_3P3V、VDDS_DDR、VDD_MPU、VDD_CORE、VDDS_PLL。他们仅供引出测试点测量，但不要引出给外部电路使用。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013142917.png)

### 模拟参考输入与地

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013143532.png)

OSD335x 有 ADC 接口，如果要使用 ADC，则必须正确使用模拟电源和模拟地。ADC 接口能承受最高 1.8V 的模拟输入（参照 VREFP 引脚）。通常来说，VREFP 可直接连接 SYS_ADC_1P8V，但如果有需要，可以分压到一个更低的电压。

### 电源管理

在 OSD335x 内部，AM335x 通过 I2C0 与 TPS65217C PMIC 进行通信。

I2C0 内部有 4.7k 上拉电阻，但如果要带设备的话，最好在外部额外添加上拉电阻。

TPS65217C PMIC 可通过 I2C 来设置以下参数：

- 电池充电电压
- 充电安全时间控制
- Buck/Boost 输出电压
- LDO 输出电压
- 上电 / 掉电时序
- 过流过温阈值

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013161739.png)

除了通过 I2C 连接，PMIC 还有些功能引脚需要连接 OSD335x：

- PMIC_POWER_EN：用于 AM335x 控制 PMIC 上电时序
- PMIC_IN_PWR_EN：使能 PMIC 的 buck 和 LDO，给高电平会开始进入上电时序控制
- RTC_PWRONRSTN：AM335x RTC 的独立电源复位脚
- PMIC_OUT_LDO_PGOOD：LDO1 和 LDO2 的输出状态，高电平输出良好，低电平代表任意一个 LDO 输出异常。
- EXT_WAKEUP：外部事件唤醒引脚
- PMIC_OUT_NWAKEUP：Host 外部事件唤醒引脚（低电平有效）
- EXTINTN：AM335x 外部中断输入引脚
- PMIC_OUT_NINT：PMIC 终端输出引脚（低电平有效）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013161927.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013163119.png)

### 电源按键

TPS65217C PMIC 内部有一个低电平有效的复位输入，通过 PMIC_IN_PB_IN 引脚连接在 OSD335x，也可以外接按键。这个输入引脚有 50ms 的去抖动时间，和一个内部上拉电阻。除此之外，这个电源按钮还有以下功能：

- 当 PMIC_IN_PB_IN 检测到下降沿输入时，PMIC 将会从关闭或睡眠模式中唤醒
- 当 PMIC_IN_PB_IN 保持低电平超过 8 秒时，PMIC 会重新上电/复位
- 如果 PMIC_IN_PB_IN 引脚长时间保持低电平，器件将继续在 ACTIVE 和 RESET 状态之间循环，每 8 秒进入复位。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013165738.png)

### 电源指示灯

我们使用 SYS_VDD2_3P3V（150mA） 作为电源指示灯的输出。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014092054.png)

## 复位

OSD335x 有几种复位方式：

- 冷复位（上电复位）：在设备上电和电源域上电时进行
- 热复位
  - 是部分复位，不影响全局逻辑
  - 是为了减少复位恢复时间

OSD335x 有 3 个复位输入（与 AM335x 上的复位输入同名）：

- PWRONRSTN：冷复位；在上电期间需要保持低电平，直到所有输入电源线都稳定为止；不可阻塞，除了 RTC 外，整个系统都会收到影响。
- WARMRSTN：热复位；一些 PRCM（电源、复位和时钟管理）和控制模块寄存器对热复位不敏感
- RTC_PWRONRSTN：RTC 模块专用的上电复位输入不受冷复位影响，RTC_PWRONRSTN 也不会对设备其他部分产生影响。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014105556.png)

## 时钟

### OSC0 与 OSC1

OSD335x 有两个时钟输入：

- OSC0：高速时钟输入（主时钟），在 19.2MHz、24MHz（推荐）、25MHz 或 26MHz 频率下工作。此时钟源为所有非 RTC 功能提供参考。OSC0 时钟输入拥有 OSC0_IN、OSC0_OUT 和 OSC0_GND 引脚。
- OSC1：低速时钟输入，运行在 32.768kHz 下，为 RTC 供电。OSC1 时钟输入拥有 OSC1_IN、OSC1_OUT 和 OSC1_GND 引脚。此时钟源默认失能，非必要输入，如果需要的话，可以接收内部 32kHz RC 晶振信号。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014095242.png)

上图中，Rbias 与 Rd 是可选的。如果不能提供准确的频率，Rbias 可用于灵活校准，可以 DNP（可不加进原理图或留空位）。但如果不需要 Rd 的话，必须用导线替代，否则会造成断路。

在参考设计中，OSC0 选用 7A-24.000MAAJ-T 24MHz 晶振，18pF 电容，1MΩ 电阻作为 Rbias。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014101932.png)

RTC_KALDO_ENN 引脚默认外部下拉（10k 电阻），用于使能内部 RTC LDO。

## 烧录调试接口

在参考设计中，使用 JTAG 接口。

https://octavosystems.com/octavosystems.com/wp-content/uploads/2017/07/JTAG.jpg

## 其他外设

### 启动配置

启动配置表可参考 [**AM335x Technical Reference Manual (TRM)**](http://www.ti.com/lit/pdf/spruh73) 的 **SYSBOOT Configuration Pins** 章节

在参考设计中，我们这样接：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110132.png)

配置以下参数：

- 设置时钟频率为 24Mhz
- 通过 XDMA_EVENT_INTR0 禁用 CLKOUT1 输出，该引脚仅用于 JTAG 仿真。
- 将启动顺序设置为 SPI0 -> MMC0 -> USB0 -> UART0

### 用户按键与 LED

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110906.png)

### 外设排针

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110947.png)

## 参考与致谢

- [SO YOU WANT TO BUILD AN EMBEDDED LINUX SYSTEM?](https://jaycarlson.net/embedded-linux/#)
- [OSD335x-SM System-in-Package Smallest AM335x Module, Quickest Design](https://octavosystems.com/octavo_products/osd335x-sm/#Technical%20Documents)
- [OSD335x Reference Design Tutorial Series](https://octavosystems.com/app_notes/osd335x-design-tutorial/)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

