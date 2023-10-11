# Fundamentos de la Prueba de Señal Mixta

> Esta publicación solo está disponible en inglés.

La señal mixta contiene tanto señales analógicas como digitales. Los dispositivos que procesan señales mixtas típicamente incluyen ADC, DAC, interruptores y multiplexores analógicos, amplificadores de retención de muestra, entre otros.

Como parte de ella, las señales analógicas son señales que usamos en el mundo real, como la voz o la temperatura, son continuas tanto en el tiempo como en la amplitud. Para procesar señales analógicas en computadoras, necesitamos convertirlas en señales digitales, ya que son discretas tanto en el tiempo como en la amplitud.

## Teoría del muestreo

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220929094314.png)

La teoría del muestreo se aplica a la señal para que sea periódica, o se introducirán errores.

### Teorema de Nyquist

Usamos el **Teorema de Nyquist** para obtener la frecuencia de muestreo mínima al muestrear señales:

$$
F_s≥2F_i
$$

Debemos muestrear a una frecuencia mayor que el doble de la frecuencia más alta de interés, para poder recrear una señal a partir de sus muestras y evitar perder información.

Si muestreamos a una frecuencia menor que la tasa de Nyquist, exhibirá un fenómeno llamado **aliasing** (componentes no deseadas) cuando intentemos convertirlo de vuelta a una señal continua en el tiempo, y algunas de las frecuencias en la señal original pueden perderse.

Para minimizar el problema de aliasing, necesitamos eliminar la frecuencia mayor que $\frac{F_s}{2}$ de la señal, a través del filtro antialiasing (por ejemplo, filtro pasa bajos):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220930154335.png)

### Muestreo Coherente

Si un conjunto de muestras de tiempo no contiene un número entero preciso de ciclos, se producirá **fugas espectrales**.

La **muestreo coherente** es para garantizar la continuidad del muestreo y evitar la fuga espectral, garantiza que un conjunto de muestras (una serie de muestras que representan la señal analógica) tenga una relación fija y bien definida entre la frecuencia de muestreo $F_s$, el número de muestras $N$, la frecuencia de la señal de prueba $F_i$ y el número de períodos de señal de prueba muestreados $M$:

$$
\frac{M}{N}=\frac{F_i}{F_s}
$$

El tiempo total requerido para tomar todas las muestras se llama **Período de Prueba Unitario (UTP)** y requiere $M$ ciclos de la señal de prueba, que tiene una frecuencia de $F_i$.

Por ejemplo, si queremos calcular el $F_s$ de una onda sinusoidal continua repetitiva, donde $F_i$ es 1kHz, $M=3$ y $N=16$:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220930164712.png)

Entonces podemos concluir que $F_s=5.333kHz$.

Consejos importantes de muestreo coherente:

- Aumentar $M$ y/o $N$ aumentará tanto la precisión como el tiempo de prueba.
- $M$ y $N$ deben ser enteros.
- $N$ debe ser una potencia de 2 al usar la Transformada Rápida de Fourier (FFT).
- Se recomienda que $M$ y $N$ sean primos entre sí para que cada muestra proporcione información única. Descrito a continuación.

Si $M$ y $N$ no son primos entre sí ($M=3,N=12$), las muestras se toman en la misma posición en cada ciclo, por lo que no hay información nueva:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220930170300.png)

Si $M$ y $N$ son primos entre sí ($M=3,N=16$), por lo que son primos entre sí y cada muestra es discreta, por lo que proporciona información única:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220930170343.png)

## Algoritmos comunes de análisis de frecuencia

Para $N$ muestras de señal en el dominio del tiempo, hay $N$ valores de señal en el dominio de la frecuencia, y hay $N/2$ valores de espectro de potencia en el dominio de la frecuencia. A continuación se muestra un ejemplo típico de componentes espectrales:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221002145846.png)

Existen varios parámetros para describir las componentes espectrales de la siguiente manera:

- Relación señal-ruido (SNR)（信噪比）
- Distorsión armónica total (THD)（总谐波失真）
- Relación señal-ruido y distorsión (SINAD)（信纳比）
- Distorsión de intermodulación (IM)（互调失真）
- Rango dinámico libre de espurias (SFDR)（无杂散动态范围）

### Relación señal-ruido (SNR)

La **relación señal-ruido (SNR)** se deriva almacenando primero el valor del fundamental (potencia de la señal):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221002151235.png)

Luego se elimina la componente de corriente continua y las armónicas (generalmente hasta 5):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221002151402.png)

A continuación, se suman todos los bins del espectro de potencia restante (la potencia del ruido) medido por el valor RMS (raíz cuadrada media, el voltaje analógico que es igual a un voltaje de corriente continua que contiene la misma cantidad de energía, para una onda sinusoidal, el valor RMS es 0,707 veces el valor pico):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221002151646.png)

En última instancia, podemos concluir que:

$$
{SNR}(dB)=10log_{10}(\frac{{Fundamental}}{{Potencia\ de\ ruido}})
$$

SNR se expresa generalmente en decibelios (dB) y a menudo es un valor positivo (suponiendo que la potencia fundamental es mucho mayor que la potencia del ruido).

### Distorsión armónica total (THD)

La **distorsión armónica total (THD)** se deriva manteniendo una suma acumulada de la potencia armónica total (generalmente solo las primeras cinco armónicas, comenzando en la segunda armónica):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221002155148.png)

Y podemos concluir que:

$$
{THD}(dB)=10log_{10}(\frac{{Potencia \ Armónica}}{{Fundamental}})
$$

THD suele ser un valor negativo (suponiendo que la Potencia Fundamental es mucho mayor que la Potencia Armónica total).

### Relación Señal-Ruido y Distorsión (SINAD)

**Relación Señal-Ruido y Distorsión (SINAD)** es la misma metodología que el cálculo de SNR, pero ahora se agrega la potencia de las armónicas y solo se anula el componente de CC.

$$
{SINAD}=\frac{S}{N+D}
$$

Y podemos concluir que:

$$
\because {SNR}=\frac{S}{N}, {THD}=\frac{D}{S}
$$

$$
\therefore {SNR}^{-1}+{THD}=\frac {N}{S}+\frac {D}{S}=\frac {N+D}{S}={SINAD}^{-1}
$$

$$
\therefore {SINAD}=({SNR}^{-1}+{THD})^{-1}
$$

### Distorsión de Intermodulación (IM)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221018162800.png)

La Distorsión de Intermodulación (IM) ocurre cuando se utilizan dos o más señales en un sistema no lineal. El espectro no solo consistirá en las señales originales, sino que también contendrá la suma y la diferencia de las señales de entrada junto con sus armónicos.

### Rango Dinámico Libre de Espurios (SFRD)

**Rango Dinámico Libre de Espurios (SFRD)** se deriva encontrando el elemento más alto después del fundamental (ignorando el componente de CC):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221002161334.png)

Tenga en cuenta que el elemento más alto puede o no ser armónico. Por lo tanto, podemos concluir que:

$$
{SFDR}(dB)=10log_{10}(\frac{{Fundamental}}{{Siguiente \ Más \ Alto}})
$$

El Rango Dinámico Libre de Espurios es un valor positivo (suponiendo que la Potencia Fundamental es mucho mayor que la Potencia de Espurio siguiente más alta.

## Arquitectura del Probador Genérico de Señal Mixta

En el probador genérico de señal mixta, el AWG (fuente de CA) y el WD (digitalizador de CA) están conectados al DUT a través de interconexiones de relé a través de la placa de canal.

### Generador de forma de onda arbitraria (AWG)

El **Generador de forma de onda arbitraria (AWG)** es un generador de señal de baja distorsión. Contiene un DAC para generar una señal analógica a partir de los datos digitales.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221006175627.png)

LPF (Filtro de paso bajo) suaviza la forma de onda y elimina los componentes de alta frecuencia. Un conjunto de puntos de datos para una forma de onda dada se almacena en la memoria de origen de forma de onda, cada vez que ocurre un reloj, un punto de datos pasará al DAC.

Parámetros importantes del AWG:

- Salida máxima de voltaje pico a pico
- Resolución de forma de onda (resolución DAC)
- Ancho de banda
- Profundidad de memoria de origen de forma de onda
- Impedancia de salida
- Ruido, THD, SNR

### Digitalizador de forma de onda (WD)

El **Digitalizador de forma de onda (WD)** muestrea señales analógicas y las convierte en valores digitales. Realiza la operación opuesta al AWG. Convierte la señal analógica en muestras digitales que representan la señal analógica original.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221006180242.png)

El filtro de paso bajo limita el ancho de banda de la señal para eliminar componentes de frecuencia no deseados como el ruido y las espurias, también proporciona anti-aliasing atenuando las espurias que se aliasarían en la banda de paso del filtro durante la conversión ADC.

Parámetros importantes del WD:

- Rango máximo de voltaje de entrada de pico a pico
- Resolución de forma de onda (resolución ADC)
- Ancho de banda
- Profundidad de memoria de captura de forma de onda
- Impedancia de entrada
- Ruido, THD, SNR, espurias

### Reloj

Los relojes analógicos y digitales se derivan de un reloj de referencia de todo el sistema. Si no hay una señal de sincronización de reloj, el desfase de tiempo puede llevar a resultados incorrectos.

### Procesador de señal digital (DSP)

El **procesador de señal digital (DSP)** es un microprocesador especializado que realiza operaciones matemáticas en matrices de números digitales. Se realizan varios algoritmos como DFT y FFT en DSP para transformar la información del dominio del tiempo en el dominio de la frecuencia.

La arquitectura de un DSP está optimizada para permitir una multiplicación rápida, sumas, cálculos de logaritmos, cálculos de cuadrados y raíces cuadradas.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221007142019.png)

El probador llevará la señal capturada almacenada al procesador DSP a través de buses de datos.

## Referencias y agradecimientos

- _Fundamentos de pruebas utilizando ATE_
- _Los fundamentos de las pruebas de señal mixta_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
