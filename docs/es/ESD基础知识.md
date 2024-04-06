# Conocimientos Fundamentales sobre ESD

ESD (Descarga Electroestática) se refiere a un fenómeno en el que dos objetos liberan electrones rápidamente cuando se acercan o entran en contacto. Es bien sabido que los objetos acumulan carga cuando entran en contacto o se frotan con otros objetos. Por ejemplo, cuando nuestras manos entran en contacto con el entorno, acumulan una gran cantidad de carga positiva. Cuando un objeto acumula una gran cantidad de carga positiva y se acerca o toca un conductor, los electrones se transfieren rápidamente desde el conductor al objeto cargado positivamente. Este proceso de transferencia rápida de electrones se llama Descarga Electroestática (ESD).

En los dispositivos electrónicos, a menudo hay muchas interfaces que se conectan a los pines de los chips a través de cables, y luego se conectan al interior del chip. Las altas tensiones generadas durante la descarga electroestática (que a menudo alcanzan miles de voltios) pueden perforar los conductos y, en el caso de corrientes elevadas, incluso pueden dañar los componentes. Por lo tanto, es importante prevenir la ESD.

La clave de la protección ESD radica en proporcionar un camino de descarga independiente para la carga estática (similar al funcionamiento de una pararrayos). Los dispositivos ESD se dividen principalmente en cuatro categorías: diodos TVS, resistencias varistor, condensadores multicapa cerámicos (MLCC) y supresores ESD.

## Modelos de Prueba ESD

|                                | HBM      | MM      | CDM      | Modelo IEC 61000-4-2 |
| ------------------------------ | -------- | ------- | -------- | -------------------- |
| Tensión de Prueba (V)          | 500-2000 | 100-200 | 500-2000 | 2000-15000           |
| Duración del Pulso (ns)        | ~150     | ~80     | ~1       | ~150                 |
| Corriente Pico a 2kV (μA_pico) | 1.33     | -       | ~5       | 7.5                  |
| Tiempo de Subida               | 25ns     | -       | <400ps   | <1ns                 |
| Número de Impulsos de Tensión  | 2        | 2       | 2        | 20                   |

### Modelo de Prueba de Descarga del Cuerpo Humano (HBM, Human Body Model)

Este modelo simula la descarga electrostática generada por el cuerpo humano y representa la situación cuando una persona toca un chip con la mano.

### Modelo de Prueba de Descarga de Máquina (MM, Machine Model)

Este modelo simula la descarga electrostática generada por una máquina o herramienta con menor resistencia al tocar un chip. A diferencia del modelo de prueba del cuerpo humano, este modelo tiene una mayor capacidad de almacenamiento de carga y carece de resistencia, lo que significa que la corriente de descarga será mucho mayor. Además, debido a los efectos de inductancia de los conductores, se producirán corrientes oscilantes, lo que implica cambios de polaridad en la corriente de descarga al chip.

### Modelo de Dispositivo Cargado (CDM, Charged Device Model)

Los dos primeros modelos simulan situaciones en las que un cuerpo cargado se descarga en un chip. El modelo de dispositivo cargado simula la situación en la que el propio chip está cargado y se descarga a tierra. Esto puede ocurrir cuando se retira un chip de su embalaje después de haber estado almacenado durante un tiempo. En esta situación, no hay resistencia ni capacitancia; el chip se descarga directamente a tierra a través de sus pines.

## Estándares de Referencia para ESD

Especificaciones de prueba HBM comunes:

| Estándar     | Capacidad de Carga ($C_d$) (pF) | Resistencia de Descarga ($R_d$) (Ω) |
| ------------ | ------------------------------- | ----------------------------------- |
| AEC-Q200-002 | 150                             | 2000                                |
| IEC61000-4-2 | 150                             | 330                                 |

Tomemos como ejemplo el estándar AEC-Q200-002, su circuito de prueba ESD HBM es el siguiente:

![ESD HBM Test Circuit](https://media.wiki-power.com/img/20211215164751.png)

Donde $C_x$ es la capacitancia del objeto de prueba, $C_d$ es la capacitancia de carga, $R_d$ es la resistencia de descarga y $R_c$ es la resistencia de protección. El método de prueba ESD es el siguiente:

- Conmutador 1 cerrado, conmutador 2 abierto: la fuente de alta tensión carga el condensador $C_d$.
- Conmutador 1 abierto, conmutador 2 cerrado: la carga almacenada en $C_d$ se aplica a $C_x$ para realizar la prueba ESD.

Curva de corriente de descarga:

![Curva de Corriente de Descarga](https://media.wiki-power.com/img/20211215165312.png)

## Proceso de Prueba ESD

Según el estándar AEC-Q200-002, el proceso de prueba HBM se puede seguir como se muestra en la siguiente imagen:

![Proceso de Prueba ESD](https://media.wiki-power.com/img/20211215165447.png)

Los niveles de resistencia resultantes se clasifican según la siguiente tabla:

| Nivel de Clasificación | Voltaje Máximo Soportado              |
| ---------------------- | ------------------------------------- |
| 1A                     | Menos de 500V (CC)                    |
| 1B                     | 0.5 kV (CC) o más, menos de 1 kV (CC) |
| 1C                     | 1 kV (CC) o más, menos de 2 kV (CC)   |
| 2                      | 2 kV (CC) o más, menos de 4 kV (CC)   |
| 3                      | 4 kV (CC) o más, menos de 6 kV (CC)   |
| 4                      | 6 kV (CC) o más, menos de 8 kV (CC)   |
| 5A                     | 8 kV (CC) o más, menos de 12 kV (AD)  |
| 5B                     | 12 kV (AD) o más, menos de 16 kV (AD) |
| 5C                     | 16 kV (AD) o más, menos de 25 kV (AD) |
| 6                      | 25 kV (AD) o más                      |

(CC) corresponde a Descarga de Contacto Directo, y (AD) a Descarga al Aire.

## Relación entre la Capacidad del Objeto de Prueba y la Resistencia ESD

El tamaño de la capacidad $C_x$ del objeto de prueba afecta la tensión en sus dos extremos de acuerdo con la siguiente relación:

$$
V_x = \frac{C_d}{C_d + C_x}V_d
$$

Cuando el voltaje de la fuente ($V_d$) y la capacidad de carga ($C_d$) son constantes, un aumento en la capacidad del objeto de prueba ($C_x$) reduce la tensión ($V_x$) en sus extremos.

En general, un mayor valor de $C_x$ tiende a aumentar la resistencia ESD. Sin embargo, debido a diferencias en el diseño, como el tipo y el grosor del dieléctrico, el rango de rendimiento de la resistencia al voltaje puede variar y no seguir exactamente esta tendencia.

### Referencia para la Capacidad de la Resistencia ESD

- Parámetros de la capacidad $C_x$: Serie GCM / Encapsulado 0402 / X7R / 50V
- Condiciones de prueba: $C_d=150pF, R_d=2kΩ$

![Referencia de Capacidad ESD](https://media.wiki-power.com/img/20211215172528.png)

Según la curva del gráfico, si se desea protegerse contra 1kV de ESD, se puede utilizar un condensador de 1000pF. En el diseño de circuitos, es recomendable colocar una resistencia grande en paralelo con el condensador para descargar la carga eléctrica del condensador después de eliminar la ESD.

## Referencias y Agradecimientos

- [Introducción a la Fiabilidad y ESD](https://mazhaoxin.github.io/2021/08/01/Reliability_and_ESD_Introduction/)
- [Apuntes de Ingeniería Electrónica: Conceptos Básicos de ESD y Selección de Protección ESD](https://haipeng.me/2019/09/03/esd-protection/)
- [Resistencia ESD de Condensadores](https://article.murata.com/en-us/article/esd-resistance-of-capacitors)
- [Comprender el Papel de los Dispositivos ESD en el Diseño de PCB](http://murata.eetrend.com/article/2021-11/1004974.html)

[Para ser reemplazado[1]]
[Para ser reemplazado[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
