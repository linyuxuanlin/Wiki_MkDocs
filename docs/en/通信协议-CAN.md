# Communication Protocol - CAN 🚧

CAN (Controller Area Network) is a serial communication bus with a multi-master architecture. The basic design specifications require high bit rates, high immunity to electromagnetic interference, and the ability to detect any errors that occur. Even when the signal transmission distance reaches 10 km, CAN-bus can still provide a data transfer rate of up to 5 Kbps.

## CAN Circuit Design

The design of the CAN module is based on the CAN chip, which converts the serial signal (RX/TX) to the CAN differential signal (CANH/CANL) and vice versa. The following are two commonly used CAN transceivers.

### Based on TJA1050

For complete information, please see [**Modularity_of_Functional_Circuit/Module Design - CAN Communication/Based on TJA1050**](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/Module%20Design%20-%20CAN%20Communication/Based%20on%20TJA1050).

#### Features

- Power supply: **5 V** (4.75-5.25 V)
- High speed: 60 Kbps-1 Mbps
- Fully compliant with ISO 11898 standard
- Low electromagnetic emission (EME)
- Differential receiver with a wide input range, resistant to electromagnetic interference (EMI)
- Can connect at least 110 nodes
- Nodes that are not powered on will not interfere with the bus

#### Operating Modes

TJA1050 has two operating modes (high speed/silent), controlled by pin S (RS).

**High-speed mode**:

High-speed mode is the normal operating mode, and it can be entered by grounding pin S. Since pin S has a built-in pull-down, even if it is not connected externally, it defaults to high-speed mode.

In this mode, the bus output signal has a fixed slope and switches at the fastest speed, which is suitable for the maximum bit rate and maximum bus length, and its transceiver has the minimum cycle delay.

**Silent mode**:

In silent mode, the transmitter is disabled and does not respond to the input signal of TXD, so the power consumption in the non-transmitting state is the same as that in the recessive state. Silent mode can be entered by connecting pin S to a high level.

In silent mode, nodes can be set to an absolutely passive state on the bus, and the microcontroller no longer directly accesses the CAN controller. TJA1050 will release the bus.

#### Chip Pins

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607102222.png)

#### Reference Circuit

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607115611.png)

As shown in the figure, the CAN protocol controller (such as a microcontroller) is connected to the transceiver through a serial line (RX/TX), which is converted to a CAN signal (CANH/CANL) on the transceiver and selects high-speed/silent mode through pin S.

### Based on SN65HVD230

For complete information, please see [**Modularity_of_Functional_Circuit/Module Design - CAN Communication/Based on SN65HVD230**](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/Module%20Design%20-%20CAN%20Communication/Based%20on%20SN65HVD230).

#### Features

- Powered by a single 3.3 V supply
- Can connect at least 120 nodes
- Low current standby mode
- Speed: up to 1 Mbps

#### Operating Modes

SN65HVD230 has three operating modes (high speed/slope/silent), controlled by pin S (RS). Generally, we use high-speed mode.

**High-speed mode**:

Pull Rs strongly to GND to enable high-speed mode.

**Slope mode**:

Use a resistor between 10k and 100k to pull Rs to GND. Please refer to the data sheet for the specific relationship between the resistor value and the speed.

**Low Power Mode:**

Force Rs to pull up to 3.3V

#### Chip Pinout

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607155539.png)

#### Reference Circuit

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607171051.png)

PESD2CAN is a CAN-specific ESD protection diode that protects the chip from static electricity and other transient factors.

The reference PCB layout is as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607171427.png)

### Differences between TJA1050 and SN65HVD230

The main difference between TJA1050 and SN65HVD230 is the working voltage. TJA1050 works in a 5V environment, while SN65HVD230 works in a 3.3V environment.

Common considerations:

- When PCB wiring the CAN signal line, it should be a differential line.
- The terminal resistor is generally only needed at the starting and ending points of the CAN line, and not in the middle.
- If it is necessary to filter and stabilize the common mode voltage of the bus, a split terminal resistor can also be used (as shown above, divided into two 60Ω resistors with a capacitor connected to ground in the middle).

## CAN Interface EMC Design

In CAN communication, cables are easily coupled with external interference, which affects signal transmission and may even affect the internal core sensitive circuit through the interface circuit.

CAN interface protection devices mainly include: filtering capacitors, common mode inductors, bridging capacitors, and TVS tubes.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211220134905.png)

- Filtering capacitors $C_1, C_2$: used to provide a low-impedance return path for interference, the selection range is 22pF~1000pF, and the typical value is 100pF.
- Common mode inductor $L_1$: used to filter out common mode interference on the differential line, the impedance selection range is 120Ω/100MHz~2200Ω/100MHz, and the typical value is 600Ω/100MHz.
- Bridging capacitors $C_3, C_4$: used for isolation between interface ground and digital ground, with a typical value of 1000pF/2kV.
- TVS tubes $D_1, D_2$: used to prevent ESD or momentary high-energy impact, so that the voltage of the line is clamped to a predetermined value, thereby ensuring that the subsequent circuit devices are not damaged by transient high-energy impacts.

## References and Acknowledgments

- [Protective Design of Interface Circuit](https://blog.csdn.net/weixin_40877615/article/details/94381422)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.