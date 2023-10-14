# Prueba de Fuga

> Esta publicación solo está disponible en inglés.

La prueba de fuga contiene la prueba de fuga de entrada (IIL y IIH) y la prueba de fuga de tristado de salida (IOZL y IOZH).

## Prueba de Fuga de Entrada (IIL y IIH)

La fuga de entrada ocurre en el circuito de búfer de un pin de entrada. IIH es la ruta de fuga desde el pin de entrada a GND cuando el DUT se impulsa a "1", e IIL es la ruta de fuga desde VDD al pin de entrada cuando se impulsa a "0":

![](https://img.wiki-power.com/d/wiki-media/img/20220911215421.png)

En realidad, la medición de IIL es la resistencia desde el pin de entrada a VDD, e IIH es la resistencia desde el pin de entrada a GND. La prueba de fuga de entrada es para garantizar que el búfer de entrada del pin no suministre o absorba más corriente no deseada de lo especificado.

### Método de Prueba (Serie)

La prueba de fuga de entrada en serie (IIL y IIH) se realiza aplicando un voltaje de VDDmax y forzando el pin de entrada específico a VDDmax (para IIH) o 0V (para IIL), mientras que otros pines de entrada se fuerzan al lado opuesto del Pin bajo prueba.

#### Prueba de IIL (Serie)

![](https://img.wiki-power.com/d/wiki-media/img/20220911225521.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Forzar VDDmax a todos los pines de entrada excepto el Pin bajo prueba.
3. Forzar 0V al Pin bajo prueba y medir el flujo de corriente:
   - **Mayor que el valor especificado (> -10uA)**: APROBADO
   - **Menor que el valor especificado (<-10uA)**: FALLIDO
4. Repetir para probar el siguiente pin.

#### Prueba de IIH (Serie)

![](https://img.wiki-power.com/d/wiki-media/img/20220912113044.png)

## Prueba de Fuga de Corriente de Entrada (IIH & IIL)

La fuga de corriente de entrada se refiere a la corriente que fluye en los pines de entrada del DUT cuando se aplica un voltaje de entrada específico. IIH significa la corriente que fluye en el pin de entrada cuando se aplica un voltaje alto, mientras que IIL significa la corriente que fluye en el pin de entrada cuando se aplica un voltaje bajo.

Para realizar esta prueba, se siguen los siguientes pasos:

1. Aplicar VDDmax al pin VDD (con pinza amperimétrica).
2. Forzar 0V a todos los pines de entrada excepto el Pin bajo prueba.
3. Forzar VDDmax al Pin bajo prueba y medir el flujo de corriente en:
   - **Valor superior al especificado (>10uA)**: FALLA
   - **Valor inferior al especificado (<10uA)**: APROBADO
4. Repetir para probar el siguiente pin.

### Método de Prueba (Paralelo)

Aunque el método serial puede identificar la fuga entre los pines de entrada, es demasiado ineficiente. El método de prueba paralelo es el más comúnmente utilizado. Se utiliza el PPMU en el método paralelo para impulsar todos los pines de entrada a VDDmax (para IIH) o 0V (para IIL) y medir la corriente de cada pin de entrada.

La única desventaja del método paralelo es que no se detectará la fuga de pin a pin, ya que todos los pines se fuerzan al mismo nivel de voltaje al mismo tiempo.

## Prueba de Fuga de Estado de Tristate de Salida (IOZL & IOZH)

El estado de tristate, también conocido como estado de alta impedancia o flotante, indica que el pin del DUT parece tener una alta impedancia externamente.

La fuga de corriente de estado de tristate de salida ocurre cuando se aplica un nivel de voltaje alto o bajo en el pin de salida del DUT, mientras que el pin está preacondicionado para estar deshabilitado. IOZL significa la corriente que fluye hacia afuera cuando se aplica el nivel bajo, e IOZH significa la corriente que fluye hacia adentro cuando se aplica el nivel alto.

![](https://img.wiki-power.com/d/wiki-media/img/20220912120527.png)

Básicamente, IOZL indica la resistencia desde un pin de salida a VDD cuando está deshabilitado, e IOZH indica la resistencia a GND. La prueba asegura que el pin no suministre o consuma más corriente no deseada de lo especificado.

Además, se requiere una entrada de control (señal de habilitación) en esta prueba, para controlar el pin de salida específico en estado bajo, alto o tristate (deshabilitado).

### Método de Prueba (Serial)

#### Prueba de IOZL (Serial)

![](https://img.wiki-power.com/d/wiki-media/img/20220912121730.png)

### Prueba IOZL (Paralelo)

![](https://img.wiki-power.com/d/wiki-media/img/20220912122050.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Preacondicionar el pin de salida específico al estado Hi-Z (deshabilitado).
3. Forzar 0V al Pin bajo prueba y medir el flujo de corriente saliente:
   - **Valor más alto que el especificado (> -10uA)**: APROBADO
   - **Valor más bajo que el especificado (< -10uA)**: FALLIDO
4. Repetir para probar el siguiente pin.

### Prueba IOZH (Serial)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Preacondicionar el pin de salida específico al estado Hi-Z (deshabilitado).
3. Forzar VDDmax al Pin bajo prueba y medir el flujo de corriente entrante:
   - **Valor más alto que el especificado (> 10uA)**: FALLIDO
   - **Valor más bajo que el especificado (< 10uA)**: APROBADO
4. Repetir para probar el siguiente pin.

### Método de prueba (Paralelo)

El método paralelo es en realidad el más comúnmente utilizado con PPMU, para conducir todos los pines de salida a VDDmax (para IOZH) o 0V (para IOZL) y medir la corriente de cada pin de salida.

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
