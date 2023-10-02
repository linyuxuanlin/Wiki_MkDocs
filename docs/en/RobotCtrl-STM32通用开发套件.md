# RobotCtrl - STM32 Universal Development Kit

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220416181125.jpeg)

Project Repository: [**linyuxuanlin/RobotCtrl**](https://github.com/linyuxuanlin/RobotCtrl)

RobotCtrl - STM32 Universal Development Kit includes three boards:

- [**RobotCtrl_Core - Core Board**](https://wiki-power.com/RobotCtrl_Core-%E6%A0%B8%E5%BF%83%E6%9D%BF)
- [**RobotCtrl_Core - Peripheral Expansion Board**](https://wiki-power.com/RobotCtrl_Func-%E5%A4%96%E8%AE%BE%E6%8B%93%E5%B1%95%E6%9D%BF)
- [**RobotCtrl_Power - Power Supply Board**](https://wiki-power.com/RobotCtrl_Power-%E7%94%B5%E6%BA%90%E4%BE%9B%E7%94%B5%E6%9D%BF)

## Design Requirements

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527111854.png)

Note: The following is a design summary, please refer to the relevant articles for specific content.

### Design Concept of RobotCtrl_Core

The schematic design of RobotCtrl_Core includes power supply circuit, MCU minimum system, USB communication, B2B connector, user buttons and LED section.

The power supply circuit uses LDO, which has the advantages of relatively simple circuit, small output ripple, low cost, and small layout area. With the corresponding decoupling capacitor and power indicator, the 5V voltage input from the USB port or B2B connector is stabilized and converted to 3.3V (maximum current is 1A).

In the design of the minimal system, the power supply is a 3.3V power input with corresponding decoupling capacitors. In addition, the ADC dedicated power supply VDDA is connected to VDD through a 120Ω magnetic bead and additional decoupling capacitors are added. The reset circuit adds an external button to trigger the NRST pin to reset the system to low level. The clock circuit adds an external high-speed clock HSE, which is connected to the OSC_IN and OSC_OUT pins through a passive crystal oscillator. The startup mode is set to boot from the on-chip flash memory by default, that is, BOOT0 is low and BOOT1 is any level, and a 10k resistor is used to pull BOOT0 to ground. The download and debug circuit directly leads the SW interface (DIO/CLK) out.

For the USB communication circuit design, the STM32F4 has a built-in USB peripheral. An external USB Micro socket is selected, and a 10Ω current limiting resistor is connected in series on the data line. TVS and ESD diodes are added to the signal line and power line respectively to meet EMC requirements.

The B2B connector is used for power supply and data communication with RobotCtrl_Func. In this design, two B2B connectors are sufficient to lead out all the IOs of the STM32F407ZE microcontroller, enhancing the expandability in the later stage.

The design concept of RobotCtrl_Func mainly includes serial communication (RS-232/TTL), CAN communication, Ethernet communication, attitude sensor, ultrasonic interface, infrared ranging interface (with optocoupler isolation), buzzer, SW download and debug interface, user buttons and LEDs, general GPIO interface, power supply, B2B connector and other modules.

The serial communication circuit provides TTL and RS-232 level interfaces. Among them, the TTL directly uses the TX/RX pins of USART1 and UART5, while the RS-232 communication circuit uses a chip to convert the TTL level of the microcontroller to RS-232 level. To improve EMC performance, the DB9 socket shell connection pin can be connected to the TVS diode to ground, and the TTL to 232 chip requires additional power supply decoupling and bootstrap capacitors.

The CAN communication circuit is built based on the CAN transceiver chip and transmitted through CAN differential voltage. A 120Ω terminal resistor needs to be added to the CAN bus to match the impedance and reduce signal reflection.

Ethernet communication is based on Ethernet PHY chips, using the RMII interface to communicate with the microcontroller, and communicating through an RJ45 port with an external network cable with a built-in isolation transformer. The clock of the Ethernet circuit uses an external 25M passive crystal oscillator and requires independent power to reduce power interference. Here, the same low-dropout linear regulator power supply scheme as the core board is used to provide power to the Ethernet circuit separately.

The interface circuit of the four-channel infrared ranging sensor is powered by 12V and signals (NPN normally open type) from RobotCtrl_Power. Therefore, 12V is drawn from RobotCtrl_Power to power it, and four optocoupler isolation chips are added to transmit high and low level signals. The design of the optocoupler isolation circuit requires calculating the resistance value of the current limiting resistor according to the current size to ensure that it is within the trigger voltage range specified in the data sheet. The design of the attitude sensor module uses the MPU6050 module and reserves the I2C interface for communication with the microcontroller.

### Design concept of RobotCtrl_Power

The schematic design of RobotCtrl_Power mainly consists of XT60 dual power input, 24V to 12V, 24V to 5V voltage stabilization circuits, as well as enable switches and power indicator lights, reverse connection protection, overvoltage protection circuits, etc.

The power input uses two parallel XT60 sockets, one of which is used for power input, and the other can be connected to a backup power supply or used as a battery power output for external use.

The reverse connection protection circuit uses MOS tube reverse connection protection design. When the power is normally connected, the MOS is conductive; when it is reversed, it is cut off to protect the circuit. In this design, a domestic P-MOS is used for reverse connection protection, and the gate voltage when forward conduction is locked by resistor voltage division and voltage stabilization diodes. To achieve overvoltage protection and ESD protection, TVS diodes are connected in parallel at the power input end.

The design of the 12V/5V voltage stabilization circuit uses a Buck non-isolated switch voltage stabilization scheme based on LMR14050. According to the principle of Buck topology and the reference of the voltage stabilization chip data sheet, the resistance value of the feedback resistor is selected to calculate the proportion to keep the output at 12V/5V. When selecting the inductor model, it is necessary to pay attention to the maximum saturation current needs to be greater than the ripple current, and leave room for margin; Schottky diodes are selected to achieve high-speed switching, and their voltage and current also need to meet the requirements of the circuit. In addition, input and output need to be connected in parallel with decoupling capacitors of appropriate sizes to filter out ripples.

The enable switch can control the opening and closing of the voltage stabilization output, and the enable pin connected to the Buck chip is used to achieve soft start and soft shutdown of the voltage stabilization output. The power indicator light can indicate the output status of the 12V/5V voltage stabilization to the user.

## References and Acknowledgments

This project is my personal graduation design. During the design, welding, and debugging of the project, I encountered many problems of various sizes. With the strong help of my mentor, colleagues, and friends, I finally succeeded in completing the project and also received the honor of an excellent graduation design. Thank you all! 

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.