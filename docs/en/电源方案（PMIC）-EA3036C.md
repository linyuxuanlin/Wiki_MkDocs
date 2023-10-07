# Power Management IC (PMIC) - EA3036C

EA3036C is a 3-channel PMIC suitable for applications powered by lithium batteries or DC 5V. It integrates three synchronous buck converters that provide high efficiency output during light and heavy loads. The internal compensation architecture simplifies application circuit design. In addition, independent enable control facilitates power-on sequencing. EA3036C is available in a 20-pin QFN 3x3 package.

Project repository: [**Collection_of_Power_Module_Design/PMIC/EA3036C**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3036C)

## Key Features

- Input voltage and control circuit voltage: 2.7-5.5V
- Output voltage (3 buck converters): 0.6V-Vin
- Single continuous load current: 1A (total output of 3 channels must be less than 6W)
- Fixed 1.5MHz switching frequency
- 100% duty cycle output
- Standby current: <1uA
- Independent enable control for each channel
- Internal compensation
- Cycle-by-cycle current limiting
- Short circuit protection
- Self-recovery over-temperature (OTP) protection
- Input over-voltage (OVP) protection
- 20-pin 3mm x 3mm QFN package

## Typical Application Circuit

![](https://f004.backblazeb2.com/file/wiki-media/img/20220417095917.png)

## Internal Functional Block Diagram

![](https://f004.backblazeb2.com/file/wiki-media/img/20220417001936.png)

## Pin Definitions

![](https://f004.backblazeb2.com/file/wiki-media/img/20220416234110.png)

| Pin Name | Pin Description                                             |
| -------- | ------------------------------------------------------------ |
| VCC      | Power input for internal control circuit                     |
| VINx     | Power input for channel x, decoupled with 10uF MLCC capacitor |
| LXx      | Switching output of internal MOS tube for channel x, can be connected to low-pass filter for more stable voltage output |
| FBx      | Feedback pin for channel x, connected to voltage output through voltage divider circuit |
| ENx      | Enable pin, cannot be left floating                          |
| GNDx     | Ground for channel x                                        |
| AGND     | Analog ground                                               |
| Bottom pad | Used for heat dissipation, needs to be grounded              |

## Feature Description

### PFM/PWM Mode

Each buck can operate in PFM/PWM mode. If the output current is less than 260mA (typical value), the regulator will automatically enter PFM mode. The output voltage and ripple in PFM mode are higher than those in PWM mode. However, PFM is more efficient than PWM in light loads.

### Enable Switch

EA3036C is a power management IC designed specifically for IPC applications, with three 1A synchronous bucks that can be controlled by individual EN pins for enable switch.

If you need to set the turn-on time for each buck, you can use the following circuit for programming:

### 180° Phase Shift Architecture

To reduce input ripple current, the EA3036C adopts a 180° phase shift architecture. Buck1 and Buck3 have the same phase, while Buck2 has a phase difference of 180°. This can reduce ripple current and thus reduce EMI.

### Overcurrent Protection

Each of the three regulators inside the EA3036C has its own cycle-by-cycle current limiting circuit. When the peak current of the inductor exceeds the current limit threshold, the output voltage begins to drop until the FB pin voltage is below the threshold, typically 30% lower than the reference value. Once the threshold is triggered, the switching frequency will decrease to 400KHz (typical).

### Peak Load Current

The peak load current capability of the EA3036C depends on the internal PMOS current limit, duty cycle (Vout/Vin), and inductance value. Under the conditions of Vin=5V and L=1.5uH, the output peak load current capability is shown in the following table:

| Output Voltage | Peak Load Current |
| -------------- | ----------------- |
| 3.3V           | 1.2A              |
| 1.8V           | 1.5A              |
| 1.5V           | 1.5A              |
| 1.2V           | 1.5A              |

It should be noted that the total output power must be less than 6W to avoid chip overheating and damage.

### Thermal Shutdown

If the chip temperature exceeds the thermal shutdown threshold, the EA3036C will automatically shut down. To avoid unstable operation, the hysteresis of the thermal shutdown is about 30°C.

### Output Voltage Regulation

The output voltage of each regulator can be adjusted by a resistor divider (R1, R2). The output voltage is calculated by the following formula:

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

If common output voltage values are required, the following resistor divider configurations (all with 1% accuracy) can be used:

| Output Voltage | R1    | R2    |
| -------------- | ----- | ----- |
| 3.3V           | 68kΩ  | 15kΩ  |
| 1.8V           | 200kΩ | 100kΩ |
| 1.5V           | 150kΩ | 100kΩ |
| 1.2V           | 100kΩ | 100kΩ |

### Input/Output Capacitor Selection

The input capacitor is used to suppress the noise amplitude of the input voltage and provide a stable, clean DC input for the device, while the output capacitor can suppress the output voltage ripple. Both input and output capacitors can use MLCC capacitors (low ESR).

The recommended capacitor models for input/output are as follows:

| NPM            | Capacitance | Voltage Rating | Package |
| -------------- | ----------- | -------------- | ------- |
| C2012X5R1A106M | 10uF        | 10V            | 0805    |
| C3216X5R1A106M | 10uF        | 10V            | 1206    |
| C2012X5R1A226M | 22uF        | 10V            | 0805    |
| C3216X5R1A226M | 22uF        | 10V            | 1206    |

### Output Inductor Selection

The selection of the output inductor mainly depends on the ripple current $\Delta I_L$ passing through the inductor. The larger the $\Delta I_L$, the larger the output voltage ripple and loss. Although small inductors can save cost and space, larger inductance values can obtain smaller $\Delta I_L$, resulting in smaller output voltage ripple and loss. The calculation formula for inductance value is:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

For most applications, the EA3036C can use 1.0~2.2uH inductors.

### Power Consumption

The total power consumption of the EA3036C should not exceed 6W, and the calculation formula is as follows:

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Layout Reference

Layout of PMIC requires attention. The following suggestions can be referred to for optimal performance:

- It is recommended to use a 4-layer PCB layout, with the LX plane and output plane on the top layer, and the VIN plane on the inner layer.
- The ground pins of the top layer input/output surface mount capacitors should be connected to the inner layer ground and bottom layer ground through vias.
- AGND should be directly connected to the internal ground layer through vias.
- Try to widen the traces for high current paths.
- Place input capacitors as close as possible to the VINx pins to reduce noise interference.
- Keep the feedback path (from VOUTx to FBx) away from noise nodes (such as LXx). LXx is a high current noise node. Use short and wide traces for layout.
- Multiple holes need to be drilled from the chip bottom pad to the inner and bottom layer ground for heat dissipation.

## Reference and Acknowledgement

- [EA3036C](http://www.everanalog.com/Product/ProductEA3036CDetailInfo.aspx)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.