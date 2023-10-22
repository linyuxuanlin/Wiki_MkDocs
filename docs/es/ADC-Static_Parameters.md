# ADC - Parámetros Estáticos

El Convertidor Analógico-Digital (ADC) es un dispositivo que convierte señales analógicas en una secuencia de datos digitales.

![Imagen del ADC](https://img.wiki-power.com/d/wiki-media/img/20221011141438.png)

Aunque la función de transferencia ideal de un ADC debería ser una línea recta, en realidad se asemeja a una escalera uniforme, donde la cantidad de escalones corresponde al número de códigos de salida digitales. Dado que lo analógico es continuo y lo digital es discreto, se introduce un error de cuantización en el proceso.

## Parámetros Estáticos

Los parámetros estáticos de un ADC incluyen principalmente:

- Tamaño del LSB (Bit Menos Significativo)
- Rango de Escala Completa (FSR, por sus siglas en inglés)
- Error de Desplazamiento
- Error de Ganancia
- Error de No Linealidad Diferencial (DNE o DNL)
- Error de No Linealidad Integral (INE o INL)

### Tamaño del LSB

El ancho de un paso se define como 1 **Bit Menos Significativo (LSB)**. La resolución de un ADC se expresa normalmente en número de bits (código de salida digital). Un ADC con una resolución de n bits tiene $2^n$ códigos digitales posibles (niveles de paso $2^n$).

$$
LSB=\frac{V_{FST}-V_{ZST}}{2^{bits}-2}
$$

En un ADC ideal, el LSB representa el ancho de cada código.

### Rango de Escala Completa (FSR)

Por ejemplo, en un convertidor de 3 bits, hay:

- 8 pasos horizontales
- 7 transiciones
- 6 pasos entre 7 transiciones

![Ejemplo de Pasos en un ADC de 3 bits](https://img.wiki-power.com/d/wiki-media/img/20221008151344.png)

- **Voltaje de Transición del Rango Cero ($V_{ZST}$)**: Voltaje de la señal de entrada analógica cuando se registra la primera transición.
- **Voltaje de Transición del Rango de Escala Completa ($V_{FST}$)**: Voltaje de la señal de entrada analógica cuando se registra la última transición.
- **Rango de Escala Completa (FSR)**: Extremo máximo de la señal de entrada analógica suministrada al ADC. $FSR = (V_{FST}-V_{ZST}) + 2 LSB$, $V_{FSR(referido a VZS)} = (V_{FST}-0.5LSB)-(V_{ZST}-0.5LSB) + 2 LSB$

### Error de Desplazamiento

**Error de Desplazamiento (Error de Escala Cero)** es la diferencia entre los puntos ideales y reales de desplazamiento (iniciales). Se mide desde el punto medio del paso cero (de lo ideal a lo real) para el convertidor analógico a digital (ADC).

![](https://img.wiki-power.com/d/wiki-media/img/20221008154521.png)

Donde

$$
V_{ZS}=V_{ZST}-0.5LSB
$$

### Error de Ganancia

**Error de Ganancia** es la diferencia entre los puntos ideales y reales de ganancia en la función de transferencia (después de que el error de desplazamiento se ha corregido a cero). Se mide desde el punto medio del paso completo para el ADC.

![](https://img.wiki-power.com/d/wiki-media/img/20221008155259.png)

Donde

$$
V_{FS}=V_{FST}-0.5LSB+2LSB
$$

### Error de No Linealidad Diferencial (DNL)

**Error de No Linealidad Diferencial (DNL)** es la diferencia entre el ancho de paso real y el ancho de paso ideal (1 LSB). Es una medida del error de linealidad de "pequeña señal" y se mide a partir de la diferencia en el voltaje de entrada analógica entre dos transiciones adyacentes y el LSB promedio del dispositivo.

![](https://img.wiki-power.com/d/wiki-media/img/20221008160020.png)

Ecuaciones para describir DNL:

$$
DNL[n]=AnchoCódigo_n-LSB_promedio
$$

$$
DNL=(V_{in2}-V_{in1})-LSB_promedio
$$

otra imagen para describir DNL:

![](https://img.wiki-power.com/d/wiki-media/img/20221008161707.png)

Si DNL es demasiado grande, faltará uno o más códigos y nunca se obtendrá una salida.

### Error de No Linealidad Integral (INL)

**Error de No Linealidad Integral (INL)** es el efecto acumulativo en cualquier entrada dada de todos los valores de no linealidad diferencial. Es una medida del error de linealidad de "gran señal". El INL en cualquier punto a lo largo de la curva es la desviación de la línea de linealidad ideal.

![](https://img.wiki-power.com/d/wiki-media/img/20221008163705.png)

Las desviaciones se miden en los puntos de transición de un paso al siguiente para el ADC. INL es la desviación de los valores de la función de paso real con respecto a la función ideal de línea recta.

Ecuaciones para describir INL:

$$
INL[n]=INL_{n-1}+{\frac{DNL_{n-1}+DNL_{n}}{2}}
$$

$$
INL=[(\frac{CódigoBinario}{2^{bits}-1})(V_{FS}-V_{ZS})+V_{offset}]-CentroCódigo
$$

![](https://img.wiki-power.com/d/wiki-media/img/20221008163911.png)

## Cómo Probar Parámetros Estáticos

### Configuración del Sistema de Prueba

Configuración del sistema de prueba para las pruebas de parámetros estáticos del ADC:

![](https://img.wiki-power.com/d/wiki-media/img/20221008184721.png)

Dado que la curva de transferencia de voltaje a código del ADC es una función de asignación de muchos a uno:

![](https://img.wiki-power.com/d/wiki-media/img/20221008185819.png)

Prácticamente utilizamos el método de histograma de rampa lineal (medición del ancho del código). La rampa de entrada es lo suficientemente lenta como para proporcionar un "número relevante de ocurrencias por código" estadísticamente.

![](https://img.wiki-power.com/d/wiki-media/img/20221008190154.png)

Diagrama de bloque de la configuración de la señal:

![](https://img.wiki-power.com/d/wiki-media/img/20221008190612.png)

### Concepto de Pruebas

El procedimiento para probar los parámetros estáticos de un dispositivo ADC se enumera a continuación.

#### 1. Crear un segmento de onda de rampa para SRC de CA

Las rampas de entrada van por encima y por debajo de ±Fs para asegurar que todos los códigos estén cubiertos:

![](https://img.wiki-power.com/d/wiki-media/img/20221008193036.png)

#### 2. Tomar datos entre el inicio (mínimo+1, p. ej., 0…01) y el final (máximo-1, p. ej., 1…10) de la rampa. Eso proporciona datos equivalentes a $2^n – 2$ códigos

El voltaje aplicado debe ser mayor que el rango de escala completa para cubrir todas las transiciones. A continuación se muestran 16 pasos entre cada transición de código:

![](https://img.wiki-power.com/d/wiki-media/img/20221008194207.png)

Para el dispositivo ADC ideal, 16 códigos de salida aparecen al mismo tiempo:

```markdown
![](https://img.wiki-power.com/d/wiki-media/img/20221008194450.png)

Sin embargo, un dispositivo real tendrá un conteo más de 16 veces para códigos más amplios y menos de 16 veces para códigos más estrechos (pero la suma de la ocurrencia total seguirá siendo $2^{bits}$ veces 16):

![](https://img.wiki-power.com/d/wiki-media/img/20221008194813.png)

#### 3. Calcular el DNL para cada paso

$$
DNL[i]=\frac{Hits[i]-\frac{\sum Hits[i]}{2^n-2}}{\frac{\sum Hits[i]}{2^n-2}}
$$

Donde $Hits[i]$ representa el Recuento de Códigos de Salida Reales, y $\frac{\sum Hits[i]}{2^n-2}$ representa el Recuento de Códigos de Salida Ideales.

![](https://img.wiki-power.com/d/wiki-media/img/20221008234157.png)

Para un ejemplo de gráfico de histograma como se muestra a continuación:

![](https://img.wiki-power.com/d/wiki-media/img/20221008234921.png)

para DNL[1] (Código 001),

- Recuento de Códigos de Salida Reales = 14
- Recuento de Códigos de Salida Ideales = (14 +18 +15 + 17+ 17 + 15) / (8 -2 ) = 16.

Por lo tanto, $DNL[1] (Código 001) = (14-16)/16 \ LSB => -0.125 \ LSB$.

#### 4. Obtener el DNL máximo y mínimo

![](https://img.wiki-power.com/d/wiki-media/img/20221008235342.png)

#### 5. Calcular el INL para cada paso

INL es el valor acumulativo del primer DNL hasta DNL[i] (excepto el DNL de cero y la escala completa):

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
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_
```

```markdown
**Traducción:** [**https://wiki-power.com/**](https://wiki-power.com/)  
Este artículo está protegido por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) y debe ser reproducido con atribución.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.