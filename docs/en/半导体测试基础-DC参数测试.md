# Semiconductor Testing Basics - DC Parameter Testing

DC parameter testing mainly measures the characteristics of individual pins on a device. For most DC parameters, the semiconductor resistivity is essentially being measured, and Ohm's law is used to explain resistivity. To verify the feasibility of the DC testing process, a resistor can also be used to simulate the DUT and eliminate problems outside of the DUT. For example, for the parameter VOL that appears in the chip specification:

| Parameter | Description        | Test Conditions        | Min | Max | Units |
| --------- | ------------------ | ---------------------- | --- | --- | ----- |
| VOL       | Output LOW Voltage | VDD = Min, IOL = 8.0mA |     | 0.4 | V     |

We can see that the maximum value of VOL is 0.4V, and IOL is 8mA, which means that when the output logic low level is present, a current of 8mA must be generated at a voltage not exceeding 0.4V. Therefore, we can conclude that the maximum resistance of this device does not exceed 50Ω. Therefore, a resistor of no more than 50Ω can be used to replace the DUT to verify the testing process. Our goal is to focus on the DUT itself, not problems outside of the DUT.

## IDD & Gross IDD

IDD represents the current (I) from the drain (D) to the drain (D) in a CMOS circuit, and if it is a TTL circuit, it is called ICC (the current from the collector to the collector). Gross IDD refers to the total current flowing into the VDD pin (can be tested at the wafer probe or finished product stage). IDD is used to determine whether the total current of the chip exceeds the standard, and generally needs to look at the current at the lowest power consumption and maximum operating frequency.

Testing Gross IDD is to determine whether DUT can continue to be tested. Usually, this test follows the OS test and is the first test after DUT is powered on. If the Gross IDD test fails (such as excessive current), then testing cannot continue.

During the Gross IDD test stage, it is not yet known whether the pre-processing can proceed normally, so the IDD specification needs to be relaxed. After the Gross IDD test is passed, the pre-processing program can be performed to accurately define the IDD specification current.

Gross IDD testing needs to be reset first to set all input pins to low/high level. Usually, VIL is set to 0V and VIH is set to VDD, and all output pins are unloaded (to prevent floating leakage current and increase IDD). The schematic diagram of the test is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220728162655.png)

Things to note:

- Current clamps need to be set to prevent damage to the testing equipment due to excessive current.
- If negative current occurs, it also means that the test fails.
- If the test fails, the problem with the testing equipment can be ruled out first. Running the test with an empty socket should result in a current of 0, otherwise it means that devices outside of the DUT are also consuming current.

### IDD Testing - Static Method

Static IDD testing measures the total current flowing into the VDD pin and generally requires the DUT to operate in the lowest power consumption mode. The difference between static IDD testing and Gross IDD testing is that Gross IDD testing does not have a pre-processing program and is only a rough test, while static IDD testing is a test performed after pre-processing.

For example, the following table is a sample IDD parameter:

| Parameter  | Description          | Test Conditions                   | Min | Max | Units |
| ---------- | -------------------- | --------------------------------- | --- | --- | ----- |
| IDD Static | Power Supply Current | VDD = 5.25V, inputs = VDD, Iout=0 |     | +22 | µA    |

The schematic diagram of IDD static testing is as follows:

The testing process is as follows:

1. Use a test vector to set the DUT to consume the least amount of current and remain in a static state.
2. Check the pin current value
   - Higher than IDD Spec: Fail
   - Other intervals: Pass

During testing, it is usually necessary to add a delay between power-up and sampling to allow parasitic capacitance to charge and avoid interference.

If it is necessary to test the static current under different logics, IDDQ parameters can be measured to increase test coverage (IDDQ measures the current in a certain static logic state, such as testing a certain state by turning on a part of MOS tube).

### IDD Test - Dynamic Method

The purpose of IDD dynamic testing is to test the current consumed by the DUT during **dynamic functional execution** (usually at the DUT's maximum operating frequency) to ensure that it does not exceed the nominal value.

For example, the following table is a sample of dynamic IDD parameters:

| Parameter   | Description          | Test Conditions                           | Min | Max | Units |
| ----------- | -------------------- | ----------------------------------------- | --- | --- | ----- |
| IDD Dynamic | Power Supply Current | VDD = 5.25V (commercial), f=f_max (66MHz) |     | +18 | mA    |

The schematic diagram of the test is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220728171447.png)

The testing process is similar to the static method.

## VOL/IOL & VOH/IOH

VOL represents the highest voltage limit when outputting a low level (L) (not recognized as logic 1). IOL represents the driving ability of the sink current (I) when outputting a low level (L) (O). They jointly measure the impedance of the pin buffer when outputting a low level, ensuring that a constant current value can be absorbed at an appropriate output voltage.

VOH represents the lowest voltage limit when outputting a high level (H) (not recognized as logic 0). IOH represents the driving ability of the source current (I) when outputting a high level (H) (O). They jointly measure the impedance of the buffer when outputting a high level, ensuring that a constant current value can be output at an appropriate output voltage.

For example, the following table is the VOL/IOL & VOH/IOH parameters of a 256 x 4 Static RAM:

| Parameter | Description         | Test Conditions           | Min | Max | Units |
| --------- | ------------------- | ------------------------- | --- | --- | ----- |
| VOL       | Output LOW Voltage  | VDD = 4.75V, IOL = 8.0mA  |     | 0.4 | V     |
| VOH       | Output HIGH Voltage | VDD = 4.75V, IOH = -5.2mA | 2.4 |     | V     |

The testing of VOL/IOL & VOH/IOH mainly verifies whether VOL/VOH is at the correct level when applying source or sink current (whether it can reach the voltage threshold at a certain output current). There are static and dynamic methods for testing. **The static method applies current to the pin and then measures the voltage one by one; the dynamic method provides VREF in the functional test to form a dynamic load current and then measures the voltage.**

### VOL/IOL Test - Serial Static Method

The schematic diagram of measuring VOL/IOL using the serial static method is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220728150542.png)

The testing process is as follows:

## VOH/IOH Testing - Serial Static Method

The test schematic for measuring VOH/IOH using the serial static method is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220728143124.png)

The testing process is as follows:

1. First, preprocess the pin to be tested as a high-level output.
2. Apply a constant IOH to the pin and wait for 1-5 milliseconds before measuring (set delay in PMU).
3. Measure the pin voltage
   - Above VOL (+0.4V): Fail
   - Other ranges: Pass

Points to note:

- IOL is a positive current value because it flows from the PMU to the DUT.
- Because a constant current is applied, a voltage clamp needs to be set. If the measured voltage is lower than the clamp voltage, it may be that the logic is set to a high level, triggering the forward bias of the power protection diode.
- The VDDmin parameter represents the minimum supply voltage that allows the DUT to be tested normally. If it is smaller, accurate test results cannot be obtained.

## IIL/IIH

IIL refers to the maximum leakage current allowed when the input pin (I) logic is low (L) and the maximum pull-up current allowed when the input pin (I) logic is high (H). For example, the IIL and IIH parameters for a 256 x 4 Static RAM are shown in the table below:

| Parameter | Description        | Test Conditions        | Min | Max | Units |
| --------- | ------------------ | ---------------------- | --- | --- | ----- |
| IIL, IIH  | Input Load Current | Vss ≤ Vin ≤ VDD(5.25V) | -10 | +10 | µA    |

IIL measures the resistance value from the input pin to VDD; IIH measures the resistance value from the input pin to VSS. This test is to ensure that the input impedance meets the design requirements and that the input current does not exceed the standard. IIL/IIH can be tested using serial/parallel/merged methods or functional testing methods. The serial method tests each pin one by one, which is accurate but relatively time-consuming.

In addition, IIL/IIH testing can usually only be performed on pure input pins. If a bidirectional pin is encountered, an output load needs to be added to stabilize the level and avoid current flowing through the protection device, affecting the test results.

### IIL/IIH Testing - Serial Static Method

The schematic for testing the input pin IIL using the serial method is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220729100620.png)

The testing process is as follows:

1. First, supply the DUT with VDDmax (worst case) power.
2. Set all input pins of the DUT to high level (VIH).
3. Use the PMU to pull a single input pin down to VSS.
4. Wait for 1-5 microseconds and measure the current value.
   - Below IIL (-10µA): Fail (current flowing into the DUT exceeds the standard)
   - Other ranges: Pass

The schematic for testing the input pin IIH using the serial method is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220729100739.png)

The testing process is as follows:

1. First, supply the DUT with VDDmax power.
2. Set all input pins of the DUT to low level (VIL).
3. Use a PMU to pull a single input pin up to VDDmax.
4. Wait for 1-5 microseconds and check the current value.
   - Higher than IIH (+10µA): Fail (current flowing out of the DUT exceeds the limit)
   - Other ranges: Pass

### IIL/IIH Test - Parallel Static Method

In some test systems, leakage current can be measured in parallel (Parallel Test Method). Parallel leakage current measurement uses multiple PMUs to measure multiple pins separately. All input pins are forced to be pulled up and the current of each pin is measured in parallel. The test results are then compared with the nominal value to draw conclusions.

![](https://img.wiki-power.com/d/wiki-media/img/20220729103317.png)

1. First, supply the DUT with VDDmax power.
2. Use multiple PMUs to force each input pin to be pulled up to VDDmax (for IIH measurement).
3. Wait for 1-5 microseconds, check the current, and draw conclusions.
4. Then pull down to VSS and repeat the above steps for IIL measurement.

The advantage of the parallel method is that it can measure the current of each pin individually and complete the IIL/IIH test quickly. The disadvantage is that it is more difficult to detect leakage between input pins because all inputs are kept at the same level.

### IIL/IIH Test - Combined Static Method

The combined test (Ganged Method) refers to merging all input pins into one pin and measuring the total leakage current with one PMU. The test schematic is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220729104449.png)

The combined test method is similar to the above. The total current limit is the nominal value of a single pin. If the test result exceeds the limit, it must be replaced with serial testing for retesting. This test is more effective for CMOS devices (high impedance input).

## IOZL/IOZH

The high impedance current IOZ refers to the leakage current (I) of the output pin (O) in high impedance state (Z). Among them, IOZL refers to the leakage current in the low level (L) state of the pin, and IOZH refers to the leakage current in the high level (H) state. It is used to see if the leakage current is excessive when the pin is turned off.

This parameter ensures that **bidirectional or high-impedance output pins can be turned off normally (output high-impedance state)**. IOZL measures the resistance of the pin to VDD in the output high-impedance state, and IOZH measures the resistance of the pin to VSS. Usually, it is expressed in the specification as follows:

| Parameter | Description           | Test Conditions                         | Min  | Max  | Units |
| --------- | --------------------- | --------------------------------------- | ---- | ---- | ----- |
| IOZ       | Output Current High-Z | VSS ≤ Vout ≤VDD(5.25V), Output Disabled | -2.0 | +2.0 | µA    |

### IOZL/IOZH Test - Serial Static Method

The schematic of the serial static test for IOZL/IOZH is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220807202447.png)

The test process is as follows:

1. First, supply the device with VDD power.
2. Set the device pins to high impedance state and use a PMU to force the pin to be pulled up / down.
3. Measure the current value of the pin.
   - Lower than -IOZ (-2µA): Fail
   - Higher than +IOZ (+2µA): Fail
   - Other ranges: Pass

The advantage of serial testing is that it can accurately measure the current value of a single pin, but the disadvantage is that it is slow. In addition, this test requires setting the clamp current.

### IOZL/IOZH Test - Parallel Static Method

The parallel static method uses multiple PMUs to simultaneously test multiple pins, and its advantages are speed.

The Input Clamp Voltage (VI) refers to the voltage measured on the input pin (I) of a TTL device (non-CMOS) when a negative current (extracted current) is applied to the pin. The purpose of this test is to verify the integrity of the clamp diode between the transistor emitter and ground. It is represented in the specification as follows:

| Parameter | Description         | Test Conditions        | Min | Max  | Units |
| --------- | ------------------- | ---------------------- | --- | ---- | ----- |
| VI        | Input Clamp Voltage | VCC = Min, Iin = -18mA |     | +1.5 | V     |

### VI Test - Serial Static Method

The VI test using the serial static method is illustrated as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220729145425.png)

The test process is as follows:

1. First, make sure that this is an input pin of a TTL device and supply power to VCCmin.
2. After setting the voltage clamp, use a PMU to extract a current of -15mA~-20mA.
3. Measure the voltage value on the pin.
   - Below VI (-1.5V): Fail
   - Other ranges: Pass

## IOS (Short Circuit Output Current)

The short circuit output current (IOS) refers to the current generated by the output pin (O) under short circuit conditions (S). The purpose is to measure the output impedance when the pin outputs a high level but is shorted to zero voltage, ensuring that the output current is not too large even under the worst load conditions. It also indicates the maximum instantaneous current that the DUT pin can provide for charging capacitive loads, which can be used to calculate the rise time. IOS is represented in the specification as follows:

| Parameter | Description                  | Test Conditions                                                                  | Min | Max | Units |
| --------- | ---------------------------- | -------------------------------------------------------------------------------- | --- | --- | ----- |
| IOS       | Output Short Circuit Current | Vout = 0V, VDD = 5.25V, \*Short only 1 output at a time for no longer than 1 sec | -85 | -30 | mA    |

### IOS Test - Serial Static Method

The IOS test using the serial static method is illustrated as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220729152549.png)

The test process is as follows:

1. Supply power to VDDmax, preprocess the device to make the pin output a high level.
2. Use a PMU to pull the pin down to 0V, measure the output current, and compare it with the nominal value to draw a conclusion.

In the IOS test, reasonable logic is needed to avoid hot switching. First, set the PMU to the voltage measurement mode with zero current, connect it to the DUT output, measure and save the VOH voltage of the DUT, then disconnect and set the PMU to pull up to the VOH voltage just measured, and then reconnect the DUT (at this time, both ends have the same voltage of VOH), and then let the PMU pull down to 0V to measure the current value. After the measurement is completed, the PMU should be restored to pull up to VOH before disconnecting. This ensures that the voltage at both ends is consistent when the relay switches on and off.

Factors that cause the test to fail:

- **Exceeding the upper limit**
  - The output impedance is too high, resulting in an absolute value of current that is insufficient.
  - The fixture itself has resistance.
  - It has not been preprocessed correctly.
- **Below the lower limit**
  - The output impedance is too low, resulting in an absolute value of current that is too large.

Some input pins may have active pull-up or pull-down structures, and it is necessary to ensure that the **resistance path of the input buffer's pull-up and pull-down** is normal. Only serial testing can be performed because the internal pull-up and pull-down structures of different pins may be different. Schematic diagram of pin structure:

![](https://img.wiki-power.com/d/wiki-media/img/20220729130655.png)

## Output Fanout

Fanout capability refers to the ability of an output pin to drive multiple input pins based on its voltage and current parameters. That is, **the driving capacity of a pin is a measure of how many input pins an output pin can drive**.

![](https://img.wiki-power.com/d/wiki-media/img/20220729132621.png)

As shown in the above figure, this TTL output can pull up about 17 input pins or pull down 30 input pins. In the specification sheet, the parameters of the pins are represented as follows:

| Parameter | Description             | Test Conditions           | Min  | Max | Units |
| --------- | ----------------------- | ------------------------- | ---- | --- | ----- |
| VOH       | Output HIGH Voltage     | VCC = 4.75V, IOH = -2.6mA | 2.4  |     | V     |
| VOL       | Output LOW Voltage      | VCC = 4.75V, IOH = 24mA   |      | 0.4 | V     |
| IIL       | Input LOW Load Current  | Vin = 0.4V                | -800 |     | µA    |
| IIH       | Input HIGH Load Current | Vin = 2.4V                |      | 150 | µA    |

The fanout capability varies greatly between TTL and CMOS devices, because CMOS has high input impedance, theoretically, a CMOS output can drive any number of CMOS inputs. However, CMOS input pins have parasitic capacitance, and the more inputs are connected, the larger the capacitance, which will cause delay due to the charging and discharging effects of the capacitance during high and low level switching.

## References and Acknowledgments

- "The Fundamentals Of Digital Semiconductor Testing"
- "DC Test Theory"

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
