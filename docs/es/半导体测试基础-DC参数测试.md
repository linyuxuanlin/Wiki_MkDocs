# Fundamentos de Pruebas de Parámetros DC en Semiconductores

Las pruebas de parámetros DC se centran principalmente en ciertas características de un solo pin en un dispositivo. Para la mayoría de los parámetros DC, es esencial medir la resistividad del semiconductor, y esto se logra mediante la Ley de Ohm. Para verificar la viabilidad del proceso de prueba DC, también se puede utilizar una resistencia equivalente al dispositivo bajo prueba (DUT) para descartar problemas fuera del DUT. Por ejemplo, en el caso del parámetro VOL que se encuentra en la hoja de especificaciones del chip:

| Parámetro | Descripción            | Condiciones de Prueba  | Mín | Máx | Unidades |
| --------- | ---------------------- | ---------------------- | --- | --- | -------- |
| VOL       | Tensión de Salida Baja | VDD = Mín, IOL = 8.0mA |     | 0.4 | V        |

Podemos observar que el valor máximo de VOL es 0.4V, con IOL igual a 8mA, lo que significa que cuando se genera una corriente de 8mA bajo un nivel lógico bajo de salida, la tensión no debe superar los 0.4V. Por lo tanto, podemos concluir que la resistencia máxima de este dispositivo no supera los 50Ω. Por lo tanto, se puede utilizar una resistencia de menos de 50Ω en lugar del DUT para verificar el proceso de prueba. Nuestro objetivo es centrar el problema en el DUT y no en cuestiones externas al DUT.

## IDD y IDD Bruto

IDD representa la corriente de drenaje (I) en circuitos CMOS desde el drenaje (D) hasta el drenaje (D), y en circuitos TTL se conoce como ICC (corriente de colector a colector). El IDD bruto se refiere a la corriente total que ingresa al pin VDD (se puede medir en las etapas de prueba de matriz o en la etapa de producto terminado). La prueba de IDD se utiliza para verificar si la corriente total del chip cumple con las especificaciones, generalmente se observa a la corriente en el mínimo consumo de energía y la frecuencia de funcionamiento máxima.

La prueba de IDD bruto se realiza para determinar si es posible continuar con la prueba del DUT. Por lo general, esta prueba sigue a la prueba del sistema operativo (OS) y es la primera prueba realizada después de que el DUT se energiza. Si la prueba de IDD bruto no se aprueba (por ejemplo, si la corriente es demasiado alta), no se puede continuar con las pruebas.

Durante la etapa de prueba de IDD bruto, aún no se sabe si el preprocesamiento se llevará a cabo de manera adecuada, por lo que se deben establecer especificaciones más flexibles para IDD. Una vez que la prueba de IDD bruto se aprueba, se pueden definir con precisión las corrientes de IDD especificadas a través del preprocesamiento.

La prueba de IDD bruto comienza con un restablecimiento para configurar todos los pines de entrada en niveles bajos o altos, generalmente VIL se configura en 0V y VIH en VDD. Todos los pines de salida se dejan en alto impedancia para evitar que una salida en alta impedancia cause una fuga de corriente que aumentaría IDD. El esquema de prueba se muestra a continuación:

![Esquema de Prueba](https://media.wiki-power.com/img/20220728162655.png)

Algunos puntos a tener en cuenta:

- Se debe utilizar una pinza de corriente para evitar dañar los equipos de prueba debido a corrientes excesivas.
- Si se detecta una corriente negativa, esto indica que la prueba no se ha superado.
- En caso de errores en la prueba, primero se debe descartar si se trata de un problema con los equipos de prueba. Ejecute una prueba con el zócalo del chip vacío; la corriente debería ser igual a 0. Si no es así, significa que otros dispositivos además del DUT también están consumiendo corriente.

### Prueba de IDD - Método Estático

La prueba estática de IDD mide la corriente total que ingresa al pin VDD y generalmente requiere que el DUT funcione en su modo de consumo mínimo de energía. La diferencia entre la prueba estática de IDD y la prueba de IDD bruto es que la prueba de IDD bruto no incluye ningún preprocesamiento, es simplemente una medición bruta, mientras que la prueba de IDD estática se realiza después del preprocesamiento.

Por ejemplo, aquí hay una muestra de parámetros IDD:

| Parámetro    | Descripción               | Condiciones de Prueba               | Mín | Máx | Unidades |
| ------------ | ------------------------- | ----------------------------------- | --- | --- | -------- |
| IDD Estático | Corriente de Alimentación | VDD = 5.25V, entradas = VDD, Iout=0 |     | +22 | µA       |

El esquema de prueba de IDD estático se muestra a continuación:

![Esquema de Prueba](https://media.wiki-power.com/img/20220728162341.png)

El proceso de prueba es el siguiente:

1. Use test vectors to set the DUT to consume the least current and keep it in a static state.
2. Check the pin current values
   - Above IDD Spec: Fail
   - Other ranges: Pass

During testing, it's typically necessary to introduce a delay between power-up and sampling to allow parasitic capacitance to charge fully and avoid interference.

If you need to test static current under different logic conditions, you can measure the IDDQ parameter to increase test coverage (IDDQ measures the current in a stationary logic state, such as opening a portion of MOSFETs for testing in a specific state).

### IDD Testing - Dynamic Method

The purpose of IDD dynamic testing is to measure the current consumed by the DUT when it is in **dynamic operation** (usually at the DUT's maximum operating frequency) to ensure it does not exceed the nominal value.

For example, the table below provides a sample of dynamic IDD parameters:

| Parameter   | Description          | Test Conditions                             | Min | Max | Units |
| ----------- | -------------------- | ------------------------------------------- | --- | --- | ----- |
| IDD Dynamic | Power Supply Current | VDD = 5.25V (commercial), f = f_max (66MHz) |     | +18 | mA    |

The testing process is similar to the static method.

## VOL/IOL & VOH/IOH

VOL represents the highest voltage (V) limit when outputting a low level (L) (not recognized as logic 1). IOL represents the drive capability of the pin's buffer to sink current (I) when outputting a low level (L). They jointly measure the pin buffer's impedance when outputting a low level, ensuring it can absorb a constant current at the appropriate output voltage.

VOH represents the lowest voltage (V) limit when outputting a high level (H) (not recognized as logic 0). IOH represents the drive capability of the buffer to source current (I) when outputting a high level (H). They jointly measure the buffer's impedance when outputting a high level, ensuring it can output a constant current at the appropriate output voltage.

For example, the table below provides VOL/IOL & VOH/IOH parameters for a 256 x 4 Static RAM:

| Parameter | Description         | Test Conditions           | Min | Max | Units |
| --------- | ------------------- | ------------------------- | --- | --- | ----- |
| VOL       | Output LOW Voltage  | VDD = 4.75V, IOL = 8.0mA  |     | 0.4 | V     |
| VOH       | Output HIGH Voltage | VDD = 4.75V, IOH = -5.2mA | 2.4 |     | V     |

Testing VOL/IOL & VOH/IOH primarily aims to verify whether VOL/VOH are at the correct voltage levels when applying sourcing or sinking current (whether they can reach the voltage threshold at a certain current output). There are static and dynamic methods for testing. **The static method involves applying current to the pins and then measuring the voltage one by one; the dynamic method introduces VREF during functional testing to create dynamic load current and then measures the voltage**.

### VOL/IOL Testing - Serial Static Method

The testing schematic for measuring VOL/IOL using the serial static method is as follows:

![Schematic](https://media.wiki-power.com/img/20220728150542.png)

The testing process is as follows:

1. First, set the pins to low-level output through preprocessing.
2. Apply a constant IOH to the pins, wait for 1-5 milliseconds, and then measure
3. Check the pin voltage
   - Above VOL (+0.4V): Fail
   - Other ranges: Pass

Points to note:

- IOL es un valor de corriente positiva, ya que fluye desde PMU hacia DUT.
- Dado que se aplica una corriente constante, es necesario configurar una abrazadera de voltaje. Si se mide un voltaje más bajo que el voltaje de la abrazadera, es posible que la lógica esté configurada en alto nivel, lo que activaría la polarización directa del diodo de protección de energía.
- El parámetro VDDmin representa el voltaje mínimo de suministro que permite que DUT realice pruebas de manera adecuada. Si es menor, no se podrán obtener resultados precisos de la prueba.

### Prueba VOH/IOH - Método estático en serie

El diagrama a continuación muestra la ilustración de la prueba VOH/IOH utilizando el método estático en serie:

![Imagen](https://media.wiki-power.com/img/20220728143124.png)

El proceso de prueba es el siguiente:

1. Se requiere la configuración previa para establecer los pines a probar en una salida de alto nivel.
2. Se aplica una corriente constante IOH a los pines y se espera de 1 a 5 milisegundos antes de realizar la medición (se establece una demora en el PMU).
3. Se verifica el voltaje en los pines.
   - Si es menor que VOH (+2.4V): Falla.
   - En cualquier otro rango: Aprobado.

Consideraciones importantes:

- Dado que IOL fluye desde PMU hacia DUT, es un valor negativo.
- Debido a que se aplica una corriente constante, se necesita configurar una abrazadera de voltaje. Si el voltaje medido es mayor que el voltaje de la abrazadera, es posible que la lógica de los pines esté configurada en nivel bajo, lo que activaría la polarización directa del diodo de protección a tierra.
- El parámetro VDDmin representa el voltaje mínimo de suministro necesario para que DUT realice pruebas de manera adecuada. Si es menor, no se obtendrán resultados precisos de la prueba.

## IIL/IIH

IIL se refiere a la corriente máxima permitida cuando la entrada del pin (I) está en un estado lógico bajo (L), lo que evalúa si la fuga de corriente desde los pines al suministro de energía cumple con las especificaciones, y también evalúa el grado de aislamiento. IIH se refiere a la corriente máxima permitida cuando la entrada del pin (I) está en un estado lógico alto (H), lo que evalúa la corriente de drenaje desde DUT a través de los pines hacia el suministro de energía. Para ilustrar, aquí se presentan los parámetros IIL y IIH de una RAM estática de 256 x 4:

| Parámetro | Descripción                   | Condiciones de prueba  | Mínimo | Máximo | Unidades |
| --------- | ----------------------------- | ---------------------- | ------ | ------ | -------- |
| IIL, IIH  | Corriente de Carga de Entrada | Vss ≤ Vin ≤ VDD(5.25V) | -10    | +10    | µA       |

IIL evalúa la resistencia de entrada desde los pines a VDD, mientras que IIH evalúa la resistencia de entrada desde los pines a VSS. Esta prueba garantiza que la impedancia de entrada cumple con los requisitos de diseño y que la corriente de entrada no excede los límites. La prueba de IIL/IIH se puede realizar de forma secuencial, paralela o combinada, y también se puede realizar mediante pruebas funcionales. El enfoque secuencial prueba un pin a la vez, lo que es preciso pero puede llevar tiempo.

Además, las pruebas de IIL/IIH generalmente solo se pueden realizar en pines de entrada pura. Si se encuentran pines bidireccionales, se debe agregar una carga de salida para mantener el nivel de voltaje estable en los pines y evitar que fluya corriente a través de los dispositivos de protección, lo que podría afectar los resultados de la prueba.

### Prueba IIL/IIH - Método estático en serie

En algunos sistemas de prueba, se puede realizar una medición en paralelo de la corriente de fuga (Método de Prueba en Paralelo). La medición en paralelo de la corriente de fuga implica la utilización de varios PMU (Unidades de Medición Programable) para medir por separado la corriente en varios pines. Todos los pines de entrada se fuerzan a un nivel alto y, simultáneamente, se mide en paralelo la corriente en cada pin. A continuación, los resultados de la prueba se comparan con los valores nominales para llegar a una conclusión.

![Imagen](https://media.wiki-power.com/img/20220729103317.png)

1. En primer lugar, se debe suministrar la fuente de alimentación VDDmax al Dispositivo Bajo Prueba (DUT).
2. Utilice varios PMU para forzar cada pin de entrada a un nivel alto de VDDmax (para medir IIH).
3. Espere de 1 a 5 microsegundos, detecte la corriente y haga la comparación para llegar a una conclusión.
4. Luego, cambie los niveles a VSS y repita los pasos anteriores para medir IIL.

La característica principal del método en paralelo es que permite medir simultáneamente la corriente individual de cada pin, lo que acelera la prueba de IIL/IIH. Sin embargo, la desventaja es que es más difícil detectar las fugas entre los pines de entrada, ya que todos los pines se mantienen al mismo nivel.

### Prueba de IIL/IIH - Método Combinado Estático

El método combinado (Ganged Method) implica la agrupación de todos los pines de entrada en un solo pin, y se utiliza un solo PMU para medir la corriente de fuga total. El diagrama de la prueba se muestra a continuación:

![Imagen](https://media.wiki-power.com/img/20220729104449.png)

El método de prueba combinada es similar al método anterior. El límite total de corriente es el valor nominal de un solo pin. Si los resultados de la prueba superan este límite, se debe realizar una prueba de repetición en serie. Este método de prueba es especialmente efectivo para dispositivos CMOS (de alta impedancia de entrada).

## IOZL/IOZH

La corriente de alta impedancia IOZ se refiere a la corriente de fuga en los pines de salida (O) cuando están en estado de alta impedancia (Z). En particular, IOZL se refiere a la corriente de fuga cuando el pin está en estado bajo (L), mientras que IOZH se refiere a la corriente de fuga cuando el pin está en estado alto (H). Esta prueba se utiliza para determinar si la corriente de fuga al apagar los pines cumple con las especificaciones.

Este parámetro garantiza que los pines de salida bidireccionales o de alta impedancia se puedan apagar adecuadamente (en estado de alta impedancia). IOZL mide la resistencia del pin a VDD en estado de alta impedancia, mientras que IOZH mide la resistencia del pin a VSS. Por lo general, se representa de la siguiente manera en las especificaciones:

| Parámetro | Descripción                            | Condiciones de Prueba                        | Mín  | Máx  | Unidades |
| --------- | -------------------------------------- | -------------------------------------------- | ---- | ---- | -------- |
| IOZ       | Corriente de Salida en Alta Impedancia | VSS ≤ Vout ≤ VDD (5.25V), Salida Desactivada | -2.0 | +2.0 | µA       |

### Prueba de IOZL/IOZH - Método Estático en Serie

El diagrama de la prueba estática en serie de IOZL/IOZH es el siguiente:

![Imagen](https://media.wiki-power.com/img/20220807202447.png)

El proceso de prueba es el siguiente:

1. En primer lugar, se debe suministrar la fuente de alimentación VDD al dispositivo.
2. Se deben configurar los pines del dispositivo en estado de alta impedancia y utilizar el PMU para forzar los pines a un nivel alto o bajo.
3. Medir el valor de corriente en los pines.
   - Menor que -IOZ (-2µA): Falla
   - Mayor que +IOZ (+2µA): Falla
   - En otro rango: Aprobado

La ventaja de la prueba en serie es que permite una medición precisa de la corriente de cada pin de forma individual, pero la desventaja es que es más lenta. Además, esta prueba requiere la configuración de la corriente de pinza.

### Prueba de IOZL/IOZH - Método Estático en Paralelo

El método estático en paralelo implica que varios PMU realicen pruebas simultáneas en varios pines, no se necesita ahondar más en esta descripción. Su principal ventaja es la rapidez.

| Parámetro | Descripción                    | Condiciones de prueba   | Mínimo | Máximo | Unidades |
| --------- | ------------------------------ | ----------------------- | ------ | ------ | -------- |
| VI        | Tensión de sujeción de entrada | VCC = Mín., Iin = -18mA |        | +1.5   | V        |

### Prueba de VI - Método estático secuencial

La prueba de VI se realiza utilizando el método estático secuencial. El diagrama de prueba se muestra a continuación:

![](https://media.wiki-power.com/img/20220729145425.png)

El proceso de prueba es el siguiente:

1. Asegúrese de que esta sea la entrada de un dispositivo TTL y suministre la energía para VCCmin.
2. Después de configurar la sujeción de voltaje, utilice el PMU para extraer una corriente de -15mA a -20mA.
3. Mida el valor de voltaje en el pin de entrada.
   - Por debajo de VI (-1.5V): Falla
   - En otro rango: Aprobado

## IOS (Corriente de cortocircuito de salida)

La corriente de cortocircuito de salida representa la corriente (I) generada cuando el pin de salida (O) está en cortocircuito (S). Su propósito es **medir la impedancia de salida cuando el pin está en un estado alto pero se cortocircuita a cero voltios, garantizando que la corriente de salida no sea excesiva en las peores condiciones de carga**. También indica la corriente máxima instantánea que el pin del DUT puede proporcionar para cargar capacitiva, lo que se utiliza para calcular el tiempo de subida. IOS se describe en las especificaciones de la siguiente manera:

| Parámetro | Descripción                          | Condiciones de prueba                                                                               | Mínimo | Máximo | Unidades |
| --------- | ------------------------------------ | --------------------------------------------------------------------------------------------------- | ------ | ------ | -------- |
| IOS       | Corriente de cortocircuito de salida | Vout = 0V, VDD = 5.25V, \* Cortocircuito solo un pin de salida a la vez durante no más de 1 segundo | -85    | -30    | mA       |

### Prueba de IOS - Método estático secuencial

El diagrama de prueba se muestra a continuación:

![](https://media.wiki-power.com/img/20220729152549.png)

El proceso de prueba es el siguiente:

1. Proporcione alimentación a VDDmax, prepare el dispositivo para que el pin de salida esté en estado alto.
2. Use el PMU para bajar el pin a 0V y mida la corriente de salida, luego compare con el valor nominal para llegar a una conclusión.

En las pruebas de IOS, es importante tener una lógica adecuada para evitar conmutaciones en caliente. En primer lugar, configure el PMU en modo de medición de voltaje de corriente cero, conéctelo a la salida del DUT, mida y guarde el voltaje VOH del DUT. Luego desconéctelo y configure el PMU para subir a VOH nuevamente, luego vuelva a conectar el DUT (en este punto, ambos extremos tienen el voltaje VOH). Luego, haga que el PMU baje a 0V y mida el valor de corriente. Después de completar la medición, el PMU debe restablecerse a VOH antes de desconectarse. De esta manera, se asegura que los voltajes en ambos extremos sean consistentes al realizar cambios de conmutación.

Factores que pueden causar que la prueba no pase:

- **Excede el valor máximo**
  - La impedancia de salida es demasiado alta, lo que resulta en una corriente absoluta insuficiente.
  - La sonda de prueba en sí tiene resistencia.
  - No se ha realizado un preprocesamiento adecuado.
- **Por debajo del valor mínimo**
  - La impedancia de salida es demasiado baja, lo que resulta en una corriente absoluta excesiva.

## Entradas resistivas (Resistencia de pull-up y pull-down)

Algunos pines de entrada pueden tener una estructura activa de pull-up y pull-down, y es necesario garantizar que las rutas de resistencia de pull-up y pull-down del búfer de entrada estén funcionando correctamente. Esto solo se puede probar de manera secuencial, ya que la estructura de pull-up y pull-down interna de los diferentes pines puede ser diferente. El diagrama de la estructura del pin se muestra a continuación:

![](https://media.wiki-power.com/img/20220729130655.png)

## Capacidad de Ramificación de Salida (Output Fanout)

La capacidad de ramificación (Fanout) se refiere a la capacidad de un pin de salida para impulsar múltiples pines de entrada en función de sus parámetros de voltaje y corriente. En otras palabras, la capacidad de conducir pines, es un indicador de cuántos pines de entrada puede manejar un pin de salida.

![Imagen](https://media.wiki-power.com/img/20220729132621.png)

Como se muestra en la figura anterior, esta salida TTL puede elevar aproximadamente 17 pines de entrada o reducir 30 pines de entrada. En las especificaciones, los parámetros de los pines se representan de la siguiente manera:

| Parámetro | Descripción                        | Condiciones de prueba     | Mín  | Máx | Unidades |
| --------- | ---------------------------------- | ------------------------- | ---- | --- | -------- |
| VOH       | Voltaje ALTO de Salida             | VCC = 4.75V, IOH = -2.6mA | 2.4  |     | V        |
| VOL       | Voltaje BAJO de Salida             | VCC = 4.75V, IOH = 24mA   |      | 0.4 | V        |
| IIL       | Corriente de Carga Baja de Entrada | Vin = 0.4V                | -800 |     | µA       |
| IIH       | Corriente de Carga Alta de Entrada | Vin = 2.4V                |      | 150 | µA       |

La capacidad de ramificación varía significativamente entre dispositivos TTL y CMOS, ya que los dispositivos CMOS tienen una alta impedancia de entrada. En teoría, una salida CMOS puede impulsar cualquier cantidad de entradas CMOS. Sin embargo, los pines de entrada CMOS tienen capacitancia parásita, y cuantos más se conecten, mayor será la capacitancia, lo que resultará en efectos de carga y descarga de capacitancia y, por lo tanto, en retrasos al cambiar entre niveles altos y bajos.

## Referencias y Agradecimientos

- "The Fundamentals Of Digital Semiconductor Testing"
- "DC Test Theory"

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
