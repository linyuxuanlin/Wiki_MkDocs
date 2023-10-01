# Basic Knowledge of ESD

ESD (Electrostatic Discharge) refers to the phenomenon of rapid transfer of electrons between two objects when they approach or come into contact with each other. As is well known, objects generate and accumulate charges during contact and friction with other objects. For example, our hands accumulate a lot of positive charges when rubbed against the outside world. When an object with a large amount of accumulated positive charges is very close to or in contact with a conductor, electrons will quickly transfer from the conductor to the object with accumulated positive charges. This rapid transfer of electrons is called electrostatic discharge (ESD).

Electronic devices usually have many interfaces, which are connected to the pins of the chip through wires and then to the inside of the chip. The high voltage (generally up to thousands of volts) generated during electrostatic discharge may break the tube, and if it is a large current, it may also burn the components, so it needs to be avoided.

The key to ESD protection is to provide a separate discharge channel for static electricity (similar to a lightning rod). ESD devices are mainly divided into four categories: TVS diodes, varistors, MLCC, and ESD suppressors.

## ESD Test Models

|                                 | HBM      | MM      | CDM      | IEC 61000-4-2 MODEL |
| ------------------------------- | -------- | ------- | -------- | ------------------- |
| Test voltage (V)                | 500-2000 | 100-200 | 500-2000 | 2000-15000          |
| Pulse time (ns)                 | ~150     | ~80     | ~1       | ~150                |
| Peak current when applying 2kV (A_pk) | 1.33     | -       | ~5       | 7.5                 |
| Rise time                       | 25ns     | -       | <400ps   | <1ns                |
| Voltage shock times             | 2        | 2       | 2        | 20                  |

### Human Body Model (HBM)

Assuming a test is conducted on the static discharge of the human body, it simulates the situation when a person touches a chip with their hand.

### Machine Model (MM)

Assuming a test is conducted on the static discharge of a machine, it simulates the situation when static electricity is released when a chip is touched by a mechanical hand or other low-resistance tool.

The difference between this model and the human body model is that the capacitance is larger and there is no resistance. Therefore, the discharge current is much larger. Additionally, due to the inductive effect of the wire, there will be oscillating current, meaning that the current discharged to the chip will change from positive to negative.

### Charged Device Model (CDM)

The first two models simulate the situation where a charged body discharges to a chip. The charged device model simulates the situation where the chip itself is charged and discharges to the ground. This phenomenon occurs when a chip is taken out of packaging that has been stored in a warehouse for some time. In this case, there is no resistance or capacitance, and the chip discharges directly to the ground through its pins.

## ESD Reference Standards

Common HBM test specifications:

| Standard      | Charging Capacitance $C_d (pF)$ | Discharge Resistance $R_d (Ω)$ |
| ------------- | ----------------------------- | ------------------------------ |
| AEC-Q200-002  | 150                           | 2000                           |
| IEC61000-4-2  | 150                           | 330                            |

Taking the AEC-Q200-002 standard as an example, its ESD HBM test circuit is as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215164751.png)

Where $C_x$ is the capacitance of the test object, $C_d$ is the charging capacitance, $R_d$ is the discharge resistance, and $R_c$ is the protection resistance. The ESD test method is as follows:

- Close switch 1 and open switch 2: the high voltage power supply charges the charge into $C_d$.
- Open switch 1 and close switch 2: the charge stored in $C_d$ is applied to $C_x$ for ESD testing.

Discharge current curve:

## ESD Testing Process

According to the AEC-Q200-002 standard, the HBM testing process can be carried out as shown in the following figure:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215165447.png)

The breakdown voltage levels obtained from the test are classified according to the following table:

| Classification | Maximum Breakdown Voltage        |
| --------------| --------------------------------|
| 1A             | Less than 500V (DC)              |
| 1B             | 0.5 kV (DC) or more, less than 1 kV (DC) |
| 1C             | 1 kV (DC) or more, less than 2 kV (DC) |
| 2              | 2 kV (DC) or more, less than 4 kV (DC) |
| 3              | 4 kV (DC) or more, less than 6 kV (DC) |
| 4              | 6 kV (DC) or more, less than 8 kV (DC) |
| 5A             | 8 kV (DC) or more, less than 12 kV (AD) |
| 5B             | 12 kV (AD) or more, less than 16 kV (AD) |
| 5C             | 16 kV (AD) or more, less than 25 kV (AD) |
| 6              | 25 kV (AD) or more                |

DC (Direct Contact Discharge) refers to direct contact discharge, while AD (Air Discharge) refers to air discharge.

## Relationship between Capacitance Value of Test Object and ESD Resistance

The capacitance value $C_x$ of the test object affects the voltage at both ends, which satisfies the following relationship:

$$
V_x=\frac{C_d}{C_d+C_x}V_d
$$

When the capacitance value of the test object ($C_x$) increases while the capacitance value of the power supply voltage ($V_d$) and charging capacitor ($C_d$) remain constant, the voltage ($V_x$) on both sides of the test object decreases.

Therefore, in general, the larger the capacitance value of $C_x$, the greater the ESD resistance. However, in reality, due to differences in design such as the type and thickness of the dielectric, the range of voltage resistance performance also varies and does not completely follow the above trend.

### Reference for Capacitance Value and ESD Resistance

- $C_x$ Capacitance Parameter: GCM Series / 0402 Package / X7R / 50V
- Test Conditions: $C_d=150pF,R_d=2kΩ$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215172528.png)

According to the chart curve, if we want to withstand 1kV ESD, we can use a 1000pF capacitor for defense. In actual circuit design, it is best to parallel a large resistor with the capacitor to discharge the electricity in the capacitor after eliminating ESD.

## References and Acknowledgments

- [Introduction to Reliability and ESD](https://mazhaoxin.github.io/2021/08/01/Reliability_and_ESD_Introduction/)
- [Electronic Engineer's Notebook: Basic Knowledge of ESD and Selection of ESD Protection](https://haipeng.me/2019/09/03/esd-protection/)
- [ESD Resistance of Capacitors](https://article.murata.com/en-us/article/esd-resistance-of-capacitors)
- [Understanding the Role of ESD Devices in PCB Design in One Article](http://murata.eetrend.com/article/2021-11/1004974.html)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.