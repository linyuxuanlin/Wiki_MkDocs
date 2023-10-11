# Power Supply Design - LDO Power Supply Rejection Ratio (PSRR) and Measurement Methods

One of the advantages of low dropout linear regulators (LDOs) compared to DC-DC converters is their low output voltage ripple. However, in high-speed circuits, the power supply rejection ratio (PSRR) of LDOs is also an important factor that should not be ignored. It is often mistakenly assumed to be a single static value. This article will explain in detail what PSRR is and how to measure it.

## Definition of Power Supply Rejection Ratio (PSRR)

The power supply rejection ratio (PSRR), also known as ripple rejection ratio, can usually be found in the data sheet of an LDO. It represents the attenuation from input to output at a certain frequency and represents the ripple suppression ability at different frequencies. In some high-speed communication circuits such as Wi-Fi and Bluetooth, high-speed LDOs with high PSRR are needed to respond quickly when the chip needs to instantly increase the current, so as not to drop below the rated voltage and cause the load to restart. In some scenarios, DC-DC converters are used as the first-level voltage reduction, and LDOs are used as the second-level voltage reduction/filtering. Because the DC-DC switching frequency is in the kHz-MHz range, that is, the LDO is above 100kHz, PSRR needs to be strictly considered.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220516174303.png)

The power supply rejection ratio (PSRR) is expressed by the following formula:

$$
PSRR(dB)=20\log\frac{V_{rp(in)}}{V_{rp(out)}}
$$

where $V_{rp(in)}$ represents input ripple and $V_{rp(out)}$ represents output ripple. The PSRR of a high-speed LDO is generally greater than 60dB, while that of a regular LDO is generally around 20dB. A PSRR of 60dB means that when the input ripple is 1V, the output ripple will be 1mV.

Let's first look at the ripple suppression curve of a regular LDO (XC6206 series):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220421142140.png)

It can be seen that the ripple suppression ratio of XC6206P302 is about 23dB at a frequency of 1kHz.

Now let's look at the ripple suppression curve of a high-speed LDO (XC6217x302):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220421141923.png)

At a frequency of 1kHz, the ripple suppression ratio of XC6217x302 is about 68dB.

## Measurement Methods for Power Supply Rejection Ratio (PSRR)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424104353.png)

The measurement of power supply rejection ratio (PSRR) involves two parts: input injection and output measurement. PSRR can be calculated based on the following methods by testing and recording the voltage ripple of the input and output.

### Input Injection

#### Signal Generator

Directly generate a sine wave using a signal generator and connect it to the input of the LDO. This method is limited by the output current of the signal generator (such as DG4062, whose peak output current is 1.65A under a 100kHz sine wave).

#### Operational Amplifier

The amplifier is used to superimpose AC ripple on the DC voltage of the power supply.

The selection of the operational amplifier needs to meet several basic conditions:

1. The bandwidth of the operational amplifier meets the testing range of the LDO.
2. The maximum output current of the operational amplifier is not less than the maximum output current of the LDO.
3. The output voltage range of the operational amplifier covers the input voltage range of the LDO.

An adder can be designed according to the following schematic:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424101211.png)

Where R1 is equal to R2, and the lowest cutoff frequency is determined by C1 and R1, while the highest cutoff frequency is determined by the bandwidth of the operational amplifier.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424104709.png)

#### Signal Generator + Operational Amplifier

Using an operational amplifier as a voltage follower for a signal generator can remove the limitation of insufficient driving current from the signal generator.

#### LC Node Method

Using inductors and capacitors to superimpose DC and AC voltages as the input to the LDO:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424102617.png)

Where capacitor C1 is used to prevent high pulse interference from VAC on VDC, and inductor L1 prevents VDC from shorting VAC, isolating the two power sources with an LC circuit.

The highest frequency of this circuit is determined by the inductor L1 and capacitor C1, and the lowest frequency is determined by C1.

#### Audio Analyzer (Audio Precision)

The audio analyzer itself does not have the ability to generate DC voltage and has weak driving capability, so it needs a high-bandwidth, high-current operational amplifier to superimpose the AC ripple it generates onto the DC voltage of the power supply and then connect it to the input of the LDO. However, due to the bandwidth limitation of the audio analyzer, PSRR above 100kHz cannot be measured.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424095319.png)

#### Dedicated Injector

This method requires a dedicated input injector (such as J2120A, bandwidth 10Hz-10MHz, maximum DC voltage of 50V, maximum output current of 5A), which can directly superimpose AC ripple and DC voltage of the power supply, but the input voltage after the injector will be attenuated. Use a network analyzer to measure the input and output voltage ripple values separately:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220421145125.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424095347.png)

### Output Measurement

#### Oscilloscope

A general oscilloscope can measure millivolt-level voltages. When the PSRR of the LDO is not higher than 40-50dB, if the input AC voltage peak-to-peak value is 1V, the peak-to-peak value of the same frequency AC voltage in the LDO output is 3mV~10mV, which can be directly measured with an oscilloscope.

The oscilloscope is not suitable for measuring LDO with high PSRR. If the output ripple is too small, the oscilloscope cannot measure it accurately.

#### Operational Amplifier + Oscilloscope

When the PSRR of the LDO is greater than 50dB, since the amplitude of the output ripple is usually less than 1mV, it cannot be directly measured using an oscilloscope. At this time, an operational amplifier can be used to amplify the AC voltage of the LDO output by 100 times or even higher. When designing the operational amplifier circuit, the following should be considered:

- The LDO output has a DC voltage, and the circuit needs to remove the DC voltage.
- The noise generated by the amplification circuit itself should be much smaller than the amplified AC voltage.
- The input offset voltage of the operational amplifier cannot be too large, otherwise a large DC voltage will be output after the amplification circuit is amplified.
- The bandwidth of the amplification circuit needs to meet the PSRR measurement frequency range of the LDO.

Design of the amplification circuit:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424103037.png)

The lowest cutoff frequency of this circuit is determined by C1 and R1, and the highest cutoff frequency is determined by the bandwidth of the operational amplifier.

#### Spectrum Analyzer / Network Analyzer

The spectrum analyzer can measure microvolt-level voltage signals and can be used with a high-impedance input probe to measure the AC voltage of the LDO output. If there is no high-impedance probe, an operational amplifier can be used to build one:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424103409.png)

## Measurement Precautions

1. When testing, the AC voltage waveform at the input of the LDO should be observed first using an oscilloscope to ensure it is normal.
2. It is best to add the corresponding decoupling capacitor to the LDO circuit according to the data sheet, but when using the operational amplifier method for testing, the input capacitor of the LDO should be removed to avoid instability of the operational amplifier.
3. If an injector is used and the output voltage is attenuated, the voltage needs to be appropriately increased.
4. Do not use an electronic load for the output load of the LDO, it is recommended to use a power resistor.
5. Use a grounded spring probe for the output to reduce noise, as shown below.

## References and Acknowledgements

- [Reducing high-speed signal chain power supply issues](https://e2e.ti.com/blogs_/b/powerhouse/posts/reducing-high-speed-signal-chain-power-supply-issues)
- [LDO Basics: Power Supply Rejection Ratio (PSRR)](https://e2echina.ti.com/blogs_/b/analogwire/posts/ldo)
- [LDO PSRR Measurement Simplified](https://www.ti.com/lit/an/slaa414a/slaa414a.pdf?ts=1650484764171&ref_url=https%253A%252F%252Fwww.google.com%252F)
- [LDO PSRR Measurement](http://www.3peakic.com.cn/Public/Uploads/files/LDO%E7%9A%84PSRR%E6%B5%8B%E9%87%8F.pdf)
- [LDO PSRR Measurement · Electronic Study Society](https://zhuanlan.zhihu.com/p/35112931)
- [Power Supply Rejection Ratio (PSRR) Measurement](https://www.rohde-schwarz.com.cn/applications/-psrr-application-card_56279-601516.html)
- [Some Things About DC-DC Transient Testing 🚧](http://www.oliverkung.top/%e5%85%b3%e4%ba%8edc-dc%e7%9e%ac%e6%80%81%e6%b5%8b%e8%af%95%e7%9a%84%e4%b8%80%e4%ba%9b%e4%b8%9c%e8%a5%bf/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
