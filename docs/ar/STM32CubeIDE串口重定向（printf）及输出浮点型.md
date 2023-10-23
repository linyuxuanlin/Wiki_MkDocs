# إعادة توجيه STM32CubeIDE للطباعة (printf) وإخراج الأعداد العشرية

## إعادة توجيه printf إلى المنفذ التسلسلي

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

// تعريف _write يوجد في syscalls.c وهو معرف باستخدام __weak، لذلك يمكن تعريفه مباشرة في ملفات أخرى
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
    int DataIdx;
    for (DataIdx = 0; DataIdx < len; DataIdx++)
    {
        while ((USART1->SR & 0X40) == 0); // انتظار الانتهاء من الإرسال
        USART1->DR = (uint8_t) *ptr++;
    }
    return len;
}

/* USER CODE END 1 */
```

## إخراج الأعداد العشرية في STM32CubeIDE

1. في الشريط الجانبي لبرنامج STM32CubeIDE، حدد المشروع، ثم انقر بزر الماوس الأيمن واختر "خصائص" - "بنية C/C++" - "الإعدادات" - "MCU GCC Linker" - "متفرقات".
2. في خانة "Other flags"، قم بإضافة مشروع جديد واكتب "-u_printf_float".
3. قم بإعادة الترجمة.

## مشكلة الأحرف العشوائية في HAL_UART_Receive_IT

يمكن حل مشكلة الأحرف العشوائية في `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10, 0xFFFF);` عن طريق تغيير عدد البايتات (10) إلى 1.

## المراجع والشكر

- [توجيه إخراج printf في STM32CubeIDE إلى المنفذ التسلسلي](https://blog.51cto.com/u_15353042/3751177)
- [تغيير إخراج الأعداد العشرية في STM32CubeIDE printf والمنفذ التسلسلي (uart)](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [الشكوك مجدداً بخصوص وظيفة HAL_UART_Receive_IT](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.