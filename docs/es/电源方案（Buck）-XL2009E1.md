# Esquema de alimentación (Buck) - XL2009E1

XL2009E1 es un chip Buck de Core Dragon con una entrada máxima de 36V, una salida de 3A y una frecuencia fija de 180kHz. Tiene una función de protección contra corriente excesiva, y cuando hay un cortocircuito, la frecuencia se reduce a 48kHz.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/DC-DC(Buck)/XL2009E1**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/XL2009E1>)

## Características principales

- Topología: DC/DC (Buck)
- Modelo del dispositivo: XL2009E1
- Encapsulado: SOP8L
- Voltaje de entrada: 8-36 V
- Voltaje de salida: 1.25-32V
- Diferencia mínima de entrada y salida: 0.3V
- Ciclo de trabajo máximo: 100%
- Frecuencia de operación: 180kHz fija
- Corriente de salida máxima: 3A
- Eficiencia (entrada 12V, salida 5V@2.1A): 89%
- Precio de referencia: ￥ 2.1
- Otras características
  - Con circuito de corriente constante en la salida
  - Protección interna contra cortocircuitos
  - Protección interna contra corriente limitada

## Circuito de aplicación típico

Según el circuito de aplicación típico proporcionado en la hoja de datos (entrada 8-36V, salida 5V@2.1A):

![](https://media.wiki-power.com/img/20220407103157.png)

## Definición de pines

![](https://media.wiki-power.com/img/20220407065806.png)

- FB: Pin de entrada de retroalimentación, se utiliza una resistencia para dividir el voltaje de $V_{OUT}$ y proporcionar retroalimentación. No se puede conectar directamente a tierra. El voltaje de referencia de retroalimentación es de 1.25V.
- OCSET: Pin de configuración de corriente constante de salida.
- VC: Capacitor de derivación del regulador interno. Por lo general, se conecta de 1uF a VIN.
- VIN: Pin de entrada de alimentación. El voltaje de entrada es de 8-36V. Se requiere un capacitor grande de desacoplamiento.
- SW: Salida del interruptor Buck.

## Descripción de características

### Diagrama de funciones internas

![](https://media.wiki-power.com/img/20220407070413.png)

### Regulación de voltaje de salida

XL2009E1 proporciona una referencia interna de voltaje de 1.25V. El voltaje de salida se divide mediante una resistencia y se aplica al pin FB desde $V_{OUT}$, donde se realiza una comparación y ajuste interno. Se recomienda utilizar resistencias de división con una desviación del 1% o inferior y un coeficiente de temperatura de 100 ppm o inferior. Se sugiere que el valor de la resistencia en el lado bajo, $R_1$, sea de 4.7k, y se calcule el valor de la resistencia en el lado alto, $R_2$, utilizando la siguiente fórmula:

$$
V_{OUT}=1.25*(1+\frac{R_2}{R_1})
$$

### Selección de diodo Schottky

La tensión de ruptura nominal del diodo debe ser al menos un 25% más alta que el voltaje de entrada máximo. Para obtener la mejor confiabilidad, la corriente nominal del diodo debe ser igual a la corriente máxima de salida del regulador. En situaciones donde el voltaje de entrada es mucho mayor que el voltaje de salida, la corriente promedio del diodo será más baja. En este caso, se puede utilizar un diodo con una corriente nominal promedio más baja, aproximadamente $(1-D) * I_{OUT}$, pero la corriente nominal de pico debe ser mayor que la corriente de carga máxima.

El manual de datos de XL2009E1 proporciona una tabla de selección directa de diodos (3A):

| Voltaje de entrada | Modelo      |
| ------------------ | ----------- |
| 20V                | SK32        |
| 30V                | SK33/30WQ03 |
| 40V                | SK34/30WQ04 |
| 50V                | SK35/30WQ05 |
| 60V                | SK36        |

### Curvas de parámetros

Relación entre el voltaje de salida y la corriente:

![](https://media.wiki-power.com/img/20220407100229.png)

Relación entre la eficiencia y la corriente de salida:

![](https://media.wiki-power.com/img/20220407103033.png)

Relación entre la corriente de salida y la resistencia RCS (control de corriente constante):

![](https://media.wiki-power.com/img/20220407102905.png)

## Referencias y Agradecimientos

- [XL2009_Datasheet](https://datasheet.lcsc.com/lcsc/1806111754_XLSEMI-XL2009E1_C73335.pdf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
