# Power Solution (LDO) - XC6206

The XC6206 series is a high-precision, low-power three-terminal positive voltage regulator that provides high current and minimal dropout voltage. It consists of a current limiting circuit, a driver transistor, a precision reference voltage, and an error correction circuit. This series is compatible with low ESR ceramic capacitors. The output voltage can be selected in the range of 1.2V to 5.0V with an increment of 0.1V.

In this article, we have chosen the XC6206 series from TOREX, in SOT-23 package. Other manufacturers may have similar models that can be used as substitutes, but please verify the detailed parameters.

Project repository: [**Collection_of_Power_Module_Design/LDO/XC6206**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/LDO/XC6206)

## Key Features

- Maximum output current: 200mA (typical value at 6.0V)
- Dropout voltage: 250mV @ 100mA (typical value at 6.0V)
- Maximum operating voltage: 6.0V
- Output voltage range: 1.2V ~ 5.0V (0.1V increment)
- Accuracy: ±30mV when Vout < 1.5V; ±2% when Vout > 1.5V; ±1% when Vout > 2V
- Low power consumption: typical value of 1.0uA
- Protection circuit: built-in current limiting circuit
- Operating temperature: -40℃ ~ +85℃
- Package options: SOT-23, SOT-89, USP-6B

## Selection Guide

![](https://media.wiki-power.com/img/20220420102910.png)

## Typical Application Circuit

![](https://media.wiki-power.com/img/20220420102323.png)

## Internal Functional Block Diagram

![](https://media.wiki-power.com/img/20220420102514.png)

Note: The diode inside the block diagram represents ESD or parasitic diodes.

## Pin Definitions

![](https://media.wiki-power.com/img/20220420103005.png)

| Pin Name | Pin Description |
| -------- | --------------- |
| VSS      | Ground          |
| Vin      | Power Input     |
| Vout     | Power Output    |

## Feature Description

Specific parameter tables for each model:

![](https://media.wiki-power.com/img/20220420103738.png)

## References and Acknowledgements

- [XC6206_Datasheet](https://www.torexsemi.com/file/xc6206/XC6206.pdf)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
