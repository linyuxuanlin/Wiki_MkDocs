---
id: IDD_Test
title: IDD Test
---

Power supply current (IDD) indicates the current flows from Drain to Drain in a CMOS circuit (named ICC in TTL circuit, means Collector to Collector). IDD can be equivalent as:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220910234238.png)

## Static IDD Test

Static IDD is a measurement of current from DUT's VDD pin, when the DUT is in static state (the DUT is not active during the test). The value of static IDD indicates the lowest current consumption of the DUT, which is important for battery operated devices, also help to indicate marginal defects.

### Test Method

Static IDD test is performed with applying a voltage of VDDmax and measuring the current value, while the DUT is preconditioned to its lowest current consumption logic state.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911201659.png)

1. Apply VDDmax to VDD pin (with current clamp).
2. Precondition DUT to its lowest current consumption logic state.
3. Measure the current flowing into VDD pin:
   - **Higher than spec value(>10uA)**: FAIL
   - **Lower than spec value(<10uA)**: PASS

## Dynamic IDD Test

Dynamic IDD is a measurement of current from DUT's VDD pin, when the DUT is constantly performing some function. Dynamic IDD is also important for battery operated devices.

### Test Method

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911201603.png)

Static IDD test is performed with applying a voltage of VDDmax and measuring the current value, while the DUT is preconditioned to a continuously working state.

1. Apply VDDmax to VDD pin (with current clamp).
2. Precondition DUT to a continuously working state.
3. Measure the current flowing into VDD pin:
   - **Higher than spec value(>50mA)**: FAIL
   - **Lower than spec value(<50mA)**: PASS

## Quiescent IDD Test (IDDQ)

Quiescent IDD is a measurement of IDD in the quiescent states (the circuit is not switching and inputs are held at static values). As processors shrink , the defect of leakage current becomes much more higher, and IDDQ test may detect minor defects within the core of the circuit that could not other wise be detected.

### Test Method

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911213042.png)

1. Apply VDDmax to VDD pin (with current clamp).
2. Precondition DUT to a certain working state (toggle certain function part to on/off such as Bluetooth and Wi-Fi).
3. Measure the current flowing into VDD pin:
   - **Higher than spec value**: FAIL
   - **Lower than spec value**: PASS
4. Repeat to test with different working states.

## References & Acknowledgements

- *The Fundamentals Of Digital Semiconductor Testing*
- *Fundamentals of Testing Using ATE*

> This article is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
