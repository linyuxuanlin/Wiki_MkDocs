# Definiciones de macros comunes en C y STM32

En el desarrollo de sistemas embebidos, existen algunas definiciones de macros comunes que pueden mejorar la compatibilidad y portabilidad del proyecto.

## Evitar la redefinición de archivos de cabecera

```c
#ifndef COMDEF_H
#define COMDEF_H

// Contenido del archivo de cabecera

#endif
```

## Definición de tipos de datos personalizados

Definir algunos tipos de datos personalizados para evitar diferencias en el número de bytes debido a las diferentes plataformas y compiladores. Esto también facilita la portabilidad.

```c
typedef unsigned char boolean; /* Tipo de valor booleano */
typedef unsigned long int uint32; /* Valor sin signo de 32 bits */
typedef unsigned short uint16; /* Valor sin signo de 16 bits */
typedef unsigned char uint8; /* Valor sin signo de 8 bits */
typedef signed long int int32; /* Valor con signo de 32 bits */
typedef signed short int16; /* Valor con signo de 16 bits */
typedef signed char int8; /* Valor con signo de 8 bits */
```

## Obtener un byte o palabra de una dirección específica

```c
#define MEM_B( x ) ( *( (byte *) (x) ) )
#define MEM_W( x ) ( *( (word *) (x) ) )
```

## Obtener el valor máximo / mínimo

```c
#define MAX( x, y ) ( ((x) > (y)) ? (x) : (y) )
#define MIN( x, y ) ( ((x) < (y)) ? (x) : (y) )
```

## Devolver el número de elementos de un arreglo

```c
#define ARR_SIZE( a ) ( sizeof( (a) ) / sizeof( (a[0]) ) )
```

## Convertir la primera letra en mayúscula

```c
#define UPCASE( c ) ( ((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c) )
```

## Verificar si un carácter es decimal

```c
#define DECCHK( c ) ((c) >= '0' && (c) <= '9')
```

## Verificar si un carácter es hexadecimal

```c
#define HEXCHK( c ) ( ((c) >= '0' && (c) <= '9') ||\
((c) >= 'A' && (c) <= 'F') ||\
((c) >= 'a' && (c) <= 'f') )
```

## Referencias y agradecimientos

- [Definiciones de macros comunes para ingenieros embebidos](https://mp.weixin.qq.com/s/4YPwxtBX6Qdlz9fGKvSCUg)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.