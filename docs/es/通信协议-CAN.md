# Protocolo de comunicación - CAN 🚧

CAN (Controller Area Network) es un bus de comunicación serial de múltiples maestros. El diseño básico requiere una alta velocidad de bits, alta inmunidad al ruido electromagnético y la capacidad de detectar cualquier error que se produzca. Incluso cuando la distancia de transmisión alcanza los 10 km, el bus CAN puede proporcionar una velocidad de transferencia de datos de hasta 5 Kbps.

## Diseño del circuito CAN

El diseño del módulo CAN se basa en el chip CAN, que convierte las señales seriales (RX/TX) en señales diferenciales CAN (CANH/CANL). A continuación se presentan dos transceptores CAN comúnmente utilizados.

### Basado en TJA1050

Para obtener información completa, consulte [**Modularity_of_Functional_Circuit/ Modulación del circuito funcional/ Comunicación CAN/ Basado en TJA1050**](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1-CAN%E9%80%9A%E4%BF%A1/%E5%9F%BA%E4%BA%8ETJA1050)

#### Características

- Alimentación: **5 V** (4.75-5.25 V)
- Velocidad alta: 60 Kbps-1 Mbps
- Cumple totalmente con la norma ISO 11898
- Baja radiación electromagnética (EME)
- Receptor diferencial con rango de entrada ajustable para inmunidad al ruido electromagnético (EMI)
- Puede conectar al menos 110 nodos
- Los nodos sin alimentación no interfieren con el bus

#### Modo de funcionamiento

El TJA1050 tiene dos modos de funcionamiento (alta velocidad / silencio), controlados por el pin S (RS).

**Modo de alta velocidad**:

El modo de alta velocidad es el modo de funcionamiento normal. Para entrar en este modo, simplemente conecte el pin S a tierra. Debido a que el pin S tiene una resistencia de pull-down interna, incluso si no está conectado externamente, el modo de alta velocidad se establecerá de forma predeterminada.

En este modo, la señal de salida del bus tiene una pendiente fija y cambia a la velocidad más rápida, lo que es adecuado para la máxima velocidad de bits y/o la máxima longitud del bus. Además, el retardo de ciclo del transceptor es mínimo.

**Modo de silencio**:

En el modo de silencio, el transmisor está deshabilitado y no importa la señal de entrada de TXD. Por lo tanto, el consumo de corriente en el modo de silencio es igual al consumo en el estado de reposo. Para entrar en el modo de silencio, simplemente conecte el pin S a un nivel alto.

En el modo de silencio, los nodos pueden configurarse en un estado absolutamente pasivo en el bus. En este caso, el microcontrolador ya no accede directamente al controlador CAN y el TJA1050 liberará el bus.

#### Pines del chip

![](https://media.wiki-power.com/img/20210607102222.png)

#### Circuito de referencia

![](https://media.wiki-power.com/img/20210607115611.png)

Como se muestra en la imagen, el controlador del protocolo CAN (por ejemplo, un microcontrolador) se conecta al transceptor a través de la línea serial (RX/TX), que se convierte en la señal CAN (CANH/CANL) en el transceptor. El modo de alta velocidad/silencio se selecciona mediante el pin S.

### Basado en SN65HVD230

Para obtener información completa, consulte [**Modularity_of_Functional_Circuit/ Modulación del circuito funcional/ Comunicación CAN/ Basado en SN65HVD230**](https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/%E6%A8%A1%E5%9D%97%E8%AE%BE%E8%AE%A1-CAN%E9%80%9A%E4%BF%A1/%E5%9F%BA%E4%BA%8ESN65HVD230)

#### Características

- Alimentado por una sola fuente de **3.3 V**
- Puede conectar al menos 120 nodos
- Modo de espera de baja corriente
- Velocidad: hasta 1 Mbps

#### Modo de funcionamiento

El SN65HVD230 tiene tres modos de funcionamiento (alta velocidad / pendiente / silencio), controlados por el pin S (RS). Normalmente, utilizamos el modo de alta velocidad.

**Modo de alta velocidad**:

Para habilitar el modo de alta velocidad, conecte Rs a tierra.

**Modo de pendiente**:

Para habilitar el modo de pendiente, utilice una resistencia entre 10k y 100k para conectar Rs a tierra. Consulte el manual de datos para obtener información específica sobre la relación entre el valor de resistencia y la velocidad.

**Modo de baja potencia**:

Para habilitar el modo de baja potencia, conecte Rs a 3.3V.

#### Pines del chip

![](https://media.wiki-power.com/img/20210607155539.png)

#### Circuito de referencia

![](https://media.wiki-power.com/img/20210607171051.png)

PESD2CAN es un diodo de protección ESD especializado para CAN, que protege el chip de daños causados por descargas electrostáticas y otros transitorios.

El diseño de PCB de referencia es el siguiente:

![](https://media.wiki-power.com/img/20210607171427.png)

### Diferencias y similitudes entre TJA1050 y SN65HVD230

La principal diferencia entre TJA1050 y SN65HVD230 es el voltaje de operación. TJA1050 opera en un entorno de 5 V, mientras que SN65HVD230 opera en un entorno de 3.3 V.

Consideraciones comunes:

- Al realizar el enrutamiento de las líneas de señal CAN en la PCB, se deben utilizar líneas diferenciales.
- Las resistencias terminales generalmente solo se necesitan en el extremo de inicio y el extremo final de la línea CAN, no se requieren en los puntos intermedios.
- Si es necesario filtrar y estabilizar el voltaje común del bus, también se pueden utilizar resistencias terminales separadas (como se muestra anteriormente, dos resistencias de 60 Ω con un capacitor conectado a tierra en el medio).

## Diseño EMC de la interfaz CAN

En la comunicación CAN, los cables son propensos a acoplar interferencias externas, lo que afecta la transmisión de señales e incluso puede afectar los circuitos internos sensibles del núcleo.

Los dispositivos de protección de la interfaz CAN incluyen principalmente: capacitores de filtrado, inductores de modo común, capacitores de derivación y diodos TVS.

![](https://media.wiki-power.com/img/20211220134905.png)

- Capacitores de filtrado $C_1, C_2$: proporcionan una ruta de retorno de baja impedancia para las interferencias, el rango de selección es de 22pF a 1000pF, con un valor típico de 100pF.
- Inductor de modo común $L_1$: utilizado para filtrar las interferencias de modo común en las líneas diferenciales, la impedancia se selecciona en el rango de 120Ω/100MHz a 2200Ω/100MHz, con un valor típico de 600Ω/100MHz.
- Capacitores de derivación $C_3, C_4$: utilizados para el aislamiento entre la tierra de la interfaz y la tierra digital, con un valor típico de 1000pF/2kV.
- Diodos TVS $D_1, D_2$: utilizados para proteger contra ESD o impactos de alta energía momentáneos, limitando el voltaje de la línea del circuito a un valor predeterminado, asegurando así que los dispositivos de circuito posteriores no se dañen por impactos transitorios de alta energía.

## Referencias y agradecimientos

- [Diseño de protección para circuitos de interfaz](https://blog.csdn.net/weixin_40877615/article/details/94381422)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
