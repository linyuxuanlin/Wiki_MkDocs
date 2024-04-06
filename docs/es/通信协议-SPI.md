# Protocolo de Comunicación - SPI

SPI (Serial Peripheral Interface) es un protocolo de comunicación **full-duplex, síncrono, serial, maestro-esclavo, bus** con una velocidad de transferencia de datos de 8 Mbit. SPI solo puede tener un maestro y puede estar conectado a uno o varios esclavos. Cuando se conectan múltiples dispositivos, se requiere el uso de pines de selección de chip (chip select, CS).

![](https://media.wiki-power.com/img/20210911095950.png)

## Pines de SPI

- **SCLK** (serial clock): Es una señal de reloj en forma de onda generada por el maestro, que se muestrea en la entrada del esclavo. Los datos en SDO y SDI se capturan según la señal de reloj en SCLK. Se transfiere 1 bit de datos en un ciclo de reloj, por lo que la velocidad de transferencia es igual a la frecuencia de reloj generada por el maestro.
- **SDI/SDO** (serial data in / serial data out): Describe la dirección del flujo de datos con respecto al maestro, pero en la placa suele aparecer como MOSI (Master Out Slave In) y MISO (Master In Slave Out). En el maestro, SDO es MOSI, mientras que en el esclavo es MISO; y en el maestro, SDI es MISO, mientras que en el esclavo es MOSI. En una topología en cadena, la señal MISO del dispositivo A se conecta a la señal MISO del dispositivo B.
- **CS/SS** (chip select / slave select): Es controlado por el maestro y se utiliza para arbitrar la prioridad de comunicación en el bus SPI. Cuando la línea CS está en bajo nivel, se activa la comunicación SPI. CS es activo en bajo nivel.

## Operación de Captura de Datos en SPI

- Los datos en SPI se capturan en el flanco ascendente o descendente de SCLK.
- El flanco de captura de datos se conoce como flanco crítico.
- Por ejemplo, en la imagen de la izquierda a continuación, se muestra la captura de un "1" lógico en el flanco ascendente de SDO, mientras que en la imagen de la derecha se muestra la captura de un "0" lógico en el flanco descendente.

![](https://media.wiki-power.com/img/20211026151750.png)

## Ejemplo de Lectura de Segmento en SPI

1. El flanco crítico es ascendente.
2. El maestro envía datos al esclavo (en el esclavo, esto corresponde a SDI).
3. El pin CS se baja a 0V para activar la comunicación SPI.
4. Los datos se transmiten en orden desde el bit más significativo (MSB) hasta el menos significativo (LSB) en cada flanco ascendente de SCLK.
5. Se completa la transmisión de datos: `1011001`.

![](https://media.wiki-power.com/img/20211026152228.png)

## Flanco Crítico en SPI

- $t_{SU}$ (tiempo de configuración): Define cuánto tiempo antes del evento del flanco crítico, los datos en SDI deben estar determinados y estables.
- $t_{HO}$ (tiempo de retención): Define cuánto tiempo los datos en SDI deben mantenerse después del evento del flanco crítico.
- $t_{DO}$ (tiempo de retardo): Define el tiempo de retardo para que los datos válidos aparezcan en SDO después del evento del flanco crítico.

![](https://media.wiki-power.com/img/20211026160940.png)

## Modos de Transferencia en SPI (4 modos)

- **CPOL** (clock polarity, polaridad del reloj): Define la polaridad del reloj en estado inactivo (sin transferencia de datos), donde `0` representa nivel bajo y `1` representa nivel alto.
- **CPHA** (clock phase, fase del reloj): Define si la captura de datos se realiza en el flanco ascendente o descendente. `0` representa la captura en el primer flanco de cambio, mientras que `1` representa la captura en el segundo flanco de cambio.

| Modo | CPOL (Polaridad del Reloj) | CPHA (Fase del Reloj)            | Flanco de Captura |
| ---- | -------------------------- | -------------------------------- | ----------------- |
| 0    | 0 (Nivel Bajo)             | 0 (Captura en el Primer Flanco)  | Ascendente        |
| 1    | 0 (Nivel Bajo)             | 1 (Captura en el Segundo Flanco) | Descendente       |
| 2    | 1 (Nivel Alto)             | 0 (Captura en el Primer Flanco)  | Descendente       |
| 3    | 1 (Nivel Alto)             | 1 (Captura en el Segundo Flanco) | Ascendente        |

![](https://media.wiki-power.com/img/20211026162028.png)

## Cadena de margaritas (Daisy Chain)

![](https://media.wiki-power.com/img/20211026164011.png)

En el modo normal, cada esclavo SPI requiere una línea CS. Cuando hay muchos esclavos, ocupan demasiados pines de E/S del maestro. Con la conexión en cadena de margaritas, solo se necesita una línea CS para controlar todos los esclavos.

El principio de la cadena de margaritas es que los datos se transmiten desde el maestro al primer esclavo, luego del primer esclavo al segundo esclavo, y así sucesivamente, los datos se transmiten en cascada a lo largo de la línea hasta el último esclavo de la serie, y el último esclavo transmite los datos al maestro a través de SDO.

## Ventajas y desventajas de SPI

Ventajas:

- Comunicación full-duplex
- Impulsión push-pull, que proporciona una buena integridad de señal y una velocidad relativamente alta
- Protocolo flexible, no se limita a 8 bits por byte
- Diseño de hardware simple
  - No se requieren resistencias pull-up, lo que reduce el consumo de energía
  - No hay mecanismos de arbitraje ni modos de falla relacionados
  - Los esclavos no necesitan un reloj (suministrado por el maestro)
  - Los dispositivos esclavos no necesitan una dirección separada
  - No se requieren transceptores
  - Las señales son unidireccionales, lo que facilita el aislamiento de corriente
- No hay límite superior en la velocidad del reloj

Desventajas:

- Requiere más pines que I2C
- Los esclavos no pueden realizar una respuesta de hardware
- No hay mecanismo de detección de errores, como el bit de paridad en UART
- Solo puede haber un maestro
- La especificación no es uniforme, lo que dificulta la verificación de la consistencia
- La distancia de transmisión es relativamente corta (en comparación con CAN, RS232, RS485, etc.)

## Referencias y agradecimientos

- "Analog Engineer's Pocket Reference"

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
