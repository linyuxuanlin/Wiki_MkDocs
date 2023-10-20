# DAC - Parámetros Dinámicos

## Parámetros Dinámicos

Los parámetros dinámicos del DAC principalmente incluyen:

- Relación Señal-Ruido (SNR)
- Distorsión Armónica Total (THD)
- Relación Señal-Ruido y Distorsión (SINAD)
- Error de Intermodulación (IM)

### Relación Señal-Ruido (SNR)

La **Relación Señal-Ruido (SNR)** de un DAC se define como la relación entre la Potencia de Señal Medida RMS (excluyendo la Distorsión Armónica) y la Potencia de Ruido RMS:

$$
SNR(dB) = 20log(\frac{V_{Señal(RMS)}}{V_{Ruido(RMS)})
$$

Dado que el SNR es una relación de potencia, el valor de $20$ en la ecuación representa el cuadrado de la relación de voltaje.

![](https://img.wiki-power.com/d/wiki-media/img/20221009221450.png)

Aunque la Distorsión Armónica no se incluye en la medición del SNR, se incluyen el ruido de cuantificación, térmico y otros ruidos residuales en el convertidor.

### Distorsión Armónica Total (THD)

La **Distorsión Armónica Total (THD)** de un DAC se define como la relación entre la componente fundamental y todas las distorsiones armónicas:

$$
THD(dB) = 20log(\frac{\sqrt{V^2_{2(RMS)}+V^2_{3(RMS)}+...+V^2_{n(RMS)}}}{V_{1(RMS)}}
$$

![](https://img.wiki-power.com/d/wiki-media/img/20221009225800.png)

## Cómo Probar los Parámetros Dinámicos

### Configuración del Sistema de Prueba

Configuración del sistema de prueba para las pruebas de parámetros dinámicos de un DAC:

![](https://img.wiki-power.com/d/wiki-media/img/20221009230212.png)

La resolución del Digitalizador de CA debe ser al menos 2 a 4 bits mejor que el Dispositivo bajo Prueba.

### Concepto de las Pruebas

El procedimiento para probar los parámetros dinámicos de un DAC se enumera a continuación.

#### 1. Generar una señal digital de entrada continua (de una onda senoidal) con el probador para que el DAC la convierta

Es una práctica común asegurarse de que el reloj analógico/digital esté referenciado a un reloj maestro común, de modo que la relación de la frecuencia de las fuentes de reloj esté fija y sincronizada, lo que hace que los resultados de las pruebas sean altamente repetibles.

![](https://img.wiki-power.com/d/wiki-media/img/20221011195204.png)

#### 2. Recopile de manera coherente un conjunto de muestras con el DAC

Para la fuente digital:

$$
\frac{Fs(dut)}{Fi}=\frac{N}{M}
$$

Donde $Fs(dut)$ es la velocidad de muestreo de la fuente digital, $Fi$ es la frecuencia de la señal, $N$ es el número de muestras y $M$ es el número de ciclos enteros.

Para la Captura Digital AC:

$$
\frac{Fs}{Fi}=\frac{Ncap}{Mc}
$$

Donde $Fs$ es la velocidad de muestreo del DAC, que también es la velocidad de muestreo de la Captura Digital, $Fi$ es la frecuencia de la señal, $Ncap$ es el número de muestras capturadas (2 veces el número) y $Mc$ es el número de ciclos enteros (impares).

#### 3. Envíe el conjunto de muestras de tiempo recopiladas al DSP para realizar el análisis DFT/FFT

![](https://img.wiki-power.com/d/wiki-media/img/20221011140834.png)

![](https://img.wiki-power.com/d/wiki-media/img/20221011140904.png)

#### 4. Analice los bins de frecuencia de interés utilizando ecuaciones o algoritmos de prueba para SNR, THD y compárelos con las especificaciones.

#### 5. Tome una decisión de aprobación o rechazo basada en los resultados.

## Referencias y Agradecimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _Los Fundamentos de las Pruebas de Señal Mixta de Brian Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe reproducirse con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.