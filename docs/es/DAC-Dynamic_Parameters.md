# DAC - Parámetros Dinámicos

> Esta publicación solo está disponible en inglés.

## Parámetros Dinámicos

Los parámetros dinámicos de DAC contienen principalmente:

- Relación Señal-Ruido (SNR)
- Distorsión Armónica Total (THD)
- Relación Señal-Ruido y Distorsión (SINAD)
- Error de Intermodulación (IM)

### Relación Señal-Ruido (SNR)

La **Relación Señal-Ruido (SNR)** de un DAC se define como la relación de la Potencia de Señal Medida RMS (excluyendo la Distorsión Armónica) a la Potencia de Ruido RMS:

$$
SNR(dB)=20log(\frac{V_{Señal(RMS)}}{V_{Ruido(RMS)}})
$$

Dado que SNR es una relación de potencia, el $20$ en la ecuación significa el cuadrado de la relación de voltaje.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009221450.png)

Aunque la Distorsión Armónica no se incluye en la medición de SNR, se incluyen la Cuantización, el Ruido Térmico y otros ruidos residuales en el convertidor.

### Distorsión Armónica Total (THD)

La **Distorsión Armónica Total (THD)** de un DAC se define como la relación del fundamental a toda la distorsión armónica:

$$
THD(dB)=20log(\frac{\sqrt{V^2_{2(RMS)}+V^2_{3(RMS)}+...+V^2_{n(RMS)}}}{V_{1(RMS)}}
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009225800.png)

## Cómo Probar los Parámetros Dinámicos

### Configuración del Sistema de Prueba

Configuración del sistema de prueba para las pruebas de parámetros dinámicos de ADC:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221009230212.png)

La resolución del Digitalizador de CA debe ser al menos 2 a 4 bits mejor que el DUT.

### Concepto de Pruebas

El procedimiento para probar los parámetros dinámicos de un DAC se describe a continuación.

#### 1.Crear una señal de datos digitales de entrada continua (de una onda sinusoidal) con el probador para que el DAC la convierta.

Es una práctica común asegurarse de que el reloj analógico/digital esté referenciado a un reloj maestro común, de modo que la relación de la frecuencia de las fuentes de reloj esté fija y sincronizada, lo que hace que los resultados de las pruebas sean altamente repetibles.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011195204.png)

#### 2. Colectar coherentemente un conjunto de muestras con el DAC

Para la fuente digital:

$$
\frac{Fs(dut)}{Fi}=\frac{N}{M}
$$

Donde $Fs(dut)$ es la tasa de muestreo de la fuente digital, $Fi$ es la frecuencia de la señal, $N$ es el número de muestras, $M$ es el número de ciclos enteros.

Para la captura digital de CA:

$$
\frac{Fs}{Fi}=\frac{Ncap}{Mc}
$$

Donde $Fs$ es la tasa de muestreo del DAC y también la tasa de muestreo de la captura digital, $Fi$ es la frecuencia de la señal, $Ncap$ es el número de muestras capturadas (2x número), $Mc$ es el número de ciclos enteros (impar).

#### 3. Enviar el conjunto de muestras de tiempo recopiladas al DSP para realizar análisis DFT / FFT

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011140834.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011140904.png)

#### 4. Analizar los bins de frecuencia de interés utilizando ecuaciones o algoritmos de prueba para SNR, THD y comparar con la especificación

#### 5. Tomar una decisión de aprobación / rechazo basada en los resultados

## Referencias y agradecimientos

- _Fundamentos de pruebas utilizando ATE_
- _Los fundamentos de las pruebas de señal mixta_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
