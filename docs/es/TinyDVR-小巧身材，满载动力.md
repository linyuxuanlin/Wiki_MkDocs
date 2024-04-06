# TinyDVR - Compacto y Potente

—— Basado en la versión Master V1.1 y Slave V7.2 de TinyDVR

![](https://media.wiki-power.com/img/20200125191345.jpg)

TinyDVR es un conjunto de controladores de motores que incluye una placa madre (Master) y una placa secundaria (Slave). La sección de alimentación y la de control se encuentran separadas, lo que, en comparación con su predecesor ZenDriver, reduce significativamente el tamaño y aumenta en gran medida la capacidad de expansión. Puedes apilar diferentes cantidades de placas secundarias según tus necesidades, lo que te permite controlar n motores.

Repositorio del proyecto: [**linyuxuanlin/TinyDVR**](https://github.com/linyuxuanlin/TinyDVR)

Vista previa en línea del proyecto:

**TinyDVR_Master**:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Master.zip"
  ></div>
</div>

**TinyDVR_Slave**:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/TinyDVR/raw/master/TinyDVR_Slave.zip"
  ></div>
</div>

## Especificaciones Básicas

1. Voltaje de entrada: **7.2 ~ 20 V**
2. Corriente de salida: **0 ~ 68 A**
3. Proporciona una salida de **5V / 3A** para su uso en controladores y otros módulos.
4. Dispositivos de protección: circuitos integrados de protección contra inversión de polaridad y aislamiento óptico.
5. Conexión sencilla para motores: es compatible con motores de corriente continua de reducción comunes en el mercado (con codificador), que se pueden conectar directamente mediante un conector de 6 pines (sin necesidad de invertir la polaridad).
6. Expandible: una placa madre puede apilar n placas secundarias para controlar n motores.

## Definición de Interfaz

### TinyDVR Master

![](https://media.wiki-power.com/img/20200125191439.png)

### TinyDVR Slave

![](https://media.wiki-power.com/img/20200125191457.png)

Detalle de los pines en la parte posterior:

- \+ : Proporciona una salida de 5V / 3A
- 1 : Puerto IN1, entrada de la señal PWM 1
- 2 : Puerto IN2, entrada de la señal PWM 2
- A : Puerto de señal de fase A del codificador
- B : Puerto de señal de fase B del codificador
- \- : GND

## Guía de Uso

### Método de Prueba

1. Conecta una fuente de alimentación de **7.2 ~ 20 V**
2. Conecta un motor en la placa secundaria correspondiente
3. Conecta el puerto de suministro de **5V** a los puertos **IN1/IN2**, en este punto el motor girará en **dirección positiva / negativa**

### Conexión a un Microcontrolador

4. Conecta una fuente de alimentación de **7.2 ~ 20 V**
5. Conecta un motor en la placa secundaria correspondiente
6. Conecta el cable de tierra en la placa controladora al cable de tierra del microcontrolador
7. Conecta los puertos IN1 e IN2 al puerto PWM correspondiente del microcontrolador (configurado en el código)
8. Para obtener instrucciones detalladas, consulta los ejemplos de prueba en el repositorio del proyecto.

## Curiosidades

Placas secundarias tempranas:
![](https://media.wiki-power.com/img/20200311182442.jpg)

Proceso de soldadura en masa:

![](https://media.wiki-power.com/img/20200311182441.jpg)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
