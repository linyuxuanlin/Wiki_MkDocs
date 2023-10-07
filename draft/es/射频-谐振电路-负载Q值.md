# Radiofrecuencia - Circuito resonante - Factor Q de carga 🚧

Definimos el factor Q de un circuito resonante como la relación entre la frecuencia central y la banda de atenuación de 3dB, también conocido como factor Q de carga, ya que describe las características de paso del circuito resonante en condiciones de carga o dentro del circuito real. El factor Q de carga de un circuito resonante depende de tres factores principales:

- Impedancia de fuente $R_s$
- Resistencia de carga $R_L$
- Factor Q de los componentes mencionados en el capítulo anterior

![](https://f004.backblazeb2.com/file/wiki-media/img/20220418111129.png)

## Influencia de $R_s$ y $R_L$ en el factor Q de carga

![](https://f004.backblazeb2.com/file/wiki-media/img/20220418111200.png)

La influencia de la impedancia de fuente y la resistencia de carga en el factor Q de carga del circuito resonante se muestra en la figura anterior. La curva original (línea punteada) es la curva de resonancia del circuito compuesto por una impedancia de fuente de 50Ω, un inductor sin pérdidas de 0.05uH y un capacitor sin pérdidas de 25pF, cuyo factor Q se calcula con la fórmula mencionada anteriormente, siendo aproximadamente 1.1, lo que no es un diseño de banda estrecha o alto factor Q.

Al cambiar la impedancia de fuente a 1000Ω, se traza una nueva curva de resonancia (línea sólida) y el factor Q del circuito resonante aumenta significativamente a 22.4. Al aumentar la impedancia de fuente, aumentamos el factor Q del circuito resonante.

El método anterior no muestra la influencia de la resistencia de carga en la curva de resonancia. Si conectamos una carga externa al circuito resonante de esta manera:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220419163311.png)

Puede ser equivalente a:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220419163441.png)

En este caso, el factor Q de carga se puede expresar como:

$$
Q=\frac{R_p}{X_p}
$$

Donde $R_p$ es la resistencia total equivalente en paralelo y $X_p$ representa la reactancia capacitiva / inductiva (son iguales en resonancia).

> Por ejemplo, si queremos diseñar un circuito resonante para que funcione con una impedancia de fuente de 150Ω y una resistencia de carga de 1000Ω. A una frecuencia de resonancia de 50 MHz, el factor Q de carga debe ser de 20. Suponiendo que los componentes son sin pérdidas y no hay coincidencia de impedancia, podemos obtener $R_p=130Ω$. Según la fórmula anterior, $X_p=\frac{R_p}{Q}=\frac{130}{20} =6.5Ω$, y como $X_p=\omega L=\frac{1}{\omega C}$, podemos elegir un inductor de 20.7nH y un capacitor de 489.7pF.

Se puede ver que la disminución de $R_p$ disminuirá el factor Q del circuito resonante y, si $R_p$ permanece constante y se cambia $X_p$, se puede lograr el mismo efecto. Por lo tanto, para una impedancia de fuente y una resistencia de carga dadas, se puede obtener el mejor factor Q del circuito resonante cuando el inductor es de valor pequeño y el capacitor es de valor grande. En cualquier caso, $X_p$ disminuirá. Por ejemplo:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220419165555.png)

Por lo tanto, se pueden utilizar ambos métodos para ajustar el factor Q:

1. Seleccione los valores óptimos de impedancia de fuente y resistencia de carga.
2. Seleccione los valores óptimos de los componentes L y C para optimizar el factor Q.

Pero generalmente solo podemos usar el segundo método, ya que en muchos casos, la fuente y la carga están fijas y no se pueden cambiar. En este caso, $X_p$ está definido por un valor Q dado, pero el valor calculado generalmente no tiene un valor físico adecuado para emparejarlo, se dará una solución en el siguiente texto.

## Influencia del factor Q de los componentes en el factor Q de carga

En el texto anterior, supusimos que los componentes utilizados en el circuito resonante eran componentes sin pérdidas y que el factor Q de los componentes no afectaría el factor Q de carga. Pero en situaciones no ideales, debemos considerar el factor Q de cada componente.

En un circuito resonante sin pérdidas, la impedancia en los terminales del circuito es infinita en resonancia. Pero en un circuito real, debido a las pérdidas de los componentes, habrá alguna resistencia en paralelo equivalente:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220419174200.png)

La resistencia (Rp) y la reactancia en paralelo relacionada (Xp) se pueden obtener de 

## Referencias y agradecimientos

- "RF-Circuit-Design (segunda edición) _Chris-Bowick" 

> Dirección original del artículo: <https://wiki-power.com/> 
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.