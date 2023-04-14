---
id: CPR-Fundamental
title: CPR - Fundamental
---

**CPR** represents of **Core Power Reduction**, an **adaptive power management technology** that determine the optimal product voltage, allow closed loop compensation of DC voltage, temperature variation, process（制程） and aging degradation（老化退化）, to optimize device power and performance,

CPR core consists of one controller, and a number of sensors embedded into the SoC, to control the VDD level of a chip. The sensors consists of multiple ring oscillators, to estimate the running speed of the chip. Then the controller provide a VDD modification command result to the PMIC, which can be programmed with software.
