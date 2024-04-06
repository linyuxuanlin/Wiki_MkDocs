# Esquema de alimentación (Boost) - SX1308

Nota: Este IC del esquema no es estable, no se recomienda su uso.

Dirección del proyecto: **<https://github.com/linyuxuanlin/Modularity_of_Functional_Circuit/tree/master/Power/SX1308>**

- **Principio**: DC/DC (Boost)
- **Voltaje de entrada**: 2-24 V
- **Voltaje de salida**: Hasta 28 V
- **Corriente de salida**: 2 A
- **Frecuencia de trabajo**: 1.2 MHz
- **Eficiencia**: Hasta un 97%
- **Precio**: ¥ 0.57
- **Características**:
  - Arranque suave incorporado
  - Bloqueo de subvoltaje de entrada
  - Cambio automático al modo PFM en carga ligera
  - Limitación de corriente
  - Protección contra sobrecalentamiento

## Definición de pines

![](https://media.wiki-power.com/img/20210713154103.png)

## Diseño de referencia

![](https://media.wiki-power.com/img/20210715141625.png)

## Ajuste de parámetros

(Para obtener parámetros más detallados, consulte el manual de datos)

### Ajuste del voltaje de salida

Ajuste el voltaje de salida mediante la modificación de las resistencias divisoras de retroalimentación $R_1$ y $R_2$ (voltaje de referencia de retroalimentación $V_{REF}=0.6 V$):

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

El pin EN es el pin de habilitación. Se activa cuando es mayor a 1.5 V y se desactiva cuando es menor a 0.4 V. No deje este pin sin conexión.

## Referencia de diseño de PCB

- Coloque el condensador de entrada de alimentación cerca de los pines de alimentación del IC.
- Coloque los condensadores de entrada y salida cerca de la tierra del IC para reducir el área del bucle de corriente.
- Amplíe y acorte las pistas de VIN, SW y VOUT para permitir un mayor flujo de corriente alterna.
- Reduzca el cobre en el pin SW del chip para prevenir EMI causado por voltaje alterno.
- Acorte las pistas de FB para evitar interferencias de ruido. Coloque la resistencia de retroalimentación cerca del chip y coloque el GND de R2 lo más cerca posible del pin GND del IC. Además, el enrutamiento de VOUT a R1 debe estar alejado de la inductancia y los nodos de conmutación.

## Resumen de problemas encontrados

- El esquema de referencia en el manual de datos en chino probablemente tenga un error en el condensador NP0 de 15 pF, que debería ser un condensador de filtrado conectado a tierra (también se puede omitir). Si no se elimina, no podrá manejar cargas pesadas.
  - Consulte el hilo técnico de referencia <http://www.crystalradio.cn/thread-1497661-1-1.html>
- **Este circuito es muy sensible al diseño de PCB**. No debe haber mucho cobre en el pin SW, ya que puede haber capacitancia parásita. Se deben seguir estrictamente las recomendaciones de diseño mencionadas anteriormente.
- Se ha comprobado que la corriente máxima de salida de carga es de aproximadamente 800 mA, lo que permite mantener estable el voltaje de salida (11.6 V).
- El pin EN no debe dejarse sin conexión. Debe ser pull-up (para habilitar Boost) o pull-down (para deshabilitar), de lo contrario, mantendrá el voltaje original de salida.

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
