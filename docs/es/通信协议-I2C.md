# Protocolo de comunicación - I2C

I2C (Inter-Integrated Circuit) es un bus de comunicación serial que permite la presencia de múltiples maestros, pero solo puede haber un maestro en línea en un momento dado. I2C consta de dos líneas de señal de drenador abierto, con una conexión simple utilizando resistencias pull-up, con niveles típicos de lógica positiva de 3.3V o 5V. La velocidad de transmisión se divide en modo rápido (400Kb/s), modo estándar (100Kb/s) y modo lento (10Kb/s).

En el bus I2C, el esclavo se selecciona mediante su dirección I2C. Esto permite que un maestro controle varios esclavos a través de dos líneas.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026174634.png)

## Pines de I2C

- **SCL** (reloj serial): una señal de onda producida por el maestro que controla la velocidad de transmisión y el bloqueo de datos.
- **SDA** (datos seriales): una señal de línea sincrónica y semidúplex que transmite datos, incluyendo señales de dirección, control y comunicación.

## Direcciones de I2C

- La dirección de I2C se divide en una dirección de 7 bits y una indicación de lectura/escritura de 1 bit.
- Cada dispositivo en el bus I2C debe tener una dirección única, y si hay una dirección duplicada, se producirán problemas. Algunos dispositivos permiten la programación de la dirección de I2C.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211027112717.png)

## Comunicación de I2C

- **START**: el maestro inicia la transmisión al bajar SDA mientras SCL está en alto.
- **STOP**: el maestro finaliza la transmisión al liberar SDA (volviendo a alto) mientras SCL está en alto.
- **ACK** (reconocimiento): cada transmisión de I2C implica la transmisión de 1 byte (8 bits) con cada pulso de SCL. El noveno pulso se reserva para la señal de confirmación del esclavo, y la señal ACK indica que la transmisión anterior fue exitosa.

### Ejemplo de segmento de transmisión de I2C

Este segmento de transmisión es `11001101`:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211104172952.png)

1. El maestro baja SDA para iniciar la señal START.
2. El primer bit se establece, el maestro baja SCL y envía la señal de reloj a través del DAC.
3. Cuando se transmite el noveno bit, el maestro no baja SDA. Si el esclavo confirma la transmisión completa, baja SDA para que el maestro lo sepa.

### Transmisión de datos efectiva

1. Durante el tiempo en que SCL se mantiene en alto (transmisión de datos), SDA debe mantenerse estable para que sea efectivo.
2. Solo se permite que SDA cambie de valor durante los pulsos bajos de SCL.
3. Cuando SDA cambia mientras SCL está en alto, se interpreta como un evento de START, RESTART o STOP.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211105172139.png)

### Temporización de subida/bajada en el circuito de interfaz

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211108093819.png)

En la figura, el transistor se enciende cuando la señal está en bajo, descargando el capacitor $C_b$ a bajo. Por otro lado, el transistor se apaga cuando la señal está en alto, y la resistencia pull-up carga $C_b$ a alto.

- $t_r$ (tiempo de subida): el tiempo máximo que tarda la señal en pasar de bajo a alto. Debido a que I2C es una señal de drenador abierto, el tiempo de subida depende de la resistencia pull-up y la constante de tiempo RC del bus.
- $t_f$ (tiempo de bajada): el tiempo máximo que tarda la señal en pasar de alto a bajo.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211108095142.png)

### Cálculo de la resistencia pull-up de I2C

- Valor mínimo de la resistencia pull-up: $R_{Pull(Min)}=\frac{V_{DD}-V_{OLMAX}}{I_{SinkMax}}$
- Valor máximo de la resistencia pull-up: $R_{Pull(Max)}=\frac{t_r}{0.8473*C_b}$

El valor mínimo de la resistencia pull-up proporcionará el tiempo de subida más corto. Si se utiliza un valor de resistencia menor que este, se consumirá demasiada corriente cuando el transistor de salida esté activado (nivel lógico bajo), lo que violará la especificación de salida lógica baja máxima.

El valor máximo de la resistencia pull-up proporcionará el tiempo de subida más largo. Si se utiliza una resistencia pull-up mayor que este valor, se violarán los requisitos de sincronización.

$V_{DD}$ representa el voltaje de alimentación; $V_{OLMAX}$ representa el nivel lógico bajo máximo (valor típico de 0.4V); $I_{SinkMax}$ representa la corriente máxima de drenaje (valor típico de 3mA); $C_b$ representa la capacitancia total del bus, que depende de la longitud y el ancho de las pistas de PCB y de la capacitancia de los dispositivos conectados al bus.

Ejemplo de cálculo:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211108103406.png)

## Referencias y agradecimientos

- "Analog Engineer's Pocket Reference"
- [¿Cómo utilizar el bus I2C? Después de leer esto, lo sabrás](https://mp.weixin.qq.com/s/IeL77NTyVdTdkcNtqjjFPA)
- [[Circuito] Protocolo del bus I2C 🚧](https://zhenhuizhang.tk/post/dian-lu-i2c-zong-xian-xie-yi/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.