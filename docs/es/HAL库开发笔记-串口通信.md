# Notas de desarrollo de la biblioteca HAL - Comunicación por puerto serie

Este artículo se basa en el kit de desarrollo RobotCtrl, con núcleo de microcontrolador STM32F407ZET6 y chip SP3232EEN para comunicación RS-232. Para ver el esquema y una introducción detallada, consulte [**RobotCtrl - Kit de desarrollo STM32 universal**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Principios básicos

Para conocer los principios básicos de la comunicación por puerto serie, consulte el artículo [**Protocolo de comunicación - Comunicación por puerto serie**](https://wiki-power.com/es/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1) (en chino).

## Experimento de comunicación por puerto serie

Antes de realizar el siguiente experimento, es necesario configurar varios parámetros, como la descarga por puerto serie y el reloj, en CubeMX. Para obtener información detallada, consulte el artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del entorno**](https://wiki-power.com/es/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) (en chino).

### Configuración del puerto serie en CubeMX

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207100329.png)

Según el esquema, el puerto serie que utilizamos para el experimento de comunicación es `USART1`, es decir, los pines `PA9` y `PA10`. Primero, debemos configurar estos dos pines como funciones de envío y recepción de `USART1` en CubeMX, y luego hacer clic en la pestaña USART1 a la izquierda para establecer el modo (Mode) como asíncrono (Asynchronous) y modificar los parámetros de velocidad de transmisión (Baud Rate) y otros parámetros a continuación:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207100941.png)

Los detalles de los parámetros son los siguientes:

- **Velocidad de transmisión** (Baud Rate): no hay una velocidad de transmisión mejor que otra, modifíquela según sea necesario para que coincida con el asistente de depuración por puerto serie.
- **Número de bits de datos** (Word Length): si la comprobación de paridad está habilitada, los datos reales se reducirán en uno en este número de bits.
- **Comprobación de paridad** (Parity): puede elegir comprobación de paridad par/impar o no comprobar.
- **Bits de parada** (Stop Bits): un bit adicional o dos se utilizan como señal de finalización de envío o recepción.
- **Dirección de datos** (Data Direction): puede elegir enviar solo, recibir solo o modo de envío y recepción.
- **Muestreo excesivo** (Over Sampling): una tasa de muestreo de 8 o 16 veces puede prevenir eficazmente errores de datos.

Por último, active la interrupción del puerto serie USART1 en la pestaña NVIC, como se muestra en la siguiente imagen:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207104641.png)

### Configuración del puerto serie en el código

Primero, agregue el siguiente código al final de `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // Recibe y escribe en aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // Envía aRxBuffer recibido
    }
}
/* USER CODE END 1 */
```

El `Buffer` es una variable global de tipo uint8_t definida en `main.c`. Después de recibir cada byte, se genera una interrupción que devuelve ese byte de datos y vuelve a habilitar la interrupción. Necesitamos definirlo en `main.c` y `stm32f4xx_it.c` respectivamente:

```c title="main.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "USART TEST\r\n"; //cadena de caracteres para enviar
uint8_t aRxBuffer[20]; //cadena de caracteres para recibir

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

Además, en `main.c`, necesitamos agregar una función de habilitación de interrupción de recepción antes de la función principal después de la inicialización de la UART:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // función de habilitación de interrupción de recepción

/* USER CODE END 2 */
```

También podemos enviar un mensaje de inicialización para indicar que la UART se ha iniciado:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // enviar aTxBuffer personalizado anterior

/* USER CODE END 2 */
```

Si necesita redirigir printf (utilice la función printf para la función de salida de la UART en STM32), consulte [**STM32CubeIDE Serial Redirect (printf) y salida de punto flotante**](https://wiki-power.com/es/STM32CubeIDE%E4%B8%B2%E5%8F%A3%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%88printf%EF%BC%89%E5%8F%8A%E8%BE%93%E5%87%BA%E6%B5%AE%E7%82%B9%E5%9E%8B).

### Descarga y verificación

Después de programar con éxito, abrimos el asistente de puerto serie y configuramos el puerto y la velocidad de transmisión correspondientes.

Después de conectar el puerto serie, se imprimirá una línea de contenido de `aTxBuffer`, y luego se devolverá e imprimirá `aRxBuffer` recibido. Como se muestra en la figura:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210403232628.png)

## Referencias y agradecimientos

- [Tutorial práctico de STM32CubeMX (Parte 6) - Comunicación serial](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [Avanzado III [UART y USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [Análisis y aplicación práctica de HAL_UART_Receive_IT no bloqueante en STM32](https://zhuanlan.zhihu.com/p/147414331)
- [Tutorial de la biblioteca HAL 6: Recepción de datos por puerto serie](https://blog.csdn.net/geek_monkey/article/details/89165040)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
