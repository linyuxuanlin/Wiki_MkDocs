# ZenDriver - High Performance Motor Driver

- Based on V5.1 Release version

Project repository: [**linyuxuanlin/ZenDriver**](https://github.com/linyuxuanlin/ZenDriver)

## Basic Parameters

1. Input voltage: **7.2 ~ 20 V**
2. Output current: **0 ~ 68 A**
3. Provides **5V 1.5A** power output for controller use
4. Protection devices: Integrated reverse connection protection, optocoupler isolation circuit

## Interface Definition

![](https://img.wiki-power.com/d/wiki-media/img/20200125192433.png)

From left to right, the **motor end** is: **M-, 5V, encoder A, encoder B, GND, M+**, corresponding to the motor pins, which can be directly connected to the motor.

From right to left, the **signal end** is: **GND, encoder B, encoder A, IN2, IN1, 5V**. Note: The 5V port **can provide power to the MCU** (maximum 1.5 A).

The **power input end** is common to all three interfaces, and it is generally recommended to connect the middle one to the battery, and the two next to it to expand the power supply to other driver boards.

## User Guide

### Direct Power Supply Test

1. Connect the **7.2 ~ 20 V** battery power supply
2. Connect the motor
3. Connect **IN1, IN2** on the **signal end** to **5V** respectively. At this time, the motor will rotate forward and backward.

### MCU Connection Test

1. Connect the **7.2 ~ 20 V** battery power supply
2. Connect the motor
3. Connect **signal end GND** to **MCU GND**, and **5V port** to **MCU 5V**
4. Connect pins **IN1, IN2** to the MCU PWM port
5. Debug with code

![](https://img.wiki-power.com/d/wiki-media/img/20200125192734.png)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
