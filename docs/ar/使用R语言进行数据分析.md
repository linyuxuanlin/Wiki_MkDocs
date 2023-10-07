# Análisis de datos con R

## Instalación de software

- [**R-software**](https://cran.r-project.org/)
  - Si se utiliza en Windows, haga clic en `Download R for Windows` en la página principal del sitio web, luego haga clic en `install R for the first time` y finalmente haga clic en `Download R 4.0.4 for Windows`. Después de descargar el software, complete la instalación por su cuenta.
  - El software de soporte de R solo se ejecuta en segundo plano y no tiene una interfaz gráfica.
- [**RStudio**](https://rstudio.com/products/rstudio/download/#download)
  - Simplemente haga clic en el botón azul `Download` o seleccione otra versión del sistema en la parte inferior de la página para descargar el software. Después de descargar el software, complete la instalación por su cuenta.

## Recursos de enseñanza

### Recursos en línea (recomendados)

- [R-tutorial](http://www.r-tutor.com/r-introduction)
- [Aprende R desde cero](https://bookdown.org/qiyuandong/intro_r/)

### Libros

- [The R-book](https://www.cs.upc.edu/~robert/teaching/estadistica/TheRBook.pdf)
- [R para Ciencia de Datos](https://r4ds.had.co.nz/index.html)

## Tipos de datos básicos

Los tipos de datos en R se dividen principalmente en los siguientes:

- **Numérico (numerics)**
- **Entero (integer)**
- **Complejo (complex)**
- **Lógico (logical)**
- **Carácter (characters)**

### Numérico (numerics)

El tipo numérico es el tipo de datos más básico en R. Cuando asignamos un valor numérico a una variable, el tipo de la variable es numérico:

```r
> x = 11.15       # Asignar el valor numérico 11.15 a la variable x
> x              # Imprimir el valor de x
[1] 11.15
> class(x)       # Imprimir el tipo de x
[1] "numeric"
```

Tanto los enteros como los decimales pueden ser variables numéricas. Pero si se crea de esta manera, las variables enteras también se considerarán variables decimales.

### Entero (integer)

Si desea crear una variable entera, debe usar la función `is.integer`:

```r
> y = as.integer(3)
> y              # Imprimir el valor de y
[1] 3
> class(y)       # Imprimir el tipo de y
[1] "integer"
> is.integer(y)  # ¿Es y un número entero?
[1] TRUE
```

Además de usar la función `is.integer`, también puede agregar el sufijo `L` para lograrlo:

```r
> y = 3L
> is.integer(y)  # ¿Es y un número entero?
[1] TRUE
```

Si desea redondear un decimal, puede usar la función `as.integer`:

```r
> as.integer(3.14)    # Convertir la variable en un número entero
[1] 3
```

También puede analizar y redondear variables de tipo cadena:

```r
> as.integer("5.27")  # Convertir la variable en un número entero
[1] 5
```

Pero si la cadena analizada no es un número, se producirá un error:

```r
> as.integer("Joe")   # Analizar una cadena que no es numérica
[1] NA
Warning message:
NAs introduced by coercion
```

Al igual que en C, en R, los enteros `1` `0` y los lógicos `TRUE` `FALSE` se corresponden:

```r
> as.integer(TRUE)    # Variable numérica de TRUE
[1] 1
> as.integer(FALSE)   # Variable numérica de FALSE
[1] 0
```

### Complejo (complex)

En R, las variables complejas se definen mediante `i`:

```r
> z = 2 + 3i       # Asignar el valor complejo 2 + 3i a la variable z
> z              # Imprimir el valor de z
[1] 2+3i
> class(z)       # Imprimir el tipo de z
[1] "complex"
```

Español:

```r
> z = 1 + 2i     # Crear una variable compleja z
> z              # Imprimir el valor de z
[1] 1+2i
> class(z)       # Imprimir el tipo de z
[1] "complex"
```

Si intentamos calcular la raíz cuadrada de `-1`, obtendremos un error:

```r
> sqrt(−1)       # Calcular la raíz cuadrada de -1
[1] NaN
Warning message:
In sqrt(−1) : NaNs produced
```

Pero si calculamos la raíz cuadrada de `-1+0i`, no habrá problema:

```r
> sqrt(−1+0i)    # Calcular la raíz cuadrada de −1+0i
[1] 0+1i
```

También podemos realizar operaciones con conversión de tipo forzado:

```r
> sqrt(as.complex(−1))
[1] 0+1i
```

### Tipo lógico (logical)

El tipo lógico se genera generalmente al comparar variables:

```r
> x = 1; y = 2   # Variables de muestra
> z = x > y      # ¿Es x mayor que y?
> z              # Imprimir la variable lógica
[1] FALSE
> class(z)       # Imprimir el tipo de z
[1] "logical"
```

Las operaciones lógicas básicas son `&` (y), `|` (o), `!` (no):

```r
> u = TRUE; v = FALSE
> u & v          # Operación "y" entre u y v
[1] FALSE
> u | v          # Operación "o" entre u y v
[1] TRUE
> !u             # Operación "no" en u
[1] FALSE
```

### Tipo caracter (character)

El tipo caracter se puede obtener mediante la conversión forzada con la función `as.character`:

```r
> x = as.character(3.14)
> x              # Imprimir la cadena
[1] "3.14"
> class(x)       # Imprimir el tipo de x
[1] "character"
```

Para combinar dos variables de tipo caracter, se puede utilizar la función `paste`:

```r
> fname = "Joe"; lname ="Smith"
> paste(fname, lname)
[1] "Joe Smith"
```

Al igual que en la sintaxis de C, se puede utilizar la función `sprintf` para imprimir con formato y mejorar la legibilidad:

```r
> sprintf("%s has %d dollars", "Sam", 100)
[1] "Sam has 100 dollars"
```

Si se desea extraer una subcadena de una cadena, se puede utilizar la función `substr` (en el ejemplo se extraen los caracteres entre el tercero y el duodécimo):

```r
> substr("Mary has a little lamb.", start=3, stop=12)
[1] "ry has a l"
```

Si se desea reemplazar el primer carácter encontrado por otro, se puede utilizar la función `sub` (en el ejemplo se reemplaza `little` por `big`):

```r
> sub("little", "big", "Mary has a little lamb.")
[1] "Mary has a big lamb."
```

## Vectores

### Vectores en R

Un vector es un arreglo que contiene elementos del mismo tipo, y los elementos de un vector se llaman componentes.

A continuación se muestra un ejemplo de vector (que contiene tres variables numéricas `2`, `3` y `5`):

```r
> c(2, 3, 5)
[1] 2 3 5
```

También puede estar compuesto completamente de valores lógicos:

```r
> c(TRUE, FALSE, TRUE, FALSE, FALSE)
[1] TRUE FALSE TRUE FALSE FALSE
```

O puede estar compuesto de valores de tipo caracter:

```r
> c("aa", "bb", "cc", "dd", "ee")
[1] "aa" "bb" "cc" "dd" "ee"
```

Para conocer la cantidad de componentes de un vector, se puede utilizar la función `length`:

```r
> length(c("aa", "bb", "cc", "dd", "ee"))
[1] 5
```

### Combinando vectores

Si desea combinar dos vectores, puede usar la función `c`:

```r
> n = c(2, 3, 5)
> s = c("aa", "bb", "cc", "dd", "ee")
> c(n, s)
[1] "2"  "3"  "5"  "aa" "bb" "cc" "dd" "ee"
```

Tenga en cuenta que en el ejemplo anterior, si combina dos vectores de diferentes tipos de datos, el tipo combinado será compatible hacia abajo (es decir, el tipo más estricto se convertirá en el tipo más relajado, como convertir un tipo numérico en un tipo de carácter).

### Operaciones básicas de vectores

Supongamos que tenemos dos vectores `a` y `b`:

```r
> a = c(1, 3, 5, 7)
> b = c(1, 2, 4, 8)
```

A continuación se muestran las operaciones básicas de vectores:

```r
> a + b
[1] 2 5 9 15

> a - b
[1] 0 1 1 -1

> 5 * a
[1] 5 15 25 35

> a * b
[1] 1 6 20 56

> a / b
[1] 1.000 1.500 1.250 0.875
```

Si la cantidad de miembros de los dos vectores que se suman no es la misma, el resultado será compatible hacia abajo, es decir, la longitud de la variable de salida dependerá del más largo:

```r
> u = c(10, 20, 30)
> v = c(1, 2, 3, 4, 5, 6, 7, 8, 9)
> u + v
[1] 11 22 33 14 25 36 17 28 39
```

### Recuperando vectores

Si desea recuperar un miembro del vector, puede usar el método de índice declarando el índice en `[ ]`, es decir, `[número de miembro]`:

```r
> s = c("aa", "bb", "cc", "dd", "ee")
> s[3]  # recupera el valor del tercer miembro y lo muestra
[1] "cc"
```

Si agrega un signo menos antes del índice, como `[-3]`, significa que recupera todos los miembros excepto el tercer miembro:

```r
> s[-3]
[1] "aa" "bb" "dd" "ee"
```

Si el índice está fuera de la longitud del vector, se producirá un error:

```r
> s[10]
[1] NA
```

【En proceso de actualización】

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.