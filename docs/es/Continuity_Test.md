# Prueba de Continuidad

La prueba de continuidad incluye la prueba de circuito abierto o cortocircuito y la prueba de cortocircuito de pines de alimentación. La primera verifica los pines de señal, mientras que la segunda verifica el pin de alimentación.

## Prueba de Continuidad de Circuito Abierto/Cortocircuito

La prueba de continuidad de circuito abierto o cortocircuito tiene como objetivo confirmar el contacto eléctrico entre el probador y el Dispositivo Bajo Prueba (DUT, por sus siglas en inglés) y verificar si existe un cortocircuito con otros pines o con tierra.

### Método de Prueba

La prueba de continuidad de circuito abierto/cortocircuito se realiza verificando los diodos de protección (diodos hacia VDD y hacia GND). Normalmente, se utiliza PPMU con el código VBT (también se puede realizar utilizando PE y un patrón funcional).

#### Prueba a través del diodo de protección de GND

![](https://img.wiki-power.com/d/wiki-media/img/20220909003924.png)

1. Aplicar 0V a todos los otros pines que no se están probando (incluyendo el pin de alimentación).
2. Aplicar una pequeña corriente negativa (-100uA) en el Pin Bajo Prueba (con un tope de voltaje).
3. Medir el voltaje en el Pin Bajo Prueba:
   - **Superior al límite máximo (>-0.2V)**: FALLA (Cortocircuito)
   - **Rango medio (-1.5V~-0.2V)**: APROBADO
   - **Inferior al límite mínimo (<-1.5V)**: FALLA (Circuito Abierto)

#### Prueba a través del diodo de protección de VDD

![](https://img.wiki-power.com/d/wiki-media/img/20220909004139.png)

1. Aplicar 0V a todos los otros pines que no se están probando (incluyendo el pin de alimentación).
2. Aplicar una pequeña corriente positiva (+100uA) en el Pin Bajo Prueba (con un tope de voltaje).
3. Medir el voltaje en el Pin Bajo Prueba:
   - **Superior al límite máximo (>1.5V)**: FALLA (Cortocircuito)
   - **Rango medio (0.2V~1.5V)**: APROBADO
   - **Inferior al límite mínimo (<0.2V)**: FALLA (Circuito Abierto)

## Prueba de Cortocircuito de Pin de Alimentación

La prueba de cortocircuito de pin de alimentación tiene como objetivo verificar si existe un cortocircuito entre el pin de VDD y el pin de GND, lo cual podría causar daños al DUT o al probador. Esta prueba se realiza siempre inmediatamente después de la prueba de continuidad de circuito abierto/cortocircuito, y en caso de falla, se apagará la alimentación del dispositivo y se rechazará el DUT.

La Prueba de Cortocircuito de Power Pin se realiza aplicando un pequeño voltaje a VDD y midiendo la corriente que fluye hacia él para comprobar si existe un cortocircuito. Normalmente se utiliza DCVI con el código VBT.

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20220910155805.png)

1. Aplicar un pequeño voltaje a VDD (100 mV) (con pinza de corriente).
2. Forzar que todos los demás pines estén a 0V con PPMU.
3. Medir la corriente que fluye al pin VDD:
   - **Más alta que la especificación máxima (>20uA)**: FALLA (Cortocircuito)
   - **En el rango medio (-1uA~20uA)**: APROBADO
   - **Más baja que la especificación mínima (<-1uA)**: FALLA

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba con ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo de [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.