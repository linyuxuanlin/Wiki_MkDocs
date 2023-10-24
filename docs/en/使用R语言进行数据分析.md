# Using R for Data Analysis

## Software Installation

- [**R-software**](https://cran.r-project.org/)
  - If you are using Windows, please go to the website's homepage, click on `Download R for Windows`, then click on `install R for the first time`, and finally click on `Download R 4.0.4 for Windows`. After downloading the software, please proceed with the installation.
  - R language is command-line software with no graphical interface.

- [**RStudio**](https://rstudio.com/products/rstudio/download/#download)
  - Simply click the blue `Download` button, or choose other system versions from the options at the bottom of the page. After downloading the software, please complete the installation on your own.

## Learning Resources

### Online Resources (Recommended)

- [R-tutorial](http://www.r-tutor.com/r-introduction)
- [Learn R Language from Scratch](https://bookdown.org/qiyuandong/intro_r/)

### Books

- [The R-book](https://www.cs.upc.edu/~robert/teaching/estadistica/TheRBook.pdf)
- [R for Data Science](https://r4ds.had.co.nz/index.html)

## Basic Data Types

R language has several fundamental data types:

- **Numeric**
- **Integer**
- **Complex**
- **Logical**
- **Character**

### Numeric

Numeric is the most basic data type in R. When we assign a numeric value to a variable, the variable's type becomes numeric:

```r
> x = 11.15       # Assign the numeric value 11.15 to variable x
> x              # Output the value of x
[1] 11.15
> class(x)       # Output the type of x
[1] "numeric"
```

Both integers and decimals can be numeric variables. However, if you create them as shown above, integer variables will also be considered decimal variables.

### Integer

To create an integer variable, you need to use the `as.integer` function:

```r
> y = as.integer(3)
> y              # Output the value of y
[1] 3
> class(y)       # Output the type of y
[1] "integer"
> is.integer(y)  # Is y an integer?
[1] TRUE
```

Apart from using the `is.integer` function, you can also append the `L` suffix to achieve the same:

```r
> y = 3L
> is.integer(y)  # Is y an integer?
[1] TRUE
```

To round a decimal to an integer, you can use the `as.integer` function:

```r
> as.integer(3.14)    # Forceful type conversion of a variable
[1] 3
```

You can also parse and round a string:

```r
> as.integer("5.27")  # Forceful type conversion of a variable
[1] 5
```

However, if the parsed string is not a numeric value, it will result in an error:

```r
> as.integer("Joe")   # Parsing a non-numeric string
[1] NA
Warning message:
NAs introduced by coercion
```

R language, like C language, maps integers `1` and `0` to logical values `TRUE` and `FALSE`:

```r
> as.integer(TRUE)    # Numeric variable for TRUE
[1] 1
> as.integer(FALSE)   # Numeric variable for FALSE
[1] 0
```

### Complex

In R language, complex variables are defined using `i`:



```r
> v = c(1, 2, 3, 4, 5)
> length(v)      # 获取向量的长度
[1] 5
```

向量的元素可以通过索引访问，索引从 `1` 开始：

```r
> v[1]          # 获取第一个元素
[1] 1
> v[3]          # 获取第三个元素
[1] 3
```

要创建一个序列，可以使用 `:` 操作符：

```r
> 1:5           # 创建一个从 1 到 5 的整数序列
[1] 1 2 3 4 5
```

向量可以进行逐元素运算，如加法、减法、乘法和除法：

```r
> x = c(1, 2, 3)
> y = c(4, 5, 6)
> x + y          # 逐元素相加
[1] 5 7 9
> x - y          # 逐元素相减
[1] -3 -3 -3
> x * y          # 逐元素相乘
[1] 4 10 18
> x / y          # 逐元素相除
[1] 0.25 0.4 0.5
```

逐元素运算也适用于逻辑型向量：

```r
> u = c(TRUE, FALSE, TRUE)
> v = c(FALSE, TRUE, FALSE)
> u & v          # 逐元素逻辑与运算
[1] FALSE FALSE FALSE
> u | v          # 逐元素逻辑或运算
[1] TRUE TRUE TRUE
```

### 向量的命名

可以给向量的每个元素起一个名字，以便更好地理解和操作：

```r
> v = c(a=1, b=2, c=3)
> v
a b c 
1 2 3
```

要访问具体的元素，可以使用名字：

```r
> v["b"]
b 
2 
```

也可以使用索引：

```r
> v[2]
b 
2 
```

### 向量的切片

可以通过索引范围来获取向量的子集，这称为切片：

```r
> x = c(1, 2, 3, 4, 5)
> x[2:4]         # 获取第二到第四个元素
[1] 2 3 4
```

### 向量的拼接

可以将两个向量拼接成一个：

```r
> a = c(1, 2, 3)
> b = c(4, 5, 6)
> c(a, b)        # 拼接 a 和 b
[1] 1 2 3 4 5 6
```

### 向量的重复

可以用 `rep` 函数来重复一个向量：

```r
> x = c(1, 2, 3)
> rep(x, times=3)  # 重复 x 三次
[1] 1 2 3 1 2 3 1 2 3
```

也可以指定每个元素的重复次数：

```r
> rep(x, each=2)   # 每个元素重复两次
[1] 1 1 2 2 3 3
```

### 向量的排序

可以使用 `sort` 函数对向量进行排序：

```r
> x = c(5, 1, 3, 2, 4)
> sort(x)          # 升序排序
[1] 1 2 3 4 5
> sort(x, decreasing=TRUE)  # 降序排序
[1] 5 4 3 2 1
```

### 向量的筛选

可以使用逻辑型向量来筛选向量中的元素，只保留满足条件的元素：

```r
> x = c(1, 2, 3, 4, 5)
> x[x > 2]  # 保留大于 2 的元素
[1] 3 4 5
```

这是 R 语言中向量的基本操作，它们在数据分析和处理中非常常用。

```r
> length(c("aa", "bb", "cc", "dd", "ee"))
[1] 5
```

### Combining Vectors

To combine two vectors, you can use the `c` function:

```r
> n = c(2, 3, 5)
> s = c("aa", "bb", "cc", "dd", "ee")
> c(n, s)
[1] "2"  "3"  "5"  "aa" "bb" "cc" "dd" "ee"
```

Please note that in the above example, when combining two vectors of different data types, the resulting vector will be of the more permissive type (i.e., it coerces to the least restrictive type, such as converting numeric to character).

### Basic Vector Operations

Let's assume we have two vectors, `a` and `b`:

```r
> a = c(1, 3, 5, 7)
> b = c(1, 2, 4, 8)
```

Here are some basic operations on vectors:

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

If the vectors being added do not have the same number of elements, the result will be of a length equal to the longer vector:

```r
> u = c(10, 20, 30)
> v = c(1, 2, 3, 4, 5, 6, 7, 8, 9)
> u + v
[1] 11 22 33 14 25 36 17 28 39
```

### Accessing Vectors

To retrieve elements from a vector, you can use square brackets `[ ]` with an index specifying which element to access, like `[index]`:

```r
> s = c("aa", "bb", "cc", "dd", "ee")
> s[3]  # Retrieve and print the value of the third element
[1] "cc"
```

If you put a negative sign before the index, such as `[-3]`, it means you want to exclude the third element and retrieve the rest:

```r
> s[-3]
[1] "aa" "bb" "dd" "ee"
```

If the index exceeds the length of the vector, it will result in an error:

```r
> s[10]
[1] NA
```

[Updating...]
```

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.