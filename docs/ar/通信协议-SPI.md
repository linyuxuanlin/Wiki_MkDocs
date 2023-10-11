# Protocolo de comunicación - SPI

SPI (Serial Peripheral Interface) es un protocolo de comunicación **full-duplex, sincrónico, serial, maestro-esclavo, de bus** con una velocidad de transferencia de datos de 8 Mbit. SPI solo puede tener un host y puede conectarse a uno o varios esclavos. Cuando se conectan múltiples dispositivos, se requiere el uso de pines de selección de chip (chip select, CS).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210911095950.png)

## Pines de SPI

- **SCLK** (reloj serial): señal de reloj de onda cuadrada impulsada por el host, muestreada como entrada desde el extremo. Las señales en SDO y SDI se bloquean según la señal de reloj en SCLK. Un ciclo de reloj transmite 1 bit de datos, por lo que la velocidad de transmisión es igual a la frecuencia de reloj generada por el host.
- **SDI/SDO** (entrada de datos serial / salida de datos serial): describe la dirección del flujo de datos en relación con el host, pero en la placa, aparecen más MOSI (Master Out Slave In) y MISO (Master In Slave Out). Correspondientemente, SDO es MOSI en el host y MISO en el esclavo; mientras que SDI es MISO en el host y MOSI en el esclavo; en una topología de cadena, el dispositivo A MISO se conecta al dispositivo B MISO.
- **CS/SS** (selección de chip / selección de esclavo): impulsado por el host, se utiliza para arbitrar la prioridad de comunicación en el bus SPI. Cuando la línea CS es de bajo nivel, activa la comunicación SPI. CS es efectivo en bajo nivel.

## Operación de bloqueo de datos SPI

- Los datos SPI se bloquean en el flanco ascendente o descendente de SCLK.
- El borde que bloquea los datos se llama borde crítico.
- Por ejemplo, la imagen izquierda a continuación representa el bloqueo de la lógica `1` en el flanco ascendente de SDO, y la imagen derecha representa el bloqueo de la lógica `0` en el flanco descendente.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026151750.png)

## Ejemplo de segmento de lectura SPI

1. El borde crítico es el flanco ascendente.
2. El host envía datos al esclavo (SDI en el esclavo).
3. El pin CS se baja a 0V para activar SPI.
4. Los datos se transmiten en orden de bits de MSB a LSB en el flanco ascendente de SCLK.
5. Se completa la transmisión de datos: `1011001`

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026152228.png)

## Bordes críticos de SPI

- $t_{SU}$ (tiempo de configuración): define cuánto tiempo antes de que ocurra el evento del borde crítico, los datos en SDI deben ser determinados y estabilizados.
- $t_{HO}$ (tiempo de retención): define cuánto tiempo los datos en SDI deben mantenerse después del evento del borde crítico.
- $t_{DO}$ (tiempo de retardo): define el tiempo de retardo de los datos efectivos en SDO después del evento del borde crítico.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026160940.png)

## Modos de transferencia SPI (4)

- **CPOL** (polaridad del reloj): la polaridad del reloj en estado inactivo (sin transferencia de datos), `0` representa nivel bajo, `1` representa nivel alto.
- **CPHA** (fase del reloj): define si el bloqueo se realiza en el flanco ascendente o descendente. `0` representa el bloqueo en el primer borde de cambio; `1` representa el bloqueo en el segundo borde de cambio.

| Modo | CPOL (Polaridad del reloj) | CPHA (Fase del reloj)         | Flanco de captura  |
| ---- | -------------------------- | ----------------------------- | ------------------ |
| 0    | 0 (Bajo)                   | 0 (Captura en primer flanco)  | Flanco ascendente  |
| 1    | 0 (Bajo)                   | 1 (Captura en segundo flanco) | Flanco descendente |
| 2    | 1 (Alto)                   | 0 (Captura en primer flanco)  | Flanco descendente |
| 3    | 1 (Alto)                   | 1 (Captura en segundo flanco) | Flanco ascendente  |

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026162028.png)

## Cadena Daisy (Daisy Chain)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211026164011.png)

En el modo normal, cada esclavo SPI necesita una línea CS. Cuando hay muchos esclavos, esto ocupa demasiados pines de entrada/salida del maestro. Con la topología de cadena Daisy, solo se necesita una línea CS para controlar todos los esclavos.

El principio de la cadena Daisy es que los datos se transmiten desde el maestro al primer esclavo, luego del primer esclavo al segundo esclavo, y así sucesivamente, los datos se encadenan en serie a lo largo de la línea hasta el último esclavo, y el último esclavo transmite los datos al maestro a través de SDO.

## Ventajas y desventajas de SPI

Ventajas:

- Comunicación full-duplex
- Conducido por push-pull, puede proporcionar una buena integridad de señal y una velocidad relativamente alta
- Protocolo flexible, no se limita a 8 bits por byte
- Diseño de hardware simple
  - No se necesitan resistencias pull-up, por lo que el consumo de energía es menor
  - No hay mecanismo de arbitraje o modos de falla relacionados
  - Los esclavos no necesitan un reloj (proporcionado por el maestro)
  - Los dispositivos esclavos no necesitan una dirección separada
  - No se necesitan transceptores
  - Las señales son unidireccionales, lo que facilita el aislamiento de corriente
- La velocidad del reloj no tiene límite superior

Desventajas:

- Utiliza más pines que I2C
- Los esclavos no pueden responder con hardware
- No hay mecanismo de detección de errores, como el bit de paridad en UART
- Solo puede haber un maestro
- La especificación no es uniforme, por lo que no se puede verificar la consistencia
- La distancia de transmisión es relativamente corta (en comparación con CAN, RS232, RS485, etc.)

## Referencias y agradecimientos

- "Analog Engineer's Pocket Reference"

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
