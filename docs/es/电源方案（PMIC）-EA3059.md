# Solución de Energía (PMIC) - EA3059

El EA3059 es un PMIC de 4 canales diseñado para aplicaciones alimentadas por baterías de litio o una fuente de alimentación de 5V de corriente continua. Este dispositivo integra internamente cuatro convertidores DC-DC sincrónicos que proporcionan una eficiencia de salida óptima tanto en condiciones de carga ligera como de carga pesada. Su arquitectura de compensación interna simplifica el diseño del circuito de aplicación. Además, el control independiente de habilitación facilita la gestión del encendido secuencial. El EA3059 se presenta en un encapsulado QFN de 24 pines de 4x4 mm.

Repositorio del proyecto: [**Colección de Diseño de Módulos de Alimentación/PMIC/EA3059**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3059)

Vista previa en línea del proyecto:

<div class="visor-de-iframes-de-altium">
  <div
    class="visor-de-ecad-de-altium"
    data-fuente-del-proyecto="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/PMIC/EA3059/EA3059_V0.2.zip"
  ></div>
</div>

## Características Principales

- Rango de voltaje de entrada y voltaje de control del circuito: 2.7-5.5V
- Voltaje de salida (4 convertidores Buck): 0.6V-Vin
- Corriente de salida: 2A continuos por canal, pico de 4A (la salida total de los 4 canales debe ser menor a 10W)
- Frecuencia de conmutación fija de 1.5MHz
- Salida al 100% de ciclo de trabajo
- Eficiencia de hasta el 95% en cada canal
- Corriente en espera: <1uA
- Control de habilitación independiente por canal
- Compensación interna
- Limitación de corriente por ciclo
- Protección contra cortocircuitos
- Protección de sobrecalentamiento autorecuperable (OTP)
- Sin protección de sobretensión de entrada (OVP) (en comparación con el EA3059)
- Encapsulado QFN de 24 pines de 4x4 mm

## Circuitos de Aplicación Típicos

![](https://media.wiki-power.com/img/20220420171841.png)

## Diagrama de Funciones Internas

![](https://media.wiki-power.com/img/20220420171859.png)

## Definición de Pines

![](https://media.wiki-power.com/img/20220420171920.png)

| Nombre del Pin | Descripción del Pin                                                                                                                            |
| -------------- | ---------------------------------------------------------------------------------------------------------------------------------------------- |
| VCC            | Alimentación interna del circuito de control                                                                                                   |
| VINx           | Alimentación del canal x, con desacople de 10uF MLCC                                                                                           |
| LXx            | Salida de conmutación del MOSFET interno del canal x, se puede conectar a un circuito de filtro paso bajo para obtener una tensión más estable |
| FBx            | Pin de retroalimentación del canal x, conectado a la salida mediante un divisor de voltaje                                                     |
| ENx            | Pin de habilitación, no debe dejarse flotante                                                                                                  |
| GNDx           | Conexión a tierra del canal x                                                                                                                  |
| AGND           | Tierra analógica                                                                                                                               |
| Pad Inferior   | Para disipación de calor, debe estar conectado a tierra                                                                                        |
| NC             | No conectado                                                                                                                                   |

## Descripción de las Características

### Modo PFM/PWM

Cada una de las salidas Buck puede operar en modo PFM/PWM. Cuando la corriente de salida es menor a 150mA (valor típico), el regulador entrará automáticamente en el modo PFM. En el modo PFM, el voltaje de salida y la ondulación de salida son mayores en comparación con el modo PWM. Sin embargo, en condiciones de carga ligera, el modo PFM ofrece una eficiencia superior al modo PWM.

### Habilitación del interruptor

El EA3059 es un circuito integrado de gestión de energía diseñado específicamente para aplicaciones OTT, que incluye cuatro reguladores Buck síncronos de 2A cada uno. Cada uno de ellos puede ser habilitado o deshabilitado de manera independiente a través de pines EN individuales.

Si es necesario establecer el tiempo de encendido de cada regulador Buck, esto se puede lograr mediante la programación de un circuito como se muestra a continuación:

![Circuito de Programación](https://media.wiki-power.com/img/20220420172125.png)

### Arquitectura con Desfase de 180°

Para reducir la ondulación de corriente de entrada, el EA3059 utiliza una arquitectura con desfase de 180°. Los reguladores Buck 1 y Buck 3 tienen fases idénticas, mientras que Buck 2 y Buck 4 tienen una diferencia de fase de 180°. Esto ayuda a reducir la ondulación de corriente y, en consecuencia, disminuye la interferencia electromagnética (EMI).

### Protección contra Corriente Excesiva

Los cuatro reguladores internos del EA3059 están equipados con sus propios circuitos de límite de corriente por ciclo. Cuando la corriente pico del inductor supera el umbral de límite de corriente, el voltaje de salida comienza a disminuir hasta que la tensión en el pin FB cae por debajo del umbral, que generalmente es un 30% menor que el valor de referencia. Una vez que se activa el umbral, la frecuencia de conmutación se reduce a 350 kHz (valor típico).

### Protección Térmica

Si la temperatura del chip supera el umbral de apagado térmico, el EA3059 se apagará automáticamente. Para evitar la inestabilidad en el funcionamiento, la histéresis del apagado térmico es de aproximadamente 30°C.

### Ajuste de Voltaje de Salida

El voltaje de salida de cada regulador se puede ajustar mediante una red de resistencias (R1 y R2). El voltaje de salida se calcula mediante la siguiente fórmula:

$$
V_{OUTx} = 0.6 * \frac{R_1}{R_2} + 0.6V
$$

![Configuración de Resistencias](https://media.wiki-power.com/img/20220420172602.png)

Si es necesario obtener voltajes de salida comunes, puede consultar la siguiente tabla para configurar las resistencias divisoras (asegurándose de utilizar resistencias del 1% de precisión):

| Voltaje de Salida | R1    | R2    |
| ----------------- | ----- | ----- |
| 3.3V              | 510kΩ | 110kΩ |
| 1.8V              | 200kΩ | 100kΩ |
| 1.5V              | 150kΩ | 100kΩ |
| 1.1V              | 68kΩ  | 82kΩ  |

### Selección de Capacitores de Entrada/Salida

Los capacitores de entrada ayudan a suprimir la amplitud del ruido en el voltaje de entrada, proporcionando una entrada continua y limpia. Los capacitores de salida ayudan a reducir la ondulación en el voltaje de salida. Tanto los capacitores de entrada como los de salida pueden ser de tipo MLCC (condensadores multicapa cerámicos con baja resistencia en serie, ESR).

Los modelos recomendados para los capacitores de entrada/salida son los siguientes:

| Modelo         | Valor | Tensión | Encapsulado |
| -------------- | ----- | ------- | ----------- |
| C2012X5R1A106M | 10uF  | 10V     | 0805        |
| C3216X5R1A106M | 10uF  | 10V     | 1206        |
| C2012X5R1A226M | 22uF  | 10V     | 0805        |
| C3216X5R1A226M | 22uF  | 10V     | 1206        |

### Selección de Inductores de Salida

La elección del inductor de salida depende principalmente de la cantidad de corriente de ondulación $\Delta I_L$ que pasa a través del inductor. Cuanto mayor sea $\Delta I_L$, mayor será la ondulación y la pérdida de voltaje de salida. Aunque los inductores más pequeños pueden ahorrar costos y espacio, los valores de inductancia más grandes pueden reducir $\Delta I_L$, lo que resulta en una menor ondulación y pérdida de voltaje de salida. La fórmula para calcular el valor del inductor es la siguiente:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

Para la mayoría de las aplicaciones, el EA3059 puede utilizar inductores de 1.0 a 2.2uH.

### Consumo de Energía

La potencia total del EA3059 no debe exceder los 10W y se puede calcular mediante la siguiente fórmula:

$$
P_{D(total)} = \sum (V_{OUTx}*I_{OUTx})
$$

## Consideraciones de Diseño

El diseño del PMIC debe realizarse con cuidado para garantizar un rendimiento óptimo. Puedes seguir las siguientes recomendaciones:

```markdown
- ...
- ...
```

[//]: # "Please note that this translation is provided in markdown format as per your request."

- Se recomienda utilizar una disposición de PCB de 4 capas, colocando el plano LX y el plano de salida en la capa superior, y el plano de VIN en una capa interna.
- Los pines de tierra de los condensadores de montaje superficial de entrada/salida en la capa superior deben estar conectados a través de agujeros pasantes a las capas internas y la capa inferior.
- AGND debe estar directamente conectado a la capa interna a través de agujeros pasantes.
- Se debe ensanchar al máximo las rutas de los caminos de alta corriente.
- Coloque los condensadores de entrada lo más cerca posible de los pines VINx para reducir la interferencia de ruido.
- Mantenga la ruta de retroalimentación (desde VOUTx hasta FBx) alejada de los nodos de ruido (como LXx). LXx es un nodo de alto ruido de corriente. Utilice rutas cortas y anchas en la disposición.
- Los pads de soldadura en la parte inferior del chip deben tener múltiples agujeros que se conecten a las capas internas y la capa inferior para disipación de calor.
- Coloque los condensadores de entrada lo más cerca posible de los pines VINx para reducir la interferencia de ruido.

El diseño de la disposición se muestra a continuación:

Capa Superior:

![Capa Superior](https://media.wiki-power.com/img/20220420175756.png)

Capa de Alimentación Intermedia:

![Capa de Alimentación Intermedia](https://media.wiki-power.com/img/20220420175833.png)

Capa de Tierra Intermedia:

![Capa de Tierra Intermedia](https://media.wiki-power.com/img/20220420175851.png)

Capa Inferior:

![Capa Inferior](https://media.wiki-power.com/img/20220420175906.png)

## Referencias y Agradecimientos

- [EA3059](http://www.everanalog.com/ProductCN/ProductEA3059DetailInfoCN.aspx)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
