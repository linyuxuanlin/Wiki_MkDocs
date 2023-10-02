# RF - Resonant Circuit - Load Q Value 🚧

We define the Q value of a resonant circuit as the ratio of its center frequency to its 3dB attenuation bandwidth, also known as the load Q value, because it describes the passband characteristics of the resonant circuit under actual circuit or load conditions. The load Q of a resonant circuit depends on three main factors:

- Source impedance $R_s$
- Load resistance $R_L$
- Q value of the components mentioned in the previous chapter

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220418111129.png)

## The Influence of $R_s$ and $R_L$ on Load Q

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220418111200.png)

The influence of source impedance and load impedance on the load Q of a resonant circuit is shown in the above figure. The original curve (dashed line) is the resonance curve of a circuit composed of a 50Ω source impedance, a lossless inductor of 0.05uH, and a lossless capacitor of 25pF. Its Q value is calculated by the formula $Q=\frac{f_e}{f_2-f_1}$ mentioned above, which is about 1.1, indicating that this is not a very narrowband or high Q value design.

By changing the source impedance to 1000Ω and plotting a new resonance curve (solid line), the Q value of the resonant circuit increases significantly to 22.4. By increasing the source impedance, we increase the Q value of the resonant circuit.

The above method cannot show the influence of load impedance on the resonance curve. If we connect an external load to the resonant circuit like this:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220419163311.png)

It can be equivalent to:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220419163441.png)

At this time, the load Q can be expressed as:

$$
Q=\frac{R_p}{X_p}
$$

where $R_p$ is the equivalent total parallel resistance and $X_p$ represents capacitive reactance/inductive reactance (they are equal at resonance).

> e.g. If we want to design a resonant circuit to operate under the conditions of a 150Ω source impedance and a 1000Ω load impedance. At a resonant frequency of 50 MHz, the load Q must be 20. Assuming lossless components and no impedance matching, we can obtain $R_p=130Ω$. According to the above formula, $X_p=\frac{R_p}{Q}=\frac{130}{20} =6.5Ω$, and since $X_p=\omega L=\frac{1}{\omega C}$, we can choose a 20.7nH inductor and a 489.7pF capacitor.

It can be seen that reducing $R_p$ will reduce the Q value of the resonant circuit, and if $R_p$ remains unchanged and $X_p$ is changed, the same effect can be achieved. Therefore, for a given source impedance and load impedance, the resonant circuit can achieve the best Q value when the inductor is a small value and the capacitor is a large value. In either case, $X_p$ will decrease. For example:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220419165555.png)

Therefore, both of these methods can be used to adjust the Q value:

1. Choose the optimal values of source impedance and load impedance.
2. Choose the optimal component values of L and C to optimize Q.

But usually we can only use the second method, because in many cases, the source and load are fixed and cannot be changed. In this case, $X_p$ is defined by a given Q value, but the calculated value usually does not have a suitable physical value to match it, and a solution will be given in the following section.

## The Influence of Component Q Value on Load Q Value

In the previous section, we assumed that the components used in the resonant circuit were lossless, and the Q value of the components did not affect the load Q value. However, in non-ideal situations, we must consider the Q value of individual components.

In a lossless resonant circuit, the impedance at the circuit terminal during resonance is infinite. However, in an actual circuit, due to component losses, there will be some equivalent parallel resistance:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220419174200.png)

Resistance (Rp) and its related parallel reactance (Xp) can be obtained from 

## References and Acknowledgments

- "RF-Circuit-Design (second-edition)_Chris-Bowick" 

> Original: <https://wiki-power.com/> 
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.