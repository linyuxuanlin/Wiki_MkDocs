# Power Solution (Buck) - LMR14050

LMR14050 is a Buck converter chip from TI, with a wide input voltage range (4-40V) and the ability to provide a continuous output current of 5A. It has a sleep mode for light loads to improve efficiency. Its high internal integration means that few peripheral components are needed for design. The switching frequency can be selected within the range of 200kHz-2.5MHz through an external resistor RT, or synchronized with an external clock within the frequency range of 250kHz-2.3MHz. Protection functions include over-temperature shutdown, output over-voltage protection (OVP), input under-voltage lockout (UVLO), cycle-by-cycle current limiting, and short-circuit protection with frequency foldback.

Project repository: [**Collection_of_Power_Module_Design/DC-DC(Buck)/LMR14050**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/LMR14050>)

Project online preview:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/DC-DC(Buck)/LMR14050/LMR14050.zip"
  ></div>
</div>

## Main Features

- Topology: DC/DC (Buck)
- Device model: LMR14050SDDA
- Package: HSOIC-8
- Input voltage: 4-40 V
- Output voltage: 0.8-28V
- Output current: 5A continuous
- Operating frequency: 200kHz-2.5MHz
- Reference price: ¥11.3
- Other features
  - 40µA ultra-low operating static current
  - Shutdown current: 1µA
  - 90mΩ high-side MOS tube
  - Shortest conduction time: 75ns
  - Current mode control
  - Thermal protection, over-voltage protection, and short-circuit protection

## Internal Functional Block Diagram

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111090855.png)

## Pin Definitions

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220110170233.png)

- BOOT: Bootstrap capacitor for the high-side MOS tube. Connect a 0.1uF capacitor between BOOT and SW.
- VIN: Power input, connected to this pin after being decoupled by capacitor $C_{IN}$.
- EN: Enable switch, internally pulled up. The output can be turned off by pulling it low to 1.2V or below, and enabled by floating or connecting to $V_{IN}$. See below for adjustment of the under-voltage lockout.
- RT/SYNC: Resistor timing or external clock input. When using an external resistor to ground to set the switching frequency, the internal amplifier will keep this pin at a fixed voltage. If the pin is pulled above the PLL upper threshold, a mode change will occur and the pin will become a synchronous input. The internal amplifier is disabled, and the pin is a high-impedance clock input for the internal PLL. If the clock edge stops, the internal amplifier is re-enabled and the operation mode returns to frequency programming through the resistor.?
- FB: Feedback input pin, fed back by a resistor voltage divider from $V_{OUT}$, cannot be directly grounded.
- SS: Soft-start control pin, connected to a capacitor to set the soft-start time.
- SW: Regulated switch output, connected to the high-side MOS tube internally. Connect to the power inductor.

## Feature Description

### Voltage Regulation Principle

The output voltage of LMR14050 is adjusted by opening the high-side N-MOS and controlling the conduction time. During the conduction of the high-side N-MOS, the SW pin voltage swings to about $V_{IN}$, and the inductor current iL increases with a linear slope of ($V_{IN}$ – $V_{OUT}$) / L. When the high-side N-MOS is turned off, the inductor current discharges with a slope of $V_{OUT}$ / L through the freewheeling diode. The control parameters of the regulator are determined by the duty cycle D = $t_{ON}$ / $T_{SW}$, where $t_{ON}$ is the high-side switch conduction time and $T_{SW}$ is the switching period. The regulator control loop adjusts the duty cycle D to maintain a constant output voltage. In an ideal buck converter, losses are ignored, and D is proportional to the output voltage and inversely proportional to the input voltage: D = $V_{OUT}$ / $V_{IN}$.

The relationship between the SW voltage and the inductor current in continuous conduction mode (CCM) is shown below:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111095020.png)

### Sleep mode

The regulator enters sleep mode in light load conditions to improve efficiency and reduce gate drive losses (by reducing switch switching). Sleep mode is triggered if the peak output is less than 300mA.

### BOOT bootstrap circuit design

LMR14050 integrates a bootstrap voltage converter internally. By connecting a bootstrap capacitor to the BOOT and SW pins, a voltage sufficient to drive the high-side MOS gate can be provided. The recommended reference value for the BOOT capacitor is 0.1uF (X7R or X5R ceramic capacitor with a voltage rating of at least 16V).

### Output voltage regulation

LMR14050 provides an internal reference voltage of 0.75V. The output voltage is divided by a resistor divider and input to the FB pin for comparison and regulation internally. The divider resistors are recommended to have a deviation of 1% or lower and a temperature coefficient of 100 ppm or lower. The low-side resistor $R_{FBB}$ (reference value is 10-100kΩ) is selected based on the desired divider current, and the high-side resistor $R_{FBT}$ is calculated using the formula below. Choosing a larger resistor value is beneficial for improving light load efficiency, but if it is too large, the regulator will be more susceptible to noise and voltage errors from the FB input current.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111105814.png)

$$
R_{FBT}=\frac{V_{OUT}-0.75}{0.75}R_{FBB}
$$

### EN enable and undervoltage lockout adjustment

LMR14050 turns on the output when $V_{IN}$ is above the 3.7V threshold and EN is above the 1.2V threshold, and turns off the regulator when $V_{IN}$ drops below 3.52V or EN drops below 1.2V. EN has an internal pull-up current source (1uA) to ensure normal output of the regulator when the EN pin is floating.

The start and stop voltage thresholds can be adjusted by adjusting the external pull-up and pull-down resistors of EN:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111111613.png)

$R_{ENT}$ and $R_{ENB}$ are calculated using the following formulas:

$$
R_{ENT}=\frac{V_{STRAT}-V_{STOP}}{I_{HYS}}
$$

$$

R_{ENB}=\frac{V_{EN}}{\frac{V_{START}-V_{EN}}{R_{ENT}}+I_{EN}}
$$

where $V_{STRAT}$ is the desired start-up voltage threshold, $V_{STOP}$ is the desired undervoltage shutdown voltage threshold, and $I_{HYS}$ is the hysteresis current from EN when the voltage exceeds 1.2V (typical value is 3.6uA).

### External soft start

Soft start is used to resist the surge current to the regulator and load when power is turned on, and can be configured by connecting a capacitor $C_{SS}$ between SS and GND externally. An internal current source $I_{SS}$ (typical value is 3uA) charges the capacitor and generates a ramp from 0V to $V_{REF}$. The soft start time can be configured using the formula:

$t_{SS}(ms)=\frac{C_{SS}(nF)*V_{REF}(V)}{I_{SS}(uA)}$

The soft start is reset when the regulator is disabled or internally shut down.

### Switching Frequency and Synchronization (RT/SYNC)

The switching frequency of LMR14050 can be programmed by the resistor $R_T$ connected between RT/SYNC and GND. The RT/SYNC pin cannot be left floating or connected to ground. The resistance value can be determined using the following formula or chart:

$$
R_T(kΩ)=32537*f_{SW}^{-1.045}(kHz)
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111135021.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111135034.png)

The switching action of LMR14050 can also be synchronized with an external clock input signal (250kHz-2.3MHz):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111141247.png)

The internal oscillator will be synchronized with the falling edge of the external clock. The recommended high level of the external clock is not less than 1.7V, the low level is not higher than 0.5V, and the minimum pulse width is not less than 30ns. If a low impedance signal source is connected, the frequency setting resistor $R_T$ needs to be connected in parallel with the AC coupling resistor $C_{COUP}$ (which can be a 10pF ceramic capacitor) and connected to the terminal resistor $R_{TERM}$ (such as 50Ω) to better match the impedance.

### Overcurrent and Short Circuit Protection

LMR14050 limits the peak current of the high-side MOSFET on a per-cycle basis to prevent overcurrent situations. The peak current of the high-side switch is limited by a constant clamp maximum peak current threshold. Therefore, the peak current limitation of the high-side switch is not affected by slope compensation and remains constant throughout the duty cycle range.

### Overvoltage Protection

LMR14050 has built-in output overvoltage protection (OVP) circuitry to minimize voltage overshoot. When the FB voltage reaches the rising OVP threshold (109% of VREF), the high-side MOSFET is turned off; when it drops below the falling OVP threshold (107% of VREF), the high-side MOSFET resumes normal operation.

### Thermal Shutdown Protection

LMR14050 has internal thermal shutdown protection. When the junction temperature exceeds 170℃, the thermal shutdown is activated and the high-side MOSFET stops switching. The chip will only perform an internal soft restart when the temperature drops below 158℃.

## Reference Design

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111143510.png)

Design parameters:

- Input voltage $V_{IN}$: 7-36V, typical value is 12V
- Output voltage $V_{OUT}$: 5V
- Maximum output current $I_{O\_MAX}$: 5A
- Transient response (0.5-5A): 5%
- Output voltage ripple: 50mV
- Input voltage ripple: 400mV
- Switching frequency $f_{SW}$: 300kHz
- Soft start time: 5ms

### Output Voltage Setting

According to the formula above, if we need an output voltage of 5V, we can choose $R_{FBT}$ as 100kΩ and $R_{FBB}$ as 17.4kΩ (approximated to 17.65kΩ, balanced by debugging losses).

If we need an output voltage of 12V, we can choose $R_{FBT}$ as 100kΩ and $R_{FBB}$ as 6.34kΩ (approximated to 6.666kΩ, balanced by debugging losses).

### Switching Frequency Setting

We choose a switching frequency of 300kHz, and according to the formula above, $R_T$ is selected as 84.5kΩ (approximated to 83.9kΩ).

### Output Inductor Selection

In DC-DC, the most critical parameters of an inductor are its inductance value, saturation current, and RMS current. The selection of the inductance value is based on the required peak-to-peak ripple current $Δi_L$. Since the ripple current increases with the input voltage, the maximum input voltage is always used to calculate the minimum inductance value $L_{MIN}$. The minimum value of the output inductor can be calculated using the formula:

$$
Δi_L=\frac{V_{OUT}*(V_{IN\_MAX}-V_{OUT})}{V_{IN\_MAX}*L*f_{SW}}
$$

$$
L_{MIN}=\frac{V_{IN\_MAX}-V_{OUT}}{I_{OUT}*K_{IND}}*\frac{V_{OUT}}{V_{IN\_MAX}*f_{SW}}
$$

Where $K_{IND}$ is the coefficient representing the ripple current of the inductor relative to the maximum output current, and a reasonable value should be 20%-40%. During instantaneous short-circuit or overcurrent operation events, the RMS and peak inductor currents may be high. The rated value of the inductor current should be higher than the current limit.

Generally speaking, the lower the inductance value, the better, because it usually brings faster transient response, smaller DCR and smaller size. However, too low inductance value may bring larger inductor current ripple, which may mistakenly trigger overcurrent protection at full load. Due to the slightly higher RMS current, it also generates more conduction losses. Larger inductor current ripple also means larger output voltage ripple. For peak current mode control, it is not recommended to have too small inductor current ripple, and larger peak current ripple can improve the signal-to-noise ratio of the comparator.

In the reference design, the value of $K_{IND}$ is taken as 0.4, so the minimum inductance value calculated is 7.17uH, and the close value is 8.2uH. An 8.2 μH ferrite inductor with 7A RMS current and 10A saturation current can be used.

### Output Capacitor Selection

The selection of output capacitor $C_{OUT}$ directly affects the steady-state output voltage ripple, loop stability, and voltage overshoot and undershoot during load current transients. The output ripple is essentially composed of two parts. One is caused by the inductor current ripple through the equivalent series resistance (ESR) of the output capacitor:

$$
ΔV_{OUT\_ESR}=Δi_L*ESR=K_{IND}*I_{OUT}*ESR
$$

The other is caused by the inductor current ripple charging and discharging the output capacitor:

$$
ΔV_{OUT\_C}=\frac{Δi_L}{8*f_{SW}*C_{OUT}}=\frac{K_{IND}*I_{OUT}}{8*f_{SW}*C_{OUT}}
$$

These two voltage ripples are not in phase, so the actual peak-to-peak ripple will be smaller than the sum of the two.

If the system requires strict voltage regulation (large current step and fast voltage slew rate), the output capacitor will be constrained by transient performance specifications. When there is a rapid increase in large loads, the output capacitor can provide the required charge before the inductor current rises to an appropriate level. The control loop of the regulator usually requires at least three clock cycles to respond to the output voltage drop. The output capacitor must be large enough to provide the current difference of three clock cycles to keep the output voltage within the specified range.

When the load suddenly decreases significantly, the output capacitor will absorb the energy stored in the inductor. The clamp diode cannot conduct current, so the energy in the inductor will cause the output voltage to overshoot. The formula for calculating the minimum output capacitance required for a specific output undershoot is:

$C_{OUT}>\frac{3*(I_{OH}-I_{OL})}{f_{SW}*V_{US}}$

The formula for calculating the minimum capacitance required to keep the voltage overshoot within a specified range is:

$C_{OUT}>\frac{I_{OH}^2-I_{OL}^2}{(V_{OUT}+V_{OS})^2-V_{OUT}^2}*L$

Where,

- $K_{IND}$ is the ripple ratio of inductor current ($Δi_L/I_{OUT}$)
- $I_{OL}$ is the low-level output current during load transient
- $I_{OH}$ is the high-level output current during load transient
- $V_{US}$ is the target output voltage undershoot
- $V_{OS}$ is the target output voltage overshoot

In the reference design, the target output ripple is 50mV. Assuming $ΔV_{OUT\_ESR}=ΔV_{OUT\_C}=50mV$, $K_{IND}$ is 0.4, $ESR$ is not greater than 25mΩ, and $C_{OUT}$ is not less than 16.7 μF, the overshoot and undershoot range of the reference design is $V_{US}=V_{OS}=5%*V_{OUT}=250mV$. Therefore, $C_{OUT}$ can be calculated to be not less than 180uF and 79.2uF, so the stricter standard of 180uF is selected, that is, 4 47uF (16V, X7R ceramic capacitor, ESR is 5mΩ) are connected in parallel.

### Schottky Diode Selection

The rated breakdown voltage of the diode is best 25% higher than the maximum input voltage. For optimal reliability, the rated current of the diode should be equal to the maximum output current of the regulator. When the input voltage is much higher than the output voltage, the average current of the diode will be lower. At this time, a diode with a lower rated average current, about $(1-D) * I_{OUT}$, can be used, but the rated peak current should be higher than the maximum load current. Generally, start with 6-7A.

### Input Capacitor Selection

LMR14050 requires high-frequency input decoupling capacitors and large-capacity input capacitors. The typical recommended value for high-frequency decoupling capacitors is 4.7-10 μF (X5R/X7R, ceramic capacitors, withstanding voltage at least twice the maximum input voltage). In the reference design, two 2.2 μF X7R ceramic capacitors with a rated voltage of 100 V are used. The high-frequency filtering capacitor needs to be placed close to the regulator.

The large-capacity capacitor provides damping for voltage spikes, with a reference value of 47uF or 100uF electrolytic capacitors.

### BOOT Capacitor Selection

LMR14050 requires a BOOT capacitor, as mentioned earlier, with a reference value of 0.1uF (X7R or X5R ceramic capacitor, withstanding voltage of at least 16V).

### Soft-Start Capacitor Selection

According to the formula mentioned earlier, if the soft-start time is set to 5ms, the soft-start capacitor should be 22 nF (close to the calculated value of 20nF).

## Layout Reference

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220110183248.png)

Layout suggestions to reduce EMI:

1. The feedback network, resistors $R_{FBT}$ and $R_{FBB}$ should be placed as close as possible to the FB pin. The sampling path of $V_{OUT}$ should be far away from the noise generation path, preferably on the other side of the shielding layer.
2. The input decoupling capacitor should be placed as close as possible to $V_{IN}$ and GND.
3. The inductor should be placed close to the SW pin to reduce magnetic noise and electrostatic noise.
4. The output capacitor $C_{OUT}$ should be placed close to the node of the inductor and diode, with the wiring as short as possible to reduce conducted and radiated noise and improve efficiency.
5. The grounding connections of the diode, $C_{IN}$, and $C_{OUT}$ should be as small as possible and connected to the system grounding layer at only one point (preferably at the grounding point of $C_{OUT}$) to minimize conducted noise in the system grounding layer.

## Actual Test

With 24V input and 5V/5A full load output, the actual output is 4.95V/5.00A, with a ripple of 15mV and a temperature of 110℃.

## Reference and Acknowledgments

- [Technical Document · LMR14050](https://www.ti.com.cn/product/cn/LMR14050#tech-docs)
- [N-1149 Layout Guidelines for Switching Power Supplies](https://www.ti.com/lit/an/snva021c/snva021c.pdf?ts=1641814411004)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
