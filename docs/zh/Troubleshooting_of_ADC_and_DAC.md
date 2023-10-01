---
id: Troubleshooting_of_ADC_and_DAC
title: Troubleshooting of ADC and DAC
---


## Why AC Source should be 2-4 bits more resolution than the ADC under test?

As an often used definition of ENOB:

$$
ENOB=\frac{SINAD-1.76}{6.02}
$$

So if the ENOB of DAC (in AC Source) get lower, the SINAD will become lower too, means that the noise and distortions will increase relatively, which will affect the accuracy of measurement.

Another point is, the resolution of AC Source lower than 2-4 bits will induce higher harmonic distortions, the digital signal at the output of the ADC is deteriorated by both DAC's and ADC's harmonic distortions, and the amplitude of 2nd-harmonic (for an example) could be summed. Cause AC Source with higher resolution will bring lower harmonic distortions, the test output results will become more accurate.

Refer to this article: [ADC Production Test Technique Using Low-Resolution Arbitrary Waveform Generator](https://www.hindawi.com/journals/vlsi/2008/482159/)

## Are there other ways to improve measurement accuracy with the AC input in the test of ADC?

Reducing the slope of the input ramp wave can improve measurement accuracy.

## What to do with high base noise in the test of ADC?

1. Increase the number of samples (N) and the number of test signal periods sampled (M), both will also result in more test time.
2. Increase sampling frequency (Fs).

It's not possible to distinguish between noise and harmonics if only sample only 1 period of signal.

> 有这条公式吗？噪声精度=采样频率/M

## How to measure the gain error of ADC practically?

Histogram method is used practically to measure the gain error, because the theoretical transition edge is hard to detect.

## Do we need an AC Digitizer with 2-4 bits more resolution in the test of the DAC?

No, it's no necessary for a very high resolution AC Digitizer. AC Digitizer that satisfied Nyquist resolution will meet the test standard.
