# Esquema de alimentación (Buck) - LMR14050

LMR14050 es un chip convertidor Buck de TI que tiene un amplio rango de voltaje de entrada (4-40V) y puede proporcionar una corriente de salida continua de 5A. Tiene un modo de suspensión en carga ligera para mejorar la eficiencia. Debido a su alta integración interna, requiere pocos componentes periféricos en el diseño. La frecuencia de conmutación se puede seleccionar en el rango de 200kHz a 2.5MHz mediante una resistencia externa $R_T$, y también se puede sincronizar con una señal de reloj externa en el rango de frecuencia de 250kHz a 2.3MHz. Las funciones de protección incluyen apagado por sobrecalentamiento, protección contra sobretensión ($V_{OUT}$ OVP), bloqueo por subtensión ($V_{IN}$ UVLO), limitación de corriente por ciclo y protección contra cortocircuitos con plegado de frecuencia.

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
- Frecuencia de operación: 200kHz-2.5MHz
- Precio de referencia: ￥ 11.3
- Otras características
  - Corriente estática de funcionamiento ultrabaja de 40µA
  - Corriente de apagado: 1µA
  - MOSFET de alta cara superior de 90mΩ
  - Tiempo de conducción más corto: 75ns
  - Control de modo de corriente
  - Protección térmica, protección contra sobretensión y protección contra cortocircuitos

## Diagrama de funciones internas

![](https://media.wiki-power.com/img/20220111090855.png)

## Definición de pines

![](https://media.wiki-power.com/img/20220110170233.png)

- BOOT: Capacitor de arranque para el MOSFET de la cara superior. Conecte un capacitor de 0.1uF entre BOOT y SW.
- VIN: Entrada de alimentación, conectada a través de un capacitor de desacoplamiento $C_{IN}$.
- EN: Interruptor de habilitación, con pull-up interno. Al conectar a tierra externamente por debajo de 1.2V, se puede desactivar la salida. Dejar flotante o conectar a $V_{IN}$ para habilitar la salida. Consulte la sección de ajuste de subtensión para más detalles.
- RT/SYNC: Temporización de resistencia o entrada de reloj externo. Cuando se utiliza una resistencia externa conectada a tierra para configurar la frecuencia de conmutación, el amplificador interno mantiene este pin a un voltaje fijo. Si se tira del pin por encima del umbral superior del PLL, se producirá un cambio de modo y el pin se convertirá en una entrada sincronizada. El amplificador interno se deshabilita y el pin se convierte en una entrada de reloj de alta impedancia para el PLL interno. Si se detiene el flanco del reloj, se vuelve a habilitar el amplificador interno y el modo de operación vuelve a la programación de frecuencia a través de la resistencia.?
- FB: Pin de entrada de retroalimentación, se utiliza una resistencia para dividir el voltaje de $V_{OUT}$ como retroalimentación, no se puede conectar directamente a tierra.
- SS: Pin de control de arranque suave, se conecta un capacitor para ajustar el tiempo de arranque suave.
- SW: Salida del interruptor regulador, conectada internamente al MOSFET de la cara superior. Conecte la bobina de potencia.

## Descripción de características

### Principio de regulación de voltaje

LMR14050 ajusta la tensión de salida mediante la apertura del N-MOS de alta lateral y el control del tiempo de conducción. Durante el período de conducción del N-MOS de alta lateral, la tensión en el pin SW oscila aproximadamente a $V_{IN}$ y la corriente de la bobina (iL) aumenta con una pendiente lineal de ($V_{IN}$ - $V_{OUT}$) / L. Cuando se apaga el N-MOS de alta lateral, la corriente de la bobina se descarga con una pendiente de $V_{OUT}$ / L a través del diodo de recirculación. Los parámetros de control del regulador están determinados por el ciclo de trabajo $D = t_{ON} / T_{SW}$, donde $t_{ON}$ es el tiempo de conducción del interruptor de alta lateral y $T_{SW}$ es el período de conmutación del interruptor. El lazo de control del regulador mantiene una tensión de salida constante ajustando el ciclo de trabajo D. En un convertidor reductor ideal, las pérdidas se ignoran y D es directamente proporcional a la tensión de salida y inversamente proporcional a la tensión de entrada: $D = V_{OUT} / V_{IN}$.

La relación entre la tensión SW y la corriente de la bobina en el modo de conducción continua (CCM) se muestra a continuación:

![](https://media.wiki-power.com/img/20220111095020.png)

### Modo de suspensión

En condiciones de carga ligera, el regulador entra en modo de suspensión para mejorar la eficiencia y reducir las pérdidas de accionamiento de la compuerta (al reducir el número de conmutaciones). Si el valor pico de la salida es inferior a 300 mA, se activará el modo de suspensión.

### Diseño del circuito de arranque (BOOT)

LMR14050 integra un convertidor de voltaje de arranque interno. Al conectar un condensador de arranque entre los pines BOOT y SW, se puede proporcionar suficiente voltaje para accionar la compuerta del MOS de alta lateral. El valor de referencia del condensador BOOT es de 0.1uF (condensador cerámico X7R o X5R con una tensión nominal de al menos 16V).

### Ajuste de la tensión de salida

LMR14050 proporciona una tensión de referencia interna de 0.75V. La tensión de salida se divide mediante una resistencia en el divisor de tensión y se aplica al pin FB para su comparación y ajuste interno. Se recomienda utilizar resistencias de división con una desviación del 1% o inferior y un coeficiente de temperatura de 100 ppm o inferior. La resistencia inferior $R_{FBB}$ (con un valor de referencia de 10-100kΩ) se selecciona en función de la corriente de división deseada, y la resistencia superior $R_{FBT}$ se calcula mediante la siguiente fórmula. Se recomienda utilizar valores de resistencia más altos para mejorar la eficiencia en condiciones de carga ligera, pero si son demasiado altos, el regulador será más susceptible al ruido y a los errores de voltaje provenientes de la corriente de entrada FB.

![](https://media.wiki-power.com/img/20220111105814.png)

$$
R_{FBT}=\frac{V_{OUT}-0.75}{0.75}R_{FBB}
$$

### Ajuste de EN (Habilitación) y UVLO (Undervoltage Lockout)

Cuando $V_{IN}$ es mayor que 3.7V y EN supera el umbral de 1.2V, LMR14050 activa la salida. Cuando $V_{IN}$ cae por debajo de 3.52V o EN cae por debajo de 1.2V, el regulador se apaga. EN tiene una fuente de corriente interna de pull-up (1uA) para garantizar un funcionamiento normal cuando el pin EN está flotante.

El ajuste de los umbrales de voltaje de inicio y apagado se puede lograr mediante la resistencia externa de pull-up y pull-down en EN, según las siguientes fórmulas:

![](https://media.wiki-power.com/img/20220111111613.png)

$R_{ENT}$ y $R_{ENB}$ se calculan de acuerdo con las siguientes fórmulas:

$$
R_{ENT}=\frac{V_{START}-V_{STOP}}{I_{HYS}}
$$

$$
R_{ENB}=\frac{V_{EN}}{\frac{V_{START}-V_{EN}}{R_{ENT}}+I_{EN}}
$$

Donde $V_{START}$ es el umbral de voltaje de inicio deseado, $V_{STOP}$ es el umbral de voltaje de apagado deseado, e $I_{HYS}$ es la corriente de histéresis de EN cuando el voltaje de EN supera los 1.2V (valor típico de 3.6uA).

### Arranque externo suave (Soft-Start)

El arranque suave se utiliza para mitigar la corriente de sobretensión en el regulador y la carga al encenderlo. Se puede configurar mediante un condensador $C_{SS}$ conectado externamente entre los pines SS y GND. Hay una fuente de corriente interna $I_{SS}$ (valor típico de 3uA) que carga el condensador y genera una pendiente de 0V a $V_{REF}$. El tiempo de arranque suave se puede configurar mediante la siguiente fórmula:

$t_{SS}(ms)=\frac{C_{SS}(nF)*V_{REF}(V)}{I_{SS}(uA)}$

El arranque suave se restablecerá cuando el regulador se desactive o se cierre internamente.

### Frecuencia de conmutación y sincronización (RT/SYNC)

LMR14050 permite programar la frecuencia de conmutación conectando una resistencia $R_T$ entre RT/SYNC y GND. El pin RT/SYNC no debe dejarse flotante ni conectarse a tierra, y su valor de resistencia se determina según la siguiente fórmula o tabla:

$$
R_T(kΩ)=32537*f_{SW}^{-1.045}(kHz)
$$

![](https://media.wiki-power.com/img/20220111135021.png)

![](https://media.wiki-power.com/img/20220111135034.png)

La acción de conmutación del LMR14050 también puede sincronizarse mediante una señal de entrada de reloj externo (250kHz-2.3MHz):

![](https://media.wiki-power.com/img/20220111141247.png)

El oscilador interno se sincronizará con el flanco descendente del reloj externo. Se recomienda que el nivel alto del reloj externo no sea inferior a 1.7V, el nivel bajo no sea superior a 0.5V y el ancho de pulso mínimo no sea inferior a 30ns. Si se conecta una fuente de señal de baja impedancia, la resistencia de ajuste de frecuencia $R_T$ debe conectarse en paralelo con una resistencia de acoplamiento de CA $C_{COUP}$ (que puede ser un condensador cerámico de 10pF) y conectarse a una resistencia terminal $R_{TERM}$ (por ejemplo, 50Ω) para lograr una mejor coincidencia de impedancia.

### Protección contra sobrecorriente y cortocircuito

El LMR14050 limita el pico de corriente del MOSFET de alta lateralidad en cada ciclo para evitar situaciones de sobrecorriente. En cada ciclo de conmutación, se compara la corriente pico del MOSFET de alta lateralidad con la salida del amplificador de error (EA) después de compensar la pendiente. La corriente pico del MOSFET de alta lateralidad está limitada por un umbral de corriente máxima constante. Por lo tanto, la limitación de corriente pico del MOSFET de alta lateralidad no se ve afectada por la compensación de pendiente y se mantiene constante en todo el rango de ciclo de trabajo.

### Protección contra sobretensión

El LMR14050 tiene un circuito de protección contra sobretensión (OVP) incorporado para minimizar la sobretensión. Cuando el voltaje de FB alcanza el umbral de OVP ascendente (109% de VREF), se apaga el MOSFET de alta lateralidad; cuando cae por debajo del umbral de OVP descendente (107% de VREF), el MOSFET de alta lateralidad vuelve a funcionar normalmente.

### Protección de apagado térmico

El LMR14050 tiene una función de protección de apagado térmico interna. Cuando la temperatura de la unión supera los 170℃, se activa el apagado térmico y el MOSFET de alta lateralidad deja de conmutar. El reinicio interno solo ocurrirá cuando la temperatura del chip caiga por debajo de 158℃.

## Diseño de referencia

![](https://media.wiki-power.com/img/20220111143510.png)

Parámetros de diseño:

- Voltaje de entrada $V_{IN}$: 7-36V, valor típico de 12V
- Voltaje de salida $V_{OUT}$: 5V
- Corriente máxima de salida $I_{O\_MAX}$: 5A
- Respuesta transitoria (0.5-5A): 5%
- Ondulación de voltaje de salida: 50mV
- Ondulación de voltaje de entrada: 400mV
- Frecuencia de conmutación $f_{SW}$: 300kHz
- Tiempo de arranque suave: 5ms

### Configuración del voltaje de salida

Según la fórmula anterior, si deseamos un voltaje de salida de 5V, podemos seleccionar $R_{FBT}$ como 100kΩ y $R_{FBB}$ como 17.4kΩ (aproximadamente 17.65kΩ, ajustado para equilibrar las pérdidas).

Si deseamos un voltaje de salida de 12V, podemos seleccionar $R_{FBT}$ como 100kΩ y $R_{FBB}$ como 6.34kΩ (aproximadamente 6.666kΩ, ajustado para equilibrar las pérdidas).

### Configuración de la frecuencia de conmutación

Seleccionamos una frecuencia de conmutación de 300kHz y, según la fórmula anterior, elegimos $R_T$ como 84.5kΩ (aproximadamente 83.9kΩ).

### Selección de la inductancia de salida

En un convertidor DC-DC, los parámetros más importantes de la inductancia son el valor de inductancia, la corriente de saturación y la corriente RMS. La selección del valor de inductancia se basa en la corriente de pico a pico de ondulación deseada $Δi_L$. Dado que la corriente de ondulación aumenta con el voltaje de entrada, siempre se utiliza el voltaje de entrada máximo para calcular el valor mínimo de inductancia $L_{MIN}$. El valor mínimo de la inductancia de salida se puede calcular mediante la siguiente fórmula:

$$
Δi_L=\frac{V_{OUT}*(V_{IN\_MAX}-V_{OUT})}{V_{IN\_MAX}*L*f_{SW}}
$$

$$
L_{MIN}=\frac{V_{IN\_MAX}-V_{OUT}}{I_{OUT}*K_{IND}}*\frac{V_{OUT}}{V_{IN\_MAX}*f_{SW}}
$$

En este caso, $K_{IND}$ es el coeficiente que representa la corriente de ondulación del inductor en relación a la corriente de salida máxima, y su valor óptimo debería estar entre el 20% y el 40%. Durante eventos de cortocircuito o sobrecarga transitoria, la corriente de ondulación del inductor puede ser alta tanto en valor RMS como en valor pico. El valor nominal de corriente del inductor debe ser mayor que el límite de corriente.

En general, es preferible tener un valor de inductancia más bajo, ya que esto suele resultar en una respuesta transitoria más rápida, una resistencia en serie equivalente (DCR) más pequeña y un tamaño más reducido. Sin embargo, un valor de inductancia demasiado bajo puede generar una corriente de ondulación del inductor más grande, lo que podría activar incorrectamente la protección contra sobrecorriente en condiciones de carga completa. Además, debido a la corriente RMS ligeramente más alta, también se producirán más pérdidas por conducción. Una mayor corriente de ondulación del inductor también implica una mayor ondulación de voltaje de salida. Para el control de corriente pico, no se recomienda tener una corriente de ondulación del inductor demasiado pequeña, ya que una mayor corriente de ondulación de pico puede mejorar la relación señal-ruido del comparador.

En el diseño de referencia, se utiliza un valor de $K_{IND}$ de 0.4, por lo que se calcula un valor mínimo de inductancia de 7.17uH, y el valor más cercano es de 8.2uH. Se puede utilizar un inductor de ferrita de 8.2 μH con una corriente RMS de 7A y una corriente de saturación de 10A.

### Selección del capacitor de salida

La elección del capacitor de salida $C_{OUT}$ afecta directamente la ondulación de voltaje en estado estacionario, la estabilidad del lazo, y el sobrepico y la caída de voltaje durante las transiciones de corriente de carga. La ondulación de voltaje de salida se compone esencialmente de dos partes. Una es causada por la ondulación de corriente del inductor a través de la resistencia serie equivalente (ESR) del capacitor de salida:

$$
ΔV_{OUT\_ESR}=Δi_L*ESR=K_{IND}*I_{OUT}*ESR
$$

La otra es causada por la carga y descarga del capacitor de salida debido a la ondulación de corriente del inductor:

$$
ΔV_{OUT\_C}=\frac{Δi_L}{8*f_{SW}*C_{OUT}}=\frac{K_{IND}*I_{OUT}}{8*f_{SW}*C_{OUT}}
$$

Estas dos ondulaciones de voltaje no están en fase, por lo que la ondulación pico a pico real será menor que la suma de ambas.

Si el sistema requiere una regulación de voltaje estricta (con transiciones de corriente de carga alta y una alta tasa de cambio), el capacitor de salida estará limitado por las especificaciones de rendimiento transitorio. Cuando se produce un aumento rápido de carga, el capacitor de salida debe suministrar la carga requerida antes de que la corriente del inductor alcance un nivel adecuado. El lazo de control del regulador generalmente requiere al menos tres ciclos de reloj para responder a una caída de voltaje de salida. El capacitor de salida debe ser lo suficientemente grande como para proporcionar la diferencia de corriente de tres ciclos de reloj y mantener el voltaje de salida dentro del rango especificado.

Cuando la carga disminuye repentinamente, el capacitor de salida absorberá la energía almacenada en el inductor. Dado que el diodo de pinza no puede conducir corriente, la energía almacenada en el inductor resultará en un sobrepico de voltaje de salida. La fórmula para calcular el valor mínimo del capacitor de salida necesario para evitar este sobrepico es:

$C_{OUT}>\frac{3*(I_{OH}-I_{OL})}{f_{SW}*V_{US}}$

La fórmula para calcular el valor mínimo del capacitor de salida necesario para mantener el sobrepico de voltaje dentro de un rango especificado es:

$C_{OUT}>\frac{I_{OH}^2-I_{OL}^2}{(V_{OUT}+V_{OS})^2-V_{OUT}^2}*L$

Donde:

- $K_{IND}$ es la relación de ondulación de corriente del inductor ($Δi_L/I_{OUT}$)
- $I_{OL}$ es la corriente de salida baja durante la transición de carga
- $I_{OH}$ es la corriente de salida alta durante la transición de carga
- $V_{US}$ es el sobrepico de voltaje objetivo
- $V_{OS}$ es el sobrepico de voltaje objetivo

En el diseño de referencia, la ondulación de salida objetivo es de 50mV. Suponiendo que $ΔV_{OUT\_ESR}=ΔV_{OUT\_C}=50mV$, $K_{IND}$ tiene un valor de 0.4, $ESR$ no es mayor a 25mΩ, y $C_{OUT}$ no es menor a 16.7 μF, el rango de sobrepico y caída objetivo en el diseño de referencia es $V_{US}=V_{OS}=5%*V_{OUT}=250mV$. Por lo tanto, se calcula que $C_{OUT}$ debe ser mayor o igual a 180uF y 79.2uF respectivamente. Se selecciona el estándar más estricto de 180uF, utilizando 4 capacitores cerámicos de 47uF (16V, X7R, ESR de 5mΩ) en paralelo.

### Selección del diodo Schottky

La tensión de ruptura nominal del diodo debe ser al menos un 25% más alta que la tensión de entrada máxima. Para obtener la máxima confiabilidad, la corriente nominal del diodo debe ser igual a la corriente de salida máxima del regulador. Cuando la tensión de entrada es mucho mayor que la tensión de salida, la corriente promedio del diodo será más baja, por lo que se puede utilizar un diodo con una corriente nominal promedio más baja, aproximadamente $(1-D) * I_{OUT}$, pero la corriente nominal de pico debe ser mayor que la corriente de carga máxima. Por lo general, se recomienda comenzar con 6-7A.

### Selección del capacitor de entrada

El LMR14050 requiere un capacitor de desacople de alta frecuencia en la entrada y un capacitor de entrada de alta capacidad. El valor típico recomendado para el capacitor de desacople de alta frecuencia es de 4.7-10 μF (capacitor cerámico X5R/X7R, con una tensión nominal al menos el doble de la tensión de entrada máxima). En el diseño de referencia, se utilizan dos capacitores cerámicos X7R de 2.2 μF y 100 V de tensión nominal. El capacitor de filtrado de alta frecuencia debe colocarse cerca del regulador.

### Selección del condensador de gran capacidad

El condensador de gran capacidad proporciona amortiguación para los picos de voltaje, con un valor de referencia de 47uF o 100uF de condensador electrolítico.

### Selección del condensador de arranque (BOOT)

El LMR14050 requiere un condensador de arranque (BOOT), como se mencionó anteriormente, el valor de referencia para el condensador BOOT es de 0.1uF (condensador cerámico X7R o X5R, con una tensión nominal de al menos 16V).

### Selección del condensador de arranque suave

Según la fórmula mencionada anteriormente, si se establece un tiempo de arranque suave de 5ms, se obtiene un valor de 22nF (aproximadamente 20nF calculado) para el condensador de arranque suave.

## Referencia de diseño

![](https://media.wiki-power.com/img/20220110183248.png)

Recomendaciones de diseño para reducir la interferencia electromagnética (EMI):

1. La red de retroalimentación, las resistencias $R_{FBT}$ y $R_{FBB}$ deben colocarse lo más cerca posible del pin FB. La ruta de muestreo de $V_{OUT}$ debe estar alejada de las rutas generadoras de ruido, preferiblemente en la capa opuesta de la capa de blindaje.
2. El condensador de desacoplamiento de entrada debe colocarse lo más cerca posible de $V_{IN}$ y GND.
3. El inductor debe colocarse cerca del pin SW para reducir el ruido magnético y el ruido electrostático.
4. El condensador de salida $C_{OUT}$ debe colocarse cerca del nodo del inductor y el diodo, con rutas de conexión lo más cortas posible para reducir el ruido de conducción y radiación, y mejorar la eficiencia.
5. La conexión a tierra del diodo, $C_{IN}$ y $C_{OUT}$ debe ser lo más pequeña posible y solo conectarse en un punto (preferiblemente en el punto de conexión a tierra de $C_{OUT}$) a la capa de tierra del sistema, para minimizar el ruido de conducción en la capa de tierra del sistema.

## Pruebas prácticas

Entrada de 24V, salida de carga completa de 5V/5A, salida real de 4.95V/5.00A, ondulación de 15mV, temperatura de 110℃.

## Referencias y agradecimientos

- [Documento técnico · LMR14050](https://www.ti.com.cn/product/cn/LMR14050#tech-docs)
- [N-1149 Pautas de diseño de layout para fuentes de alimentación conmutadas](https://www.ti.com/lit/an/snva021c/snva021c.pdf?ts=1641814411004)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
