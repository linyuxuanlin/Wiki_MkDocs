# RobotCtrl_Core - Placa central

![](https://img.wiki-power.com/d/wiki-media/img/20220527113423.png)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl/RobotCtrl_Core**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core_V2.81B.zip"
  ></div>
</div>

Nota: el proyecto está incluido en [**RobotCtrl - Kit de desarrollo universal STM32**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Diseño del esquemático

Las principales funciones de RobotCtrl_Core son las siguientes:

- Circuito de regulación de alimentación (5V a 3.3V, con puntos de prueba)
- Sistema mínimo de microcontrolador
  - Circuito de alimentación (desacoplamiento de alimentación, fuente de alimentación analógica ADC)
  - Circuito de reinicio (botón de reinicio externo)
  - Circuito de reloj (oscilador pasivo HSE)
  - Interfaz de descarga y depuración (SW)
  - Modo de arranque (seleccionar el arranque desde la memoria flash principal)
  - Circuito de alimentación y comunicación USB (USB-Micro)
- Conector B2B (con todos los IO)
- Periféricos integrados en la placa

### Circuito de alimentación

RobotCtrl_Core puede recibir una fuente de alimentación de 5V a través del puerto USB o del conector B2B, y convertirla en una fuente de 3.3V para el núcleo del microcontrolador y los periféricos integrados en la placa. El circuito de regulación de alimentación utiliza un LDO (AMS1117-3.3, con una corriente máxima de 1A), incluye un indicador de alimentación y tiene puntos de prueba clave reservados.

El principio básico del LDO se puede encontrar en el artículo [**Topología de alimentación - Regulación lineal**](https://wiki-power.com/es/%E7%94%B5%E6%BA%90%E6%8B%93%E6%89%91-%E7%BA%BF%E6%80%A7%E7%A8%B3%E5%8E%8B).

### Sistema mínimo de microcontrolador

El diseño del sistema mínimo de microcontrolador se divide en varias partes: alimentación, reinicio, descarga y depuración, reloj y modo de arranque. Se pueden encontrar conocimientos básicos en los artículos [**Cómo diseñar el sistema mínimo de un microcontrolador**](https://wiki-power.com/es/%E5%A6%82%E4%BD%95%E8%AE%BE%E8%AE%A1%E4%B8%80%E6%AC%BE%E5%8D%95%E7%89%87%E6%9C%BA%E7%9A%84%E6%9C%80%E5%B0%8F%E7%B3%BB%E7%BB%9F) y [**Desarrollo de hardware STM32F4**](https://wiki-power.com/es/STM32F4%E7%A1%AC%E4%BB%B6%E5%BC%80%E5%8F%91).

### Circuito de alimentación

Capacitores de desacoplamiento:

- VDD: un capacitor cerámico total de 10 μF, más un capacitor cerámico de 100 nF junto a cada pin VDD.
- VDDA: un capacitor cerámico de 100 nF + un capacitor cerámico de 1 µF.

Capacitores VCAP

- Conectar cada uno a tierra con un capacitor cerámico de 2.2 µF.

### Circuito de reinicio

Se utiliza un monitor de alimentación, es decir, PDR_ON se tira hacia arriba a través de una resistencia de 120Ω. Además, se ha añadido un botón de reinicio con un sistema antirrebote de hardware.

### Circuito de reloj

Se utiliza un oscilador pasivo HSE de 8M de Murata.

### Interfaz de descarga y depuración

Este diseño tiene una interfaz de descarga y depuración directamente conectada, sin necesidad de resistencias de pull-up/pull-down externas (ya que están integradas en el STM32).

### Modo de arranque

Seleccionar el arranque desde la memoria flash principal, es decir, BOOT0 se conecta en serie con una resistencia de 10 K, y BOOT1 es arbitrario.

### Circuito de alimentación y comunicación USB (USB-Micro)

El STM32 tiene un periférico USB incorporado, por lo que solo es necesario sacar el puerto (en el chip STM32F07ZE es PA11 y PA12) para lograr la comunicación USB.

La interfaz USB también admite la función de alimentación externa (VUSB).

## Conector B2B

El conector B2B utiliza la serie 3710 de Elecrow, la placa central RobotCtrl_Core utiliza un par de 3710M060037G3FT01 (macho) y la placa de expansión RobotCtrl_Func utiliza un par de F060037G0FR01 (hembra) para la combinación. Un par de B2B (120 pines en total) es suficiente para sacar todos los IO del STM32F407ZE y maximizar el uso de los recursos del sistema.

Consulte la [hoja de datos del terminal 3710F](http://www.openedv.com/thread-78182-1-1.html) para obtener información sobre el conector B2B.

## Botón de usuario y LED

Para poder realizar una verificación y depuración simples, RobotCtrl_Core tiene un botón de usuario y un LED de usuario integrados. El botón está configurado como modo de entrada GPIO, con una resistencia de pull-up interna y un condensador MLCC para evitar el rebote del hardware. El LED está configurado como modo de salida GPIO, con el pin en alto para encenderlo y una resistencia en serie para limitar la corriente.

Consulte el esquemático para obtener información específica sobre los pines.

## Pruebas de hardware

Las pruebas de alimentación deben realizarse con una fuente de alimentación de 5V conectada al puerto USB (o mediante la placa de expansión de dispositivos externos a través del conector B2B), y midiendo el voltaje correspondiente en el punto de prueba de 3.3V. La prueba real dio como resultado 3.32V, lo que fue validado.

Las pruebas de función se realizaron mediante la grabación del programa inicial (el botón de usuario controla el LED de usuario), y se probaron el encendido, la grabación del programa, los botones de reinicio y de usuario, los LED de alimentación y de usuario, y la función USB. En las pruebas reales, el programa inicial se grabó correctamente en la placa central del microcontrolador a través de ST-Link. El botón de reinicio reinició el sistema correctamente; en el programa de prueba, el LED de usuario se encendió/apagó mediante el botón de usuario; al encenderse, el LED de alimentación se encendió correctamente. La prueba de la función USB utilizó un programa de puerto serie virtual USB, abriendo la herramienta de puerto serie (con cualquier velocidad de transmisión), enviando cualquier carácter y recibiendo el mismo carácter, lo que validó la función.

## Referencias y agradecimientos

- [Explicación detallada del pin PDR_ON de STM32 (reimpresión + complemento)](https://blog.csdn.net/Frankenstien_/article/details/105971841)
- [Capítulo 56 de Elecrow [STM32-F407 Explorer] Experimento de lector de tarjetas USB (esclavo)](https://zhuanlan.zhihu.com/p/136163591)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
