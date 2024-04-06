# Protocolo de comunicación - I2C

I2C (Inter-Integrated Circuit) es un bus de comunicación serial que permite la presencia de múltiples maestros, pero solo puede haber un maestro en línea en un momento dado. I2C consta de dos líneas de señal de drenaje abierto, con una conexión simple utilizando resistencias pull-up, con niveles típicos de 3.3V o 5V en lógica positiva. Las velocidades de transferencia se dividen en modo rápido (400Kb/s), modo estándar (100Kb/s) y modo lento (10Kb/s).

En el bus I2C, los dispositivos esclavos son seleccionados mediante su dirección I2C. Esto permite que un solo maestro controle múltiples dispositivos a través de dos líneas.

![](https://media.wiki-power.com/img/20211026174634.png)

## Pines de I2C

- **SCL** (reloj serial): Es una señal de onda generada por el maestro para controlar la velocidad de transferencia y el almacenamiento de datos.
- **SDA** (datos seriales): Es una línea de señal **semidúplex y sincrónica**, que transmite datos que incluyen direcciones, señales de control y datos de comunicación.

## Direcciones de I2C

- La dirección de I2C se divide en 7 bits de dirección y 1 bit de indicación de lectura/escritura.
- Cada dispositivo en el bus I2C debe tener una dirección única, ya que habrá problemas si hay direcciones duplicadas. Algunos dispositivos permiten programar su dirección I2C.

![](https://media.wiki-power.com/img/20211027112717.png)

## Comunicación I2C

- **START**: El maestro inicia la comunicación al bajar la línea SDA mientras SCL está en alto.
- **STOP**: El maestro finaliza la comunicación al liberar la línea SDA (volviéndola a nivel alto) mientras SCL está en alto.
- **ACK** (acknowledge): Cada transferencia I2C consiste en la transmisión de 1 byte (8 bits) en cada pulso de SCL. El noveno pulso de cada transferencia se reserva para la señal de confirmación del esclavo, y la señal ACK indica el éxito de la transferencia anterior.

### Ejemplo de segmento de transferencia I2C

El valor transmitido en este segmento es `11001101`:

![](https://media.wiki-power.com/img/20211104172952.png)

1. El maestro baja la línea SDA para generar la señal START.
2. El primer bit se establece y el maestro baja la línea SCL para generar la señal de reloj.
3. Cuando se transmite el noveno bit, el maestro no baja la línea SDA. Si el esclavo confirma la transferencia completa, baja la línea SDA para que el maestro lo sepa.

### Transferencia de datos válida

1. Durante el tiempo en que SCL se mantiene en alto (transmisión de datos), SDA debe mantenerse estable para que sea válida.
2. Solo se permite cambiar el valor de SDA durante los intervalos de baja de SCL.
3. Cuando SCL está en alto y SDA cambia, se interpreta como un evento de START, RESTART o STOP.

![](https://media.wiki-power.com/img/20211105172139.png)

### Temporización de subida/bajada en el circuito de interfaz

![](https://media.wiki-power.com/img/20211108093819.png)

En la figura, el transistor se enciende durante el nivel bajo y descarga el capacitor $C_b$ a nivel bajo. Por otro lado, el transistor se apaga durante el nivel alto y la resistencia pull-up carga el capacitor $C_b$ a nivel alto.

- $t_r$ (tiempo de subida): Es el tiempo máximo que tarda la señal en pasar de nivel bajo a nivel alto. Debido a que la señal I2C es de drenaje abierto, el tiempo de subida está determinado por la resistencia pull-up y la constante de tiempo RC del capacitor de bus.
- $t_f$ (tiempo de bajada): Es el tiempo máximo que tarda la señal en pasar de nivel alto a nivel bajo.

![](https://media.wiki-power.com/img/20211108095142.png)

### Cálculo de la resistencia pull-up de I2C

- Valor mínimo de la resistencia pull-up: $R_{Pull(Min)}=\frac{V_{DD}-V_{OLMAX}}{I_{SinkMax}}$
- Valor máximo de la resistencia pull-up: $R_{Pull(Max)}=\frac{t_r}{0.8473*C_b}$

El valor mínimo de la resistencia pull-up proporcionará el tiempo de subida más corto. Si se utiliza un valor de resistencia menor, se consumirá demasiada corriente cuando el transistor de salida esté encendido (nivel bajo lógico), lo cual viola las especificaciones de salida de nivel bajo lógico máximo.

La resistencia de pull-up con el valor máximo resultará en el tiempo de subida más largo. Si se utiliza una resistencia de pull-up mayor que este valor, se violarán los requisitos de sincronización.

$V_{DD}$ representa el voltaje de alimentación; $V_{OLMAX}$ representa el nivel lógico bajo máximo (valor típico de 0.4V); $I_{SinkMax}$ representa la corriente de drenaje máxima (valor típico de 3mA); $C_b$ representa la capacidad total del bus, que depende de la longitud y anchura de las trazas del PCB, así como de la capacidad de los dispositivos conectados al bus.

Ejemplo de cálculo:

![](https://media.wiki-power.com/img/20211108103406.png)

## Referencias y Agradecimientos

- "Analog Engineer’s Pocket Reference"
- [¿Cómo utilizar el bus I2C? Después de leer esto, lo sabrás](https://mp.weixin.qq.com/s/IeL77NTyVdTdkcNtqjjFPA)
- [[Circuito] Protocolo del bus I2C 🚧](https://zhenhuizhang.tk/post/dian-lu-i2c-zong-xian-xie-yi/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
