# Design of OSD335x Minimum System

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012144907.png)

The OSD335x-SM chip from TI is a System-in-Package (SIP) module that integrates a Cortex-A8 AM335x processor, DDR3 memory, TPS65217C PMIC (power management chip), TL5209 LDO, necessary passive components, and a 4KB EEPROM in a BGA package.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012153036.png)

The minimum system of OSD335x includes four parts: power supply, clock, reset, and programming/debugging interface. To make it easier to use, a pair of buttons, several LEDs, and some peripheral pins can also be added.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012155857.png)

## Power Supply

### Input

- VIN_AC: Main power input (DC5V@2A), with optional fuse, bead, diode, input protection, etc.
- VIN_USB: USB power input (DC5V@0.5A, can be increased to 1.3A through internal PMIC), also serves as reference voltage and current for USB 2.0 host.
- VIN_BAT: Can be used as battery input (2.75-5.5V) or output (for battery charging), but not as event input.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012173057.png)

### Output

- SYS_VOUT: equal to the input voltage of the PMIC, it should be noted that the components connected to this pin should be able to operate within the 3-5V range, as the PMIC switches between different power inputs when the battery is charging.
- SYS_VDD1_3P3V: 3.3V output provided by the TL5209 LDO and enabled by PMIC's LDO4, serving as the main power output.
- SYS_VDD2_3P3V: 3.3V output provided by PMIC's LDO2.
- SYS_RTC_1P8V: 1.8V output provided by PMIC's LDO1, also used to drive the internal RTC of AM335x.
- SYS_VDD_1P8V: 1.8V output provided by PMIC's LDO3.
- SYS_ADC_1P8V: 1.8V output provided by PMIC's LDO3, filtered for analog applications and also used to power the AM335x ADC internally.

It is recommended to add test points for all power outputs to facilitate debugging.

There are also some pins for internal power supply: VDDSHV_3P3V, VDDS_DDR, VDD_MPU, VDD_CORE, VDDS_PLL. They are only for measuring through test points, and should not be connected to external circuits.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013142917.png)

### Analog Reference Input and Ground

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013143532.png)

OSD335x has an ADC interface, and if you want to use the ADC, you must correctly use the analog power and ground. The ADC interface can withstand a maximum analog input of 1.8V (refer to the VREFP pin). Generally, VREFP can be directly connected to SYS_ADC_1P8V, but if necessary, it can be divided to a lower voltage.

### Power Management

Inside OSD335x, AM335x communicates with the TPS65217C PMIC through I2C0.

I2C0 has a 4.7k pull-up resistor internally, but if you want to connect devices, it is better to add an external pull-up resistor.

The TPS65217C PMIC can set the following parameters through I2C:

- Battery charging voltage
- Charging safety time control
- Buck/Boost output voltage
- LDO output voltage
- Power-up/power-down timing
- Overcurrent/overtemperature threshold

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013161739.png)

In addition to the I2C connection, the PMIC also has some functional pins that need to be connected to the OSD335x:

- PMIC_POWER_EN: Used by the AM335x to control the PMIC power-up timing
- PMIC_IN_PWR_EN: Enables the PMIC buck and LDO, and entering the power-up timing control will start with a high level
- RTC_PWRONRSTN: Independent power reset pin for AM335x RTC
- PMIC_OUT_LDO_PGOOD: Output status of LDO1 and LDO2, high level indicates good output, low level indicates any LDO output abnormality.
- EXT_WAKEUP: External event wakeup pin
- PMIC_OUT_NWAKEUP: Host external event wakeup pin (active low)
- EXTINTN: AM335x external interrupt input pin
- PMIC_OUT_NINT: PMIC terminal output pin (active low)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013161927.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013163119.png)

### Power button

The TPS65217C PMIC has a low-level effective reset input internally, which is connected to the OSD335x through the PMIC_IN_PB_IN pin and can also be externally connected to a button. This input pin has a 50ms debounce time and an internal pull-up resistor. In addition, this power button has the following functions:

- When PMIC_IN_PB_IN detects a falling edge input, the PMIC will wake up from shutdown or sleep mode
- When PMIC_IN_PB_IN stays at a low level for more than 8 seconds, the PMIC will power up/reset again
- If the PMIC_IN_PB_IN pin stays at a low level for a long time, the device will continue to cycle between ACTIVE and RESET states, entering reset every 8 seconds.

### Power Indicator

We use SYS_VDD2_3P3V (150mA) as the output for the power indicator.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014092054.png)

## Reset

OSD335x has several reset methods:

- Cold reset (power-on reset): performed when the device and power domain are powered on
- Warm reset
  - Partial reset that does not affect global logic
  - Designed to reduce reset recovery time

OSD335x has 3 reset inputs (with the same name as the reset inputs on AM335x):

- PWRONRSTN: cold reset; needs to be kept low during power-up and until all input power lines are stable; cannot be blocked, and except for RTC, the entire system will be affected.
- WARMRSTN: warm reset; some PRCM (power, reset, and clock management) and control module registers are not sensitive to warm reset
- RTC_PWRONRSTN: dedicated power-on reset input for the RTC module, not affected by cold reset, and does not affect other parts of the device.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014105556.png)

## Clock

### OSC0 and OSC1

OSD335x has two clock inputs:

- OSC0: high-speed clock input (main clock), operating at 19.2MHz, 24MHz (recommended), 25MHz, or 26MHz frequency. This clock source provides a reference for all non-RTC functions. OSC0 clock input has OSC0_IN, OSC0_OUT, and OSC0_GND pins.
- OSC1: low-speed clock input, running at 32.768kHz, for powering the RTC. OSC1 clock input has OSC1_IN, OSC1_OUT, and OSC1_GND pins. This clock source is disabled by default and is not necessary. If needed, it can receive the internal 32kHz RC crystal signal.

In the above figure, Rbias and Rd are optional. If an accurate frequency cannot be provided, Rbias can be used for flexible calibration and can be DNP (not included in the schematic or left empty). However, if Rd is not needed, it must be replaced with a wire, otherwise it will cause an open circuit.

In the reference design, OSC0 uses a 7A-24.000MAAJ-T 24MHz crystal oscillator, 18pF capacitor, and 1MΩ resistor as Rbias.

RTC_KALDO_ENN pin is externally pulled down by default (10k resistor) to enable the internal RTC LDO.

## Burn-in and Debug Interface

In the reference design, use the JTAG interface.

https://octavosystems.com/octavosystems.com/wp-content/uploads/2017/07/JTAG.jpg

## Other peripherals

### Boot Configuration

The boot configuration table can refer to the "SYSBOOT Configuration Pins" section of the [AM335x Technical Reference Manual (TRM)](http://www.ti.com/lit/pdf/spruh73).

In the reference design, we connect as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110132.png)

Configure the following parameters:

- Set the clock frequency to 24Mhz
- Disable CLKOUT1 output through XDMA_EVENT_INTR0, which is only used for JTAG simulation.
- Set the boot order to SPI0 -> MMC0 -> USB0 -> UART0

### User Buttons and LEDs

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110906.png)

### Peripheral Pinout

## Reference and Acknowledgements

- [SO YOU WANT TO BUILD AN EMBEDDED LINUX SYSTEM?](https://jaycarlson.net/embedded-linux/#)
- [OSD335x-SM System-in-Package Smallest AM335x Module, Quickest Design](https://octavosystems.com/octavo_products/osd335x-sm/#Technical%20Documents)
- [OSD335x Reference Design Tutorial Series](https://octavosystems.com/app_notes/osd335x-design-tutorial/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
