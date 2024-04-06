# RF - Parámetros S

Los parámetros S (parámetros de dispersión), también conocidos como S-Parameters, se utilizan para caracterizar las propiedades de señales reflejadas o transmitidas en el dominio de frecuencia en términos de amplitud y fase. Estos parámetros se representan como una matriz de números complejos. Podemos considerar un circuito como una caja negra (sin tener en cuenta los elementos internos del circuito) y medir sus propiedades en los puertos utilizando los parámetros S.

## Explicación Detallada de los Parámetros S

La nomenclatura de los parámetros S sigue un patrón específico. El primer número indica el puerto de medición, y el segundo número indica el puerto de referencia. Por ejemplo, S21 representa la señal medida en el puerto 2 en relación con la fuente de excitación de la señal en el puerto 1. Los parámetros S pueden expresarse en términos de potencia, voltaje o corriente.

![Imagen](https://media.wiki-power.com/img/20220627100338.png)

En la imagen anterior, S11 y S22 representan los coeficientes de reflexión (reflejo/entrada), mientras que S21 y S12 representan los coeficientes de transmisión (transmisión/entrada).

### S11

![Imagen](https://media.wiki-power.com/img/20220621000000.gif)

S11 se refiere a la señal de reflexión en el puerto 1 en comparación con la señal incidente en el puerto 1. Matemáticamente, se expresa como $S11=\frac{S_{Reflexión}}{S_{Incidente}}$.

### S21

![Imagen](https://media.wiki-power.com/img/20220621000001.gif)

S21 se refiere a la señal de transmisión en el puerto 2 en relación con la señal incidente en el puerto 1. Matemáticamente, se expresa como $S21=\frac{S_{Transmisión}}{S_{Incidente}}$.

### S12

![Imagen](https://media.wiki-power.com/img/20220621000002.gif)

S12 se refiere a la señal de transmisión en el puerto 1 en relación con la señal incidente en el puerto 2. Matemáticamente, se expresa como $S12=\frac{S_{Transmisión}}{S_{Incidente}}$.

### S22

![Imagen](https://media.wiki-power.com/img/20220621000003.gif)

S22 se refiere a la señal de reflexión en el puerto 2 en relación con la señal incidente en el puerto 2. Matemáticamente, se expresa como $S22=\frac{S_{Reflexión}}{S_{Incidente}}$.

## Referencias y Agradecimientos

- [Significado de los Parámetros S y Métodos Prácticos de Medición de Redes Vectoriales](http://jietaipu.com/resource/88.html)
- "Conceptos Básicos de Medición de Parámetros S para Alta Velocidad Digital"

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
