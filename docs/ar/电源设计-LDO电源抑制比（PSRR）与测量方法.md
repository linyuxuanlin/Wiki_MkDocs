# Diseño de fuentes de alimentación - Relación de rechazo de fuente de alimentación (PSRR) y métodos de medición de LDO

Una de las ventajas de los reguladores lineales de baja caída de voltaje (LDO) en comparación con los convertidores DC-DC es que tienen una pequeña ondulación de voltaje de salida. Sin embargo, en circuitos de alta velocidad, la relación de rechazo de fuente de alimentación (PSRR) de LDO también es un factor importante que no se puede ignorar. A menudo se confunde con un valor estático único, este artículo explicará en detalle la relación de rechazo de fuente de alimentación (PSRR) y cómo medirla.

## Definición de la relación de rechazo de fuente de alimentación (PSRR)

La relación de rechazo de fuente de alimentación (Power Supply Rejection Ratio, PSRR), también conocida como relación de rechazo de ondulación, se puede encontrar en el manual de datos de LDO. Representa la atenuación de LDO desde la entrada hasta la salida a una determinada frecuencia y representa la capacidad de supresión de ondulación a diferentes frecuencias. En algunos circuitos de comunicación de alta velocidad, como Wi-Fi, Bluetooth, etc., se requieren LDO de alta velocidad con una gran relación de rechazo de fuente de alimentación para responder rápidamente cuando el chip necesita aumentar la corriente instantáneamente, evitando que la carga se reinicie debido a una caída de voltaje por debajo del voltaje nominal. En algunos casos, se utiliza un convertidor DC-DC como reductor de voltaje de primer nivel y LDO como reductor de voltaje / filtro de segundo nivel, ya que la frecuencia de conmutación del convertidor DC-DC está en el rango de kHz-MHz, es decir, por encima de 100 kHz para LDO, por lo que es necesario considerar estrictamente la PSRR.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220516174303.png)

La relación de rechazo de fuente de alimentación (PSRR) se expresa mediante la fórmula:

$$
PSRR(dB)=20\log\frac{V_{rp(in)}}{V_{rp(out)}}
$$

Donde $V_{rp(in)}$ representa la ondulación de entrada y $V_{rp(out)}$ representa la ondulación de salida. La PSRR de LDO de alta velocidad generalmente es superior a 60 dB, mientras que la PSRR de LDO común es de alrededor de 20 dB. Una PSRR de 60 dB significa que cuando la ondulación de entrada es de 1 V, la ondulación de salida será de 1 mV.

Primero, veamos la curva de supresión de ondulación del LDO común (serie XC6206):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220421142140.png)

Se puede ver que a una frecuencia de 1 kHz, la relación de rechazo de ondulación de XC6206P302 es de aproximadamente 23 dB.

Ahora, veamos la curva de supresión de ondulación del LDO de alta velocidad (XC6217x302):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220421141923.png)

A una frecuencia de 1 kHz, la relación de rechazo de ondulación de XC6217x302 es de aproximadamente 68 dB.

## Métodos de medición de la relación de rechazo de fuente de alimentación (PSRR)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424104353.png)

La medición de la relación de rechazo de fuente de alimentación (PSRR) se divide en dos partes: la inyección de entrada y la medición de salida. Se puede calcular el valor de PSRR mediante la siguiente prueba y registrando la ondulación de voltaje de entrada y salida según la fórmula.

### Inyección de entrada

#### Generador de señales

Se utiliza un generador de señales para generar directamente una onda sinusoidal y se conecta al terminal de entrada de LDO. Este método está limitado por la corriente de salida del generador de señales (como el pico de corriente de salida de DG4062 a una onda sinusoidal de 100 kHz es de 1,65 A).

#### Amplificador operacional

La función del amplificador operacional es superponer la ondulación de CA en el voltaje de CC de la fuente de alimentación.

La elección del amplificador operacional debe cumplir con varios requisitos básicos:

1. La banda de paso del amplificador operacional cumple con el rango de prueba de LDO.
2. La corriente de salida máxima del amplificador operacional no es menor que la corriente de salida máxima de LDO.
3. El rango de voltaje de salida del amplificador operacional cubre el rango de voltaje de entrada de LDO.

Se puede diseñar un sumador según el siguiente diagrama:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424101211.png)

Donde R1 y R2 son iguales, la frecuencia de corte inferior más baja está determinada por C1 y R1, y la frecuencia de corte superior más alta está determinada por la banda de paso del amplificador operacional.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424104709.png)

#### Generador de señales + amplificador operacional

El uso de un seguidor de voltaje con amplificador operacional como generador de señal puede eliminar las limitaciones de corriente de conducción del generador de señal.

#### Método de nodo LC

Utilizando inductores y capacitores para superponer voltajes de CC y CA, se utilizan juntos como entrada de LDO:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424102617.png)

Donde el capacitor C1 se utiliza para evitar que VAC tenga un alto impacto de pulso en VDC, el inductor L1 evita que VDC cause un cortocircuito en VAC, y se utiliza LC para aislar las dos fuentes de alimentación.

La frecuencia máxima de este circuito está determinada por el inductor L1 y el capacitor C1, y la frecuencia mínima está determinada por C1.

#### Analizador de audio (Audio Precision)

El analizador de audio en sí no tiene la capacidad de generar voltajes de CC y tiene una capacidad de conducción débil, por lo que se necesita un amplificador operacional de alta banda ancha y alta corriente para superponer la ondulación de CA que produce en el voltaje de CC de la fuente de alimentación y luego conectarlo a la entrada de LDO. Pero debido a las limitaciones de ancho de banda del analizador de audio, no se pueden medir PSRR por encima de 100 kHz.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424095319.png)

#### Inyector especial

Este método requiere un inyector de entrada especial (como J2120A, con un ancho de banda de 10 Hz a 10 MHz, un voltaje máximo de CC de 50 V y una corriente de salida máxima de 5 A), que puede superponer directamente la ondulación de CA y el voltaje de CC de la fuente de alimentación, pero la tensión de entrada después del inyector se atenuará. Use un analizador de red para medir los valores de ondulación de voltaje de entrada y salida:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220421145125.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424095347.png)

### Medición de salida

#### Osciloscopio

Un osciloscopio común puede medir voltajes en milivoltios. Cuando el PSRR de LDO no es superior a 40-50 dB, si el voltaje de CA de entrada tiene una amplitud de 1 V, la amplitud de voltaje de CA de la misma frecuencia en la salida de LDO es de 3 mV a 10 mV, lo que se puede medir directamente con un osciloscopio.

El osciloscopio no es adecuado para medir LDO de alta PSRR. Si la ondulación de salida es demasiado pequeña, el osciloscopio no puede medir con precisión.

#### Amplificador operacional + osciloscopio

Cuando el PSRR de LDO es superior a 50 dB, debido a que la amplitud de ondulación de salida generalmente es inferior a 1 mV, no se puede medir directamente con un osciloscopio. En este caso, se puede considerar utilizar un amplificador operacional para amplificar el voltaje de CA de salida de LDO en 100 veces o más. Al diseñar el circuito del amplificador operacional, se deben considerar los siguientes aspectos:

- La salida de LDO tiene un voltaje de CC, por lo que el circuito debe eliminar el voltaje de CC.
- El ruido generado por el circuito de amplificación debe ser mucho menor que el voltaje de CA amplificado.
- El voltaje de desviación de entrada del amplificador operacional no debe ser demasiado grande, de lo contrario, el circuito amplificado producirá un voltaje de CC muy grande.
- La banda ancha del circuito de amplificación debe cumplir con el rango de frecuencia de medición de PSRR de LDO.

Diseño del circuito de amplificación:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424103037.png)

La frecuencia de corte más baja de este circuito está determinada por C1 y R1, y la frecuencia de corte más alta está determinada por la banda ancha del amplificador operacional.

#### Analizador de espectro / analizador de red

El analizador de espectro puede medir señales de voltaje en microvoltios y se puede utilizar con una sonda de entrada de alta impedancia para medir el voltaje de CA de salida de LDO. Si no hay una sonda de alta impedancia, se puede utilizar un amplificador operacional:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424103409.png)

## Precauciones de medición

1. Al realizar pruebas, primero use un osciloscopio para observar si la forma de onda de voltaje de CA en la entrada de LDO es normal.
2. Es mejor agregar capacitores de acoplamiento correspondientes al circuito LDO según el manual de datos, pero al realizar pruebas con amplificadores operacionales, se debe eliminar el capacitor de entrada de LDO para evitar la inestabilidad del amplificador operacional.
3. Si se utiliza un inyector y la tensión de salida se atenúa, la tensión debe aumentarse adecuadamente.
4. No use una carga electrónica para la carga de salida de LDO, se recomienda usar una resistencia de potencia.
5. Use una sonda de tierra para reducir el ruido en la salida, como se muestra en la siguiente figura.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220424104154.png)

## Referencias y Agradecimientos

- [Reduciendo problemas de suministro de energía de cadena de señal de alta velocidad](https://e2e.ti.com/blogs_/b/powerhouse/posts/reducing-high-speed-signal-chain-power-supply-issues)
- [Conocimientos básicos de LDO: Relación de supresión de fuente de alimentación](https://e2echina.ti.com/blogs_/b/analogwire/posts/ldo)
- [Simplificación de la medición de PSRR de LDO](https://www.ti.com/lit/an/slaa414a/slaa414a.pdf?ts=1650484764171&ref_url=https%253A%252F%252Fwww.google.com%252F)
- [Medición de PSRR de LDO](http://www.3peakic.com.cn/Public/Uploads/files/LDO%E7%9A%84PSRR%E6%B5%8B%E9%87%8F.pdf)
- [Medición de PSRR de LDO · Comunidad de Investigación Electrónica](https://zhuanlan.zhihu.com/p/35112931)
- [Medición de la relación de supresión de fuente de alimentación (PSRR)](https://www.rohde-schwarz.com.cn/applications/-psrr-application-card_56279-601516.html)
- [Algo sobre las pruebas transitorias de DC-DC 🚧](http://www.oliverkung.top/%e5%85%b3%e4%ba%8edc-dc%e7%9e%ac%e6%80%81%e6%b5%8b%e8%af%95%e7%9a%84%e4%b8%80%e4%ba%9b%e4%b8%9c%e8%a5%bf/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
