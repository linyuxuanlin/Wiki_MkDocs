# Prueba de Fuga

La prueba de fuga incluye la prueba de fuga de entrada (IIL y IIH) y la prueba de fuga tristate de salida (IOZL y IOZH).

## Prueba de Fuga de Entrada (IIL & IIH)

La fuga de entrada ocurre en el circuito del buffer de un pin de entrada. IIH es la vía de fuga desde el pin de entrada a GND cuando el DUT se conduce a "1", e IIL es la vía de fuga desde VDD al pin de entrada cuando se conduce a "0":

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220911215421.png)

En realidad, la medición de IIL es la resistencia desde el pin de entrada a VDD, y IIH es la resistencia desde el pin de entrada a GND. La prueba de fuga de entrada tiene como objetivo garantizar que el buffer de entrada del pin no suministre ni absorba más corriente no deseada de la especificada.

### Método de Prueba (Serie)

La prueba de fuga de entrada en serie (IIL & IIH) se realiza aplicando un voltaje de VDDmax y forzando el pin de entrada específico a VDDmax (para IIH) o 0V (para IIL), mientras que los otros pines de entrada se fuerzan al lado opuesto del Pin bajo Prueba.

#### Prueba IIL (Serie)

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220911225521.png)

1. Aplicar VDDmax al pin de VDD (con una pinza de corriente).
2. Forzar VDDmax en todos los pines de entrada, excepto el Pin bajo Prueba.
3. Forzar 0V en el Pin bajo Prueba y medir el flujo de corriente saliente:
   - **Mayor que el valor especificado (> -10uA)**: APROBADO
   - **Menor que el valor especificado (< -10uA)**: FALLA
4. Repetir para probar el siguiente pin.

#### Prueba IIH (Serie)

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220912113044.png)

1. Aplicar VDDmax al pin de VDD (con una pinza de corriente).
2. Forzar 0V en todos los pines de entrada, excepto el Pin bajo Prueba.
3. Forzar VDDmax en el Pin bajo Prueba y medir el flujo de corriente entrante:
   - **Mayor que el valor especificado (> 10uA)**: FALLA
   - **Menor que el valor especificado (< 10uA)**: APROBADO
4. Repetir para probar el siguiente pin.

### Método de Prueba (Paralelo)

Dado que el método serial puede identificar la fuga entre los pines de entrada, pero es demasiado ineficiente. El método de prueba en paralelo es el más comúnmente utilizado en realidad. PPMU se utiliza en el método en paralelo, para llevar todos los pines de entrada a VDDmax (para IIH) o 0V (para IIL) y medir la corriente de cada pin de entrada.

La única desventaja del método en paralelo es que no se detectará la fuga de pin a pin, porque todos los pines se fuerzan al mismo nivel de voltaje al mismo tiempo.

## Prueba de Fuga de Tristate de Salida (IOZL e IOZH)

Tristate, también llamado estado High-Z o flotante, indica que parece ser una alta impedancia externamente al pin del DUT.

La fuga de tristate de salida ocurre cuando se aplica un nivel de voltaje ALTO o BAJO al pin de salida del DUT, mientras el pin se condiciona para estar deshabilitado. IOZL significa la corriente que fluye cuando se aplica el nivel BAJO, y IOZH significa la corriente que fluye cuando se aplica el nivel ALTO.

![](https://img.wiki-power.com/d/wiki-media/img/20220912120527.png)

Esencialmente, IOZL indica la resistencia desde un pin de salida a VDD cuando está deshabilitado, y IOZH indica la resistencia a GND. La prueba asegura que el pin no suministrará o absorberá más corriente no deseada de la especificada.

Además, se requiere una entrada de control (señal de habilitación) en esta prueba, para controlar el pin de salida específico al estado BAJO, ALTO o High-Z (deshabilitado).

### Método de Prueba (Serial)

#### Prueba IOZL (Serial)

![](https://img.wiki-power.com/d/wiki-media/img/20220912121730.png)

1. Aplicar VDDmax al pin de VDD (con una pinza de corriente).
2. Condicionar el pin de salida específico al estado Hi-Z (deshabilitado).
3. Forzar 0V al Pin bajo Prueba y medir la corriente que fluye hacia afuera:
   - **Mayor que el valor especificado (> -10uA)**: APROBADO
   - **Menor que el valor especificado (< -10uA)**: FALLA
4. Repetir para probar el siguiente pin.

#### Prueba IOZH (Serial)

```markdown
![](https://img.wiki-power.com/d/wiki-media/img/20220912122050.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Precocionar el pin de salida específico al estado de alta impedancia (desactivado).
3. Forzar VDDmax al Pin bajo Prueba y medir el flujo de corriente en:
   - **Mayor que el valor especificado (>10uA)**: FALLA
   - **Menor que el valor especificado (<10uA)**: APROBADO
4. Repetir para probar el siguiente pin.

### Método de Prueba (Paralelo)

El método paralelo es más comúnmente utilizado con PPMU, para llevar todos los pines de salida a VDDmax (para IOZH) o 0V (para IOZL) y medir la corriente de cada pin de salida.

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba con ATE_

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe ser reproducida con atribución.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.