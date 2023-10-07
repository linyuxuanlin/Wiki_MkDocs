# RF - S Parameters

S parameters (Scattering parameters, S-Parameters) are used to reflect the characteristics (amplitude/phase) of the reflected/transmitted signals in the frequency domain. It is a complex matrix. We can view the internal circuit as a black box (without considering internal circuit elements) and measure its port characteristics through S parameters.

## Detailed Explanation of S Parameters

The naming convention of S parameters is that the first digit represents the measured port and the second digit represents the reference port. For example, S21 represents the signal measured at port 2 relative to the signal excitation source at port 1. The form of the S parameter wave can be power, voltage, or current.

![](https://f004.backblazeb2.com/file/wiki-media/img/20220627100338.png)

As shown in the figure above, S11 and S22 represent the reflection coefficient (reflection/input), and S21 and S12 represent the transmission coefficient (transmission/input).

### S11

![](https://f004.backblazeb2.com/file/wiki-media/img/20220621000000.gif)

S11 refers to the reflection signal at port 1 relative to the incident signal at port 1, and is calculated as $S11=\frac{S_{Reflection}}{S_{Incident}}$.

### S21

![](https://f004.backblazeb2.com/file/wiki-media/img/20220621000001.gif)

S21 refers to the transmission signal at port 2 relative to the incident signal at port 1, and is calculated as $S21=\frac{S_{Transmission}}{S_{Incident}}$.

### S12

![](https://f004.backblazeb2.com/file/wiki-media/img/20220621000002.gif)

S12 refers to the transmission signal at port 1 relative to the incident signal at port 2, and is calculated as $S12=\frac{S_{Transmission}}{S_{Incident}}$.

### S22

![](https://f004.backblazeb2.com/file/wiki-media/img/20220621000003.gif)

S22 refers to the reflection signal at port 2 relative to the incident signal at port 2, and is calculated as $S22=\frac{S_{Reflection}}{S_{Incident}}$.

## References and Acknowledgments

- [The Meaning of S Parameters and Vector Network Analyzer Measurement Methods](http://jietaipu.com/resource/88.html)
- "S-Parameter Measurements Basics for High Speed Digital"

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.