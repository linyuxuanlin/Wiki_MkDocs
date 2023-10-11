# EMC Design Guide

Electromagnetic Compatibility (EMC) refers to the ability of equipment to function properly in its electromagnetic environment without causing unacceptable electromagnetic interference to anything in the environment. In simple terms, it means that your board is not susceptible to interference and does not interfere with others, achieving a "compatible" state.

EMC includes Electromagnetic Interference (EMI) and Electromagnetic Susceptibility (EMS).

EMI has the following elements:

- Radiated Emission (RE): The interference source couples (interferes) its signal to another electrical network through space.
- Conducted Emission (CE): The interference source couples (interferes) its signal to another electrical network through a conductive medium.
- Harmonics: Harmonic current disturbance testing.
- Flicker: Voltage variation and flicker testing.

EMS has the following elements:

- Radiated Susceptibility (RS): Radio frequency electromagnetic field radiation susceptibility testing.
- Conducted Susceptibility (CS): Radio frequency field-induced conducted interference susceptibility testing (high current injection).
- Electrostatic Discharge (ESD): Electrostatic susceptibility testing (electrostatic discharge experiment).
- Electrical Fast Transient (EFT): Resistance to rapid transient pulse group testing.
- Voltage Dip (DIP): Short interruption and voltage variation resistance testing.
- Surge and Lightning (SURGE): Surge (lightning) resistance testing.
- Power Frequency Magnetic Field (PFMF): Power frequency magnetic field resistance testing.

## Basic Methods for EMC Optimization

The elements that cause EMC problems are electromagnetic interference sources, coupling paths, and sensitive equipment.

Rules:

1. The larger the area of the high-frequency current loop S, the more serious the EMI radiation.
2. The higher the frequency f of the loop current, the more serious the EMI radiation, and the electromagnetic radiation field strength increases proportionally with the square of the current frequency f.

Basic response methods:

- Suppression of transmission channels: Specific methods include filtering, shielding, grounding, overlapping, and reasonable wiring.
- Spatial separation: Increasing the distance between the source of interference and sensitive circuits is an effective method to suppress spatial radiation interference and induced coupling interference.
- Time separation: Useful signals are briefly turned off when interference signals are emitted, and transmitted during the time when interference signals stop.
- Spectrum processing: Spectrum change, spread spectrum technology.
- Electrical isolation: Opto-isolation, relay isolation, transformer isolation, DC/DC conversion.

### Minimize the area of high-frequency lines and power loops

Basic principles:

1. Signals always return to the source end.
2. Signal return flow always follows the path of minimum impedance.

In high-frequency signals, the signal return path is usually the path of minimum inductance, which is also usually the path of minimum loop area. In low frequencies (usually KHz frequency and below), the signal return flow often follows the path of minimum resistance.

### Keep the signal return screen as intact as possible

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215190631.png)

As shown in the figure, if the signal return plane is cut, the signal current will not be able to return to the source through the optimized (shortest) path, and when looking for alternative return paths, it will become unpredictable and increase the signal loop area.

In special cases, digital ground and analog ground need to be isolated to prevent crosstalk.

### Keep high-speed signals away from connectors

Cables connected to the PCB through connectors are efficient antennas, and high-speed signals are prone to generate potential differences, which will drive current to the connected cables, causing radiation to exceed the standard.

### Suppress the rise and fall time of high-speed signals

Slowing down the rise and fall time of digital signals can effectively control high-order harmonic frequencies. Too long conversion time can lead to signal integrity and overheating problems.

## EMC components

Common EMC components include common mode inductors, ferrite beads, and filtering capacitors.

Common filter models:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211219173751.png)

### Common mode inductor

Equivalent model of common mode inductor:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211219173856.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211219174546.png)

### Magnetic Beads

For the introduction and selection of magnetic beads, please refer to the [**Basic Components - Inductors and Magnetic Beads · Magnetic Beads**](https://wiki-power.com/en/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E7%94%B5%E6%84%9F%E4%B8%8E%E7%A3%81%E7%8F%A0#%E7%A3%81%E7%8F%A0) section.

### Filter Capacitors

For the introduction and selection of capacitors, please refer to the [**Basic Components - Capacitors**](https://wiki-power.com/en/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E7%94%B5%E5%AE%B9) section.

## EMC Design for PCB 🚧

### 3W and 20H Principles

The 3W principle means that if the center distance between lines is not less than 3 times the line width, 70% of the inter-line electric field can be kept from interfering with each other. To achieve 98% interference-free electric field, use the 10W rule.

The 20H principle means that the edge of the power plane should be at least shrunk by an amount equivalent to 20 times the distance between the two planes compared to the edge of the ground plane, in order to suppress edge radiation effects and limit 70% of the electric field within the grounding edge. Shrinking by 100H can limit 98% of the electric field inside.

## References and Acknowledgments

- [Introduction to Electromagnetic Compatibility](https://blog.infonet.io/2021/04/04/%E7%94%B5%E7%A3%81%E5%85%BC%E5%AE%B9%E4%BB%8B%E7%BB%8D/)
- [Electromagnetic Compatibility (EMC): A Simple and Rough Guide to EMC Design](https://zhuanlan.zhihu.com/p/142866381)
- [EMI/EMC Design Cheat Sheet - Essential Handbook for Electronic Product Design Engineers](https://www.mr-wu.cn/emc-emi-she-ji-mi-ji/)
- [Using Hybrid Common Mode Inductors to Suppress Conducted EMI](https://www.richtek.com/Design%20Support/Technical%20Document/AN008?sc_lang=zh-CN)
- [[Circuit] EMC Basic Concepts - Common Mode and Differential Mode Interference](https://zhenhuizhang.tk/post/dian-lu-emc-ji-chu-gai-nian-_-gong-mo-chai-mo-gan-rao/)

Sorry, there is no Chinese article provided for translation. Please provide the article for translation.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
