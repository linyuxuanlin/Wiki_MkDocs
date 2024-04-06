# Prueba IDD

La corriente de suministro de energía (IDD) indica la corriente que fluye desde el drenaje al drenaje en un circuito CMOS (llamada ICC en un circuito TTL, que significa colector a colector). IDD puede ser equivalente a:

![](https://media.wiki-power.com/img/20220910234238.png)

## Prueba IDD Estática

IDD estática es una medición de la corriente desde el pin VDD del DUT cuando el DUT se encuentra en estado estático (el DUT no está activo durante la prueba). El valor de IDD estática indica el consumo de corriente más bajo del DUT, lo cual es importante para dispositivos alimentados por batería y también ayuda a indicar defectos marginales.

### Método de Prueba

La prueba IDD estática se realiza aplicando un voltaje de VDDmax y midiendo el valor de corriente mientras el DUT se encuentra en su estado lógico de menor consumo de corriente.

![](https://media.wiki-power.com/img/20220911201659.png)

1. Aplicar VDDmax al pin VDD (con una pinza de corriente).
2. Acondicionar el DUT a su estado lógico de menor consumo de corriente.
3. Medir la corriente que fluye al pin VDD:
   - **Mayor que el valor especificado (>10uA)**: FALLA
   - **Menor que el valor especificado (<10uA)**: APROBADO

## Prueba IDD Dinámica

IDD dinámica es una medición de la corriente desde el pin VDD del DUT cuando el DUT está constantemente realizando alguna función. IDD dinámica también es importante para dispositivos alimentados por batería.

### Método de Prueba

![](https://media.wiki-power.com/img/20220911201603.png)

La prueba IDD dinámica se realiza aplicando un voltaje de VDDmax y midiendo el valor de corriente mientras el DUT se encuentra en un estado de funcionamiento continuo.

1. Aplicar VDDmax al pin VDD (con una pinza de corriente).
2. Acondicionar el DUT a un estado de funcionamiento continuo.
3. Medir la corriente que fluye al pin VDD:
   - **Mayor que el valor especificado (>50mA)**: FALLA
   - **Menor que el valor especificado (<50mA)**: APROBADO

## Prueba IDD en Reposo (IDDQ)

La IDD quiescente es una medida de la corriente de fuga en los estados quiescentes (el circuito no está cambiando y las entradas se mantienen en valores estáticos). A medida que los procesadores se vuelven más pequeños, el defecto de corriente de fuga se vuelve mucho más alto, y la prueba IDDQ puede detectar defectos menores dentro del núcleo del circuito que de otra manera no podrían detectarse.

### Método de Prueba

![Imagen](https://media.wiki-power.com/img/20220911213042.png)

1. Aplicar VDDmax al pin VDD (con una abrazadera de corriente).
2. Preacondicionar el DUT a un estado de funcionamiento específico (alternar ciertas partes de la función de encendido/apagado, como Bluetooth y Wi-Fi).
3. Medir la corriente que fluye al pin VDD:
   - **Mayor que el valor especificado**: FALLA
   - **Menor que el valor especificado**: APROBADO
4. Repetir la prueba con diferentes estados de funcionamiento.

## Referencias y Agradecimientos

- _Los Fundamentos de la Prueba de Semiconductores Digitales_
- _Fundamentos de la Prueba Utilizando ATE_

> Original: <https://wiki-power.com/>
> Esta publicación está protegida por un acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
