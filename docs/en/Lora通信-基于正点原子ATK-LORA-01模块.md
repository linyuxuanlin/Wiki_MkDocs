# Lora Communication - Based on the DFRobot ATK-LORA-01 Module

The ATK-LORA-01 is a small-sized, low-power, low-consumption, high-performance long-range LORA wireless serial module. The module is designed with the efficient ISM frequency band RF SX1278 spread spectrum chip. The module operates at a frequency range of 410MHz to 441MHz, with a step frequency of 1MHz, and a total of 32 channels. Various parameters such as serial port rate, transmission power, air rate, and operating mode can be modified online through AT commands, and firmware upgrade is supported.

## Basic Module Parameters

- Operating Frequency: 410-441 MHz, 32 channels
- Industrial Frequency Band: Default 433MHz license-free band
- Wireless Rate: 6 adjustable levels (0.3, 1.2, 2.4, 4.8, 9.6, 19.2Kbps)
- Communication Interface: TTL serial, UART serial, 8N1, 8E1, 8O1, with 8 baud rates ranging from 1200 to 115200 (default 9600, 8N1)
- Transmission Power: 100mW (20dB), 4 adjustable levels (0-3), each level increases or decreases by approximately 3dBm
- Operating Voltage: 3.3-5V
- Operating Current: 2.3uA-118mA
  - Transmission: 118mA (20dBm 100mW, voltage 5V)
  - Reception: 17mA (Mode 0, Mode 1), minimum of approximately 2.3uA (Mode 2+2S Wake-up)
- Operating Temperature: -40~85℃
- Receiver Sensitivity up to -136dBm, transmission distance of 3000 meters
- Dual 512 circular FIFO

## Interface Definition

| Name | IO Mode        | Description                                                                 |
| ---- | -------------- | --------------------------------------------------------------------------- |
| MD0  | Input          | Configuration parameter entry; When powered on, it enters firmware upgrade mode in conjunction with the AUX pin |
| AUX  | ① Output; ② Input | ① Used to indicate the module's operating status, wake up the external MCU; ② When powered on, it enters firmware upgrade mode in conjunction with the MD0 pin |
| RXD  | Input          | TTL serial input, connected to external TXD output pin                       |
| TXD  | Output         | TTL serial output, connected to external RXD input pin                       |
| GND  |                | Ground                                                                      |
| VCC  |                | DC 3.3~5V power input                                                        |

Notes:

1. The module's pin level is 3.3V, so level conversion adaptation is required for communication with 5V microcontrollers.
2. The wireless serial module operates at TTL level, so it should be connected to a MCU with TTL level.

## Mode Configuration

The MD0 and AUX pins have two functions, and different states are entered based on their combination. When the module is powered on for the first time, the AUX pin is in input mode. If the MD0 and AUX pins are both connected to 3.3V TTL high level and maintained for 1 second (with no change in pin level), the module will enter firmware upgrade mode and wait for firmware upgrade. Otherwise, it will enter wireless communication mode (the AUX pin will return to output mode to indicate the module's operating status).

The MD0 and AUX pins have internal pull-down resistors and are low level when floating. They are pulled high to 3.3V TTL high level.

| Function         | Description              | Method of Access                   |
| ---------------- | ------------------------ | ---------------------------------- |
| Configuration    | Module parameter setup (AT command) | After power on, AUX floating, MD0 pulled high |
| Communication    | Used for wireless communication | After power on, AUX floating, MD0 floating |
| Firmware Upgrade | Used for firmware upgrade | After power on, AUX pulled high, MD0 pulled high, hold for 1s |

In wireless communication mode, the AUX pin is set as an output to indicate the module's working status.

## Function Configuration

Under "Configuration", the serial port needs to be set as follows: Baud rate "115200", Stop bit "1", Data bit "8", Parity bit "None". The module's working parameters can be set using AT commands. Refer to the following AT command table for configuration:

| Command   | Function                      |
| --------- | ----------------------------- |
| AT        | Test module response          |
| AT+MODEL? | Query device model            |
| AT+CGMR?  | Get software version number   |
| AT+UPDATE | Check if device is in firmware upgrade mode |
| ATE1      | Command echo on               |
| ATE0      | Command echo off              |
| AT+RESET  | Module reset (reboot)         |
| AT+DEFAULT | Restore factory settings      |
| AT+FLASH= | Save parameters               |
| AT+ADDR=? | Query device configuration address range |
| AT+ADDR?  | Query device address          |
| AT+ADDR=  | Configure device address      |
| AT+TPOWER=? | Query transmission power configuration range |
| AT+TPOWER? | Query transmission power      |
| AT+TPOWER= | Configure transmission power  |
| AT+CWMODE=? | Query configuration working mode range |
| AT+CWMODE? | Query working mode            |
| AT+CWMODE= | Configure working mode        |
| AT+TMODE=? | Query configuration sending status range |
| AT+TMODE?  | Query sending status          |
| AT+TMODE=  | Configure sending status      |
| AT+WLRATE=? | Query wireless rate and channel configuration range |
| AT+WLRATE? | Query wireless rate and channel |
| AT+WLRATE= | Configure wireless rate and channel |
| AT+WLTIME=? | Query configuration sleep time range |
| AT+WLTIME? | Query sleep time              |
| AT+WLTIME= | Configure sleep time          |
| AT+UART=? | Query serial port configuration range |
| AT+UART?  | Query serial port configuration |
| AT+UART=  | Configure serial port         |

When exiting the configuration function (MD0=0), the module will reconfigure the parameters. During the configuration process, AUX will remain at a high level and will output a low level after completion. The module will return to idle state.

## Sleep Time

The sleep time is the interval for the receiving party to listen. For the transmitting party, it is the duration for continuously transmitting the wake-up code. When the module is in "wake-up mode", it will automatically add the wake-up code for configuring the sleep time before the user data. When the module is in "power-saving mode", the configured sleep time will be the interval for listening.

## Device Modes

### General Mode (Mode 0)

- Transmitting: The module receives user data from the serial port and transmits wireless data packets with a length of 58 bytes. When the user input data reaches 58 bytes, the module will start wireless transmission. At this time, the user can continue to input the data to be transmitted. If the number of bytes to be transmitted by the user is less than 58 bytes, the module will wait for 1 byte of time. If there is no further user input, it will be considered as the end of data. At this time, the module will transmit all the data wirelessly. When the module starts sending the first packet of user data, the AUX pin will output a high level. After the module sends all the data through the RF chip and starts transmission, the AUX will output a low level. This indicates that the last wireless data packet has been transmitted. The user can continue to input data up to 512 bytes. The data packets sent through the general mode can only be received by modules in the general mode and wake-up mode.
- Receiving: The module keeps the wireless receiving function open and can receive data packets sent by modules in the general mode and wake-up mode. After receiving a data packet, the AUX pin of the module outputs a high level. After a delay of 2-3ms, the module starts to send the wireless data through the TXD pin of the serial port. After all the wireless data is output through the serial port, the AUX pin of the module outputs a low level.

### Wake-up Mode (Mode 1)

- Transmitting: The conditions for starting data packet transmission by the module are the same as in the general mode. The only difference is that the module will automatically add a wake-up code (sleep time) before each data packet. The length of the wake-up code depends on the sleep time set in the user parameters. The purpose of the wake-up code is to wake up the receiving module in power-saving mode. Therefore, the data transmitted in wake-up mode can be received by modules in general mode, 1, and 2.
- Receiving: Same as the general mode.

### Power-saving Mode (Mode 2)

- Transmitting: The module is in sleep mode, and the serial port is closed, so it cannot receive serial port data from an external MCU. Therefore, this mode does not have the function of wireless transmission.
- Receiving: In power-saving mode, the transmitting party must work in wake-up mode. The wireless module listens to the wake-up code periodically. Once a valid wake-up code is received, the module will continue to be in receiving state, waiting for the entire valid data packet to be received. Then, the module will output a high level on the AUX pin, and after a delay of 2-3ms, it will open the serial port to send the received wireless data through TXD. After completion, the AUX pin will output a low level. The wireless module will continue to work in the "sleep-listen" state. By setting different wake-up times, the module has different response delays and power consumption. Users need to find a balance between communication delay and average power consumption.

### Signal Strength Mode (Mode 3)

The signal strength mode can be used to view the signal strength of both communication parties and provide a reference for evaluating communication quality.

- Transmitting: Same as the general mode.
- Receiving: Outputs information about signal strength.

![](https://img.wiki-power.com/d/wiki-media/img/20220118110058.png)

SNR: Signal-to-Noise Ratio (larger values indicate more stability), RSSI: Received Signal Strength Indication (larger values indicate stronger signal)

## Communication Modes

- Transparent Transmission: For example, Device A sends 5 bytes of data AA BB CC DD EE to Device B, and Device B receives the data AA BB CC DD EE. (Transparent transmission is for communication between devices with the same address and the same communication channel. User data can be in the form of characters or hexadecimal data).
  - Point-to-Point
  - Point-to-Multi-point
  - Broadcast Listening
- Directed Transmission: For example, Device A (address: 0x1400, channel: 0x17 (channel 23, 433MHz)) needs to send data AA BB CC to Device B (address: 0x1234, channel: 0x10 (channel 16, 426MHz)). The communication format is: 12 34 10 AA BB CC, where 1234 is the address of module B and 10 is the channel. Module B can receive AA BB CC. Similarly, if Device B needs to send data AA BB CC to Device A, the communication format is: 14 00 17 AA BB CC, and Device A can receive AA BB CC. (Directed transmission can achieve communication between devices with different addresses and communication channels. The data format is hexadecimal. The sending format is: high byte of address + low byte of address + channel + user data).
  - Point-to-Multi-point
  - Broadcast Listening

Broadcast and Data Monitoring: Setting the module address to 0xFFFF allows you to monitor the data transmission of all modules on the same channel. The data sent can be received by any module with any address on the same channel, thus serving the purpose of broadcasting and monitoring.

## Transparent Transmission Mode

### Point-to-Point

![](https://img.wiki-power.com/d/wiki-media/img/20220118110614.png)

- Two modules with the same address, same channel, and the same wireless rate (not serial baud rate) can send and receive data to each other (one sends, one receives).
- Each module can perform sending/receiving.
- Data is completely transparent, what is sent is what is received.

|          | Sending Module | Receiving Module |
| -------- | -------------- | ---------------- |
| Quantity | 1              | 1                |
| Content  | Data           | Data             |

For example:

Devices A and B have the address 0x1234, channel 0x12, and the same rate.  
Device A sends: AA BB CC DD  
Device B receives: AA BB CC DD

The transparent transmission method is simple, just use the Lora module as a serial port. Device A can send data through the serial port, and Device B can receive it from the serial port, and vice versa.

### Point-to-Multi

![](https://img.wiki-power.com/d/wiki-media/img/20220118110709.png)

- Modules with the same address, same channel, and the same wireless rate (not serial baud rate), any module can send data and all other modules can receive it.
- Each module can perform sending/receiving.
- Data is completely transparent, what is sent is what is received.

|          | Sending Module | Receiving Module |
| -------- | -------------- | ---------------- |
| Quantity | 1              | N                |
| Content  | Data           | Data             |

The difference from point-to-point is that there can be multiple receiving modules.

For example:
Devices A to F have the address 0x1234, channel 0x12, and the same rate.  
Device A sends: AA BB CC DD  
Devices B to F receive: AA BB CC DD

### Broadcast Monitoring

![](https://img.wiki-power.com/d/wiki-media/img/20220118110853.png)

- If the module address is 0xFFFF, the module is in broadcast monitoring mode. The data sent can be received by all other modules with the same rate and channel (broadcast); at the same time, it can monitor the data transmission of all modules on the same rate and channel (monitoring).
- Broadcast monitoring does not require the addresses to be the same.

|          | Sending Module | Receiving Module |
| -------- | -------------- | ---------------- |
| Quantity | 1              | N                |
| Content  | Data           | Data             |

The difference from point-to-multi is that the addresses can be different.

For example:
Device A has the address 0xFFFF, devices B to F have different addresses. Devices B and C have the address 0x1234, and devices D, E, and F have the address 0x5678. All devices A to F have the same rate.  
Broadcast:  
Device A broadcasts: AA BB CC DD  
Devices B to F receive: AA BB CC DD  
Monitoring:  
Device B sends to C: AA BB CC DD  
Device A monitors: AA BB CC DD  
Device D sends to E and F: 11 22 33 44  
Device A monitors: 11 22 33 44

## Directed Transmission Mode

### Point-to-Point

- When sending, the module can modify the address and channel, allowing the user to specify the data to be sent to any address and channel.
- It can achieve networking and relay functions.

|          | Sending Module       | Receiving Module |
| -------- | -------------------- | ---------------- |
| Quantity | 1                    | 1                |
| Content  | Address + Channel + Data | Data             |

The difference from point-to-point transparent transmission is that the module address and channel can be changed, but the rate remains the same.

Translate into English:

![](https://img.wiki-power.com/d/wiki-media/img/20220118111903.png)

For example:
Device A address 0X1234, channel 0X17;
Device B address 0xABCD, channel 0X01;
Device C address 0X1256, channel 0x13.

Device A sends: AB CD 01 AA BB CC DD
Device B receives: AA BB CC DD
Device C receives: None

Device A sends: 12 56 13 AA BB CC DD
Device B receives: None
Device C receives: AA BB CC DD

#### No code test

Prepare 2 USB to TTL converters and 2 LoRa modules. Connect them to the USB to TTL converters (power, common ground, TX/RX connections). Connect the MD0 pins of the two LoRa modules to VCC, then plug them into the computer's USB ports. Open the configuration software and set the following parameters:

Device A:

- General mode
- Directed transmission
- **Baud rate: 115200 (must be 115200)**
- Parity: None
- Air rate: 19.2k
- Sleep time: 1s
- **Module address: 0**
- **Communication channel: 0**
- Transmit power: 20dBm

Device B:

- General mode
- Directed transmission
- **Baud rate: 115200 (must be 115200)**
- Parity: None
- Air rate: 19.2k
- Sleep time: 1s
- **Module address: 65534**
- **Communication channel: 10**
- Transmit power: 20dBm

After configuring, click "Save Configuration" and **remove the MD0 pins before disconnecting the power**.

Power on the two modules again, open the configuration software, and check "HEX" (hexadecimal) for both transmit and receive.

In the transmit area of Device A, enter `FF FE 0A 11 12 13 14`, click "Send", and you will receive `11 12 13 14` in the receive area of Device B. Or, in the transmit area of Device B, enter `00 00 00 11 12 13`, and you will receive `11 12 13` in the receive area of Device A.

In this case, `FF FE` is the hexadecimal representation of the address 65534 of Device B, and the channel is 10 (hexadecimal representation is `0A`). The transmitted data is `11 12 13 14`. Similarly, the data transmitted by Device B includes the address of Device A `00 00`, channel `00`, and content `11 12 13`. The format of the transmitted data is **high address + low address + channel + user data**.

#### Testing with code

Point-to-point directed transmission only adds an address byte compared to point-to-point transparent transmission. It can be defined as follows:

```c title="main.c"
/* USER CODE BEGIN PV */
uint8_t B_Addr[2] = { 0xFF, 0xFE };
uint8_t B_Chan[1] = { 0x0A };
/* USER CODE END PV */
```

After configuring the code with UART (HAL library environment), send the address bytes before sending data each time:

```c title="main.c"
HAL_UART_Transmit(&huart1, B_Addr, 2, 0xFFFF);
HAL_UART_Transmit(&huart1, B_Chan, 1, 0xFFFF);
```

This way, the receiving device (Device B) can receive a frame of data sent by Device A (excluding the address bytes).

### Broadcast Listening

![](https://img.wiki-power.com/d/wiki-media/img/20220118112544.png)

- If the module address is 0xFFFF, the module is in broadcast listening mode, and the data sent can be received by all other modules with the same rate and channel (broadcast); at the same time, it can listen to data transmissions from all modules on the same rate and channel (listening);
- Broadcast listening does not require the addresses to be the same.
- The channel address can be set. When the address is 0xFFFF, it is in broadcast mode; otherwise, it is in directed transmission mode.

|          | Sending Module   | Receiving Module |
| -------- | ---------------- | ---------------- |
| Quantity | 1                | N                |
| Content  | 0xFFFF+Channel+Data | Data             |

For example:

Device A has the address 0xFFFF and operates on channel 0x12.  
Devices B and C have the address 0x1234 and operate on channel 0x13.  
Device D has the address 0xAB00 and operates on channel 0x01.  
Device E has the address 0xAB01 and operates on channel 0x12.  
Device F has the address 0xAB02 and operates on channel 0x12.

Device A broadcasts: FF FF 13 AA BB CC DD  
Devices B and C receive: AA BB CC DD

Device A sends: AB 00 01 11 22 33 44  
Only device D receives: 11 22 33 44

Device E sends: AB 02 12 66 77 88 99  
Device F receives: 66 77 88 99  
Device A listens: 66 77 88 99

## References and Acknowledgements

- [LORA Module ATK-LORA-01](http://www.openedv.com/docs/modules/iot/atk-lora-01.html)
- [ATK-LORA Module Usage Tutorial by DFRobot](https://www.bilibili.com/video/BV1D44y1t7bn)
- [ATK-LORA-01 Wireless Serial Module Data Download and Technical Discussion](http://www.openedv.com/thread-309019-1-1.html)
- [Testing Method for Two LORA Modules Transmitting Data in General Mode (Using PC Testing)](http://www.openedv.com/forum.php?mod=viewthread&tid=288951)
- [ATK-LORA-01 Wireless Serial Module Only Receives 00](http://www.openedv.com/forum.php?mod=viewthread&tid=328190&highlight=ATK-LORA-01)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.