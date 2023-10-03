# RobotCtrl_Func - Peripheral Expansion Board

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527113505.png)

Project Repository: [**linyuxuanlin/RobotCtrl/RobotCtrl_Func**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func)

Online Preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func_V0.8B.zip"
  ></div>
</div>

Note: This project is included in the [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/en/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Schematic Design

The main functions of RobotCtrl_Func are as follows:

- 12V power input, 5V power input/output, 3.3V power output (with test points)
- 5V to 3.3V voltage regulator circuit * 2 (for sensors/Ethernet, with test points)
- Ethernet communication circuit
- CAN communication circuit * 2
- Serial communication circuit (RS-232 and TTL levels)
- Buzzer circuit
- User buttons * 2
- User LEDs * 3
- MPU6050 attitude sensor module
- Infrared ranging sensor interface * 4
- Ultrasonic interface * 5
- User GPIO interface * 6
- B2B connector (with all IO pins)
- SW download interface

### Power Supply

The RobotCtrl_Func board has 2 built-in LDOs, similar to those in the RobotCtrl_Core board. One LDO is used for external sensor peripherals, while the other is used solely for the Ethernet circuit.

The Ethernet communication circuit is based on an Ethernet PHY chip and uses the RMII interface to communicate with the microcontroller. Communication is achieved through an RJ45 port with a built-in isolation transformer that connects to an external network cable. The Ethernet circuit's clock uses an external 25M passive crystal oscillator and requires independent power to reduce power interference. The same low-dropout linear regulator power supply scheme as the core board is used to power the Ethernet circuit separately. The principle of Ethernet communication can be found in the article "HAL Library Development Notes - Ethernet Communication (LwIP)."

The CAN communication circuit is built on a CAN transceiver chip and uses CAN differential voltage transmission. The CAN protocol controller (such as a microcontroller) is connected to the transceiver through a serial line (RX/TX), which is then converted into a CAN signal (CANH/CANL) on the transceiver and selects high-speed/silent mode through the RS pin. A 120Ω terminal resistor must be added to the CAN bus to match the impedance and reduce signal reflection. The principle of CAN communication can be found in the articles "Communication Protocol - CAN" and "HAL Library Development Notes - Serial Communication."

The serial communication circuit is based on a UART chip and uses a serial port to communicate with external devices. The UART chip converts parallel data into serial data for transmission and converts serial data into parallel data for reception. The principle of serial communication can be found in the article "HAL Library Development Notes - Serial Communication."

The RobotCtrl_Func board is equipped with a serial communication circuit with RS-232 level and additionally has a USART1/UART5 with TTL level. The principle of serial communication can be referred to in the articles "Communication Protocol - Serial Communication" and "HAL Library Development Notes - Serial Communication".

The RS-232 communication circuit uses a chip that converts TTL to 232 level to convert the TTL of the microcontroller to RS-232 level. To improve EMC performance, the DB9 socket shell connection pin can be connected to a TVS diode to ground, and the TTL to 232 chip requires an external power decoupling and bootstrap capacitor.

The buzzer circuit uses a 12V buzzer and can be controlled by a transistor.

The principle of user buttons and LEDs can be referred to in RobotCtrl_Core, and will not be further explained here.

The MPU6050 module is directly mounted and reserved for I2C interface for communication with the microcontroller. The principle of I2C communication can be referred to in the articles "Communication Protocol - I2C" and "HAL Library Development Notes - I2C Communication (MPU6050)".

The interface for the infrared ranging sensor is also available.

Interface Circuit for Four Infrared Ranging Sensors

The interface circuit for the four infrared ranging sensors uses 12V power and signal (NPN normally open type). Therefore, 12V is supplied from RobotCtrl_Power and four optocoupler isolation chips are added to transmit high and low level signals. The design of the optocoupler isolation circuit requires calculating the resistance value of the current limiting resistor based on the current size to ensure that it is within the triggering voltage range specified in the data sheet. The principle of optocouplers can be found in the article "Basic Components - Optocouplers".

Power Input Interface and B2B Connector

The power input interface of the peripheral expansion board has 4 rows of pins for connection with the power supply board at the bottom. The B2B connector is used for power supply and data communication for the main control board.

Hardware Testing

Power Testing

Power Input (all test items require power to be connected in this way):

- VCC_12V: input through P1.
- VCC_5V: input through P2 or J1_1/2.
- GND: connected to the ground through P3, P4, J1_31/32 or J2_30/31.

5V to 3.3V Voltage Regulator (for sensors):

- VCC_3V3S: measure whether the voltage at both ends of C30 is 3.3V.

5V to 3.3V Voltage Regulator (for Ethernet):

- VCC_3V3E: measure whether the voltage at both ends of C26 is 3.3V.

On-board Sensor Testing

User Button:

- Configure PE2/PE3 as GPIO pull-up input mode, press the button to read low level, release to high level.

User LED:

- Configure PC6/PC7/PC8 as GPIO output mode, output high level, LED lights up in sequence; output low level, LED turns off.

MPU6050 Attitude Sensor Module:

- Measure whether the 1st pin of M1 module is connected to VCC_3V3S.
- Test the connectivity of IO pins.

Buzzer:

- Measure whether the positive pole of BUZZER1 is connected to VCC_12V.
- Configure PC9 as GPIO output mode, output high level, the buzzer makes sound; output low level, the buzzer does not make sound.

Serial Port to RS232:

- Measure whether both ends of C3 are connected to VCC_3V3S.
- Run the test program and test through PB10/PB11 pins.

CAN Bus Communication:

- Measure whether the voltage at both ends of C10/C13 is VCC_5V.
- Run the test program (loopback test) and test through PD0/PD1, PB12/PB13 pins.

Ethernet communication:

- Measure whether IC2_9 to ground is VCC_3V3S voltage.
- Measure whether VDD1A/VDD2A to ground is VCC_3V3E voltage.
- Run the test program and test Ethernet communication through the RMII interface.

### Interface test

Infrared ranging sensor interface:

- Measure whether the 1st pin of J16/J17/J18/J19 sockets to ground is VCC_12V voltage.
- Configure PF2/PF3/PF4/PF5 as GPIO pull-down input, and make IR1/IR2/IR3/IR4 high level (VCC_12V) externally, then PF2/PF3/PF4/PF5 will read high level; otherwise, it will be low level.

Ultrasonic interface:

- Measure whether the 4th pin of J3/J4/J5/J6/J7 sockets to ground is VCC_3V3S voltage.
- Test IO pin connectivity.

User GPIO interface:

- Measure whether the 4th pin of J9/J10/J11 sockets to ground is VCC_3V3S voltage.
- Test IO pin connectivity.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.