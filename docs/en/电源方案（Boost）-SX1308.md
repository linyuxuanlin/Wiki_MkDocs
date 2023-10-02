# Power Solution (Boost) - SX1308

Note: This IC is unstable and not recommended for use.

Project link: **<https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/Power/SX1308>**

- **Principle**: DC/DC (Boost)
- **Input voltage**: 2-24 V
- **Output voltage**: up to 28 V
- **Output current**: 2 A
- **Operating frequency**: 1.2 MHz
- **Efficiency**: up to 97%
- **Price**: ¥0.57
- **Features**
  - Built-in soft start
  - Input undervoltage lockout
  - Automatic switch to PFM mode under light load
  - Current limiting
  - Overheat protection

## Pin Definitions

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713154103.png)

## Reference Design

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210715141625.png)

## Parameter Adjustment

(For more detailed parameters, please refer to the datasheet)

### Output Voltage Adjustment

The output voltage can be set by adjusting the feedback voltage divider resistors $R_1$ and $R_2$ (feedback voltage $V_{REF}=0.6 V$):

$V_{OUT}=V_{REF}\times(1+\frac{R_1}{R_2})$

Generally, if $R_2$ is selected as 10 kΩ, the relationship between $V_{OUT}$ and $R_1$ is as follows:

| $V_{OUT}$ |  $R_1$  |
| :-------: | :-----: |
|    5 V    | 73.2 kΩ |
|   10 V    | 158 kΩ  |
|   12 V    | 191 kΩ  |
|   15 V    | 240 kΩ  |
|   20 V    | 324 kΩ  |

### Enable Pin

EN is the enable pin, which starts when it is greater than 1.5 V and shuts down when it is less than 0.4 V. Do not leave this pin floating.

## PCB Layout Reference

- Place the input capacitor near the IC power pin.
- Place the input and output capacitors near the IC's GND to reduce the current loop area.
- Widen and shorten the traces of VIN, SW, and VOUT to pass larger AC currents.
- Reduce the copper area at the SW pin of the chip to prevent EMI caused by AC voltage.
- Shorten the FB trace to prevent noise interference. Place the feedback resistor near the chip, and place the GND of R2 as close as possible to the GND pin of the IC. The wiring from VOUT to R1 should be far away from the inductor and switch nodes.

## Pitfalls Summary

- The 15 pF NP0 capacitor in the Chinese datasheet's reference schematic is likely drawn incorrectly and should be a grounded filtering capacitor (which can also be omitted). If not removed, it cannot handle large loads.
  - Refer to the technical post <http://www.crystalradio.cn/thread-1497661-1-1.html>.
- **This circuit is greatly affected by PCB layout**. The copper area at the SW pin should not be too large, or there will be parasitic capacitance. Other layout considerations should strictly follow the above reference.
- The maximum output current under load was tested to be around 800 mA, which can basically maintain a stable output voltage (11.6 V output).
- **The EN pin cannot be left floating** and must be pulled up (to enable Boost) or pulled down (to disable it), otherwise it will output at the original voltage.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.