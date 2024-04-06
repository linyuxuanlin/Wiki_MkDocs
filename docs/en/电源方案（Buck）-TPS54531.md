# Power Solution (Buck) - TPS54531

The TPS54531 is a 3.5V to 28V input, 5A, 570kHz Buck converter with Eco-mode from TI.

Project Repository: [**Collection_of_Power_Module_Design/DC-DC(Buck)/TPS54531**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/TPS54531>)

Project Online Preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/DC-DC(Buck)/TPS54531/TPS54531.zip"
  ></div>
</div>

## Key Features

- **Topology**: DC/DC (Buck)
- **Input Voltage**: 3.5-28 V
- **Output Voltage**: Minimum 0.8 V
- **Output Current**: 5 A
- **Switching Frequency**: 570 kHz
- **Efficiency**: Up to 92%
- **Price**: ¥3.80
- **Features**:
  - Eco-mode function with pulse skipping at light loads
  - Adjustable soft-start to limit inrush current
  - Programmable undervoltage lockout (UVLO) threshold
  - Overvoltage transient protection
  - Cycle-by-cycle current limit, frequency foldback, and thermal shutdown protection

## Pin Definitions

![](https://media.wiki-power.com/img/20210713153815.png)

## Reference Design

![](https://media.wiki-power.com/img/20210713173605.png)

## Parameter Adjustment

(For more detailed parameters, please refer to the datasheet)

### Output Voltage Adjustment

The output voltage can be set by adjusting the feedback voltage divider resistors $R_5$ and $R_6$ (with reference voltage $V_{REF}=0.8 V$):

$$
V_{OUT}=V_{REF}\times[\frac{R5}{R6}+1]
$$

$R_5$ is approximately 10 kΩ. In the reference design, we need an output of 4.96 V, so we take $R_5$ = 10.2 kΩ and $R_6$ = 1.96 kΩ.

### Enable Pin

The EN pin is disabled when it is below 1.25 V and floating to enable. Here, two resistors are used for undervoltage lockout.

### Eco-mode Power Saving Mode

When the peak current of the inductor is below 160 mA, the chip enters the power-saving mode and shuts off the output.

### Thermal Shutdown

When the chip temperature exceeds 165℃, the chip stops operating. It restarts when the temperature is below 165℃.

## PCB Layout Reference

![](https://media.wiki-power.com/img/20210713161521.png)

![](https://media.wiki-power.com/img/20210713162833.png)

## Pitfall Summary

- The current of the freewheeling diode and inductor should be greater than the output current.
- The backside of the chip should have bare copper with tin plating for heat dissipation.
- The layout should follow the current flow of the Buck converter.
- The finished board can output a current of 5 A, but additional heat dissipation is required for continuous operation above 3 A. Power devices such as diodes and inductors may become hot.

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
