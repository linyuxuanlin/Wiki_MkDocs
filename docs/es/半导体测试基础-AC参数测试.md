# Fundamentos de Pruebas de Semiconductores - Pruebas de Parámetros AC

Las pruebas AC aseguran que la secuencia de temporización de un Dispositivo Bajo Prueba (DUT) cumple con los requisitos de sus especificaciones.

## Parámetros AC Básicos

### Tiempo de Establecimiento (Setup Time)

![Imagen](https://media.wiki-power.com/img/20220809094845.png)

El tiempo de establecimiento se refiere al tiempo mínimo durante el cual los datos (representados como `DATA IN` en la imagen) deben permanecer estables antes de que ocurra un cambio en la señal de referencia (en la imagen, `WE`) para garantizar una lectura correcta. Los datos pueden cambiar libremente antes del tiempo de establecimiento mínimo, pero si el cambio es demasiado tardío, es posible que no se puedan reconocer, lo que podría llevar a errores. La representación en las especificaciones es la siguiente:

| Parámetro | Descripción                                    | Mín | Máx | Unidad |
| --------- | ---------------------------------------------- | --- | --- | ------ |
| $t_{SD}$  | Establecimiento de Datos al Final de Escritura | 11  |     | ns     |

### Tiempo de Mantenimiento (Hold Time)

![Imagen](https://media.wiki-power.com/img/20220809094858.png)

El tiempo de mantenimiento se refiere al tiempo mínimo durante el cual los datos (representados como `DATA IN` en la imagen) deben mantenerse estables después de que ocurra un cambio en la señal de referencia (en la imagen, `WE`) para garantizar que no haya errores. En otras palabras, se trata del tiempo durante el cual los datos deben mantener su nivel estable antes de la activación de la señal de reloj. Si el tiempo de mantenimiento es demasiado corto, existe la posibilidad de que los datos no se reconozcan correctamente. Las especificaciones se presentan de la siguiente manera:

| Parámetro | Descripción                                        | Mín | Máx | Unidad |
| --------- | -------------------------------------------------- | --- | --- | ------ |
| $t_{HD}$  | Mantenimiento de Datos desde el Final de Escritura | 1   |     | ns     |

### Retardo de Propagación (Propagation Delay)

![Imagen](https://media.wiki-power.com/img/20220809094910.png)

El retardo de propagación se refiere al intervalo de tiempo entre la transmisión de una señal y la respuesta correspondiente de otra señal relacionada. Por lo general, se mide desde el cambio en la señal de entrada (representada como `ADDR` en la imagen) hasta la aparición de la respuesta en la salida correspondiente (representada como `DATA OUT` en la imagen). Este parámetro garantiza que la señal de salida aparezca dentro de un cierto período después de que aparezca la señal de entrada. Las especificaciones se presentan de la siguiente manera:

| Parámetro | Descripción               | Mín | Máx | Unidad |
| --------- | ------------------------- | --- | --- | ------ |
| $t_{AA}$  | Dirección a Datos Válidos |     | 15  | ns     |

### Ancho de Pulso Mínimo (Minimum Pulse Widths)

![Imagen](https://media.wiki-power.com/img/20220809094924.png)

El ancho de pulso mínimo generalmente incluye el ancho de pulso mínimo bajo y el ancho de pulso mínimo alto y se utiliza para garantizar el valor mínimo operativo en la sincronización de pulsos. Las especificaciones se presentan de la siguiente manera:

| Parámetro | Descripción                    | Mín | Máx | Unidad |
| --------- | ------------------------------ | --- | --- | ------ |
| $t_{WL}$  | Tiempo Mínimo en Bajo de Reloj | 20  |     | ns     |
| $t_{WH}$  | Tiempo Mínimo en Alto de Reloj | 25  |     | ns     |

### Frecuencia Máxima (Maximum Frequency)

![Imagen](https://media.wiki-power.com/img/20220809094934.png)

La "Máxima Frecuencia de Trabajo" se refiere coloquialmente a la velocidad máxima a la que un dispositivo puede funcionar. En la hoja de especificaciones se presenta de la siguiente manera:

| Parámetro | Descripción                | Mín. | Máx. | Unidad |
| --------- | -------------------------- | ---- | ---- | ------ |
| $f_{MAX}$ | Frecuencia de reloj máxima |      | 22.2 | MHz    |

### Tiempo de Habilitación de Salida (Output Enable Time)

![Imagen](https://media.wiki-power.com/img/20220809094941.png)

Se refiere al tiempo necesario para que un pin cambie de un estado de alta impedancia (deshabilitado) a un nivel de accionamiento válido (alto o bajo), asegurando que el buffer de salida pueda cambiar el estado del pin en el tiempo especificado. Se calcula midiendo el intervalo de tiempo desde que se emite la señal de control hasta que se detecta el cambio en la salida conmutada. En la hoja de especificaciones se presenta de la siguiente manera:

| Parámetro | Descripción            | Mín. | Máx. | Unidad |
| --------- | ---------------------- | ---- | ---- | ------ |
| $t_{DOE}$ | OE LOW a Datos Válidos |      | 10   | ns     |

### Tiempo de Deshabilitación de Salida (Output Disable Time)

![Imagen](https://media.wiki-power.com/img/20220809094948.png)

Se refiere al tiempo necesario para que un pin cambie de un nivel de accionamiento válido (alto o bajo) a un estado de alta impedancia (deshabilitado), asegurando que el buffer de salida pueda cambiar el estado del pin en el tiempo especificado. Se calcula midiendo el intervalo de tiempo desde que se emite la señal de control hasta que se detecta el cambio en la salida conmutada. En la hoja de especificaciones se presenta de la siguiente manera:

| Parámetro  | Descripción             | Mín. | Máx. | Unidad |
| ---------- | ----------------------- | ---- | ---- | ------ |
| $t_{HZOE}$ | OE HIGH a Datos Válidos |      | 8    | ns     |

## Parámetros de Temporización

### Temporización del Ciclo de Lectura (Read Cycle Timing)

Un ejemplo de temporización de ciclo de lectura para una memoria RAM estática de 256 x 4:

![Imagen](https://media.wiki-power.com/img/20220731190300.png)

| Parámetro  | Descripción                         | Mín. | Máx. | Unidad |
| ---------- | ----------------------------------- | ---- | ---- | ------ |
| $t_{RC}$   | Tiempo de Ciclo de Lectura          | 15   |      | ns     |
| $t_{AA}$   | Dirección a Datos Válidos           |      | 15   | ns     |
| $t_{ACS}$  | Selección de Chip a Datos Válidos   |      | 10   | ns     |
| $t_{DOE}$  | OE LOW a Datos Válidos              |      | 10   | ns     |
| $t_{HZCS}$ | Selección de Chip a Alta Impedancia |      | 8    | ns     |
| $t_{HZOE}$ | OE HIGH a Alta Impedancia           |      | 8    | ns     |
| $t_{LZCS}$ | Selección de Chip a Baja Impedancia | 2    |      | ns     |
| $t_{LZOE}$ | OE LOW a Baja Impedancia            | 2    |      | ns     |

```markdown
1. El primer paso es determinar la duración del ciclo de escritura a partir del parámetro $t_{RC}$.
2. Identificar qué señal controla la función de escritura. En el ejemplo de la imagen de arriba, la salida de datos de la RAM está controlada por el flanco descendente de OE.

### Temporización del Ciclo de Escritura (Write Cycle Timing)

Un ejemplo de ciclo de escritura para una RAM estática de 256 x 4:

![](https://media.wiki-power.com/img/20220731190328.png)

| Parámetro  | Descripción                                           | Mínimo | Máximo | Unidad |
| ---------- | ----------------------------------------------------- | ------ | ------ | ------ |
| $t_{WC}$   | Tiempo del Ciclo de Escritura                         | 15     |        | ns     |
| $t_{HZWE}$ | WE de Bajo a Alta Impedancia                          |        | 8      | ns     |
| $t_{LZWE}$ | WE de Alto a Bajo Impedancia                          | 2      |        | ns     |
| $t_{PWE}$  | Ancho de Pulso de WE                                  | 11     |        | ns     |
| $t_{SD}$   | Configuración de Datos al Final de la Escritura       | 11     |        | ns     |
| $t_{HD}$   | Retención de Datos desde el Final de la Escritura     | 1      |        | ns     |
| $t_{SA}$   | Configuración de Dirección al Inicio de la Escritura  | 2      |        | ns     |
| $t_{HA}$   | Retención de Dirección desde el Final de la Escritura | 2      |        | ns     |
| $t_{SCS}$  | CS de Bajo a Final de Escritura                       | 11     |        | ns     |
| $t_{AW}$   | Configuración de Dirección al Final de la Escritura   | 13     |        | ns     |

1. El primer paso es determinar la duración del ciclo de escritura a partir del parámetro $t_{WC}$.
2. Identificar qué señal controla la función de escritura. En el ejemplo de la imagen de arriba, la entrada de datos en la RAM está controlada por el flanco ascendente de WE.

## Referencias y Agradecimientos

- "Los Fundamentos de la Prueba de Semiconductores Digitales"
```

Nota: He mantenido el formato Markdown y he realizado las traducciones manteniendo la claridad y precisión del contenido original.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
