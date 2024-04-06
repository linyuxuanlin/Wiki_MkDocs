# Desarrollo de hardware STM32F4

En este artículo, se explicará el sistema mínimo de MCU de STM32F4 (energía, reloj, restablecimiento, modos de inicio, gestión de depuración).

## Energía

La tensión de funcionamiento normal de STM32F4 es de 1,8 a 3,6 V (en algunas situaciones puede ser reducida por debajo de 1,7 V, como se indica en el datasheet), con un regulador interno que proporciona una fuente de alimentación digital de 1,2 V.

Cuando la fuente de alimentación principal VDD se desconecta, la tensión de VBAT se utiliza para alimentar el RTC y los registros de respaldo.

### Introducción a los pines

#### Alimentación y voltaje de referencia del ADC

Para mejorar la precisión de la conversión, el ADC cuenta con pines de alimentación independientes que pueden filtrarse y aislar el ruido en la PCB.

La fuente de voltaje del ADC proviene del pin VDDA independiente. Al diseñar el circuito, asegúrese de conectar VSSA al mismo suministro de tierra, no a VSS.

Si el encapsulado del chip tiene más de 100 pines, encontrará los pines VREF+ y VREF-, que se utilizan para proporcionar una referencia de voltaje externa al ADC. VREF- debe conectarse a VSSA interna. Si el chip tiene menos de 100 pines, estos dos pines no se dirigen hacia el exterior, ya que están conectados internamente a VDDA y VSSA.

#### Alimentación de batería de respaldo

Si es necesario mantener los registros de respaldo después de que VDD se desconecte, VBAT se puede conectar a una batería u otra fuente de energía.

VBAT también puede alimentar el RTC y es controlado por el circuito de reinicio por caída de voltaje (PDR) incorporado en el módulo de reinicio.

#### Regulador interno

El regulador interno siempre está habilitado después del reinicio y opera en tres modos:

- Funcionamiento: el regulador proporciona una fuente de alimentación a 1.2 V para el dominio (núcleo, memoria y periféricos digitales).
- Parada: el regulador suministra una fuente de alimentación de baja potencia a 1.2 V al dominio, mientras que se mantienen los registros y el contenido de la SRAM.
- En espera: el regulador se apaga. El contenido de los registros y la SRAM se pierde, a excepción de los circuitos en espera y el dominio de respaldo.

### Diseño del circuito

A continuación se muestra el método de diseño de los pines de alimentación:

- **VDD**
  - **Capacitores de desacoplamiento**: Un capacitor cerámico/tantalio de 10 μF en total, más un capacitor cerámico de 100 nF junto a cada pin VDD.
- **VDDA**
  - **Capacitores de desacoplamiento**: Un capacitor cerámico de 100 nF y un capacitor cerámico/tantalio de 1 μF.
  - **Filtrado de ruido analógico**: Puede conectarse a VDD mediante un inductor de filtro.
- **VREF+**
  - **Capacitores de desacoplamiento**: Si se habilita la función VREF+, debe agregarse un capacitor de 100 nF y otro de 1 μF.
  - **Filtrado de ruido analógico**: Puede conectarse a VDDA a través de una resistencia de 47 Ω.
- **VBAT**: Conéctelo a una batería externa (1.65 V-3.6 V). Si no se necesita una fuente de batería, conéctelo al pin VDD.
- **VCAP1/VCAP2**: Conecte un par de capacitores cerámicos de 2.2 μF a tierra (ESR < 2 Ω). Si solo hay un VCAP1, conecte un capacitor cerámico de 4.7 μF (ESR < 1 Ω).

### Restablecimiento y supervisión de la alimentación

#### Restablecimiento en encendido (POR) / Restablecimiento por caída de voltaje (PDR)

![Imagen](https://media.wiki-power.com/img/20210529143014.png)

El chip STM32F4 integra un circuito POR/PDR. Las características específicas del restablecimiento en encendido/caída de voltaje se muestran en la imagen anterior. Si es necesario deshabilitar esta función, puede hacerlo a través del pin PDR_ON.

#### Restablecimiento del sistema

Las condiciones para el restablecimiento del sistema son las siguientes:

- Nivel bajo en el pin NRST (restablecimiento externo).
- Fin de la cuenta del reloj del perro guardián de ventana (WWDG).
- Fin de la cuenta del perro guardián independiente (IWDG).
- Restablecimiento por software (restablecimiento por software).
- Restablecimiento de gestión de baja potencia.

![Imagen](https://media.wiki-power.com/img/20210529143925.png)

Puede determinar la fuente de restablecimiento consultando las señales de restablecimiento en el registro de control y estado (RCC_CSR).

Incluso si no se requiere un circuito de restablecimiento externo, se recomienda agregar un condensador de pull-down adicional para mejorar el rendimiento de EMC.

## Reloj

En STM32F4, puede usar tres fuentes de reloj diferentes para alimentar el reloj del sistema (SYSCLK):

- HSI (señal de reloj interna de alta velocidad)
- HSE (señal de reloj externa de alta velocidad)
- Reloj PLL

También hay dos fuentes de reloj secundarias:

- LSI RC (RC interno de baja velocidad de 32 kHz), utilizado para alimentar el reloj independiente del perro guardián y también se puede utilizar para la activación automática en el modo de parada/standby del RTC.
- LSE (cristal externo de baja velocidad de 32.768 kHz), utilizado para alimentar el RTC.

Si desea reducir el consumo de energía, cada reloj se puede apagar cuando no se utiliza.

```markdown
### External High-Speed Clock (HSE)

La fuente de reloj HSE puede proporcionarse de dos maneras: fuente externa (activa) y oscilador de cristal externo / resonador cerámico (inactivo).

![Imagen](https://media.wiki-power.com/img/20210529145726.png)

#### Fuente Externa (Derivación HSE)

Si se elige la entrada de señal de reloj externa activa, se debe suministrar una fuente de reloj de 1-50 MHz, con el pin OSC_IN conectado a una señal de reloj externa con un ciclo de trabajo de aproximadamente el 50% (forma de onda cuadrada, senoidal o triangular), mientras que el pin OSC_OUT debe permanecer en alta impedancia.

#### Oscilador de Cristal Externo / Resonador Cerámico (Cristal HSE)

Si se opta por el uso de un oscilador de cristal externo, la frecuencia debe estar en el rango de 4-26 MHz. Al diseñar el circuito, el resonador y la capacitancia de carga deben estar lo más cerca posible de los pines del oscilador para minimizar la distorsión de la salida y el tiempo de arranque del oscilador. El valor de la capacitancia de carga debe ajustarse adecuadamente según el oscilador seleccionado.

Se deben utilizar capacitores cerámicos CL1 y CL2 de tamaño idéntico (5-25 pF, valor típico de 25 pF).

### External Low-Speed Clock (LSE)

La fuente de reloj LSE puede proporcionarse de dos maneras: fuente externa (activa) y oscilador de cristal externo / resonador cerámico (inactivo).

![Imagen](https://media.wiki-power.com/img/20210529152354.png)

#### Fuente Externa (Derivación LSE)

Si se elige la entrada de señal de reloj externa activa, se debe suministrar una fuente de reloj de menos de 1 MHz, con el pin OSC32_IN conectado a una señal de reloj externa con un ciclo de trabajo de aproximadamente el 50% (forma de onda cuadrada, senoidal o triangular), mientras que el pin OSC32_OUT debe permanecer en alta impedancia.

#### Oscilador de Cristal Externo / Resonador Cerámico (Cristal LSE)

Si se opta por el uso de un oscilador de cristal externo, la frecuencia debe ser de 32.768 kHz y puede usarse como fuente de reloj para RTC. Al diseñar el circuito, el resonador y la capacitancia de carga deben estar lo más cerca posible de los pines del oscilador para minimizar la distorsión de la salida y el tiempo de arranque del oscilador. El valor de la capacitancia de carga debe ajustarse adecuadamente según el oscilador seleccionado.

## Modo de Arranque

El modo de arranque, también conocido como modo de autoarranque, se puede seleccionar mediante los pines BOOT0 y BOOT1 para elegir entre tres modos de arranque diferentes: arranque desde la memoria flash principal, arranque desde la memoria de sistema o arranque desde la SRAM integrada.

Para obtener más detalles sobre los modos de arranque, consulte el artículo [**Modos de Arranque de STM32**](https://wiki-power.com/STM32%E7%9A%84%E5%90%AF%E5%8A%A8%E6%A8%A1%E5%BC%8F) (en inglés).

En condiciones normales, se recomienda conectar un resistor de 10 KΩ a BOOT0, mientras que BOOT1 puede dejarse sin conexión. Si es necesario cambiar el modo de arranque, puede seguir el diseño a continuación:

![Imagen](https://media.wiki-power.com/img/20200605163537.png)

## Gestión de Depuración

En general, los dispositivos STM32 utilizan el protocolo SWJ para la depuración y descarga de firmware.

### Puerto de Depuración SWJ

Los microcontroladores STM32F4 incorporan una interfaz SWJ (SW/JTAG). En esta interfaz, SW-DP utiliza 2 pines (reloj + datos) y JTAG-DP utiliza 5 pines, algunos de los cuales son compartidos. Para conocer las diferencias detalladas, consulte el artículo [**Diferencias y Conexiones entre SWD y JTAG**](https://wiki-power.com/SWD%E4%B8%8EJTAG%E7%9A%84%E5%8C%BA%E5%88%AB%E4%B8%8E%E8%81%94%E7%B3%BB) (en inglés).

En los microcontroladores STM32F4, la asignación de pines para SWJ es la siguiente:

![Imagen](https://media.wiki-power.com/img/20210529210858.png)

### Resistencias Pull-up/Pull-down Internas para JTAG

Los pines JTAG no deben dejarse flotantes, ya que están directamente relacionados con los disparadores utilizados para el control del modo de depuración. Por lo tanto, en el interior del chip, se han incorporado resistencias pull-up/pull-down para estos pines:

- **JNTRST**: pull-up interno
- **JTDI**: pull-up interno
- **JTMS/SWDIO**: pull-up interno
- **TCK/SWCLK**: pull-down interno

Una vez que el software libera las E/S JTAG, se pueden utilizar como puertos de E/S normales.

### Diseño de Hardware para Conectar un Enchufe JTAG Estándar

![Imagen](https://media.wiki-power.com/img/20210529211840.png)

## Diseño de Referencia
```

```markdown
![](https://media.wiki-power.com/img/20210529213723.png)

## Referencias y Agradecimientos

- [AN4488: Inicio del desarrollo de hardware de MCU STM32F4xxxx](https://www.st.com/content/ccc/resource/technical/document/application_note/76/f9/c8/10/8a/33/4b/f0/DM00115714.pdf/files/DM00115714.pdf/jcr:content/translations/en.DM00115714.pdf)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
