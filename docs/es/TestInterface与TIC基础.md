# Test Interface y TIC básico

En las pruebas de semiconductores, **TIC (Test Interface Controller, controlador de interfaz de prueba)** es un controlador principal de bus que sigue el protocolo de **Interfaz de Prueba** de la especificación **AMBA (Advanced Microcontroller Bus Architecture, arquitectura avanzada de bus de microcontrolador)**. AMBA es un estándar de comunicación en chip para microcontroladores integrados que incluye tres tipos de protocolos de bus:

- **AHB** (Advanced High-performance Bus, bus de alto rendimiento)
- **ASB** (Advanced System Bus, bus de sistema)
- **APB** (Advanced Peripheral Bus, bus periférico)

Dado que la filosofía de AMBA es realizar pruebas aisladas en módulos individuales del sistema, las pruebas de cada módulo solo dependen de la interfaz del bus, por lo que se necesita un método de prueba para probar las entradas y salidas de los dispositivos periféricos no conectados al bus.

![](https://media.wiki-power.com/img/202308262214877.png)

Este método de prueba se puede lograr mediante la Interfaz de Prueba. Utiliza un sencillo protocolo de tres líneas para controlar la lectura y escritura de vectores; al mismo tiempo, utiliza la **EBI (External Bus Interface, interfaz de bus externo)** como ruta de datos para importar vectores externos al bus interno.

## Pines de la Interfaz de Prueba

![](https://media.wiki-power.com/img/202308262225257.png)

Como se muestra en la figura anterior, los pines de la Interfaz de Prueba constan de tres partes:

- Un pin de reloj **TCLK**
- Tres pines de control **TREQA**, **TREQB** y **TACK**
- Un bus de prueba de 32 bits **TBUS[31:0]**

En la configuración mínima, la Interfaz de Prueba solo necesita TREQA y TACK como **pines dedicados** para controlar la entrada y salida del modo de prueba. Los otros pines se pueden implementar mediante la reutilización de pines en el dispositivo.

**TREQA/TREQB (Test Bus Request, solicitud de bus de prueba)** es una señal de **entrada**. Durante el funcionamiento normal del sistema, TREQA se utiliza para solicitar entrar en el modo de prueba y permitir la carga de vectores. Durante el proceso de prueba, TREQA se utiliza junto con TREQB para indicar el tipo de vector que se utilizará en el próximo ciclo.

**TACK (Test Bus Acknowledge, confirmación de bus de prueba)** es una señal de **salida** que indica el estado del bus y cuándo se completa una prueba. Cuando TACK está en nivel bajo, indica que el vector actual necesita más tiempo hasta que TACK se vuelva alto. Solo cuando TACK está en nivel alto, TREQA/TREQB leerán las señales de control externas.

**TCLK (Test Clock)** es una señal de reloj de entrada. El reloj de prueba de la Interfaz de Prueba es proporcionado externamente. Al cambiar entre el modo normal y el modo de prueba, se requiere que el reloj TCLK no tenga fluctuaciones.

**TBUS[31:0] (Test Bus)** es un bus de interfaz de prueba bidireccional de 32 bits. En el estado de entrada, se utiliza para transmitir la dirección del vector, la información de control y realizar operaciones de escritura; en el estado de salida, se puede utilizar para realizar operaciones de lectura. Cuando se necesita cambiar el estado de entrada/salida de TBUS, el protocolo del bus de prueba garantiza proporcionar un ciclo de cambio de dirección.

Cuando el sistema está en funcionamiento normal, la tabla de verdad controlada por las tres líneas de la Interfaz de Prueba es la siguiente:

| TREQA | TREQB | TACK | Estado                                      |
| ----- | ----- | ---- | ------------------------------------------- |
| 0     | 0     | 0    | Funcionamiento normal, no en modo de prueba |
| 1     | 0     | 0    | Solicitar entrar en modo de prueba          |
| 0     | 1     | 0    | Reservado para solicitudes de host externo  |
| -     | -     | 1    | Entró en modo de prueba                     |

Inicialmente, TREQA está en nivel bajo, lo que indica que no se ha entrado en el modo de prueba. Cuando TREQA se establece en nivel alto, se solicita entrar en el modo de prueba. Luego, cuando TACK emite un nivel alto, indica que TIC permite entrar en el modo de prueba. En este momento, TCLK se convierte en la fuente de reloj interno. Una vez que se entra en el modo de prueba, los valores en las tres líneas y el estado del sistema correspondiente son los siguientes:

| TREQA | TREQB | TACK | Estado                                  |
| ----- | ----- | ---- | --------------------------------------- |
| -     | -     | 0    | La operación actual no se ha completado |
| 1     | 1     | 1    | Vector de dirección/control/turnaround  |
| 1     | 0     | 1    | Vector de prueba de escritura           |
| 0     | 1     | 1    | Vector de prueba de lectura             |
| 0     | 0     | 1    | Salir del modo de prueba                |

A continuación, se puede establecer TREQB en nivel alto para cargar el Vector de Dirección. Luego se pueden realizar operaciones de lectura y escritura. Cuando se necesita salir del modo de prueba, se debe ingresar primero un Vector de Dirección para asegurarse de que todas las transferencias internas se hayan completado. Luego, se establecen tanto TREQA como TREQB en nivel bajo para indicar que se está saliendo del modo de prueba. Finalmente, TACK emitirá un nivel bajo para indicar que se ha salido del modo de prueba.

## Tipos de Vector

En la Interfaz de Prueba, hay 5 tipos de Vector:

- **Vector de Dirección**: Vector que declara una dirección
- **Vector de Prueba de Escritura**: Vector de escritura (0/1)
- **Vector de Prueba de Lectura**: Vector de lectura (L/H)
- **Vector de Control**: Vector de control
- **Vector de Turnaround**: Vector de cambio de dirección

La activación de los Vectores de Dirección/Control/Turnaround se determina por los mismos valores comunes de TREQA/TREQB. Para determinar el tipo de Vector, se pueden seguir las siguientes reglas:

- Si solo hay un Vector de Dirección/Control/Turnaround: es un Vector de Dirección.
- Si hay una secuencia continua de Vectores de Dirección/Control/Turnaround: excepto el último, todos son Vectores de Dirección y el último es un Vector de Control.
- Después de uno o varios Vectores de Lectura: siempre habrá un Vector de Turnaround. (En ASB es uno solo, en AHB son dos)

Además, el **Vector de Ráfaga** es una secuencia de varios Vectores de Prueba de Escritura/Lectura juntos (todos del mismo tipo, no mezclados). Esto permite aplicar una dirección una sola vez y aumentar la velocidad de prueba. Esta dirección puede ser estática (todos los Vectores usan la misma dirección inicialmente ingresada) o incremental (dependiendo de si TIC tiene un incrementador de dirección habilitado). Si no hay un incrementador, se utilizará una dirección estática de forma predeterminada.

### Vector de Dirección

Antes de cualquier operación de lectura/escritura, es necesario pasar el Vector de Dirección. Sigue las siguientes reglas:

- Ambos TREQA/TREQB deben establecerse en 1 para indicar que el siguiente ciclo es el Vector de Dirección.
- En el siguiente ciclo, la Dirección se carga en TBUS[31:0]. En este momento, los valores de TREQA/TREQB determinarán conjuntamente el estado del siguiente ciclo.

En algunos sistemas de señales de alta velocidad, puede ser necesario cargar varios Vectores de Dirección de forma continua (para permitir suficiente tiempo para que la Dirección se transfiera desde el exterior hacia el bus de Dirección interno). En este caso, el TIC establecerá la salida TACK en 0 después del primer Vector de Dirección para forzar la carga del segundo Vector de Dirección en el siguiente ciclo.

### Vector de Control

El Vector de Control siempre sigue a uno o varios Vectores de Dirección. Se utiliza para actualizar la información de Control interna del TIC. Sigue las siguientes reglas:

- Ambos TREQA/TREQB deben establecerse en 1 para indicar que el siguiente ciclo es el Vector de Dirección.
- En el siguiente ciclo, la Dirección se carga en TBUS[31:0]. En este momento, tanto TREQA como TREQB se mantienen en 1, y el Vector de Control aparecerá en el siguiente ciclo.
- En el siguiente ciclo, la información de Control se carga en TBUS[31:0]. En este momento, los valores de TREQA/TREQB determinarán el estado del siguiente ciclo.

Si se necesita configurar un Vector de Control inválido, se puede establecer el bit 0 en 0 para preservar la información del Vector de Control pero no aplicarla.

### Vector de Prueba de Escritura

Una vez que se haya ingresado con éxito al modo de prueba y se haya especificado la Dirección, se pueden realizar operaciones de lectura/escritura. La operación de escritura utiliza la Dirección definida por el Vector de Dirección anterior. El Vector de Prueba de Escritura puede seguir a los siguientes Vectores:

- Un solo Vector de Dirección.
- Una secuencia de Vectores de Dirección/Control.
- Otro Vector de Prueba de Escritura. Formando una ráfaga de escritura.
- Vector de TurnAround después de una operación de lectura única/múltiple.

Cuando el estado de transferencia requiere un retraso, TACK se vuelve a nivel bajo. Durante este tiempo de espera, TREQA/TREQB debe cambiar para especificar el tipo de Vector siguiente, pero la operación de escritura en TBUS[31:0] debe continuar y no se deben realizar operaciones de lectura.

### Vector de Prueba de Lectura

Similar al Vector de Prueba de Escritura, la operación de lectura utiliza la Dirección determinada por el Vector anterior y puede seguir a los siguientes Vectores:

- Un solo Vector de Dirección.
- Una secuencia de Vectores de Dirección/Control.
- Otro Vector de Prueba de Lectura. Formando una ráfaga de lectura.
- Operación de escritura única/múltiple.

Después de una operación de lectura única o múltiple, siempre debe haber un Vector de TurnAround para evitar conflictos de bus en las señales TBUS externas.

### Vector de TurnAround

El Vector de TurnAround se utiliza para cambiar la dirección de transferencia en el bus TBUS al cambiar entre operaciones de escritura/lectura. Es necesario insertar un Vector de TurnAround cuando la operación de lectura se convierte en escritura. Esta operación no escribirá una nueva Dirección.

---

Estos son algunos conceptos básicos sobre la Interfaz de Prueba y el TIC. Para obtener información específica sobre el funcionamiento del TIC en AHB, consulte el siguiente artículo [**TIC en AHB**](https://wiki-power.com/AHB%E4%B8%8A%E7%9A%84TIC) (en proceso de redacción...).

## Referencias y Agradecimientos

- _IHI0011 - ARM advanced microcontroller bus architecture (AMBA) specification.Rev 2.0_

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
