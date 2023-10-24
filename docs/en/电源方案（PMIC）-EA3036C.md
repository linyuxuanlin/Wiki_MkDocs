# Power Solution (PMIC) - EA3036C

EA3036C is a 3-channel PMIC suitable for applications powered by a lithium battery or a 5V DC supply. It integrates three synchronous buck converters internally, providing high-efficiency outputs in both light and heavy load conditions. The internal compensation architecture simplifies the design of the application circuit. In addition, the independent enable control facilitates power-on sequencing. EA3036C is available in a 20-pin QFN 3x3 package.

Project Repository: [**Collection_of_Power_Module_Design/PMIC/EA3036C**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3036C)

## Key Features

- Input Voltage and Control Circuit Voltage: 2.7-5.5V
- Output Voltage (3 Buck Converters): 0.6V-Vin
- Single-channel Continuous Load Current: 1A (total output of 3 channels must be less than 6W)
- Fixed 1.5MHz Switching Frequency
- 100% Duty Cycle Output
- Standby Current: <1uA
- Independent Enable Control for each channel
- Internal Compensation
- Cycle-by-cycle Current Limiting
- Short Circuit Protection
- Self-recovery Overtemperature (OTP) Protection
- Input Overvoltage (OVP) Protection
- 20-pin 3mm x 3mm QFN Package

## Typical Application Circuit

![](https://img.wiki-power.com/d/wiki-media/img/20220417095917.png)

## Internal Functional Block Diagram

![](https://img.wiki-power.com/d/wiki-media/img/20220417001936.png)

## Pin Definitions

![](https://img.wiki-power.com/d/wiki-media/img/20220416234110.png)

| Pin Name | Pin Description                                             |
| -------- | ---------------------------------------------------------- |
| VCC      | Power input pin for internal control circuit                |
| VINx     | Power input pin for channel x, decoupled with 10uF MLCC     |
| LXx      | Switching output of internal MOSFET for channel x, can be connected to a low-pass filter for more stable voltage output |
| FBx      | Feedback pin for channel x, connected to voltage output through a voltage divider |
| ENx      | Enable pin, must not be left floating                       |
| GNDx     | Ground for channel x                                        |
| AGND     | Analog ground                                               |
| Bottom Pad | Heat dissipation, needs to be connected to ground           |

## Feature Description

### PFM/PWM Mode

Each Buck converter can operate in PFM/PWM mode. If the output current is less than 260mA (typical value), the regulator will automatically enter PFM mode. The output voltage and ripple in PFM mode are higher than those in PWM mode. However, PFM mode is more efficient than PWM mode in light load conditions.

### Enable Switch

EA3036C is a power management IC designed specifically for IPC applications, which includes three 1A synchronous Bucks that can be controlled by individual EN pins for enable switch.

If it is necessary to set the turn-on time for each Buck, programming can be done using the following circuit:

![](https://img.wiki-power.com/d/wiki-media/img/20220417100845.png)

### 180° Phase Shift Architecture

In order to reduce input ripple current, the EA3036C adopts a 180° phase-shift architecture. Buck1 and Buck3 have the same phase, while Buck2 has a phase difference of 180°. This can reduce ripple current and thus reduce EMI.

### Overcurrent Protection

Each of the three regulators inside the EA3036C has its own cycle-by-cycle current limiting circuit. When the peak current of the inductor exceeds the current limit threshold, the output voltage starts to decrease until the voltage at the FB pin is below the threshold, typically 30% lower than the reference value. Once the threshold is triggered, the switching frequency will decrease to 400KHz (typical value).

### Peak Load Current

The peak load current capability of the EA3036C depends on the internal PMOS current limit, duty cycle (Vout/Vin), and inductance value. Under the conditions of Vin=5V and L=1.5uH, the peak load current capability for different output voltages is shown in the table below:

| Output Voltage | Peak Load Current |
| -------------- | ---------------- |
| 3.3V           | 1.2A             |
| 1.8V           | 1.5A             |
| 1.5V           | 1.5A             |
| 1.2V           | 1.5A             |

It should be noted that the total output power must be less than 6W to avoid chip overheating and damage.

### Thermal Shutdown

If the chip temperature exceeds the thermal shutdown threshold, the EA3036C will automatically shut down. To avoid instability, the hysteresis of the thermal shutdown is approximately 30°C.

### Output Voltage Regulation

The output voltage of each regulator can be adjusted using a resistor divider (R1, R2). The output voltage is calculated by the following equation:

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

![](https://img.wiki-power.com/d/wiki-media/img/20220417230210.png)

If common output voltage values are required, the resistor values for the divider can be configured as shown in the table below (using 1% accuracy resistors):

| Output Voltage | R1    | R2    |
| -------------- | ----- | ----- |
| 3.3V           | 68kΩ  | 15kΩ  |
| 1.8V           | 200kΩ | 100kΩ |
| 1.5V           | 150kΩ | 100kΩ |
| 1.2V           | 100kΩ | 100kΩ |

### Input/Output Capacitor Selection

The input capacitor is used to suppress the noise amplitude of the input voltage and provide a stable and clean DC input to the device. The output capacitor can suppress the output voltage ripple. MLCC capacitors (low ESR) can be used for both input and output.

The recommended models for the input/output capacitors are as follows:

| NPM            | Capacitance | Voltage Rating | Package |
| -------------- | ----------- | -------------- | ------- |
| C2012X5R1A106M | 10uF        | 10V            | 0805    |
| C3216X5R1A106M | 10uF        | 10V            | 1206    |
| C2012X5R1A226M | 22uF        | 10V            | 0805    |
| C3216X5R1A226M | 22uF        | 10V            | 1206    |

### Output Inductor Selection

The selection of the output inductor mainly depends on the ripple current $\Delta I_L$ passing through the inductor. The larger the $\Delta I_L$, the larger the output voltage ripple and losses. Although smaller inductance can save cost and space, larger inductance values can achieve smaller $\Delta I_L$, resulting in smaller output voltage ripple and losses. The calculation formula for inductance value is as follows:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

For most applications, the EA3036C can use inductors with a value of 1.0~2.2uH.

### Power Dissipation

The total power dissipation of the EA3036C should not exceed 6W. The calculation formula is as follows:

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Layout Reference

The layout of the PMIC needs to be carefully designed. The following suggestions can be followed to achieve optimal performance:

- It is recommended to use a 4-layer PCB layout, with the LX plane and output plane placed on the top layer, and the VIN plane placed on an inner layer.
- The ground pins of the top layer input/output surface mount capacitors should be connected to the inner layer ground and bottom layer ground through vias.
- AGND should be directly connected to the internal ground layer through vias.
- Try to widen the traces for high current paths.
- Place the input capacitors as close as possible to the VINx pins to reduce noise interference.
- Keep the feedback path (from VOUTx to FBx) away from noise nodes (such as LXx). LXx is a high current noise node. Use short and wide traces to complete the layout.
- Multiple vias should be used to connect the bottom solder pads of the chip to the inner layer and bottom layer ground for heat dissipation.

## References and Acknowledgements

- [EA3036C](http://www.everanalog.com/Product/ProductEA3036CDetailInfo.aspx)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.