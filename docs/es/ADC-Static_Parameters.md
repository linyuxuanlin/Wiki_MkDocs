# ADC - Parámetros Estáticos

> Esta publicación solo está disponible en inglés.

El Convertidor Analógico a Digital (ADC) es un dispositivo que convierte señales analógicas en una secuencia de datos digitales.

![](https://img.wiki-power.com/d/wiki-media/img/20221011141438.png)

Aunque la función de transferencia ideal del ADC debería ser una línea recta, en realidad es una escalera uniforme, donde el número de escalones corresponde al número de códigos de salida digitales. Dado que lo analógico es continuo y lo digital es discreto, se introducirá un error de cuantificación en el procedimiento.

## Parámetros Estáticos

Los parámetros estáticos del ADC principalmente contienen:

- Tamaño del LSB
- Rango de escala completa (FSR)
- Error de desplazamiento
- Error de ganancia
- Error de no linealidad diferencial (DNE o DNL)
- Error de no linealidad integral (INE o INL)

### Tamaño del LSB

El ancho de un paso se define como 1 **Bit Menos Significativo (LSB)**. La resolución de un ADC se expresa normalmente como el número de bits (código de salida digital). Un ADC con una resolución de n bits tiene $2^n$ posibles códigos digitales ($2^n$ niveles de paso).

$$
LSB=\frac{V_{FST}-V_{ZST}}{2^{bits}-2}
$$

Para un ADC ideal, el LSB representa todo el ancho de cada código.

### Rango de escala completa (FSR)

Por ejemplo, para un convertidor de 3 bits, hay:

- 8 pasos horizontales
- 7 transiciones
- 6 pasos entre 7 transiciones

![](https://img.wiki-power.com/d/wiki-media/img/20221008151344.png)

- **Voltaje de Transición de Rango Cero ($V_{ZST}$)**: Voltaje de la señal de entrada analógica cuando se registra la primera transición.
- **Voltaje de Transición de Rango Completo ($V_{FST}$)**: Voltaje de la señal de entrada analógica cuando se registra la última transición.
- **Rango Completo (FSR)**: Extremo máximo de la señal de entrada analógica suministrada al ADC. $FSR = (V_{FST}-V_{ZST}) + 2 LSB$, $V_{FSR(refer to VZS)} = (V_{FST}-0.5LSB)-(V_{ZST}-0.5LSB) + 2 LSB$

### Error de Desplazamiento

**Error de Desplazamiento** (Error de Escala Cero) es la diferencia entre los puntos de desplazamiento ideal y real (inicial). Se mide a partir del punto medio del paso cero (ideal a real) para el ADC.

![](https://img.wiki-power.com/d/wiki-media/img/20221008154521.png)

Donde

$$
V_{ZS}=V_{ZST}-0.5LSB
$$

### Error de Ganancia

**Error de Ganancia** es la diferencia entre los puntos de ganancia ideal y real en la función de transferencia (después de que el error de desplazamiento se ha corregido a cero). Se mide a partir del punto medio del paso completo para el ADC.

![](https://img.wiki-power.com/d/wiki-media/img/20221008155259.png)

Donde

$$
V_{FS}=V_{FST}-0.5LSB+2LSB
$$

### Error de No Linealidad Diferencial (DNL)

**Error de No Linealidad Diferencial (DNL)** es la diferencia entre el ancho de paso real y el ancho de paso ideal (1 LSB). Es una medida del error de linealidad "pequeña señal" y se mide a partir de la diferencia en el voltaje de entrada analógico entre 2 transiciones adyacentes y el LSB promedio del dispositivo.

![](https://img.wiki-power.com/d/wiki-media/img/20221008160020.png)

Ecuaciones para describir DNL:

$$
DNL[n]=CodeWidth_n-LSB_{average}
$$

$$
DNL=(V_{in2}-V_{in1})-LSB_{average}
$$

otra imagen para describir DNL:

Si DNL excede un valor demasiado grande, uno o más códigos faltarán y nunca recibirán una salida.

### Error de No Linealidad Integral (INL)

El **Error de No Linealidad Integral (INL)** es el efecto acumulativo en cualquier entrada dada de todos los valores de no linealidad diferencial. Es una medida del error de linealidad "de gran señal". INL en cualquier punto a lo largo de la curva es la desviación de la línea de linealidad ideal.

![](https://img.wiki-power.com/d/wiki-media/img/20221008163705.png)

Las desviaciones se miden en los puntos de transición de un paso al siguiente para el ADC. INL es la desviación de los valores de la función de paso real a la función de línea recta ideal.

Ecuaciones para describir INL:

$$
INL[n]=INL_{n-1}+{\frac{DNL_{n-1}+DNL_{n}}{2}}
$$

$$
INL=[(\frac{BinaryCode}{2^{bits}-1})(V_{FS}-V_{ZS})+V_{offset}]-CodeCentor
$$

![](https://img.wiki-power.com/d/wiki-media/img/20221008163911.png)

## Cómo probar parámetros estáticos

### Configuración del sistema de prueba

Configuración del sistema de prueba para pruebas de parámetros estáticos de ADC:

![](https://img.wiki-power.com/d/wiki-media/img/20221008184721.png)

Dado que la curva de transferencia de voltaje a código del ADC es una función de mapeo de muchos a uno:

![](https://img.wiki-power.com/d/wiki-media/img/20221008185819.png)

Prácticamente utilizamos el método de histograma de rampa lineal (medición de ancho de código). La rampa de entrada es lo suficientemente lenta como para dar un "número estadísticamente relevante de hits por código".

![](https://img.wiki-power.com/d/wiki-media/img/20221008190154.png)

Diagrama de bloques de la configuración de la señal:

![](https://img.wiki-power.com/d/wiki-media/img/20221008190612.png)

### Concepto de pruebas

El procedimiento para probar los parámetros estáticos de un ADC DUT se detalla a continuación.

#### 1. Crear un segmento de onda de rampa para AC SRC

La rampa de entrada va por encima y por debajo de ±Fs para asegurar que se cubran todos los códigos:

![](https://img.wiki-power.com/d/wiki-media/img/20221008193036.png)

#### 2. Tomar datos entre el inicio (min+1, por ejemplo, 0…01) y el final (max-1, por ejemplo, 1…10) de la rampa. Eso da un valor de datos de $2^n-2$ códigos

La tensión aplicada debe ser más amplia que el rango de escala completa para cubrir todas las transiciones. Se muestran 16 pasos entre cada transición de código:

![](https://img.wiki-power.com/d/wiki-media/img/20221008194207.png)

para el ADC DUT ideal, 16 códigos de salida aparecen al mismo tiempo:

![](https://img.wiki-power.com/d/wiki-media/img/20221008194450.png)

Sin embargo, un dispositivo real tendrá una cuenta más de 16 veces para códigos más amplios y menos de 16 veces para códigos más estrechos (pero la suma del total de ocurrencias debe seguir siendo $2^{bits}$ veces de 16):

![](https://img.wiki-power.com/d/wiki-media/img/20221008194813.png)

#### 3. Calcular el DNL para cada paso

$$
DNL[i]=\frac{Hits[i]-\frac{\sum Hits[i]}{2^n-2}}{\frac{\sum Hits[i]}{2^n-2}}
$$

Donde $Hits[i]$ representa el recuento real de códigos de salida y $\frac{\sum Hits[i]}{2^n-2}$ representa el recuento ideal de códigos de salida.

![](https://img.wiki-power.com/d/wiki-media/img/20221008234157.png)

Para un ejemplo de gráfico de histograma como se muestra a continuación:

![](https://img.wiki-power.com/d/wiki-media/img/20221008234921.png)

para DNL[1] (Código 001),

- Recuento real de códigos de salida = 14
- Recuento ideal de códigos de salida = (14 +18 +15 + 17+ 17 + 15) / (8 -2 ) = 16.

Por lo tanto, $DNL[1] (Código 001) = (14-16)/16 \ LSB => -0.125 \ LSB$.

#### 4. Obtener el DNL máximo y mínimo

![](https://img.wiki-power.com/d/wiki-media/img/20221008235342.png)

#### 5. Calcular el INL para cada paso

INL es el valor acumulativo del primer DNL hasta el DNL[i] (excepto el DNL cero y el DNL de escala completa):

$$
INL[i]=DNL[i]+DNL[i-1]+...+DNL[2]+DNL[1]
$$

Tenga en cuenta que $DNL[0]$ no se utiliza,

$$
INL[0]=INL[FullScale]=0
$$

Para un ejemplo de gráfico a continuación,

![](https://img.wiki-power.com/d/wiki-media/img/20221009201547.png)

$$
INL[1] = DNL[1] = -0.125 * LSB
$$

$$
INL[2] = DNL[2] + DNL[1] = 0 * LSB
$$

$$
INL[3] = DNL[3] + DNL[2] + DNL[1] \\
INL[3]= 0.0625 * LSB
$$

#### 6. Obtener el INL máximo y mínimo

![](https://img.wiki-power.com/d/wiki-media/img/20221009201838.png)

## Referencias y Agradecimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _Los Fundamentos de las Pruebas de Señal Mixta_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
