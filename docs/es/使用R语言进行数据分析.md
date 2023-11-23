# Análisis de datos con R

## Instalación de software

- [**Software R**](https://cran.r-project.org/)
  - Si estás utilizando Windows, ve al sitio web y haz clic en `Descargar R para Windows`, luego selecciona `Instalar R por primera vez` y finalmente, descarga `Descargar R 4.0.4 para Windows`. Una vez descargado, procede a instalar el software.
  - El software R se ejecuta solo en segundo plano y no tiene una interfaz gráfica.

- [**RStudio**](https://rstudio.com/products/rstudio/download/#download)
  - Haz clic directamente en el botón azul "Descargar" o elige otras versiones del sistema en la parte inferior de la página. Luego, descarga el software y procede a instalarlo.

## Recursos de aprendizaje

### Recursos en línea (recomendados)

- [Tutorial de R](http://www.r-tutor.com/r-introduction)
- [Aprendizaje de R desde cero](https://bookdown.org/qiyuandong/intro_r/)

### Libros

- [El libro de R](https://www.cs.upc.edu/~robert/teaching/estadistica/TheRBook.pdf)
- [R para Ciencia de Datos](https://r4ds.had.co.nz/index.html)

## Tipos de datos básicos

R tiene varios tipos de datos principales:

- **Numéricos (numerics)**
- **Enteros (integer)**
- **Complejos (complex)**
- **Lógicos (logical)**
- **Caracteres (characters)**

### Numéricos (numerics)

Los datos numéricos son el tipo de dato más básico en R. Cuando asignas un valor numérico a una variable, esa variable se convierte en un dato numérico:

```r
> x = 11.15       # Asignamos el valor 11.15 a la variable x
> x              # Mostramos el valor de x
[1] 11.15
> class(x)       # Mostramos el tipo de x
[1] "numeric"
```

Tanto los enteros como los decimales pueden ser variables numéricas. Sin embargo, si creas una variable de esta manera, incluso los enteros se considerarán decimales.

### Enteros (integer)

Para crear variables de tipo entero, debes utilizar la función `as.integer`:

```r
> y = as.integer(3)
> y              # Mostramos el valor de y
[1] 3
> class(y)       # Mostramos el tipo de y
[1] "integer"
> is.integer(y)  # ¿Es y un entero?
[1] TRUE
```

También puedes añadir la sufijo `L` para lograr lo mismo:

```r
> y = 3L
> is.integer(y)  # ¿Es y un entero?
[1] TRUE
```

Si necesitas redondear un decimal para obtener un entero, puedes utilizar la función `as.integer`:

```r
> as.integer(3.14)    # Convertimos la variable a un entero
[1] 3
```

También puedes analizar y redondear variables de tipo carácter:

```r
> as.integer("5.27")  # Convertimos la variable a un entero
[1] 5
```

Sin embargo, si intentas analizar una cadena que no es numérica, obtendrás un error:

```r
> as.integer("Joe")   # Analizamos una cadena no numérica
[1] NA
Warning message:
NAs introduced by coercion
```

Al igual que en C, en R, los enteros `1` y `0` se asocian a los valores lógicos `TRUE` y `FALSE`:

```r
> as.integer(TRUE)    # Valor numérico de TRUE
[1] 1
> as.integer(FALSE)   # Valor numérico de FALSE
[1] 0
```

### Complejos (complex)

En R, las variables complejas se definen utilizando `i`:

```r
> z = 1 + 2i     # Create a complex variable z
> z              # Output the value of z
[1] 1+2i
> class(z)       # Output the type of z
[1] "complex"
```

Si intentamos calcular la raíz cuadrada de `-1`, obtendremos un error:

```r
> sqrt(-1)       # Calcular la raíz cuadrada de -1
[1] NaN
Warning message:
In sqrt(-1) : NaNs produced
```

Pero si calculamos la raíz cuadrada del número complejo `-1+0i`, no tendremos problemas:

```r
> sqrt(-1+0i)    # Calcular la raíz cuadrada de -1+0i
[1] 0+1i
```

También podemos realizar la operación utilizando conversión de tipo forzada:

```r
> sqrt(as.complex(-1))
[1] 0+1i
```

### Tipo lógico (logical)

Los valores lógicos generalmente se generan a través de comparaciones entre variables:

```r
> x = 1; y = 2   # Variables de ejemplo
> z = x > y      # ¿x es mayor que y?
> z              # Mostrar el valor lógico
[1] FALSE
> class(z)       # Mostrar el tipo de z
[1] "logical"
```

Las operaciones lógicas básicas incluyen `&` (y), `|` (o), `!` (no):

```r
> u = TRUE; v = FALSE
> u & v          # Operación "y" entre u y v
[1] FALSE
> u | v          # Operación "o" entre u y v
[1] TRUE
> !u             # Operación "no" en u
[1] FALSE
```

### Tipo carácter (character)

Los valores de tipo carácter se pueden obtener utilizando la función `as.character`:

```r
> x = as.character(3.14)
> x              # Mostrar la cadena de caracteres
[1] "3.14"
> class(x)       # Mostrar el tipo de x
[1] "character"
```

Para combinar dos variables de tipo carácter, se puede utilizar la función `paste`:

```r
> fname = "Joe"; lname ="Smith"
> paste(fname, lname)
[1] "Joe Smith"
```

Al igual que en la sintaxis de C, se puede usar `sprintf` para formatear la salida y mejorar la legibilidad:

```r
> sprintf("%s tiene %d dólares", "Sam", 100)
[1] "Sam tiene 100 dólares"
```

Si deseas extraer una subcadena de una cadena de caracteres, puedes utilizar la función `substr` (en el ejemplo, se extraen los caracteres entre la posición 3 y la posición 12):

```r
> substr("Mary has a little lamb.", start=3, stop=12)
[1] "ry has a l"
```

Si deseas reemplazar la primera instancia de un carácter por otro, puedes utilizar la función `sub` (en el ejemplo, se reemplaza "little" por "big"):

```r
> sub("little", "big", "Mary has a little lamb.")
[1] "Mary has a big lamb."
```

## Vectores

### Vectores en el lenguaje R

Un vector es un arreglo que contiene elementos del mismo tipo, y los miembros de un vector se llaman "componentes".

Aquí tienes un ejemplo de un vector (que contiene tres variables numéricas: `2`, `3` y `5`):

```r
> c(2, 3, 5)
[1] 2 3 5
```

También se pueden crear vectores con valores lógicos:

```r
> c(TRUE, FALSE, TRUE, FALSE, FALSE)
[1] TRUE FALSE TRUE FALSE FALSE
```

Y también se pueden crear vectores de caracteres:

```r
> c("aa", "bb", "cc", "dd", "ee")
[1] "aa" "bb" "cc" "dd" "ee"
```

Si deseas saber cuántos elementos contiene un vector, puedes utilizar la función `length`:
```

```r
> length(c("aa", "bb", "cc", "dd", "ee"))
[1] 5
```

### Concatenación de vectores

Si deseas combinar dos vectores, puedes utilizar la función `c`:

```r
> n = c(2, 3, 5)
> s = c("aa", "bb", "cc", "dd", "ee")
> c(n, s)
[1] "2"  "3"  "5"  "aa" "bb" "cc" "dd" "ee"
```

Ten en cuenta que en el ejemplo anterior, si combinas dos vectores con tipos de datos diferentes, el tipo resultante será el tipo más laxo (es decir, se realizará una conversión de tipo forzada desde un tipo más estricto a un tipo más relajado, como convertir valores numéricos a valores de caracteres).

### Operaciones básicas en vectores

Supongamos que tenemos dos vectores `a` y `b`:

```r
> a = c(1, 3, 5, 7)
> b = c(1, 2, 4, 8)
```

Aquí se muestran las operaciones básicas en vectores:

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

Si los vectores que se suman tienen una cantidad diferente de miembros, el resultado tendrá una longitud igual a la del vector más largo:

```r
> u = c(10, 20, 30)
> v = c(1, 2, 3, 4, 5, 6, 7, 8, 9)
> u + v
[1] 11 22 33 14 25 36 17 28 39
```

### Acceso a elementos en un vector

Para extraer elementos de un vector, puedes usar la notación de índices dentro de `[ ]`, es decir, `[número de miembro]`:

```r
> s = c("aa", "bb", "cc", "dd", "ee")
> s[3]  # Extrae el valor del tercer miembro y lo muestra
[1] "cc"
```

Si prefieres excluir un miembro específico, puedes usar un índice precedido por un signo negativo, por ejemplo, `[-3]`, lo que significa que se excluirá el tercer miembro y se mostrarán los demás:

```r
> s[-3]
[1] "aa" "bb" "dd" "ee"
```

Si el índice está fuera del rango del vector, se generará un error:

```r
> s[10]
[1] NA
```

【Actualización en curso】
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.