# RobotCtrl_Core - Core Board

![](https://img.wiki-power.com/d/wiki-media/img/20220527113423.png)

Project Repository: [**linyuxuanlin/RobotCtrl/RobotCtrl_Core**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core)

Project Online Preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core_V2.81B.zip"
  ></div>
</div>

Note: This project is included in the [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/en/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Schematic Design

The main functions of RobotCtrl_Core are as follows:

- Power supply voltage stabilization circuit (5V to 3.3V, with test points)
- Microcontroller minimum system
  - Power supply circuit (power supply decoupling, ADC analog power supply)
  - Reset circuit (external reset button)
  - Clock circuit (HSE passive crystal oscillator)
  - Download and debug interface (SW)
  - Boot mode (select boot from main flash memory)
  - USB power supply and communication circuit (USB-Micro)
- B2B connector (with all IOs)
- On-board peripherals

### Power Supply Circuit

RobotCtrl_Core can be powered by a 5V power supply through the USB interface or B2B connector, and converted to 3.3V for use by the microcontroller core and on-board peripherals. The voltage stabilization circuit uses an LDO (AMS1117-3.3, with a maximum current of 1A), with a power indicator light and critical test points reserved.

The basic principle of LDO can be referred to the article "Power Supply Topology - Linear Regulator".

### Minimum System for Microcontroller

The design of the minimum system for microcontroller is divided into several parts: power supply, reset, download debugging, clock, and startup mode. Basic knowledge can be referred to the articles "How to Design a Minimum System for Microcontroller" and "STM32F4 Hardware Development".

### Power Circuit

Decoupling Capacitor:

- VDD: A total of 10 μF ceramic capacitor, plus a 100 nF ceramic capacitor next to each VDD pin.
- VDDA: 100 nF ceramic capacitor + 1 µF ceramic capacitor.

VCAP Capacitor

- Each is connected to a 2.2 µF ceramic capacitor to ground.

### Reset Circuit

Enable the power monitor, that is, PDR_ON is pulled up through a 120Ω resistor. In addition, a reset button with hardware debouncing is also added.

### Clock Circuit

The external high-speed clock (HSE) uses Murata 8M passive crystal oscillator.

### Download and Debug Interface

This design directly leads out the download and debug interface without external pull-up/down resistors (because STM32 has integrated them internally).

### Startup Mode

Select to start from the main flash memory, that is, BOOT0 is connected in series with a 10 K pull-down resistor, and BOOT1 is arbitrary.

### USB Power and Communication Circuit (USB-Micro)

STM32 has a built-in USB peripheral, so it only needs to directly lead out the interface (on the STM32F07ZE chip, it is PA11 and PA12) to achieve USB communication.

The USB interface also supports external power supply function (VUSB).

## B2B Connector

B2B connectors use the 3710 series from DFRobot. The RobotCtrl_Core core board uses a pair of 3710M060037G3FT01 (male connectors), and the RobotCtrl_Func expansion board uses a pair of F060037G0FR01 (female connectors) to match. One pair of B2B connectors (a total of 120 pins) is enough to fully utilize all the IO of the STM32F407ZE, maximizing system resources.

For information on the B2B connectors, please refer to the [3710F terminal data](http://www.openedv.com/thread-78182-1-1.html).

## User Buttons and LEDs

In order to perform simple verification and debugging, the RobotCtrl_Core board is equipped with a user button and a user LED. The button is configured as a GPIO input mode with internal pull-up and a MLCC capacitor is added for hardware debouncing. The LED is configured as a GPIO output mode, with the pin set to high to light up, and a resistor is connected in series to limit the current.

Please refer to the schematic for specific pin information.

## Hardware Testing

Power testing requires 5V power supply from the USB socket (or power supply through the peripheral expansion board via the B2B connector), and the corresponding voltage can be measured at the 3.3V test point. The actual test result is 3.32V, which passes verification.

Function testing is performed by burning the initial program (user button controls user LED) and testing power-on, program burning, reset button and user button, power LED and user LED, and USB function. In actual testing, the initial program can be burned into the MCU core board normally through ST-Link. The reset button can reset the system normally; in the test program, the user LED can be turned on/off by pressing the user button; when powered on, the power LED lights up normally. For USB function testing, a program using a USB virtual serial port is used. Open the serial port tool (with any baud rate), send any character, and the same character will be returned, passing the test.

## References and Acknowledgments

- [Explanation of STM32's PDR_ON pin (reprint + supplement)](https://blog.csdn.net/Frankenstien_/article/details/105971841)
- [DFRobot's STM32-F407 Explorer Chapter 56 USB Card Reader (Slave) Experiment](https://zhuanlan.zhihu.com/p/136163591)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
