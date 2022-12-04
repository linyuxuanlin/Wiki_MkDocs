---
id: STM32CubeIDE串口重定向（printf）及输出浮点型
title: STM32CubeIDE 串口重定向（printf）及输出浮点型
---

## 重定向 printf 至串口

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

//_write 函数在 syscalls.c 中， 使用 __weak 定义， 所以可以直接在其他文件中定义 _write 函数
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
	int DataIdx;
	for (DataIdx = 0; DataIdx < len; DataIdx++)
	{
		  while ((USART1->SR & 0X40) == 0); //等待发送完毕
		  USART1->DR = (uint8_t) *ptr++;
	}
	return len;
}

/* USER CODE END 1 */
```

## STM32CubeIDE 串口输出浮点型

1. 在 STM32CubeIDE 侧栏选中工程，右键选择 `Properties` - `C/C++ Build` - `Settings` - `MCU GCC Linker` - `Miscellaneous`。
2. 在 `Other flags` 栏添加一个项目，填 `-u_printf_float`。
3. 重新编译即可。

## HAL_UART_Receive_IT 乱码问题

将 `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10,0xFFFF);` 的字长（`10`）改为 `1` 即可。

## 参考与致谢

- [STM32CubeIDE 实现 printf 重定向输出到串口](https://blog.51cto.com/u_15353042/3751177)
- [STM32CubeIDE 之 printf 重定向及串口（uart）输出浮点型数据的修改](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [再次质疑 HAL_UART_Receive_IT函数](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

