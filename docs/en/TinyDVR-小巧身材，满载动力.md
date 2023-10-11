# TinyDVR - Small Size, Loaded with Power

—— Based on TinyDVR Master V1.1 & Slave V7.2 Release

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191345.jpg)

TinyDVR is a motor driver kit that includes a motherboard (Master) and a daughterboard (Slave). The power supply and drive parts are separated, and the volume is greatly reduced compared to its predecessor ZenDriver, greatly improving scalability. You can stack different numbers of daughterboards according to your needs to drive n motors.

Project repository: [**linyuxuanlin/TinyDVR**](https://github.com/linyuxuanlin/TinyDVR)

Project online preview:

**TinyDVR_Master**:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Master.zip"
  ></div>
</div>

**TinyDVR_Slave**:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Slave.zip"
  ></div>
</div>

## Basic Parameters

1. Input voltage: **7.2 ~ 20 V**
2. Output current: **0 ~ 68 A**
3. Provides **5V / 3A** power output for controllers and other modules
4. Protection device: integrated anti-reverse, optocoupler isolation circuit
5. Convenient motor connection: for commonly used DC reduction motors (with encoders), can be directly connected with 6-pin cable (no need to match polarity)
6. Expandable: one motherboard can stack n daughterboards to achieve n-channel motor drive

## Interface Definition

### TinyDVR Master

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191439.png)

### TinyDVR Slave

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191457.png)

Back pin details:

- \+ : Provides 5V / 3A power output
- 1 : IN1 port, input PWM signal 1
- 2 : IN2 port, input PWM signal 2
- A : Encoder A phase signal port
- B : Encoder B phase signal port
- \- : GND

## User Guide

### Test Method

1. Connect to **7.2 ~ 20 V** battery power supply
2. Connect the motor to the corresponding daughterboard
3. Connect **IN1/IN2** ports to **5V** power supply port, the motor will **rotate forward/reverse**

### Connect to MCU

4. Connect to **7.2 ~ 20 V** battery power supply
5. Connect the motor to the corresponding daughterboard
6. Common ground (connect the GND of the drive board to the GND of the MCU)
7. Connect IN1 and IN2 ports to the corresponding PWM ports of the MCU (set in the code)
8. Test method: see the test routine in the project repository

## Behind the Scenes

Early daughterboard:
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182442.jpg)

Batch welding:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182441.jpg)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
