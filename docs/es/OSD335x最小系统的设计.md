# Diseño del sistema mínimo OSD335x

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012144907.png)

El chip OSD335x-SM de TI es un módulo SIP (System-in-Package) que integra el procesador Cortex-A8 AM335x, memoria DDR3, el PMIC (chip de gestión de energía) TPS65217C, el LDO TL5209, los componentes pasivos necesarios y una EEPROM de 4KB en un encapsulado BGA.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012153036.png)

El sistema mínimo OSD335x consta de cuatro partes: alimentación, reloj, reset y puerto de programación y depuración. Para facilitar su uso, también se pueden agregar un par de botones, algunos LED y algunos pines de periféricos.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012155857.png)

## Alimentación

### Entrada

- VIN_AC: entrada de alimentación principal (DC5V@2A), se pueden agregar fusibles, ferritas, diodos de protección y otros dispositivos según sea necesario.
- VIN_USB: entrada de alimentación USB (DC5V@0.5A, se puede aumentar a 1.3A a través del PMIC interno), también se utiliza como voltaje y corriente de referencia para el host USB 2.0.
- VIN_BAT: se puede utilizar como entrada de batería (con alimentación de batería de 2.75-5.5V) o salida (para cargar la batería), no se puede utilizar como entrada de eventos.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211012173057.png)

### Salida

- SYS_VOUT: igual al voltaje del PMIC de entrada, tenga en cuenta que los componentes conectados a este pin deben ser capaces de funcionar en el rango de 3-5V, ya que el PMIC cambia la entrada de alimentación cuando se carga la batería.
- SYS_VDD1_3P3V: salida de 3.3V proporcionada por el LDO TL5209 y habilitada por el LDO4 del PMIC, como salida de alimentación principal.
- SYS_VDD2_3P3V: salida de 3.3V proporcionada por el LDO2 del PMIC.
- SYS_RTC_1P8V: salida de 1.8V proporcionada por el LDO1 del PMIC, también se utiliza para alimentar el RTC interno de AM335x.
- SYS_VDD_1P8V: salida de 1.8V proporcionada por el LDO3 del PMIC.
- SYS_ADC_1P8V: salida de 1.8V proporcionada por el LDO3 del PMIC, con filtrado para aplicaciones analógicas y también para alimentar el ADC de AM335x internamente.

Se recomienda agregar puntos de prueba para todas las salidas de alimentación para facilitar la depuración.

También hay algunos pines de alimentación interna: VDDSHV_3P3V, VDDS_DDR, VDD_MPU, VDD_CORE, VDDS_PLL. Solo se utilizan para medición de puntos de prueba, no se deben utilizar para circuitos externos.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013142917.png)

### Entrada y tierra de referencia analógica

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013143532.png)

El OSD335x tiene una interfaz ADC, por lo que es necesario utilizar correctamente la alimentación y la tierra analógicas si se desea utilizar el ADC. La interfaz ADC puede soportar una entrada analógica máxima de 1.8V (consulte el pin VREFP). Por lo general, VREFP se puede conectar directamente a SYS_ADC_1P8V, pero si es necesario, se puede dividir a un voltaje más bajo.

### Gestión de energía

Dentro del OSD335x, el AM335x se comunica con el PMIC TPS65217C a través de I2C0.

I2C0 tiene una resistencia de pull-up de 4.7k interna, pero es mejor agregar una resistencia de pull-up adicional en el exterior si se va a utilizar un dispositivo.

El PMIC TPS65217C se puede configurar a través de I2C para ajustar los siguientes parámetros:

- Voltaje de carga de la batería
- Control de tiempo de carga segura
- Voltaje de salida Buck/Boost
- Voltaje de salida LDO
- Secuencia de encendido/apagado
- Umbral de sobrecorriente y sobrecalentamiento

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013161739.png)

Además de la conexión a través de I2C, el PMIC también tiene algunos pines de función que deben conectarse al OSD335x:

- PMIC_POWER_EN: utilizado por AM335x para controlar la secuencia de encendido del PMIC
- PMIC_IN_PWR_EN: habilita los buck y LDO del PMIC, y comienza el control de la secuencia de encendido cuando se aplica un nivel alto
- RTC_PWRONRSTN: pin de reinicio de energía independiente del RTC de AM335x
- PMIC_OUT_LDO_PGOOD: estado de salida de LDO1 y LDO2, un nivel alto indica una buena salida y un nivel bajo indica una salida anormal de cualquier LDO.
- EXT_WAKEUP: pin de activación externa
- PMIC_OUT_NWAKEUP: pin de activación externa del host (activo en nivel bajo)
- EXTINTN: pin de entrada de interrupción externa de AM335x
- PMIC_OUT_NINT: pin de salida terminal del PMIC (activo en nivel bajo)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013161927.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013163119.png)

### Botón de encendido

El PMIC TPS65217C tiene una entrada de reinicio activa en nivel bajo que se conecta al OSD335x a través del pin PMIC_IN_PB_IN, y también se puede conectar a un botón externo. Este pin de entrada tiene un tiempo de rebote de 50 ms y una resistencia de pull-up interna. Además, el botón de encendido tiene las siguientes funciones:

- Cuando se detecta una transición de nivel bajo en PMIC_IN_PB_IN, el PMIC se despertará del modo de apagado o suspensión.
- Si PMIC_IN_PB_IN se mantiene en nivel bajo durante más de 8 segundos, el PMIC se reiniciará/encenderá de nuevo.
- Si PMIC_IN_PB_IN se mantiene en nivel bajo durante mucho tiempo, el dispositivo continuará alternando entre los estados ACTIVO y RESET, con un intervalo de 8 segundos para cada reinicio.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211013165738.png)

### Indicador de alimentación

Utilizamos SYS_VDD2_3P3V (150mA) como salida del indicador de alimentación.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014092054.png)

## Reinicio

El OSD335x tiene varios métodos de reinicio:

- Reinicio en frío (reinicio al encender): se realiza al encender el dispositivo y el dominio de alimentación.
- Reinicio en caliente
  - Es un reinicio parcial que no afecta a la lógica global.
  - Se utiliza para reducir el tiempo de recuperación del reinicio.

El OSD335x tiene 3 entradas de reinicio (con el mismo nombre que las entradas de reinicio en AM335x):

- PWRONRSTN: reinicio en frío; debe mantenerse en nivel bajo durante el encendido hasta que todas las líneas de alimentación de entrada estén estables; no se puede bloquear y afecta a todo el sistema excepto al RTC.
- WARMRSTN: reinicio en caliente; algunos registros de módulos de control y gestión de energía, reinicio y reloj no son sensibles al reinicio en caliente.
- RTC_PWRONRSTN: entrada de reinicio de encendido especializada para el módulo RTC que no se ve afectada por el reinicio en frío, y que no afecta a otras partes del dispositivo.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014105556.png)

## Reloj

### OSC0 y OSC1

El OSD335x tiene dos entradas de reloj:

- OSC0: Entrada de reloj de alta velocidad (reloj principal), funciona a una frecuencia de 19.2MHz, 24MHz (recomendado), 25MHz o 26MHz. Esta fuente de reloj proporciona referencia para todas las funciones que no son RTC. La entrada de reloj OSC0 tiene pines OSC0_IN, OSC0_OUT y OSC0_GND.
- OSC1: Entrada de reloj de baja velocidad, funciona a 32.768kHz y proporciona energía para RTC. La entrada de reloj OSC1 tiene pines OSC1_IN, OSC1_OUT y OSC1_GND. Esta fuente de reloj está desactivada de forma predeterminada y no es necesaria, pero puede recibir una señal de cristal RC interno de 32kHz si es necesario.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014095242.png)

En la figura anterior, Rbias y Rd son opcionales. Si no se puede proporcionar una frecuencia precisa, Rbias se puede utilizar para calibrar de forma flexible y se puede DNP (no incluir en el esquema original o dejar un espacio vacío). Pero si no se necesita Rd, debe reemplazarse con un cable para evitar un circuito abierto.

En el diseño de referencia, se utiliza un cristal de 24MHz 7A-24.000MAAJ-T, un condensador de 18pF y una resistencia de 1MΩ como Rbias para OSC0.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014101932.png)

El pin RTC_KALDO_ENN tiene una resistencia externa de 10k para habilitar el LDO RTC interno de forma predeterminada.

## Interfaz de programación y depuración

En el diseño de referencia, se utiliza la interfaz JTAG.

https://octavosystems.com/octavosystems.com/wp-content/uploads/2017/07/JTAG.jpg

## Otros periféricos

### Configuración de inicio

La tabla de configuración de inicio se puede consultar en la sección **SYSBOOT Configuration Pins** del [**Manual de referencia técnica (TRM) de AM335x**](http://www.ti.com/lit/pdf/spruh73).

En el diseño de referencia, se realiza la siguiente configuración:

- Se establece la frecuencia del reloj en 24Mhz.
- Se desactiva la salida CLKOUT1 a través de XDMA_EVENT_INTR0, que solo se utiliza para la simulación JTAG.
- Se establece el orden de inicio en SPI0 -> MMC0 -> USB0 -> UART0.

### Botones y LED de usuario

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110906.png)

### Pines de periféricos

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211014110947.png)

## Referencias y agradecimientos

- [SO YOU WANT TO BUILD AN EMBEDDED LINUX SYSTEM?](https://jaycarlson.net/embedded-linux/#)
- [OSD335x-SM System-in-Package Smallest AM335x Module, Quickest Design](https://octavosystems.com/octavo_products/osd335x-sm/#Technical%20Documents)
- [OSD335x Reference Design Tutorial Series](https://octavosystems.com/app_notes/osd335x-design-tutorial/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
