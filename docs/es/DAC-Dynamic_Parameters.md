# DAC - Parámetros Dinámicos

## Parámetros Dinámicos

Los parámetros dinámicos del DAC (Convertidor Analógico-Digital) principalmente incluyen:

- Relación Señal-Ruido (SNR)
- Distorsión Armónica Total (THD)
- Relación Señal-Ruido y Distorsión (SINAD)
- Error de Intermodulación (IM)

### Relación Señal-Ruido (SNR)

La **Relación Señal-Ruido (SNR)** de un DAC se define como la relación entre la Potencia de Señal Medida RMS (excluyendo la Distorsión Armónica) y la Potencia de Ruido RMS:

$$
SNR (dB) = 20log\left(\frac{V_{Señal(RMS)}}{V_{Ruido(RMS)}}\right)
$$

Dado que el SNR es una relación de potencia, el valor de $20$ en la ecuación representa el cuadrado de la relación de voltaje.

![Imagen](https://media.wiki-power.com/img/20221009221450.png)

Aunque la Distorsión Armónica no se incluye en la medición del SNR, se incluyen el ruido de cuantización, térmico y otros ruidos residuales en el convertidor.

### Distorsión Armónica Total (THD)

La **Distorsión Armónica Total (THD)** de un DAC se define como la relación entre la componente fundamental y todas las distorsiones armónicas:

$$
THD (dB) = 20log\left(\frac{\sqrt{V^2_{2(RMS)}+V^2_{3(RMS)}+...+V^2_{n(RMS)}}}{V_{1(RMS)}}\right)
$$

![Imagen](https://media.wiki-power.com/img/20221009225800.png)

## Cómo Probar los Parámetros Dinámicos

### Configuración del Sistema de Pruebas

Configuración del sistema de pruebas para las pruebas de parámetros dinámicos del DAC:

![Imagen](https://media.wiki-power.com/img/20221009230212.png)

La resolución del Digitalizador AC debe ser al menos de 2 a 4 bits mejor que el Dispositivo Bajo Prueba (DUT).

### Concepto de las Pruebas

El procedimiento para probar los parámetros dinámicos de un DAC se enumera a continuación.

#### 1. Generar una señal de datos digitales de entrada continua (una onda senoidal) con el probador para que el DAC la convierta.

Es práctica común asegurarse de que los relojes analógicos/digitales estén referenciados a un reloj maestro común, de manera que la relación de la frecuencia de las fuentes de reloj esté fija y sincronizada, lo que hace que los resultados de las pruebas sean altamente repetibles.

![](https://media.wiki-power.com/img/20221011195204.png)

#### 2. Recolectar coherentemente un conjunto de muestras con el DAC

Para la Fuente Digital:

$$
\frac{Fs(dut)}{Fi}=\frac{N}{M}
$$

Donde $Fs(dut)$ es la tasa de muestreo de la Fuente Digital, $Fi$ es la frecuencia de la señal, $N$ es el número de muestras, $M$ es el número de ciclos enteros.

Para la Captura Digital AC:

$$
\frac{Fs}{Fi}=\frac{Ncap}{Mc}
$$

Donde $Fs$ es la tasa de muestreo del DAC y también la tasa de muestreo de la Captura Digital, $Fi$ es la frecuencia de la señal, $Ncap$ es el número de muestras capturadas (el doble del número), $Mc$ es el número de ciclos enteros (impar).

#### 3. Enviar el conjunto de muestras de tiempo recopiladas al DSP para realizar análisis de DFT/FFT

![](https://media.wiki-power.com/img/20221011140834.png)

![](https://media.wiki-power.com/img/20221011140904.png)

#### 4. Analizar las bandas de frecuencia de interés utilizando ecuaciones o algoritmos de prueba para SNR (Relación Señal-Ruido), THD (Distorsión Armónica Total) y comparar con las especificaciones.

#### 5. Tomar una decisión de aprobación o rechazo basada en los resultados.

## Referencias y Agradecimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo de [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
