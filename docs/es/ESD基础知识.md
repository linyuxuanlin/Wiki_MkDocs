# Fundamentos de ESD

ESD (descarga electrostática) se refiere al fenómeno de transferencia rápida de electrones entre dos objetos cuando se acercan o entran en contacto. Es bien sabido que los objetos generan y acumulan cargas eléctricas durante el contacto y la fricción con otros objetos. Por ejemplo, nuestras manos acumulan muchas cargas positivas cuando se frotan con el exterior. Cuando un objeto con una gran cantidad de cargas positivas acumuladas se acerca o entra en contacto con un conductor, los electrones se transfieren rápidamente del conductor al objeto con cargas positivas acumuladas. Este proceso de transferencia rápida de electrones se conoce como descarga electrostática (ESD).

Los dispositivos electrónicos suelen tener muchos interfaces que se conectan a los pines del chip a través de cables y luego al interior del chip. La alta tensión (generalmente de hasta varios miles de voltios) generada durante la descarga electrostática puede perforar el chip y, si la corriente es alta, puede incluso fundir los componentes, por lo que se debe evitar.

La clave para la protección contra ESD es proporcionar un canal de descarga separado para la electricidad estática (como un pararrayos). Los dispositivos ESD se dividen principalmente en cuatro categorías: diodos TVS, resistencias de protección contra sobretensiones, condensadores multicapa cerámicos (MLCC) y supresores de ESD.

## Modelo de prueba ESD

|                                  | HBM      | MM      | CDM      | Modelo IEC 61000-4-2 |
| -------------------------------- | -------- | ------- | -------- | -------------------- |
| Voltaje de prueba (V)            | 500-2000 | 100-200 | 500-2000 | 2000-15000           |
| Tiempo de pulso (ns)             | ~150     | ~80     | ~1       | ~150                 |
| Corriente de pico a 2kV ($A_pk$) | 1.33     | -       | ~5       | 7.5                  |
| Tiempo de subida                 | 25ns     | -       | <400ps   | <1ns                 |
| Número de impulsos de voltaje    | 2        | 2       | 2        | 20                   |

### Modelo de cuerpo humano (HBM, Human Body Model)

Este modelo simula la descarga electrostática del cuerpo humano y simula la situación en la que una persona toca el chip con la mano.

### Modelo de máquina (MM, Machine Model)

Este modelo simula la descarga electrostática mecánica y simula la situación en la que se produce una descarga electrostática al tocar el chip con una mano mecánica u otra herramienta de baja resistencia.

La diferencia con el modelo de cuerpo humano es que tiene una capacidad mayor y no tiene resistencia, por lo que la corriente de descarga será mucho mayor. Además, debido al efecto de la inductancia del cable, también habrá una corriente de oscilación, es decir, la corriente de descarga del chip cambiará de positiva a negativa.

### Modelo de dispositivo cargado (CDM, Charged Device Model)

Los dos modelos anteriores simulan la situación en la que un objeto cargado descarga en el chip. El modelo de dispositivo cargado simula la situación en la que el chip se carga a sí mismo y descarga a tierra. Este fenómeno ocurre cuando se saca el chip del paquete después de haber estado almacenado en un almacén durante un tiempo. En este caso, no hay resistencia ni capacidad, y el chip se descarga directamente a tierra a través de los pines.

## Normas de referencia ESD

Especificaciones comunes de prueba HBM:

| Estándar     | Capacidad de carga $C_d (pF)$ | Resistencia de descarga $R_d (Ω)$ |
| ------------ | ----------------------------- | --------------------------------- |
| AEC-Q200-002 | 150                           | 2000                              |
| IEC61000-4-2 | 150                           | 330                               |

Tomando como ejemplo la norma AEC-Q200-002, el circuito de prueba ESD HBM es el siguiente:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215164751.png)

Donde $C_x$ es la capacidad del objeto de prueba, $C_d$ es la capacidad de carga, $R_d$ es la resistencia de descarga y $R_c$ es la resistencia de protección. El método de prueba ESD es el siguiente:

- Interruptor 1 cerrado, interruptor 2 abierto: la fuente de alimentación de alta tensión carga la carga en $C_d$.
- Interruptor 1 abierto, interruptor 2 cerrado: la carga almacenada en $C_d$ se aplicará a $C_x$ para realizar la prueba de ESD.

Curva de corriente de descarga:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215165312.png)

## Proceso de prueba de ESD

Según el estándar AEC-Q200-002, el proceso de prueba HBM se puede realizar según la siguiente figura:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215165447.png)

Los niveles de resistencia a la tensión probados se clasifican según la siguiente tabla:

| Nivel de clasificación | Tensión máxima                         |
| ---------------------- | -------------------------------------- |
| 1A                     | Menos de 500V (DC)                     |
| 1B                     | Más de 0,5 kV (DC), menos de 1 kV (DC) |
| 1C                     | Más de 1 kV (DC), menos de 2 kV (DC)   |
| 2                      | Más de 2 kV (DC), menos de 4 kV (DC)   |
| 3                      | Más de 4 kV (DC), menos de 6 kV (DC)   |
| 4                      | Más de 6 kV (DC), menos de 8 kV (DC)   |
| 5A                     | Más de 8 kV (DC), menos de 12 kV (AD)  |
| 5B                     | Más de 12 kV (AD), menos de 16 kV (AD) |
| 5C                     | Más de 16 kV (AD), menos de 25 kV (AD) |
| 6                      | Más de 25 kV (AD)                      |

DC (descarga de contacto directo) es una descarga directa de contacto; AD (descarga de aire) es una descarga de aire.

## Relación entre la capacidad del objeto de prueba y la resistencia a la ESD

El valor de la capacidad del objeto de prueba $C_x$ afectará el voltaje en ambos extremos, cumpliendo la siguiente relación:

$$
V_x=\frac{C_d}{C_d+C_x}V_d
$$

Cuando la tensión de la fuente de alimentación ($V_d$) y la capacidad de carga ($C_d$) son constantes, el aumento de la capacidad del objeto de prueba ($C_x$) hará que el voltaje ($V_x$) en ambos lados disminuya.

Por lo tanto, en general, cuanto mayor sea la capacidad de $C_x$, mayor será la resistencia a la ESD. Sin embargo, en realidad, debido a las diferencias en el diseño, como el tipo y el grosor del dieléctrico, el rango de rendimiento de resistencia a la tensión también es diferente y no cumple completamente con la tendencia anterior.

### Referencia de capacidad y resistencia a la ESD

- Parámetros de capacidad de $C_x$: serie GCM / encapsulado 0402 / X7R / 50V
- Condiciones de prueba: $C_d=150pF,R_d=2kΩ$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211215172528.png)

Según la curva del gráfico, si queremos resistir una ESD de 1 kV, podemos usar un capacitor de 1000 pF para la defensa. En el diseño de circuitos reales, es mejor conectar un gran resistor en paralelo con el capacitor para descargar la electricidad en el capacitor después de eliminar la ESD.

## Referencias y agradecimientos

- [Introducción a la fiabilidad y ESD](https://mazhaoxin.github.io/2021/08/01/Reliability_and_ESD_Introduction/)
- [Notas de un ingeniero electrónico: conocimientos básicos sobre ESD y selección de protección ESD](https://haipeng.me/2019/09/03/esd-protection/)
- [Resistencia ESD de capacitores](https://article.murata.com/en-us/article/esd-resistance-of-capacitors)
- [Comprender el papel de los dispositivos ESD en el diseño de PCB en un solo artículo](http://murata.eetrend.com/article/2021-11/1004974.html)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
