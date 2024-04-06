# ADC - Parámetros Dinámicos

## Parámetros Dinámicos

Los parámetros dinámicos de un ADC principalmente incluyen:

- Relación Señal-Ruido (SNR)
- Distorsión Armónica Total (THD)
- Relación Señal-Ruido y Distorsión (SINAD)
- Error de Intermodulación (IM)

### Relación Señal-Ruido (SNR)

La **Relación Señal-Ruido (SNR)** de un ADC se define como la relación entre la Potencia de la Señal Medida RMS (excluyendo la Distorsión Armónica) y la Potencia del Ruido RMS:

$$
SNR (dB) = 20 log\left(\frac{V_{Señal(RMS)}}{V_{Ruido(RMS)}}\right)
$$

Dado que el SNR es una relación de potencia, el valor $20$ en la ecuación representa el cuadrado de la relación de voltaje.

![Imagen](https://media.wiki-power.com/img/20221009221450.png)

Aunque la Distorsión Armónica no se incluye en la medición del SNR, se incluyen el Ruido de Cuantización, el Ruido Térmico y otros ruidos residuales en el conversor.

### Distorsión Armónica Total (THD)

La **Distorsión Armónica Total (THD)** de un ADC se define como la relación entre el valor fundamental y todas las distorsiones armónicas:

$$
THD (dB) = 20 log\left(\frac{\sqrt{V^2_{2(RMS)}+V^2_{3(RMS)}+...+V^2_{n(RMS)}}}{V_{1(RMS)}}\right)
$$

![Imagen](https://media.wiki-power.com/img/20221009225800.png)

## Cómo Probar los Parámetros Dinámicos

### Configuración del Sistema de Pruebas

Configuración del sistema de pruebas para los parámetros dinámicos del ADC:

![Imagen](https://media.wiki-power.com/img/20221009230212.png)

La resolución del SRC de CA debe ser al menos de 2 a 4 bits mejor que la del Dispositivo Bajo Prueba (DUT).

### Concepto de las Pruebas

Un ADC tiene un mejor SNR teórico de:

$$
SNR = (6.02N + 1.76) dB
$$

Donde $N$ es el número de bits del ADC.

A continuación, se detalla el procedimiento para probar los parámetros dinámicos de un ADC DUT.

#### 1. Generar una señal de entrada continua con el equipo de prueba para que el ADC la convierta.

Es una práctica común asegurarse de que el reloj analógico/digital esté referenciado a un reloj maestro común, de manera que la relación de la frecuencia de las fuentes de reloj esté fija y sincronizada, lo que hace que los resultados de las pruebas sean altamente repetibles.

![Imagen](https://media.wiki-power.com/img/20221011122459.png)

#### 2. Recolecta un conjunto de muestras con el ADC de manera coherente

Para la Fuente de CA:

$$
\frac{Fs}{Fi}=\frac{Ns}{Ms}
$$

Donde $Fs$ es la tasa de muestreo de la Fuente de CA, $Fi$ es la frecuencia de la señal, $Ns$ es el número de muestras (no necesita ser un número múltiplo de 2), $Ms$ es el número de ciclos enteros (no necesita ser impar).

Para la Captura Digital:

$$
\frac{Fs(dut)}{Fi}=\frac{Ncap}{Mc}
$$

Donde $Fs(dut)$ es la tasa de muestreo del ADC y también la tasa de muestreo de la Captura Digital, $Fi$ es la frecuencia de la señal, $Ncap$ es el número de muestras capturadas (número múltiplo de 2), $Mc$ es el número de ciclos enteros (impar).

#### 3. Envía el conjunto de muestras de tiempo recopiladas al DSP para realizar un análisis DFT / FFT

![Imagen](https://media.wiki-power.com/img/20221011140834.png)

?

![Imagen](https://media.wiki-power.com/img/20221011140904.png)

#### 4. Analiza los bins de frecuencia de interés utilizando ecuaciones o algoritmos de prueba para SNR, THD y compáralos con las especificaciones.

#### 5. Toma una decisión de aprobación o falla basada en los resultados.

## Referencias y Agradecimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _Los Fundamentos de las Pruebas de Señal Mixta de Brian Lowe_

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por un acuerdo de [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe reproducirse con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
