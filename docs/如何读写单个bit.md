---
id: 如何读写单个bit
title: 如何读写单个 bit
---

```c
#define BitVal(data,y) ( (data>>y) & 1)             // Return Data.Y value
#define SetBit(data,y)    data |= (1 << y)          // Set Data.Y to 1
#define ClearBit(data,y)  data &= ~(1 << y)         // Clear Data.Y to 0
#define TogleBit(data,y)     (data ^=BitVal(y))     // Togle Data.Y value
#define Togle(data)   (data =~data )                // Togle Data value
```

## 参考与致谢

- [How to read/write arbitrary bits in C/C++](https://stackoverflow.com/questions/11815894/how-to-read-write-arbitrary-bits-in-c-c)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

