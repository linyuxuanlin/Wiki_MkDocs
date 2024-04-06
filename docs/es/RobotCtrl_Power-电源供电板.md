# RobotCtrl_Power - Placa de suministro de energía eléctrica

![Imagen](https://media.wiki-power.com/img/20220527113517.png)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl/RobotCtrl_Power**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power_V0.3B.zip"
  ></div>
</div>

Nota: Este proyecto forma parte de [**RobotCtrl - Kit de desarrollo general STM32**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Diseño del esquemático

Las principales funciones de RobotCtrl_Power son las siguientes:

- Entrada de energía de 24V (teóricamente acepta de 15V a 40V).
- Regulador de voltaje de batería a 12V/5A (con interruptor de habilitación y luces indicadoras).
- Regulador de voltaje de batería a 5V/5A (con interruptor de habilitación y luces indicadoras).
- Protección contra inversión de polaridad (P-MOS).
- Protección contra sobretensión (activada a partir de 30V).
- Conectores de salida de energía de batería, 12V y 5V.

### Entrada de energía

La entrada de energía utiliza dos conectores XT60PW-M para redundancia de energía dual (también se pueden usar uno como entrada y otro como salida) y proporciona dos filas de pines para pruebas de salida.

La función de protección contra inversión de polaridad se logra mediante P-MOS. A pesar de que los conectores XT60 están diseñados para evitar conexiones incorrectas, es importante prevenir la posibilidad de que los cables de energía positivos y negativos se suelden incorrectamente. Cuando hay una inversión de polaridad, el P-MOS no se activa, evitando que la energía fluya al sistema. Puedes obtener más información sobre el diseño de la función de protección contra inversión de polaridad en el artículo [**Diseño de circuitos de protección contra inversión de polaridad**](https://wiki-power.com/%E9%98%B2%E5%8F%8D%E6%8E%A5%E7%94%B5%E8%B7%AF%E7%9A%84%E8%AE%BE%E8%AE%A1).

La protección contra sobretensión transitoria y la protección contra ESD se realizan mediante diodos TVS, que desvían el exceso de voltaje cuando este supera los 30V, protegiendo así el sistema.

### Circuitos de regulación de 12V y 5V

Para los circuitos de regulación de 12V y 5V se utilizan dos reguladores TI LMR14050 DC-DC Buck, cada uno de los cuales puede proporcionar hasta 5A de corriente. Puedes obtener información detallada sobre el diseño en el artículo [**Solución de fuente de alimentación (Buck) - LMR14050**](https://wiki-power.com/%E7%94%B5%E6%BA%90%E6%96%B9%E6%A1%88%EF%BC%88Buck%EF%BC%89-LMR14050).

Además, se ha añadido un interruptor de habilitación y luces indicadoras a cada circuito de regulación.

### Puertos de salida de energía

Los puertos de VBAT, 12V y 5V utilizan un par de conectores de 4 pines cada uno. El puerto de 12V tiene un conector adicional KF2EDGR-3.81 para proporcionar energía a sensores especiales.

## Diseño de PCB

En el diseño del PCB de RobotCtrl_Power, es importante colocar las resistencias divisoras de voltaje de retroalimentación lo más cerca posible de los pines FB del chip, y la ruta de muestreo Vout debe seguir la trayectoria de generación de ruido fundamental (lazo de inductor-diodo) y preferiblemente pasar a través de orificios pasantes después de la capa de blindaje. Los inductores deben colocarse cerca del pin SW para reducir el ruido magnético y el ruido estático. Los nodos de conexión a tierra de los diodos, los condensadores de entrada y salida deben ser lo más pequeños posible y preferiblemente conectarse a una única ubicación de tierra del sistema para minimizar la conducción de ruido en la capa de tierra del sistema. Los condensadores de salida deben colocarse cerca de los nodos de los inductores y los diodos, y las rutas de señal deben ser cortas y anchas para reducir la conducción y radiación de ruido y mejorar la eficiencia.

El PCB de RobotCtrl_Power consta de una capa superior y una capa inferior para señales y alimentación, con dos capas de plano de tierra intercaladas para mejorar la integridad de señal y alimentación.

## Pruebas de hardware

- **Prueba de Protección contra Polaridad Inversa:** Comprobar si el sistema puede permanecer apagado cuando se invierte la polaridad de la tensión de entrada.

- **Interruptor de Habilitación y Luz de Indicación de Alimentación:** Verificar si el sistema puede funcionar adecuadamente.

- **Salida:** Evaluar si las salidas de 12V/5V cumplen con las especificaciones y medir el nivel de ondulación.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
