# Prueba de Continuidad

La prueba de continuidad consta de una prueba de circuito abierto/cortocircuito y una prueba de cortocircuito en el pin de alimentación. La primera verifica los pines de señal, mientras que la segunda verifica el pin de alimentación.

## Prueba de Continuidad de Circuito Abierto/Cortocircuito

La prueba de continuidad de circuito abierto/cortocircuito tiene como objetivo confirmar el contacto eléctrico entre el probador y el dispositivo bajo prueba (DUT, por sus siglas en inglés) y verificar si existe un cortocircuito con otros pines o con tierra.

### Método de Prueba

La prueba de continuidad de circuito abierto/cortocircuito se realiza mediante la prueba de los diodos de protección (diodos hacia VDD y hacia GND). Generalmente, se utiliza el código PPMU con VBT (también se puede probar utilizando PE y un patrón funcional).

#### Prueba a través del diodo de protección a tierra

![Prueba a través del diodo de protección a tierra](https://media.wiki-power.com/img/20220909003924.png)

1. Aplicar 0V a todos los pines que no se están probando (incluido el pin de alimentación).
2. Aplicar una pequeña corriente negativa (-100uA) en el Pin Bajo Prueba (con limitación de voltaje).
3. Medir el voltaje en el Pin Bajo Prueba:
   - **Mayor que la especificación máxima (> -0.2V)**: FALLA (Cortocircuito)
   - **En el rango medio (-1.5V ~ -0.2V)**: APROBADO
   - **Menor que la especificación mínima (< -1.5V)**: FALLA (Circuito Abierto)

#### Prueba a través del diodo de protección a VDD

![Prueba a través del diodo de protección a VDD](https://media.wiki-power.com/img/20220909004139.png)

1. Aplicar 0V a todos los pines que no se están probando (incluido el pin de alimentación).
2. Aplicar una pequeña corriente positiva (+100uA) en el Pin Bajo Prueba (con limitación de voltaje).
3. Medir el voltaje en el Pin Bajo Prueba:
   - **Mayor que la especificación máxima (> 1.5V)**: FALLA (Cortocircuito)
   - **En el rango medio (0.2V ~ 1.5V)**: APROBADO
   - **Menor que la especificación mínima (< 0.2V)**: FALLA (Circuito Abierto)

## Prueba de Cortocircuito en el Pin de Alimentación

La prueba de cortocircuito en el pin de alimentación tiene como objetivo verificar si hay un cortocircuito entre el pin de VDD y el pin de GND, lo cual podría causar daños al DUT o al probador. La prueba de cortocircuito en el pin de alimentación siempre se realiza inmediatamente después de la prueba de continuidad de circuito abierto/cortocircuito. Si esta prueba falla, se apagará la alimentación del dispositivo y se rechazará el DUT.

### Método de Prueba

El Test de Cortocircuito en el Pin de Alimentación se realiza aplicando un pequeño voltaje a VDD y midiendo la corriente que entra en él para comprobar si existe un cortocircuito. Normalmente se utiliza DCVI con el código VBT.

![Imagen](https://media.wiki-power.com/img/20220910155805.png)

1. Aplicar un pequeño voltaje a VDD (100mV) (con una pinza de corriente).
2. Forzar que todos los demás pines estén a 0V con PPMU.
3. Medir la corriente que fluye en el pin VDD:
   - **Superior al límite máximo (>20uA)**: FALLA (Cortocircuito)
   - **En el rango intermedio (-1uA~20uA)**: APROBADO
   - **Inferior al límite mínimo (<-1uA)**: FALLA

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de Pruebas Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
