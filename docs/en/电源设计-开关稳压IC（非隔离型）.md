# Power Supply Design - Switching Regulator IC (Non-Isolated)

## Factors to Consider in Design

The design of a switching power supply should consider at least the following conditions:

- **Input/Output Voltage**: Select according to the recommended working voltage range of the device, considering the actual voltage fluctuation range, to ensure that it does not exceed the device specifications.
- **Output Current**: The output current should reserve a certain margin, and the instantaneous peak current and heating of the circuit should be evaluated to meet the derating requirements.
- **Ripple**: Ripple is an important parameter for measuring the output voltage fluctuation of the circuit, and attention should be paid to light load and heavy load ripple. Usually, an oscilloscope with a bandwidth of 20 M is used for testing.
- **Efficiency**: Both light load and heavy load situations should be considered. Light load affects standby power, and heavy load affects temperature rise. Generally, the efficiency of 10 mA under 12 V input and 5 V output needs to reach 80% or more.
- **Transient Response**: The transient response characteristic reflects whether the system can adjust in time to ensure the stability of the output voltage when the load changes drastically. The smaller the output voltage fluctuation, the better, generally requiring less than 10% peak-to-peak.
- **Switching Frequency**: Usually above 500 kHz, it is related to the selection of inductance and capacitance, and other issues such as EMC and noise under light load are also related to it.
- **Feedback Reference Voltage and Accuracy**: The feedback voltage is compared with the internal reference voltage, and different voltages are output with the external feedback voltage divider. Different products have different reference voltages, such as 0.6-0.8 V, and the feedback resistor should be selected with 1% accuracy.
- **Linearity Stability and Load Stability**: Linearity stability reflects the stability of the output voltage when the input voltage changes; load stability reflects the stability of the output voltage when the output load changes. Generally, it is required to be 1%, and the maximum should not exceed 3%.
- **EN Level**: The EN high and low levels should meet the device specifications, and some ICs cannot exceed a specific voltage range. Due to the need for timing control, this pin will increase capacitance, and there should be a ground resistor for level adjustment and shutdown discharge.
- **Protection Performance**: There should be overcurrent protection OCP, overheat protection OTP, etc., and the conditions should disappear and be self-recovered after protection.
- **Others**: The project requires soft start; thermal resistance and packaging; the temperature range of use should cover high and low temperatures, etc.

Selection principles: universality, high cost-effectiveness, easy procurement, long life cycle, compatibility and substitutability, derating, easy production and standardization.

## Modulation Methods

### PFM (Pulse Frequency Modulation)

The switching pulse width is constant, and the output voltage is stabilized by changing the pulse output frequency. It is suitable for long-term use (especially for small loads) and has the advantage of low power consumption.

### PWM (Pulse Width Modulation)

The frequency of the switching pulse is constant, and the output voltage is stabilized by changing the pulse width. It has high efficiency and low ripple and noise.

## Can the Bottom of the Power Inductor be Covered with Ground Copper?

From the perspective of EMI, it is recommended to cover copper; from the perspective of inductance, for shielded inductors, the inductance is basically unaffected, so it is also recommended to cover copper; for E-shaped inductors, covering copper has a slight effect on the inductance, which can be determined according to the situation.

## Judging Whether the Inductor is Saturated by Experiment

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210723133831.png)

In addition, it can also be judged from abnormal temperature rise, whistling, and other situations.

## Requirements for Peripheral Component Selection

- **Input/Output Capacitance**: It needs to meet the voltage resistance (1.5-2 times the input voltage) and input ripple requirements.
- **BST Capacitance**: Bootstrap startup capacitance, used to raise the voltage to turn on the upper tube inside the chip. Generally, it is based on the recommended value in the datasheet (generally 0.1-1uF), and the voltage resistance is generally higher than the input voltage.
- **Inductor**: The required inductance is different for different output voltages; pay attention to the temperature rise and saturation current to meet the margin requirements, generally 1.3 times the maximum current (or the inductor saturation current must be greater than the maximum output current + 0.5*inductor ripple current).
- **Feedback Capacitance**: Take the value according to the datasheet requirements. Different manufacturers' chips have different values, and different output voltages also have different requirements.
- **Feedback Resistor and EN Divider Resistor**: The value should be taken according to the specification, and the accuracy should be selected as 1%.

## Switching Power Supply Ripple Analysis

🚧

## PCB Layout Requirements

- Inductors: Preferably choose integrated inductors as they have lower EMI.
- Feedback network: Feedback traces should be kept as far away as possible from inductors and power supply noise traces. While meeting the first condition, try to keep the traces short and thick. It is best to have the traces on the opposite side of the PCB from the inductor and separated by a ground plane in the middle. The voltage divider resistor is usually connected to the signal ground AGND, and the feedback trace can be grounded.
- Decoupling capacitors: Input decoupling ceramic capacitors should be placed as close as possible to the chip's $V_{IN}$ and GND to reduce parasitic inductance. The negative terminal of the capacitor can be connected through a via to reduce impedance. Generally, a large electrolytic capacitor is also needed for forward feed, and the power input should pass through a large capacitor before a small capacitor.
- The power loop should be kept as short and thick as possible to minimize the loop area and reduce noise radiation. The inductor should be close to the SW pin and away from the feedback line. The output capacitor should be close to the inductor, and a ground via should be added to the ground terminal.
- The capacitor trace of BST should be kept as short as possible and not too thin.
- The chip's heat dissipation should be in accordance with the design requirements, and vias should be added underneath for heat dissipation as much as possible.

## References and Acknowledgments

- [Detailed Explanation of the Three Basic Topologies of Switching Power Supplies - Full Text](http://www.elecfans.com/article/83/116/2016/20160307404422_a.html)
- [Master These Techniques to Easily Operate DC-DC Circuits](https://mp.weixin.qq.com/s/fqTPyfAKdTlbRxy0-ho9gA)
- [MPS, Is It Against the Rules to Add a Ground Plane to the Bottom of the Inductor?](https://mp.weixin.qq.com/s/CgR2jUgujLy3nqwU52rW2Q)
- [【Short Video】MPS Power Supply Classroom Episode 3: Tips for Judging Inductor Saturation](https://mp.weixin.qq.com/s?__biz=MzIwMTE4MzQwMw==&mid=2884003106&idx=1&sn=41c7eef3377037a1a1d21179447d0df1&scene=19#wechat_redirect)
- [How to Choose Inductors for BUCK DC-DC Converters?](https://mp.weixin.qq.com/s/tTSoUaeaVQI4TM6ruKpeKw)
- [AN-1149 Layout Guidelines for Switching Power Supplies](https://www.ti.com/lit/an/snva021c/snva021c.pdf?ts=1641814411004)
- [Switching Power Supply Ripple Analysis 🚧](http://www.oliverkung.top/%e5%bc%80%e5%85%b3%e7%94%b5%e6%ba%90%e7%ba%b9%e6%b3%a2%e5%88%86%e6%9e%90/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.