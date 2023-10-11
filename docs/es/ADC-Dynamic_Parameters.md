# ADC - Parámetros Dinámicos

> Esta publicación solo está disponible en inglés.

## Parámetros Dinámicos

Los parámetros dinámicos de ADC contienen principalmente:

- Relación señal-ruido (SNR)
- Distorsión armónica total (THD)
- Relación señal-ruido y distorsión (SINAD)
- Error de intermodulación (IM)

### Relación señal-ruido (SNR)

La **relación señal-ruido (SNR)** de un ADC se define como la relación entre la potencia de la señal medida RMS (excluyendo la distorsión armónica) y la potencia de ruido RMS:

$$
SNR(dB)=20log(\frac{V_{Señal(RMS)}}{V_{Ruido(RMS)}})
$$

Dado que SNR es una relación de potencia, el $20$ en la ecuación significa el cuadrado de la relación de voltaje.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009221450.png)

Aunque la distorsión armónica no se incluye en la medición de SNR, se incluyen el ruido de cuantificación, térmico y otros residuales en el convertidor.

### Distorsión armónica total (THD)

La **distorsión armónica total (THD)** de un ADC se define como la relación entre el fundamental y toda la distorsión armónica:

$$
THD(dB)=20log(\frac{\sqrt{V^2_{2(RMS)}+V^2_{3(RMS)}+...+V^2_{n(RMS)}}}{V_{1(RMS)}})
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009225800.png)

## Cómo probar los parámetros dinámicos

### Configuración del sistema de prueba

La configuración del sistema de prueba para las pruebas de parámetros dinámicos de ADC es:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009230212.png)

La resolución de AC SRC debe ser al menos 2 a 4 bits mejor que DUT.

### Concepto de pruebas

ADC tiene un mejor SNR teórico de:

$$
SNR = (6.02N + 1.76) dB
$$

Donde $N$ es el número de bits del ADC.

El procedimiento para probar los parámetros dinámicos de un ADC DUT se enumera a continuación.

#### 1. Hacer una señal de entrada continua con el probador para que el ADC convierta.

Es una práctica común asegurarse de que el reloj analógico/digital esté referenciado a un reloj maestro común, de modo que la relación de la frecuencia de las fuentes de reloj sea fija y sincronizada, lo que hace que los resultados de las pruebas sean altamente repetibles.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011122459.png)

#### 2. Recopilar un conjunto de muestras con el ADC coherentemente

Para la fuente de CA:

$$
\frac{Fs}{Fi}=\frac{Ns}{Ms}
$$

Donde $Fs$ es la tasa de muestreo de la fuente de CA, $Fi$ es la frecuencia de la señal, $Ns$ es el número de muestras (no tiene que ser un número 2x), $Ms$ es el número de ciclos enteros (no tiene que ser impar).

Para la captura digital:

$$
\frac{Fs(dut)}{Fi}=\frac{Ncap}{Mc}
$$

Donde $Fs(dut)$ es la tasa de muestreo del ADC, también la tasa de muestreo de la captura digital, $Fi$ es la frecuencia de la señal, $Ncap$ es el número de muestras capturadas (número 2x), $Mc$ es el número de ciclos enteros (impar).

#### 3. Enviar el conjunto de muestras de tiempo recopiladas al DSP para realizar el análisis DFT/FFT

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011140834.png)

?

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011140904.png)

#### 4. Analizar los intervalos de frecuencia de interés utilizando ecuaciones o algoritmos de prueba para SNR, THD y comparar con la especificación

#### 5. Tomar una decisión de aprobado / rechazo basada en los resultados

## Referencias y agradecimientos

- _Fundamentos de prueba utilizando ATE_
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
