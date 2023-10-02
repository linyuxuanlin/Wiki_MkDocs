# Lora Communication - Based on the DFRobot ATK-LORA-01 Module

The ATK-LORA-01 is a small, low-power, high-performance long-range LORA wireless serial module. The module is designed using the efficient ISM band RF SX1278 spread spectrum chip, with a working frequency of 410MHz~441MHz, with 32 channels in 1MHz frequency steps. Various parameters such as serial port rate, transmission power, air speed, and working mode can be modified online through AT commands, and firmware upgrade is also supported.

## Basic Module Parameters

- Working frequency: 410-441 MHz, 32 channels
- Industrial frequency band: Default 433MHz license-free band
- Wireless rate: 6 levels adjustable (0.3, 1.2, 2.4, 4.8, 9.6, 19.2Kbps)
- Communication method: Serial TTL, UART serial, 8N1, 8E1, 8O1, 8 baud rates from 1200-115200 (default 9600, 8N1)
- Transmission power: 100mW (20dB), 4 levels adjustable (0-3), each level increases or decreases by about 3dBm
- Working voltage: 3.3-5V
- Working current: 2.3uA-118mA
  - Transmission: 118mA (20dBm 100mW voltage 5V)
  - Reception: 17mA (mode 0, mode 1), minimum of about 2.3uA (mode 2+2S wake-up)
- Working temperature: -40~85℃
- Receiver sensitivity up to -136dBm, transmission distance up to 3000 meters
- Dual 512 circular FIFO

## Interface Definition

| Name | IO Mode        | Description                                                                                       |
| ---- | -------------- | ------------------------------------------------------------------------------------------------- |
| MD0  | Input          | Used for configuring module parameters; when powered on, it enters firmware upgrade mode with AUX pin |
| AUX  | ① Output; ② Input | ① Used to indicate module working status, wake up external MCU; ② When powered on, it enters firmware upgrade mode with MD0 pin |
| RXD  | Input          | TTL serial input, connected to external TXD output pin                                           |
| TXD  | Output         | TTL serial output, connected to external RXD input pin                                           |
| GND  |                | Ground                                                                                            |
| VCC  |                | DC3.3~5V power input                                                                               |

Notes:

1. The module's pin level is 3.3V, and level conversion adaptation is required for communication with 5V MCU.
2. The wireless serial module is TTL level, please connect with MCU of TTL level.

## Mode Configuration

The MD0 and AUX pins have two functions, entering different states depending on their cooperation. When the module is first powered on, the AUX pin is in input mode. If both MD0 and AUX pins are connected to 3.3V TTL high level and kept for 1 second (without changing the pin level), the module will enter firmware upgrade mode and wait for firmware upgrade. Otherwise, it will enter wireless communication mode (the AUX pin will return to output mode to indicate the module's working status).

The MD0 and AUX pins are internally pulled down, and floating is low level. Pulling up is 3.3V TTL high level.

| Function     | Introduction             | Entry Method                        |
| ------------ | ------------------------ | ----------------------------------- |
| Configuration| Module parameter setting (AT command) | After power on, AUX is floating, MD0 is pulled high |
| Communication| Used for wireless communication | After power on, AUX is floating, MD0 is floating |
| Firmware upgrade| Used for firmware upgrade | After power on, AUX is pulled high, MD0 is pulled high, and kept for 1s |

In wireless communication mode, the AUX pin is output to indicate the module's working status.

## Function Configuration

Under "Configuration", the serial port needs to be set to ASDASD: baud rate "115200", stop bit "1", data bit "8", parity bit "none", and the module's working parameters are set through AT commands. Refer to the following AT command table for configuration software:

| Command     | Function                     |
| ----------- | ---------------------------- |
| AT          | Test module response         |
| AT+MODEL?   | Query device model           |
| AT+CGMR?    | Get software version number  |
| AT+UPDATE   | Check if device is in firmware upgrade mode |
| ATE1        | Enable command echo          |
| ATE0        | Disable command echo         |
| AT+RESET    | Module reset (reboot)        |
| AT+DEFAULT  | Restore factory settings     |
| AT+FLASH=   | Save parameters              |
| AT+ADDR=?   | Query device configuration address range |
| AT+ADDR?    | Query device address         |
| AT+ADDR=    | Configure device address     |
| AT+TPOWER=? | Query transmission power configuration range |
| AT+TPOWER?  | Query transmission power     |
| AT+TPOWER=  | Configure transmission power |
| AT+CWMODE=? | Query configuration mode range |
| AT+CWMODE?  | Query mode                   |
| AT+CWMODE=  | Configure mode               |
| AT+TMODE=?  | Query send status configuration range |
| AT+TMODE?   | Query send status            |
| AT+TMODE=   | Configure send status        |
| AT+WLRATE=? | Query wireless rate and channel configuration range |
| AT+WLRATE?  | Query wireless rate and channel |
| AT+WLRATE=  | Configure wireless rate and channel |
| AT+WLTIME=? | Query configuration sleep time range |
| AT+WLTIME?  | Query sleep time             |
| AT+WLTIME=  | Configure sleep time         |
| AT+UART=?   | Query serial port configuration range |
| AT+UART?    | Query serial port configuration |
| AT+UART=    | Configure serial port        |

When exiting the configuration function (MD0=0), the module will reconfigure the parameters. During the configuration process, AUX remains high and outputs low after completion, returning the module to idle state.

## Sleep Time

The sleep time is the listening interval for the receiving end and the duration of transmitting the wake-up code for the transmitting end. When the module is in "wake-up mode", it will automatically add a wake-up code for configuring the sleep time before the user data. When the module is in "power-saving mode", the configured sleep time is the listening interval.

## Device Modes

### General Mode (Mode 0)

- Transmission: The module receives user data from the serial port and transmits a wireless data packet of 58 bytes. When the user input data reaches 58 bytes, the module will start wireless transmission. If there is no user data input after waiting for 1 byte time and the user needs to transmit less than 58 bytes, the module will consider the data transmission complete and send all the data wirelessly. When the module starts sending the first packet of user data, the AUX pin outputs high level. After all the data is transmitted through the RF chip and the transmission is started, the AUX outputs low level. This indicates that the last wireless data packet has been transmitted. Users can continue to input data up to 512 bytes. The data packets sent through the general mode can only be received by the receiving module in general mode or wake-up mode.
- Reception: The module always turns on the wireless reception function and can receive data packets sent by the general mode and wake-up mode. After receiving the data packet, the module outputs high level on the AUX pin. After a delay of 2-3ms, it starts to output the wireless data through the serial port TXD pin. After all the wireless data is output through the serial port, the module outputs low level on the AUX pin.

### Wake-up Mode (Mode 1)

- Transmission: The condition for starting data packet transmission is the same as in general mode, except that the module will automatically add a wake-up code (sleep time) before each data packet. The length of the wake-up code depends on the sleep time set in the user parameters. The purpose of the wake-up code is to wake up the receiving module in power-saving mode. Therefore, the data transmitted in wake-up mode can be received by the general mode, 1, and 2.
- Reception: Same as general mode.

### Power-saving Mode (Mode 2)

- Transmission: The module is in sleep mode and the serial port is closed, so it cannot receive serial data from an external MCU. Therefore, this mode does not have wireless transmission function.
- Reception: In power-saving mode, the transmitting party must operate in wake-up mode. The wireless module listens for the wake-up code at regular intervals. Once it receives a valid wake-up code, the module will remain in reception mode and wait for the entire valid data packet to be received. Then, the module will output a high level on AUX, and after a delay of 2-3ms, it will open the serial port and send the received wireless data through TXD. After completion, AUX will output a low level. The wireless module will continue to work in "sleep-listen" mode. By setting different wake-up times, the module has different reception response delays and power consumption. Users need to find a balance between communication delay time and average power consumption.

### Signal Strength Mode (Mode 3)

The signal strength mode can view the signal strength of both communication parties and provide reference for evaluating the communication quality.

- Transmission: Same as general mode.
- Reception: Outputs information about signal strength.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110058.png)

SNR: Signal-to-Noise Ratio (the larger the more stable), RSSI: Received Signal Strength Indication (the larger the more stable)

## Communication Modes

- Transparent Transmission: For example, Device A sends 5 bytes of data AA BB CC DD EE to Device B, and Device B receives the data AA BB CC DD EE. (Transparent transmission, for communication between devices with the same address and communication channel, user data can be in character or hexadecimal format).
  - Point-to-Point
  - Point-to-Multipoint
  - Broadcast Listening
- Directed Transmission: For example, Device A (address: 0x1400, channel: 0x17 (23 channel 433Mhz)) needs to send data AA BB CC to Device B (address: 0x1234, channel: 0x10 (16 channel, 426Mhz)), and the communication format is: 12 34 10 AA BB CC, where 1234 is the address of module B and 10 is the channel, so module B can receive AA BB CC. Similarly, if Device B needs to send data AA BB CC to Device A, the communication format is: 14 00 17 AA BB CC, and Device A can receive AA BB CC. (Directed transmission, can achieve communication between devices with different addresses and communication channels, data format is hexadecimal, sending format: high address + low address + channel + user data).
  - Point-to-Multipoint
  - Broadcast Listening.

Broadcast and Data Monitoring: Setting the module address to 0xFFFF allows for monitoring data transmission of all modules on the same channel; data sent can be received by any module on the same channel with any address, thus serving as a broadcast and monitoring function.

## Transparent Transmission Mode

### Point-to-Point

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110614.png)

- Two modules with the same address, channel, and wireless rate (non-serial baud rate), where one module sends and the other receives (must be one sender and one receiver).
- Each module can send/receive.
- Data is completely transparent, what is sent is what is received.

|          | Sending Module | Receiving Module |
| -------- | -------------- | ---------------- |
| Quantity | 1              | 1                |
| Content  | Data           | Data             |

For example:

Devices A and B have addresses of 0x1234, channels of 0x12, and the same rate.  
Device A sends: AA BB CC DD  
Device B receives: AA BB CC DD

The transparent transmission method is simple, just use the Lora module as a serial port, and Device A can send data through the serial port, which Device B can receive, and vice versa.

### Point-to-Multipoint

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110709.png)

- Modules with the same address, channel, and wireless rate (non-serial baud rate), where any module can send and other modules can receive.
- Each module can send/receive.
- Data is completely transparent, what is sent is what is received.

|          | Sending Module | Receiving Module |
| -------- | -------------- | ---------------- |
| Quantity | 1              | N                |
| Content  | Data           | Data             |

The difference from point-to-point is that multiple modules can receive.

For example:
Devices A to F have addresses of 0x1234, channel of 0x12, and the same rate.  
Device A sends: AA BB CC DD  
Devices B to F receive: AA BB CC DD

### Broadcast Monitoring

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118110853.png)

- If the module address is 0xFFFF, the module is in broadcast listening mode, and the data sent can be received by all other modules with the same rate and channel (broadcast); at the same time, it can listen to the data transmission of all modules on the same rate and channel (listening).
- Broadcast listening does not require the same address.

|          | Sending Module | Receiving Module |
| -------- | -------------- | ---------------- |
| Quantity | 1              | N                |
| Content  | Data           | Data             |

The difference from point-to-multipoint is that the addresses can be different.

For example:
Device A has an address of 0xFFFF, and devices B~F do not all have the same address. Devices B and C have an address of 0x1234, and devices D, E, and F have an address of 0x5678. Devices A~F all have the same rate.
Broadcast:
Device A broadcasts: AA BB CC DD
Devices B~F receive: AA BB CC DD
Listening:
Device B sends to C: AA BB CC DD
Device A listens: AA BB CC DD
Device D sends to E and F: 11 22 33 44
Device A listens: 11 22 33 44

## Directed Transmission Mode

### Point-to-Point

- When the module sends, the address and channel can be modified, and the user can specify that the data is sent to any address and channel.
- Networking and relay functions can be realized.

|          | Sending Module       | Receiving Module |
| -------- | -------------------- | ---------------- |
| Quantity | 1                    | 1                |
| Content  | Address+Channel+Data | Data             |

The difference from point-to-point transparent transmission is that the module address and channel can be changed, but the rate remains the same.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118111903.png)

For example:
Device A has an address of 0X1234 and a channel of 0X17;
Device B has an address of 0xABCD and a channel of 0X01;
Device C has an address of 0X1256 and a channel of 0x13.

Device A sends: AB CD 01 AA BB CC DD  
Device B receives: AA BB CC DD  
Device C receives: None

Device A sends: 12 56 13 AA BB CC DD  
Device B receives: None  
Device C receives: AA BB CC DD

#### Codeless Testing

Prepare 2 USB to TTL converters and 2 LoRa modules. Connect them to the USB to TTL converters (power, common ground, TX/RX matching), connect the MD0 of the two LoRa modules to VCC, plug them into the computer USB, open the configuration software, and configure the following parameters:

Device A:

- General mode
- Directional transmission
- **Baud rate: 115200 (must be 115200)**
- Parity: None
- Air speed: 19.2k
- Sleep time: 1s
- **Module address: 0**
- **Communication channel: 0**
- Transmit power: 20dBm

Device B:

- General mode
- Directional transmission
- **Baud rate: 115200 (must be 115200)**
- Parity: None
- Air speed: 19.2k
- Sleep time: 1s
- **Module address: 65534**
- **Communication channel: 10**
- Transmit power: 20dBm

After configuring, click `Save Configuration`, and then **unplug MD0 and power off**.

Power on the two modules again, open the configuration software, and **select `HEX` (hexadecimal) for both send and receive**.

In the send area of A, enter `FF FE 0A 11 12 13 14`, click send, and you can receive `11 12 13 14` in the receive area of B; or in the send area of B, enter `00 00 00 11 12 13`, and you can receive `11 12 13` in the receive area of A.

Among them, `FF FE` is the hexadecimal number of the address 65534 of B, the channel is 10 (hexadecimal number is `0A`), and the content data sent is `11 12 13 14`. Similarly, the data sent by B includes A's address `00 00`, channel `00`, and content `11 12 13`. The format of the sent data is **high address + low address + channel + user data**.

#### Code Testing

Point-to-point fixed transmission only adds address bytes compared to point-to-point transparent transmission. It can be defined as follows:

```c title="main.c"
/* USER CODE BEGIN PV */
uint8_t B_Addr[2] = { 0xFF, 0xFE };
uint8_t B_Chan[1] = { 0x0A };
/* USER CODE END PV */
```

After configuring the code with UART (HAL library environment), send the address byte before sending data each time:

```c title="main.c"
HAL_UART_Transmit(&huart1, B_Addr, 2, 0xFFFF);
HAL_UART_Transmit(&huart1, B_Chan, 1, 0xFFFF);
```

In this way, the receiving device (Device B) can receive a frame of data (excluding the address byte) sent by Device A.

### Broadcast Listening

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220118112544.png)

- If the module address is 0xFFFF, the module is in broadcast listening mode, and the data sent can be received by all other modules with the same rate and channel (broadcast); at the same time, it can listen to the data transmission of all modules on the same rate and channel (listening);
- Broadcast listening does not require the same address.
- The channel address can be set. When the address is 0xFFFF, it is in broadcast mode; when it is other, it is in directional transmission mode.

|          | Sending Module   | Receiving Module |
| -------- | ---------------- | ---------------- |
| Quantity | 1                | N                |
| Content  | 0xFFFF+Channel+Data | Data             |

For example:

Device A address 0xFFFF channel 0x12;
Devices B and C address 0x1234, channel 0x13;
Device D address 0xAB00, channel 0x01;
Device E address 0xAB01, channel 0x12;
Device F address 0xAB02, channel 0x12;

Device A broadcasts: FF FF 13 AA BB CC DD
Devices B and C receive: AA BB CC DD

Device A sends: AB 00 01 11 22 33 44
Only Device D receives: 11 22 33 44

Device E sends: AB 02 12 66 77 88 99  
Device F receives: 66 77 88 99  
Device A listens: 66 77 88 99

## References and Acknowledgments

- [LORA Module ATK-LORA-01](http://www.openedv.com/docs/modules/iot/atk-lora-01.html)
- [Tutorial for Using the ATK-LORA LORA Module from DFRobot](https://www.bilibili.com/video/BV1D44y1t7bn)
- [【DFRobot Product Information】LORA Module ATK-LORA-01 Data Download and Technical Discussion Link](http://www.openedv.com/thread-309019-1-1.html)
- [Test Method for Two LORA Modules Working in General Mode for Directional Data Transmission (Tested Using Upper Computer)](http://www.openedv.com/forum.php?mod=viewthread&tid=288951)
- [ATK-LORA-01 Wireless Serial Module Only Receives 00](http://www.openedv.com/forum.php?mod=viewthread&tid=328190&highlight=ATK-LORA-01)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.