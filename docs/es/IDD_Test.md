# Prueba de IDD

La corriente de suministro de energía (IDD) indica la corriente que fluye de Drain a Drain en un circuito CMOS (llamada ICC en el circuito TTL, lo que significa de Colector a Colector). IDD puede ser equivalente a:

![](https://img.wiki-power.com/d/wiki-media/img/20220910234238.png)

## Prueba de IDD Estática

IDD estática es una medición de la corriente desde el pin VDD del DUT, cuando el DUT está en estado estático (el DUT no está activo durante la prueba). El valor de IDD estática indica el consumo de corriente más bajo del DUT, lo cual es importante para dispositivos operados con batería y también ayuda a indicar defectos marginales.

### Método de Prueba

La prueba de IDD estática se realiza aplicando un voltaje de VDDmax y midiendo el valor de corriente, mientras el DUT se condiciona a su estado lógico de menor consumo de corriente.

![](https://img.wiki-power.com/d/wiki-media/img/20220911201659.png)

1. Aplicar VDDmax al pin VDD (con abrazadera de corriente).
2. Condicionar el DUT a su estado lógico de menor consumo de corriente.
3. Medir la corriente que fluye hacia el pin VDD:
   - **Mayor que el valor especificado (>10uA)**: FALLA
   - **Menor que el valor especificado (<10uA)**: APROBADO

## Prueba de IDD Dinámica

IDD dinámica es una medición de la corriente desde el pin VDD del DUT, cuando el DUT está constantemente realizando alguna función. La IDD dinámica también es importante para dispositivos operados con batería.

### Método de Prueba

![](https://img.wiki-power.com/d/wiki-media/img/20220911201603.png)

La prueba de IDD dinámica se realiza aplicando un voltaje de VDDmax y midiendo el valor de corriente, mientras el DUT se condiciona a un estado de funcionamiento continuo.

1. Aplicar VDDmax al pin VDD (con abrazadera de corriente).
2. Condicionar el DUT a un estado de funcionamiento continuo.
3. Medir la corriente que fluye hacia el pin VDD:
   - **Mayor que el valor especificado (>50mA)**: FALLA
   - **Menor que el valor especificado (<50mA)**: APROBADO

## Prueba de IDD en Reposo (IDDQ)

La IDD quiescente es una medición de la corriente de fuga IDD en los estados de reposo (el circuito no está cambiando y las entradas se mantienen en valores estáticos). A medida que los procesadores se reducen en tamaño, el defecto de corriente de fuga se vuelve mucho más alto, y la prueba IDDQ puede detectar defectos menores en el núcleo del circuito que de otra manera no podrían ser detectados.

### Método de Prueba

![](https://img.wiki-power.com/d/wiki-media/img/20220911213042.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Preacondicionar el DUT a un estado de funcionamiento específico (activar/desactivar ciertas partes de la función, como Bluetooth y Wi-Fi).
3. Medir la corriente que fluye en el pin VDD:
   - **Mayor que el valor especificado**: FALLA
   - **Menor que el valor especificado**: APROBADO
4. Repetir la prueba con diferentes estados de funcionamiento.

## Referencias y Agradecimientos

- _Los Fundamentos de las Pruebas de Semiconductores Digitales_
- _Fundamentos de Pruebas Utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), y debe reproducirse con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.