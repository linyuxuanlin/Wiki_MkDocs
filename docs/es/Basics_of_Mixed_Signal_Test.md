# Fundamentos de Prueba de Señal Mixta

La señal mixta contiene tanto señales analógicas como digitales. Los dispositivos que procesan señales mixtas suelen incluir convertidores analógico-digitales (ADC), convertidores digitales-analógicos (DAC), interruptores y multiplexores analógicos, amplificadores de muestreo y retención, y así sucesivamente.

Como parte de esto, las señales analógicas son señales que utilizamos en el mundo real, como voz o temperatura; son continuas tanto en el tiempo como en la amplitud. Para procesar señales analógicas en computadoras, necesitamos convertirlas en señales digitales, ya que son discretas tanto en el tiempo como en la amplitud.

## Teoría del Muestreo

![](https://img.wiki-power.com/d/wiki-media/img/20220929094314.png)

La teoría del muestreo se aplica a la señal para que sea periódica, o se introducirán errores.

### Teorema de Nyquist

Utilizamos el **Teorema de Nyquist (奈奎斯特定理)** para obtener la frecuencia mínima de muestreo cuando se toman muestras de señales:

$$
F_s≥2F_i
$$

Debemos muestrear a una frecuencia mayor que el doble de la frecuencia más alta de interés para poder recrear una señal a partir de sus muestras y evitar la pérdida de información.

Si muestreamos a una frecuencia inferior a la tasa de Nyquist, se producirá un fenómeno llamado **aliasing (混叠)** (componentes no deseadas) cuando intentemos convertirlo nuevamente en una señal continua en el tiempo, y algunas de las frecuencias en la señal original pueden perderse.

Para minimizar el problema del aliasing, debemos eliminar las frecuencias mayores que $\frac{F_s}{2}$ de la señal a través de un filtro antialiasing (por ejemplo, un filtro pasa bajos):

![](https://img.wiki-power.com/d/wiki-media/img/20220930154335.png)

### Muestreo Coherente

Si un conjunto de muestras en el tiempo no contiene un número entero preciso de ciclos, se producirá **fuga espectral (频谱泄露)**.

**Muestreo coherente (相干采样)** es para asegurar la continuidad del muestreo y prevenir la fuga espectral, garantiza que un conjunto de muestras (una serie de muestras que representan la señal analógica) tenga una relación fija y bien definida entre la frecuencia de muestra $F_s$, el número de muestras $N$, la frecuencia de la señal de prueba $F_i$, y el número de periodos de señal de prueba muestreados $M$:

$$
\frac{M}{N}=\frac{F_i}{F_s}
$$

El tiempo total requerido para tomar todas las muestras se llama **Periodo de Prueba Unitario (UTP)** y requiere $M$ ciclos de la señal de prueba, que tiene una frecuencia de $F_i$.

Por ejemplo, si queremos calcular la $F_s$ de una sinusoide continua repetida, donde $F_i$ es 1 kHz, $M=3$ y $N=16`:

![](https://img.wiki-power.com/d/wiki-media/img/20220930164712.png)

Así que podemos concluir que $F_s=5.333 kHz`.

Consejos importantes sobre el muestreo coherente:

- Aumentar $M` y/o $N` aumentará tanto la precisión como el tiempo de prueba.
- $M` y $N` deben ser números enteros.
- $N` debe ser una potencia de 2 cuando se utiliza la Transformada Rápida de Fourier (FFT).
- Se recomienda que $M` y $N` sean primos entre sí (互质) para que cada muestra proporcione información única. Se describe a continuación.

Si $M` y $N` no son primos entre sí ($M=3`, $N=12`), las muestras se toman en la misma posición en cada ciclo, por lo que no hay nueva información:

![](https://img.wiki-power.com/d/wiki-media/img/20220930170300.png)

Si $M` y $N` son primos entre sí ($M=3`, $N=16`), entonces son primos entre sí y cada muestra es discreta, por lo que proporciona información única:

![](https://img.wiki-power.com/d/wiki-media/img/20220930170343.png)

## Algoritmos Comunes de Análisis de Frecuencia

```markdown
Para $N$ muestras de una señal en el dominio del tiempo, existen $N$ valores de la señal en el dominio de la frecuencia y $N/2$ valores del espectro de potencia en el dominio de la frecuencia. A continuación, se muestra un ejemplo típico de componentes espectrales:

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221002145846.png)

Existen varios parámetros para describir las componentes espectrales de la siguiente manera:

- Relación Señal a Ruido (SNR)（Relación Señal a Ruido）
- Distorsión Armónica Total (THD)（Distorsión Armónica Total）
- Relación Señal a Ruido y Distorsión (SINAD)（Relación Señal a Ruido y Distorsión）
- Distorsión de Intermodulación (IM)（Distorsión de Intermodulación）
- Rango Dinámico Libre de Espurias (SFDR)（Rango Dinámico Libre de Espurias）

### Relación Señal a Ruido (SNR)

La **Relación Señal a Ruido (SNR)** se deriva almacenando primero el valor del fundamental (potencia de la señal):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221002151235.png)

Luego, se elimina el componente de corriente continua (CC) y las armónicas (generalmente hasta la quinta):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221002151402.png)

A continuación, se suman todos los bins del espectro de potencia restante (la potencia del ruido) medida por el valor RMS (Root Mean Squared, la tensión analógica que es igual a una tensión de CC que contiene la misma cantidad de energía; para una onda sinusoidal, el valor RMS es 0.707 veces el valor pico):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221002151646.png)

En última instancia, podemos concluir que:

$$
{SNR}(dB)=10\log_{10}(\frac{{Fundamental}}{{Potencia\ de\ Ruido}})
$$

La SNR generalmente se expresa en decibelios (dB) y a menudo es un valor positivo (suponiendo que la Potencia Fundamental es mucho mayor que la Potencia de Ruido).

### Distorsión Armónica Total (THD)

La **Distorsión Armónica Total (THD)** se deriva manteniendo una suma acumulativa de la potencia armónica total (generalmente solo las primeras cinco armónicas, comenzando en la segunda armónica):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221002155148.png)

Y podemos concluir que:

```
```

```markdown
$$
\text{THD}(dB)=10\log_{10}\left(\frac{\text{Potencia Armónica}}{\text{Fundamental}}\right)
$$

THD es a menudo un valor negativo (asumiendo que la Potencia Fundamental es mucho mayor que la Potencia Armónica total).

### Relación Señal a Ruido y Distorsión (SINAD)

**Relación Señal a Ruido y Distorsión (SINAD)** es la misma metodología que se utiliza para calcular la SNR, pero ahora se añade la potencia de las armónicas y se anula solo el componente de corriente continua.

$$
\text{SINAD}=\frac{S}{N+D}
$$

Y podemos concluir que:

$$
\because \text{SNR}=\frac{S}{N}, \text{THD}=\frac{D}{S}
$$

$$
\therefore \text{SNR}^{-1}+\text{THD}=\frac{N}{S}+\frac{D}{S}=\frac{N+D}{S}=\text{SINAD}^{-1}
$$

$$
\therefore \text{SINAD}=(\text{SNR}^{-1}+\text{THD})^{-1}
$$

### Distorsión de Intermodulación (IM)

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221018162800.png)

La Distorsión de Intermodulación (IM) ocurre cuando dos o más señales se utilizan en un sistema no lineal. El espectro no solo contendrá las señales originales, sino que también contendrá la suma y la diferencia de las señales de entrada junto con sus armónicas.

### Rango Dinámico Libre de Espurias (SFRD)

**Rango Dinámico Libre de Espurias (SFRD)** se obtiene encontrando el elemento más alto después del fundamental (ignorando el componente de corriente continua):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221002161334.png)

Tenga en cuenta que el elemento más alto puede o no ser un armónico. Por lo tanto, podemos concluir que:

$$
\text{SFDR}(dB)=10\log_{10}\left(\frac{\text{Fundamental}}{\text{Siguiente más Alto}}\right)
$$

El Rango Dinámico Libre de Espurias es un valor positivo (asumiendo que la Potencia Fundamental es mucho mayor que la Potencia Espuria más alta).

## Arquitectura del Probador Genérico de Señal Mixta

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221006174550.png)

En el probador genérico de señal mixta, el Generador de Funciones Arbitrarias (fuente de CA) y el Analizador de Forma de Onda (digitalización de CA) están conectados al Dispositivo Bajo Prueba (DUT) a través de conexiones de relé a través de la placa de canal.
```
```

### Generador de Formas de Onda Arbitrarias (AWG)

**El Generador de Formas de Onda Arbitrarias (AWG)** es un generador de señales de baja distorsión. Contiene un DAC para generar una señal analógica a partir de datos digitales.

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221006175627.png)

El LPF (Filtro Paso Bajo) se utiliza para suavizar la forma de onda y eliminar componentes de alta frecuencia. Un conjunto de puntos de datos para una forma de onda dada se almacena en la memoria de origen de la forma de onda, y cada vez que ocurre un pulso, un punto de datos se envía al DAC.

Parámetros importantes de AWG:

- Salida de Voltaje Máximo Pico a Pico
- Resolución de la Forma de Onda (Resolución del DAC)
- Ancho de Banda
- Profundidad de Memoria de Origen de la Forma de Onda
- Impedancia de Salida
- Ruido, THD, SNR

### Digitalizador de Formas de Onda (WD)

**El Digitalizador de Formas de Onda (WD)** muestrea señales analógicas y las convierte en valores digitales. Realiza la operación opuesta a la del AWG. Convierte señales analógicas en muestras digitales que representan la señal analógica original.

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221006180242.png)

El filtro paso bajo limita el ancho de banda de la señal para eliminar componentes de frecuencia no deseados, como ruido y espurias, y proporciona un anti-aliasing al atenuar espurias que podrían ser aliasadas en la banda de paso del filtro durante la conversión del ADC.

Parámetros importantes de WD:

- Rango de Voltaje de Entrada Máximo Pico a Pico
- Resolución de la Forma de Onda (Resolución del ADC)
- Ancho de Banda
- Profundidad de Memoria de Captura de Forma de Onda
- Impedancia de Entrada
- Ruido, THD, SNR, espurias

### Reloj

Los relojes analógicos y digitales se derivan de un reloj de referencia en todo el sistema. Si no hay una señal de sincronización de reloj, el desfase de tiempo puede llevar a resultados incorrectos.

### Procesador de Señal Digital (DSP)

El **Procesador de Señal Digital (DSP)** es un microprocesador especializado que realiza operaciones matemáticas en matrices de números digitales. En un DSP se ejecutan diversos algoritmos como la Transformada Discreta de Fourier (DFT) y la Transformada Rápida de Fourier (FFT) para transformar información del dominio temporal al dominio de frecuencia.

La arquitectura de un DSP está optimizada para permitir multiplicaciones rápidas, sumas, cálculos de logaritmos, operaciones de cuadrado y cálculos de raíz cuadrada.

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20221007142019.png)

El probador llevará la señal capturada almacenada al procesador DSP a través de buses de datos.

## Referencias y Agradecimientos

- _Fundamentos de Pruebas con ATE_
- _Los Fundamentos de las Pruebas de Señal Mixta por Brian Lowe_

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.