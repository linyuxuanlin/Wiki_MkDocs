# TinyDVR - Pequeño pero poderoso

—— Basado en TinyDVR Master V1.1 & Slave V7.2 Release

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191345.jpg)

TinyDVR es un kit de accionamiento de motor que incluye una placa base (Master) y una placa secundaria (Slave). La parte de alimentación y la parte de accionamiento están separadas, lo que reduce significativamente el tamaño en comparación con su predecesor ZenDriver y mejora en gran medida la escalabilidad. Puede apilar diferentes cantidades de placas secundarias según sus necesidades para controlar n motores.

Repositorio del proyecto: [**linyuxuanlin/TinyDVR**](https://github.com/linyuxuanlin/TinyDVR)

Vista previa en línea del proyecto:

**TinyDVR_Master**：

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Master.zip"
  ></div>
</div>

**TinyDVR_Slave**：

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Slave.zip"
  ></div>
</div>

## Parámetros básicos

1. Voltaje de entrada: **7.2 ~ 20 V**
2. Corriente de salida: **0 ~ 68 A**
3. Proporciona una salida de alimentación de **5V / 3A** para el controlador y otros módulos.
4. Dispositivos de protección: circuito integrado de protección contra polaridad inversa y aislamiento óptico.
5. Conexión sencilla del motor: para motores reductores de corriente continua comunes en el mercado (con codificador), se pueden conectar directamente con un cable plano de 6 pines (sin necesidad de cruzar cables).
6. Escalable: una placa base puede apilar n placas secundarias para controlar n motores.

## Definición de interfaces

### TinyDVR Master

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191439.png)

### TinyDVR Slave

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200125191457.png)

Explicación detallada de los pines traseros:

- \+ : Proporciona una salida de alimentación de 5V / 3A
- 1 : Puerto IN1, entrada de señal PWM 1
- 2 : Puerto IN2, entrada de señal PWM 2
- A : Puerto de señal de fase A del codificador
- B : Puerto de señal de fase B del codificador
- \- : GND

## Guía de uso

### Método de prueba

1. Conecte la alimentación de la batería de **7.2 ~ 20 V**
2. Conecte el motor correspondiente en la placa secundaria correspondiente
3. Conecte la salida de alimentación de **5V** a los puertos **IN1/ IN2** respectivamente. En este momento, el motor girará en **dirección positiva / negativa**.

### Conexión con microcontrolador

4. Conecte la alimentación de la batería de **7.2 ~ 20 V**
5. Conecte el motor correspondiente en la placa secundaria correspondiente
6. Conexión a tierra común (conectar GND de la placa de accionamiento con GND del microcontrolador)
7. Los puertos IN1 e IN2 se conectan a los puertos PWM correspondientes del microcontrolador (configuración en el código)
8. Método de prueba: consulte el programa de prueba en el repositorio del proyecto.

## Detalles interesantes

Placa secundaria temprana:
![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182442.jpg)

Soldadura en masa:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200311182441.jpg)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
