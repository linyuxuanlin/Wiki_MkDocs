# Redirección de printf y salida de números decimales en STM32CubeIDE

## Redirección de printf hacia el puerto serie

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

/* USER CODE BEGIN 1 */

// La función _write se encuentra en syscalls.c y se define como __weak, por lo que puede definirse directamente en otros archivos.
__attribute__((weak)) int _write(int file, char *ptr, int len)
{
	int DataIdx;
	for (DataIdx = 0; DataIdx < len; DataIdx++)
	{
		  while ((USART1->SR & 0X40) == 0); // Espera hasta que se complete la transmisión
		  USART1->DR = (uint8_t) *ptr++;
	}
	return len;
}

/* USER CODE END 1 */
```

## Salida de números decimales en STM32CubeIDE

1. En el panel lateral de STM32CubeIDE, selecciona el proyecto y haz clic con el botón derecho. Luego, elige `Propiedades` - `C/C++ Build` - `Configuración` - `MCU GCC Linker` - `Miscelánea`.
2. Agrega un nuevo elemento en la sección `Other flags` y escribe `-u_printf_float`.
3. Vuelve a compilar el proyecto.

## Problema de caracteres corruptos en HAL_UART_Receive_IT

Para solucionar el problema de caracteres corruptos en HAL_UART_Receive_IT, cambia la longitud de datos en la línea `HAL_UART_Transmit(&huart1, (uint8_t *)aRxBuffer, 10, 0xFFFF);` de `10` a `1`.

## Referencias y Agradecimientos

- [Redirección de printf a través de puerto serie en STM32CubeIDE](https://blog.51cto.com/u_15353042/3751177)
- [Modificación de la redirección de printf y salida de datos decimales por UART en STM32CubeIDE](https://blog.csdn.net/qq_42980638/article/details/98359026)
- [Cuestionando nuevamente la función HAL_UART_Receive_IT](https://shequ.stmicroelectronics.cn/forum.php?mod=viewthread&tid=615546)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.