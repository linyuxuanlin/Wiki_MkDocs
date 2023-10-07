# STM32CubeIDE Redirección de puerto serie (printf) y salida de punto flotante

## Redirigir printf al puerto serie

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

// La función _write se encuentra en syscalls.c y se define con __weak, por lo que se puede definir directamente en otros archivos
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
	int DataIdx;
	for (DataIdx = 0; DataIdx < len; DataIdx++)
	{
		  while ((USART1->SR & 0X40) == 0); // Esperar a que se envíe
		  USART1->DR = (uint8_t) *ptr++;
	}
	return len;
}

/* USER CODE END 1 */
```

## Salida de punto flotante por puerto serie en STM32CubeIDE

1. En la barra lateral de STM32CubeIDE, seleccione el proyecto, haga clic derecho y seleccione `Properties` - `C/C++ Build` - `Settings` - `MCU GCC Linker` - `Miscellaneous`.
2. Agregue un elemento en la sección `Other flags` y escriba `-u_printf_float`.
3. Vuelva a compilar.

## Problema de caracteres ilegibles en HAL_UART_Receive_IT

Cambie la longitud de la palabra (`10`) en `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10,0xFFFF);` a `1`.

## Referencias y agradecimientos

- [Redirigir printf al puerto serie en STM32CubeIDE](https://blog.51cto.com/u_15353042/3751177)
- [Modificar la salida de punto flotante y redirigir printf al puerto serie en STM32CubeIDE](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [Cuestionando de nuevo la función HAL_UART_Receive_IT](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.