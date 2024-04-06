# Prueba de Umbral de Nivel 🚧

![Imagen](https://media.wiki-power.com/img/20220912163403.png)

La prueba de umbral de nivel incluye el Umbral de Nivel de Salida (VOL y VOH) y el Umbral de Nivel de Entrada (VIL y VIH). Se originan a partir de los umbrales de nivel típicos de TTL y CMOS:

|              | VCC   | VOL             | VOH             | VIL             | VIH             | GND   |
| :----------- | :---- | :-------------- | :-------------- | :-------------- | :-------------- | :---- |
| TTL (5V)     | 5.00V | 0.40V           | 2.40V           | 0.80V           | 2.00V           | 0.00V |
| LVTTL (3.3V) | 3.30V | 0.40V           | 2.40V           | 0.80V           | 1.50V           | 0.00V |
| CMOS (5V)    | 5.00V | 0.50V (0.1 VCC) | 4.50V (0.9 VCC) | 1.50V (0.3 VCC) | 3.50V (0.7 VCC) | 0.00V |
| CMOS (3.3V)  | 3.30V | 0.33V (0.1 VCC) | 2.97V (0.9 VCC) | 0.99V (0.3 VCC) | 2.31V (0.7 VCC) | 0.00V |
| CMOS (2.5V)  | 2.50V | 0.40V           | 2.00V           | 0.70V           | 1.70V           | 0.00V |
| CMOS (1.8V)  | 1.80V | 0.45V           | 1.35V           | 0.63V           | 1.170V          | 0.00V |

## Prueba de Umbral de Nivel de Salida (VOL/IOL & VOH/IOH)

VOL representa el voltaje de salida máximo cuando el nivel de voltaje de salida es BAJO, mientras que IOL representa la capacidad máxima de corriente de hundimiento en el estado de salida BAJO. En realidad, miden la resistencia del pin de salida cuando se proporciona la lógica `0`, asegurando que pueda proporcionar corriente de IOL sin exceder el voltaje de VOL, examinando la capacidad de hundir corriente y mantenerse en un estado lógico correcto.

VOH representa el voltaje de salida mínimo cuando el nivel de voltaje de salida es ALTO, y IOH representa la capacidad máxima de corriente de fuente en el estado de salida ALTO. Estas medidas en realidad evalúan la resistencia del pin de salida cuando proporciona la lógica `1`, asegurando que pueda suministrar una corriente de IOH sin que el voltaje sea inferior a VOH, lo que examina la capacidad de corriente de fuente y mantiene un estado lógico correcto.

### Método de Prueba (Serie)

#### Prueba VOL/IOL (Serie)

![Imagen](https://media.wiki-power.com/img/20220912172403.png)

1. Aplicar VDDmin al pin VDD (con una pinza de corriente).
2. Precondicionar el pin de salida específico a la lógica '0'.
3. Forzar IOLmax en el Pin bajo Prueba (fluir hacia el DUT) y medir el voltaje en él:
   - **Superior al valor especificado (>0.4V)**: FALLA
   - **Inferior al valor especificado (<0.4V)**: APROBADO
4. Repetir la prueba con diferentes pines de salida.

#### Prueba VOH/IOH (Serie)

![Imagen](https://media.wiki-power.com/img/20220912172445.png)

1. Aplicar VDDmin al pin VDD (con una pinza de corriente).
2. Precondicionar el pin de salida específico a la lógica '1'.
3. Forzar IOHmax en el Pin bajo Prueba (fluir desde el DUT) y medir el voltaje en él:
   - **Superior al valor especificado (>2.4V)**: APROBADO
   - **Inferior al valor especificado (<2.4V)**: FALLA
4. Repetir la prueba con diferentes pines de salida.

## Prueba del Umbral del Nivel de Entrada (VIL & VIH)

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
