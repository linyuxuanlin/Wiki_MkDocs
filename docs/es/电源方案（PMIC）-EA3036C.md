# Solución de Alimentación (PMIC) - EA3036C

El EA3036C es un PMIC de 3 canales diseñado para aplicaciones alimentadas por baterías de litio o fuente de alimentación de 5V de corriente continua. Este dispositivo integra internamente tres convertidores reductores sincrónicos que ofrecen eficiencia en operaciones de carga ligera y pesada. Su arquitectura de compensación interna simplifica el diseño del circuito de la aplicación. Además, el control de habilitación independiente facilita la secuencia de encendido. El EA3036C se presenta en un encapsulado QFN de 20 pines de 3x3 mm.

Repositorio del proyecto: [**Colección_de_Diseño_de_Módulos_de_Potencia/PMIC/EA3036C**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3036C)

## Características Principales

- Voltaje de entrada y voltaje del circuito de control: 2.7-5.5V
- Voltaje de salida (3 convertidores Buck): 0.6V-Vin
- Corriente de carga continua por canal: 1A (la suma de las tres salidas no debe superar los 6W)
- Frecuencia de conmutación fija de 1.5MHz
- Salida con ciclo de trabajo del 100%
- Corriente en espera: <1uA
- Control de habilitación independiente para cada canal
- Compensación interna
- Limitación de corriente por ciclo
- Protección contra cortocircuitos
- Protección contra sobrecalentamiento con recuperación automática (OTP)
- Protección contra sobretensión de entrada (OVP)
- Encapsulado QFN de 20 pines de 3mm x 3mm

## Circuitos de Aplicación Típicos

![](https://media.wiki-power.com/img/20220417095917.png)

## Diagrama de Funciones Internas

![](https://media.wiki-power.com/img/20220417001936.png)

## Definición de Pines

![](https://media.wiki-power.com/img/20220416234110.png)

| Nombre del Pin  | Descripción del Pin                                                                                                                |
| --------------- | ---------------------------------------------------------------------------------------------------------------------------------- |
| VCC             | Entrada de alimentación interna para circuito de control                                                                           |
| VINx            | Entrada de alimentación del canal x, conecte un condensador cerámico de 10uF para desacoplar                                       |
| LXx             | Salida de conmutación del MOSFET interno del canal x, se puede conectar a un filtro pasa bajo para obtener una tensión más estable |
| FBx             | Pin de retroalimentación del canal x, conectado al voltaje de salida a través de un divisor de tensión                             |
| ENx             | Pin de habilitación, no debe dejarse en flotación                                                                                  |
| GNDx            | Tierra del canal x                                                                                                                 |
| AGND            | Tierra analógica                                                                                                                   |
| Pads Inferiores | Para disipación de calor, deben estar conectados a tierra                                                                          |

## Descripción de Características

### Modo PFM/PWM

Cada convertidor Buck puede operar en modo PFM/PWM. Si la corriente de salida es menor de 260mA (valor típico), el regulador entrará automáticamente en modo PFM. En modo PFM, el voltaje de salida y el rizado de salida son mayores que en modo PWM. Sin embargo, en situaciones de carga ligera, el modo PFM ofrece una mayor eficiencia que el modo PWM.

### Interruptor de Habilitación

El EA3036C es un IC de administración de energía diseñado específicamente para aplicaciones IPC, que incluye tres convertidores Buck sincrónicos de 1A cada uno, con control de habilitación individual a través de pines EN.

Si se necesita ajustar el tiempo de encendido de cada convertidor Buck, se puede utilizar el siguiente circuito de programación:

![](https://media.wiki-power.com/img/20220417100845.png)

### Arquitectura de Desplazamiento de Fase de 180°

Con el fin de reducir la corriente de ondulación de entrada, el EA3036C utiliza una arquitectura de desplazamiento de fase de 180°. Buck1 y Buck3 tienen fases idénticas, mientras que la fase de Buck2 difiere en 180°. Esto permite reducir la corriente de ondulación y, por ende, disminuir las interferencias electromagnéticas (EMI).

### Protección contra Sobrecorriente

Los tres reguladores internos del EA3036C cuentan con sus propios circuitos de límite de corriente por ciclo. Cuando la corriente pico en el inductor supera el umbral de límite de corriente, el voltaje de salida comienza a disminuir, hasta que el voltaje en el pin FB esté por debajo del umbral, generalmente un 30% más bajo que el valor de referencia. Una vez que se activa este umbral, la frecuencia de conmutación disminuye a 400KHz (valor típico).

### Corriente Pico de Carga

La capacidad de corriente pico de carga del EA3036C depende de la limitación de corriente interna del PMOS, la relación de trabajo (Vout/Vin) y el valor del inductor. En condiciones de Vin=5V y L=1.5uH, la capacidad de corriente pico de carga de salida es la siguiente:

| Voltaje de Salida | Corriente Pico de Carga |
| ----------------- | ----------------------- |
| 3.3V              | 1.2A                    |
| 1.8V              | 1.5A                    |
| 1.5V              | 1.5A                    |
| 1.2V              | 1.5A                    |

Es importante tener en cuenta que la potencia total de salida debe ser menor a 6W para evitar el sobrecalentamiento del chip.

### Desconexión Térmica

Si la temperatura del chip supera el umbral de desconexión térmica, el EA3036C se apagará automáticamente. Para evitar la inestabilidad en el funcionamiento, la histéresis de desconexión térmica es de aproximadamente 30°C.

### Ajuste del Voltaje de Salida

El voltaje de salida de cada regulador se puede ajustar mediante una red de resistencias divisoras (R1, R2). El voltaje de salida se calcula utilizando la siguiente fórmula:

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

![Imagen](https://media.wiki-power.com/img/20220417230210.png)

Si se requiere obtener valores de voltaje de uso común, se pueden utilizar las siguientes resistencias divisoras (siempre con una precisión del 1%):

| Voltaje de Salida | R1    | R2    |
| ----------------- | ----- | ----- |
| 3.3V              | 68kΩ  | 15kΩ  |
| 1.8V              | 200kΩ | 100kΩ |
| 1.5V              | 150kΩ | 100kΩ |
| 1.2V              | 100kΩ | 100kΩ |

### Selección de Capacitores de Entrada / Salida

Los capacitores de entrada se utilizan para reducir la amplitud del ruido en el voltaje de entrada y proporcionar una entrada de corriente continua estable y limpia. Los capacitores de salida ayudan a reducir la ondulación del voltaje de salida. Tanto los capacitores de entrada como los de salida pueden ser capacitores cerámicos multicapa (MLCC) con una baja resistencia en serie equivalente (ESR).

Los modelos recomendados de capacitores de entrada / salida son los siguientes:

| NPM            | Valor | Tensión | Encapsulado |
| -------------- | ----- | ------- | ----------- |
| C2012X5R1A106M | 10uF  | 10V     | 0805        |
| C3216X5R1A106M | 10uF  | 10V     | 1206        |
| C2012X5R1A226M | 22uF  | 10V     | 0805        |
| C3216X5R1A226M | 22uF  | 10V     | 1206        |

### Selección de Inductores de Salida

La elección del inductor de salida depende principalmente de la cantidad de corriente de ondulación a través del inductor, ΔIL. Cuanto mayor sea ΔIL, mayor será la ondulación del voltaje de salida y las pérdidas. La fórmula para calcular el valor del inductor es la siguiente:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

Para la mayoría de las aplicaciones, se puede utilizar un inductor de 1.0 a 2.2uH con el EA3036C.

### Consumo de Energía

El consumo de energía total del EA3036C no debe exceder los 6W y se calcula de la siguiente manera:

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Consideraciones de Diseño

El diseño del PMIC requiere atención meticulosa para lograr un rendimiento óptimo. Se pueden seguir las siguientes recomendaciones:

- Se recomienda utilizar un diseño de PCB de 4 capas, colocando las planos de LX y salidas en la capa superior, y el plano de VIN en una capa interna.
- Los pines de tierra de los condensadores de montaje superficial de entrada/salida en la capa superior deben estar conectados a las capas internas y la capa inferior a través de agujeros pasantes.
- La conexión a tierra AGND debe estar directamente vinculada a la capa de tierra interna a través de agujeros pasantes.
- Es importante ensanchar las rutas de alta corriente tanto como sea posible.
- Coloque los condensadores de entrada lo más cerca posible de los pines VINx para minimizar la interferencia de ruido.
- Aleje la ruta de retroalimentación (desde VOUTx hasta FBx) de los nodos de ruido (como LXx). LXx es un nodo de alto ruido de corriente. Utilice trazas cortas y anchas para el diseño.
- Debe perforarse múltiples agujeros desde los pads de soldadura en la parte inferior del chip hacia las capas internas y la capa inferior para mejorar la disipación de calor.

## Referencias y Agradecimientos

- [EA3036C](http://www.everanalog.com/Product/ProductEA3036CDetailInfo.aspx)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
