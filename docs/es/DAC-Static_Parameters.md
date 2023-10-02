# DAC - Parámetros Estáticos

> Esta publicación solo está disponible en inglés.

El Convertidor Digital a Analógico (DAC) es un dispositivo que convierte una secuencia de datos de entrada digital en señales analógicas.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011141644.png)

## Parámetros Estáticos

Los parámetros estáticos del DAC contienen principalmente:

- Salida de escala cero
- Rango de escala completa (FSR)
- Tamaño del LSB
- Error de desplazamiento
- Error de ganancia
- Error de no linealidad diferencial (DNE o DNL)
- Error de no linealidad integral (INE o INL)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011144045.png)

### Salida de escala cero

La **Salida de escala cero** es el valor de salida medido cuando se presenta el código de entrada digital de nivel cero/nulo al DUT.

### Rango de escala completa (FSR)

El rango de voltaje de salida del DAC entre las salidas analógicas mínima ($V_{ZS}$) y máxima ($V_{FS}$) se llama **Rango de escala completa (FSR)**:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011142249.png)

### Tamaño del LSB

El cambio promedio en voltaje cuando se encuentra entre los códigos de entrada se define como LSB:

$$
LSB=\frac{FSR_{medido}}{2^{bits}-1}
$$

### Error de desplazamiento

El **Error de desplazamiento** (Error de escala cero) es la diferencia de voltaje entre los puntos de desplazamiento (inicial) ideal y real.

$$
ErrorDeDesplazamiento=V_{ZS(Real)}-V_{ZS(Ideal)}
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011144415.png)

### Error de ganancia

El **Error de ganancia** es la diferencia de voltaje entre los puntos de ganancia ideal y real en la función de transferencia.

$$
ErrorDeGanancia=FSR_{Ideal}-FSR_{Real}
$$

Donde

$$
FSR_{Ideal}=V_{FS(Ideal)}-V_{ZS(Ideal)}
$$

$$
FSR_{Real}=V_{FS(Real)}-V_{ZS(Real)}
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011144925.png)

### Error de no linealidad diferencial (DNL)

**Error de no linealidad diferencial (DNL)** es la diferencia en el voltaje de salida en un punto específico, en comparación con la salida en la entrada anterior, menos un LSB del dispositivo:

$$
DNL=(V_{in2}-V_{in1})-LSB_{promedio}
$$

donde $V_{in2}$ es el voltaje de la transición superior, $V_{in1}$ es el inferior.

DNL es una medida del error de linealidad de "señal pequeña". La medición de DNL se realiza de un paso al siguiente, no de cada paso al valor ideal.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011153556.png)

### Error de no linealidad integral (INL)

**Error de no linealidad integral (INL)** es el efecto acumulativo de todos los valores de no linealidad diferencial. Es una medida del error de linealidad de "señal grande". INL en cualquier punto a lo largo de la curva es la desviación de la línea de linealidad ideal.

$$
SalidaEsperada[i]=FSR*CódigoDeEntrada[i]+ErrorDeDesplazamiento
$$

$$
INL[i]=\frac{SalidaReal[i]-SalidaEsperada[i]}{LSB_{promedio}}
$$

Además, INL también se puede expresar como una función de DNL:

$$
INL[i]=\sum_{n=1}^{n=i}DNL[n]
$$

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011184739.png)

## Cómo probar parámetros estáticos

### Configuración del sistema de prueba

Configuración del sistema de prueba para pruebas de parámetros estáticos de DAC:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185006.png)

Diagrama de bloques de la configuración de la señal:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185447.png)

### Concepto de pruebas

El procedimiento para probar los parámetros estáticos de un DAC DUT se muestra a continuación.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185739.png)

#### 1. Medir el voltaje de salida aplicando las entradas de datos digitales desde Cero Escala hasta Escala Completa

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20221011185711.png)

#### 2. Calcular DNL para cada código de entrada

$$
DNL[i]=\frac{OutputMeasured[i]-OutputMeasured[i-1]-LSB_{average}}{LSB_{average}}
$$

Donde

$$
LSB_{average}=\frac{OutputMeasured[n]-OutputMeasured[0]}{2^{bits}-1}
$$

#### 3. Obtener el DNL máximo y mínimo

#### 4. Calcular INL para cada paso

#### 5. Obtener el INL máximo y mínimo

## Referencias y Agradecimientos

- *Fundamentos de Pruebas Usando ATE*
- *The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe*

> Original: <https://wiki-power.com/>  
> Este post está protegido por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducido con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.