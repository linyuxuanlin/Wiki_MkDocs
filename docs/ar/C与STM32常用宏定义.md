# تعريفات الماكروالشائعة في لغة السي و المستخدمة في STM32

في تطوير الأنظمة المضمنة ، هناك بعض التعريفات الماكروية العامة التي يمكن أن تجعل المشروع أكثر توافقية وقابلية للنقل.

## تجنب تعريف الملف الرأسي بشكل متكرر

```c
#ifndef COMDEF_H
#define COMDEF_H

//محتوى الملف الرأسي

#endif
```

## تعريفات الأنواع المخصصة

تعريف بعض الأنواع المخصصة ، لتجنب اختلاف عدد بايتات الأنواع بسبب اختلاف المنصات والمترجمات. وبهذه الطريقة يسهل النقل.

```c
typedef unsigned char boolean; /* نوع القيمة الثنائية الصحيحة. */
typedef unsigned long int uint32; /* قيمة غير موقعة بـ 32 بت */
typedef unsigned short uint16; /* قيمة غير موقعة بـ 16 بت */
typedef unsigned char uint8; /* قيمة غير موقعة بـ 8 بت */
typedef signed long int int32; /* قيمة موقعة بـ 32 بت */
typedef signed short int16; /* قيمة موقعة بـ 16 بت */
typedef signed char int8; /* قيمة موقعة بـ 8 بت */
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

## إرجاع عدد عناصر المصفوفة

```c
#define ARR_SIZE( a ) ( sizeof( (a) ) / sizeof( (a[0]) ) )
```

## تحويل الحرف الأول إلى حرف كبير

```c
#define UPCASE( c ) ( ((c) >= 'a' && (c) <= 'z') ? ((c) - 0x20) : (c) )
```

## التحقق من أن الحرف عشري

```c
#define DECCHK( c ) ((c) >= '0' && (c) <= '9')
```

## التحقق من أن الحرف سداسي عشري

```c
#define HEXCHK( c ) ( ((c) >= '0' && (c) <= '9') ||\
((c) >= 'A' && (c) <= 'F') ||\
((c) >= 'a' && (c) <= 'f') )
```

## المراجع والشكر

- [تعريفات الماكرو الشائعة لمهندسي الأنظمة المضمنة](https://mp.weixin.qq.com/s/4YPwxtBX6Qdlz9fGKvSCUg)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.