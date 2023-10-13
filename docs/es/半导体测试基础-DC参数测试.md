# Fundamentos de prueba de semiconductores - Prueba de parámetros DC

La prueba de parámetros DC mide principalmente algunas características de un solo pin en el dispositivo. Para la mayoría de los parámetros DC, esencialmente se está midiendo la resistividad del semiconductor, y la ley de Ohm se utiliza para explicar la resistividad. Si se necesita verificar la viabilidad del proceso de prueba DC, también se puede utilizar un resistor para equivaler al DUT y descartar problemas fuera del DUT. Por ejemplo, para el parámetro VOL que aparece en la hoja de especificaciones del chip:

| Parámetro | Descripción       | Condiciones de prueba  | Min | Max | Unidades |
| --------- | ----------------- | ---------------------- | --- | --- | -------- |
| VOL       | Voltaje de salida | VDD = Min, IOL = 8.0mA |     | 0.4 | V        |

Podemos ver que el valor máximo de VOL es 0.4V, IOL es 8mA, lo que significa que cuando se produce una corriente de 8mA en una situación de nivel bajo lógico de salida, debe ser a un voltaje no superior a 0.4V, por lo que podemos concluir que la resistencia máxima del dispositivo no supera los 50Ω. Por lo tanto, se puede utilizar una resistencia no superior a 50Ω para reemplazar el DUT y verificar el proceso de prueba. Nuestro objetivo es centrar el problema en el DUT, no en problemas fuera del DUT.

## IDD y Gross IDD

IDD representa la corriente (I) desde el drenador (D) hasta el drenador (D) en un circuito CMOS, y si es un circuito TTL, se llama ICC (corriente desde el colector hasta el colector). Gross IDD se refiere a la corriente total que fluye hacia el pin VDD (se puede probar en la etapa de prueba de Wafer Probe o producto terminado). IDD se utiliza para verificar si la corriente total del chip cumple con las especificaciones, generalmente se debe verificar la corriente en el consumo de energía mínimo y la frecuencia de trabajo máxima.

La prueba de Gross IDD se realiza para determinar si se puede continuar probando el DUT. Por lo general, esta prueba se realiza inmediatamente después de la prueba del sistema operativo y es la primera prueba después de que el DUT se enciende. Si la prueba de Gross IDD no pasa (como una corriente demasiado grande), entonces no se puede continuar probando.

Durante la etapa de prueba de Gross IDD, aún no se sabe si el preprocesamiento se puede realizar normalmente, por lo que se debe relajar la especificación de IDD. Después de que la prueba de Gross IDD pase, se puede definir con precisión la corriente de especificación de IDD mediante el programa de preprocesamiento.

La prueba de Gross IDD debe comenzar con un reinicio para establecer todos los pines de entrada en un nivel bajo / alto. Por lo general, VIL se establece en 0V y VIH se establece en VDD, y todos los pines de salida están en carga libre (para evitar la corriente de fuga flotante que aumenta IDD). El diagrama de prueba es el siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20220728162655.png)

Algunos puntos a tener en cuenta:

- Se debe establecer un pinza de corriente para evitar dañar el equipo de prueba debido a una corriente demasiado grande.
- Si hay corriente negativa, también significa que la prueba no pasa.
- Si hay un error en la prueba, primero se debe descartar el problema del equipo de prueba. Si se ejecuta la prueba con el zócalo vacío, la corriente debería ser 0, de lo contrario, significa que otros dispositivos fuera del DUT también están consumiendo corriente.

### Prueba IDD - Método estático

La prueba IDD estática mide la corriente total que fluye hacia el pin VDD y generalmente requiere que el DUT funcione en modo de consumo de energía mínimo. La diferencia entre la prueba IDD estática y la prueba de Gross IDD es que la prueba de Gross IDD aún no tiene un programa de preprocesamiento y es una prueba aproximada, mientras que la prueba IDD estática ya tiene un modo de preprocesamiento y se realiza después del preprocesamiento.

Por ejemplo, la siguiente tabla es una muestra de parámetros IDD:

| Parámetro    | Descripción               | Condiciones de prueba               | Min | Max | Unidades |
| ------------ | ------------------------- | ----------------------------------- | --- | --- | -------- |
| IDD estática | Corriente de alimentación | VDD = 5.25V, entradas = VDD, Iout=0 |     | +22 | µA       |

El diagrama de prueba IDD estática es el siguiente:

El proceso de prueba es el siguiente:

1. Configure el DUT con el vector de prueba para consumir la corriente mínima y mantenerse en estado estático.
2. Verifique el valor de corriente de los pines
   - Mayor que IDD Spec: Fail
   - Otro rango: Pass

Durante la prueba, generalmente se requiere un retraso entre la alimentación y la toma de muestras para permitir que los capacitores parásitos se carguen y evitar interferencias.

Si necesita probar la corriente estática en diferentes lógicas, puede medir el parámetro IDDQ para aumentar la cobertura de prueba (IDDQ mide la corriente en un estado lógico estático, como probar un estado con algunos MOSFET abiertos).

### Prueba IDD - Método dinámico

El propósito de la prueba dinámica IDD es medir la corriente consumida por el DUT durante la **ejecución dinámica de la función** (generalmente a la máxima frecuencia del DUT) para garantizar que no supere el valor nominal.

Por ejemplo, la siguiente tabla es una muestra de parámetros IDD dinámicos:

| Parámetro    | Descripción             | Condiciones de prueba                      | Min | Max | Unidades |
| ------------ | ----------------------- | ------------------------------------------ | --- | --- | -------- |
| IDD Dinámico | Corriente de suministro | VDD = 5.25V (comercial), f = f_max (66MHz) |     | +18 | mA       |

Diagrama de prueba:

![](https://img.wiki-power.com/d/wiki-media/img/20220728171447.png)

El proceso de prueba es similar al método estático.

## VOL/IOL & VOH/IOH

VOL representa la limitación de voltaje máximo cuando se produce una salida de nivel bajo (L) (no se reconocerá como lógica 1). IOL representa la capacidad de conducción de corriente de drenaje (I, sink) cuando se produce una salida de nivel bajo (L). Juntos miden la impedancia del pin del buffer cuando se produce una salida de nivel bajo para garantizar que pueda absorber un valor constante de corriente en el voltaje de salida adecuado.

VOH representa la limitación de voltaje mínimo cuando se produce una salida de nivel alto (H) (no se reconocerá como lógica 0). IOH representa la capacidad de conducción de corriente de fuente (I, source) cuando se produce una salida de nivel alto (H). Juntos miden la impedancia del buffer cuando se produce una salida de nivel alto para garantizar que pueda producir un valor constante de corriente en el voltaje de salida adecuado.

Por ejemplo, la siguiente tabla muestra los parámetros VOL/IOL y VOH/IOH de una RAM estática de 256 x 4:

| Parámetro | Descripción            | Condiciones de prueba     | Min | Max | Unidades |
| --------- | ---------------------- | ------------------------- | --- | --- | -------- |
| VOL       | Voltaje de salida bajo | VDD = 4.75V, IOL = 8.0mA  |     | 0.4 | V        |
| VOH       | Voltaje de salida alto | VDD = 4.75V, IOH = -5.2mA | 2.4 |     | V        |

La prueba de VOL/IOL y VOH/IOH se realiza principalmente para verificar si VOL/VOH está en el nivel correcto cuando se aplica corriente de fuente o drenaje (si puede alcanzar el umbral de voltaje en la corriente de salida adecuada). Hay dos métodos de prueba: estático y dinámico. **El método estático aplica corriente a los pines y luego mide el voltaje uno por uno; el método dinámico proporciona VREF durante la prueba de función para formar una corriente de carga dinámica y luego mide el voltaje.**

### Prueba VOL/IOL - Método estático en serie

El diagrama de prueba de VOL/IOL utilizando el método estático en serie es el siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20220728150542.png)

El proceso de prueba es el siguiente:

## Pruebas de VOH/IOH - Método estático en serie

El diagrama de prueba para medir VOH/IOH utilizando el método estático en serie es el siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20220728143124.png)

El proceso de prueba es el siguiente:

1. Primero, se debe configurar el pin de prueba como una salida de nivel alto mediante preprocesamiento.
2. Se aplica IOH constante al pin y se espera de 1 a 5 milisegundos antes de medir (según la configuración de delay en el PMU).
3. Se mide el voltaje del pin.
   - Si es mayor que VOL (+0.4V): Fail
   - En cualquier otro rango: Pass

Consideraciones importantes:

- IOL es un valor de corriente positiva, ya que fluye desde el PMU hacia el DUT.
- Debido a que se aplica una corriente constante, se debe configurar un clamp de voltaje. Si se mide un voltaje más bajo que el voltaje del clamp, es posible que la lógica del pin se haya configurado como un nivel alto, lo que activa el diodo de protección de la fuente.
- El parámetro VDDmin indica el voltaje mínimo de suministro de energía que permite que el DUT se pruebe correctamente. Si es menor, no se pueden obtener resultados de prueba precisos.

## IIL/IIH

IIL se refiere a la corriente máxima de pull-up permitida (I, source, desde VSS del DUT a través del pin hacia el exterior) cuando la lógica del pin de entrada (I) es un nivel bajo (L). Esto se utiliza para verificar si la corriente de fuga del pin al suministro de energía está dentro de los límites y para verificar el grado de aislamiento. IIH se refiere a la corriente máxima de pull-down permitida (I, sink, desde VDD del DUT a través del pin hacia el exterior) cuando la lógica del pin de entrada (I) es un nivel alto (H). Por ejemplo, los parámetros IIL y IIH para una RAM estática de 256 x 4 son los siguientes:

| Parámetro | Descripción                   | Condiciones de prueba  | Mínimo | Máximo | Unidades |
| --------- | ----------------------------- | ---------------------- | ------ | ------ | -------- |
| IIL, IIH  | Corriente de carga de entrada | Vss ≤ Vin ≤ VDD(5.25V) | -10    | +10    | µA       |

IIL mide la resistencia del pin de entrada al suministro de energía VDD; IIH mide la resistencia del pin de entrada a VSS. Esta prueba se utiliza para garantizar que la impedancia de entrada cumpla con los requisitos de diseño y que la corriente de entrada no exceda los límites. IIL/IIH se pueden medir mediante métodos en serie, paralelos o combinados, así como mediante pruebas de función. El método en serie prueba los pines uno por uno, lo que es preciso pero relativamente lento.

Además, las pruebas de IIL/IIH generalmente solo se pueden realizar en pines de entrada pura. Si se encuentra un pin bidireccional, se debe agregar una carga de salida para estabilizar el nivel alto o bajo y evitar que se genere corriente en los dispositivos de protección, lo que afectaría los resultados de la prueba.

### Pruebas de IIL/IIH - Método estático en serie

El diagrama de prueba para medir IIL en pines de entrada utilizando el método estático en serie es el siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20220729100620.png)

El proceso de prueba es el siguiente:

1. Primero, se debe suministrar la fuente de alimentación VDDmax (peor caso) al DUT.
2. Se configuran todos los pines de entrada del DUT en nivel alto (VIH).
3. Se baja un solo pin de entrada a VSS utilizando el PMU.
4. Se espera de 1 a 5 microsegundos y se mide el valor de corriente.
   - Si es menor que IIL (-10µA): Fail (la corriente que fluye hacia el DUT excede los límites)
   - En cualquier otro rango: Pass

El diagrama de prueba para medir IIH en pines de entrada utilizando el método estático en serie es el siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20220729100739.png)

El proceso de prueba es el siguiente:

# Pruebas de IIL/IIH

## Método estático en serie

1. Proporcionar la fuente de alimentación VDDmax al DUT.
2. Establecer todos los pines de entrada del DUT en nivel bajo (VIL).
3. Usar PMU para elevar un solo pin de entrada a VDDmax.
4. Esperar de 1 a 5 microsegundos y medir la corriente.
   - Si es mayor que IIH (+10µA): Fail (la corriente que sale del DUT es demasiado alta)
   - En otros intervalos: Pass

## Método estático en paralelo

En algunos sistemas de prueba, se puede medir la corriente de fuga en paralelo (Método de prueba paralela). La medición de corriente de fuga en paralelo implica la medición de múltiples pines con múltiples PMU, donde todos los pines de entrada se elevan a un nivel alto y se mide la corriente de cada pin en paralelo. Luego, los resultados se comparan con los valores nominales para obtener una conclusión.

1. Proporcionar la fuente de alimentación VDDmax al DUT.
2. Usar múltiples PMU para elevar cada pin de entrada a VDDmax (medir IIH).
3. Esperar de 1 a 5 microsegundos y medir la corriente para obtener una conclusión.
4. Luego, bajar a VSS y repetir los pasos anteriores para medir IIL.

La característica del método en paralelo es que se pueden medir rápidamente las corrientes individuales de cada pin de entrada. La desventaja es que es más difícil detectar las fugas entre los pines de entrada, ya que todos los pines se mantienen en el mismo nivel.

## IOZL/IOZH

La corriente de alta impedancia IOZ se refiere a la corriente de fuga (I) de un pin de salida (O) en estado de alta impedancia (Z). IOZL se refiere a la corriente de fuga en el estado de nivel bajo (L) del pin, mientras que IOZH se refiere a la corriente de fuga en el estado de nivel alto (H) del pin. Se utiliza para verificar si la corriente de fuga está dentro de los límites cuando se apaga el pin de salida de doble dirección o de alta impedancia.

Este parámetro garantiza que los pines de salida bidireccionales o de alta impedancia se puedan apagar correctamente (estado de alta impedancia de salida). IOZL mide la resistencia del pin a VDD en estado de alta impedancia de salida, mientras que IOZH mide la resistencia del pin a VSS. Por lo general, se expresa en las especificaciones de la siguiente manera:

| Parámetro | Descripción                            | Condiciones de prueba                      | Mínimo | Máximo | Unidades |
| --------- | -------------------------------------- | ------------------------------------------ | ------ | ------ | -------- |
| IOZ       | Corriente de salida de alta impedancia | VSS ≤ Vout ≤VDD(5.25V), Salida desactivada | -2.0   | +2.0   | µA       |

## Método estático en serie

1. Proporcionar la fuente de alimentación VDD al dispositivo.
2. Establecer los pines del dispositivo en estado de alta impedancia y usar PMU para forzar el pin a un estado alto o bajo.
3. Medir la corriente del pin.
   - Si es menor que -IOZ (-2µA): Fail
   - Si es mayor que +IOZ (+2µA): Fail
   - En otros intervalos: Pass

La ventaja de la prueba en serie es que se puede medir con precisión la corriente de cada pin. La desventaja es que es lenta y requiere la configuración de la corriente de pinza.

## Método estático en paralelo

El método estático en paralelo implica el uso de múltiples PMU para medir múltiples pines en paralelo. No se profundizará en este método aquí, pero su ventaja es la velocidad.

La pinza de voltaje de entrada VI se refiere al voltaje medido en el pin de entrada (I) de un dispositivo TTL (no CMOS) cuando se aplica una corriente negativa (corriente de extracción) en el pin. El propósito de esta prueba es **verificar la integridad del diodo de pinza entre el emisor del transistor y la tierra**. Se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción                 | Condiciones de prueba  | Mín | Máx  | Unidades |
| --------- | --------------------------- | ---------------------- | --- | ---- | -------- |
| VI        | Voltaje de pinza de entrada | VCC = Min, Iin = -18mA |     | +1.5 | V        |

### Prueba VI - Método estático en serie

La prueba VI estática en serie se realiza de la siguiente manera:

![](https://img.wiki-power.com/d/wiki-media/img/20220729145425.png)

El proceso de prueba es el siguiente:

1. Asegurarse de que es un pin de entrada de un dispositivo TTL y suministrar energía a VCCmin.
2. Después de configurar la pinza de voltaje, utilizar PMU para extraer una corriente de -15mA~-20mA.
3. Medir el voltaje en el pin:
   - Por debajo de VI (-1.5V): Fallo
   - En cualquier otro rango: Aprobado

## IOS (Corriente de cortocircuito de salida)

La corriente de cortocircuito de salida indica la corriente (I) generada en el pin de salida (O) cuando se produce un cortocircuito (S). El propósito es **medir la impedancia de salida cuando el pin de salida está en un estado alto pero se cortocircuita a cero voltios, para asegurarse de que la corriente de salida no sea demasiado alta en las peores condiciones de carga, y también indica la corriente máxima instantánea que el pin DUT puede proporcionar para cargar la carga capacitiva, lo que se puede utilizar para calcular el tiempo de subida**. IOS se representa en las especificaciones de la siguiente manera:

| Parámetro | Descripción                          | Condiciones de prueba                                                                         | Mín | Máx | Unidades |
| --------- | ------------------------------------ | --------------------------------------------------------------------------------------------- | --- | --- | -------- |
| IOS       | Corriente de cortocircuito de salida | Vout = 0V, VDD = 5.25V, \*Solo cortocircuitar una salida a la vez durante no más de 1 segundo | -85 | -30 | mA       |

### Prueba IOS - Método estático en serie

La prueba IOS estática en serie se realiza de la siguiente manera:

![](https://img.wiki-power.com/d/wiki-media/img/20220729152549.png)

El proceso de prueba es el siguiente:

1. Suministrar energía a VDDmax, preparar el dispositivo para que el pin de salida tenga un estado alto.
2. Utilizar PMU para bajar el pin a 0V, medir la corriente de salida y compararla con el valor nominal para obtener una conclusión.

En la prueba de IOS, se necesita una lógica razonable para evitar el cambio térmico. En primer lugar, se debe configurar PMU en el modo de medición de voltaje de corriente cero forzado, conectarlo a la salida DUT, medir y guardar el voltaje VOH de DUT, luego desconectarlo y configurar PMU para subir a VOH justo, y luego volver a conectar DUT (en este momento, ambos extremos tienen el mismo voltaje de VOH), y luego bajar PMU a 0V para medir el valor de corriente. Después de completar la medición, PMU debe volver a subir a VOH antes de desconectarlo. De esta manera, se puede garantizar que cuando el relé cambia de estado, los voltajes en ambos extremos sean consistentes.

Factores que pueden causar una prueba fallida:

- **Exceder el límite superior**
  - La impedancia de salida es demasiado alta, lo que resulta en una corriente absoluta insuficiente.
  - La abrazadera en sí tiene resistencia.
  - No se ha realizado el pretratamiento correcto.
- **Por debajo del límite inferior**
  - La impedancia de salida es demasiado baja, lo que resulta en una corriente absoluta demasiado alta.

Algunos pines de entrada pueden tener una estructura activa de pull-up o pull-down, lo que requiere garantizar que la ruta de resistencia de pull-up/down del buffer de entrada esté funcionando correctamente. Solo se puede probar en serie, ya que la estructura de pull-up/down interna de diferentes pines puede ser diferente. Diagrama esquemático de la estructura del pin:

![](https://img.wiki-power.com/d/wiki-media/img/20220729130655.png)

## Capacidad de ventilador de salida (Output Fanout)

La capacidad de ventilador (Fanout) se refiere a la capacidad del pin de salida para conducir varios pines de entrada según sus parámetros de voltaje y corriente. Es decir, la capacidad de conducción del pin es un indicador de cuántos pines de entrada puede conducir un pin de salida.

![](https://img.wiki-power.com/d/wiki-media/img/20220729132621.png)

Como se muestra en la figura anterior, esta salida TTL puede elevar aproximadamente 17 pines de entrada o bajar 30 pines de entrada. En las especificaciones del pin, los parámetros se expresan de la siguiente manera:

| Parámetro | Descripción                        | Condiciones de prueba     | Mínimo | Máximo | Unidades |
| --------- | ---------------------------------- | ------------------------- | ------ | ------ | -------- |
| VOH       | Voltaje alto de salida             | VCC = 4.75V, IOH = -2.6mA | 2.4    |        | V        |
| VOL       | Voltaje bajo de salida             | VCC = 4.75V, IOH = 24mA   |        | 0.4    | V        |
| IIL       | Corriente de carga baja de entrada | Vin = 0.4V                | -800   |        | µA       |
| IIH       | Corriente de carga alta de entrada | Vin = 2.4V                |        | 150    | µA       |

La capacidad de ventilador varía mucho entre los dispositivos TTL y CMOS, ya que la impedancia de entrada de CMOS es alta, teóricamente una salida CMOS puede conducir cualquier número de entradas CMOS. Pero los pines de entrada CMOS tienen capacitancia parásita, cuanto más se conectan las entradas, mayor es la capacitancia, lo que produce un efecto de carga y descarga de la capacitancia al cambiar entre los niveles alto y bajo, lo que produce una demora.

## Referencias y agradecimientos

- "The Fundamentals Of Digital Semiconductor Testing"
- "DC Test Theory"

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
