# Fundamentos de la Transformada de Fourier

Existen varios algoritmos para transformar datos del dominio temporal al dominio de frecuencia, como se detalla a continuación.

## Serie de Fourier

Una **Serie de Fourier** se resume en la creación de una forma de onda compleja mediante la suma de ondas senoidales puras con diferentes amplitudes y frecuencias, y en la descomposición de una señal compleja en una suma de sinusoides de diferentes amplitudes y frecuencias.

### Condiciones de Dirichlet

Las Condiciones de Dirichlet especifican un conjunto de condiciones que deben cumplirse antes de que una señal pueda descomponerse en una Serie de Fourier:

- La señal es una función matemática, es decir, un único punto y solo uno corresponde a cada punto en el eje x.
- La señal es periódica.
- El área delimitada por la señal a lo largo de un periodo es finita.

### Descomposición en una Serie de Fourier

Una señal compleja que cumple con las Condiciones de Dirichlet puede representarse como una suma de sinusoides:

$$
f(t) = a_0 + A \left\{ \sum_{n=1}^\infty [a_n \cos(n \omega_1 t + \phi_n) + b_n \sin(n \omega_1 t + \phi_n)] \right\}
$$

donde:

- $a_0$ es el componente de corriente continua (CC).
- $A$ es un factor de escala general para todos los componentes armónicos.
- $\omega_1$ es la frecuencia de la fundamental.
- $n$ es un multiplicador entero de la frecuencia fundamental para cada término armónico.

Esto demuestra que no solo podemos sumar una serie de ondas senoidales para crear cualquier otra onda, sino también que las frecuencias de los sinusoides son múltiplos enteros (armónicos) de una única frecuencia fundamental.

## Transformada de Fourier Discreta (DFT)

La **Transformada de Fourier Discreta (DFT)** toma datos de amplitud frente al tiempo y los traduce a datos de amplitud frente a frecuencia.

Matemáticamente, el algoritmo es una suma de series del producto de cada muestra por un número complejo:

$$
X(b) = \sum_{n=0}^{N-1} x[n](\cos(2\pi nb/N) - j\sin(2\pi nb/N))
$$

donde:

- $n$ es uno de las $N$ muestras.
- $N$ es el número total de muestras.
- $b$ es uno de los $B$ intervalos de frecuencia (cada intervalo representa un rango de frecuencia de $F_s /N$).
- $j$ es el operador imaginario.

El algoritmo de la Transformada de Fourier Discreta (DFT) utiliza cada punto de muestra en la suma de 0 a N-1 para cada frecuencia analizada. Todos los puntos de muestra N contienen información sobre todas las frecuencias B, por lo tanto, cada una de las B frecuencias para las cuales se desea información requiere una suma de productos de muestras de tiempo N. Debido a las razones mencionadas anteriormente, el procesamiento de una DFT es lento, ya que se requieren $N^2$ cálculos. Por ejemplo, una DFT de 2000 puntos requiere 4 millones de cálculos, a menudo cálculos en punto flotante, que son más lentos que los cálculos en números enteros.

## Transformada Rápida de Fourier (FFT)

La **Transformada Rápida de Fourier (FFT)** soluciona el problema de velocidad de la DFT saltándose partes de las sumas que producen información redundante. Reglas para utilizar la FFT:

- El número de puntos de muestra debe ser una potencia de 2 ($2^n$).
- El número de sumas y multiplicaciones es: $\frac{N}{2}\log_2 N$.

## Referencias y Reconocimientos

- _Fundamentos de Pruebas Utilizando ATE_
- _The-Fundamentals-of-Mixed-Signal-Testing_Brian-Lowe_

> Original: <https://wiki-power.com/>  
> Esta publicación está protegida por un acuerdo de [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.es), y debe ser reproducida con atribución.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.