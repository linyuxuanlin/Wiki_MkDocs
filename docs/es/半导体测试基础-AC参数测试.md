# Fundamentos de prueba de semiconductores - Prueba de parámetros AC

La prueba AC asegura que la secuencia de tiempo de un DUT cumpla con los requisitos de sus especificaciones.

## Parámetros AC básicos

### Tiempo de establecimiento (Setup Time)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094845.png)

El tiempo de establecimiento se refiere al tiempo mínimo que los datos (en la imagen, `DATA IN`) deben mantenerse estables e invariables antes de que la señal de referencia (en la imagen, `WE`) cambie (tomando un valor medio de 1,5 V) para garantizar que se puedan leer correctamente. Antes del tiempo mínimo de establecimiento, los datos pueden cambiar libremente, pero si se excede el tiempo mínimo de establecimiento (manteniéndose estables demasiado tarde), es posible que no se puedan reconocer, lo que puede provocar errores. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción                | Mín | Máx | Unidad |
| --------- | -------------------------- | --- | --- | ------ |
| $t_{SD}$  | Configuración de datos al final de la escritura | 11  |     | ns     |

### Tiempo de retención (Hold Time)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094858.png)

El tiempo de retención se refiere al tiempo mínimo que los datos (en la imagen, `DATA IN`) deben mantenerse estables después de que la señal de referencia (en la imagen, `WE`) cambie (alcanzando un cierto umbral de voltaje) para garantizar que no haya errores. Si el tiempo de retención es demasiado corto, existe la posibilidad de que los datos no se reconozcan correctamente. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción                | Mín | Máx | Unidad |
| --------- | -------------------------- | --- | --- | ------ |
| $t_{HD}$  | Retención de datos desde el final de la escritura | 1   |     | ns     |

### Retardo de propagación (Propagation Delay)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094910.png)

El retardo de propagación se refiere al intervalo de tiempo entre la transmisión de una señal y la transmisión de otra señal relacionada. En la mayoría de los casos, se mide el intervalo de tiempo entre el cambio de la señal de entrada (en la imagen, `ADDR`) y la respuesta correspondiente de la salida (en la imagen, `DATA OUT`) (el tiempo necesario desde la entrada hasta la salida). Garantiza que la señal de salida pueda aparecer dentro de un cierto tiempo después de que aparezca la señal de entrada. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción           | Mín | Máx | Unidad |
| --------- | --------------------- | --- | --- | ------ |
| $t_{AA}$  | Dirección a datos válidos |     | 15  | ns     |

### Ancho de pulso mínimo (Minimum Pulse Widths)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094924.png)

El ancho de pulso mínimo generalmente incluye el ancho de pulso mínimo bajo y el ancho de pulso mínimo alto, que se utilizan para garantizar que el tiempo de operación mínimo de temporización de pulso sea el valor mínimo. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción             | Mín | Máx | Unidad |
| --------- | ----------------------- | --- | --- | ------ |
| $t_{WL}$  | Tiempo mínimo de reloj bajo | 20  |     | ns     |
| $t_{WH}$  | Tiempo mínimo de reloj alto | 25  |     | ns     |

### Frecuencia Máxima (Maximum Frequency)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094934.png)

La frecuencia máxima de trabajo se refiere a la velocidad máxima a la que un dispositivo puede funcionar. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción               | Mín | Máx  | Unidad |
| --------- | ------------------------- | --- | ---- | ------ |
| $f_{MAX}$ | Frecuencia máxima de reloj |     | 22.2 | MHz    |

### Tiempo de Habilitación de Salida (Output Enable Time)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094941.png)

Se refiere al tiempo necesario para que un pin cambie de un estado de alta impedancia (deshabilitado) a un estado de nivel de conducción válido (alto o bajo), asegurando que el buffer de salida pueda cambiar el estado del pin dentro del tiempo especificado. Se mide calculando el intervalo de tiempo desde que se emite la señal de control hasta que se detecta el cambio de salida. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción              | Mín | Máx | Unidad |
| --------- | ------------------------ | --- | --- | ------ |
| $t_{DOE}$ | OE bajo a datos válidos   |     | 10  | ns     |

### Tiempo de Deshabilitación de Salida (Output Disable Time)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220809094948.png)

Se refiere al tiempo necesario para que un pin cambie de un estado de nivel de conducción válido (alto o bajo) a un estado de alta impedancia (deshabilitado), asegurando que el buffer de salida pueda cambiar el estado del pin dentro del tiempo especificado. Se mide calculando el intervalo de tiempo desde que se emite la señal de control hasta que se detecta el cambio de salida. Se representa en las especificaciones de la siguiente manera:

| Parámetro  | Descripción                | Mín | Máx | Unidad |
| ---------- | -------------------------- | --- | --- | ------ |
| $t_{HZOE}$ | OE alto a datos válidos     |     | 8   | ns     |

## Parámetros de Temporización

### Temporización del Ciclo de Lectura (Read Cycle Timing)

Un ejemplo del ciclo de lectura de una RAM estática de 256 x 4:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220731190300.png)

| Parámetro  | Descripción                | Min | Max | Unidad |
| ---------- | -------------------------- | --- | --- | ------ |
| $t_{RC}$   | Tiempo de ciclo de lectura  | 15  |     | ns     |
| $t_{AA}$   | Dirección a datos válidos   |     | 15  | ns     |
| $t_{ACS}$  | Selección de chip a datos válidos |     | 10  | ns     |
| $t_{DOE}$  | OE bajo a datos válidos     |     | 10  | ns     |
| $t_{HZCS}$ | Selección de chip a alta impedancia |     | 8   | ns     |
| $t_{HZOE}$ | OE alto a alta impedancia   |     | 8   | ns     |
| $t_{LZCS}$ | Selección de chip a baja impedancia | 2   |     | ns     |
| $t_{LZOE}$ | OE bajo a baja impedancia   | 2   |     | ns     |

1. Primero, el parámetro $t_{RC}$ determina la duración del ciclo de lectura.
2. Determine qué señal controla la función de lectura. En el ejemplo de la figura anterior, la salida de datos de la RAM está controlada por el flanco descendente de OE.

### Temporización del ciclo de escritura (Write Cycle Timing)

Un ejemplo de ciclo de escritura para una RAM estática de 256 x 4:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220731190328.png)

| Parámetro  | Descripción                   | Min | Max | Unidad |
| ---------- | ----------------------------- | --- | --- | ------ |
| $t_{WC}$   | Tiempo de ciclo de escritura  | 15  |     | ns     |
| $t_{HZWE}$ | WE bajo a alta impedancia     |     | 8   | ns     |
| $t_{LZWE}$ | WE alto a baja impedancia     | 2   |     | ns     |
| $t_{PWE}$  | Ancho de pulso de WE          | 11  |     | ns     |
| $t_{SD}$   | Configuración de datos hasta el final de escritura | 11  |     | ns     |
| $t_{HD}$   | Retención de datos desde el final de escritura | 1   |     | ns     |
| $t_{SA}$   | Configuración de dirección hasta el inicio de escritura | 2   |     | ns     |
| $t_{HA}$   | Retención de dirección desde el final de escritura | 2   |     | ns     |
| $t_{SCS}$  | CS bajo hasta el final de escritura | 11  |     | ns     |
| $t_{AW}$   | Configuración de dirección hasta el final de escritura | 13  |     | ns     |

1. Primero, el parámetro $t_{WC}$ determina la duración del ciclo de escritura.
2. Determine qué señal controla la función de escritura. En el ejemplo de la figura anterior, la entrada de datos de la RAM está controlada por el flanco ascendente de WE.

## Referencias y agradecimientos

- "The Fundamentals Of Digital Semiconductor Testing"

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.