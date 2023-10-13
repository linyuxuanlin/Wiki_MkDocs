# ZenDriver - Controlador de motor de alto rendimiento

- Basado en la versión V5.1 Release

Repositorio del proyecto: [**linyuxuanlin/ZenDriver**](https://github.com/linyuxuanlin/ZenDriver)

## Parámetros básicos

1. Voltaje de entrada: **7.2 ~ 20 V**
2. Corriente de salida: **0 ~ 68 A**
3. Proporciona una salida de alimentación de **5V 1.5A**, que puede ser utilizada por el controlador
4. Dispositivos de protección: circuito integrado de protección contra polaridad inversa y aislamiento óptico

## Definición de interfaces

![](https://img.wiki-power.com/d/wiki-media/img/20200125192433.png)

En el **lado del motor**, de izquierda a derecha, se encuentran: **M-, 5V, codificador A, codificador B, GND, M+**, correspondientes a los pines del motor, que se pueden conectar directamente al motor.

En el **lado de la señal**, de derecha a izquierda, se encuentran: **GND, codificador B, codificador A, IN2, IN1, 5V**. Tenga en cuenta que el puerto de 5V **puede proporcionar energía para el microcontrolador** (máximo 1.5 A).

En la **entrada de alimentación**, los tres puertos son universales, y se recomienda conectar la batería al puerto central, y los otros dos puertos se pueden utilizar para expandir la alimentación a otras placas de control.

## Guía de uso

### Prueba de alimentación directa

1. Conecte una batería de **7.2 ~ 20 V**
2. Conecte el motor
3. Conecte **IN1, IN2** a la salida de **5V** en el **lado de la señal**, y el motor girará en ambas direcciones.

### Prueba de conexión al microcontrolador

1. Conecte una batería de **7.2 ~ 20 V**
2. Conecte el motor
3. Conecte **GND** en el **lado de la señal** al **GND** del microcontrolador, y el puerto **5V** al **5V** del microcontrolador.
4. Conecte los pines **IN1, IN2** al puerto PWM del microcontrolador.
5. Depure el código.

![](https://img.wiki-power.com/d/wiki-media/img/20200125192734.png)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
