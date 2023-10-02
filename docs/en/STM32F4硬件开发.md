# STM32F4 Hardware Development

This article will explain the minimum system of the STM32F4 MCU, including power, clock, reset, startup mode, and debugging management.

## Power

The normal operating voltage of the STM32F4 is 1.8-3.6 V (in some cases it can be reduced to below 1.7 V, as stated in the data sheet), with a built-in regulator providing an internal 1.2 V digital power supply.

When the main power supply VDD is disconnected, the voltage of VBAT can be used to power the RTC and backup registers.

### Introduction to each pin

#### ADC power and reference voltage

To improve conversion accuracy, the ADC has an independent power pin that can be filtered and shielded from noise on the PCB.

The ADC voltage source is input from the separate VDDA pin. When designing the circuit, VSSA should be connected to the same power ground, not VSS.

If the chip package has more than 100 pins, there will be VREF+ and VREF- pins, which are used to input external reference voltage to the ADC. VREF- should be connected to the internal VSSA. If the chip has less than 100 pins, these two pins are not led out and are internally connected to VDDA and VSSA.

#### Backup battery power

If it is necessary to preserve the contents of the backup register after VDD is disconnected, VBAT can be connected to a battery or other power source.

VBAT can also power the RTC and is controlled by the built-in power-down reset (PDR) circuit in the reset module.

#### Built-in regulator

The built-in regulator is always in the enabled state after reset and has three operating modes:

- Run: The regulator provides full power supply to the 1.2 V domain (core, memory, and digital peripherals).
- Stop: The regulator provides low power supply to the 1.2 V domain while preserving the contents of the registers and SRAM.
- Standby: The regulator is powered off. The contents of the registers and SRAM, except for the standby circuit and backup domain, will be lost.

### Circuit design

The following is the design method for power pins:

- **VDD**
  - **Decoupling Capacitor**: A total of 10 μF ceramic/tantalum capacitor, plus a 100 nF ceramic capacitor for each VDD pin.
- **VDDA**
  - **Decoupling Capacitor**: 100 nF ceramic capacitor + 1 µF ceramic/tantalum capacitor.
  - **Filtering Analog Noise**: Can be connected to VDD through a ferrite bead.
- **VREF+**
  - **Decoupling Capacitor**: If VREF+ function is enabled, a 100 nF and a 1 µF capacitor are required.
  - **Filtering Analog Noise**: Can be connected to VDDA through a 47 Ω resistor.
- **VBAT**: Connect to an external battery (1.65 V-3.6 V). If battery power is not required, connect to the VDD pin.
- **VCAP1/VCAP2**: Connect a 2.2 µF ceramic capacitor (ESR < 2 Ω) to ground for each pin; if only VCAP1 is used, connect a 4.7 µF ceramic capacitor (ESR < 1 Ω).

### Reset and Power Monitoring

#### Power-On Reset (POR) / Power-Down Reset (PDR)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529143014.png)

The STM32F4 chip integrates POR/PDR circuitry, and the specific characteristics of power-on/reset and power-down/reset are shown in the above figure. If this function needs to be disabled, it can be achieved through the PDR_ON pin.

#### System Reset

The trigger conditions for a system reset are:

- NRST pin low level (external reset)
- Window watchdog count expires (WWDG reset)
- Independent watchdog count expires (IWDG reset)
- Software reset (SW reset)
- Low-power management reset

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529143925.png)

The reset source can be determined by checking the reset flag in the control/status register (RCC_CSR).

Even if an external reset circuit is not required, it is recommended to add a pull-down capacitor to improve EMC performance.

## Clock

On the STM32F4, three different clock sources can be used to drive the system clock (SYSCLK):

- HSI (High-Speed Internal clock signal)
- HSE (High-Speed External clock signal)
- PLL clock

There are also two secondary clock sources:

- LSI RC (32 kHz Low-Speed Internal RC) is used to drive independent watchdogs and can also be used to automatically wake up RTC shutdown/standby modes.
- LSE (32.768 kHz Low-Speed External Crystal Oscillator) is used to drive RTC.

If power consumption needs to be reduced, each clock can be individually turned off when not in use.

### External High-Speed Clock (HSE)

There are two ways to provide the HSE clock source: external source (active) and external crystal oscillator/ceramic resonator (passive).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529145726.png)

#### External Source (HSE Bypass)

If an active external clock signal input is selected, a clock source of 1-50 MHz must be provided, with OSC_IN connected to an external clock signal (square wave, sine wave, or triangle wave) with a duty cycle of approximately 50%, and OSC_OUT kept in high-impedance state.

#### External Crystal Oscillator/Ceramic Resonator (HSE Crystal)

If an external crystal oscillator is used, the frequency range is 4-26 MHz. When designing the circuit, the resonator and load capacitance must be placed as close as possible to the oscillator pins to minimize output distortion and start-up stabilization time. The value of the load capacitance must be adjusted appropriately according to the selected oscillator.

CL1 and CL2 should use ceramic capacitors of the same size (5-25 pF, typical value 25 pF).

### External Low-Speed Clock (LSE)

There are two ways to provide the LSE clock source: external source (active) and external crystal oscillator/ceramic resonator (passive).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529152354.png)

#### External Source (LSE Bypass)

If an active external clock signal input is selected, a clock source of below 1 MHz must be provided, with OSC32_IN connected to an external clock signal (square wave, sine wave, or triangle wave) with a duty cycle of approximately 50%, and OSC32_OUT kept in high-impedance state.

#### External Crystal Oscillator/Ceramic Resonator (LSE Crystal)

If an external crystal oscillator is used, the frequency range is 32.768 kHz, which can be used as the clock source for RTC. When designing the circuit, the resonator and load capacitance must be placed as close as possible to the oscillator pins to minimize output distortion and start-up stabilization time. The value of the load capacitance must be adjusted appropriately according to the selected oscillator.

## Boot Mode

The boot mode is also called the bootstrap mode. Three different boot modes can be selected by using the BOOT0 and BOOT1 pins: boot from main flash memory, boot from system memory, and boot from internal SRAM.

For a detailed introduction to the boot mode, please refer to the article [STM32 Boot Mode](https://wiki-power.com/STM32%E7%9A%84%E5%90%AF%E5%8A%A8%E6%A8%A1%E5%BC%8F).

In general, we connect a 10K pull-down resistor to the BOOT0 pin and leave the BOOT1 pin unconnected. If mode switching is required, the following design can be used:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200605163537.png)

## Debugging Management

The STM32 generally uses the SWJ protocol for download and debugging.

### SWJ Debug Port

The STM32F4 has a built-in SWJ (SW/JTAG) interface. Among them, SW-DP has 2 pins (clock + data), JTAG-DP has 5 pins, and some pins are multiplexed. For detailed differences, please refer to the article [Difference and Connection between SWD and JTAG](https://wiki-power.com/SWD%E4%B8%8EJTAG%E7%9A%84%E5%8C%BA%E5%88%AB%E4%B8%8E%E8%81%94%E7%B3%BB).

In STM32F4, the pin allocation of SWJ is as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529210858.png)

### Internal Pull-up and Pull-down of JTAG

JTAG pins cannot be left floating (because they are directly connected to the triggers used for mode debugging control), so they have integrated pull-up and pull-down inside the chip:

- **JNTRST**: internal pull-up
- **JTDI**: internal pull-up
- **JTMS/SWDIO**: internal pull-up
- **TCK/SWCLK**: internal pull-down

After the software releases the JTAG I/O, it can be used as a normal I/O port.

### Hardware Design for Connecting Standard JTAG Sockets

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529211840.png)

## Reference Design

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210529213723.png)

## Reference and Acknowledgements

- [AN4488: Getting started with STM32F4xxxx MCU hardware development](https://www.st.com/content/ccc/resource/technical/document/application_note/76/f9/c8/10/8a/33/4b/f0/DM00115714.pdf/files/DM00115714.pdf/jcr:content/translations/en.DM00115714.pdf)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.