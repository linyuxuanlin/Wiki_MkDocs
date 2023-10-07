# AirForce - Motor Driver Module Full of Spirituality

The AirForce project is a motor driver combination kit that includes the AirPort motherboard with integrated voltage stabilization function and the AirCraft dual motor driver sub-board. It can drive up to 16 motors depending on the number of motors required. Due to its small size, strong performance, and high expandability, it is named Project AirForce.

Features:

- Small size, convenient interface wiring
- The interface is not completely black box packaging, which improves the wiring ability
- Does not occupy too many timer pin resources of the microcontroller (STM32)

Project repository: [**linyuxuanlin/AirForceDVR**](https://github.com/linyuxuanlin/AirForceDVR)

## AirPort - Motherboard with Integrated Voltage Stabilization Function

🚧

## AirCraft - Dual Motor Driver Sub-board

![](https://f004.backblazeb2.com/file/wiki-media/img/20201101231734.jpg)

The AirCraft dual motor driver sub-board is designed based on the TB6612FNG integrated driver chip, plus a logical control method. It only requires 4 pins (2 normal + 2 PWM) to control two motors (direction/speed). Compared with the general solution on the market, it reduces two IOs and reduces the occupation of the main controller's valuable pin resources. As for the parameters of the driver chip, the maximum continuous driving current of a single channel can reach 1.2A, and the peak value is 2A/3.2A (continuous pulse/single pulse), which is more than enough to drive motors on general robots.

### Product Parameters

- Logic part input voltage VCC: 3.3~5V (default **5V**)
- Drive part input voltage VM: 2.5~12V (default **12V**)
- Number of motor drive channels: 2 channels
- **Single channel** maximum continuous driving current: **1.2A**
- Starting peak value: **2A/3.2A** (continuous pulse/single pulse)
- Interface method: 2.54mm pitch pin header, XH2.54 female seat
- Module size: 23.7 × 15.8 (mm)

### Pin Description

![](https://f004.backblazeb2.com/file/wiki-media/img/20201022104033.png)

| Interface Group | Name | Function Description |
| :------: | :--: | :------------------: |
| Control Interface | PWM1 | Motor M1 speed control pin |
| Control Interface | DIR1 | Motor M1 direction control pin |
| Control Interface | DIR2 | Motor M2 direction control pin |
| Control Interface | PWM2 | Motor M2 speed control pin |
| Power Interface |  5V  | Logic control part power supply |
| Power Interface |  G   |        GND        |
| Power Interface | 12V  |       Motor power supply       |
| Motor Interface | M1+  |    Motor M1 output 1    |
| Motor Interface | M1-  |    Motor M1 output 2    |
| Motor Interface | M2+  |    Motor M2 output 1    |
| Motor Interface | M1-  |    Motor M2 output 2    |

### Control Tutorial

- Control Interface
  - **DIR1/DIR2**: Positive and negative rotation control signal input terminal
    - e.g. If DIR1 is assigned a value of 1 (high level), then the M1 motor rotates forward; if DIR1 is assigned a value of 0 (low level), then the M1 motor rotates backward.
  - **PWM1/PWM2**: Enable terminals for controlling two motors (can use PWM for speed control)
- Power Interface: Connect to any power interface on the AirPort motherboard (or external 12V and 5V input)
- Motor Interface: Connect to the input of the motor

### Dimensional Drawing

🚧

## Reference and Acknowledgement

- [Dual Motor Driver TB6612 Micro Motor Driver Module](https://wiki.dfrobot.com.cn/_SKU_DRI0044_Dual_Motor_Driver__TB6612__%E5%BE%AE%E5%9E%8B%E7%94%B5%E6%9C%BA%E9%A9%B1%E5%8A%A8%E6%A8%A1%E5%9D%97)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.