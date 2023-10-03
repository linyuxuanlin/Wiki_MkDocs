# RobotCtrl_Power - Placa de alimentación

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220527113517.png)

Repositorio del proyecto: [**linyuxuanlin/RobotCtrl/RobotCtrl_Power**](https://github.com/linyuxuanlin/RobotCtrl/tree/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/RobotCtrl/raw/main/RobotCtrl_MultiBoard_Project/RobotCtrl_Power_V0.3B.zip"
  ></div>
</div>

Nota: el proyecto está incluido en [**RobotCtrl - Kit de desarrollo universal STM32**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Diseño del esquemático

Las principales funciones de RobotCtrl_Power son las siguientes:

- Entrada de alimentación de 24V (teóricamente puede ser de 15-40V)
- Regulador de voltaje de batería a 12V/5A (con interruptor de habilitación y luz indicadora)
- Regulador de voltaje de batería a 5V/5A (con interruptor de habilitación y luz indicadora)
- Protección contra polaridad inversa (P-MOS)
- Protección contra sobretensión (comienza a proteger por encima de 30V)
- Interfaces de salida de alimentación de batería, alimentación de 12V y alimentación de 5V

### Entrada de alimentación

Se utilizan dos conectores XT60PW-M para la entrada de alimentación, como entrada de alimentación de respaldo doble (también se puede utilizar como una entrada y una salida), y se proporcionan dos filas de pines para pruebas de salida.

La función de protección contra polaridad inversa se implementa mediante P-MOS. Aunque XT60 tiene un diseño a prueba de errores, aún es necesario evitar la soldadura inversa de los cables de alimentación positivo y negativo. Cuando se invierte la polaridad, el P-MOS no se encenderá y la alimentación no se suministrará al sistema. El diseño de la función de protección contra polaridad inversa se puede consultar en el artículo [**Diseño de circuitos de protección contra polaridad inversa**](https://wiki-power.com/es/%E9%98%B2%E5%8F%8D%E6%8E%A5%E7%94%B5%E8%B7%AF%E7%9A%84%E8%AE%BE%E8%AE%A1).

La protección contra sobretensión transitoria y la protección contra ESD se realizan mediante un diodo TVS. Cuando se conecta una tensión superior a 30V, el diodo TVS desvía el exceso de voltaje para proteger el sistema.

### Circuitos reguladores de voltaje de 12V y 5V

Los circuitos reguladores de voltaje de 12V y 5V utilizan el esquema Buck DC-DC LMR14050 de TI para dos rutas, cada una de las cuales puede soportar una corriente máxima de 5A. El diseño específico se puede consultar en el artículo [**Esquema de alimentación (Buck) - LMR14050**](https://wiki-power.com/es/%E7%94%B5%E6%BA%90%E6%96%B9%E6%A1%88%EF%BC%88Buck%EF%BC%89-LMR14050).

Además, cada ruta tiene un interruptor de habilitación y una luz indicadora de alimentación.

### Puertos de salida de alimentación

VBAT, 12V y 5V de salida utilizan un par de pines de 4 pines cada uno, y la salida de 12V también utiliza un conector KF2EDGR-3.81 para suministrar energía a sensores especiales.

## Diseño de PCB

El diseño de PCB de RobotCtrl_Power requiere que las resistencias de división de voltaje de retroalimentación estén lo más cerca posible del pin FB del chip, y que la ruta de muestreo de Vout se genere lo más cerca posible del camino de generación de ruido de la teoría de la inductancia y el diodo, preferiblemente a través de un orificio pasante en la capa de blindaje. El inductor debe colocarse cerca del pin SW para reducir el ruido magnético y el ruido electrostático; los nodos de conexión a tierra de los diodos, los capacitores de entrada y salida deben ser lo más pequeños posible, y preferiblemente conectarse a la tierra del sistema en un solo punto para minimizar el ruido de conducción en la capa de tierra del sistema; los capacitores de salida deben colocarse lo más cerca posible de los nodos del inductor y el diodo, y las líneas deben ser cortas y gruesas para reducir el ruido de conducción y radiación y mejorar la eficiencia.

El diseño de PCB de RobotCtrl_Power utiliza señales y alimentación en la capa superior e inferior, e inserta dos capas de plano de tierra en el medio para mejorar la integridad de la señal y la alimentación.

## Pruebas de hardware

- Prueba de protección contra inversión de polaridad: ¿el sistema puede funcionar sin encenderse cuando se invierte la polaridad de entrada de voltaje?
- Interruptor de habilitación y luz indicadora de alimentación: prueba si pueden funcionar correctamente.
- Salida: prueba si las salidas de 12V/5V cumplen con los estándares y el tamaño de la ondulación.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.