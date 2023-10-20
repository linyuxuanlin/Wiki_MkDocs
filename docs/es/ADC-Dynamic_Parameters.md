# ADC - Parámetros Dinámicos

## Parámetros Dinámicos

Los parámetros dinámicos de ADC principalmente incluyen:

- Relación Señal-Ruido (SNR)
- Distorsión Armónica Total (THD)
- Relación Señal-Ruido y Distorsión (SINAD)
- Error de Intermodulación (IM)

### Relación Señal-Ruido (SNR)

La **Relación Señal-Ruido (SNR)** de un ADC se define como la relación entre la Potencia de la Señal Medida RMS (excluyendo la Distorsión Armónica) y la Potencia del Ruido RMS:

$$
SNR(dB)=20log(\frac{V_{Señal(RMS)}}{V_{Ruido(RMS)}})
$$

Dado que el SNR es una relación de potencia, el valor $20$ en la ecuación representa el cuadrado de la relación de voltaje.

![](https://img.wiki-power.com/d/wiki-media/img/20221009221450.png)

Aunque la Distorsión Armónica no se incluye en la medición del SNR, se incluyen el Ruido de Cuantización, Térmico y otros ruidos residuales en el convertidor.

### Distorsión Armónica Total (THD)

La **Distorsión Armónica Total (THD)** de un ADC se define como la relación entre el valor fundamental y todas las distorsiones armónicas:

$$
THD(dB)=20log(\frac{\sqrt{V^2_{2(RMS)}+V^2_{3(RMS)}+...+V^2_{n(RMS)}}}{V_{1(RMS)}})
$$

![](https://img.wiki-power.com/d/wiki-media/img/20221009225800.png)

## Cómo Probar los Parámetros Dinámicos

### Configuración del Sistema de Prueba

La configuración del sistema de prueba para las pruebas de parámetros dinámicos de ADC es la siguiente:

![](https://img.wiki-power.com/d/wiki-media/img/20221009230212.png)

La resolución del SRC de CA debe ser al menos 2 a 4 bits mejor que el DUT.

### Concepto de Pruebas

El ADC tiene un SNR teórico máximo de:

$$
SNR = (6.02N + 1.76) dB
$$

Donde $N$ es el número de bits del ADC.

A continuación se muestra el procedimiento para probar los parámetros dinámicos de un ADC DUT.

#### 1. Generar una señal de entrada continua con el probador para que el ADC la convierta

Es práctica común asegurarse de que el reloj analógico/digital esté referenciado a un reloj maestro común, de modo que la relación de la frecuencia de las fuentes de reloj sea fija y sincronizada, lo que hace que los resultados de las pruebas sean altamente repetibles.

![](https://img.wiki-power.com/d/wiki-media/img/20221011122459.png)

#### 2. Recopilar un conjunto de muestras con el ADC de manera coherente

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

#### 3. Enviar el conjunto de muestras de tiempo recopiladas al DSP para realizar el análisis de DFT / FFT

![](https://img.wiki-power.com/d/wiki-media/img/20221011140834.png)

?

![](https://img.wiki-power.com/d/wiki-media/img/20221011140904.png)

#### 4. Analizar los bins de frecuencia de interés utilizando ecuaciones o algoritmos de prueba para SNR, THD y comparar con las especificaciones

#### 5. Tomar una decisión de aprobado / reprobado basada en los resultados

## Referencias y Agradecimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.es), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.