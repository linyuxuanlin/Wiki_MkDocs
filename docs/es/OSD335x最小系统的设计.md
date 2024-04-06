# Diseño del Sistema Mínimo de OSD335x

![](https://media.wiki-power.com/img/20211012144907.png)

El chip OSD335x-SM de TI es un módulo SIP (System-in-Package) que integra un procesador Cortex-A8 AM335x, memoria DDR3, PMIC TPS65217C (circuito integrado de gestión de energía), LDO TL5209, componentes pasivos necesarios y una EEPROM de 4KB, todo en un encapsulado BGA.

![](https://media.wiki-power.com/img/20211012153036.png)

El sistema mínimo de OSD335x consta de cuatro partes: energía, reloj, reinicio y una interfaz de programación y depuración. Para facilitar su uso, se pueden agregar un par de botones, algunos LEDs y varios pines periféricos.

![](https://media.wiki-power.com/img/20211012155857.png)

## Energía

### Entradas

- VIN_AC: Entrada de alimentación principal (DC5V @ 2A), que puede incluir fusibles, inductores, diodos Schottky y protección de entrada según sea necesario.
- VIN_USB: Entrada de alimentación USB (DC5V @ 0.5A, ampliable a 1.3A mediante el PMIC interno). También se utiliza como referencia de voltaje y corriente para el host USB 2.0.
- VIN_BAT: Puede utilizarse como entrada de batería (rango de 2.75-5.5V) o como salida para cargar la batería, pero no como entrada de eventos.

![](https://media.wiki-power.com/img/20211012173057.png)

### Salidas

- SYS_VOUT: Igual a la tensión de entrada del PMIC. Se debe tener en cuenta que los componentes conectados a este pin deben funcionar en el rango de 3-5V, ya que el PMIC cambia entre diferentes fuentes de alimentación durante la carga de la batería.
- SYS_VDD1_3P3V: Salida de 3.3V proporcionada por el LDO TL5209 y habilitada por el LDO4 del PMIC, que se utiliza como salida de energía principal.
- SYS_VDD2_3P3V: Salida de 3.3V proporcionada por el LDO2 del PMIC.
- SYS_RTC_1P8V: Salida de 1.8V proporcionada por el LDO1 del PMIC, que también se utiliza para alimentar el RTC interno del AM335x.
- SYS_VDD_1P8V: Salida de 1.8V proporcionada por el LDO3 del PMIC.
- SYS_ADC_1P8V: Salida de 1.8V proporcionada por el LDO3 del PMIC con filtrado adicional para aplicaciones analógicas y alimentación del ADC del AM335x.

Se recomienda añadir puntos de prueba para todas las salidas de energía para facilitar la depuración.

También hay pines que proporcionan energía interna, como VDDSHV_3P3V, VDDS_DDR, VDD_MPU, VDD_CORE y VDDS_PLL. Estos pines solo se utilizan para mediciones de prueba internas y no deben conectarse a circuitos externos.

![](https://media.wiki-power.com/img/20211013142917.png)

### Entradas y tierra de referencia analógicas

![](https://media.wiki-power.com/img/20211013143532.png)

El OSD335x tiene una interfaz ADC que requiere conexiones adecuadas de alimentación analógica y tierra para su funcionamiento. La interfaz ADC puede manejar una entrada analógica de hasta 1.8V (según la referencia en el pin VREFP). Normalmente, VREFP se conecta directamente a SYS_ADC_1P8V, pero si es necesario, se puede dividir a un voltaje más bajo.

Gestión de energía

Dentro del OSD335x, el AM335x se comunica con el PMIC TPS65217C a través de I2C0.

I2C0 incluye resistencias pull-up de 4.7k internas, pero es recomendable agregar resistencias pull-up externas si se conectan dispositivos.

El PMIC TPS65217C se puede configurar a través de I2C para controlar:

- Voltaje de carga de la batería
- Control de tiempo de carga segura
- Voltaje de salida de Buck/Boost
- Voltaje de salida de LDO
- Secuencia de encendido/apagado
- Umbrales de sobrecorriente y sobrecalentamiento

![](https://media.wiki-power.com/img/20211013161739.png)

Además de la conexión I2C, el PMIC tiene pines de funciones adicionales que deben conectarse al OSD335x.

- **PMIC_POWER_EN:** Utilizado para controlar la secuencia de encendido en el PMIC para AM335x.
- **PMIC_IN_PWR_EN:** Habilita los reguladores buck y LDO del PMIC. Un nivel alto dará inicio al control de secuencia de encendido.
- **RTC_PWRONRSTN:** Es la entrada independiente de reinicio de energía para el RTC de AM335x.
- **PMIC_OUT_LDO_PGOOD:** Estado de salida de LDO1 y LDO2. Un nivel alto indica una salida óptima, mientras que un nivel bajo señala un problema en cualquiera de las salidas de LDO.
- **EXT_WAKEUP:** Pin de activación externa por eventos.
- **PMIC_OUT_NWAKEUP:** Pin de activación externa para el host (efectivo en nivel bajo).
- **EXTINTN:** Pin de entrada de interrupción externa para AM335x.
- **PMIC_OUT_NINT:** Pin de salida del PMIC (efectivo en nivel bajo).

![Imagen](https://media.wiki-power.com/img/20211013161927.png)

![Imagen](https://media.wiki-power.com/img/20211013163119.png)

### Botón de encendido

El PMIC TPS65217C tiene una entrada de reinicio de nivel bajo, conectada al OSD335x a través del pin PMIC_IN_PB_IN, que también se puede conectar a un botón externo. Este pin de entrada presenta un tiempo de rebote de 50 ms y una resistencia interna de pull-up. Además de esto, el botón de encendido tiene las siguientes funciones:

- Cuando PMIC_IN_PB_IN detecta un flanco descendente de entrada, el PMIC se despertará del modo de apagado o suspensión.
- Si PMIC_IN_PB_IN se mantiene en nivel bajo durante más de 8 segundos, el PMIC se reiniciará/encenderá de nuevo.
- Si el pin PMIC_IN_PB_IN permanece en nivel bajo durante un largo período, el dispositivo continuará alternando entre los estados ACTIVO y RESET, con un ciclo de 8 segundos.

![Imagen](https://media.wiki-power.com/img/20211013165738.png)

### Indicador de energía

Utilizamos SYS_VDD2_3P3V (150 mA) como la salida del indicador de energía.

![Imagen](https://media.wiki-power.com/img/20211014092054.png)

## Reinicio

El OSD335x tiene varias formas de reinicio:

- Reinicio en frío (reinicio al encender): Se realiza al encender el dispositivo y el dominio de energía.
- Reinicio en caliente:
  - Es un reinicio parcial que no afecta la lógica global.
  - Está diseñado para minimizar el tiempo de recuperación tras el reinicio.

El OSD335x cuenta con 3 entradas de reinicio (con los mismos nombres que las entradas de reinicio en AM335x):

- PWRONRSTN: Reinicio en frío; debe mantenerse en nivel bajo durante el encendido hasta que todas las líneas de suministro estén estables. No se puede bloquear, y afecta a todo el sistema, excepto al RTC.
- WARMRSTN: Reinicio en caliente; algunos registros de módulos de control y gestión de energía, reinicio y reloj (PRCM) no son sensibles al reinicio en caliente.
- RTC_PWRONRSTN: Entrada de reinicio al encender dedicada al módulo RTC, no se ve afectada por el reinicio en frío, ni afecta a otras partes del dispositivo.

![Imagen](https://media.wiki-power.com/img/20211014105556.png)

## Relojes

### OSC0 y OSC1

El OSD335x tiene dos entradas de reloj:

- OSC0: Entrada de reloj de alta velocidad (reloj principal) que opera a frecuencias de 19,2 MHz, 24 MHz (recomendado), 25 MHz o 26 MHz. Esta fuente de reloj sirve como referencia para todas las funciones excepto el RTC. La entrada de reloj OSC0 tiene los pines OSC0_IN, OSC0_OUT y OSC0_GND.
- OSC1: Entrada de reloj de baja velocidad que funciona a 32.768 kHz y alimenta el RTC. La entrada de reloj OSC1 tiene los pines OSC1_IN, OSC1_OUT y OSC1_GND. Esta fuente de reloj está desactivada de forma predeterminada y es opcional; solo se utiliza si es necesario y puede recibir una señal de oscilador RC de 32 kHz interna.

![Imagen](https://media.wiki-power.com/img/20211014095242.png)

En la figura anterior, Rbias y Rd son opcionales. Si no se puede proporcionar una frecuencia precisa, Rbias se puede utilizar para calibrar de manera flexible, y se puede omitir en el esquema eléctrico o dejarse en blanco. Sin embargo, si no se necesita Rd, debe sustituirse por un cable, de lo contrario, se producirá una interrupción en el circuito.

En el diseño de referencia, se utiliza un oscilador de 24 MHz 7A-24.000MAAJ-T con condensadores de 18pF y una resistencia de 1 MΩ como Rbias.

![Imagen](https://media.wiki-power.com/img/20211014101932.png)

El pin RTC_KALDO_ENN tiene una resistencia de 10kΩ para una configuración predeterminada de pull-down externo, lo que habilita el regulador de voltaje interno del RTC.

## Interfaz de Programación y Depuración

En el diseño de referencia, se utiliza la interfaz JTAG.

![Imagen](https://octavosystems.com/octavosystems.com/wp-content/uploads/2017/07/JTAG.jpg)

## Otros Dispositivos Periféricos

### Configuración de Inicio

La tabla de configuración de inicio se puede encontrar en el capítulo **Pines de Configuración SYSBOOT** del [**Manual de Referencia Técnica AM335x (TRM)**](http://www.ti.com/lit/pdf/spruh73).

En el diseño de referencia, se configuran los siguientes parámetros:

- Se establece una frecuencia de reloj de 24 MHz.
- Se deshabilita la salida CLKOUT1 a través de XDMA_EVENT_INTR0, ya que este pin se utiliza solo para la emulación JTAG.
- La secuencia de inicio se configura como SPI0 -> MMC0 -> USB0 -> UART0.

### Botones de Usuario y LED

![Imagen](https://media.wiki-power.com/img/20211014110906.png)

### Conectores de Periféricos

![Imagen](https://media.wiki-power.com/img/20211014110947.png)

## Referencias y Agradecimientos

- [SO YOU WANT TO BUILD AN EMBEDDED LINUX SYSTEM?](https://jaycarlson.net/embedded-linux/#)
- [OSD335x-SM System-in-Package Smallest AM335x Module, Quickest Design](https://octavosystems.com/octavo_products/osd335x-sm/#Technical%20Documents)
- [Serie de Tutoriales de Diseño de Referencia OSD335x](https://octavosystems.com/app_notes/osd335x-design-tutorial/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
