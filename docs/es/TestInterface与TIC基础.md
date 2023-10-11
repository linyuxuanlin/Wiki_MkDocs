# Test Interface y Fundamentos de TIC

En las pruebas de semiconductores, **TIC (Test Interface Controller, Controlador de Interfaz de Prueba)** es un controlador principal de bus que sigue el protocolo de **Interfaz de Prueba** en la especificación de **AMBA (Advanced Microcontroller Bus Architecture, Arquitectura de Bus de Microcontrolador Avanzado)**. AMBA es un estándar de comunicación en chip para microcontroladores integrados que incluye tres tipos de protocolos de bus:

- **AHB** (Advanced High-performance Bus, Bus de Alto Rendimiento)
- **ASB** (Advanced System Bus, Bus del Sistema)
- **APB** (Advanced Peripheral Bus, Bus Periférico Avanzado)

Dado que la filosofía de AMBA es aislar las pruebas de cada módulo individual en el sistema, cada prueba de módulo depende solo de la interfaz del bus, por lo que se necesita un método de prueba para probar las entradas y salidas de los periféricos no conectados al bus.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262214877.png)

Este método de prueba se puede implementar a través de la Interfaz de Prueba. Utiliza un simple protocolo de tres vías para controlar la lectura y escritura de vectores; al mismo tiempo, utiliza la **EBI (External Bus Interface, Interfaz de Bus Externo)** como ruta de datos para importar vectores externos a los buses internos.

## Pines de la Interfaz de Prueba

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202308262225257.png)

Como se puede ver en la figura anterior, los pines de la Interfaz de Prueba constan de tres partes:

- Un pin de reloj **TCLK**
- Tres pines de control **TREQA**, **TREQB** y **TACK**
- Un bus de prueba de 32 bits **TBUS[31:0]**

En la configuración mínima, la Interfaz de Prueba solo necesita TREQA y TACK como **pines dedicados** para controlar la entrada y salida del modo de prueba. Otros pines se pueden implementar mediante la reutilización de pines en el dispositivo.

**TREQA/TREQB (Test Bus Request, Solicitud de Bus de Prueba)** es una señal de **entrada**. Durante el funcionamiento normal del sistema, TREQA se utiliza para solicitar el modo de prueba, lo que permite cargar vectores. Durante el proceso de prueba, TREQA y TREQB se utilizan juntos para indicar el tipo de vector que se utilizará en el siguiente ciclo.

**TACK (Test Bus Acknowledge, Confirmación de Bus de Prueba)** es una señal de **salida** que indica el estado del bus y cuándo se completa una prueba. Cuando TACK está en bajo, indica que el vector actual necesita más tiempo hasta que TACK se vuelva alto. Solo cuando TACK está en alto, TREQA/TREQB leerán las señales de control externas.

**TCLK (Test Clock)** es una señal de reloj de entrada. El reloj de prueba de la Interfaz de Prueba se proporciona desde el exterior. Al cambiar entre el modo normal y el modo de prueba, se requiere que el reloj TCLK no tenga bordes.

**TBUS[31:0] (Test Bus)** es un bus de interfaz de prueba bidireccional de 32 bits. En el estado de entrada, se utiliza para transmitir la dirección del vector, la información de control y la operación de escritura; en el estado de salida, se puede utilizar para realizar operaciones de lectura. Cuando se necesita cambiar el estado de entrada/salida de TBUS, el protocolo de bus de prueba garantiza un ciclo para cambiar la dirección.

Cuando el sistema está funcionando normalmente, la tabla de verdad controlada por tres líneas de la Interfaz de Prueba es la siguiente:

| TREQA | TREQB | TACK | Estado                                      |
| ----- | ----- | ---- | ------------------------------------------- |
| 0     | 0     | 0    | Funcionamiento normal, no en modo de prueba |
| 1     | 0     | 0    | Solicita entrar en modo de prueba           |
| 0     | 1     | 0    | Reservado para solicitudes de host externo  |
| -     | -     | 1    | Ya se encuentra en modo de prueba           |

Inicialmente, TREQA está en bajo nivel, lo que indica que aún no se ha entrado en el modo de prueba. Cuando TREQA se establece en alto nivel, se solicita entrar en el modo de prueba. Luego, cuando TACK emite un nivel alto, indica que TIC permite entrar en el modo de prueba. En este momento, TCLK se convierte en la fuente de reloj interno. Una vez que se entra en el modo de prueba, los valores en las tres líneas y los estados del sistema correspondientes son los siguientes:

| TREQA | TREQB | TACK | Estado                                          |
| ----- | ----- | ---- | ----------------------------------------------- |
| -     | -     | 0    | La operación actual aún no se ha completado     |
| 1     | 1     | 1    | Vector de dirección/control/cambio de dirección |
| 1     | 0     | 1    | Vector de prueba de escritura                   |
| 0     | 1     | 1    | Vector de prueba de lectura                     |
| 0     | 0     | 1    | Salir del modo de prueba                        |

A continuación, se puede establecer TREQB en alto para cargar el Vector de dirección. Luego, se pueden realizar operaciones de lectura/escritura. Cuando se necesita salir del modo de prueba, primero se debe ingresar un Vector de dirección para asegurarse de que todas las transferencias internas se hayan completado. Luego, se deben establecer TREQA y TREQB en bajo nivel para indicar que se está saliendo del modo de prueba. Finalmente, TACK emitirá un nivel bajo, indicando que se ha salido del modo de prueba.

## Tipos de Vector

En la interfaz de prueba, hay cinco tipos de Vector:

- **Vector de dirección**: Vector que declara la dirección.
- **Vector de prueba de escritura**: Vector que se escribe (0/1).
- **Vector de prueba de lectura**: Vector que se lee (L/H).
- **Vector de control**: Vector de control.
- **Vector de cambio de dirección**: Vector de cambio de dirección.

La activación de los vectores de dirección/control/cambio de dirección depende del valor común de TREQA/TREQB. Para determinar el tipo de Vector, se pueden seguir las siguientes reglas:

- Si solo aparece un Vector de dirección/control/cambio de dirección, entonces es un Vector de dirección.
- Si aparece una serie continua de vectores de dirección/control/cambio de dirección, excepto el último que es un Vector de control, entonces todos son vectores de dirección.
- Después de uno o varios vectores de lectura, siempre habrá un Vector de cambio de dirección. (En ASB es uno, en AHB son dos).

Además, el **Vector de ráfaga** es una serie de varios vectores de prueba de escritura/lectura concatenados (todos del mismo tipo, no mezclados). De esta manera, solo se necesita aplicar una dirección, lo que acelera la prueba. Esta dirección puede mantenerse estática (todos los vectores usan la misma dirección inicial transmitida) o puede ser una dirección incremental (dependiendo de si TIC tiene un incrementador de dirección habilitado). Si no hay un incrementador de dirección, se utilizará una dirección estática de forma predeterminada.

### Vector de dirección

Antes de cualquier operación de lectura/escritura, se debe pasar el Vector de Dirección. Sigue las siguientes reglas:

- TREQA/TREQB deben establecerse en 1 para indicar que el siguiente ciclo es el Vector de Dirección.
- En el siguiente ciclo, la Dirección se carga en TBUS[31:0]. En este momento, los valores en TREQA/TREQB determinarán conjuntamente el estado del siguiente ciclo.

En algunos sistemas de señal de alta velocidad, puede ser necesario cargar múltiples Vectores de Dirección consecutivos (aumentando suficiente tiempo para que la Dirección se transfiera desde el exterior al bus de Dirección interno). En este caso, TIC forzará la carga del segundo ciclo del Vector de Dirección cuando la salida TACK del primer Vector de Dirección sea 0.

### Vector de Control

El Vector de Control siempre seguirá a uno o varios Vectores de Dirección y se utiliza para actualizar la información de Control interna de TIC. Sigue las siguientes reglas:

- TREQA/TREQB deben establecerse en 1 para indicar que el siguiente ciclo es el Vector de Dirección.
- En el siguiente ciclo, la Dirección se carga en TBUS[31:0]. En este momento, TREQA/TREQB seguirán siendo 1 y el Vector de Control aparecerá en el siguiente ciclo.
- En el siguiente ciclo, la información de Control se cargará en TBUS[31:0]. En este momento, los valores en TREQA/TREQB determinarán el estado del siguiente ciclo.

Si se necesita establecer un Vector de Control inválido, se puede establecer el bit 0 en 0 para mantener la información del Vector de Control pero no aplicarla.

### Vector de Prueba de Escritura

Después de ingresar con éxito en el modo de prueba y especificar la Dirección, se pueden realizar operaciones de lectura/escritura. La Dirección utilizada para la operación de escritura se define en el Vector de Dirección anterior. El Vector de Prueba de Escritura puede seguir a los siguientes Vectores:

- Un solo Vector de Dirección.
- Una secuencia de Vectores de Dirección/Control.
- Otro Vector de Prueba de Escritura. Formando una ráfaga de escritura.
- El Vector de TurnAround después de una operación de lectura única/múltiple.

Cuando se necesita retrasar el estado de transferencia, TACK se vuelve bajo. Durante este tiempo de espera, TREQA/TREQB deben cambiar para especificar el tipo de Vector siguiente, pero la operación de escritura en TBUS[31:0] debe continuar y no se deben realizar operaciones de lectura.

### Vector de Prueba de Lectura

Similar al Vector de Prueba de Escritura, la operación de lectura utiliza la Dirección definida por el Vector anterior y puede seguir a los siguientes Vectores:

- Un solo Vector de Dirección.
- Una secuencia de Vectores de Dirección/Control.
- Otro Vector de Prueba de Lectura. Formando una ráfaga de lectura.
- Una operación de escritura única/múltiple.

Después de una operación de lectura única o múltiple, siempre debe haber un Vector de TurnAround para evitar conflictos en la señal TBUS externa.

### Vector de TurnAround

El Vector de TurnAround se puede utilizar para cambiar la dirección de transferencia de TBUS al cambiar entre operaciones de escritura/lectura. Es necesario insertar un Vector de TurnAround cuando se cambia de una operación de lectura a una de escritura. Esta operación no escribirá una nueva Dirección.

---

Estos son algunos conocimientos básicos sobre la Interfaz de Prueba y TIC. Para obtener información específica sobre el funcionamiento de TIC en AHB, consulte el siguiente artículo [**TIC en AHB**](https://wiki-power.com/es/AHB%E4%B8%8A%E7%9A%84TIC) (en proceso de escritura...).

## Referencias y Agradecimientos

- _IHI0011 - ARM advanced microcontroller bus architecture (AMBA) specification.Rev 2.0_

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
