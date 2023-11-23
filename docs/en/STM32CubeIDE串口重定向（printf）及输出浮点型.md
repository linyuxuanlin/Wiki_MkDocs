# Redirecting printf to UART in STM32CubeIDE and Printing Floating-Point Numbers

## Redirecting printf to UART

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

// The _write function is defined in syscalls.c using __weak, allowing you to define it in other files.
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
    int DataIdx;
    for (DataIdx = 0; DataIdx < len; DataIdx++)
    {
        while ((USART1->SR & 0X40) == 0); // Wait for transmission to complete
        USART1->DR = (uint8_t) *ptr++;
    }
    return len;
}

/* USER CODE END 1 */
```

## Printing Floating-Point Numbers in STM32CubeIDE

1. In the STM32CubeIDE, select your project from the sidebar, right-click, and choose `Properties` - `C/C++ Build` - `Settings` - `MCU GCC Linker` - `Miscellaneous`.
2. Add a new entry in the `Other flags` section and enter `-u_printf_float`.
3. Recompile your project.

## Fixing Garbled Output in HAL_UART_Receive_IT

To fix the issue of garbled output when using `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10,0xFFFF);`, change the data length (`10`) to `1`.

## References and Acknowledgments

- [Redirecting printf Output to UART in STM32CubeIDE](https://blog.51cto.com/u_15353042/3751177)
- [Modifying printf Redirection and UART Output of Floating-Point Data in STM32CubeIDE](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [Revisiting the HAL_UART_Receive_IT Function](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.