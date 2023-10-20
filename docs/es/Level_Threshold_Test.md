```markdown
# Prueba de umbral de nivel 🚧

![](https://img.wiki-power.com/d/wiki-media/img/20220912163403.png)

La prueba de umbral de nivel incluye el Umbral de Nivel de Salida (VOL y VOH) y el Umbral de Nivel de Entrada (VIL y VIH). Se originan a partir de los umbrales de nivel típicos de TTL y CMOS:

|              | VCC   | VOL             | VOH             | VIL             | VIH             | GND   |
| :----------- | :---- | :-------------- | :-------------- | :-------------- | :-------------- | :---- |
| TTL (5V)     | 5.00V | 0.40V           | 2.40V           | 0.80V           | 2.00V           | 0.00V |
| LVTTL (3.3V) | 3.30V | 0.40V           | 2.40V           | 0.80V           | 1.50V           | 0.00V |
| CMOS (5V)    | 5.00V | 0.50V (0.1 VCC) | 4.50V (0.9 VCC) | 1.50V (0.3 VCC) | 3.50V (0.7 VCC) | 0.00V |
| CMOS (3.3V)  | 3.30V | 0.33V (0.1 VCC) | 2.97V (0.9 VCC) | 0.99V (0.3 VCC) | 2.31V (0.7 VCC) | 0.00V |
| CMOS (2.5V)  | 2.50V | 0.40V           | 2.00V           | 0.70V           | 1.70V           | 0.00V |
| CMOS (1.8V)  | 1.80V | 0.45V           | 1.35V           | 0.63V           | 1.170V          | 0.00V |

## Prueba de Umbral de Nivel de Salida (VOL/IOL y VOH/IOH)

VOL representa el voltaje de salida máximo cuando el nivel de voltaje de salida es BAJO, IOL representa la máxima capacidad de corriente de **saturación** en el estado de salida BAJO. En realidad, miden la resistencia del pin de salida cuando se proporciona la lógica `0`, asegurando que pueda suministrar una corriente de IOL sin exceder el voltaje de VOL, examinando la capacidad de saturación de corriente y manteniendo un estado lógico correcto.
```

```markdown
VOH representa el voltaje de salida mínimo cuando el nivel de voltaje de salida es ALTO, IOH representa la máxima capacidad de corriente de fuente en el estado de salida ALTO. En realidad, miden la resistencia del pin de salida al proporcionar la lógica `1`, asegurando que pueda proporcionar una corriente de IOH sin caer por debajo del voltaje de VOH, examinando la capacidad de corriente de fuente y manteniendo un estado lógico correcto.

### Método de Prueba (Serie)

#### Prueba VOL/IOL (Serie)

![](https://img.wiki-power.com/d/wiki-media/img/20220912172403.png)

1. Aplicar VDDmin al pin VDD (con abrazadera de corriente).
2. Preacondicionar el pin de salida específico a la lógica '0'.
3. Forzar IOLmax al Pin bajo Prueba (fluir hacia el DUT) y medir el voltaje en él:
   - **Mayor que el valor especificado (>0.4V)**: FALLA
   - **Menor que el valor especificado (<0.4V)**: APROBADO
4. Repetir la prueba con diferentes pines de salida.

#### Prueba VOH/IOH (Serie)

![](https://img.wiki-power.com/d/wiki-media/img/20220912172445.png)

1. Aplicar VDDmin al pin VDD (con abrazadera de corriente).
2. Preacondicionar el pin de salida específico a la lógica '1'.
3. Forzar IOHmax al Pin bajo Prueba (fluir desde el DUT) y medir el voltaje en él:
   - **Mayor que el valor especificado (>2.4V)**: APROBADO
   - **Menor que el valor especificado (<2.4V)**: FALLA
4. Repetir la prueba con diferentes pines de salida.

## Prueba del Umbral de Nivel de Entrada (VIL y VIH)

## Referencias y Reconocimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.