# Esquema de alimentación (PMIC) - EA3059

EA3059 es un PMIC de 4 canales adecuado para aplicaciones alimentadas por baterías de litio o DC de 5V. Incorpora cuatro convertidores reductores síncronos que proporcionan una salida de alta eficiencia en cargas ligeras y pesadas. La arquitectura de compensación interna hace que el diseño del circuito de aplicación sea simple. Además, el control de habilitación independiente facilita el control del orden de encendido. EA3059 utiliza un paquete QFN de 24 pines de 4x4.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/PMIC/EA3059**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3059)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/PMIC/EA3059/EA3059_V0.2.zip"
  ></div>
</div>

## Características principales

- Voltaje de entrada y voltaje de circuito de control: 2.7-5.5V
- Voltaje de salida (4 convertidores Buck): 0.6V-Vin
- Corriente de salida: carga continua de una sola vía de 2A, pico de 4A (la salida total de los 4 canales debe ser inferior a 10W)
- Frecuencia de conmutación fija de 1.5MHz
- Salida de ciclo de trabajo del 100%
- Eficiencia de cada canal del 95%
- Corriente de espera: <1uA
- Control de habilitación independiente para cada canal
- Compensación interna
- Limitación de corriente por ciclo
- Protección contra cortocircuitos
- Protección contra sobrecalentamiento (OTP) con recuperación automática
- Sin protección contra sobretensión de entrada (OVP) (en comparación con EA3059)
- Paquete QFN de 24 pines de 4mm x 4mm

## Circuito de aplicación típico

![](https://img.wiki-power.com/d/wiki-media/img/20220420171841.png)

## Diagrama de funciones internas

![](https://img.wiki-power.com/d/wiki-media/img/20220420171859.png)

## Definición de pines

![](https://img.wiki-power.com/d/wiki-media/img/20220420171920.png)

| Nombre del pin | Descripción del pin                                                                                                                             |
| -------------- | ----------------------------------------------------------------------------------------------------------------------------------------------- |
| VCC            | Pin de entrada de alimentación del circuito de control interno                                                                                  |
| VINx           | Pin de entrada de alimentación del canal x, con un condensador MLCC de 10uF para la eliminación de ruido                                        |
| LXx            | Salida de conmutación del MOS interno del canal x, que se puede conectar a un circuito de filtro paso bajo para obtener una tensión más estable |
| FBx            | Pin de retroalimentación del canal x, conectado a la salida de tensión a través de un circuito divisor de tensión                               |
| ENx            | Pin de habilitación, no debe dejarse en flotación                                                                                               |
| GNDx           | Tierra del canal x                                                                                                                              |
| AGND           | Tierra analógica                                                                                                                                |
| Pad inferior   | Para disipación de calor, debe estar conectado a tierra                                                                                         |
| NC             | Sin conexión                                                                                                                                    |

## Descripción de características

### Modo PFM/PWM

Cada canal Buck puede funcionar en modo PFM/PWM. Si la corriente de salida es menor que 150 mA (valor típico), el regulador entrará automáticamente en modo PFM. La tensión de salida y la ondulación de salida en modo PFM son mayores que en modo PWM. Sin embargo, en cargas ligeras, PFM es más eficiente que PWM.

### Interruptor de habilitación

EA3059 es un IC de gestión de energía diseñado específicamente para aplicaciones OTT, que incluye cuatro canales Buck síncronos de 2A, que se pueden controlar mediante un interruptor de habilitación individual en el pin EN.

Si se necesita establecer el tiempo de encendido de cada canal Buck, se puede programar mediante el siguiente circuito:

![](https://img.wiki-power.com/d/wiki-media/img/20220420172125.png)

### Arquitectura de desplazamiento de fase de 180°

Para reducir la corriente de ondulación de entrada, EA3059 utiliza una arquitectura de desplazamiento de fase de 180°. La fase de Buck1 y Buck3 es la misma, y la fase de Buck2 y Buck4 difiere en 180°. Esto puede reducir la corriente de ondulación y, por lo tanto, reducir la EMI.

### Protección contra sobrecorriente

Cada regulador interno de EA3059 tiene su propio circuito de limitación de corriente por ciclo. Cuando la corriente de pico del inductor supera el umbral de limitación de corriente, la tensión de salida comienza a disminuir hasta que la tensión en el pin FB es inferior al umbral, que suele ser un 30% inferior al valor de referencia. Una vez que se activa el umbral, la frecuencia de conmutación se reduce a 350 kHz (valor típico).

### Apagado térmico

Si la temperatura del chip es superior al umbral de apagado térmico, EA3059 se apagará automáticamente. Para evitar la inestabilidad del trabajo, la histéresis del apagado térmico es de aproximadamente 30°C.

### Ajuste de tensión de salida

La tensión de salida de cada regulador se puede ajustar mediante un divisor de resistencia (R1, R2). La tensión de salida se calcula mediante la siguiente fórmula:

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

![](https://img.wiki-power.com/d/wiki-media/img/20220420172602.png)

Si se necesitan valores de voltaje de salida comunes, se puede consultar la siguiente tabla para configurar la resistencia de división (se debe utilizar una precisión del 1%):

| Tensión de salida | R1    | R2    |
| ----------------- | ----- | ----- |
| 3.3V              | 510kΩ | 110kΩ |
| 1.8V              | 200kΩ | 100kΩ |
| 1.5V              | 150kΩ | 100kΩ |
| 1.1V              | 68kΩ  | 82kΩ  |

### Selección de capacitores de entrada/salida

El capacitor de entrada se utiliza para suprimir la amplitud del ruido de la tensión de entrada y proporcionar una entrada de CC estable y limpia al dispositivo, mientras que el capacitor de salida puede suprimir la ondulación de la tensión de salida. Se pueden utilizar capacitores MLCC tanto para la entrada como para la salida (baja ESR).

Los modelos de capacitores recomendados para entrada/salida son los siguientes:

| NPM            | Valor | Voltaje | Paquete |
| -------------- | ----- | ------- | ------- |
| C2012X5R1A106M | 10uF  | 10V     | 0805    |
| C3216X5R1A106M | 10uF  | 10V     | 1206    |
| C2012X5R1A226M | 22uF  | 10V     | 0805    |
| C3216X5R1A226M | 22uF  | 10V     | 1206    |

### Selección de inductores de salida

La selección del inductor de salida depende principalmente de la cantidad de corriente de ondulación $\Delta I_L$ que pasa a través del inductor. Cuanto mayor sea $\Delta I_L$, mayor será la ondulación de la tensión de salida y las pérdidas. Aunque los inductores pequeños pueden ahorrar costos y espacio, los valores de inductancia más grandes pueden obtener una $\Delta I_L$ más pequeña, lo que resulta en una ondulación de tensión de salida y pérdidas más pequeñas. La fórmula de cálculo del valor del inductor es la siguiente:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

Para la mayoría de las aplicaciones, se pueden utilizar inductores de 1.0 a 2.2 uH.

### Consumo de energía

El consumo total de energía de EA3059 no debe superar los 10 W, y la fórmula de cálculo es la siguiente:

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Referencia de diseño de Layout

El diseño de Layout de PMIC debe ser cuidadoso. Se pueden seguir las siguientes recomendaciones para obtener el mejor rendimiento:

- Se recomienda utilizar una disposición de PCB de 4 capas, colocando el plano LX y el plano de salida en la capa superior, y el plano VIN en la capa interna.
- Los pines de tierra de los capacitores de montaje superficial de entrada/salida en la capa superior deben estar conectados a través de orificios pasantes a la tierra de la capa interna y la capa inferior.
- AGND debe estar conectado directamente a la capa interna de tierra a través de orificios pasantes.
- Se deben ensanchar las rutas de corriente de alta corriente tanto como sea posible.
- Coloque los capacitores de entrada lo más cerca posible de los pines VINx para reducir la interferencia de ruido.
- Aleje la ruta de retroalimentación (desde VOUTx hasta FBx) de los nodos de ruido (como LXx). LXx es un nodo de ruido de alta corriente. Utilice rutas cortas y anchas para el diseño.
- Los pads de soldadura en la parte inferior del chip deben tener varios orificios que se conecten a la capa interna y la capa inferior de tierra para la disipación de calor.
- Coloque los capacitores de entrada lo más cerca posible de los pines VINx para reducir la interferencia de ruido.

Referencia de diseño:

Capa superior:

![](https://img.wiki-power.com/d/wiki-media/img/20220420175756.png)

Capa de alimentación intermedia:

![](https://img.wiki-power.com/d/wiki-media/img/20220420175833.png)

Capa de tierra intermedia:

![](https://img.wiki-power.com/d/wiki-media/img/20220420175851.png)

Capa inferior:

![](https://img.wiki-power.com/d/wiki-media/img/20220420175906.png)

## Referencias y agradecimientos

- [EA3059](http://www.everanalog.com/ProductCN/ProductEA3059DetailInfoCN.aspx)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
