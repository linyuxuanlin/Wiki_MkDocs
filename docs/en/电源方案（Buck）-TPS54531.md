# Power Solution (Buck) - TPS54531

TPS54531 is a 3.5V to 28V input, 5A, 570kHz Buck converter with Eco-mode from TI.

Project repository: [**Collection_of_Power_Module_Design/DC-DC(Buck)/TPS54531**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/TPS54531>)

Project online preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/DC-DC(Buck)/TPS54531/TPS54531.zip"
  ></div>
</div>

## Main Features

- **Topology**: DC/DC (Buck)
- **Input Voltage**: 3.5-28 V
- **Output Voltage**: Minimum 0.8 V
- **Output Current**: 5 A
- **Switching Frequency**: 570 kHz
- **Efficiency**: Up to 92%
- **Price**: ¥3.80
- **Features**
  - Eco-mode function for light load pulse skipping
  - Adjustable slow start to limit inrush current
  - Programmable undervoltage lockout (UVLO) threshold
  - Overvoltage transient protection
  - Cycle-by-cycle current limiting, frequency foldback, and thermal shutdown protection

## Pin Definitions

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713153815.png)

## Reference Design

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713173605.png)

## Parameter Adjustment

(For more detailed parameters, please refer to the datasheet)

### Output Voltage Adjustment

Set the output voltage (feedback voltage $V_{REF}=0.8 V$) by adjusting the feedback voltage divider resistors $R_5$ and $R_6$:

$$
V_{OUT}=V_{REF}\times[\frac{R5}{R6}+1]
$$

$R_5$ is approximately 10 kΩ. In the reference design, we need an output of 4.96 V, so we take $R_5$ = 10.2 kΩ and $R_6$ = 1.96 kΩ.

### Enable Pin

The EN pin is disabled below 1.25 V and floating to enable. Here, two resistors are used for undervoltage lockout.

### Eco-mode Energy-saving Mode

When the peak current of the inductor is less than 160 mA, the chip enters the energy-saving mode and turns off the output.

### Thermal Shutdown

When the chip temperature exceeds 165℃, the chip stops running; when it is below 165℃, it restarts.

## PCB Layout Reference

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713161521.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713162833.png)

## Pitfalls Summary

- The current of the freewheeling diode and inductor should be greater than the output current.
- The back of the chip needs bare copper plating for heat dissipation.
- The layout should follow the Buck current flow.
- The finished board can output 5 A current, but additional heat dissipation is required for long runs above 3 A. Power devices such as diodes and inductors will heat up.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
