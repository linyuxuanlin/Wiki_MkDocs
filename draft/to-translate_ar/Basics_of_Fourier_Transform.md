# Fundamentos de la Transformada de Fourier

> Esta publicación solo está disponible en inglés.

Existen varios algoritmos para transformar datos del dominio del tiempo al dominio de la frecuencia, como se muestra a continuación.

## Serie de Fourier

Una **Serie de Fourier** es un resumen de cómo crear una forma de onda compleja sumando ondas senoidales puras con diferentes amplitudes y frecuencias, y descomponer una señal compleja en una suma de sinusoides de diferentes amplitudes y frecuencias.

### Condiciones de Dirichlet

Las Condiciones de Dirichlet especifican un conjunto de condiciones que deben cumplirse antes de que una señal pueda descomponerse en una Serie de Fourier:

- La señal es una función matemática, es decir, un solo punto y solo uno de y corresponde a cada punto de x.
- La señal es periódica.
- El área limitada por la señal en un período es finita.

### Descomposición en una Serie de Fourier

Una señal compleja que cumple las Condiciones de Dirichlet puede representarse como una suma de sinusoides:

$$
f(t)=a_0+A\{\sum_{n=1}^\infty[a_n cos(n \omega_1 t+\phi_n)+b_n sin(n \omega_1 t+\phi_n)]\}
$$

donde:

- $a_0$ es el componente DC.
- $A$ es un factor de escala general para todos los componentes armónicos.
- $\omega_1$ es la frecuencia fundamental.
- $n$ es un multiplicador entero de la frecuencia fundamental para cada término armónico.

Esto demuestra que no solo podemos sumar una serie de ondas senoidales para crear cualquier otra onda, sino que también que las frecuencias de las sinusoides son múltiplos enteros (armónicos) de una sola frecuencia fundamental.

## Transformada de Fourier Discreta (DFT)

La **Transformada de Fourier Discreta (DFT)** toma datos de amplitud versus tiempo y los traduce a datos de amplitud versus frecuencia.

Matemáticamente, el algoritmo es una suma de la serie del producto de cada muestra por un número complejo:

$$
X(b)=\sum_{n=0}^{N-1}x[n](cos(2\pi nb/N)-jsin(2\pi nb/N))
$$

# Transformada de Fourier Discreta (DFT)

La **Transformada de Fourier Discreta (DFT)** es una técnica matemática utilizada para analizar señales en el dominio de la frecuencia. La DFT se utiliza para convertir una señal de tiempo discreto en su representación de frecuencia discreta. La DFT se define como:

$$X_b = \sum_{n=0}^{N-1} x_n e^{-j2\pi bn/N}$$

donde:

- $n$ es uno de $N$ muestras.
- $N$ es el número total de muestras.
- $b$ es uno de $B$ intervalos de frecuencia (cada intervalo representa un rango de frecuencia de $F_s /N$).
- $j$ es el operador imaginario.

El algoritmo DFT utiliza cada punto de muestra en la suma de 0 a N-1 para cada frecuencia analizada. Todos los puntos de muestra N contienen información sobre todas las B frecuencias, por lo que cada una de las B frecuencias para las que se desea información requiere una suma de N productos de muestra de tiempo. Debido a las razones anteriores, procesar una DFT es lento, porque se necesitan $N^2$ cálculos. Por ejemplo, una DFT de 2000 puntos requiere 4 millones de cálculos, a menudo cálculos de punto flotante, que son más lentos que los cálculos enteros.

## Transformada Rápida de Fourier (FFT)

La **Transformada Rápida de Fourier (FFT)** remedia el problema de velocidad de la DFT saltando sobre porciones de las sumas que producen información redundante. Reglas para usar FFT:

- El número de puntos de muestra debe ser una potencia de 2 ($2^n$).
- El número de sumas y multiplicaciones es: $\frac{N}{2}\log_2 N$.

## Referencias y Agradecimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por el acuerdo [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en), debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.