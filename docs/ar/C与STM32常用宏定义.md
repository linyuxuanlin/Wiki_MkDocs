# C 与 STM32 常用宏定义

في تطوير الأنظمة المضمنة ، هناك بعض التعريفات المشتركة التي يمكن أن تجعل المشروع أكثر توافقية وقابلية للنقل.

## منع إعادة تعريف الملف الرأسي

```c
#ifndef COMDEF_H
#define COMDEF_H

//محتوى الملف الرأسي

#endif
```

## تعريفات الأنواع المخصصة

تعريف بعض الأنواع المخصصة ، لمنع اختلاف عدد بايتات الأنواع بسبب اختلاف المنصات والمترجمات. وبالتالي يسهل النقل.

```c
typedef unsigned char boolean; /* نوع قيمة منطقية. */
typedef unsigned long int uint32; /* قيمة 32 بت غير موقعة */
typedef unsigned short uint16; /* قيمة 16 بت غير موقعة */
typedef unsigned char uint8; /* قيمة 8 بت غير موقعة */
typedef signed long int int32; /* قيمة 32 بت موقعة */
typedef signed short int16; /* قيمة 16 بت موقعة */
typedef signed char int8; /* قيمة 8 بت موقعة */
```

## الحصول على كلمة أو بايت محدد في عنوان محدد

```c
#define MEM_B( x ) ( *( (byte *) (x) ) )
#define MEM_W( x ) ( *( (word *) (x) ) )
```

## الحصول على الحد الأقصى / الحد الأدنى

```c
#define MAX( x, y ) ( ((x) > (y)) ? (x) : (y) )
#define MIN( x, y ) ( ((x) < (y)) ? (x) : (y) )
```

## العودة بعدد عناصر المصفوفة

```c
#define ARR_SIZE( a ) ( sizeof( (a) ) / sizeof( (a[0]) ) )
```

## تحويل الحرف الأول إلى حرف كبير

```c
#define UPCASE( c ) ( ((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c) )
```

## التحقق من الحرف إذا كان عشريًا

```c
#define DECCHK( c ) ((c) >= '0' && (c) <= '9')
```

## التحقق من الحرف إذا كان سداسي عشريًا

```c
#define HEXCHK( c ) ( ((c) >= '0' && (c) <= '9') ||\
((c) >= 'A' && (c) <= 'F') ||\
((c) >= 'a' && (c) <= 'f') )
```

## المراجع والشكر

- [تعريفات مهندسي الأنظمة المضمنة الشائعة](https://mp.weixin.qq.com/s/4YPwxtBX6Qdlz9fGKvSCUg)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.