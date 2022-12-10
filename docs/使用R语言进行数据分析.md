---
id: 使用R语言进行数据分析
title: 使用 R 语言进行数据分析
---

## 软件安装

- [**R-software**](https://cran.r-project.org/)
  - 如果是在 Windows 上使用，请在网站主页点击 `Download R for Windows`，然后点击 `install R for the first time`，最后点击 `Download R 4.0.4 for Windows`，下载软件后请自行完成安装。
  - R 语言支持软件仅在后台运行，没有图形化界面。
- [**RStudio**](https://rstudio.com/products/rstudio/download/#download)
  - 直接点击蓝色的 `Download` 按钮，或者在页面下方选择其他系统版本下载。下载软件后请自行完成安装。

## 教学资源

### 在线资源（推荐）

- [R-tutorial](http://www.r-tutor.com/r-introduction)
- [零基础学 R 语言](https://bookdown.org/qiyuandong/intro_r/)

### 书籍

- [The R-book](https://www.cs.upc.edu/~robert/teaching/estadistica/TheRBook.pdf)
- [R for Data Science](https://r4ds.had.co.nz/index.html)

## 基本数据类型

R 语言的数据类型，主要有以下这几种：

- **数值型（numerics）**
- **整数型（integer）**
- **复数型（complex）**
- **逻辑型（logical）**
- **字符型（characters）**

### 数值型（numerics）

数值型是 R 语言中最基本的数据类型。当我们把一个数字值赋给变量，那变量的类型就是数值型：

```r
> x = 11.15       # 把 11.15 这个数值赋给变量 x
> x              # 输出出 x 的值
[1] 11.15
> class(x)       # 输出 x 的类型
[1] "numeric"
```

整数或小数都可以是数值型变量。但如果按照以上的方法创建，那么整数变量也会被视为小数变量。

### 整数型（integer）

如果要创建整数型变量，就得使用函数 `is.integer`：

```r
> y = as.integer(3)
> y              # 输出 y 的值
[1] 3
> class(y)       # 输出 y 的类型
[1] "integer"
> is.integer(y)  # y 是否为整数？
[1] TRUE
```

除了使用 `is.integer` 函数，你也可以附加 `L` 后缀来实现：

```r
> y = 3L
> is.integer(y)  # y 是否为整数？
[1] TRUE
```

如果要对小数进行取整，我们可以使用函数 `as.integer`：

```r
> as.integer(3.14)    # 对变量进行强制数值转换
[1] 3
```

也可以对字符串类型进行解析并取整：

```r
> as.integer("5.27")  # 对变量进行强制数值转换
[1] 5
```

但如果解析的字符串不是数值，那就会出错：

```r
> as.integer("Joe")   # 解析一个非数值型的字符串
[1] NA
Warning message:
NAs introduced by coercion
```

R 语言像 C 语言一样，把整数 `1` `0` 与逻辑 `TRUE` `FALSE`对应了起来：

```r
> as.integer(TRUE)    # TRUE 的数值型变量
[1] 1
> as.integer(FALSE)   # FALSE 的数值型变量
[1] 0
```

### 复数型（complex）

在 R 语言中，复数变量通过 `i` 来定义：

```r
> z = 1 + 2i     # 创建一个复数变量 z
> z              # 输出 z 的值
[1] 1+2i
> class(z)       # 输出 z 的类型
[1] "complex"
```

如果我们单纯对 `-1` 开方，那将会出错：

```r
> sqrt(−1)       # 对 -1 开方
[1] NaN
Warning message:
In sqrt(−1) : NaNs produced
```

但是对复数 `−1+0i` 开方，那就没问题：

```r
> sqrt(−1+0i)    # 对 −1+0i 开方
[1] 0+1i
```

也可以用强制类型转换来进行运算：

```r
> sqrt(as.complex(−1))
[1] 0+1i
```

### 逻辑型（logical）

逻辑型通常通过比较变量而产生：

```r
> x = 1; y = 2   # 样本变量
> z = x > y      # x 比 y 大吗？
> z              # 输出逻辑变量
[1] FALSE
> class(z)       # 输出 z 的类型
[1] "logical"
```

基本逻辑操作有 `&`（与），`|`（或）, `!`（非）：

```r
> u = TRUE; v = FALSE
> u & v          # 对 u，v 进行 "与" 运算
[1] FALSE
> u | v          # 对 u，v 进行 "或" 运算
[1] TRUE
> !u             # 对 u 进行 "非" 运算
[1] FALSE
```

### 字符型（character）

字符型可通过函数 `as.character` 进行强制类型转换得到：

```r
> x = as.character(3.14)
> x              # 输出字符串
[1] "3.14"
> class(x)       # 输出 x 的类型
[1] "character"
```

要合并两个字符型变量，可以使用函数 `paste`：

```r
> fname = "Joe"; lname ="Smith"
> paste(fname, lname)
[1] "Joe Smith"
```

像 C 语法一样，可以用格式输出以增加可读性，用函数 `sprintf` 即可：

```r
> sprintf("%s has %d dollars", "Sam", 100)
[1] "Sam has 100 dollars"
```

如果要从字符串中提取子串，可以使用函数 `substr`（示例中把第 `3` 到第 `12` 个字符之间的字符截取了下来）：

```r
> substr("Mary has a little lamb.", start=3, stop=12)
[1] "ry has a l"
```

如果要把第一个遇见的字符替换成另外一个，可以使用函数 `sub`（示例中把 `little` 替换成了 `big`）：

```r
> sub("little", "big", "Mary has a little lamb.")
[1] "Mary has a big lamb."
```

## 向量

### R 语言中的向量

向量是一个包含相同类型元素的数组，向量中的成员被官方称为 components。

以下是一个示例向量（包含三个数值变量 `2` `3` `5`）：

```r
> c(2, 3, 5)
[1] 2 3 5
```

也可以全部由逻辑型构成：

```r
> c(TRUE, FALSE, TRUE, FALSE, FALSE)
[1] TRUE FALSE TRUE FALSE FALSE
```

也可以由字符型构成：

```r
> c("aa", "bb", "cc", "dd", "ee")
[1] "aa" "bb" "cc" "dd" "ee"
```

如果想知道一个向量内有多少个成员，可以使用函数 `length`：

```r
> length(c("aa", "bb", "cc", "dd", "ee"))
[1] 5
```

### 合并向量

如果要合并两个向量，可以使用函数 `c`：

```r
> n = c(2, 3, 5)
> s = c("aa", "bb", "cc", "dd", "ee")
> c(n, s)
[1] "2"  "3"  "5"  "aa" "bb" "cc" "dd" "ee"
```

注意在上面的例子中，如果合并两个不同数据类型的向量，那合并后的类型将会是向下兼容的（即将比较严格的类型，进行强制类型转换为比较宽松的类型，例如将数值型变成字符型）

### 向量基本运算

我们先假定两个向量 `a` `b`：

```r
> a = c(1, 3, 5, 7)
> b = c(1, 2, 4, 8)
```

以下就是向量的基本运算：

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

如果相加的两个向量成员数量不一致，那么结果将会向下兼容，即输出变量的长度取决于较长的那个：

```r
> u = c(10, 20, 30)
> v = c(1, 2, 3, 4, 5, 6, 7, 8, 9)
> u + v
[1] 11 22 33 14 25 36 17 28 39
```

### 检索向量

如果要从向量中取出成员，可以使用在 `[ ]` 中声明索引的方法，也就是 `[第几个成员]` ：

```r
> s = c("aa", "bb", "cc", "dd", "ee")
> s[3]  # 取出第三个成员的值并输出
[1] "cc"
```

如果索引前加一个负号，比如 `[-3]`，就意味着取出除第三个成员外的其他成员：

```r
> s[-3]
[1] "aa" "bb" "dd" "ee"
```

如果索引超出了向量的长度，那就会报错：

```r
> s[10]
[1] NA
```

【更新中】
