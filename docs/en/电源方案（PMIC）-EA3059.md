# Power Management IC (PMIC) - EA3059

EA3059 is a 4-channel PMIC suitable for applications powered by lithium batteries or DC 5V. It integrates four synchronous buck converters that provide high-efficiency output during light and heavy loads. The internal compensation architecture simplifies application circuit design. In addition, independent enable control facilitates power-on sequencing. EA3059 uses a 24-pin QFN 4x4 package.

Project repository: [**Collection_of_Power_Module_Design/PMIC/EA3059**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3059)

Project preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/PMIC/EA3059/EA3059_V0.2.zip"
  ></div>
</div>

## Key Features

- Input voltage and control circuit voltage: 2.7-5.5V
- Output voltage (4 Buck converters): 0.6V-Vin
- Output current: single-channel continuous load 2A, peak 4A (total output of 4 channels must be less than 10W)
- Fixed 1.5MHz switching frequency
- 100% duty cycle output
- Efficiency of each channel up to 95%
- Standby current: <1uA
- Independent enable control for each channel
- Internal compensation
- Current limit per cycle
- Short circuit protection
- Self-recovery over-temperature (OTP) protection
- No input over-voltage (OVP) protection (compared to EA3059)
- 24-pin 4mm x 4mm QFN package

## Typical Application Circuit

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420171841.png)

## Internal Functional Block Diagram

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420171859.png)

## Pin Definitions

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420171920.png)

| Pin Name | Pin Description                                             |
| -------- | ------------------------------------------------------------ |
| VCC      | Power input pin for internal control circuit                 |
| VINx     | Power input pin for channel x, with 10uF MLCC capacitor decoupling |
| LXx      | Switching output of internal MOS tube for channel x, can be connected to low-pass filter for more stable voltage output |
| FBx      | Feedback pin for channel x, connected to voltage output through voltage divider circuit |
| ENx      | Enable pin, cannot be left floating                          |
| GNDx     | Ground for channel x                                        |
| AGND     | Analog ground                                               |
| Bottom Pad | Used for heat dissipation, needs to be grounded               |
| NC       | No connection                                               |

## Feature Description

### PFM/PWM Mode

Each Buck can operate in PFM/PWM mode. If the output current is less than 150mA (typical value), the regulator will automatically enter PFM mode. The output voltage and ripple in PFM mode are higher than those in PWM mode. However, PFM is more efficient than PWM under light load.

### Enable Switch

EA3059 is a power management IC designed specifically for OTT applications, which includes four 2A synchronous Bucks that can be controlled by a separate EN pin for enable switch control.

If you need to set the turn-on time for each Buck, you can program it using the following circuit:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420172125.png)

### 180° Phase-Shift Architecture

To reduce input ripple current, EA3059 uses a 180° phase-shift architecture. Buck1 and Buck3 have the same phase, while Buck2 and Buck4 have a phase difference of 180°. This can reduce ripple current and thus reduce EMI.

### Overcurrent Protection

Each regulator in EA3059 has its own per-cycle current limiting circuit. When the peak inductor current exceeds the current limit threshold, the output voltage starts to drop until the FB pin voltage is lower than the threshold, usually 30% lower than the reference value. Once the threshold is triggered, the switching frequency will decrease to 350KHz (typical value).

### Thermal Shutdown

If the chip temperature exceeds the thermal shutdown threshold, EA3059 will automatically shut down. To avoid unstable operation, the hysteresis of thermal shutdown is about 30°C.

### Output Voltage Adjustment

The output voltage of each regulator can be adjusted by a resistor divider (R1, R2). The output voltage is calculated by the following formula:

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420172602.png)

If you need to output common voltage values, you can refer to the following table to configure the divider resistors (all need to use 1% accuracy):

| Output Voltage | R1    | R2    |
| -------------- | ----- | ----- |
| 3.3V           | 510kΩ | 110kΩ |
| 1.8V           | 200kΩ | 100kΩ |
| 1.5V           | 150kΩ | 100kΩ |
| 1.1V           | 68kΩ  | 82kΩ  |

### Input/Output Capacitor Selection

The input capacitor is used to suppress the noise amplitude of the input voltage, providing a stable and clean DC input for the device, and the output capacitor can suppress the output voltage ripple. Both input and output can use MLCC capacitors (low ESR).

The recommended models for input/output capacitors are as follows:

| NPM            | Capacitance | Voltage | Package |
| -------------- | ----------- | ------- | ------- |
| C2012X5R1A106M | 10uF        | 10V     | 0805    |
| C3216X5R1A106M | 10uF        | 10V     | 1206    |
| C2012X5R1A226M | 22uF        | 10V     | 0805    |
| C3216X5R1A226M | 22uF        | 10V     | 1206    |

### Output Inductor Selection

The selection of the output inductor mainly depends on the ripple current $\Delta I_L$ through the inductor. The larger the $\Delta I_L$, the larger the output voltage ripple and loss. Although small inductors can save cost and space, larger inductance values can obtain smaller $\Delta I_L$, resulting in smaller output voltage ripple and loss. The calculation formula for inductance value is:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

For most applications, EA3059 can use 1.0~2.2uH inductors.

### Power Consumption

The total power consumption of EA3059 should not exceed 10W, calculated by the following formula:

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Layout Reference

The layout of the PMIC needs to be carefully designed. You can refer to the following suggestions to achieve the highest performance:

- It is recommended to use a 4-layer PCB layout, with the LX plane and output plane on the top layer, and the VIN plane on the inner layer.
- The ground pins of the top layer input/output surface mount capacitors should be connected to the inner layer ground and bottom layer ground through vias.
- AGND should be directly connected to the internal ground layer through vias.
- Try to widen the traces for high current paths.
- Place the input capacitors as close as possible to the VINx pins to reduce noise interference.
- Keep the feedback path (from VOUTx to FBx) away from noise nodes (such as LXx). LXx is a high current noise node. Use short and wide traces to complete the layout.
- Multiple holes need to be drilled from the chip's bottom pads to the inner and bottom layer grounds for heat dissipation.
- Place the input capacitors as close as possible to the VINx pins to reduce noise interference.

Layout reference:

Top layer:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175756.png)

Middle power layer:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175833.png)

Middle ground layer:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175851.png)

Bottom layer:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220420175906.png)

## Reference and Acknowledgement

- [EA3059](http://www.everanalog.com/ProductCN/ProductEA3059DetailInfoCN.aspx)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.