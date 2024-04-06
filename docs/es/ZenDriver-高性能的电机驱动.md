# ZenDriver - Motor Driver de Alto Rendimiento

—— Basado en la versión V5.1 Release

Repositorio del proyecto: [**linyuxuanlin/ZenDriver**](https://github.com/linyuxuanlin/ZenDriver)

## Especificaciones Básicas

1. Voltaje de Entrada: **7.2 ~ 20 V**
2. Corriente de Salida: **0 ~ 68 A**
3. Ofrece una salida de **5V 1.5A** para alimentar el controlador
4. Dispositivos de Protección: Integrados con circuitos de protección contra inversión de polaridad y aislamiento óptico

## Definición de Interfaces

![](https://media.wiki-power.com/img/20200125192433.png)

Los pines en el **lado del motor** de izquierda a derecha son: **M-, 5V, Encoder A, Encoder B, GND, M+**, correspondientes a los pines del motor y pueden conectarse directamente al motor.

Los pines en el **lado de señal** de derecha a izquierda son: **GND, Encoder B, Encoder A, IN2, IN1, 5V**. Nota: el puerto de 5V **puede suministrar energía al microcontrolador** (hasta 1.5 A).

Los tres puertos en el **lado de entrada de alimentación** son comunes, generalmente se recomienda conectar la batería al puerto del medio, y los dos puertos adyacentes se utilizan para proporcionar energía a otras placas de control.

## Guía de Uso

### Prueba de Alimentación Directa

1. Conecte una batería de **7.2 ~ 20 V** como fuente de alimentación.
2. Conecte el motor.
3. Conecte **5V** en el **lado de señal** a **IN1 e IN2**, en este momento, el motor girará en ambas direcciones.

### Conexión para Pruebas con un Microcontrolador

1. Conecte una batería de **7.2 ~ 20 V** como fuente de alimentación.
2. Conecte el motor.
3. Conecte **GND del lado de señal** al **GND del microcontrolador**, y el puerto **5V** al **5V del microcontrolador**.
4. Los pines **IN1 e IN2** deben conectarse a los pines PWM del microcontrolador.
5. Depure mediante código.

![](https://media.wiki-power.com/img/20200125192734.png)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
