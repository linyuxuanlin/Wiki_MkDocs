# Prueba IDD

> Esta publicación solo está disponible en inglés.

La corriente de suministro de energía (IDD) indica la corriente que fluye desde el drenador hasta el drenador en un circuito CMOS (llamado ICC en el circuito TTL, que significa colector a colector). IDD puede ser equivalente a:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220910234238.png)

## Prueba IDD estática

IDD estática es una medición de la corriente desde el pin VDD del DUT, cuando el DUT está en estado estático (el DUT no está activo durante la prueba). El valor de IDD estática indica el consumo de corriente más bajo del DUT, que es importante para dispositivos operados con batería, y también ayuda a indicar defectos marginales.

### Método de prueba

La prueba IDD estática se realiza aplicando un voltaje de VDDmax y midiendo el valor de corriente, mientras el DUT está preacondicionado a su estado lógico de menor consumo de corriente.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911201659.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Preacondicionar el DUT a su estado lógico de menor consumo de corriente.
3. Medir la corriente que fluye hacia el pin VDD:
   - **Valor superior al especificado (>10uA)**: FALLA
   - **Valor inferior al especificado (<10uA)**: APROBADO

## Prueba IDD dinámica

IDD dinámica es una medición de la corriente desde el pin VDD del DUT, cuando el DUT está realizando constantemente alguna función. IDD dinámica también es importante para dispositivos operados con batería.

### Método de prueba

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911201603.png)

La prueba IDD dinámica se realiza aplicando un voltaje de VDDmax y midiendo el valor de corriente, mientras el DUT está preacondicionado a un estado de trabajo continuo.

## Prueba de corriente de suministro máximo (IDDQ)

La prueba de corriente de suministro máximo (IDDQ) es una medición de IDD en los estados de reposo (el circuito no está cambiando y las entradas se mantienen en valores estáticos). A medida que los procesadores se reducen, el defecto de corriente de fuga se vuelve mucho más alto, y la prueba IDDQ puede detectar defectos menores dentro del núcleo del circuito que de otra manera no podrían ser detectados.

### Método de prueba

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911213042.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Preacondicionar DUT a un estado de trabajo continuo.
3. Medir la corriente que fluye hacia el pin VDD:
   - **Mayor que el valor especificado (>50mA)**: FALLA
   - **Menor que el valor especificado (<50mA)**: APROBADO

## Prueba de corriente de reposo (IDDQ)

La corriente de reposo es una medición de IDD en los estados de reposo (el circuito no está cambiando y las entradas se mantienen en valores estáticos). A medida que los procesadores se reducen, el defecto de corriente de fuga se vuelve mucho más alto, y la prueba IDDQ puede detectar defectos menores dentro del núcleo del circuito que de otra manera no podrían ser detectados.

### Método de prueba

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220911213042.png)

1. Aplicar VDDmax al pin VDD (con pinza de corriente).
2. Preacondicionar DUT a un cierto estado de trabajo (activar/desactivar cierta parte de la función como Bluetooth y Wi-Fi).
3. Medir la corriente que fluye hacia el pin VDD:
   - **Mayor que el valor especificado**: FALLA
   - **Menor que el valor especificado**: APROBADO
4. Repetir la prueba con diferentes estados de trabajo.

## Referencias y agradecimientos

- _Los fundamentos de la prueba de semiconductores digitales_
- _Fundamentos de la prueba utilizando ATE_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.