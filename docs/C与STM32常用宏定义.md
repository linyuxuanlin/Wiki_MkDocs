---
id: C与STM32常用宏定义
title: C 与 STM32 常用宏定义
---

在嵌入式开发中，有些通用的宏定义，可以让项目兼容性和可移植性更佳。

## 防止头文件被重复定义

```c
#ifndef COMDEF_H
#define COMDEF_H

//头文件内容

#endif
```

## 自定义数据类型

自定义一些类型，防止由于各种平台和编译器的不同，而产生的类型字节数差异。这样也方便移植。

```c
typedef unsigned char boolean; /* Boolean value type. */
typedef unsigned long int uint32; /* Unsigned 32 bit value */
typedef unsigned short uint16; /* Unsigned 16 bit value */
typedef unsigned char uint8; /* Unsigned 8 bit value */
typedef signed long int int32; /* Signed 32 bit value */
typedef signed short int16; /* Signed 16 bit value */
typedef signed char int8; /* Signed 8 bit value */
```

## 获取指定地址上的一个字或字节

```c
#define MEM_B( x ) ( *( (byte *) (x) ) )
#define MEM_W( x ) ( *( (word *) (x) ) )
```

## 获取最大 / 最小值

```c
#define MAX( x, y ) ( ((x) > (y)) ? (x) : (y) )
#define MIN( x, y ) ( ((x) < (y)) ? (x) : (y) )
```

## 返回数组元素的个数

```c
#define ARR_SIZE( a ) ( sizeof( (a) ) / sizeof( (a[0]) ) )
```

## 将首字母转换为大写

```c
#define UPCASE( c ) ( ((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c) )
```

## 判断字符是否为十进制

```c
#define DECCHK( c ) ((c) >= '0' && (c) <= '9')
```

## 判断字符是否为十六进制

```c
#define HEXCHK( c ) ( ((c) >= '0' && (c) <= '9') ||\
((c) >= 'A' && (c) <= 'F') ||\
((c) >= 'a' && (c) <= 'f') )
```

## 参考与致谢

- [嵌入式工程师常用的宏定义](https://mp.weixin.qq.com/s/4YPwxtBX6Qdlz9fGKvSCUg)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
