# Notas de desarrollo de la biblioteca HAL - Comunicación serie

Este artículo se basa en el conjunto de desarrollo RobotCtrl de desarrollo propio, con un núcleo de microcontrolador STM32F407ZET6 y utiliza el chip SP3232EEN para la comunicación RS-232. Para ver el esquema y obtener una descripción detallada, por favor consulta [**RobotCtrl - STM32 Conjunto de Desarrollo Universal**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Principios Básicos

Para comprender los principios básicos de la comunicación serie, consulta el artículo [**Protocolo de Comunicación - Comunicación Serie**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1).

## Experimento de Comunicación Serie

Antes de llevar a cabo el próximo experimento, es necesario configurar varios parámetros en CubeMX, como la descarga de la comunicación serie, la configuración de la frecuencia del reloj, entre otros. Para conocer los detalles completos, consulta el artículo [**Notas de Desarrollo de la Biblioteca HAL - Configuración del Entorno**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) para obtener instrucciones detalladas.

### Configuración en CubeMX

![Imagen](https://media.wiki-power.com/img/20210207100329.png)

De acuerdo con el esquema original, el puerto serie que utilizaremos para el experimento es `USART1`, es decir, los pines `PA9` y `PA10`. En CubeMX, primero debemos configurar estos dos pines como pines de envío y recepción para `USART1`. Luego, en la pestaña `USART1` de la izquierda, establecer el modo como asíncrono (Asynchronous) y ajustar los parámetros como la velocidad en baudios (Baud Rate):

![Imagen](https://media.wiki-power.com/img/20210207100941.png)

Los detalles de los parámetros son los siguientes:

- **Configuración de Baud Rate**: No hay una velocidad de baudios única que sea la mejor; se debe ajustar según las necesidades y para que coincida con el asistente de depuración de comunicación serie.
- **Número de bits de datos** (Word Length): Si se habilita la comprobación de paridad, el número real de bits de datos será uno menos.
- **Paridad** (Parity): Puede elegir entre la comprobación de paridad par o impar, o no utilizarla.
- **Bits de parada** (Stop Bits): Un bit adicional o dos se utilizan como señales de fin de transmisión o recepción.
- **Dirección de datos** (Data Direction): Puede seleccionar entre enviar solamente, recibir solamente o el modo de enviar y recibir.
- **Muestreo excesivo** (Over Sampling): Una tasa de muestreo 8x o 16x puede prevenir eficazmente errores de datos.

Por último, habilita las interrupciones de USART1 en la pestaña NVIC, como se muestra en la imagen:

![Imagen](https://media.wiki-power.com/img/20210207104641.png)

### Configuración en el Código

Primero, debes agregar el siguiente código al final del archivo `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // Recibir e ingresar en aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // Enviar el aRxBuffer recibido
    }
}
/* USER CODE END 1 */
```

Aquí, `Buffer` es una variable global de tipo uint8_t definida en el archivo `main.c`. En este código, se genera una interrupción después de recibir cada byte, se devuelve ese byte de datos y se habilita la interrupción nuevamente. Asegúrate de definir esta variable tanto en `main.c` como en `stm32f4xx_it.c`.

```c title="main.c"
/* Variables Privadas -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "PRUEBA DE USART\r\n"; // Cadena a enviar
uint8_t aRxBuffer[20]; // Cadena de recepción

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* Variables Privadas -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

Además, en `main.c`, necesitamos habilitar la interrupción de recepción después de la inicialización de UART y antes del bucle principal:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // Habilitar la interrupción de recepción

/* USER CODE END 2 */
```

También puedes enviar un mensaje de inicialización para indicar que la UART está lista:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // Enviar la cadena aTxBuffer

/* USER CODE END 2 */
```

Si necesitas redirigir la función `printf` para usarla en la salida por UART en un dispositivo STM32, consulta [**STM32CubeIDE 串口重定向（printf）及输出浮点型**](https://wiki-power.com/STM32CubeIDE%E4%B8%B2%E5%8F%A3%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%88printf%EF%BC%89%E5%8F%8A%E8%BE%93%E5%87%BA%E6%B5%AE%E7%82%B9%E5%9E%8B) para obtener más información.

### Descarga y Verificación

Después de cargar el programa con éxito, abre un programa de asistencia de UART y configura el puerto y la velocidad de baudios correspondientes.

Una vez que estés conectado al puerto UART, se imprimirá inicialmente el contenido de `aTxBuffer`, y luego se mostrará en la pantalla el contenido recibido en `aRxBuffer`, tal como se muestra en la imagen:

![Imagen](https://media.wiki-power.com/img/20210403232628.png)

## Referencias y Agradecimientos

- [STM32CubeMX 实战教程（六）—— 串口通信](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [进阶篇 III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [STM32 非阻塞 HAL_UART_Receive_IT 解析与实际应用](https://zhuanlan.zhihu.com/p/147414331)
- [HAL 库教程 6：串口数据接收](https://blog.csdn.net/geek_monkey/article/details/89165040)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
