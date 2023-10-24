# كيفية قراءة وكتابة بت واحد

```c
#define BitVal(data,y) ( (data>>y) & 1)             // إرجاع قيمة Data.Y
#define SetBit(data,y)    data |= (1 << y)          // تعيين Data.Y إلى 1
#define ClearBit(data,y)  data &= ~(1 << y)         // مسح Data.Y وتعيينها إلى 0
#define TogleBit(data,y)     (data ^=BitVal(y))     // تبديل قيمة Data.Y
#define Togle(data)   (data =~data )                // تبديل قيمة Data
```

## المراجع والشكر

- [كيفية قراءة وكتابة بتات عشوائية في لغة C/C++](https://stackoverflow.com/questions/11815894/how-to-read-write-arbitrary-bits-in-c-c)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.