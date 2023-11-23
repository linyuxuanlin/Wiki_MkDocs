# How to Read and Write Individual Bits

```c
#define BitVal(data,y) ( (data>>y) & 1)             // Return Data.Y value
#define SetBit(data,y)    data |= (1 << y)          // Set Data.Y to 1
#define ClearBit(data,y)  data &= ~(1 << y)         // Clear Data.Y to 0
#define TogleBit(data,y)     (data ^=BitVal(y))     // Toggle Data.Y value
#define Togle(data)   (data =~data )                // Toggle Data value
```

## References and Acknowledgements

- [How to read/write arbitrary bits in C/C++](https://stackoverflow.com/questions/11815894/how-to-read-write-arbitrary-bits-in-c-c)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.