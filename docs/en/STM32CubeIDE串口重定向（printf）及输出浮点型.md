# STM32CubeIDE Serial Port Redirection (printf) and Outputting Floating Point Numbers

## Redirecting printf to Serial Port

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

// The _write function is defined in syscalls.c using __weak, so it can be defined in other files directly
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
	int DataIdx;
	for (DataIdx = 0; DataIdx < len; DataIdx++)
	{
		  while ((USART1->SR & 0X40) == 0); // Wait until transmission is complete
		  USART1->DR = (uint8_t) *ptr++;
	}
	return len;
}

/* USER CODE END 1 */
```

## Outputting Floating Point Numbers in STM32CubeIDE

1. In the STM32CubeIDE sidebar, select the project, right-click and select `Properties` - `C/C++ Build` - `Settings` - `MCU GCC Linker` - `Miscellaneous`.
2. Add a new item in the `Other flags` section and enter `-u_printf_float`.
3. Recompile the project.

## HAL_UART_Receive_IT Garbled Data Issue

Change the word length (`10`) in `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10,0xFFFF);` to `1`.

## References and Acknowledgements

- [Implementing printf Redirect Output to Serial Port in STM32CubeIDE](https://blog.51cto.com/u_15353042/3751177)
- [Modifying printf Redirect and Serial Port (UART) Output of Floating Point Data in STM32CubeIDE](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [Questioning the HAL_UART_Receive_IT Function Again](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.