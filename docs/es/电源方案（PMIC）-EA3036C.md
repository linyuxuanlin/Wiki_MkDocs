# Esquema de alimentación (PMIC) - EA3036C

EA3036C es un PMIC de 3 canales adecuado para aplicaciones alimentadas por baterías de litio o DC de 5V. Incorpora tres convertidores reductores sincrónicos que proporcionan una salida de alta eficiencia en condiciones de carga ligera y pesada. La arquitectura de compensación interna simplifica el diseño del circuito de aplicación. Además, el control de habilitación independiente facilita el control del orden de encendido. EA3036C utiliza un paquete QFN de 20 pines de 3x3.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/PMIC/EA3036C**](https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/PMIC/EA3036C)

## Características principales

- Voltaje de entrada y voltaje de circuito de control: 2.7-5.5V
- Voltaje de salida (3 convertidores reductores): 0.6V-Vin
- Corriente de carga continua de un solo canal: 1A (la salida total de 3 canales debe ser inferior a 6W)
- Frecuencia de conmutación fija de 1.5MHz
- Salida de ciclo de trabajo del 100%
- Corriente de espera: <1uA
- Control de habilitación independiente para cada canal
- Compensación interna
- Limitación de corriente por ciclo
- Protección contra cortocircuitos
- Protección contra sobrecalentamiento (OTP) con recuperación automática
- Protección contra sobretensión de entrada (OVP)
- Paquete QFN de 20 pines de 3 mm x 3 mm

## Circuito de aplicación típico

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220417095917.png)

## Diagrama de funciones internas

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220417001936.png)

## Definición de pines

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220416234110.png)

| Nombre del pin | Descripción del pin                                         |
| -------------- | ----------------------------------------------------------- |
| VCC            | Pin de entrada de alimentación del circuito de control interno |
| VINx           | Pin de entrada de alimentación del canal x, con un condensador MLCC de 10uF para desacoplar |
| LXx            | Salida de conmutación del MOS interno del canal x, que se puede conectar a un circuito de filtro de paso bajo para obtener una tensión más estable |
| FBx            | Pin de retroalimentación del canal x, conectado a la salida de tensión a través de un circuito divisor de tensión |
| ENx            | Pin de habilitación, no puede dejarse en flotación |
| GNDx           | Tierra del canal x                                           |
| AGND           | Tierra analógica                                             |
| Pad inferior   | Para disipación de calor, debe conectarse a tierra            |

## Descripción de características

### Modo PFM/PWM

Cada canal Buck puede funcionar en modo PFM/PWM. Si la corriente de salida es inferior a 260 mA (valor típico), el regulador entrará automáticamente en modo PFM. La tensión de salida y la ondulación de salida en modo PFM son mayores que en modo PWM. Sin embargo, en condiciones de carga ligera, PFM es más eficiente que PWM.

### Interruptor de habilitación

EA3036C es un IC de gestión de energía diseñado específicamente para aplicaciones IPC, que incluye tres canales Buck sincrónicos de 1A que se pueden controlar mediante un solo pin de habilitación.

Si es necesario establecer el tiempo de encendido de cada canal Buck, se puede programar mediante el siguiente circuito:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220417100845.png)

### Arquitectura de desplazamiento de fase de 180°

Para reducir la corriente de ondulación de entrada, el EA3036C utiliza una arquitectura de desplazamiento de fase de 180°. Buck1 y Buck3 tienen la misma fase, mientras que la fase de Buck2 está desplazada 180°. De esta manera, se puede reducir la corriente de ondulación y, por lo tanto, reducir la EMI.

### Protección contra sobrecorriente

Los tres reguladores internos del EA3036C tienen su propio circuito de limitación de corriente por ciclo. Cuando la corriente de pico del inductor supera el umbral de límite de corriente, el voltaje de salida comienza a disminuir hasta que el voltaje en el pin FB cae por debajo del umbral, generalmente un 30% más bajo que el valor de referencia. Una vez que se activa el umbral, la frecuencia de conmutación se reduce a 400 kHz (valor típico).

### Corriente de carga pico

La capacidad de corriente de carga pico del EA3036C depende de la limitación de corriente PMOS interna, la relación de trabajo (Vout/Vin) y el valor del inductor. En las condiciones de Vin=5V y L=1.5uH, la capacidad de corriente de carga pico de salida es la siguiente:

| Voltaje de salida | Corriente de carga pico |
| ---------------- | ---------------------- |
| 3.3V             | 1.2A                   |
| 1.8V             | 1.5A                   |
| 1.5V             | 1.5A                   |
| 1.2V             | 1.5A                   |

Es importante tener en cuenta que la potencia de salida total debe ser menor a 6W para evitar daños por sobrecalentamiento del chip.

### Protección de apagado térmico

Si la temperatura del chip supera el punto de umbral de apagado térmico, el EA3036C se apagará automáticamente. Para evitar una operación inestable, el retardo de apagado térmico es de aproximadamente 30°C.

### Regulación de voltaje de salida

El voltaje de salida de cada regulador se puede ajustar mediante un divisor de resistencia (R1, R2). El voltaje de salida se calcula mediante la siguiente fórmula:

$$
V_{OUTx}=0.6*\frac{R_1}{R_2}+0.6V
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220417230210.png)

Si se requieren valores de voltaje comunes de salida, se pueden utilizar las siguientes configuraciones de resistencia de divisor (todas deben ser de precisión del 1%):

| Voltaje de salida | R1    | R2    |
| ---------------- | ----- | ----- |
| 3.3V             | 68kΩ  | 15kΩ  |
| 1.8V             | 200kΩ | 100kΩ |
| 1.5V             | 150kΩ | 100kΩ |
| 1.2V             | 100kΩ | 100kΩ |

### Selección de capacitores de entrada/salida

El capacitor de entrada se utiliza para suprimir la amplitud del ruido del voltaje de entrada y proporcionar una entrada de CC estable y limpia al dispositivo, mientras que el capacitor de salida puede suprimir la ondulación del voltaje de salida. Se pueden utilizar capacitores MLCC (baja ESR) tanto para la entrada como para la salida.

Los modelos recomendados de capacitores de entrada/salida son los siguientes:

| NPM            | Valor | Voltaje nominal | Encapsulado |
| -------------- | ----- | -------------- | ----------- |
| C2012X5R1A106M | 10uF  | 10V            | 0805        |
| C3216X5R1A106M | 10uF  | 10V            | 1206        |
| C2012X5R1A226M | 22uF  | 10V            | 0805        |
| C3216X5R1A226M | 22uF  | 10V            | 1206        |

### Selección de inductores de salida

La selección del inductor de salida depende principalmente de la cantidad de corriente de ondulación $\Delta I_L$ que pasa a través del inductor. Cuanto mayor sea $\Delta I_L$, mayor será la ondulación del voltaje de salida y las pérdidas. Aunque los inductores pequeños pueden ahorrar costos y espacio, los valores de inductancia más grandes pueden obtener $\Delta I_L$ más pequeños, lo que resulta en una ondulación de voltaje de salida y pérdidas más pequeñas. La fórmula para calcular el valor del inductor es la siguiente:

$$
L=\frac{V_{PWR}-V_{OUT}}{\Delta I_L*F_{SW}}*\frac{V_{OUT}}{V_{PWR}}
$$

Para la mayoría de las aplicaciones, se pueden utilizar inductores de 1.0~2.2uH con el EA3036C.

### Consumo de energía

El consumo total de energía del EA3036C no debe superar los 6W, y la fórmula de cálculo es la siguiente:

$$
P_{D(total)}=\Sigma (V_{OUTx}*I_{OUTx})
$$

## Referencia de diseño de PCB

El diseño de Layout de PMIC requiere atención. Se pueden seguir las siguientes recomendaciones para obtener el mejor rendimiento:

- Se recomienda utilizar un diseño de PCB de 4 capas, colocando el plano LX y el plano de salida en la capa superior, y el plano VIN en la capa interna.
- Los pines de tierra de los capacitores de montaje superficial de entrada/salida en la capa superior deben estar conectados a través de agujeros a la capa interna y la capa inferior.
- AGND debe estar conectado directamente a la capa interna a través de agujeros.
- Ampliar las vías de corriente alta tanto como sea posible.
- Colocar los capacitores de entrada lo más cerca posible de los pines VINx para reducir la interferencia de ruido.
- Mantener la ruta de retroalimentación (de VOUTx a FBx) alejada de los nodos de ruido (como LXx). LXx es un nodo de ruido de alta corriente. Utilizar rutas cortas y anchas para el diseño.
- Los pads de soldadura en la parte inferior del chip deben tener varios agujeros conectados a la capa interna y la capa inferior para la disipación de calor.

## Referencias y agradecimientos

- [EA3036C](http://www.everanalog.com/Product/ProductEA3036CDetailInfo.aspx)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.