# Esquema de alimentación (Buck) - LMR14050

LMR14050 es un chip convertidor Buck de TI que tiene un amplio rango de voltaje de entrada (4-40V) y puede proporcionar una corriente de salida continua de 5A. Tiene un modo de suspensión en carga ligera para mejorar la eficiencia. Debido a su alta integración interna, se requieren pocos componentes periféricos en el diseño. La frecuencia de conmutación se puede seleccionar en el rango de 200kHz-2.5MHz mediante una resistencia externa $R_T$, o se puede sincronizar con un reloj externo en el rango de frecuencia de 250 kHz-2.3 MHz. Las funciones de protección incluyen apagado por sobrecalentamiento, protección contra sobretensión $V_{OUT}$ (OVP), bloqueo por subvoltaje $V_{IN}$ (UVLO), limitación de corriente por ciclo y protección contra cortocircuitos con plegado de frecuencia.

Repositorio del proyecto: [**Collection_of_Power_Module_Design/DC-DC(Buck)/LMR14050**](<https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/tree/main/DC-DC(Buck)/LMR14050>)

Vista previa en línea del proyecto:

<div class="altium-iframe-viewer">
  <div
    class="altium-ecad-viewer"
    data-project-src="https://github.com/linyuxuanlin/Collection_of_Power_Module_Design/raw/main/DC-DC(Buck)/LMR14050/LMR14050.zip"
  ></div>
</div>

## Características principales

- Topología: DC/DC (Buck)
- Modelo del dispositivo: LMR14050SDDA
- Encapsulado: HSOIC-8
- Voltaje de entrada: 4-40 V
- Voltaje de salida: 0.8-28V
- Corriente de salida: 5A continua
- Frecuencia de trabajo: 200kHz-2.5MHz
- Precio de referencia: ¥11.3
- Otras características
  - Corriente estática de trabajo ultra baja de 40µA
  - Corriente de apagado: 1µA
  - MOSFET de alta lateral de 90mΩ
  - Tiempo de conducción más corto: 75ns
  - Control de modo de corriente
  - Protección térmica, protección contra sobretensión y protección contra cortocircuitos

## Diagrama de funciones internas

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111090855.png)

## Definición de pines

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220110170233.png)

- BOOT: Capacitor de arranque para el MOSFET de alta lateral. Conecte un capacitor de 0.1uF entre BOOT y SW.
- VIN: Entrada de alimentación, conectada a través de un capacitor de desacoplamiento $C_{IN}$.
- EN: Interruptor de habilitación, con una resistencia interna de pull-up. La salida se puede desactivar mediante una señal de entrada inferior a 1.2V. La salida se habilita mediante una señal flotante o conectada a $V_{IN}$. Consulte la sección de ajuste de bloqueo por subvoltaje a continuación.
- RT/SYNC: Entrada de temporización de resistencia o reloj externo. Cuando se utiliza una resistencia externa conectada a tierra para establecer la frecuencia de conmutación, el amplificador interno mantiene este pin a un voltaje fijo. Si el pin se tira por encima del umbral superior del PLL, se producirá un cambio de modo y el pin se convertirá en una entrada sincronizada. El amplificador interno se desactiva y el pin es una entrada de reloj de alta impedancia del PLL interno. Si el borde del reloj se detiene, el amplificador interno se reactiva y el modo de operación vuelve a la programación de frecuencia a través del resistor.?
- FB: Pin de entrada de retroalimentación, conectado a través de una resistencia de división de voltaje desde $V_{OUT}$. No se puede conectar directamente a tierra.
- SS: Pin de control de arranque suave, conectado a un capacitor para establecer el tiempo de arranque suave.
- SW: Salida de conmutación regulada, conectada internamente al MOSFET de alta lateral. Conecte la bobina de potencia.

## Descripción de características

### Principio de regulación



La tensión de salida del LMR14050 se ajusta abriendo el N-MOS de alta lateral y controlando el tiempo de conducción. Durante el tiempo de conducción del N-MOS de alta lateral, la tensión en el pin SW oscila a aproximadamente $V_{IN}$ y la corriente de la bobina L aumenta con una pendiente lineal ($V_{IN}$ - $V_{OUT}$) / L; cuando se apaga el N-MOS de alta lateral, la corriente de la bobina L se descarga con una pendiente de $V_{OUT}$ / L a través del diodo de recuperación. Los parámetros de control del regulador están determinados por el ciclo de trabajo $D = t_{ON} / T_{SW}$, donde $t_{ON}$ es el tiempo de conducción del interruptor superior y $T_{SW}$ es el período de conmutación. El lazo de control del regulador ajusta el ciclo de trabajo D para mantener una tensión de salida constante. En un convertidor reductor ideal, las pérdidas se ignoran, D es proporcional a la tensión de salida y es inversamente proporcional a la tensión de entrada: $D = V_{OUT} / V_{IN}$.

La relación entre la tensión SW y la corriente de la bobina L en el modo de conducción continua (CCM) es la siguiente:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111095020.png)

### Modo de suspensión

En condiciones de carga ligera, el regulador entra en modo de suspensión para mejorar la eficiencia y reducir las pérdidas de conducción de la puerta (al reducir el número de conmutaciones). Si el pico de salida es inferior a 300 mA, se activará el modo de suspensión.

### Diseño del circuito de arranque automático (BOOT)

El LMR14050 integra un convertidor de voltaje de arranque automático. Conectando un capacitor de arranque entre los pines BOOT y SW, se puede proporcionar suficiente voltaje para conducir la puerta del MOS de alta lateral. El valor de referencia del capacitor BOOT es de 0,1 uF (capacitor cerámico X7R o X5R con una tensión nominal de al menos 16 V).

### Ajuste de la tensión de salida

El LMR14050 proporciona una tensión de referencia interna de 0,75 V. La tensión de salida se ajusta mediante un divisor de resistencia conectado al pin FB, que se compara y ajusta internamente. Se recomienda utilizar resistencias de desviación del 1% o menos y un coeficiente de temperatura de 100 ppm o menos para el divisor de resistencia. Seleccione la resistencia inferior $R_{FBB}$ (valor de referencia de 10-100 kΩ) en función de la corriente de división de tensión deseada y calcule la resistencia superior $R_{FBT}$ mediante la fórmula. Se recomienda utilizar valores de resistencia más altos para mejorar la eficiencia en condiciones de carga ligera, pero si son demasiado altos, el regulador será más susceptible al ruido y los errores de voltaje de entrada de la corriente de entrada de FB.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111105814.png)

$$
R_{FBT}=\frac{V_{OUT}-0.75}{0.75}R_{FBB}
$$

### Ajuste de la habilitación y el bloqueo de subvoltaje

Cuando $V_{IN}$ es superior a 3,7 V y EN es superior al umbral de 1,2 V, el LMR14050 activa la salida. Cuando $V_{IN}$ cae por debajo de 3,52 V o EN cae por debajo de 1,2 V, el regulador se apaga. EN tiene una fuente de corriente interna de pull-up (1 uA) para garantizar que el regulador produzca una salida normal cuando el pin EN está flotando.

Puede ajustar los umbrales de voltaje de inicio y apagado ajustando las resistencias de pull-up y pull-down externas de EN:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111111613.png)

$R_{ENT}$ y $R_{ENB}$ se calculan según las siguientes fórmulas:

$$
R_{ENT}=\frac{V_{STRAT}-V_{STOP}}{I_{HYS}}
$$

$$

R_{ENB}=\frac{V_{EN}}{\frac{V_{START}-V_{EN}}{R_{ENT}}+I_{EN}}
$$

Donde $V_{STRAT}$ es el umbral de voltaje de inicio deseado, $V_{STOP}$ es el umbral de voltaje de apagado deseado e $I_{HYS}$ es la corriente de histéresis de EN cuando el voltaje de EN supera los 1,2 V (valor típico de 3,6 uA).

### Arranque suave externo

El arranque suave se utiliza para resistir las corrientes transitorias de sobretensión en el regulador y la carga al encender. Puede configurarlo conectando un capacitor $C_{SS}$ entre los pines SS y GND. Hay una fuente de corriente interna $I_{SS}$ (valor típico de 3 uA) que carga el capacitor y genera una pendiente de 0 V a $V_{REF}$. El tiempo de arranque suave se puede configurar mediante la siguiente fórmula:

$t_{SS}(ms)=\frac{C_{SS}(nF)*V_{REF}(V)}{I_{SS}(uA)}$

El arranque suave se restablecerá cuando el regulador se desactive o se apague internamente.

### Frecuencia de conmutación y sincronización (RT/SYNC)

La frecuencia de conmutación del LMR14050 se puede programar mediante una resistencia $R_T$ conectada entre RT/SYNC y GND. El pin RT/SYNC no puede dejarse flotando o conectarse a tierra, y su valor de resistencia se determina según la siguiente fórmula o gráfico:

$$
R_T(kΩ)=32537*f_{SW}^{-1.045}(kHz)
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111135021.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111135034.png)

La acción de conmutación del LMR14050 también se puede sincronizar con una señal de entrada de reloj externa (250kHz-2.3MHz):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111141247.png)

El oscilador interno se sincroniza con el flanco descendente del reloj externo. Se recomienda que el nivel alto del reloj externo no sea inferior a 1.7V, el nivel bajo no sea superior a 0.5V y el ancho de pulso mínimo no sea inferior a 30ns. Si se conecta una fuente de señal de baja impedancia, la resistencia de programación de frecuencia $R_T$ debe conectarse en paralelo con una resistencia de acoplamiento de CA $C_{COUP}$ (puede ser un condensador cerámico de 10pF) y una resistencia terminal $R_{TERM}$ (por ejemplo, 50Ω) para lograr una mejor coincidencia de impedancia.

### Protección contra sobrecorriente y cortocircuito

El LMR14050 limita el pico de corriente del MOSFET de alta lateral en cada ciclo para evitar situaciones de sobrecorriente. En cada ciclo de conmutación, se compara la corriente máxima del MOSFET de alta lateral con la salida del amplificador de error (EA) menos la compensación de pendiente. La corriente máxima del MOSFET de alta lateral está limitada por un umbral máximo de corriente de pinza constante. Por lo tanto, la limitación del pico de corriente del MOSFET de alta lateral no se ve afectada por la compensación de pendiente y se mantiene constante en todo el rango de ciclo de trabajo.

### Protección contra sobretensión

El LMR14050 tiene un circuito de protección contra sobretensión de salida (OVP) incorporado para minimizar el sobrevoltaje. Cuando el voltaje de retroalimentación (FB) alcanza el umbral de OVP ascendente (109% de VREF), se apaga el MOSFET de alta lateral; cuando cae por debajo del umbral de OVP descendente (107% de VREF), el MOSFET de alta lateral vuelve a funcionar normalmente.

### Protección de apagado térmico

El LMR14050 tiene una función de protección de apagado térmico interna. Cuando la temperatura de la unión supera los 170℃, se activa el apagado térmico y se detiene la conmutación del MOSFET de alta lateral. El reinicio interno se produce cuando la temperatura del chip cae por debajo de 158℃.

## Diseño de referencia

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220111143510.png)

Parámetros de diseño:

- Voltaje de entrada $V_{IN}$: 7-36V, valor típico de 12V
- Voltaje de salida $V_{OUT}$: 5V
- Corriente máxima de salida $I_{O\_MAX}$: 5A
- Respuesta transitoria (0.5-5A): 5%
- Ondulación del voltaje de salida: 50mV
- Ondulación del voltaje de entrada: 400mV
- Frecuencia de conmutación $f_{SW}$: 300kHz
- Tiempo de arranque suave: 5ms

### Configuración del voltaje de salida

Según la fórmula anterior, si necesitamos una salida de 5V, podemos elegir $R_{FBT}$ como 100kΩ y $R_{FBB}$ como 17.4kΩ (valor aproximado de 17.65kΩ, equilibrado mediante ajuste).

Si necesitamos una salida de 12V, podemos elegir $R_{FBT}$ como 100kΩ y $R_{FBB}$ como 6.34kΩ (valor aproximado de 6.666kΩ, equilibrado mediante ajuste).

### Configuración de la frecuencia de conmutación

Elegimos una frecuencia de conmutación de 300kHz, por lo que según la fórmula anterior, elegimos $R_T$ como 84.5kΩ (valor aproximado de 83.9kΩ).

### Selección de la inductancia de salida

En un convertidor DC-DC, los parámetros más críticos de la inductancia son el valor de inductancia, la corriente de saturación y la corriente RMS. La selección del valor de inductancia se basa en la corriente de pico a pico de ondulación deseada $Δi_L$. Debido a que la corriente de ondulación aumenta con el voltaje de entrada, siempre se utiliza el voltaje de entrada máximo para calcular el valor mínimo de inductancia $L_{MIN}$. El valor mínimo de la inductancia de salida se puede calcular mediante la siguiente fórmula:

$$
Δi_L=\frac{V_{OUT}*(V_{IN\_MAX}-V_{OUT})}{V_{IN\_MAX}*L*f_{SW}}
$$

$$
L_{MIN}=\frac{V_{IN\_MAX}-V_{OUT}}{I_{OUT}*K_{IND}}*\frac{V_{OUT}}{V_{IN\_MAX}*f_{SW}}
$$

Donde $K_{IND}$ es el coeficiente que representa la corriente de ondulación del inductor en relación a la corriente máxima de salida, y su valor razonable debería estar entre el 20% y el 40%. Durante eventos de operación de cortocircuito o sobrecarga instantánea, la corriente de inductor RMS y de pico puede ser muy alta. El valor nominal de la corriente del inductor debe ser mayor que el límite de corriente.

En general, es mejor tener un valor de inductancia más bajo, ya que generalmente proporciona una respuesta transitoria más rápida, una DCR más pequeña y un tamaño más pequeño. Sin embargo, un valor de inductancia demasiado bajo puede provocar una gran corriente de ondulación en el inductor, lo que puede activar incorrectamente la protección contra sobrecarga en carga completa. Debido a que la corriente RMS es ligeramente alta, también produce más pérdidas de conducción. Una corriente de ondulación en el inductor más grande también significa una ondulación de voltaje de salida más grande. Para el control de modo de corriente pico, no se recomienda una corriente de ondulación en el inductor demasiado pequeña, y una corriente de pico más grande puede mejorar la relación señal-ruido del comparador.

En el diseño de referencia, el valor de $K_{IND}$ se toma como 0,4, por lo que el valor mínimo de inductancia se calcula como 7,17 uH, y el valor cercano es 8,2 uH. Se puede utilizar un inductor de ferrita de 8,2 μH con una corriente RMS de 7A y una corriente de saturación de 10A.

### Selección del capacitor de salida

La selección del capacitor de salida $C_{OUT}$ afecta directamente la ondulación de voltaje de salida en estado estable, la estabilidad del lazo y el sobrevoltaje y la caída de voltaje durante la transición de corriente de carga. La ondulación de salida se compone esencialmente de dos partes. Uno es causado por la corriente de ondulación del inductor a través de la resistencia equivalente en serie (ESR) del capacitor de salida:

$$
ΔV_{OUT\_ESR}=Δi_L*ESR=K_{IND}*I_{OUT}*ESR
$$

El otro es causado por la carga y descarga del capacitor de salida por la corriente de ondulación del inductor:

$$
ΔV_{OUT\_C}=\frac{Δi_L}{8*f_{SW}*C_{OUT}}=\frac{K_{IND}*I_{OUT}}{8*f_{SW}*C_{OUT}}
$$

Estas dos ondulaciones de voltaje no están en fase, por lo que la ondulación pico a pico real será menor que la suma de ambas.

Si el sistema requiere una regulación de voltaje estricta (escalones de corriente grandes y una tasa de cambio de voltaje rápida), entonces la selección del capacitor de salida estará limitada por las especificaciones de rendimiento transitorio. Cuando se produce un aumento rápido de carga grande, el capacitor de salida puede proporcionar la carga necesaria antes de que la corriente del inductor alcance el nivel adecuado. El lazo de control del regulador generalmente requiere al menos tres ciclos de reloj para responder a la caída de voltaje de salida. El capacitor de salida debe ser lo suficientemente grande como para proporcionar la diferencia de corriente de tres ciclos de reloj para mantener el voltaje de salida dentro del rango especificado.

Cuando la carga disminuye repentinamente, el capacitor de salida absorberá la energía almacenada en el inductor. El diodo de pinza no puede conducir corriente, por lo que la energía eléctrica en el inductor provocará un sobrevoltaje en la salida. La fórmula para calcular el valor mínimo del capacitor de salida necesario para una caída de voltaje específica es:

$C_{OUT}>\frac{3*(I_{OH}-I_{OL})}{f_{SW}*V_{US}}$

La fórmula para calcular el valor mínimo del capacitor de salida necesario para mantener el sobrevoltaje dentro del rango especificado es:

$C_{OUT}>\frac{I_{OH}^2-I_{OL}^2}{(V_{OUT}+V_{OS})^2-V_{OUT}^2}*L$

Donde:

- $K_{IND}$ es la relación de ondulación de corriente del inductor ($Δi_L/I_{OUT}$)
- $I_{OL}$ es la corriente de salida baja durante la transición de carga
- $I_{OH}$ es la corriente de salida alta durante la transición de carga
- $V_{US}$ es la caída de voltaje de salida objetivo
- $V_{OS}$ es el sobrevoltaje de salida objetivo

En el diseño de referencia, la ondulación de salida objetivo es de 50 mV. Suponiendo que $ΔV_{OUT\_ESR}=ΔV_{OUT\_C}=50mV$, $K_{IND}$ tiene un valor de 0,4, $ESR$ no es mayor a 25 mΩ, y $C_{OUT}$ no es menor a 16,7 μF, el rango de sobrevoltaje y caída de voltaje en el diseño de referencia es de $V_{US}=V_{OS}=5%*V_{OUT}=250mV$. Por lo tanto, $C_{OUT}$ se puede calcular como no menor a 180 uF y 79,2 uF, y se selecciona el estándar más estricto de 180 uF, utilizando 4 capacitores cerámicos de 47 uF (16V, X7R, ESR de 5 mΩ) en paralelo.

### Selección del diodo Schottky

La tensión de ruptura nominal del diodo debe ser al menos un 25% mayor que la tensión de entrada máxima. Para obtener la mejor confiabilidad, la corriente nominal del diodo debe ser igual a la corriente máxima de salida del regulador. Cuando la tensión de entrada es mucho mayor que la tensión de salida, la corriente promedio del diodo será más baja, y en este caso se puede utilizar un diodo con una corriente nominal promedio más baja, aproximadamente $(1-D) * I_{OUT}$, pero la corriente nominal de pico debe ser mayor que la corriente máxima de carga. Por lo general, se recomienda comenzar con una corriente nominal de 6-7 A. 

### Selección del capacitor de entrada

LMR14050 requiere un condensador de acoplamiento de alta frecuencia y un condensador de entrada de alta capacidad. El valor típico recomendado para el condensador de acoplamiento de alta frecuencia es de 4.7-10 μF (X5R/X7R, condensador cerámico, con una resistencia de voltaje de al menos el doble del voltaje de entrada máximo). En el diseño de referencia, se utilizan dos condensadores cerámicos X7R de 2.2 μF y 100 V de voltaje nominal. El condensador de filtrado de alta frecuencia debe colocarse cerca del regulador de voltaje.

El condensador de alta capacidad proporciona amortiguación para los picos de voltaje, con un valor de referencia de 47uF o 100uF de condensador electrolítico.

### Selección del condensador de arranque BOOT

LMR14050 requiere un condensador de arranque BOOT, como se mencionó anteriormente, el valor de referencia del condensador BOOT es de 0.1uF (condensador cerámico X7R o X5R, resistencia de voltaje de al menos 16V).

### Selección del condensador de arranque suave

Según la fórmula anterior, si se establece un tiempo de arranque suave de 5ms, se puede obtener un valor de condensador de arranque suave de 22 nF (aproximadamente 20nF de valor calculado).

## Referencia de diseño de Layout

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220110183248.png)

Sugerencias de diseño de Layout para reducir la EMI:

1. La red de retroalimentación, la resistencia $R_{FBT}$ y $R_{FBB}$ deben colocarse lo más cerca posible del pin FB. La ruta de muestreo de $V_{OUT}$ debe estar alejada de la ruta de generación de ruido, preferiblemente a través de una capa de blindaje en el otro lado.
2. El condensador de acoplamiento de entrada debe colocarse lo más cerca posible de $V_{IN}$ y GND.
3. La inductancia debe colocarse cerca del pin SW para reducir el ruido magnético y electrostático.
4. El condensador de salida $C_{OUT}$ debe colocarse cerca del nodo de la inductancia y el diodo, con líneas lo más cortas posible para reducir el ruido de conducción y radiación y mejorar la eficiencia.
5. La conexión a tierra del diodo, $C_{IN}$ y $C_{OUT}$ debe ser lo más pequeña posible y solo conectarse en un punto (preferiblemente en el punto de conexión a tierra de $C_{OUT}$) al plano de tierra del sistema para minimizar el ruido de conducción en el plano de tierra del sistema.

## Pruebas reales

Entrada de 24V, salida de carga completa de 5V/5A, salida real de 4.95V/5.00A, ondulación de 15mV, temperatura de 110℃.

## Referencias y agradecimientos

- [Documentación técnica · LMR14050](https://www.ti.com.cn/product/cn/LMR14050#tech-docs)
- [N-1149 Directrices de diseño de Layout para fuentes de alimentación conmutadas](https://www.ti.com/lit/an/snva021c/snva021c.pdf?ts=1641814411004)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.