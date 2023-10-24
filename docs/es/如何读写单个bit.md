# Cómo leer y escribir un solo bit

```c
#define BitVal(data,y) ( (data>>y) & 1)             // Devuelve el valor de Data.Y
#define SetBit(data,y)    data |= (1 << y)          // Establece Data.Y en 1
#define ClearBit(data,y)  data &= ~(1 << y)         // Establece Data.Y en 0
#define TogleBit(data,y)     (data ^=BitVal(y))     // Invierte el valor de Data.Y
#define Togle(data)   (data =~data )                // Invierte el valor de Data
```

## Referencias y agradecimientos

- [Cómo leer/escribir bits arbitrarios en C/C++](https://stackoverflow.com/questions/11815894/how-to-read-write-arbitrary-bits-in-c-c)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.