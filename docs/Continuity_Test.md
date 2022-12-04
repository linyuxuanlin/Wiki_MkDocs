---
id: Continuity_Test
title: Continuity Test
---

Continuity test contains open/short test and power pin short test. The former checks the signal pins, while the latter checks the power pin.

## Open/Short Continuity Test

Open/short continuity test is to confirm the electronical contact between tester and DUT, and whether if short-circuit existed to other pins or to ground.

### Test Method

Open/short continuity test is performed with testing the protection diodes (diodes to VDD and to GND). Usually use PPMU with VBT code (also can be tested using PE and functional pattern).

#### Test through GND protection diode

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220909003924.png)

1. Force 0V to all other pins that are not tested (include power pin).
2. Force a small negative current (-100uA) on the Pin Under Test (with voltage clamp).
3. Meaure voltage on the Pin Under Test：
   - **Higher than max spec(>-0.2V)**: FAIL (Short)
   - **Midband(-1.5V~-0.2V**): PASS
   - **Lower than min spec(<-1.5V)**: FAIL (Open)

#### Test through VDD protection diode

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220909004139.png)

1. Force 0V to all other pins that are not tested (include power pin).
2. Force a small positive current (+100uA) on the Pin Under Test (with voltage clamp).
3. Meaure voltage on the Pin Under Test：
   - **Higher than max spec(>1.5V)**: FAIL (Short)
   - **Midband(0.2V~1.5V)**: PASS
   - **Lower than min spec(<0.2V)**: FAIL (Open)

## Power Pin Short Test

Power pin short test is to check if there is a short-circuit from VDD to GND pin, which will cause damagement to DUT or tester. Power pin short test always run immediately after open/short continuity test, and when it fails, device power will be shut off and the DUT will be rejected.

### Test Method

Power Pin Short Test is performed by applying a small voltage to VDD, and measure the current into it, to check if a short-circuit existed. Usually use DCVI with VBT code.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220910155805.png)

1. Apply a small voltage to VDD (100mV) (with current clamp).
2. Force all other pins to 0V with PPMU.
3. Measure current flowing into VDD pin:
   - **Higher than max spec(>20uA)**: FAIL (Short)
   - **Midband(-1uA~20uA)**: PASS
   - **Lower than min spec(<-1uA)**: FAIL

## References & Acknowledgements

- *The Fundamentals Of Digital Semiconductor Testing*
- *Fundamentals of Testing Using ATE*

> This article is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
