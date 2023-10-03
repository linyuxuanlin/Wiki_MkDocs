# Protocolo de comunicación - CAN 🚧

CAN (Controller Area Network) es un bus de comunicación serie de múltiples maestros. El diseño básico requiere una alta velocidad de bits, alta resistencia a interferencias electromagnéticas y la capacidad de detectar cualquier error que se produzca. Cuando la distancia de transmisión de la señal alcanza los 10 km, el bus CAN aún puede proporcionar una velocidad de transmisión de datos de hasta 5 Kbps.

## Diseño del circuito CAN

El diseño del módulo CAN se basa en el chip CAN, que convierte la señal serie (RX/TX) en la señal diferencial CAN (CANH/CANL). A continuación se presentan dos transceptores CAN comúnmente utilizados.

### Basado en TJA1050

Para obtener información completa, consulte [**Modularity_of_Functional_Circuit/ Modulación de diseño - Comunicación CAN / Basado en TJA1050**](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1-CAN%E9%80%9A%E4%BF%A1/%E5%9F%BA%E4%BA%8ETJA1050)

#### Características

- Alimentación: **5 V** (4.75-5.25 V)
- Velocidad alta: 60 Kbps-1 Mbps
- Cumple completamente con la norma ISO 11898
- Baja radiación electromagnética (EME)
- Receptor diferencial con rango de entrada de préstamo, resistente a interferencias electromagnéticas (EMI)
- Se pueden conectar al menos 110 nodos
- Los nodos sin alimentación no interferirán con el bus

#### Modo de trabajo

TJA1050 tiene dos modos de trabajo (alta velocidad / silencioso), controlados por el pin S (RS).

**Modo de alta velocidad**:

El modo de alta velocidad es el modo de trabajo normal, y se puede ingresar a este modo conectando el pin S a tierra. Debido a que el pin S tiene una resistencia de pull-down incorporada, incluso si no está conectado externamente, el modo de alta velocidad es el modo predeterminado.

En este modo, la señal de salida del bus tiene una pendiente fija y cambia a la velocidad más rápida, lo que es adecuado para la velocidad de bits máxima o la longitud máxima del bus, y su retardo de transmisión es mínimo.

**Modo silencioso**:

En el modo silencioso, el transmisor está deshabilitado y no importa la señal de entrada de TXD, por lo que el consumo de energía en el estado de no transmisión es el mismo que en el estado de silencio. Se puede ingresar al modo silencioso conectando el pin S a un nivel alto.

En el modo silencioso, los nodos se pueden configurar en un estado absolutamente pasivo con respecto al bus, y el microcontrolador ya no accede directamente al controlador CAN. TJA1050 liberará el bus.

#### Pines del chip

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607102222.png)

#### Circuito de referencia

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607115611.png)

Como se muestra en la figura, el controlador de protocolo CAN (por ejemplo, un microcontrolador) se conecta al transceptor a través de la línea serie (RX/TX), que se convierte en una señal CAN (CANH/CANL) en el transceptor y se selecciona el modo de alta velocidad / silencioso mediante el pin S.

### Basado en SN65HVD230

Para obtener información completa, consulte [**Modularity_of_Functional_Circuit/ Modulación de diseño - Comunicación CAN / Basado en SN65HVD230**](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1-CAN%E9%80%9A%E4%BF%A1/%E5%9F%BA%E4%BA%8ESN65HVD230)

#### Características

- Alimentado por una sola fuente de **3.3 V**
- Se pueden conectar al menos 120 nodos
- Modo de espera de baja corriente
- Velocidad: hasta 1 Mbps

#### Modo de trabajo

SN65HVD230 tiene tres modos de trabajo (alta velocidad / pendiente / silencioso), controlados por el pin S (RS). Generalmente usamos el modo de alta velocidad.

**Modo de alta velocidad**:

Conecte Rs a tierra para habilitar el modo de alta velocidad.

**Modo de pendiente**:

Use una resistencia entre 10k y 100k para bajar Rs a tierra. Consulte el manual de datos para obtener la relación específica entre la resistencia y la velocidad.



**Modo de baja potencia**:

Elevar Rs a 3.3V

#### Pines del chip

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607155539.png)

#### Circuito de referencia

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607171051.png)

PESD2CAN es un diodo de protección ESD especializado para CAN, que protege al chip de daños por descargas electrostáticas y otros transitorios.

El diseño de PCB de referencia es el siguiente:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210607171427.png)

### Diferencias entre TJA1050 y SN65HVD230

La principal diferencia entre TJA1050 y SN65HVD230 es el voltaje de trabajo, TJA1050 trabaja en un entorno de 5V, mientras que SN65HVD230 trabaja en un entorno de 3.3V.

Consideraciones comunes:

- Las líneas de señal CAN deben ser diferencialmente enrutadas en el diseño de PCB.
- Las resistencias terminales generalmente solo se necesitan en el extremo inicial y final de la línea CAN, no en el medio.
- Si se requiere filtrado y estabilización del voltaje común del bus, también se pueden utilizar resistencias terminales separadas (como se muestra arriba, divididas en dos resistencias de 60 Ω con un capacitor conectado a tierra en el medio).

## Diseño EMC de la interfaz CAN

En la comunicación CAN, el cable es propenso a acoplar interferencias externas, lo que afecta la transmisión de señales e incluso puede afectar los circuitos internos sensibles del núcleo a través del circuito de interfaz.

Los dispositivos de protección de la interfaz CAN incluyen principalmente: capacitores de filtrado, inductores comunes, capacitores de derivación y tubos TVS.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211220134905.png)

- Capacitores de filtrado $C_1, C_2$: se utilizan para proporcionar una ruta de retorno de baja impedancia para las interferencias, el rango de selección es de 22pF a 1000pF, y el valor típico es de 100pF.
- Inductor común $L_1$: se utiliza para filtrar las interferencias comunes en la línea diferencial, el rango de impedancia seleccionado es de 120Ω/100MHz a 2200Ω/100MHz, y el valor típico es de 600Ω/100MHz.
- Capacitores de derivación $C_3, C_4$: se utilizan para el aislamiento entre la tierra de la interfaz y la tierra digital, el valor típico es de 1000pF/2kV.
- Tubos TVS $D_1, D_2$: se utilizan para proteger contra ESD o impactos de alta energía momentánea, limitando el voltaje del circuito a un valor predeterminado para garantizar que los dispositivos de circuito posteriores no se dañen por impactos de alta energía momentánea.

## Referencias y agradecimientos

- [Diseño de protección de circuito de interfaz](https://blog.csdn.net/weixin_40877615/article/details/94381422)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.