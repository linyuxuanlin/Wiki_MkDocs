# Radiofrecuencia - Parámetros S

Los parámetros S (Scattering parameters, S-Parameters, parámetros de dispersión) se utilizan para reflejar las características (amplitud/fase) de las señales de reflexión/transmisión en el dominio de la frecuencia. Es una matriz compleja. Podemos considerar el interior del circuito como una caja negra (sin tener en cuenta los elementos del circuito interno) y medir sus características de puerto a través de los parámetros S.

## Descripción detallada de los parámetros S

La convención de nomenclatura de los parámetros S es que el primer número representa el puerto de medición y el segundo número representa el puerto de referencia. Por ejemplo, S21 representa la señal medida en el puerto 2 en relación con la fuente de excitación de señal en el puerto 1. La forma de onda de los parámetros S puede ser potencia, voltaje o corriente.

![](https://img.wiki-power.com/d/wiki-media/img/20220627100338.png)

Como se muestra en la figura anterior, S11 y S22 representan los coeficientes de reflexión (reflexión/entrada), mientras que S21 y S12 representan los coeficientes de transmisión (transmisión/entrada).

### S11

![](https://img.wiki-power.com/d/wiki-media/img/20220621000000.gif)

S11 se refiere a la señal de reflexión en el puerto 1 en relación con la señal incidente en el puerto 1, $S11=\frac{S_{Reflection}}{S_{Incident}}$.

### S21

![](https://img.wiki-power.com/d/wiki-media/img/20220621000001.gif)

S21 se refiere a la señal de transmisión en el puerto 2 en relación con la señal incidente en el puerto 1, $S21=\frac{S_{Transmission}}{S_{Incident}}$.

### S12

![](https://img.wiki-power.com/d/wiki-media/img/20220621000002.gif)

S12 se refiere a la señal de transmisión en el puerto 1 en relación con la señal incidente en el puerto 2, $S12=\frac{S_{Transmission}}{S_{Incident}}$.

### S22

![](https://img.wiki-power.com/d/wiki-media/img/20220621000003.gif)

S22 se refiere a la señal de reflexión en el puerto 2 en relación con la señal incidente en el puerto 2, $S22=\frac{S_{Reflection}}{S_{Incident}}$.

## Referencias y agradecimientos

- [Significado de los parámetros S y método de medición práctica de la red vectorial](http://jietaipu.com/resource/88.html)
- "S-Parameter Measurements Basics for High Speed Digital"

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
