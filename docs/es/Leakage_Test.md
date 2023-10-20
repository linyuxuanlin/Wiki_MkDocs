# Prueba de Fuga

La prueba de fuga consta de la prueba de fuga de entrada (IIL y IIH) y la prueba de fuga de tristate de salida (IOZL y IOZH).

## Prueba de Fuga de Entrada (IIL & IIH)

La fuga de entrada ocurre en el circuito de búfer de un pin de entrada. IIH es la vía de fuga desde el pin de entrada a GND cuando el DUT se lleva a "1", y IIL es la vía de fuga desde VDD al pin de entrada cuando se lleva a "0":

![](https://img.wiki-power.com/d/wiki-media/img/20220911215421.png)

En realidad, la medición de IIL es la resistencia desde el pin de entrada a VDD, y IIH es la resistencia desde el pin de entrada a GND. La prueba de fuga de entrada tiene como objetivo garantizar que el búfer de entrada del pin no genere o absorba más corriente no deseada de la especificada.

### Método de Prueba (Serial)

La prueba de fuga de entrada en serie (IIL & IIH) se realiza aplicando un voltaje de VDDmax y forzando el pin de entrada específico a VDDmax (para IIH) o 0V (para IIL), mientras que los otros pines de entrada se fuerzan al lado opuesto del Pin bajo Prueba.

#### Prueba IIL (Serial)

![](https://img.wiki-power.com/d/wiki-media/img/20220911225521.png)

1. Aplicar VDDmax al pin de VDD (con abrazadera de corriente).
2. Forzar VDDmax en todos los pines de entrada excepto el Pin bajo Prueba.
3. Forzar 0V en el Pin bajo Prueba y medir el flujo de corriente:
   - **Mayor que el valor especificado (> -10uA)**: APROBADO
   - **Menor que el valor especificado (< -10uA)**: FALLA
4. Repetir para probar el siguiente pin.

#### Prueba IIH (Serial)

![](https://img.wiki-power.com/d/wiki-media/img/20220912113044.png)

1. Aplicar VDDmax al pin de VDD (con abrazadera de corriente).
2. Forzar 0V en todos los pines de entrada excepto el Pin bajo Prueba.
3. Forzar VDDmax en el Pin bajo Prueba y medir el flujo de corriente hacia adentro:
   - **Mayor que el valor especificado (> 10uA)**: FALLA
   - **Menor que el valor especificado (< 10uA)**: APROBADO
4. Repetir para probar el siguiente pin.

### Método de Prueba (Paralelo)

Dado que el método serial puede identificar la fuga entre pines de entrada, pero es demasiado ineficiente. El método de prueba en paralelo es el más comúnmente utilizado en realidad. El PPMU se utiliza en el método en paralelo para llevar todos los pines de entrada a VDDmax (para IIH) o 0V (para IIL) y medir la corriente de cada pin de entrada.

La única desventaja del método en paralelo es que no se detectará la fuga de pin a pin, porque todos los pines se fuerzan al mismo nivel de voltaje al mismo tiempo.

## Prueba de Fuga en Tres Estados de Salida (IOZL e IOZH)

Tres estados, también conocidos como Alta Impedancia o estado flotante, indican que aparentemente hay una alta impedancia externamente en el pin del DUT.

La fuga en tres estados de salida ocurre cuando se aplica un nivel de voltaje ALTO o BAJO al pin de salida del DUT, mientras el pin está preacondicionado para estar deshabilitado. IOZL significa la corriente que fluye cuando se aplica el nivel BAJO, e IOZH significa la corriente que fluye cuando se aplica el nivel ALTO.

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220912120527.png)

Básicamente, IOZL indica la resistencia desde un pin de salida a VDD cuando está deshabilitado, e IOZH indica la resistencia a GND. La prueba asegura que el pin no suministrará o consumirá más corriente no deseada de la especificada.

Además, se requiere una entrada de control (señal de habilitación) en esta prueba, para controlar el pin de salida específico a un estado BAJO, ALTO o Alto-Z (deshabilitado).

### Método de Prueba (Serial)

#### Prueba IOZL (Serial)

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220912121730.png)

1. Aplicar VDDmax al pin de VDD (con abrazadera de corriente).
2. Preacondicionar el pin de salida específico a un estado de Alta Impedancia (deshabilitado).
3. Forzar 0V al Pin bajo Prueba y medir la corriente que fluye hacia afuera:
   - **Mayor que el valor especificado (> -10uA)**: APROBADO
   - **Menor que el valor especificado (< -10uA)**: FALLIDO
4. Repetir para probar el siguiente pin.

#### Prueba IOZH (Serial)

```markdown
![](https://img.wiki-power.com/d/wiki-media/img/20220912122050.png)

1. Aplicar VDDmax al pin VDD (con abrazadera de corriente).
2. Precargar el pin de salida específico al estado Hi-Z (deshabilitar).
3. Forzar VDDmax al Pin bajo prueba y medir el flujo de corriente en:
   - **Más alto que el valor especificado (>10uA)**: FALLA
   - **Más bajo que el valor especificado (<10uA)**: APROBADO
4. Repetir para probar el siguiente pin.

### Método de Prueba (Paralelo)

El método paralelo es más comúnmente utilizado en realidad con PPMU, para llevar todos los pines de salida a VDDmax (para IOZH) o 0V (para IOZL) y medir la corriente de cada pin de salida.

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de Pruebas Utilizando ATE_

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.