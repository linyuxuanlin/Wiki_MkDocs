# Fundamentos de ADC y DAC

En el mundo real, la mayoría de las señales son analógicas, como la temperatura, el sonido, la presión, etc. Sin embargo, en el procesamiento y transmisión de señales, se utiliza principalmente la señal digital para reducir la interferencia del ruido. Por lo tanto, a menudo convertimos la señal analógica del mundo real en una señal digital a través de ADC para realizar operaciones, transmisión y almacenamiento, y luego convertirla en una señal analógica a través de DAC para presentarla.

![](https://f004.backblazeb2.com/file/wiki-media/img/20220724210409.png)

Pero hay que tener en cuenta que la señal analógica en el mundo real es continua, lo que significa que tiene una resolución infinita, pero después de convertirse en una señal digital, perderá cierta precisión y se convertirá en valores discretos en tiempo y amplitud.

## Principios básicos de ADC

ADC (Convertidor analógico a digital) se refiere a un convertidor que convierte señales analógicas del mundo real, como temperatura, presión, sonido o imágenes, en una forma digital más fácil de almacenar, procesar y transmitir.

### Muestreo

Dado que la señal analógica de entrada es continua y la señal digital de salida es discreta, solo se puede realizar un muestreo instantáneo, y luego convertir el valor de muestreo en una cantidad digital de salida y comenzar un nuevo ciclo de muestreo.

Para representar con precisión la señal de entrada analógica $v_1$ con la señal $v_s$, se debe cumplir al menos el teorema de muestreo, es decir, la frecuencia de muestreo $f_s$ debe ser al menos el doble de la frecuencia máxima de la señal de entrada analógica $f_{i(max)}$ (generalmente se toma de 3 a 5 veces, pero las frecuencias demasiado altas requieren una velocidad de trabajo más rápida y deben considerarse los costos):

$$
f_s≥2\cdot f_{i(max)}
$$

![](https://f004.backblazeb2.com/file/wiki-media/img/20220724180529.png)

Si se cumple el teorema de muestreo, la señal $v_s$ se puede restaurar a $v_1$ mediante un filtro paso bajo. El coeficiente de transferencia de voltaje del filtro debe mantenerse constante por debajo de $f_{i(max)}$ y caer rápidamente a cero antes de $f_s-f_{i(max)}$.

### Mantenimiento

El circuito de mantenimiento permite que la señal se mantenga durante un período de tiempo después del muestreo para que el ADC tenga suficiente tiempo para realizar la conversión. Cuanto mayor sea la frecuencia de pulso de muestreo y la densidad de muestreo, más cerca estará la señal de salida del circuito de mantenimiento de la forma de onda de la señal de entrada. La forma básica del circuito de muestreo-mantenimiento es la siguiente:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220723161306.png)

Los pasos básicos del muestreo-mantenimiento son los siguientes:

1. Cuando la señal de control de muestreo $v_L$ es alta, el MOSFET $T$ se enciende, la señal $v_1$ pasa a través de la resistencia $R_1$ y el MOSFET $T$ y carga el capacitor $C_H$.
2. Si se toma $R_1=R_F$, después de que se complete la carga, $v_0=v_c=-v_1$.
3. Cuando la señal de control de muestreo $v_L$ cae a nivel bajo, el MOSFET $T$ se apaga y la tensión en el capacitor $C_H$ no cambia abruptamente, por lo que $v_0$ también puede mantenerse durante un período de tiempo y el resultado del muestreo se puede registrar.

### Cuantificación

La cantidad digital obtenida por muestreo debe ser un múltiplo entero de una unidad de cantidad mínima especificada. Este proceso de conversión se llama cuantificación, y la unidad de cantidad mínima tomada se llama unidad de cuantificación $\Delta$. El tamaño de la cantidad representada por el bit menos significativo (LSB) de la señal digital es igual a $\Delta$.

Como el voltaje analógico es continuo, no necesariamente es divisible por $\Delta$, lo que resulta en un error de cuantificación.

Cuanto más fina sea la unidad de cuantificación, menor será el error de cuantificación y mayor será el número de bits de código binario utilizado, lo que aumentará la complejidad del circuito.

### Codificación

La conversión cuantificada se representa en binario (u otro sistema de numeración), lo que se llama codificación.

## Tipos comunes de ADC

### Comparador paralelo (Flash)

El ADC de comparador paralelo, también conocido como ADC Flash, es un tipo de ADC directo que puede convertir directamente el voltaje analógico de entrada en una cantidad digital de salida sin la necesidad de una conversión intermedia. Está compuesto por una serie de comparadores de voltaje, cada uno de los cuales compara la señal de entrada con un voltaje de referencia único. La salida del comparador se conecta a la entrada del circuito codificador para producir una salida binaria.

![](https://f004.backblazeb2.com/file/wiki-media/img/20220723163931.png)

No solo es la técnica ADC más simple en teoría de operación, sino que también es la más efectiva en velocidad, solo limitada por la propagación de comparadores y retardos de puerta. Desafortunadamente, para cualquier cantidad dada de bits de salida, es el componente más denso.

El ADC de comparación en paralelo tiene la velocidad de conversión más rápida, pero el inconveniente es que requiere el uso de muchos comparadores de voltaje y circuitos de conversión de código a gran escala (la mayoría de las salidas comunes de comparación en paralelo son de 8 bits o menos).

### Tipo de aproximación sucesiva

El ADC de aproximación sucesiva utiliza una estructura de circuito de comparación de retroalimentación. Está compuesto por comparadores, DAC, registros, fuente de pulso de reloj y lógica de control:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220723211839.png)

Su principio es establecer una cantidad digital, obtener una tensión de salida analógica correspondiente a través de DAC. Compare secuencialmente esta tensión analógica con la señal de tensión analógica de entrada desde el bit más alto. Si no son iguales, ajuste la cantidad digital tomada hasta que las dos tensiones analógicas sean iguales. La cantidad digital tomada finalmente es el resultado de conversión buscado. Su proceso es como pesar un objeto por su peso en una balanza, primero agregue una pesa grande, luego agregue o cambie a una pesa pequeña de forma secuencial.

La ventaja del ADC de aproximación sucesiva es su alta velocidad, bajo consumo de energía y ventaja de costo-beneficio en baja resolución (12 bits); la desventaja es que la velocidad de conversión es generalmente baja y el tamaño del circuito es mediano.

### Tipo de doble integración (V-T)

El ADC de doble integración es un tipo de ADC indirecto que convierte la señal de voltaje analógica de entrada en una señal de ancho de tiempo proporcional a ella primero, y luego cuenta los pulsos de reloj de frecuencia fija dentro de este ancho de tiempo. El valor de conteo es la señal digital proporcional a la entrada analógica. Por lo tanto, también se llama ADC de transformación de voltaje-tiempo (V-T).

El ADC de doble integración está compuesto por integradores, comparadores, contadores, lógica de control y fuente de señal de reloj, como se muestra en la figura:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220723213208.png)

La ventaja del ADC de doble integración es su rendimiento de trabajo estable (dos integraciones, excluyendo las diferencias de parámetros RC), fuerte capacidad antiinterferencias (la integración no se ve muy afectada por el ruido); la desventaja es que la velocidad de conversión es baja (la precisión de conversión depende del tiempo de integración).

### Tipo Σ-Δ

El principio del ADC de modulación Σ-Δ es diferente del tipo de comparación en paralelo y de aproximación sucesiva mencionados anteriormente. No cuantifica y codifica el valor absoluto de la señal de muestreo, sino que cuantifica y codifica la diferencia (incremento) entre dos valores de muestreo adyacentes. Su estructura básica es la siguiente:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220723230949.png)

Está compuesto por un integrador de voltaje lineal, un cuantizador de salida de 1 bit, un DAC de entrada de 1 bit y un circuito sumador. El valor digital de salida $V_0$ procesado por el cuantizador se convierte en una señal analógica $V_F$ a través del DAC y se retroalimenta al circuito sumador de entrada. Reste la señal de entrada $v_1$ para obtener la diferencia $v_D$. El integrador realiza una integración lineal en $v_D$, la tensión de salida $v_{INT}$ se cuantifica en un bit y se convierte en una señal digital de salida. Debido al uso de un cuantizador de salida de 1 bit, en un estado de trabajo continuo, la señal de salida $V_0$ es una corriente de datos compuesta por 0 y 1.

La ventaja del ADC de modulación Σ-Δ es que se puede lograr fácilmente una medición de alta resolución; la desventaja es que la velocidad de conversión es baja y el tamaño del circuito es grande.

### Transformación de voltaje-frecuencia (V-F)

El ADC de transformación de voltaje-frecuencia (V-F) es un tipo de ADC indirecto. Está compuesto principalmente por un convertidor V-F (también llamado oscilador controlado por voltaje, VCO), un contador y su puerta de control de señal de reloj, un registro y un disparador de estado estable:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220723233236.png)

Su principio es:

- Convertir la señal de voltaje analógica de entrada en una señal de frecuencia correspondiente.
- Contar la tasa de señal de frecuencia en un tiempo fijo.
- El resultado del conteo es proporcional al valor de amplitud de la tensión de entrada.

## Parámetros principales del ADC

## Principios básicos del ADC

- **Resolución**: la cantidad de cambio en la tensión analógica de entrada necesaria para producir un cambio de una unidad en la cantidad digital de salida. Por lo general, se expresa en términos de la cantidad de bits binarios utilizados para representar la señal analógica de entrada, y se define como 1/2^n de la escala completa (Fs) del ADC.
- **Error de cuantificación**: el error que se produce al cuantificar una señal analógica debido a la limitación del número de bits utilizados en el ADC. Para representar con precisión una señal analógica, se necesitaría un número infinito de bits en el ADC, por lo que todos los ADC tienen un error de cuantificación. El error de cuantificación es la máxima desviación entre la curva de conversión de un ADC con resolución limitada y la curva de conversión de un ADC con resolución infinita.
- **Velocidad de conversión**: la cantidad de conversiones que se realizan por segundo.
- **Rango de conversión**: la tensión máxima que el ADC puede medir, que generalmente es igual a la tensión de referencia. Si la señal de entrada es demasiado grande, puede dañar el ADC. Si la señal es demasiado pequeña, se puede aumentar la resolución reduciendo la tensión de referencia. Sin embargo, al cambiar la tensión de referencia, también se cambia el valor de conversión correspondiente, por lo que al calcular la tensión real, se debe tener en cuenta la tensión de referencia. Por lo tanto, la tensión de referencia generalmente debe ser estable y no tener armónicos de alta frecuencia.
- **Error de offset**: el valor de salida del ADC cuando la señal de entrada es cero.
- **Error de escala completa**: la diferencia entre el valor de entrada ideal y el valor de entrada correspondiente a la salida máxima del ADC.
- **Linealidad**: la máxima desviación entre la función de transferencia real del ADC y la línea ideal.

## Principios básicos del DAC

DAC (convertidor digital-analógico) convierte una señal digital en una señal analógica proporcional. Por ejemplo, una computadora puede generar una salida digital que varía de `00000000` a `11111111`, y el DAC la convierte en una tensión de 0 a 10 V. En términos generales, los DAC se pueden dividir en dos tipos: sumador de corriente y divisor de voltaje.

## Tipos comunes de DAC

### Árbol de conmutación

El DAC de árbol de conmutación es el más simple y directo. Está compuesto por una red de resistencias y un árbol de conmutación:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220724172844.png)

Estos interruptores están controlados por tres entradas $d_0,d_1,d_2$, y la salida se puede calcular como:

$$
v_0=\frac{V_{REF}}{2^1} d_2+\frac{V_{REF}}{2^2} d_1+\frac{V_{REF}}{2^3} d_0
$$

$$
v_0=\frac{V_{REF}}{2^3} (d_2 2^2+d_1 2^1+d_0 2^0)
$$

Para un DAC de árbol de conmutación de n bits, la salida se puede calcular como:

$$
v_0=\frac{V_{REF}}{2^n} (d_{n-1} 2^{n-1}+d_{n-2} 2^{n-2}+...+d_1 2^1+d_0 2^0)
$$

La ventaja del DAC de árbol de conmutación es que solo se necesita un tipo de resistencia, y los requisitos de resistencia de conmutación no son altos si la corriente de salida es baja. Sin embargo, la desventaja es que se necesitan muchos interruptores.

### Red de resistencias ponderadas

El término "ponderado" se refiere al valor que representa cada bit en un número binario. Por ejemplo, en un número binario de n bits $D_n=d_{n-1}d_{n-2}...d_1 d_0$, el valor de cada bit, de MSB a LSB, es $2^{n-1},2^{n-2}...2^1,2^0$.

El DAC de red de resistencias ponderadas (que produce una tensión de salida) se compone de una red de resistencias ponderadas, cuatro interruptores analógicos y un amplificador sumador:

![](https://f004.backblazeb2.com/file/wiki-media/img/20220724003300.png)

En este artículo se discute el funcionamiento de los convertidores digital-analógico (DAC, por sus siglas en inglés) de tipo red de resistencias y de tipo red de resistencias invertida, así como el DAC de corriente ponderada. 

En el DAC de red de resistencias, se utilizan cuatro interruptores electrónicos, denominados S0, S1, S2 y S3, que son controlados por cuatro señales d0, d1, d2 y d3. Cuando la entrada es 1, el interruptor se conecta a la tensión de referencia VREF, mientras que cuando la entrada es 0, el interruptor se conecta a tierra. Por lo tanto, cuando di=1, la corriente i fluye hacia el amplificador de suma, mientras que cuando di=0, la corriente i es cero. El amplificador de suma es un amplificador de retroalimentación negativa, de tal manera que cuando el potencial en la entrada inversora V- es menor que el potencial en la entrada no inversora V+, la tensión de salida v0 con respecto a tierra es positiva, mientras que cuando V- es mayor que V+, v0 es negativa. Además, cuando V- es ligeramente mayor que V+, se puede obtener una gran tensión de salida negativa en v0. La señal v0 se retroalimenta a través de RF a V-, lo que hace que V- disminuya hasta que se iguala a V+ (0V).

Suponiendo que el amplificador operacional es un dispositivo ideal (es decir, que la corriente de entrada es cero), se puede obtener:

vO=-RF iΣ=-RF (I3+I2+I1+I0)

Además, como V-≈0, las corrientes en cada rama son:

I3=VREF/2^0R d3

I2=VREF/2^1R d2

I1=VREF/2^2R d1

I0=VREF/2^3R d0

donde dn puede ser 0 o 1. Sustituyendo en la ecuación anterior y suponiendo que RF=R/2, se obtiene la siguiente ecuación para la tensión de salida:

vO=-VREF/2^4(d3 2^3+d2 2^2+d1 2^1+d0 2^0)

Además, para un DAC de red de resistencias ponderadas de n bits, cuando RF=R/2, la fórmula para la tensión de salida es:

vO=-VREF/2^n(dn-1 2^n-1+dn-2 2^n-2+...+d1 2^1+d0 2^0)

vO=-VREF/2^nDn

Por lo tanto, la tensión analógica de salida es proporcional a la cantidad digital de entrada Dn, y su rango de variación es de 0 a -2^n-1/2^n VREF. Por otro lado, si se desea obtener una tensión de salida positiva, se debe proporcionar una VREF negativa.

La ventaja del DAC de red de resistencias es su estructura simple, pero la desventaja es que los valores de resistencia pueden diferir significativamente, lo que puede causar una gran imprecisión en la práctica. Para mejorar esto, se puede utilizar una red de resistencias invertida, que solo utiliza dos valores de resistencia, R y 2R (también conocido como DAC R2R), lo que ayuda a mejorar la precisión de control.

En el DAC de red de resistencias invertida, cuando la resistencia de retroalimentación del amplificador operacional es R, la tensión de salida es:

vO=-RiΣ=-VREF/2^nDn

Por lo tanto, la fórmula de cálculo es la misma que la del DAC de red de resistencias.

Cuando se analizan las redes de resistencias y las redes de resistencias invertidas, se consideran los interruptores analógicos como dispositivos ideales, pero en la práctica tienen una resistencia de conducción y una caída de voltaje, y la consistencia entre los interruptores puede ser diferente, lo que puede causar errores de conversión y afectar la precisión. Para solucionar esto, se puede utilizar un DAC de corriente ponderada, que tiene una serie de fuentes de corriente constante, donde la corriente de cada fuente es la mitad de la anterior y está en proporción directa con el peso binario de la entrada. El uso de fuentes de corriente constante hace que el tamaño de cada corriente de rama no esté influenciado por la resistencia de conducción y la caída de voltaje de los interruptores.

En el DAC de corriente ponderada, cuando un bit de entrada es 1, el interruptor correspondiente conecta la fuente de corriente constante al amplificador operacional de entrada, mientras que cuando el código de entrada es 0, el interruptor se conecta a tierra, por lo que la tensión de salida es:

vO=RF VREF/2^nRR Dn

Los principales parámetros de un DAC son la resolución, la precisión, la velocidad de conversión y la linealidad.

- **Resolución**: la relación entre la tensión mínima de salida (es decir, la tensión cuando la entrada digital es 1) y la tensión máxima de salida (es decir, la tensión cuando la entrada digital es el valor máximo, con todos los bits en 1). Por lo general, se expresa en función del número de bits de la entrada digital.
- **Rango de conversión**: la tensión máxima que el DAC puede producir, generalmente en relación con la tensión de referencia o sus múltiplos.
- **Tiempo de establecimiento**: el tiempo de retardo desde la entrada digital hasta la salida analógica.
- **Precisión de conversión**: similar a la precisión de conversión del ADC.

## Referencias y agradecimientos

- [ADC/DAC Application Design Handbook](https://picture.iczhiku.com/resource/eetop/syIFpRpWgQqgOXnx.pdf)
- [Conversión analógica a digital y digital a analógica](https://www.cnblogs.com/redlightASl/p/15542623.html)
- [ADC y DAC (convertidores analógico a digital y digital a analógico)](https://www.youtube.com/playlist?list=PLwjK_iyK4LLCnW-df-_53d-6yYrGb9zZc)
- [Principios de DAC](https://www.bilibili.com/read/cv4873472/)
- [Referencia de bolsillo del ingeniero analógico](《Analog Engineer’s Pocket Reference》)
- [Tecnología digital electrónica (6ª edición) \_ Yan Shi](《数字电子技术（第六版）\_阎石》)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.