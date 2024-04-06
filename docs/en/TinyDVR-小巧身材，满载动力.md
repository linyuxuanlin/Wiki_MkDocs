# TinyDVR - Compact Size, Loaded with Power

**— Based on TinyDVR Master V1.1 & Slave V7.2 Release**

![TinyDVR](https://media.wiki-power.com/img/20200125191345.jpg)

TinyDVR is a motor driver kit that includes a mainboard (Master) and a subboard (Slave). It separates the power supply and the driving components, resulting in a significantly reduced size compared to its predecessor, ZenDriver. This design greatly enhances its expandability. You can stack different numbers of subboards according to your needs to drive multiple motors.

Project Repository: [**linyuxuanlin/TinyDVR**](https://github.com/linyuxuanlin/TinyDVR)

Online Preview of the Project:

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

## Basic Specifications

1. Input Voltage: **7.2 ~ 20 V**
2. Output Current: **0 ~ 68 A**
3. Provides a **5V / 3A** power output for controllers and other modules
4. Protection Devices: Integrated reverse connection protection and optocoupler isolation circuit
5. Motor Connection: Compatible with commonly available DC geared motors (with encoders) and can be directly connected with a 6-pin connector (no need for soldering)
6. Expandable: One mainboard can stack multiple subboards, enabling control of multiple motors.

## Interface Definitions

### TinyDVR Master

![TinyDVR Master](https://media.wiki-power.com/img/20200125191439.png)

### TinyDVR Slave

![TinyDVR Slave](https://media.wiki-power.com/img/20200125191457.png)

Explanation of Back Pins:

- \+ : Provides 5V / 3A power output
- 1 : IN1 port, input PWM signal 1
- 2 : IN2 port, input PWM signal 2
- A : Encoder A-phase signal port
- B : Encoder B-phase signal port
- \- : GND

## User Guide

### Testing Procedure

1. Connect a **7.2 ~ 20 V** battery for power supply.
2. Attach the motor to the corresponding subboard.
3. Connect the **5V** power supply to the **IN1/IN2** ports. At this point, the motor will operate in the **forward/reverse** direction.

### Connecting to a Microcontroller

4. Connect a **7.2 ~ 20 V** battery for power supply.
5. Attach the motor to the corresponding subboard.
6. Connect the ground (drive board GND to microcontroller GND).
7. Connect IN1 and IN2 ports to the microcontroller's respective PWM ports (set in your code).
8. Testing procedure can be found in the project repository's test routine.

## Behind the Scenes

Early subboards:
![Early Subboards](https://media.wiki-power.com/img/20200311182442.jpg)

Bulk soldering:

![Bulk Soldering](https://media.wiki-power.com/img/20200311182441.jpg)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
