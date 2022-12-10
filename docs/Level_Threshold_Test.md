---
id: Level_Threshold_Test
title: Level Threshold Test 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220912163403.png)

Level threshold test includes Output Level Threshold (VOL & VOH) and Input Level Threshold (VIL & VIH). They are originated from typical TTL and CMOS level threshold:

|                       |  VCC                      | VOL          | VOH       | VIL      | VIH          | GND |
| :---------        | :---- | :-------        | :---------------| :---------- | :------        | :---- |
|  TTL (5V)          | 5.00V                    | 0.40V     | 2.40V       | 0.80V           | 2.00V                  | 0.00V   |
|  LVTTL (3.3V)   | 3.30V                        | 0.40V    | 2.40V      | 0.80V         | 1.50V                   | 0.00V
|  CMOS (5V)     | 5.00V                 | 0.50V (0.1 VCC)          | 4.50V (0.9 VCC)       | 1.50V (0.3 VCC)| 3.50V (0.7 VCC)| 0.00V   |
|  CMOS (3.3V)  | 3.30V            | 0.33V (0.1 VCC)      | 2.97V (0.9 VCC)   | 0.99V (0.3 VCC)  | 2.31V (0.7 VCC)  | 0.00V   |
|  CMOS (2.5V)  | 2.50V                      | 0.40V      | 2.00V  | 0.70V       | 1.70V             | 0.00V   |
|  CMOS (1.8V)  | 1.80V                          | 0.45V      | 1.35V | 0.63V      | 1.170V         | 0.00V   |

## Output Level Threshold Test (VOL/IOL & VOH/IOH)

VOL represents the maximum output voltage when output LOW voltage level, IOL represents the maximum **sinking** current capability in LOW output state. They actually measures the resistance of the output pin when provide the logic `0`, insures it can provide current of IOL without exceeding the voltage of VOL, examining the capability of sink current and stay in a correct logic state.

VOH represents the minimum output voltage when output HIGH voltage level, IOH represents the maximum **source** current capability in HIGH output state.They actually measures the resistance of the output pin when provide the logic `1`, insures it can provide current of IOH without less than the voltage of VOH, examining the capability of source current and stay in a correct logic state.

### Test Method (Serial)

#### VOL/IOL Test (Serial)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220912172403.png)

1. Apply VDDmin to VDD pin (with current clamp).
2. Precondition specific output pin to logic '0'.
3. Force IOLmax to the Pin under Test (flow into DUT), and measure the voltage on it:
   - **Higher than spec value(>0.4V)**: FAIL
   - **Lower than spec value(<0.4V)**: PASS
4. Repeat to test with different output pins.

#### VOH/IOH Test (Serial)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220912172445.png)

1. Apply VDDmin to VDD pin (with current clamp).
2. Precondition specific output pin to logic '1'.
3. Force IOHmax to the Pin under Test (flow out of DUT), and measure the voltage on it:
   - **Higher than spec value(>2.4V)**: PASS
   - **Lower than spec value(<2.4V)**: FAIL
4. Repeat to test with different output pins.

## Input Level Threshold Test(VIL & VIH)

## References & Acknowledgements

- *The Fundamentals Of Digital Semiconductor Testing*
- *Fundamentals of Testing Using ATE*

> This article is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
