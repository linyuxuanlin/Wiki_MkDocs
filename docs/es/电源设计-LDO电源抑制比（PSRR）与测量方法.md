# Diseño de Fuentes de Alimentación - Relación de Rechazo de la Fuente de Alimentación LDO (PSRR) y su Método de Medición

Uno de los beneficios de los reguladores de voltaje lineales de baja caída (LDO) en comparación con las fuentes de alimentación CC-CC es la baja amplitud de las fluctuaciones en su voltaje de salida. Sin embargo, en circuitos de alta velocidad, la Relación de Rechazo de la Fuente de Alimentación (PSRR) de los LDO es un factor que no se puede pasar por alto. A menudo se malinterpreta como un valor estático único. En este artículo, se explicará en detalle qué es la Relación de Rechazo de la Fuente de Alimentación (PSRR) y cómo se mide.

## Definición de la Relación de Rechazo de la Fuente de Alimentación (PSRR)

La Relación de Rechazo de la Fuente de Alimentación (Power Supply Rejection Ratio, PSRR), también conocida como la relación de atenuación de las fluctuaciones, generalmente se encuentra en las hojas de datos de los reguladores LDO. Representa el grado de atenuación desde la entrada hasta la salida de un LDO a una frecuencia particular y denota la capacidad de atenuación de las fluctuaciones a diferentes frecuencias. En algunos circuitos de comunicación de alta velocidad, como Wi-Fi y Bluetooth, es necesario utilizar LDO de alta velocidad con una alta PSRR. Esto permite que el chip responda rápidamente cuando se requiere un aumento instantáneo de corriente, evitando que el voltaje caiga por debajo del valor nominal y cause un reinicio de la carga. En algunos casos, se utiliza una fuente de alimentación CC-CC como un regulador de voltaje de nivel primario y un LDO como un regulador de voltaje y filtro de nivel secundario. Cuando la frecuencia de conmutación de la fuente de alimentación CC-CC se encuentra en el rango de kHz a MHz, es esencial considerar con seriedad la PSRR del LDO si esta frecuencia supera los 100 kHz.

![Imagen](https://media.wiki-power.com/img/20220516174303.png)

La Relación de Rechazo de la Fuente de Alimentación (PSRR) se expresa mediante la siguiente fórmula:

$$
PSRR (dB) = 20 \log \frac{V_{rp (in)}}{V_{rp (out)}}
$$

Donde $V_{rp (in)}$ representa las fluctuaciones de voltaje de entrada y $V_{rp (out)}$ representa las fluctuaciones de voltaje de salida. El PSRR de un LDO de alta velocidad suele ser superior a 60 dB, mientras que el de un LDO común es generalmente de alrededor de 20 dB. Un PSRR de 60 dB significa que cuando las fluctuaciones de voltaje de entrada son de 1 V, las fluctuaciones de voltaje de salida serán de 1 mV.

Comencemos observando la curva de atenuación de las fluctuaciones de un LDO común (Serie XC6206):

![Imagen](https://media.wiki-power.com/img/20220421142140.png)

Podemos ver que a una frecuencia de 1 kHz, el PSRR de XC6206P302 es aproximadamente 23 dB.

Ahora, observemos la curva de atenuación de las fluctuaciones de un LDO de alta velocidad (Serie XC6217x302):

![Imagen](https://media.wiki-power.com/img/20220421141923.png)

A una frecuencia de 1 kHz, el PSRR de XC6217x302 es aproximadamente 68 dB.

## Método de Medición de la Relación de Rechazo de la Fuente de Alimentación (PSRR)

![Imagen](https://media.wiki-power.com/img/20220424104353.png)

La medición de la Relación de Rechazo de la Fuente de Alimentación (PSRR) se divide en dos partes: **inyección en la entrada** y **medición en la salida**. A través de los siguientes métodos de prueba y registrando las fluctuaciones de voltaje en la entrada y la salida, es posible calcular el valor de PSRR mediante la fórmula.

### Inyección en la entrada

#### Generador de señales

Utilice un generador de señales para generar directamente una señal sinusoidal y conéctelo a la entrada del LDO. Este método está limitado por la corriente de salida del generador de señales (por ejemplo, la corriente de salida máxima del DG4062 a una señal sinusoidal de 100 kHz es de 1.65 A).

#### Amplificador operacional

La función de un amplificador operacional es superponer las fluctuaciones de CA en el voltaje de CC de la fuente de alimentación.

La elección del amplificador operacional debe cumplir con varios requisitos básicos:

1. El ancho de banda del amplificador operacional debe estar dentro del rango de prueba del LDO.
2. La corriente de salida máxima del amplificador operacional no debe ser menor que la corriente de salida máxima del LDO.
3. El rango de voltaje de salida del amplificador operacional debe abarcar el rango de voltaje de entrada del LDO.

Puede diseñar un sumador de acuerdo con el siguiente esquema:

![Imagen](https://media.wiki-power.com/img/20220424101211.png)

Donde R1 y R2 son iguales, la frecuencia de corte más baja está determinada por C1 y R1 en conjunto, y la frecuencia de corte más alta está determinada por el ancho de banda del amplificador operacional.

![Imagen](https://media.wiki-power.com/img/20220424104709.png)

#### Generador de señales + Amplificador operacional

Utilice un amplificador operacional como un seguidor de voltaje del generador de señales para eliminar las limitaciones de corriente de salida del generador de señales.

#### Método del nodo LC

Utilice inductores y condensadores para combinar las fluctuaciones de voltaje de CC y CA, y aplíquelas juntas a la entrada del LDO.

Aquí tienes la traducción del texto:

```markdown
![](https://media.wiki-power.com/img/20220424102617.png)

En este circuito, el condensador C1 se utiliza para evitar que VAC genere un alto impacto de pulso en VDC, mientras que la inductancia L1 previene un cortocircuito en VAC cuando se utiliza LC para aislar las dos fuentes de alimentación.

La frecuencia máxima de este circuito está determinada por la inductancia L1 y el condensador C1, y la frecuencia mínima está determinada por C1.

#### Analizador de Audio (Audio Precision)

El analizador de audio en sí no tiene la capacidad de generar voltaje DC continuo y tiene una capacidad de manejo limitada. Por lo tanto, necesita un amplificador operacional de alta velocidad con una corriente significativa para superponer la ondulación AC generada sobre el voltaje DC de la fuente de alimentación continua, y luego conectarlo a la entrada de LDO. Sin embargo, debido a las limitaciones de ancho de banda del analizador de audio, no se pueden medir PSRR por encima de 100kHz.

![](https://media.wiki-power.com/img/20220424095319.png)

#### Inyector Especializado

Este método requiere el uso de un inyector de entrada especializado, como el J2120A, con un ancho de banda de 10Hz a 10MHz, un voltaje máximo de 50V de corriente continua y una corriente de salida de hasta 5A. Este inyector puede superponer directamente la ondulación AC y el voltaje DC de la fuente de alimentación continua, pero el voltaje de entrada después del inyector sufrirá una cierta atenuación. Se pueden medir los valores de la ondulación del voltaje de entrada y salida con un analizador de red.

![](https://media.wiki-power.com/img/20220421145125.png)
![](https://media.wiki-power.com/img/20220424095347.png)

### Medición de Salida

#### Osciloscopio

Un osciloscopio convencional puede medir voltajes en milivoltios. Cuando el PSRR del LDO es inferior a 40-50dB y el voltaje pico a pico de la señal de entrada AC es de 1V, el voltaje pico a pico de la señal AC a la salida del LDO oscilará entre 3mV y 10mV y se puede medir directamente con un osciloscopio.

Los osciloscopios no son adecuados para medir LDO con alto PSRR. Si la ondulación de salida es demasiado pequeña, el osciloscopio no podrá medirla con precisión.

#### Amplificador Operacional + Osciloscopio

Cuando el PSRR del LDO es superior a 50dB, la ondulación de salida generalmente es menor de 1mV y no se puede medir directamente con un osciloscopio. En este caso, se puede considerar el uso de un amplificador operacional para amplificar la señal AC de salida del LDO en 100 veces o más. Al diseñar el circuito del amplificador operacional, se deben tener en cuenta los siguientes aspectos:

- El voltaje DC de salida del LDO debe ser eliminado por el circuito.
- El ruido generado por el circuito de amplificación debe ser mucho menor que la señal AC amplificada.
- La desviación de voltaje de entrada del amplificador operacional no debe ser demasiado grande, de lo contrario, generará un voltaje DC considerable después de la amplificación.
- El ancho de banda del circuito de amplificación debe estar dentro del rango de frecuencia de medición del PSRR del LDO.

Diseño del circuito de amplificación:

![](https://media.wiki-power.com/img/20220424103037.png)

La frecuencia de corte más baja de este circuito está determinada por C1 y R1, y la frecuencia de corte más alta está determinada por el ancho de banda del amplificador operacional.

#### Analizador de Espectro / Analizador de Red

Un analizador de espectro puede medir señales de voltaje en microvoltios y se puede utilizar con sondas de alta impedancia para medir la señal AC de salida del LDO. Si no se dispone de sondas de alta impedancia, se puede utilizar un amplificador operacional:

![](https://media.wiki-power.com/img/20220424103409.png)

## Consideraciones de Medición

1. Al realizar pruebas, primero observe la forma de onda del voltaje AC en la entrada del LDO con un osciloscopio.
2. Es recomendable seguir las especificaciones del manual y agregar los capacitores de desacople correspondientes al circuito del LDO. Sin embargo, al realizar pruebas con un amplificador operacional, se deben quitar los capacitores de entrada del LDO para evitar problemas de estabilidad del amplificador operacional.
3. Si se utiliza un inyector, y el voltaje de salida se atenúa, es necesario aumentar adecuadamente el voltaje.
4. No se recomienda utilizar una carga electrónica para la carga del LDO; se sugiere utilizar resistencias de carga.
5. Utilice una sonda de resorte de tierra en la salida para reducir el ruido, como se muestra en la imagen siguiente:

![](https://media.wiki-power.com/img/20220424104154.png)

## Referencias y Agradecimientos
```

Espero que esta traducción sea de ayuda. Si tienes alguna pregunta adicional o necesitas más traducciones, no dudes en preguntar.

- [Reduciendo problemas en la fuente de alimentación de la cadena de señal de alta velocidad](https://e2e.ti.com/blogs_/b/powerhouse/posts/reducing-high-speed-signal-chain-power-supply-issues)
- [Conceptos fundamentales de LDO: Relación de rechazo de la fuente de alimentación](https://e2echina.ti.com/blogs_/b/analogwire/posts/ldo)
- [Simplificación de la medición de PSRR en LDO](https://www.ti.com/lit/an/slaa414a/slaa414a.pdf?ts=1650484764171&ref_url=https%253A%252F%252Fwww.google.com%252F)
- [Medición de PSRR en LDO](http://www.3peakic.com.cn/Public/Uploads/files/LDO%E7%9A%84PSRR%E6%B5%8B%E9%87%8F.pdf)
- [Medición de PSRR en LDO · Comunidad de estudio electrónico](https://zhuanlan.zhihu.com/p/35112931)
- [Medición de la Relación de Rechazo de la Fuente de Alimentación (PSRR)](https://www.rohde-schwarz.com.cn/applications/-psrr-application-card_56279-601516.html)
- [Algunas notas sobre pruebas transitorias de DC-DC 🚧](http://www.oliverkung.top/%e5%85%b3%e4%ba%8edc-dc%e7%9e%ac%e6%80%81%e6%b5%8b%e8%af%95%e7%9a%84%e4%b8%80%e4%ba%9b%e4%b8%9c%e8%a5%bf/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
