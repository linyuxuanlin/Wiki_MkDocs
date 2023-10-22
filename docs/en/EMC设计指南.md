# EMC Design Guidelines

**Electromagnetic Compatibility (EMC)** refers to a device's ability to operate normally in its electromagnetic environment without causing intolerable electromagnetic interference to anything in that environment. In simpler terms, it means that your board should not be susceptible to interference from others and should also strive not to interfere with others, achieving a "compatible" state.

**Electromagnetic Compatibility (EMC)** includes **Electromagnetic Interference (EMI)** and **Electromagnetic Susceptibility (EMS)**.

EMI includes the following elements:

- **Radiated Emission (RE)**: This refers to interference sources coupling their signals (interference) to another electrical network through space.
- **Conducted Emission (CE)**: This involves coupling the signals on one electrical network to another through conductive media.
- **Harmonics**: Testing for harmonic current interference.
- **Flicker**: Testing for voltage variations and flicker.

EMS includes the following elements:

- **Radiated Susceptibility (RS)**: Testing for susceptibility to radiofrequency electromagnetic field radiation.
- **Conducted Susceptibility (CS)**: Testing for susceptibility to conducted interference induced by radiofrequency fields (high current injection).
- **Electrostatic Discharge (ESD)**: Testing for susceptibility to electrostatic interference (static discharge experiments).
- **Electrical Fast Transient (EFT)**: Testing for resistance to rapid transient pulse group interference.
- **Voltage Dips (DIP)**: Testing for short-term interruptions and voltage variations.
- **Surges and Lightning (SURGE)**: Testing for resistance to surges (lightning) interference.
- **Power Frequency Magnetic Field (PFMF)**: Testing for resistance to power frequency magnetic field interference.

## Basic Methods for EMC Optimization

The factors contributing to EMC issues are electromagnetic interference sources, coupling paths, and sensitive devices.

Key principles:

1. The larger the area of the high-frequency current loop (S), the more severe the radiated emission (EMI).
2. The higher the frequency (f) of the loop current, the more severe the radiated emission (EMI). The electromagnetic radiation field strength increases proportionally with the square of the current frequency (f).

Basic mitigation methods include:

- Suppression of transmission channels: Specific methods include filtering, shielding, grounding, cross-coupling, and proper wiring.
- Spatial separation: Increasing the distance between the source of interference and sensitive circuits effectively suppresses spatial radiation interference and induced coupling interference.
- Temporal separation: Useful signals are momentarily interrupted when interference signals are emitted, and transmission occurs during the periods when interference signals cease.
- Spectrum processing: Altering the spectrum and spreading techniques.
- Electrical isolation: Optoelectronic isolation, relay isolation, transformer isolation, DC/DC conversion.

### Minimizing the Area of High-Frequency Lines and Power Loops

Fundamental principles:

1. Signals always return to the source.
2. Signal return flows through the path with the lowest impedance.

In high-frequency signals, the signal return path is usually the one with the lowest inductance, often corresponding to the smallest loop area. In low frequencies (typically KHz and below), the signal return path usually follows the path of least resistance.

### Maintain Signal Return Plane Integrity

![Image](https://img.wiki-power.com/d/wiki-media/img/20211215190631.png)

As shown in the image, cutting the signal return plane can disrupt the optimal (shortest) path for signal current to return to the source, making it unpredictable and increasing the signal loop area. In special cases, digital and analog grounds need to be isolated to prevent interference.

### Keep High-Speed Signals Away from Connectors

Cables connected to PCBs through connectors act as efficient antennas, and high-speed signals are prone to generating potential differences that drive current into connected cables, causing excessive radiation.

### Suppress High-Speed Signal Rise and Fall Times

Slowing down the rise and fall times of digital signals effectively controls high-order harmonic frequencies. Excessively long transition times can lead to signal integrity and overheating issues.

## EMC Components

Common EMC components include common-mode inductors, ferrite beads, and filtering capacitors.

Common filter models:

![Image](https://img.wiki-power.com/d/wiki-media/img/20211219173751.png)

### Common-Mode Inductors

Equivalent models of common-mode inductors:

![Image](https://img.wiki-power.com/d/wiki-media/img/20211219173856.png)

![Image](https://img.wiki-power.com/d/wiki-media/img/20211219174546.png)

### Ferrite Beads

Introduction and Selection of Ferrite Beads

For information and selection criteria regarding ferrite beads, please refer to the [**Basic Components - Inductors and Ferrite Beads - Ferrite Beads**](https://example.com/ferrite-beads) section.

Filter Capacitors

To learn about capacitors and their selection, please visit the [**Basic Components - Capacitors**](https://example.com/capacitors) section.

EMC Design for PCB 🚧

### The 3W and 20H Principles

The 3W principle states that when the center-to-center distance between lines is not less than 3 times the line width, it can maintain a 70% separation of electric fields without interfering with each other. To achieve a 98% separation of electric fields, the 10W rule is employed.

The 20H principle ensures that the edge of the power plane should be inset by at least 20 times the spacing between two adjacent layers compared to the edge of the ground plane. This is done to suppress edge radiation effects and can confine 70% of the electric field within the ground edge; by setting the inset to 100H, 98% of the electric field can be confined within.

References and Acknowledgments

- [Introduction to Electromagnetic Compatibility](https://example.com/emc-introduction)
- [EMC (Electromagnetic Compatibility): A Practical EMC Design Guide](https://example.com/emc-design-guide)
- [EMI/EMC Design Handbook – A Must-Have Manual for Electronic Product Design Engineers](https://example.com/emc-emi-handbook)
- [Using Hybrid Common Mode Inductors to Suppress Conducted Electromagnetic Interference](https://example.com/hybrid-inductors)
- [EMC Basics - Common Mode and Differential Mode Interference](https://example.com/emc-basics)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.