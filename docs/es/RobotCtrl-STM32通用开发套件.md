# RobotCtrl - Kit de Desarrollo Universal STM32

![RobotCtrl](https://media.wiki-power.com/img/20220416181125.jpeg)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl**](https://github.com/linyuxuanlin/RobotCtrl)

RobotCtrl, el Kit de Desarrollo Universal STM32, consta de tres placas:

- [**RobotCtrl_Core - Placa Principal**](https://wiki-power.com/RobotCtrl_Core-%E6%A0%B8%E5%BF%83%E6%9D%BF)
- [**RobotCtrl_Core - Placa de Expansión de Periféricos**](https://wiki-power.com/RobotCtrl_Func-%E5%A4%96%E8%AE%BE%E6%8B%93%E5%B1%95%E6%9D%BF)
- [**RobotCtrl_Power - Placa de Suministro de Energía**](https://wiki-power.com/RobotCtrl_Power-%E7%94%B5%E6%BA%90%E4%BE%9B%E7%94%B5%E6%9D%BF)

## Requisitos de Diseño

![Diseño](https://media.wiki-power.com/img/20220527111854.png)

Nota: Lo siguiente es un resumen de diseño. Para obtener información detallada, por favor diríjase a los artículos relacionados.

### Enfoque de Diseño para RobotCtrl_Core

El diseño de la placa principal, RobotCtrl_Core, incluye circuitos de alimentación, el sistema mínimo del microcontrolador, comunicación USB, conectores B2B, teclas de usuario y sección de LED.

Para el circuito de alimentación, se utiliza un regulador LDO debido a su simplicidad, baja ondulación de salida, costo reducido y un área de diseño compacta. Junto con capacitores de desacople y un indicador de energía, se regula y convierte la tensión de entrada de 5V desde el puerto USB o conector B2B a 3.3V (con una corriente máxima de 1A).

En el diseño del sistema mínimo, la alimentación es de 3.3V con capacitores de desacople correspondientes. Además, la alimentación dedicada para el ADC (VDDA) se conecta a través de una inductancia de 120Ω y se agrega capacitancia adicional para el desacople. El circuito de reinicio incluye un botón externo que, al activarse, lleva la señal NRST a un nivel bajo para reiniciar el sistema. El circuito de reloj incorpora un oscilador externo de alta velocidad (HSE) conectado a los pines OSC_IN y OSC_OUT, y el modo de arranque se configura por defecto para iniciar desde la memoria Flash incorporada en el chip. Esto se logra con la señal BOOT0 en nivel bajo y BOOT1 en cualquier nivel, usando una resistencia de 10k para llevar BOOT0 a tierra. El circuito de depuración y descarga dirige directamente la interfaz SW (DIO/CLK).

El diseño del circuito de comunicación USB aprovecha el USB periférico incorporado en el STM32F4. Se utiliza un conector USB Micro, con resistencias de limitación de corriente de 10Ω en serie en las líneas de señal y de alimentación, junto con diodos TVS y diodos ESD en cada línea para cumplir con los requisitos de compatibilidad electromagnética (EMC).

El conector B2B se utiliza para la alimentación y comunicación de datos entre RobotCtrl_Core y RobotCtrl_Func. En este diseño, dos conectores B2B son suficientes para llevar todas las E/S del microcontrolador STM32F407ZE, lo que mejora la capacidad de expansión futura.

### Enfoque de Diseño para RobotCtrl_Func

El diseño de la placa de expansión, RobotCtrl_Func, incluye circuitos para comunicación serie (RS-232/TTL), comunicación CAN, comunicación Ethernet, sensores de actitud, interfaz ultrasónica, interfaz de medición de distancia infrarroja (con aislamiento óptico), zumbador, interfaz de depuración por SW, teclas de usuario y LED, E/S GPIO general, alimentación y conectores B2B, entre otros módulos.

El circuito de comunicación serie proporciona interfaces de nivel TTL y RS-232. La interfaz TTL está conectada directamente a los pines TX/RX de USART1 y UART5, mientras que el circuito de comunicación RS-232 utiliza un chip para convertir el nivel TTL del microcontrolador a nivel RS-232. Para mejorar el rendimiento de compatibilidad electromagnética, la carcasa del conector DB9 se conecta a tierra a través de diodos TVS. Además, el chip de conversión TTL a RS-232 requiere capacitores de desacople y capacitores de autoarranque.

El circuito de comunicación CAN se basa en chips de transmisión y recepción CAN que utilizan la transmisión de nivel diferencial de CAN. Se requiere una resistencia de terminación de 120Ω en el bus CAN para igualar la impedancia y reducir las reflexiones de la señal.

La comunicación Ethernet se basa en el chip PHY Ethernet utilizando la interfaz RMII para comunicarse con el microcontrolador. Se establece la comunicación a través del conector RJ45 con transformador de aislamiento incorporado y cableado externo. El circuito Ethernet utiliza un oscilador pasivo externo de 25 MHz y requiere alimentación independiente para reducir interferencias de energía. Se utiliza el mismo regulador de baja caída de voltaje que la placa base central para proporcionar alimentación independiente al circuito Ethernet.

El circuito de interfaz de los cuatro sensores de distancia infrarrojos se alimenta a 12V y utiliza señales de tipo NPN normalmente abiertas. Por lo tanto, se deriva una fuente de 12V desde RobotCtrl_Power para alimentarlos y se agrega un circuito de aislamiento óptico de cuatro canales para transmitir señales de alto y bajo nivel. El diseño del circuito de aislamiento óptico debe calcular la resistencia limitadora de corriente según la corriente para asegurarse de que esté dentro del rango de voltaje de disparo especificado en el manual.

El diseño del módulo de sensor de actitud utiliza el módulo MPU6050 y reserva una interfaz I2C para la comunicación con el microcontrolador.

### Concepto de diseño de RobotCtrl_Power

El diseño del esquemático de RobotCtrl_Power consta principalmente de una entrada de doble fuente XT60, circuito de regulación de 24V a 12V, circuito de regulación de 24V a 5V, interruptor de habilitación, indicador de energía, circuito de protección contra polaridad inversa, circuito de protección contra sobretensión, entre otras partes.

La entrada de energía utiliza dos conectores XT60 en paralelo. Uno se utiliza para la entrada de energía y el otro se puede usar como una fuente de energía de respaldo o para suministrar energía externa desde la batería.

El circuito de protección contra polaridad inversa se basa en un diseño con MOSFET. Cuando la conexión de energía es normal, el MOSFET está encendido, pero se apaga en caso de polaridad inversa, protegiendo el circuito. En este diseño, se utiliza un MOSFET P de fabricación nacional para la protección contra polaridad inversa, junto con una red de resistores divisores y diodos reguladores de tensión para bloquear el voltaje de puerta cuando el MOSFET está encendido en la dirección correcta. Para protección contra sobretensión y ESD, se conectan diodos bidireccionales TVS en paralelo en la entrada de energía.

El diseño del circuito de regulación de 12V/5V utiliza una solución de regulación no aislada tipo Buck basada en el LMR14050. Se seleccionan valores de resistencia de retroalimentación de acuerdo a los principios de la topología Buck y a las especificaciones del datasheet del chip, para mantener la salida en 12V/5V. Al elegir la inductancia, es importante que la corriente máxima de saturación sea mayor que la corriente pulsante con suficiente margen. Se selecciona un diodo Schottky para lograr una conmutación rápida, y sus especificaciones de tensión y corriente deben cumplir con los requisitos del circuito. Además, se conectan condensadores de desacople tanto en la entrada como en la salida para filtrar el rizado.

El interruptor de habilitación controla la activación y desactivación de la salida regulada y se conecta al pin de habilitación del chip Buck para lograr una activación y desactivación suave de la salida regulada. El indicador de energía muestra el estado de la salida regulada de 12V/5V al usuario.

## Referencias y Agradecimientos

![](https://media.wiki-power.com/img/20220416181139.jpeg)

Este proyecto es mi diseño de graduación personal. En el proceso de diseño, soldadura y depuración, me enfrenté a numerosos problemas de diversos tamaños. Con la invaluable ayuda de mi tutor, colegas y amigos, finalmente pude superar todos los obstáculos y obtener el reconocimiento de un proyecto de graduación sobresaliente. ¡Gracias a todos!

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
