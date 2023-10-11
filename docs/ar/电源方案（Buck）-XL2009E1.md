# Esquema de alimentación (Buck) - XL2009E1

XL2009E1 es un chip Buck de 36V de entrada máxima, 3A de salida y 180kHz fijo de Longan, con protección contra sobrecorriente. Cuando hay un cortocircuito, la frecuencia se reduce a 48kHz.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/DC-DC(Buck)/XL2009E1**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/XL2009E1>)

## Características principales

- Topología: DC/DC (Buck)
- Modelo del dispositivo: XL2009E1
- Encapsulado: SOP8L
- Voltaje de entrada: 8-36 V
- Voltaje de salida: 1.25-32V
- Diferencia mínima de entrada/salida: 0.3V
- Ciclo de trabajo máximo: 100%
- Frecuencia de trabajo: 180kHz fijo
- Corriente de salida máxima: 3A
- Eficiencia (entrada 12V, salida 5V@2.1A): 89%
- Precio de referencia: ¥2.1
- Otras características
  - Con anillo de corriente constante de salida
  - Protección contra cortocircuitos incorporada
  - Protección contra sobrecorriente incorporada

## Circuito de aplicación típico

Según el circuito de aplicación típico proporcionado por el manual de datos (entrada 8-36V, salida 5V@2.1A):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407103157.png)

## Definición de pines

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407065806.png)

- FB: Pin de entrada de retroalimentación, se introduce una retroalimentación a través de una resistencia desde $V_{OUT}$ y no se puede conectar directamente a tierra. La tensión de referencia de retroalimentación es de 1.25V.
- OCSET: Pin de configuración de corriente constante de salida.
- VC: Capacitor de derivación del regulador interno. Por lo general, se conecta de 1uF a VIN.
- VIN: Pin de entrada de alimentación. El voltaje de entrada es de 8-36V. Se requiere un gran capacitor de acoplamiento.
- SW: Salida de conmutación Buck.

## Descripción de características

### Diagrama de funciones internas

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407070413.png)

### Regulación de voltaje de salida

XL2009E1 proporciona una tensión de referencia interna de 1.25V. La tensión de salida se divide mediante un divisor de resistencia y se introduce en el pin FB desde $V_{OUT}$ para su comparación y regulación interna. Se recomienda utilizar resistencias de desviación con una desviación del 1% o inferior y un coeficiente de temperatura de 100 ppm o inferior. El uso de valores de resistencia más grandes para el divisor de resistencia es beneficioso para mejorar la eficiencia de carga ligera, pero si son demasiado grandes, el regulador será más susceptible al ruido y al error de voltaje de entrada de la corriente de entrada de FB. Se recomienda que el valor de la resistencia de bajo lado $R_1$ sea de 4.7k, y el valor de la resistencia de alto lado $R_2$ se calcule mediante la fórmula:

$$
V_{OUT}=1.25*(1+\frac{R_2}{R_1})
$$

### Selección de diodo Schottky

La tensión de ruptura nominal del diodo debe ser al menos un 25% mayor que el voltaje de entrada máximo. Para obtener la mejor confiabilidad, la corriente nominal del diodo debe ser igual a la corriente de salida máxima del regulador. Cuando el voltaje de entrada es mucho mayor que el voltaje de salida, la corriente media del diodo será más baja. En este caso, se puede utilizar un diodo con una corriente nominal media más baja, aproximadamente $(1-D) * I_{OUT}$, pero la corriente nominal de pico debe ser mayor que la corriente de carga máxima.

El manual de datos de XL2009E1 proporciona una tabla de selección directa de diodos (3A):

| Voltaje de entrada | Modelo      |
| ------------------ | ----------- |
| 20V                | SK32        |
| 30V                | SK33/30WQ03 |
| 40V                | SK34/30WQ04 |
| 50V                | SK35/30WQ05 |
| 60V                | SK36        |

### Curvas de parámetros

Relación entre voltaje de salida y corriente:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407100229.png)

Relación entre eficiencia y corriente de salida:

Relación entre la corriente de salida y la resistencia RCS (control de corriente constante):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220407102905.png)

## Referencias y agradecimientos

- [Hoja de datos XL2009](https://datasheet.lcsc.com/lcsc/1806111754_XLSEMI-XL2009E1_C73335.pdf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
