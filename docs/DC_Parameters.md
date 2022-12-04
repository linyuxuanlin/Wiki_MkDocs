---
id: DC_Parameters
title: DC Parameters
---

Testing DC parameters is essentially measuring the resistivity of the silicon. They can be tested DC method, with DCVI/PPMU forcing current then measuring voltage, or forcing voltage then measuring current. Will compare the measured value with the spec value out of the tester, then conclude a test result with PASS or FAIL. Items can be tested under DC method are as follows:

- [**Power Supply Current Test (IDD)**](https://wiki-power.com/DC-IDD_Test)
  - Gross IDD Test
  - Static IDD Test
  - Dynamic IDD Test
  - Quiescent IDD Test (IDDQ)
- [**Leakage Test**](https://wiki-power.com/DC-Leakage_Test)
  - Input Leakage Test (IIL & IIH)
  - Output Tristate Leakage Test (IOZL & IOZH)
- [**Level Threshold Test**](https://wiki-power.com/DC-Level_Threshold_Test)
  - Output Level Threshold Test (VOL/IOL & VOH/IOH)
  - Input Level Threshold Test (VIL & VIH)
- Optional tests
  - Input Clamp (VI)
  - Output Short-circuit Current (IOS) Test
  - Resistive Inputs Test
  - Output Fanout Test

DC parameters can also be tested with digital functional method, will be compared with the spec value by voltage comparator inside the PE (Pin Electronic) during functional test procedure, and conclude a Go/No-Go test result without specific values.

Metions that current is defined to positive when flow into DUT, and negative when flow outside of DUT.

## References & Acknowledgements

- *The Fundamentals Of Digital Semiconductor Testing*
- *Fundamentals of Testing Using ATE*

> This article is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
