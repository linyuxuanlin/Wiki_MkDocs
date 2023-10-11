# Prueba de continuidad

> Esta publicación solo está disponible en inglés.

La prueba de continuidad contiene la prueba de circuito abierto/cortocircuito y la prueba de cortocircuito de los pines de alimentación. La primera verifica los pines de señal, mientras que la segunda verifica el pin de alimentación.

## Prueba de continuidad de circuito abierto/cortocircuito

La prueba de continuidad de circuito abierto/cortocircuito es para confirmar el contacto electrónico entre el probador y el DUT, y si existe un cortocircuito a otros pines o a tierra.

### Método de prueba

La prueba de continuidad de circuito abierto/cortocircuito se realiza probando los diodos de protección (diodos a VDD y a GND). Por lo general, se utiliza PPMU con el código VBT (también se puede probar con PE y patrón funcional).

#### Prueba a través del diodo de protección de GND

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220909003924.png)

1. Forzar 0V a todos los demás pines que no se están probando (incluido el pin de alimentación).
2. Forzar una corriente negativa pequeña (-100uA) en el Pin bajo prueba (con pinza de voltaje).
3. Medir el voltaje en el Pin bajo prueba:
   - **Mayor que la especificación máxima (> -0.2V)**: FALLA (Cortocircuito)
   - **Banda media (-1.5V ~ -0.2V)**: APROBADO
   - **Menor que la especificación mínima (<-1.5V)**: FALLA (Circuito abierto)

#### Prueba a través del diodo de protección de VDD

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220909004139.png)

1. Forzar 0V a todos los demás pines que no se están probando (incluido el pin de alimentación).
2. Forzar una corriente positiva pequeña (+100uA) en el Pin bajo prueba (con pinza de voltaje).
3. Medir el voltaje en el Pin bajo prueba:
   - **Mayor que la especificación máxima (> 1.5V)**: FALLA (Cortocircuito)
   - **Banda media (0.2V ~ 1.5V)**: APROBADO
   - **Menor que la especificación mínima (<0.2V)**: FALLA (Circuito abierto)

## Prueba de cortocircuito de los pines de alimentación

La prueba de cortocircuito de pines de alimentación es para verificar si hay un cortocircuito desde el pin VDD hasta el pin GND, lo que causará daños al DUT o al probador. La prueba de cortocircuito de pines de alimentación siempre se ejecuta inmediatamente después de la prueba de continuidad abierta/cerrada, y cuando falla, se apagará la alimentación del dispositivo y se rechazará el DUT.

### Método de prueba

La prueba de cortocircuito de pines de alimentación se realiza aplicando un pequeño voltaje a VDD y midiendo la corriente que entra en él para verificar si existe un cortocircuito. Por lo general, se utiliza DCVI con código VBT.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220910155805.png)

1. Aplicar un pequeño voltaje a VDD (100 mV) (con pinza amperimétrica).
2. Forzar todos los demás pines a 0V con PPMU.
3. Medir la corriente que fluye hacia el pin VDD:
   - **Mayor que la especificación máxima (>20uA)**: FALLA (Cortocircuito)
   - **Banda media (-1uA~20uA)**: APROBADO
   - **Menor que la especificación mínima (<-1uA)**: FALLA

## Referencias y Agradecimientos

- _Los fundamentos de la prueba de semiconductores digitales_
- _Fundamentos de la prueba utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
