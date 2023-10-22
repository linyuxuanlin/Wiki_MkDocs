```markdown
# Definiciones de macros comunes en C para STM32

En el desarrollo de sistemas embebidos, es importante utilizar definiciones de macros comunes que mejoren la compatibilidad y portabilidad del proyecto.

## Evitar la definición repetida de archivos de encabezado

```c
#ifndef COMDEF_H
#define COMDEF_H

// Contenido del archivo de encabezado

#endif
```

## Tipos de datos personalizados

Es conveniente definir tipos de datos personalizados para evitar discrepancias en la cantidad de bytes de tipos de datos debido a diferencias entre plataformas y compiladores. Esto facilita la portabilidad del código.

```c
typedef unsigned char boolean; /* Tipo de valor booleano */
typedef unsigned long int uint32; /* Valor sin signo de 32 bits */
typedef unsigned short uint16; /* Valor sin signo de 16 bits */
typedef unsigned char uint8; /* Valor sin signo de 8 bits */
typedef signed long int int32; /* Valor con signo de 32 bits */
typedef signed short int16; /* Valor con signo de 16 bits */
typedef signed char int8; /* Valor con signo de 8 bits */
```

## Obtener un byte o palabra en una dirección específica

```c
#define MEM_B( x ) ( *( (byte *) (x) ) )
#define MEM_W( x ) ( *( (word *) (x) ) )
```

## Obtener el valor máximo / mínimo

```c
#define MAX( x, y ) ( ((x) > (y)) ? (x) : (y) )
#define MIN( x, y ) ( ((x) < (y)) ? (x) : (y) )
```

## Calcular el tamaño de un arreglo

```c
#define ARR_SIZE( a ) ( sizeof( (a) ) / sizeof( (a[0]) ) )
```

## Convertir la primera letra a mayúscula

```c
#define UPCASE( c ) ( ((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c) )
```

## Verificar si un carácter es un dígito decimal

```c
#define DECCHK( c ) ((c) >= '0' && (c) <= '9')
```

## Verificar si un carácter es un dígito hexadecimal

```c
#define HEXCHK( c ) ( ((c) >= '0' && (c) <= '9') ||\
((c) >= 'A' && (c) <= 'F') ||\
((c) >= 'a' and (c) <= 'f') )
```

## Referencias y Agradecimientos

- [Common Macros for Embedded Engineers](https://mp.weixin.qq.com/s/4YPwxtBX6Qdlz9fGKvSCUg)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.