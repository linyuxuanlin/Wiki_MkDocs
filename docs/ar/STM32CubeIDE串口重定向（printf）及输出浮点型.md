# إعادة توجيه المنافذ التسلسلية (printf) وإخراج أرقام عشرية في STM32CubeIDE

## إعادة توجيه printf إلى المنفذ التسلسلي (Serial Port)

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

// The _write function is defined in syscalls.c using __weak, so it can be redefined in other files directly
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
	int DataIdx;
	for (DataIdx = 0; DataIdx < len; DataIdx++)
	{
		  while ((USART1->SR & 0X40) == 0); //wait until transmit data register is empty
		  USART1->DR = (uint8_t) *ptr++;
	}
	return len;
}

/* USER CODE END 1 */
```

## إخراج أرقام عشرية على المنفذ التسلسلي في STM32CubeIDE

1. في الشريط الجانبي لـ STM32CubeIDE ، حدد المشروع ، انقر بزر الماوس الأيمن واختر `Properties` - `C/C++ Build` - `Settings` - `MCU GCC Linker` - `Miscellaneous`.
2. في خانة `Other flags` ، أضف مشروعًا واحدًا ، واملأ `-u_printf_float`.
3. أعد الترميز.

## HAL_UART_Receive_IT مشكلة الرموز العشوائية

قم بتغيير طول الكلمة (`10`) في `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10,0xFFFF);` إلى `1`.

## المراجع والشكر

- [توجيه إخراج printf إلى المنفذ التسلسلي في STM32CubeIDE](https://blog.51cto.com/u_15353042/3751177)
- [تعديل إخراج أرقام عشرية في STM32CubeIDE printf إعادة التوجيه وإخراج عبر المنفذ التسلسلي (UART)](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [الشكوك المستمرة بخصوص دالة HAL_UART_Receive_IT](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> عنوان النص: <https://wiki-power.com/>  
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.