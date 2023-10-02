# Data Analysis with R Language

## Software Installation

- [**R-software**](https://cran.r-project.org/)
  - If you are using Windows, click on `Download R for Windows` on the homepage, then click on `install R for the first time`, and finally click on `Download R 4.0.4 for Windows`. After downloading the software, please complete the installation yourself.
  - R language support software only runs in the background and has no graphical interface.
- [**RStudio**](https://rstudio.com/products/rstudio/download/#download)
  - Click on the blue `Download` button directly, or select other system versions to download at the bottom of the page. After downloading the software, please complete the installation yourself.

## Teaching Resources

### Online Resources (Recommended)

- [R-tutorial](http://www.r-tutor.com/r-introduction)
- [Learn R Language from Scratch](https://bookdown.org/qiyuandong/intro_r/)

### Books

- [The R-book](https://www.cs.upc.edu/~robert/teaching/estadistica/TheRBook.pdf)
- [R for Data Science](https://r4ds.had.co.nz/index.html)

## Basic Data Types

R language has the following main data types:

- **Numeric**
- **Integer**
- **Complex**
- **Logical**
- **Character**

### Numeric

Numeric is the most basic data type in R language. When we assign a numeric value to a variable, the variable's type is numeric:

```r
> x = 11.15       # Assign the numeric value 11.15 to variable x
> x              # Output the value of x
[1] 11.15
> class(x)       # Output the type of x
[1] "numeric"
```

Integers or decimals can both be numeric variables. But if created using the above method, integer variables will also be treated as decimal variables.

### Integer

To create an integer variable, you need to use the `is.integer` function:

```r
> y = as.integer(3)
> y              # Output the value of y
[1] 3
> class(y)       # Output the type of y
[1] "integer"
> is.integer(y)  # Is y an integer?
[1] TRUE
```

In addition to using the `is.integer` function, you can also add the `L` suffix to achieve this:

```r
> y = 3L
> is.integer(y)  # Is y an integer?
[1] TRUE
```

If you want to round a decimal, you can use the `as.integer` function:

```r
> as.integer(3.14)    # Force variable conversion to numeric
[1] 3
```

You can also parse and round string types:

```r
> as.integer("5.27")  # Force variable conversion to numeric
[1] 5
```

But if the parsed string is not a number, an error will occur:

```r
> as.integer("Joe")   # Parse a non-numeric string
[1] NA
Warning message:
NAs introduced by coercion
```

Like C language, R language also corresponds integer `1` `0` to logical `TRUE` `FALSE`:

```r
> as.integer(TRUE)    # Numeric variable of TRUE
[1] 1
> as.integer(FALSE)   # Numeric variable of FALSE
[1] 0
```

### Complex

In R language, complex variables are defined using `i`:

```r
> z = 3 + 4i        # Define a complex variable
> z                # Output the value of z
[1] 3+4i
> class(z)         # Output the type of z
[1] "complex"
```

# Basic Data Types in R

## Numeric

Numeric data types in R are used to represent real numbers. They can be created using the following syntax:

```r
> x = 3.14     # create a numeric variable x
> x           # print the value of x
[1] 3.14
> class(x)    # print the type of x
[1] "numeric"
```

Basic arithmetic operations can be performed on numeric variables:

```r
> x + 2       # addition
[1] 5.14
> x - 1       # subtraction
[1] 2.14
> x * 3       # multiplication
[1] 9.42
> x / 2       # division
[1] 1.57
> x ^ 2       # exponentiation
[1] 9.8596
```

## Integer

Integer data types in R are used to represent whole numbers. They can be created using the following syntax:

```r
> y = 5L      # create an integer variable y
> y           # print the value of y
[1] 5
> class(y)    # print the type of y
[1] "integer"
```

Basic arithmetic operations can also be performed on integer variables.

## Complex

Complex data types in R are used to represent complex numbers. They can be created using the following syntax:

```r
> z = 1 + 2i     # create a complex variable z
> z              # print the value of z
[1] 1+2i
> class(z)       # print the type of z
[1] "complex"
```

If we try to take the square root of -1, we will get an error:

```r
> sqrt(-1)       # square root of -1
[1] NaN
Warning message:
In sqrt(-1) : NaNs produced
```

However, if we take the square root of the complex number -1+0i, we get a result:

```r
> sqrt(-1+0i)    # square root of -1+0i
[1] 0+1i
```

We can also perform operations on -1 by converting it to a complex number:

```r
> sqrt(as.complex(-1))
[1] 0+1i
```

## Logical

Logical data types in R are used to represent boolean values (TRUE or FALSE). They can be created by comparing variables:

```r
> x = 1; y = 2   # sample variables
> z = x > y      # is x greater than y?
> z              # print the logical variable
[1] FALSE
> class(z)       # print the type of z
[1] "logical"
```

Basic logical operations include `&` (and), `|` (or), and `!` (not):

```r
> u = TRUE; v = FALSE
> u & v          # and operation on u and v
[1] FALSE
> u | v          # or operation on u and v
[1] TRUE
> !u             # not operation on u
[1] FALSE
```

## Character

Character data types in R are used to represent strings. They can be created by using the `as.character` function:

```r
> x = as.character(3.14)
> x              # print the string
[1] "3.14"
> class(x)       # print the type of x
[1] "character"
```

To concatenate two character variables, we can use the `paste` function:

```r
> fname = "Joe"; lname ="Smith"
> paste(fname, lname)
[1] "Joe Smith"
```

We can also use formatted output for readability, using the `sprintf` function:

```r
> sprintf("%s has %d dollars", "Sam", 100)
[1] "Sam has 100 dollars"
```

To extract a substring from a string, we can use the `substr` function (in this example, we extract the characters between the 3rd and 12th positions):

```r
> substr("Mary has a little lamb.", start=3, stop=12)
[1] "ry has a l"
```

To replace the first occurrence of a character in a string, we can use the `sub` function (in this example, we replace "little" with "big"):

```r
> sub("little", "big", "Mary has a little lamb.")
[1] "Mary has a big lamb."
```

## Vectors

### Vectors in R

A vector in R is an array of elements of the same type, called components. Here is an example vector (containing three numeric variables 2, 3, 5):

```r
> c(2, 3, 5)
[1] 2 3 5
```

Vectors can also be composed entirely of logical or character variables:

```r
> c(TRUE, FALSE, TRUE, FALSE, FALSE)
[1] TRUE FALSE TRUE FALSE FALSE

> c("aa", "bb", "cc", "dd", "ee")
[1] "aa" "bb" "cc" "dd" "ee"
```

To find out how many elements are in a vector, we can use the `length` function:

```r
> length(c("aa", "bb", "cc", "dd", "ee"))
[1] 5
```

### Merging Vectors

To merge two vectors, you can use the `c` function:

```r
> n = c(2, 3, 5)
> s = c("aa", "bb", "cc", "dd", "ee")
> c(n, s)
[1] "2"  "3"  "5"  "aa" "bb" "cc" "dd" "ee"
```

Note that in the example above, if you merge two vectors of different data types, the resulting type will be downward compatible (i.e., the stricter type is forced to be converted to the looser type, such as converting numeric to character).

### Basic Vector Operations

Let's assume two vectors `a` and `b`:

```r
> a = c(1, 3, 5, 7)
> b = c(1, 2, 4, 8)
```

The following are basic vector operations:

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

If the number of members to be added in the two vectors is not the same, the result will be downward compatible, i.e., the length of the output variable depends on the longer one:

```r
> u = c(10, 20, 30)
> v = c(1, 2, 3, 4, 5, 6, 7, 8, 9)
> u + v
[1] 11 22 33 14 25 36 17 28 39
```

### Retrieving Vectors

To retrieve a member from a vector, you can use the method of declaring an index in `[ ]`, i.e., `[which member]`:

```r
> s = c("aa", "bb", "cc", "dd", "ee")
> s[3]  # retrieve the value of the third member and output it
[1] "cc"
```

If a negative sign is added before the index, such as `[-3]`, it means to retrieve all members except the third one:

```r
> s[-3]
[1] "aa" "bb" "dd" "ee"
```

If the index exceeds the length of the vector, an error will be reported:

```r
> s[10]
[1] NA
```

[Updating]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.