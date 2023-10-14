# Basics of ADC and DAC

In the real world, most signals are analog, such as temperature, sound, and air pressure. However, in signal processing and transmission, digital signals are often used to reduce noise interference. Therefore, we often convert analog signals from the real world into digital signals through ADC for calculation, transmission, and storage, and then convert them back into analog signals through DAC to present them.

![](https://img.wiki-power.com/d/wiki-media/img/20220724210409.png)

However, it should be noted that analog signals in the real world are continuous, which means they have infinite resolution. But after being converted into digital signals, a certain degree of precision will be lost, and both time and amplitude will become discrete values.

## Basic Principles of ADC

ADC (Analog-to-Digital Converter) refers to an analog/digital converter that can convert real-world analog signals, such as temperature, pressure, sound, or images, into digital form that is easier to store, process, and transmit.

### Sampling

Because the input analog signal is continuous and the output digital signal is discrete, only instantaneous sampling can be performed, and then the sampled value is converted into the output digital signal, and the next round of sampling begins.

In order to accurately represent the analog input signal $v_1$ with the signal $v_s$, the sampling theorem must be satisfied, that is, the sampling frequency $f_s$ must be at least twice the highest frequency component $f_{i(max)}$ of the analog input signal (usually 3-5 times is taken, but too high frequency requires faster working speed, which needs to be considered comprehensively):

$$
f_s≥2\cdot f_{i(max)}
$$

![](https://img.wiki-power.com/d/wiki-media/img/20220724180529.png)

As long as the sampling theorem is satisfied, the low-pass filter can be used to restore $v_s$ to $v_1$. The voltage transmission coefficient of the filter should remain unchanged when it is lower than $f_{i(max)}$, and rapidly decrease to 0 before $f_s-f_{i(max)}$.

### Hold

The hold circuit can keep the signal for a period of time after sampling is completed, allowing the ADC to have sufficient time for conversion. Generally, the higher the sampling pulse frequency and the denser the sampling, the more sampling values there are, and the output signal of the sampling-hold circuit is closer to the waveform of the input signal. The basic form of the sampling-hold circuit is as follows:

```markdown

```

Sampling - Basic Steps of Holding:

1. When the sampling control signal $v_L$ is high, the MOS transistor $T$ conducts, and $v_1$ charges the capacitor $C_H$ through resistor $R_1$ and MOS transistor $T$.
2. If $R_1=R_F$, then after charging, $v_0=v_c=-v_1$.
3. When the sampling control signal $v_L$ falls back to the low level, the MOS transistor $T$ is cut off, and the voltage on the capacitor $C_H$ will not change abruptly, so $v_0$ can also be held for a period of time, and the sampling result can be recorded.

### Quantization

The digital quantity obtained by sampling must be an integer multiple of a certain specified minimum value unit, and this conversion process is called quantization, and the minimum quantity unit taken is called the quantization unit $\Delta$. The size of the quantity represented by the lowest effective bit LSB of the digital signal is equal to $\Delta$.

Because the analog voltage is continuous, it may not be divisible by $\Delta$, resulting in quantization error.

The finer the quantization level, the smaller the quantization error, the more binary code bits are used, and the circuit is more complex.

### Encoding

Representing the quantized result in binary (or other base) is called encoding.

## Common Types of ADC

### Parallel Comparison Type (Flash)

Parallel comparison type ADC, also known as Flash ADC, belongs to direct ADC, which can directly convert the input analog voltage into output digital quantity without intermediate variable conversion. It consists of a series of voltage comparators, each of which compares the input signal with a unique divided reference voltage. The output of the comparator is connected to the input of the encoder circuit, generating binary output.

![](https://img.wiki-power.com/d/wiki-media/img/20220723163931.png)

Not only is it the simplest in operation theory, but it is also the most efficient ADC technology in terms of speed, only limited by the comparator and gate propagation delay. Unfortunately, for any given number of output bits, it is the most dense component.

The conversion speed of parallel comparison type ADC is the fastest, but the disadvantage is that it requires many voltage comparators and large-scale code conversion circuits (common parallel comparison type outputs are mostly below 8 bits).

### Successive Approximation Type

The Successive Approximation ADC uses a feedback comparison circuit structure, consisting of a comparator, DAC, register, clock pulse source, and control logic:

![](https://img.wiki-power.com/d/wiki-media/img/20220723211839.png)

The principle is to set a digital quantity, obtain a corresponding output analog voltage through the DAC, and sequentially compare this analog voltage with the input analog voltage signal starting from the highest bit. If they are not equal, adjust the selected digital quantity until the two analog voltages are equal, and the final selected digital quantity is the conversion result. The process is like using a balance to weigh an object's weight by adding larger weights first and then gradually adding or replacing smaller weights.

The advantages of the Successive Approximation ADC are high speed, low power consumption, and cost-effectiveness in low resolution (12-bit); the disadvantages are generally slower conversion rate and medium circuit size.

The Dual-Integration ADC is an indirect ADC that first converts the input analog voltage signal into a time width signal proportional to it, and then counts the fixed-frequency clock pulses within this time width, and the counted value is the digital signal proportional to the analog input voltage. Therefore, this type of ADC is also called a Voltage-Time Transformation (V-T) ADC.

The Dual-Integration ADC consists of an integrator, comparator, counter, control logic, and clock signal source, as shown in the figure:

![](https://img.wiki-power.com/d/wiki-media/img/20220723213208.png)

The advantages of the Dual-Integration ADC are stable performance (two integrations, excluding RC parameter differences) and strong anti-interference ability (integration is less affected by noise); the disadvantages are low conversion rate (conversion accuracy depends on integration time).

The Σ-Δ Modulation ADC works differently from the parallel and successive approximation ADCs mentioned above. It does not quantize and encode the absolute value of the sampled signal, but quantizes and encodes the difference (increment) between two adjacent sampled values. Its basic structure is as follows:

![](https://img.wiki-power.com/d/wiki-media/img/20220723230949.png)

It consists of a linear voltage integrator, a 1-bit output quantizer, a 1-bit input DAC, and a summing circuit. The output digital signal V0 processed by the quantizer is converted to an analog signal VF by the DAC and fed back to the input summing circuit for negative feedback, subtracted from the input signal v1, and the difference vD is obtained. The integrator linearly integrates vD and outputs the voltage VINT to the quantizer, which quantizes it into a 1-bit digital output. Since a 1-bit output quantizer is used, the output signal V0 is a data stream composed of 0 and 1 in continuous operation.

The advantage of Σ-Δ modulation ADC is that high-resolution measurement can be easily achieved, but the disadvantage is low conversion rate and large circuit scale.

### Voltage-Frequency Conversion (V-F)

Voltage-Frequency Conversion (V-F) ADC is an indirect ADC. It mainly consists of a V-F converter (also called a voltage-controlled oscillator, VCO), a counter and its clock signal control gate, a register, a monostable trigger, and other parts:

![](https://img.wiki-power.com/d/wiki-media/img/20220723233236.png)

Its principle is:

- Convert the input analog voltage signal into the corresponding frequency signal.
- Count the frequency signal within a fixed time.
- The counting result is proportional to the amplitude of the input voltage.

## Main Parameters of ADC

- **Resolution**: The amount of change in analog voltage required to produce a change of one unit in the digital output. It is usually expressed in binary digits, with a resolution of n indicating that the full scale (FS) is divided into 2^n equal parts.
- **Quantization Error**: The error introduced by the finite number of bits used to represent the analog signal in the ADC. To accurately represent the analog signal, the number of bits in the ADC needs to be very large or even infinite, so all ADC devices have quantization errors. The maximum deviation between the step-like conversion characteristic curve of an ADC with limited resolution and the conversion characteristic curve of an ADC with infinite resolution is the quantization error.
- **Conversion Rate**: The number of conversions performed per second.
- **Conversion Range**: The maximum voltage that an ADC can measure, which is usually equal to the reference voltage. Exceeding this voltage may damage the ADC. When the signal is small, the reference voltage can be lowered to improve the resolution. Changing the reference voltage will also change the corresponding conversion value. When calculating the actual voltage, the reference voltage needs to be taken into account, so the reference voltage should generally be stable and free of high-order harmonics.
- **Offset Error**: The value of the ADC conversion output signal when the input signal is 0.
- **Full Scale Error**: The difference between the input signal corresponding to the full scale output of the ADC and the ideal input signal value.
- **Linearity**: The maximum deviation between the actual transfer function of the ADC and the ideal straight line.

## Basic Principles of DAC

DAC (Digital-to-Analog Converter) refers to a digital/analog converter that can convert digital signals into proportional analog voltage or current. For example, a computer may produce digital output ranging from `00000000` to `11111111`, and the DAC converts it into a voltage ranging from 0 to 10V. From a basic principle, DAC can be divided into two types: current summing type and voltage divider type.

## Common Types of DAC

### Switched Resistor

Switched resistor DAC is the simplest and most direct type of DAC, consisting of a resistor divider and a tree-like switch network:

![](https://img.wiki-power.com/d/wiki-media/img/20220724172844.png)

These switches are controlled by 3-bit inputs $d_0,d_1,d_2$, and we have:

$$
v_0=\frac{V_{REF}}{2^1} d_2+\frac{V_{REF}}{2^2} d_1+\frac{V_{REF}}{2^3} d_0
$$

$$
v_0=\frac{V_{REF}}{2^3} (d_2 2^2+d_1 2^1+d_0 2^0)
$$

Furthermore, for an n-bit binary input switch tree DAC, the output is:

$$
v_0=\frac{V_{REF}}{2^n} (d_{n-1} 2^{n-1}+d_{n-2} 2^{n-2}+...+d_1 2^1+d_0 2^0)
$$

The switch tree DAC has the advantage of a single type of resistor and low requirements for switch conduction resistance when the output terminal does not take current. However, the disadvantage is that it uses too many switches.

### Weighted Resistor Network

The weight refers to the value represented by each bit of a multi-bit binary number. For example, for an n-bit binary number $D_n=d_{n-1}d_{n-2}...d_1 d_0$, the weights from the most significant bit (MSB) to the least significant bit (LSB) are $2^{n-1},2^{n-2}...2^1,2^0$.

The principle of the weighted resistor network DAC (which belongs to the voltage output type) is shown in the following figure (4 bits), which consists of a weighted resistor network, 4 analog switches, and 1 summing amplifier:

![](https://img.wiki-power.com/d/wiki-media/img/20220724003300.png)

Here, $S_0,S_1,S_2,S_3$ are 4 electronic switches controlled by the 4 signals $d_0,d_1,d_2,d_3$. When the input is 1, the switch is connected to $V_{REF}$, and when the input is 0, the switch is grounded. Therefore, when $d_i=1$, the current $I_i$ flows to the summing amplifier, and when $d_i=0$, the current is zero. The summing amplifier is a negative feedback amplifier. When the potential of the inverting input $V_-$ is lower than that of the non-inverting input $V_+$, the output voltage $v_0$ to ground is positive, and when $V_->V_+$, $v_0$ is negative. When $V_-$ is slightly higher than $V_+$, a large negative output voltage can be generated at $v_0$. $v_0$ is fed back to $V_-$ through $R_F$, causing $V_-$ to decrease back to 0V.

Assuming the operational amplifier is an ideal device (with zero input current), we can obtain:

$$
v_O=-R_F i_{\sum}=-R_F (I_3+I_2+I_1+I_0)
$$

Since $V_-\approx 0$, the current in each branch is:

$$
I_3=\frac{V_{REF}}{2^0 R} d_3
$$

$$
I_2=\frac{V_{REF}}{2^1 R} d_2
$$

$$
I_1=\frac{V_{REF}}{2^2 R} d_1
$$

$$
I_0=\frac{V_{REF}}{2^3 R} d_0
$$

Here, $d_n$ can be either 0 or 1. Substituting into the above equations and assuming that the feedback resistor $R_F=\frac{R}{2}$, the output voltage can be obtained as:

$$
v_O=-\frac{V_{REF}}{2^4}(d_3 2^3+d_2 2^2+d_1 2^1+d_0 2^0)
$$

Furthermore, for an n-bit weighted resistor network DAC, when the feedback resistor $R_F=\frac{R}{2}$, the output voltage calculation formula is:

$$
v_O=-\frac{V_{REF}}{2^n}(d_{n-1} 2^{n-1}+d_{n-2} 2^{n-1}+...+d_{1} 2^{1}+d_{0} 2^{0})
$$

$$
v_O=-\frac{V_{REF}}{2^n}D_n
$$

Therefore, the output analog voltage is proportional to the input digital quantity $D_n$, and its range of variation is from 0 to $-\frac{2^n-1}{2^n}V_{REF}$. On the other hand, if a positive output voltage is required, a negative $V_{REF}$ should be provided.

The advantage of the weighted resistor network DAC is its simple structure, but the disadvantage is that the resistance values may differ greatly, which may cause significant accuracy differences in reality. To improve this, a bipolar weighted resistor network can be used, which is not explained here, but still cannot fundamentally solve the problem.

### Inverted T-shaped resistor network

To improve the problem of the resistance values of the weighted resistor network DAC being too different, an inverted T-shaped resistor network DAC can be used, which only uses two types of resistors with resistance values of R and 2R (so it is also called an R2R DAC), and has great help for control accuracy:

![](https://img.wiki-power.com/d/wiki-media/img/20220724165753.png)

When the feedback resistor of the summing amplifier has a resistance value of R, the output voltage is:

$$
v_O=-Ri_{\sum}=-\frac{V_{REF}}{2^n}D_n
$$

It can be seen that the calculation formula of the inverted T-shaped resistor network is the same as that of the weighted resistor network DAC.

### Weighted current type

When analyzing the weighted resistor network and inverted T-shaped resistor network, the analog switch is treated as an ideal device. However, in reality, they have a certain on-resistance and voltage drop, and there are differences in consistency between switches, which can cause conversion errors and affect accuracy. The solution is to use a current-output DAC, which has a set of constant current sources, with each current source being half the size of the previous one and proportional to the weight of the corresponding input binary bit. The use of constant current sources ensures that the current in each branch is no longer affected by the on-resistance and voltage drop of the switch.

![](https://img.wiki-power.com/d/wiki-media/img/20220724171436.png)

When a certain bit of the input digital quantity is 1, the corresponding switch connects the constant current source to the input of the operational amplifier; when the input code is 0, the corresponding switch is grounded, so the output voltage is:

$$
v_O=\frac{R_F V_{REF}}{2^n R_R}D_n
$$

## Main Parameters of DAC

- **Resolution**: The ratio of the smallest output voltage (i.e., the voltage when the input digital quantity is 1) to the maximum output voltage (i.e., the voltage when the input digital quantity is the maximum, with each bit being 1). Generally expressed by the number of bits of the input digital quantity.
- **Conversion Range**: The maximum voltage that the DAC can output, usually related to the reference voltage or its multiple.
- **Settling Time**: The delay time from the input digital quantity to the output analog quantity.
- **Conversion Accuracy**: Similar to the conversion accuracy of ADC.

## References and Acknowledgments

- [ADC/DAC Application Design Handbook](https://picture.iczhiku.com/resource/eetop/syIFpRpWgQqgOXnx.pdf)
- [Analog-to-Digital Conversion and Digital-to-Analog Conversion](https://www.cnblogs.com/redlightASl/p/15542623.html)
- [ADC and DAC (Analog to Digital And Digital to Analog Converters)](https://www.youtube.com/playlist?list=PLwjK_iyK4LLCnW-df-_53d-6yYrGb9zZc)
- [Talking about DAC Principles](https://www.bilibili.com/read/cv4873472/)
- Analog Engineer's Pocket Reference
- Digital Electronics Technology (6th Edition) by Yan Shi

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
