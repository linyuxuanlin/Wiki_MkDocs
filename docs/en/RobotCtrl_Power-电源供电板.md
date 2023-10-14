# RobotCtrl_Power - Power Supply Board

![](https://img.wiki-power.com/d/wiki-media/img/20220527113517.png)

Project Repository: [**linyuxuanlin/RobotCtrl/RobotCtrl_Power**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power)

Online Preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power_V0.3B.zip"
  ></div>
</div>

Note: This project is included in the [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/en/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Schematic Design

The main functions of RobotCtrl_Power are as follows:

- 24V power input (theoretical range is 15-40V)
- Battery power converted to 12V/5A regulator (with enable switch and indicator light)
- Battery power converted to 5V/5A regulator (with enable switch and indicator light)
- Reverse protection (P-MOS)
- Overvoltage protection (protection starts at over 30V)
- Battery power output, 12V power output, and 5V power output interfaces

### Power Input

Two XT60PW-M sockets are used for power input, providing dual power backup input (can also be used as one input and one output), and two rows of pins are provided for output testing.

The reverse connection prevention function is implemented using P-MOS. Although XT60 has a foolproof design, it is still necessary to prevent the situation of welding the positive and negative power lines in reverse. When reversed, the P-MOS will not conduct, and the power will not enter the system. The design of reverse connection prevention function can refer to the article "Design of Reverse Connection Circuit".

Transient overvoltage protection and ESD protection use TVS tubes. When the input voltage is greater than 30V, it will divert excess voltage to protect the downstream system.

The 12V and 5V voltage stabilization circuits use two TI LMR14050 DC-DC Buck schemes, each of which can carry a maximum current of 5A. The specific design can refer to the article "Power Scheme (Buck)-LMR14050". In addition, each circuit has an enable switch and a power indicator.

VBAT, 12V, and 5V outputs each use a pair of 4-pin headers, and the 12V output also adds a KF2EDGR-3.81 socket to provide power to special sensors.

For the PCB layout of RobotCtrl_Power, it is important to place the feedback network's upper and lower voltage divider resistors as close as possible to the chip's FB pin, and the Vout sampling path should follow the principle noise generation path (inductor-diode loop), preferably through a via to the shield layer. The inductor should be placed near the SW pin to reduce magnetic and electrostatic noise. The grounding nodes of the diodes, input and output capacitors should be as small as possible and preferably connected to the system ground plane at only one point to minimize the conducted noise in the system ground plane. The output capacitor should be placed as close as possible to the nodes of the inductor and diode, and the routing should be as short and thick as possible to reduce conducted and radiated noise and improve efficiency.

RobotCtrl_Power's PCB top and bottom layers carry signals and power, with two ground planes inserted in the middle to enhance signal and power integrity.

Hardware testing includes:

- Reverse connection test: whether the system can remain off when the input voltage is reversed.
- Enable switch and power indicator: whether they can operate normally.
- Output: whether the 12V/5V output meets the standard and the ripple size.

Sorry, there is no Chinese article provided for translation. Please provide the article for translation.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
