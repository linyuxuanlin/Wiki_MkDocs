---
id: Basics_of_Fourier_Transform
title: Basics of Fourier Transform 🚧
---

There are several algorithms for transforming data from the time domain to the frequency domain as below.

## Fourier Series

A **Fourier Series**（傅里叶级数） is summarized as creating a complex waveform by summing pure sine waves with different amplitudes and frequencies, and to decompose a complex signal into a sum of sinusoids of different amplitudes and frequencies.

### Dirichlet Conditions

Dirichlet Conditions specify a set of conditions that must be met before a signal can be decomposed into a Fourier Series:

- The signal is a mathematical function, i.e., one and only one y-point corresponds to each x-point.
- The signal is periodic.
- The area bounded by the signal over one period is finite.

### Decompose into a Fourier Series

A complex signal that meets the Dirichlet Conditions can be represented by a sum of sinusoids:

$$
f(t)=a_0+A\{\sum_{n=1}^\infin[a_n cos(n \omega_1 t+\phi_n)+b_n sin(n \omega_1 t+\phi_n)]\}
$$

where:

- $a_0$ is the DC component.
- $A$ is an overall scale factor for all harmonic components.
- $\omega_1$ is the frequency of the fundamental.
- $n$ is an integer multiplier of the fundamental frequency for each harmonic term.

This proves that not only can we sum a series of sine and cosine waves to create any other wave, but also that the frequencies of the sinusoids are integer multiples (harmonics) of a single fundamental frequency.

## Discrete Fourier Transform (DFT)

**Discrete Fourier Transform (DFT)**: takes amplitude versus time data, and then translates to amplitude versus frequency data.

Mathematically, the algorithm is a series summation of the product of each sample times a complex number:

$$
X(b)=\sum_{n=0}^{N-1}x[n](cos(2\pi nb/N)-jsin(2\pi nb/N))
$$

where:

- $n$ is one of $N$ samples.
- $N$ is total number of samples.
- $b$ is one of $B$ frequency bins (each bin represents a frequency range of $F_s /N$).
- $j$ is the imaginary operator.

The DFT algorithm uses each sample point in the summation from 0 to N-1 for each analyzed frequency. All N sample points contain information about all B frequencies, thus each of the B frequencies for which information is desired requires a summation of N time sample products. Because of the reasons above, processing a DFT is slow, because $N^2$ calculations are necessary. For example, a 2000 point DFT requires 4 million calculations, often floating point calculations, which are slower than integer calculations.

## Fast Fourier Transform (FFT)

**Fast Fourier Transform (FFT)** remedies the DFT speed problem by skipping over portions of the summations which produce redundant information. Rules for using FFT:

- The number of sample points must be a power of 2 ($2^n$).
- The number of additions and multiplications is: $\frac{N}{2}\log_2 N$.

## References & Acknowledgements

- *Fundamentals of Testing Using ATE*
- *The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe*

> This article is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
