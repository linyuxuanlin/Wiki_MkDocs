# How to Read and Write a Single Bit

```c
#define BitVal(data,y) ( (data>>y) & 1)             // Return Data.Y value
#define SetBit(data,y)    data |= (1 << y)          // Set Data.Y to 1
#define ClearBit(data,y)  data &= ~(1 << y)         // Clear Data.Y to 0
#define TogleBit(data,y)     (data ^=BitVal(y))     // Toggle Data.Y value
#define Togle(data)   (data =~data )                // Toggle Data value
```

## References and Acknowledgements

- [How to read/write arbitrary bits in C/C++](https://stackoverflow.com/questions/11815894/how-to-read-write-arbitrary-bits-in-c-c++)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.