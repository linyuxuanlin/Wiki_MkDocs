# RobotCtrl - Kit de desarrollo universal STM32

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220416181125.jpeg)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl**](https://github.com/linyuxuanlin/RobotCtrl)

RobotCtrl - Kit de desarrollo universal STM32 consta de tres placas:

- [**RobotCtrl_Core - Placa principal**](https://wiki-power.com/RobotCtrl_Core-%E6%A0%B8%E5%BF%83%E6%9D%BF)
- [**RobotCtrl_Core - Placa de expansión de periféricos**](https://wiki-power.com/RobotCtrl_Func-%E5%A4%96%E8%AE%BE%E6%8B%93%E5%B1%95%E6%9D%BF)
- [**RobotCtrl_Power - Placa de suministro de energía**](https://wiki-power.com/RobotCtrl_Power-%E7%94%B5%E6%BA%90%E4%BE%9B%E7%94%B5%E6%9D%BF)

## Requisitos de diseño

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527111854.png)

Nota: Lo siguiente es un resumen del diseño, para obtener información detallada, consulte los artículos relacionados.

### Idea de diseño de RobotCtrl_Core

El diseño del esquemático de RobotCtrl_Core incluye el circuito de suministro de energía, el sistema mínimo de microcontrolador, la comunicación USB, el conector B2B, la sección de botones y LED de usuario.

El circuito de suministro de energía utiliza LDO, cuyas ventajas son que el circuito es relativamente simple, la ondulación de salida es pequeña, el costo es bajo y el área de diseño es pequeña. Junto con los capacitores de desacoplamiento y la luz indicadora de alimentación correspondiente, convierte el voltaje de 5V de entrada del puerto USB o del conector B2B en un voltaje regulado de 3.3V (corriente máxima de 1A).

En el diseño del sistema mínimo, la fuente de alimentación es una entrada de 3.3V y se agrega un capacitor de desacoplamiento correspondiente. Además, la fuente de alimentación especializada ADC VDDA se conecta a VDD a través de una perla magnética de 120Ω y se agrega un capacitor de desacoplamiento adicional. El circuito de reinicio agrega un botón externo, que activa el pin NRST a un nivel bajo para reiniciar el sistema. El circuito de reloj agrega un reloj externo de alta velocidad HSE, que se conecta a OSC_IN y OSC_OUT a través de un cristal pasivo. El modo de inicio se selecciona de forma predeterminada para arrancar desde la memoria flash integrada en el chip, es decir, BOOT0 es bajo y BOOT1 es cualquier nivel, y se utiliza una resistencia de 10k para bajar BOOT0 a tierra. El circuito de descarga y depuración USB se conecta directamente a la interfaz SW (DIO/CLK).

El diseño del circuito de comunicación USB, STM32F4 tiene un periférico USB integrado. Se utiliza un conector USB Micro externo, se conecta una resistencia limitadora de corriente de 10Ω en serie en la línea de datos y se agrega un diodo TVS y ESD en la línea de señal y la línea de alimentación respectivamente para cumplir con los requisitos de EMC.

El conector B2B se utiliza para la alimentación y la comunicación de datos entre RobotCtrl_Func. En este diseño, dos conectores B2B son suficientes para sacar todos los IO del microcontrolador STM32F407ZE, lo que mejora la capacidad de expansión posterior.

### Idea de diseño de RobotCtrl_Func

El diseño del esquemático de RobotCtrl_Func incluye principalmente la comunicación serie (RS-232/TTL), la comunicación CAN, la comunicación Ethernet, el sensor de actitud, la interfaz de ultrasonidos, la interfaz de medición de distancia por infrarrojos (con aislamiento óptico), el zumbador, la interfaz de descarga y depuración SW, los botones y LED de usuario, la interfaz GPIO general, la fuente de alimentación y el conector B2B.

El circuito de comunicación serie proporciona interfaces de nivel TTL y RS-232. Entre ellas, TTL utiliza directamente los pines TX/RX de USART1 y UART5, mientras que el circuito de comunicación RS-232 utiliza un chip que convierte el nivel TTL del microcontrolador en el nivel RS-232. Para mejorar el rendimiento EMC, el conector DB9 se conecta a tierra a través de un diodo TVS y el chip TTL a RS-232 requiere un acoplamiento de alimentación adicional y un capacitor de arranque automático.

El circuito de comunicación CAN se basa en el chip de recepción y transmisión CAN y se transmite mediante un nivel de diferencial CAN. Se requiere una resistencia terminal de 120Ω en el bus CAN para adaptar la impedancia y reducir la reflexión de la señal.

La comunicación Ethernet se basa en el chip PHY Ethernet, que se comunica con el microcontrolador a través de la interfaz RMII y se comunica a través del puerto RJ45 con un cable de red externo con un transformador de aislamiento incorporado. El reloj del circuito Ethernet utiliza un oscilador pasivo externo de 25M y requiere una fuente de alimentación independiente para reducir la interferencia de la fuente de alimentación. Aquí se utiliza el mismo regulador de voltaje lineal de baja caída que la placa base para suministrar energía al circuito Ethernet de forma independiente.

El circuito de interfaz de los cuatro sensores de distancia infrarrojos se alimenta con 12V y señal (tipo NPN normalmente abierto) debido a que los sensores infrarrojos utilizan 12V, por lo que se utiliza el pin RobotCtrl_Power para suministrar energía y se agregan cuatro chips de aislamiento óptico para transmitir señales de nivel alto y bajo. El diseño del circuito de aislamiento óptico requiere el cálculo de la resistencia limitadora de corriente según el tamaño de la corriente para garantizar que esté dentro del rango de voltaje de activación especificado en la hoja de datos. El módulo del sensor de actitud utiliza el módulo MPU6050 y reserva la interfaz I2C para comunicarse con el microcontrolador.

La idea de diseño de RobotCtrl_Power se compone principalmente de una entrada de doble fuente de alimentación XT60, un circuito de regulación de voltaje de 24V a 12V y 24V a 5V, así como un interruptor de habilitación y luces indicadoras de energía, circuitos de protección contra polaridad inversa y sobretensión, entre otros.

La entrada de energía utiliza dos conectores XT60 en paralelo, uno para la entrada de energía y el otro para una fuente de energía de respaldo externa o para suministrar energía de la batería a dispositivos externos.

El circuito de protección contra polaridad inversa utiliza un diseño de MOSFET para prevenir la polaridad inversa. Cuando la fuente de alimentación está conectada normalmente, el MOSFET está en conducción; cuando hay polaridad inversa, se corta para proteger el circuito. En este diseño, se utiliza un MOSFET P chino para prevenir la polaridad inversa y se utiliza una resistencia de división y un diodo de bloqueo de voltaje para bloquear la tensión de la puerta en conducción hacia adelante. Para lograr la protección contra sobretensión y ESD, se colocan diodos TVS en paralelo en la entrada de energía.

El diseño del circuito de regulación de voltaje de 12V/5V utiliza un esquema de regulación de conmutación Buck no aislado basado en LMR14050. Según el principio de la topología Buck y la referencia del manual de datos del chip de regulación, se seleccionan los valores de resistencia de retroalimentación para mantener la salida en 12V/5V. Al seleccionar el modelo del inductor, es necesario asegurarse de que la corriente de saturación máxima sea mayor que la corriente de pulso y dejar suficiente margen; se selecciona un diodo Schottky para lograr una conmutación de alta velocidad, y su voltaje y corriente también deben cumplir con los requisitos del circuito. Además, se deben colocar capacitores de acoplamiento de tamaño adecuado en paralelo en la entrada y salida para filtrar las ondulaciones.

El interruptor de habilitación puede controlar la apertura y el cierre de la salida de regulación de voltaje, y se conecta al pin de habilitación del chip Buck para lograr una apertura suave y un cierre suave de la salida de regulación de voltaje. La luz indicadora de energía puede indicar el estado de salida de regulación de voltaje de 12V/5V al usuario.

## Referencias y agradecimientos

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220416181139.jpeg)

Este proyecto es mi proyecto de graduación personal. En el diseño, soldadura y depuración del proyecto, encontré muchos problemas grandes y pequeños. Con la ayuda de mi tutor, colegas y amigos, finalmente pude completar el proyecto con éxito y obtener el honor de un excelente proyecto de graduación. ¡Gracias a todos!

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.