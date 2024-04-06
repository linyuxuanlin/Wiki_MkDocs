# RobotCtrl_Func - Expansion Board for Peripherals

![Imagen](https://media.wiki-power.com/img/20220527113505.png)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl/RobotCtrl_Func**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func_V0.8B.zip"
  ></div>
</div>

Nota: Este proyecto está incluido en [**RobotCtrl - STM32 Kit de Desarrollo Universal**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Diseño del Esquemático

Las principales funciones de RobotCtrl_Func son las siguientes:

- Entrada de alimentación de 12V, entrada/salida de alimentación de 5V, salida de alimentación de 3.3V (con puntos de prueba)
- 2 circuitos de regulación de voltaje de 5V a 3.3V (para sensores / Ethernet, con puntos de prueba)
- Circuito de comunicación Ethernet
- 2 circuitos de comunicación CAN
- Circuito de comunicación serie (RS-232 y nivel TTL)
- Circuito de zumbador
- 2 botones de usuario
- 3 LEDs de usuario
- Módulo de sensor de actitud MPU6050
- 4 interfaces de sensor de medición de distancia por infrarrojos
- 5 interfaces ultrasónicas
- 6 interfaces de E/S de usuario
- Conector B2B (que expone todos los pines de E/S)
- Interfaz de descarga SW

### Alimentación

RobotCtrl_Func cuenta con 2 reguladores de voltaje LDO, cuyo principio es similar al de RobotCtrl_Core. Uno de ellos se utiliza para alimentar sensores externos, mientras que el otro se utiliza exclusivamente para el circuito Ethernet.

### Circuito de Comunicación Ethernet

La comunicación Ethernet se basa en un chip PHY de Ethernet, que se comunica con el microcontrolador a través de la interfaz RMII y utiliza un conector RJ45 con transformador aislante incorporado para la conexión de la red. El circuito Ethernet utiliza un oscilador pasivo externo de 25M para el reloj y requiere una alimentación independiente para reducir las interferencias de la fuente de alimentación. En este caso, se utiliza el mismo esquema de regulación de voltaje lineal de bajo dropout (LDO) que en la placa base para alimentar el circuito Ethernet de manera independiente. Para obtener más información sobre el principio de comunicación Ethernet, consulte el artículo [**HAL 库开发笔记 - 以太网通信（LwIP）**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8®­记-%E4%BB%A5%E5%A4ª网通信（LwIP）).

### Circuito de Comunicación CAN

El circuito de comunicación CAN se basa en chips transceptores CAN y utiliza la transmisión diferencial de nivel CAN. El controlador de protocolo CAN (por ejemplo, un microcontrolador) se conecta al transceptor a través de las líneas seriales (RX/TX), que se convierten en señales CAN (CANH/CANL) en el transceptor. El modo de alta velocidad/silencio se selecciona a través del pin RS. Es necesario añadir una resistencia de terminación de 120Ω en el bus CAN para que coincida con la impedancia y reducir las reflexiones de la señal. Para obtener más información sobre el principio de comunicación CAN, consulte los artículos [**通信协议 - CAN**](https://wiki-power.com/通信协议-CAN) y [**HAL 库开发笔记 - 串口通信**](https://wiki-power.com/HAL库开发笔记-CAN通信).

### Circuito de Comunicación en Serie

El circuito RobotCtrl_Func cuenta con una comunicación serie con niveles RS-232 integrada, y adicionalmente, se dispone de una comunicación USART1/UART5 con niveles TTL. Los principios de la comunicación serie se pueden consultar en los siguientes artículos: [**Protocolo de Comunicación - Comunicación Serie**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1) y [**Notas de Desarrollo de la Biblioteca HAL - Comunicación Serie**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1).

Para la comunicación RS-232, se emplea un chip que convierte los niveles TTL del microcontrolador a niveles RS-232. Con el fin de mejorar el rendimiento de compatibilidad electromagnética (EMC), los pines de conexión en el conector DB9 pueden estar conectados a un diodo TVS a tierra. El chip TTL a RS-232 requiere de una fuente de alimentación adicional y capacitores de arranque.

### Circuito del Zumbador

El circuito del zumbador utiliza un zumbador de 12V y se controla mediante un solo transistor.

### Botones del Usuario y LEDs

Los principios de funcionamiento de los botones del usuario y los LEDs se pueden consultar en RobotCtrl_Core; por lo tanto, no se profundizará en ellos aquí.

### Módulo del Sensor de Postura

Se utiliza el módulo MPU6050 montado directamente y se reserva una interfaz I2C para la comunicación con el microcontrolador. Los principios de la comunicación I2C se explican en los siguientes artículos: [**Protocolo de Comunicación - I2C**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C) y [**Notas de Desarrollo de la Biblioteca HAL - Comunicación I2C (MPU6050)**](https://wiki-power.com/HAL%E5%BA%93%E5%BC€%C5%8F%E5%8F%91%E7%AC%94%E8%AE%B0-I2C%E9%80%9A%E4%BF%A1%EF%BC%88MPU6050%EF%BC%89).

### Interfaz del Sensor de Distancia Infrarroja

El circuito de la interfaz para cuatro sensores de distancia infrarroja se configura para trabajar con una alimentación y señales de 12V (tipo NPN normalmente abierto). Para proporcionarles alimentación, se deriva una alimentación de 12V desde RobotCtrl_Power, y se añaden cuatro optoacopladores para transmitir señales de nivel alto y bajo. El diseño del circuito de optoacoplamiento requiere calcular el valor de la resistencia de limitación de corriente según la corriente utilizada para asegurarse de que se encuentre dentro del rango de voltaje de activación especificado en el manual. Los principios de funcionamiento del optoacoplador se explican en el artículo [**Componentes Básicos - Optoacopladores**](https://wiki-power.com/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E5%85%89%E7%94%B5%E8%80%A6%E5%90%88%E5%99%A8).

### Interfaz de Entrada de Alimentación y Conector B2B

La interfaz de entrada de alimentación de la placa de expansión de periféricos consta de 4 pines, que se conectan a la placa de alimentación en la parte inferior. El conector B2B se utiliza para alimentar la placa principal y para la comunicación de datos.

## Pruebas de Hardware

### Pruebas de Alimentación

Entrada de Alimentación (se requiere seguir este procedimiento para todas las pruebas):

- VCC_12V: Se conecta a través de P1.
- VCC_5V: Se conecta a través de P2 o J1_1/2.
- GND: Se conecta a través de P3, P4, J1_31/32 o J2_30/31 y se conecta a tierra externa.

Regulador de Voltaje de 5V a 3.3V (para sensores):

- VCC_3V3S: Se mide para comprobar si la tensión en los extremos de C30 es de 3.3V.

Regulador de Voltaje de 5V a 3.3V (para Ethernet):

- VCC_3V3E: Se mide para comprobar si la tensión en los extremos de C26 es de 3.3V.

### Pruebas de Sensores Integrados en la Placa

Botones del Usuario:

- Se configuran PE2/PE3 en modo de entrada con resistencia pull-up. Se lee un nivel bajo cuando se presiona el botón y un nivel alto cuando se suelta.

LEDs del Usuario:

- Se configuran PC6/PC7/PC8 en modo de salida. Se encienden los LEDs secuencialmente estableciendo niveles altos y se apagan estableciendo niveles bajos.

Módulo del Sensor de Postura MPU6050:

- Se mide si el pin 1 del módulo M1 está conectado a VCC_3V3S a tierra.
- Se verifica la conectividad de los pines de entrada/salida (IO).

Zumbador:

- Se mide si el polo positivo de BUZZER1 está conectado a VCC_12V.
- Se configura PC9 en modo de salida. El zumbador emite sonido con un nivel alto y se silencia con un nivel bajo.

Conversor Serie a RS232:

- Comprueba si los extremos de C3 tienen un voltaje de VCC_3V3S.
- Ejecuta el programa de prueba utilizando los pines PB10/PB11.

Comunicación en el bus CAN:

- Comprueba si los extremos de C10/C13 tienen un voltaje de VCC_5V.
- Ejecuta el programa de prueba (prueba de bucle) utilizando los pines PD0/PD1 y PB12/PB13.

Comunicación Ethernet:

- Comprueba si IC2_9 a tierra tiene un voltaje de VCC_3V3S.
- Comprueba si VDD1A/VDD2A a tierra tienen un voltaje de VCC_3V3E.
- Ejecuta el programa de prueba utilizando la interfaz RMII para la comunicación Ethernet.

### Pruebas de interfaz

Interfaz del sensor de distancia por infrarrojos:

- Mide si el pin 1 de los conectores J16/J17/J18/J19 está a un voltaje de VCC_12V en referencia a tierra.
- Configura PF2/PF3/PF4/PF5 como entradas con resistencia de pull-down para que IR1/IR2/IR3/IR4 estén en nivel alto (VCC_12V); si es lo contrario, estarán en nivel bajo.

Interfaz de ultrasonidos:

- Mide si el pin 4 de los conectores J3/J4/J5/J6/J7 está a un voltaje de VCC_3V3S en referencia a tierra.
- Prueba la conectividad de los pines de entrada/salida (IO).

Interfaz de GPIO de usuario:

- Mide si el pin 4 de los conectores J9/J10/J11 está a un voltaje de VCC_3V3S en referencia a tierra.
- Prueba la conectividad de los pines de entrada/salida (IO).

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
