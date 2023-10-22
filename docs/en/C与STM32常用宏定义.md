# Common Macro Definitions in C for STM32

In embedded development, utilizing common macro definitions can enhance project compatibility and portability across various platforms.

## Prevent Header Files from Being Redefined

```c
#ifndef COMDEF_H
#define COMDEF_H

// Header file contents

#endif
```

## Custom Data Types

Defining custom data types is essential to ensure consistency in the byte sizes of types across different platforms and compilers. This approach also facilitates portability.

```c
typedef unsigned char boolean; /* Boolean value type. */
typedef unsigned long int uint32; /* Unsigned 32-bit value */
typedef unsigned short uint16; /* Unsigned 16-bit value */
typedef unsigned char uint8; /* Unsigned 8-bit value */
typedef signed long int int32; /* Signed 32-bit value */
typedef signed short int16; /* Signed 16-bit value */
typedef signed char int8; /* Signed 8-bit value */
```

## Accessing a Word or Byte at a Specified Address

```c
#define MEM_B(x) (*(byte *)(x))
#define MEM_W(x) (*(word *)(x))
```

## Finding the Maximum / Minimum Value

```c
#define MAX(x, y) (((x) > (y)) ? (x) : (y))
#define MIN(x, y) (((x) < (y)) ? (x) : (y))
```

## Determining the Number of Elements in an Array

```c
#define ARR_SIZE(a) (sizeof(a) / sizeof(a[0]))
```

## Converting the First Letter to Uppercase

```c
#define UPCASE(c) (((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c))
```

## Checking if a Character is a Decimal Digit

```c
#define DECCHK(c) ((c) >= '0' && (c) <= '9')
```

## Checking if a Character is a Hexadecimal Digit

```c
#define HEXCHK(c) (((c) >= '0' && (c) <= '9') ||\
((c) >= 'A' && (c) <= 'F') ||\
((c) >= 'a' && (c) <= 'f'))
```

## References and Acknowledgments

- [Common Macro Definitions for Embedded Engineers](https://mp.weixin.qq.com/s/4YPwxtBX6Qdlz9fGKvSCUg)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.