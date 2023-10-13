# Power Solution (Buck) - XL2009E1

XL2009E1 is a Buck chip from Xilinx with a maximum input of 36V, output of 3A, and fixed frequency of 180kHz. It has overcurrent protection, and when short-circuited, the frequency drops to 48kHz.

Project repository: [**Collection_of_Power_Module_Design/DC-DC(Buck)/XL2009E1**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/XL2009E1>)

## Main Features

- Topology: DC/DC (Buck)
- Device Model: XL2009E1
- Package: SOP8L
- Input Voltage: 8-36V
- Output Voltage: 1.25-32V
- Minimum Input-Output Difference: 0.3V
- Maximum Duty Cycle: 100%
- Operating Frequency: Fixed 180kHz
- Maximum Output Current: 3A
- Efficiency (Input 12V, Output 5V@2.1A): 89%
- Reference Price: ¥2.1
- Other Features
  - Output Constant Current Loop
  - Built-in Short Circuit Protection
  - Built-in Current Limit Protection

## Typical Application Circuit

According to the datasheet's typical application circuit (input 8-36V, output 5V@2.1A):

![](https://img.wiki-power.com/d/wiki-media/img/20220407103157.png)

## Pin Definitions

![](https://img.wiki-power.com/d/wiki-media/img/20220407065806.png)

- FB: Feedback input pin, feedback is input through a resistor divider from $V_{OUT}$, cannot be directly grounded. The feedback reference voltage is 1.25V.
- OCSET: Output constant current setting pin.
- VC: Internal regulator bypass capacitor. Generally connected to 1uF to VIN.
- VIN: Power input pin. Input voltage is 8-36V. Requires a large decoupling capacitor.
- SW: Buck switch output.

## Feature Description

### Internal Functional Block Diagram

![](https://img.wiki-power.com/d/wiki-media/img/20220407070413.png)

### Output Voltage Regulation

XL2009E1 provides an internal reference voltage of 1.25V. The output voltage is divided by resistors from $V_{OUT}$ and input to the FB pin for internal comparison and adjustment. The divider resistors are recommended to have a deviation of 1% or lower and a temperature coefficient of 100 ppm or lower. Choosing larger resistor values for the divider is beneficial for improving light load efficiency, but if they are too large, the regulator will be more susceptible to noise and voltage errors from the FB input current. It is recommended to use a low-side resistor $R_1$ value of 4.7k and calculate the high-side resistor $R_2$ using the formula:

$$
V_{OUT}=1.25*(1+\frac{R_2}{R_1})
$$

### Schottky Diode Selection

The rated breakdown voltage of the diode should be 25% higher than the maximum input voltage. For optimal reliability, the rated current of the diode should be equal to the maximum output current of the regulator. When the input voltage is much higher than the output voltage, the average current of the diode will be lower, and a diode with a lower average current rating can be used, approximately $(1-D) * I_{OUT}$, but the peak current rating should be higher than the maximum load current.

The datasheet for XL2009E1 provides a direct selection table (3A):

| Input Voltage | Model       |
| ------------- | ----------- |
| 20V           | SK32        |
| 30V           | SK33/30WQ03 |
| 40V           | SK34/30WQ04 |
| 50V           | SK35/30WQ05 |
| 60V           | SK36        |

### Parameter Curve

Relationship between output voltage and current:

![](https://img.wiki-power.com/d/wiki-media/img/20220407100229.png)

Relationship between efficiency and output current:

Relationship between Output Current and RCS Resistance (Constant Current Control):

![](https://img.wiki-power.com/d/wiki-media/img/20220407103033.png)

Reference and Acknowledgements:

- [XL2009_Datasheet](https://datasheet.lcsc.com/lcsc/1806111754_XLSEMI-XL2009E1_C73335.pdf)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
