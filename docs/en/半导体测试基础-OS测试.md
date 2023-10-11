# Semiconductor Testing Basics - OS Testing

Open-Short Test (OS), also known as continuity or contact test, is used to **verify the electrical contact of all pins of the device with the testing system and ensure that there is no short circuit with other pins or with the power supply (ground)**. OS testing can quickly detect electrical and physical defects in the DUT, such as pin shorts, missing bond wires, electrostatic damage to pins, and manufacturing defects; it can also detect problems related to testing accessories, such as ProbeCard or device Socket contact issues.

**The process of OS testing is carried out by using protection diodes for VDD and ground**. There are generally two testing methods: one is to inject current with PMU to measure voltage; the other is to provide VREF with functional testing method to form dynamic load current and then measure voltage.

### OS Testing - Static Method

Serial/parallel static method tests OS, which is actually injecting current to measure voltage, because this current will cause a protection diode to forward bias, so the abnormality of open and short circuits can be detected by detecting the forward voltage drop. The test schematic diagram of applying positive current to forward bias the power supply diode is as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220805165031.png)

The test process is as follows:

1. Ground all pins of the DUT, including power and ground.
2. PMU applies current (about 100µA) to the pins.
3. Detect the pin voltage
   - Higher than VOH (+1.5V): Fail (Open)
   - Lower than VOL (+0.2V): Fail (Short)
   - Other intervals (forward voltage, such as 0.65V): Pass

The test schematic diagram of applying negative current to forward bias the ground diode is as follows:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220728142155.png)

The test process is as follows:

1. Ground all pins of the DUT, including power and ground.
2. PMU applies current (about -100µA) to the pins.
3. Detect the pin voltage
   - Higher than VOH (-0.2V): Fail (Short)
   - Lower than VOL (-1.5V): Fail (Open)
   - Other intervals (voltage drop after forward bias is about -0.65V): Pass

Because the PMU provides constant current, a voltage clamp needs to be set to clamp the voltage generated during open circuit pin testing, otherwise the voltage will be infinite. If the clamp voltage is set to 3V, then when a pin is open, its test result is 3V.

This method is only suitable for testing signal IO pins and cannot be used to test power supply pins. Although power supply pins can also be tested under open circuit conditions, different test limits need to be set due to their different internal structures.

In summary, the characteristics of OS static testing are:

- The serial method tests only one pin at a time, with simple steps but low efficiency, suitable for DUTs with fewer pins.
- The parallel method requires the testing system to have PPMU, and the disadvantage is that it cannot detect adjacent pin shorts. The solution is to test in two steps (such as testing pins 1357 in the first step and pins 2468 in the second step).
- Apply current and measure voltage.

## References and Acknowledgments

- "The Fundamentals Of Digital Semiconductor Testing"
- "DC Test Theory"

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
