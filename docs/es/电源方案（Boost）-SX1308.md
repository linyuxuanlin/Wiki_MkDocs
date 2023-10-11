# Esquema de alimentación (Boost) - SX1308

Nota: Este IC de esquema no es estable, no se recomienda su uso.

Dirección del proyecto: **<https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/Power/SX1308>**

- **Principio**: DC/DC (Boost)
- **Voltaje de entrada**: 2-24 V
- **Voltaje de salida**: hasta 28 V
- **Corriente de salida**: 2 A
- **Frecuencia de trabajo**: 1.2 MHz
- **Eficiencia**: hasta el 97%
- **Precio**: ¥ 0.57
- **Características**
  - Arranque suave incorporado
  - Bloqueo de subvoltaje de entrada
  - Cambio automático al modo PFM en carga ligera
  - Limitación de corriente
  - Protección contra sobrecalentamiento

## Definición de pines

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210713154103.png)

## Diseño de referencia

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210715141625.png)

## Ajuste de parámetros

(Para obtener parámetros más detallados, consulte el manual de datos)

### Ajuste del voltaje de salida

Ajuste el voltaje de salida (voltaje de retroalimentación $V_{REF}=0.6 V$) ajustando las resistencias de división de retroalimentación $R_1$ y $R_2$:

$V_{OUT}=V_{REF}\times(1+\frac{R_1}{R_2})$

Por lo general, si se selecciona $R_2$ como 10 kΩ, la relación entre $V_{OUT}$ y $R_1$ es la siguiente:

| $V_{OUT}$ |  $R_1$  |
| :-------: | :-----: |
|    5 V    | 73.2 kΩ |
|   10 V    | 158 kΩ  |
|   12 V    | 191 kΩ  |
|   15 V    | 240 kΩ  |
|   20 V    | 324 kΩ  |

### Pin de habilitación

EN es el pin de habilitación, se inicia cuando es mayor de 1.5 V y se apaga cuando es menor de 0.4 V. No deje este pin sin conexión.

## Referencia de diseño de PCB

- Coloque el capacitor de entrada de alimentación cerca de los pines de alimentación del IC.
- Coloque los capacitores de entrada y salida cerca de la GND del IC para reducir el área del circuito de corriente.
- Amplíe y acorte las líneas de alimentación VIN, SW y VOUT para permitir un mayor flujo de corriente alterna.
- Reduzca el cobre en el pie de SW del chip para prevenir EMI causado por voltaje alterno.
- Acorte las líneas de retroalimentación para evitar interferencias de ruido, coloque la resistencia de retroalimentación cerca del chip, la GND de R2 debe colocarse lo más cerca posible del pin GND del IC, y la línea de distribución de VOUT a R1 debe estar lejos del inductor y los nodos de conmutación.

## Resumen de problemas comunes

- El diagrama de referencia en el manual de datos en chino probablemente dibujó mal el capacitor NP0 de 15 pF, que debería ser un capacitor de filtro conectado a tierra (también se puede omitir). Si no se elimina, no podrá manejar grandes cargas.
  - Consulte el hilo técnico <http://www.crystalradio.cn/thread-1497661-1-1.html>
- Este circuito es muy sensible a la disposición de PCB. El cobre en el pie de SW no debe ser demasiado grande, de lo contrario habrá capacitancia parásita. Otros aspectos deben seguir estrictamente la referencia de diseño anterior.
- La corriente máxima de salida medida es de alrededor de 800 mA, y el voltaje de salida se mantiene estable (11.6 V de salida).
- El pin EN no debe dejarse sin conexión, debe ser pull-up (para habilitar Boost) o pull-down (para deshabilitar), de lo contrario el voltaje original se mantendrá como salida.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
