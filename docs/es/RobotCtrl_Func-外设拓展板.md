# RobotCtrl_Func - Placa de expansión de periféricos

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527113505.png)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl/RobotCtrl_Func**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Func_V0.8B.zip"
  ></div>
</div>

Nota: el proyecto está incluido en [**RobotCtrl - Kit de desarrollo universal STM32**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Diseño del esquemático

Las principales funciones de RobotCtrl_Func son las siguientes:

- Entrada de alimentación de 12V, entrada / salida de alimentación de 5V, salida de alimentación de 3.3V (con puntos de prueba)
- 2 circuitos de regulación de voltaje de 5V a 3.3V (para sensores / Ethernet, con puntos de prueba)
- Circuito de comunicación Ethernet
- 2 circuitos de comunicación CAN
- Circuito de comunicación en serie (RS-232 y nivel TTL)
- Circuito de zumbador
- 2 botones de usuario
- 3 LED de usuario
- Módulo de sensor de actitud MPU6050
- Interfaz de sensor de distancia infrarrojo (4)
- Interfaz de ultrasonido (5)
- Interfaz GPIO de usuario (6)
- Conector B2B (con todos los IO)
- Interfaz de descarga SW

### Alimentación

RobotCtrl_Func tiene 2 LDO, similar al RobotCtrl_Core, donde uno se utiliza para sensores periféricos y el otro se utiliza para el circuito Ethernet. 

### Circuito de comunicación Ethernet

La comunicación Ethernet se basa en el chip PHY Ethernet, que se comunica con el microcontrolador a través de la interfaz RMII y se comunica a través del puerto RJ45 con aislamiento incorporado. El reloj del circuito Ethernet utiliza un oscilador pasivo externo de 25M y requiere una fuente de alimentación independiente para reducir la interferencia de la fuente de alimentación. Aquí se utiliza el mismo esquema de alimentación lineal de baja caída que en la placa principal para proporcionar energía al circuito Ethernet de forma independiente. Se puede consultar el artículo [**HAL 库开发笔记 - 以太网通信（LwIP）**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%BB%A5%E5%A4%AA%E7%BD%91%E9%80%9A%E4%BF%A1%EF%BC%88LwIP%EF%BC%89) para obtener más información sobre el principio de la comunicación Ethernet.

### Circuito de comunicación CAN

El circuito de comunicación CAN se basa en el chip transceptor CAN y se transmite a través del nivel de voltaje diferencial CAN. El controlador de protocolo CAN (como el microcontrolador) se conecta al transceptor a través de un cable serie (RX / TX), que se convierte en una señal CAN (CANH / CANL) en el transceptor y se selecciona el modo de alta velocidad / silencioso a través del pin RS. Es necesario agregar una resistencia terminal de 120Ω en el bus CAN para adaptar la impedancia y reducir la reflexión de la señal. Se puede consultar el artículo [**通信协议 - CAN**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-CAN) y [**HAL 库开发笔记 - 串口通信**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-CAN%E9%80%9A%E4%BF%A1) para obtener más información sobre el principio de la comunicación CAN.

### Circuito de comunicación en serie

La placa RobotCtrl_Func tiene un circuito de comunicación en serie con niveles RS-232 integrado y también tiene un USART1/UART5 con niveles TTL adicionales. El principio de la comunicación en serie se puede encontrar en los artículos [**Protocolo de comunicación - Comunicación en serie**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1) y [**Nota de desarrollo de la biblioteca HAL - Comunicación en serie**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1).

El circuito de comunicación RS-232 utiliza un chip que convierte los niveles TTL en niveles RS-232. Para mejorar el rendimiento de EMC, el conector DB9 tiene un pin de conexión a tierra que se puede conectar a un diodo TVS y el chip TTL a RS-232 requiere una fuente de alimentación externa y capacitores de arranque.

### Circuito del zumbador

Se utiliza un zumbador de 12V que se puede controlar con un transistor.

### Botones y LED del usuario

El principio de los botones y LED del usuario se puede encontrar en RobotCtrl_Core, por lo que no se explicará aquí.

### Módulo de sensor de actitud

Se utiliza directamente el módulo MPU6050, con una interfaz I2C reservada para la comunicación con el microcontrolador. El principio de la comunicación I2C se puede encontrar en los artículos [**Protocolo de comunicación - I2C**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-I2C) y [**Nota de desarrollo de la biblioteca HAL - Comunicación I2C (MPU6050)**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-I2C%E9%80%9A%E4%BF%A1%EF%BC%88MPU6050%EF%BC%89).

### Interfaz del sensor de distancia por infrarrojos

El circuito de la interfaz del sensor de distancia por infrarrojos consta de cuatro chips de aislamiento óptico y se alimenta con 12V y señales (tipo NPN normalmente abierto) del sensor de infrarrojos desde RobotCtrl_Power. El diseño del circuito de aislamiento óptico requiere calcular el valor de la resistencia limitadora de corriente según la corriente para garantizar que esté dentro del rango de voltaje de activación especificado en la hoja de datos. El principio del acoplador óptico se puede encontrar en el artículo [**Componentes básicos - Acoplador óptico**](https://wiki-power.com/%E5%9F%BA%E6%9C%AC%E5%85%83%E5%99%A8%E4%BB%B6-%E5%85%89%E7%94%B5%E8%80%A6%E5%90%88%E5%99%A8).

### Interfaz de entrada de alimentación y conector B2B

La interfaz de entrada de alimentación de la placa de expansión de periféricos consta de 4 pines de fila, que se conectan a la placa de alimentación inferior. El conector B2B se utiliza para suministrar energía y comunicación de datos a la placa de control principal.

## Pruebas de hardware

### Pruebas de alimentación

Entrada de alimentación (todas las pruebas deben seguir esta operación):

- VCC_12V: a través de P1.
- VCC_5V: a través de P2 o J1_1/2.
- GND: a través de P3, P4, J1_31/32 o J2_30/31 conectados a tierra externa.

Regulador de voltaje de 5V a 3.3V (para sensores):

- VCC_3V3S: mida si el voltaje en ambos extremos de C30 es de 3.3V.

Regulador de voltaje de 5V a 3.3V (para Ethernet):

- VCC_3V3E: mida si el voltaje en ambos extremos de C26 es de 3.3V.

### Pruebas de sensores integrados

Botones del usuario:

- Configure PE2/PE3 como modo de entrada de pull-up GPIO, lea un nivel bajo al presionar el botón y un nivel alto al soltarlo.

LED del usuario:

- Configure PC6/PC7/PC8 como modo de salida GPIO, emita un nivel alto y los LED se encenderán secuencialmente; emita un nivel bajo y se apagarán.

Módulo de sensor de actitud MPU6050:

- Mida si el pin 1 del módulo M1 está conectado a tierra con el voltaje VCC_3V3S.
- Pruebe la conectividad del pin IO.

Zumbador:

- Mida si el polo positivo de BUZZER1 está conectado a tierra con el voltaje VCC_12V.
- Configure PC9 como modo de salida GPIO, emita un nivel alto y el zumbador emitirá un sonido; emita un nivel bajo y no emitirá sonido.

Convertidor de serie a RS232:

Pruebas de interfaz

Medición de voltaje:

- Medir si los extremos de C3 tienen voltaje VCC_3V3S.
- Ejecutar el programa de prueba y realizar la prueba a través de los pines PB10/PB11.

Comunicación del bus CAN:

- Medir si los extremos de C10/C13 tienen voltaje VCC_5V.
- Ejecutar el programa de prueba (prueba de bucle de retroalimentación) y realizar la prueba a través de los pines PD0/PD1, PB12/PB13.

Comunicación Ethernet:

- Medir si IC2_9 a tierra tiene voltaje VCC_3V3S.
- Medir si VDD1A/VDD2A a tierra tienen voltaje VCC_3V3E.
- Ejecutar el programa de prueba y realizar la prueba de comunicación Ethernet a través de la interfaz RMII.

Pruebas de interfaz

Interfaz de sensor de distancia infrarrojo:

- Medir si el pin 1 de los conectores J16/J17/J18/J19 a tierra tiene voltaje VCC_12V.
- Configurar PF2/PF3/PF4/PF5 como entrada de pull-down GPIO, y hacer que IR1/IR2/IR3/IR4 sean altos (VCC_12V) externamente, entonces PF2/PF3/PF4/PF5 leerán un nivel alto; de lo contrario, leerán un nivel bajo.

Interfaz de ultrasonido:

- Medir si el pin 4 de los conectores J3/J4/J5/J6/J7 a tierra tiene voltaje VCC_3V3S.
- Probar la conectividad de los pines de entrada/salida.

Interfaz GPIO del usuario:

- Medir si el pin 4 de los conectores J9/J10/J11 a tierra tiene voltaje VCC_3V3S.
- Probar la conectividad de los pines de entrada/salida.

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.