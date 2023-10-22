# Notas de desarrollo de la biblioteca HAL - Comunicación serie

En este artículo, basado en el kit de desarrollo RobotCtrl personalizado, con un núcleo de microcontrolador STM32F407ZET6 y el uso del chip SP3232EEN para la comunicación RS-232, se detallarán los esquemas y la información detallada. Para más detalles, consulte [**RobotCtrl - Kit de Desarrollo Universal STM32**](enlace a reemplazar[3]).

## Principios básicos

Para comprender los principios básicos de la comunicación serie, consulte el artículo [**Protocolo de Comunicación - Comunicación Serie**](enlace a reemplazar[3]).

## Experimento de Comunicación Serie

Antes de avanzar en los experimentos, es necesario configurar varios parámetros, como la descarga en serie y la configuración de la sincronización de reloj, en CubeMX. Para obtener instrucciones detalladas, siga los pasos en el artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del Entorno**](enlace a reemplazar[3]).

### Configuración en CubeMX

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210207100329.png)

De acuerdo con el esquema original, el puerto serie que utilizaremos para el experimento es `USART1`, es decir, los pines `PA9` y `PA10`. En CubeMX, primero debemos configurar estos dos pines para que funcionen como las funciones de transmisión y recepción de `USART1`. Luego, en la pestaña de `USART1` en la parte izquierda, estableceremos el modo como asíncrono y ajustaremos los parámetros, como la velocidad de baudios (Baud Rate):

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210207100941.png)

Los detalles de los parámetros son los siguientes:

- **Configuración de la Velocidad de Baudios** (Baud Rate): No hay una velocidad de baudios específica que sea la mejor, debe ajustarse según las necesidades reales y coincidir con la configuración en la herramienta de depuración de puerto serie.
- **Número de Bits de Datos** (Word Length): Si se habilita la comprobación de paridad, el número real de bits de datos será uno menos que este valor.
- **Comprobación de Paridad** (Parity): Puede seleccionar comprobación de paridad par o impar, o deshabilitarla.
- **Bits de Parada** (Stop Bits): Uno o dos bits adicionales utilizados como señales de fin de transmisión o recepción.
- **Dirección de Datos** (Data Direction): Puede elegir entre transmitir únicamente, recibir únicamente o modo de transmisión y recepción.
- **Muestreo Excesivo** (Over Sampling): Una tasa de muestreo de 8 veces o 16 veces puede ayudar a prevenir errores de datos de manera efectiva.

Por último, en la pestaña NVIC, habilitaremos las interrupciones del puerto serie USART1, como se muestra en la siguiente imagen:

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210207104641.png)

### Configuración en el código

Primero, necesitamos agregar el siguiente código al final del archivo `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // Recibe y escribe en aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // Envía de vuelta los datos recibidos en aRxBuffer
    }
}
/* USER CODE END 1 */
```

Donde `aRxBuffer` es una variable global definida como tipo `uint8_t` en el archivo `main.c`. Con este código, cada vez que se recibe un byte, se genera una interrupción que devuelve ese byte y vuelve a habilitar la interrupción. Debe definir `aRxBuffer` en ambos archivos `main.c` y `stm32f4xx_it.c`.

```c title="main.c"
/* Variables Privadas -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "PRUEBA DE USART\r\n"; // Cadena para enviar
uint8_t aRxBuffer[20]; // Cadena para recibir

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

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // Habilitar interrupción de recepción

/* USER CODE END 2 */
```

También puedes enviar un mensaje de inicialización para indicar que la UART está lista:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // Enviar aTxBuffer personalizado

/* USER CODE END 2 */
```

Si necesitas redirigir la función `printf` para utilizarla como salida de UART en un dispositivo STM32, consulta [STM32CubeIDE Redirección de UART para printf y salida de números de punto flotante](https://www.ejemplo.com) para obtener más detalles.

### Descarga y Verificación

Después de programar con éxito el dispositivo, abre una utilidad de puerto serie y configura el puerto y la velocidad de baudios correspondientes.

Al conectar el puerto serie, verás primero el contenido de `aTxBuffer` impreso, seguido de la respuesta con el contenido de `aRxBuffer`. Como se muestra en la imagen a continuación:

![](https://img.wiki-power.com/d/wiki-media/img/20210403232628.png)

## Referencias y Agradecimientos

- [Tutorial práctico de STM32CubeMX (Parte 6) - Comunicación UART](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [UART y USART en Profundidad](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [STM32 Recepción No Bloqueante con HAL_UART_Receive_IT: Análisis y Aplicación Práctica](https://zhuanlan.zhihu.com/p/147414331)
- [Tutorial de la Biblioteca HAL - Parte 6: Recepción de Datos de UART](https://blog.csdn.net/geek_monkey/article/details/89165040)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

Here is the translated text in Spanish while maintaining the original markdown format and not interpreting the content. If you have any further requests or need any clarifications, please let me know.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.