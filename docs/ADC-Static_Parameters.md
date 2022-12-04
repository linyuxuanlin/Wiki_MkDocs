---
id: ADC-Static_Parameters
title: ADC - Static Parameters
---

Analog to Digital Converter (ADC) is a device to converts analog signals into a sequence of digital data.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011141438.png)

Though ADC's ideal transfer function should be a straight line, but actually is a uniform staircase, that the number of steps corresponds to the number of digital output codes. Since analog is continuous and digital is discrete, quantization error will be introduced in the procedure.

## Static Parameters

ADC's static parameters mainly contain:

- LSB Size
- Full Scale Range (FSR)
- Offset Error
- Gain Error
- Differential Non-Linearity Error (DNE or DNL)
- Integral Non-Linearity Error (INE or INL)

### LSB Size

The width of one step is defined as 1 **Least Significant Bit (LSB)**. The resolution of an ADC is normally expressed as number of bits (digital output code). An ADC with an n-bit resolution has $2^n$ possible digital codes ($2^n$ step levels).

$$
LSB=\frac{V_{FST}-V_{ZST}}{2^{bits}-2}
$$

For an ideal ADC, LSB represents all of the each code's width.

### Full Scale Range (FSR)

For example, for a 3 bit converter, there are:

- 8 horizontal steps
- 7 transitions
- 6 steps between 7 transitions

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008151344.png)

- **Zero Scale Range Transition Voltage ($V_{ZST}$)**: Voltage of the analog input signal when the first transition is recorded.
- **Full Scale Range Transition Voltage ($V_{FST}$)**: Voltage of the analog input signal when the last transition is recorded.
- **Full Scale Range (FSR)**: Maximum extreme of the analog input signal supplied to the ADC. $FSR = (V_{FST}-V_{ZST}) + 2 LSB$, $V_{FSR(refer to VZS)} = (V_{FST}-0.5LSB)-(V_{ZST}-0.5LSB) + 2 LSB$

### Offset Error

**Offset Error** (Zero-Scale Error) is the difference between ideal and actual offset (initial) points. It is measured from the midpoint of the zero step (ideal to actual) for the ADC.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008154521.png)

Where

$$
V_{ZS}=V_{ZST}-0.5LSB
$$

### Gain Error

**Gain Error** is the difference between ideal and actual gain points on the transfer function (after the offset error has been corrected to zero). It is measured from the midpoint of the full step for the ADC.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008155259.png)

Where

$$
V_{FS}=V_{FST}-0.5LSB+2LSB
$$

### Differential Non-Linearity Error (DNL)

**Differential Non-Linearity Error (DNL)** is the difference between an actual step width and an ideal step width (1 LSB). It's a measure of "small-signal" linearity error, and is measured from the difference in the analog input voltage between 2 adjacent transitions and the device's average LSB.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008160020.png)

Equations to describe DNL:

$$
DNL[n]=CodeWidth_n-LSB_{average}
$$

$$
DNL=(V_{in2}-V_{in1})-LSB_{average}
$$

another image to decribe DNL:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008161707.png)

If DNL exceeds is too large, one or more codes will be missing and never receive an output.

### Integral Non-Linearity Error (INL)

**Integral Non-Linearity Error (INL)** is the cumulative effect at any given input of all differential non-linearity values. It is a measure of "large-signal" linearity error. INL at any point along the curve is the deviation of the ideal linearity line.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008163705.png)

The deviations are measured at the transition points from one step to the next for the ADC. INL is the deviation of the values of the actual step function to the ideal straight line function.

Equations to describe INL:

$$
INL[n]=INL_{n-1}+{\frac{DNL_{n-1}+DNL_{n}}{2}}
$$

$$
INL=[(\frac{BinaryCode}{2^{bits}-1})(V_{FS}-V_{ZS})+V_{offset}]-CodeCentor
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008163911.png)

## How to Test Static Parameters

### Test System Setup

Test system setup for ADC static parameter tests:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008184721.png)

Since the ADC voltage-to-code transfer curve is a many-to-one mapping function:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008185819.png)

We use linear ramp histogram method (code width measurement) practically. The input ramp is slow enough to give a statistically relevant "number of hits per code".

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008190154.png)

Block diagram of signal setup:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008190612.png)

### Tests Concept

Procedure of testing the static parameters of an ADC DUT is listed below.

#### 1. Make a ramp wave segment for AC SRC

The input ramps goes above and below ±Fs to assure that all codes are covered:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008193036.png)

#### 2. Take data between the start (min+1, e.g. 0…01) and the end (max-1, e.g. 1…10) of the ramp. That gives $2^n – 2$ codes' worth of data

Voltage applied must be wider than the full-scale range to cover all transitions. 16 steps in-between each code transition is shown below:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008194207.png)

for the ideal ADC DUT, 16 output codes are appear in the same times:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008194450.png)

However, a real device will have a count more than 16 times for wider codes, and less than 16 times for narrower ones (But sum of the total occurrence should be still $2^{bits}$ times of 16):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008194813.png)

#### 3. Calculate for DNL for each step

$$
DNL[i]=\frac{Hits[i]-\frac{\sum Hits[i]}{2^n-2}}{\frac{\sum Hits[i]}{2^n-2}}
$$

Where $Hits[i]$ represents the Actual Output Code Count, and $\frac{\sum Hits[i]}{2^n-2}$ represents the Ideal Output Code Count.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008234157.png)

For an example historam graph as shown below:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008234921.png)

for DNL[1](Code 001),

- Actual Output Code Count = 14
- Idea Output Code Count = (14 +18 +15 + 17+ 17 + 15) / (8 -2 ) = 16.

Therefore DNL[1] (Code 001) = (14-16)/16 \* LSB => -0.125 \* LSB.

#### 4. Get the max and min DNL

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221008235342.png)

#### 5. Calculate for INL for each step

INL is the cumulative value of the first DNL to the DNL[i] (except zero and full scale DNL):

$$
INL[i]=DNL[i]+DNL[i-1]+...+DNL[2]+DNL[1]
$$

Note that $DNL[0]$ is not used,

$$
INL[0]=INL[FullScale]=0
$$

For an example graph below,

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009201547.png)

$$
INL[1] = DNL[1] = -0.125 * LSB
$$

$$
INL[2] = DNL[2] + DNL[1] = 0 * LSB
$$

$$
INL[3] = DNL[3] + DNL[2] + DNL[1] \\
INL[3]= 0.0625 * LSB
$$

#### 6. Get the max and min INL

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009201838.png)

## References & Acknowledgements

- *Fundamentals of Testing Using ATE*
- *The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe*

> This article is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
