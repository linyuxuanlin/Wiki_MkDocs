# Desarrollo de hardware STM32F4

Este artículo explicará el sistema mínimo de MCU de STM32F4 (alimentación, reloj, reinicio, modo de arranque, gestión de depuración).

## Alimentación

La tensión de trabajo normal de STM32F4 es de 1,8-3,6 V (en algunos casos puede ser inferior a 1,7 V, como se indica en la hoja de datos), y cuenta con un regulador interno que proporciona una fuente de alimentación digital de 1,2 V.

Cuando se interrumpe la alimentación principal VDD, se puede suministrar energía a la RTC y a los registros de copia de seguridad a través del voltaje de VBAT.

### Introducción a los pines

#### Alimentación y voltaje de referencia ADC

Para mejorar la precisión de conversión, ADC cuenta con pines de alimentación independientes que pueden filtrarse y aislar el ruido de la PCB.

La fuente de voltaje ADC proviene del pin VDDA independiente. En el diseño del circuito, se debe conectar VSSA al mismo suministro de tierra en lugar de VSS.

Si el encapsulado del chip tiene más de 100 pines, habrá pines VREF+ y VREF-, que se utilizan para proporcionar voltaje de referencia externo al ADC. VREF- debe conectarse a VSSA interno. Si el número de pines del chip es inferior a 100, estos dos pines no se conectan y se conectan internamente a VDDA y VSSA.

#### Alimentación de la batería de respaldo

Si se necesita mantener el contenido del registro de copia de seguridad después de que se interrumpe VDD, se puede conectar VBAT a una batería u otra fuente de alimentación.

VBAT también puede suministrar energía a la RTC, controlada por el circuito de reinicio por caída de energía (PDR) integrado en el módulo de reinicio.

#### Regulador interno

El regulador interno siempre está habilitado después del reinicio y tiene tres modos de funcionamiento:

- Ejecución: el regulador proporciona suministro de energía de plena potencia de 1,2 V (núcleo, memoria y periféricos digitales).
- Parada: el regulador proporciona suministro de energía de baja potencia de 1,2 V al núcleo y conserva el contenido de los registros y la SRAM.
- En espera: el regulador se apaga. Se perderá el contenido de los registros y la SRAM, excepto el circuito de espera y el dominio de copia de seguridad.

### Diseño del circuito

A continuación se muestra el método de diseño de los pines de alimentación:

- **VDD**
  - **Condensador de desacoplamiento**: un condensador cerámico/tantalio de 10 μF en total, más un condensador cerámico de 100 nF conectado a cada pin VDD.
- **VDDA**
  - **Condensador de desacoplamiento**: un condensador cerámico de 100 nF + un condensador cerámico/tantalio de 1 µF.
  - **Filtrar el ruido analógico**: se puede conectar a VDD mediante un núcleo magnético.
- **VREF+**
  - **Condensador de desacoplamiento**: si se utiliza la función VREF+, se necesitan un condensador de 100 nF y otro de 1 µF.
  - **Filtrar el ruido analógico**: se puede conectar a VDDA mediante una resistencia de 47 Ω.
- **VBAT**: conecte una batería externa (1,65 V-3,6 V). Si no se necesita una fuente de alimentación de batería, conéctela al pin VDD.
- **VCAP1/VCAP2**: conecte un condensador cerámico de 2,2 µF (ESR < 2 Ω) a tierra para cada uno; si solo hay VCAP1, conecte un condensador cerámico de 4,7 µF (ESR < 1 Ω).

### Reinicio y supervisión de alimentación

#### Reinicio por encendido (POR) / Reinicio por caída de energía (PDR)

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529143014.png)

El chip STM32F4 integra el circuito POR/PDR, y las características específicas del reinicio por encendido / caída de energía se muestran en la figura anterior. Si se desea deshabilitar esta función, se puede hacer a través del pin PDR_ON.

#### Reinicio del sistema

Las condiciones de activación del reinicio del sistema son:

- Bajo nivel de voltaje en el pin NRST (reinicio externo)
- Finalización del conteo del perro guardián de ventana (reinicio WWDG)
- Finalización del conteo del perro guardián independiente (reinicio IWDG)
- Reinicio de software (reinicio SW)
- Reinicio de gestión de baja potencia

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529143925.png)

Se puede determinar la fuente de reinicio mediante la visualización de la bandera de reinicio en el registro de control / estado (RCC_CSR).

Incluso si no se necesita un circuito de reinicio externo, se recomienda agregar un condensador de descarga para mejorar el rendimiento de EMS.

## Reloj

En STM32F4, se pueden utilizar tres fuentes de reloj diferentes para impulsar el reloj del sistema (SYSCLK):

- HSI (señal de reloj interno de alta velocidad)
- HSE (señal de reloj externo de alta velocidad)
- Reloj PLL

También hay dos fuentes de reloj secundarias:

- LSI RC (32 kHz RC interno de baja velocidad), utilizado para conducir un watchdog independiente, también se puede utilizar para despertar automáticamente en modo de apagado / espera RTC.
- LSE (32.768 kHz cristal externo de baja velocidad), utilizado para conducir RTC.

Si se necesita reducir el consumo de energía, cada reloj se puede apagar individualmente cuando no se está utilizando.

### Reloj externo de alta velocidad (HSE)

Hay dos formas de proporcionar la fuente de reloj HSE: fuente externa (activa) y cristal externo / resonador cerámico (pasivo).

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529145726.png)

#### Fuente externa (bypass HSE)

Si se elige la entrada de señal de reloj externa activa, se debe proporcionar una fuente de reloj de 1-50 MHz, OSC_IN se conecta a una señal de reloj externa con un ciclo de trabajo de aproximadamente el 50% (onda cuadrada, senoidal o triangular), y OSC_OUT se mantiene en alta impedancia.

#### Cristal externo / resonador cerámico (HSE cristal)

Si se utiliza un cristal externo, el rango de frecuencia es de 4-26 MHz. Al diseñar el circuito, el resonador y la capacidad de carga deben estar lo más cerca posible de los pines del oscilador para minimizar la distorsión de salida y el tiempo de estabilización de la oscilación. El valor de la capacidad de carga debe ajustarse adecuadamente según el oscilador seleccionado.

CL1 y CL2 deben tener el mismo tamaño (5-25 pF, valor típico 25 pF) de capacidad de cerámica.

### Reloj externo de baja velocidad (LSE)

Hay dos formas de proporcionar la fuente de reloj LSE: fuente externa (activa) y cristal externo / resonador cerámico (pasivo).

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529152354.png)

#### Fuente externa (bypass LSE)

Si se elige la entrada de señal de reloj externa activa, se debe proporcionar una fuente de reloj de menos de 1 MHz, OSC32_IN se conecta a una señal de reloj externa con un ciclo de trabajo de aproximadamente el 50% (onda cuadrada, senoidal o triangular), y OSC32_OUT se mantiene en alta impedancia.

#### Cristal externo / resonador cerámico (LSE cristal)

Si se utiliza un cristal externo, el rango de frecuencia es de 32.768 kHz y se puede utilizar como fuente de reloj RTC. Al diseñar el circuito, el resonador y la capacidad de carga deben estar lo más cerca posible de los pines del oscilador para minimizar la distorsión de salida y el tiempo de estabilización de la oscilación. El valor de la capacidad de carga debe ajustarse adecuadamente según el oscilador seleccionado.

## Modo de arranque

El modo de arranque también se llama modo de autorecuperación. Se pueden seleccionar tres modos de arranque diferentes mediante los pines BOOT0 y BOOT1: arranque desde la memoria flash principal, arranque desde la memoria del sistema, arranque desde la SRAM incorporada.

Para obtener más información sobre el modo de arranque, consulte el artículo [**Modo de arranque de STM32**](https://wiki-power.com/es/STM32%E7%9A%84%E5%90%AF%E5%8A%A8%E6%A8%A1%E5%BC%8F)

En general, conectamos una resistencia de 10 K en serie con BOOT0 y BOOT1 es arbitrario. Si es necesario cambiar de modo, se puede diseñar de la siguiente manera:

![](https://f004.backblazeb2.com/file/wiki-media/img/20200605163537.png)

## Gestión de depuración

STM32 generalmente utiliza el protocolo SWJ para la descarga y depuración.

### Puerto de depuración SWJ

El STM32F4 tiene una interfaz SWJ (SW/JTAG) integrada. Entre ellas, SW-DP tiene 2 pines (reloj + datos) y JTAG-DP tiene 5 pines, algunos de los cuales son compartidos. Para obtener más información, consulte el artículo [**Diferencias y conexiones entre SWD y JTAG**](https://wiki-power.com/es/SWD%E4%B8%8EJTAG%E7%9A%84%E5%8C%BA%E5%88%AB%E4%B8%8E%E8%81%94%E7%B3%BB)

En STM32F4, la asignación de pines SWJ es la siguiente:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529210858.png)

### Pull-up y pull-down internos de JTAG

Los pines JTAG no pueden estar en el aire (porque están conectados directamente a los disparadores utilizados para el control de depuración de modo), por lo que se integran en el chip para tirar hacia arriba y hacia abajo:

- **JNTRST**: Pull-up interno
- **JTDI**: Pull-up interno
- **JTMS/SWDIO**: Pull-up interno
- **TCK/SWCLK**: Pull-down interno

Después de liberar el I/O de JTAG mediante software, se puede utilizar como un puerto I/O normal.

### Diseño de hardware para conectar un conector JTAG estándar

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529211840.png)

## Diseño de referencia

![](https://f004.backblazeb2.com/file/wiki-media/img/20210529213723.png)

## Referencias y agradecimientos

- [AN4488: Getting started with STM32F4xxxx MCU hardware development](https://www.st.com/content/ccc/resource/technical/document/application_note/76/f9/c8/10/8a/33/4b/f0/DM00115714.pdf/files/DM00115714.pdf/jcr:content/translations/en.DM00115714.pdf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.