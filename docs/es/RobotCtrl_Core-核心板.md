# RobotCtrl_Core - Core Board

![Imagen](https://media.wiki-power.com/img/20220527113423.png)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl/RobotCtrl_Core**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core)

Vista en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Core_V2.81B.zip"
  ></div>
</div>

Nota: Este proyecto está incluido en [**RobotCtrl - STM32 Kit de Desarrollo Universal**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Diseño del esquema

Las principales funciones de RobotCtrl_Core son las siguientes:

- Circuito de regulación de suministro de energía (de 5V a 3.3V, con puntos de prueba)
- Sistema mínimo de microcontrolador
  - Circuito de alimentación (desacoplamiento de alimentación, fuente de alimentación analógica ADC)
  - Circuito de reinicio (botón de reinicio externo)
  - Circuito de reloj (oscilador de cristal pasivo HSE)
  - Interfaz de depuración y descarga (SW)
  - Modo de arranque (selección de arranque desde la memoria flash principal)
  - Circuito de suministro de energía y comunicación USB (USB-Micro)
- Conector B2B (todos los pines de E/S disponibles)
- Periféricos integrados en la placa

### Circuito de suministro de energía

RobotCtrl_Core puede recibir una fuente de alimentación de 5V a través del puerto USB o el conector B2B, y convertirla a 3.3V para alimentar el núcleo del microcontrolador y los periféricos integrados en la placa. El circuito de regulación de energía utiliza un regulador LDO (AMS1117-3.3, con una corriente máxima de 1A) y cuenta con un indicador de alimentación, así como puntos de prueba clave reservados.

El principio básico del LDO se puede encontrar en el artículo [**Topología de fuentes de alimentación - Regulación lineal**](https://wiki-power.com/%E7%94%B5%E6%BA%90%E6%8B%93%E6%89%91-%E7%BA%BF%E6%80%A7%E7%A8%B3%E5%8E%8B).

### Sistema mínimo de microcontrolador

El diseño del sistema mínimo del microcontrolador se divide en varios aspectos: alimentación, reinicio, depuración y descarga, reloj y modo de arranque. Puede encontrar información básica en los siguientes artículos: [**Cómo diseñar un sistema mínimo para un microcontrolador**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E8%AE%BE%E8%AE%A1%E4%B8%80%E6%AC%BE%E5%8D%95%E7%89%87%E6%9C%BA%E7%9A%84%E6%9C%80%E5%B0%8F%E7%B3%BB%E7%BB%9F) y [**Desarrollo de hardware STM32F4**](https://wiki-power.com/STM32F4%E7%A1%AC%E4%BB%B6%E5%BC%80%E5%8F%91).

### Circuito de alimentación

Condensadores de desacoplamiento:

- VDD: Un condensador cerámico de 10 μF en total, además de un condensador cerámico de 100 nF cerca de cada pin de VDD.
- VDDA: Condensador cerámico de 100 nF + condensador cerámico de 1 µF.

Condensadores VCAP

- Conectar un condensador cerámico de 2.2 µF a tierra en cada par.

### Circuito de reinicio

Se habilita el monitor de alimentación, es decir, PDR_ON se sube mediante una resistencia de 120Ω. Además, se ha añadido un botón de reinicio con eliminación de rebotes hardware.

### Circuito de reloj

Se utiliza un oscilador de cristal pasivo HSE de 8M de Murata como fuente de reloj externa de alta velocidad (HSE).

### Interfaz de depuración y descarga

Este diseño expone directamente la interfaz de depuración y descarga, sin necesidad de resistencias de pull-up/pull-down externas (ya que el STM32 las integra internamente).

### Modo de arranque

Se elige arrancar desde la memoria flash principal, es decir, BOOT0 está conectado a una resistencia de 10 K de pull-down, mientras que BOOT1 es libre.

### Circuito de suministro de energía y comunicación USB (USB-Micro)

```markdown
El STM32 cuenta con un periférico USB integrado, lo que permite lograr la comunicación USB simplemente extrayendo los puertos (en el chip STM32F07ZE, se encuentran en PA11 y PA12).

El puerto USB también es compatible con la función de alimentación externa (VUSB).

## Conector B2B

Para los conectores B2B se ha seleccionado la serie 3710 de Poin2, donde la placa central RobotCtrl_Core utiliza un par de conectores 3710M060037G3FT01 (machos) y la placa de expansión RobotCtrl_Func utiliza un par de conectores F060037G0FR01 (hembras) para su combinación. Un par de conectores B2B (con un total de 120 pines) es suficiente para aprovechar al máximo todos los puertos de E/S del STM32F407ZE, optimizando el uso de los recursos del sistema.

Para obtener información adicional sobre los conectores B2B, consulte el documento [**3710F Data Sheet**](http://www.openedv.com/thread-78182-1-1.html).

## Botones y LEDs de Usuario

Para facilitar la verificación y depuración, la placa RobotCtrl_Core incluye un botón y un LED de usuario. El botón se configura como una entrada GPIO con resistencia pull-up interna y se le agrega un condensador MLCC para reducir el rebote. El LED se configura como una salida GPIO y se enciende poniendo el pin en alto; además, se coloca una resistencia en serie en el medio para limitar la corriente.

Consulte el esquema eléctrico para conocer los pines específicos.

## Pruebas de Hardware

Para la prueba de alimentación, se necesita conectar el conector USB a una fuente de alimentación de 5V (o utilizar la placa de expansión a través del conector B2B). Se debe medir un voltaje de 3.3V en el punto de prueba correspondiente. En la práctica, se obtiene un voltaje de 3.32V, lo que indica una prueba exitosa.

La prueba de funciones implica cargar el programa inicial (donde el botón de usuario controla el LED de usuario), y se evalúa el arranque, la carga del programa, el botón de reinicio y el botón de usuario, el LED de alimentación y el LED de usuario, así como la función USB. Durante la prueba práctica, el programa inicial se carga correctamente en la placa base del microcontrolador a través de ST-Link. El botón de reinicio restablece el sistema de manera adecuada, y el programa de prueba permite encender y apagar el LED de usuario mediante el botón de usuario. Al encender la alimentación, el LED de alimentación se enciende correctamente. La prueba de la función USB utiliza un programa de puerto serie virtual USB, que al abrirse en una herramienta de puerto serie (a cualquier velocidad de transmisión) envía caracteres y los devuelve, lo que demuestra su funcionamiento adecuado.

## Referencias y Agradecimientos

- [Explicación detallada del pin PDR_ON del STM32 (Reimpresión + Complemento)](https://blog.csdn.net/Frankenstien_/article/details/105971841)
- [Capítulo 56 de la serie "Explorador STM32-F407" de Poin2: Experimento de lector de tarjetas USB (modo Esclavo)](https://zhuanlan.zhihu.com/p/136163591)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
