# Notas de desarrollo de la biblioteca HAL - Temporizador básico TIM

En STM32, hay tres tipos de temporizadores: temporizador básico, temporizador general y temporizador avanzado, utilizados para procesar diversas tareas periódicas. En este artículo, detallaré el temporizador básico.

## Principios básicos

Los temporizadores que utilizamos comúnmente se dividen en tres categorías: temporizador básico, temporizador general y temporizador avanzado. En la serie STM32F4, se corresponden de la siguiente manera:

- Temporizador básico
  - TIM6
  - TIM7
- Temporizador general
  - TIM2-TIM5
  - TIM9-TIM14
- Temporizador avanzado
  - TIM1
  - TIM8
- (Temporizador SysTick)

Por lo general, utilizamos el temporizador básico como temporizador y el temporizador general para generar señales PWM.

### Características del temporizador básico

En la serie STM32F4, las características de los temporizadores básicos TIM6 y TIM7 son las siguientes:

- Montado en el bus APB1
- Contador de incremento automático de 16 bits
- Predivisor programable de 16 bits para dividir la frecuencia del reloj del contador en tiempo de ejecución, con un coeficiente de división entre 1 y 65536
- Circuito de sincronización utilizado para activar el DAC
- Genera una interrupción/solicitud de DMA cuando se produce un evento de desbordamiento del contador

### Referencia de funciones de temporizador comunes

- **HAL_TIM_Base_Init()**: Inicializa la unidad de tiempo base del temporizador.
- **HAL_TIM_Base_DeInit()**: Desactiva el temporizador, lo contrario a la inicialización.
- **HAL_TIM_Base_MspInit()**: Función de inicialización MSP, se llama automáticamente al inicializar el temporizador.
- **HAL_TIM_Base_MspDeInit()**: Lo contrario al anterior.
- **HAL_TIM_Base_Start()**: Inicia el temporizador.
- **HAL_TIM_Base_Stop()**: Detiene el temporizador.
- **HAL_TIM_Base_Start_IT()**: Inicia el temporizador en modo de interrupción.
- **HAL_TIM_Base_Stop_IT()**: Detiene el temporizador en modo de interrupción.
- **HAL_TIM_Base_Start_DMA()**: Inicia el temporizador en modo DMA.
- **HAL_TIM_Base_Stop_DMA()**: Detiene el temporizador en modo DMA.

## Hacer que el LED parpadee con temporizador básico

En este experimento, utilizaremos el temporizador básico para implementar una función de temporización que haga que el LED cambie de estado de encendido a apagado cada 0,5 segundos.

### Configuración del temporizador básico en CubeMX

En primer lugar, abrimos la página de configuración del árbol de reloj de configuración de Clock Configuration y encontramos y anotamos el valor de APB1 Timer clocks en el extremo derecho:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210407152250.png)

Esto se debe a que los temporizadores TIM2-TIM7, TIM12-TIM14 de la serie STM32F4 están montados en el bus APB1 de baja velocidad, mientras que TIM1, TIM8-TIM11 están montados en el bus APB2 de alta velocidad. Aquí utilizaremos el temporizador básico TIM6, por lo que debemos ver la velocidad de APB1 (que después de la división y multiplicación es de 90 MHz).

A continuación, encontramos TIM6 en la barra lateral Timer, activamos el temporizador y configuramos los siguientes parámetros:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210407173136.png)

Significado de los parámetros:

- **Prescaler**: 8999
- **Counter Mode**: Up (cuenta desde cero hasta el valor de predivisión y luego desborda)
- **Counter Period**: 4999
- **auto-reload preload**: Enable (se recarga automáticamente cuando se produce un desbordamiento)

Como estoy utilizando una fuente de reloj de 90 MHz, establezco el predivisor en 8999 (es decir, una división de 9000), lo que resulta en una frecuencia de 10 kHz (90 MHz/9000). El valor de recarga se establece en 4999 (cuenta 5000 veces por ciclo), lo que da como resultado un ciclo de 500 ms.

Luego, en la pestaña NVIC, habilitamos la interrupción:

### Configuración del temporizador básico en el código

En `main.c`, inicie el temporizador:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_Base_Start_IT(&htim6);

/* USER CODE END 2 */
```

Agregue una función de devolución de llamada en `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */

void HAL_TIM_PeriodElapsedCallback(TIM_HandleTypeDef *htim)
{
    if(htim->Instance == TIM6)
    {
        HAL_GPIO_TogglePin(LED1_GPIO_Port, LED1_Pin);
    }

}

/* USER CODE END 1 */
```

Para la configuración del LED, consulte el artículo anterior [**HAL 库开发笔记-GPIO**](https://wiki-power.com/es/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0%EF%BC%88%E4%BA%8C%EF%BC%89-GPIO).

Después de descargar y grabar, el LED cambiará de estado según el período de 500 ms que hemos establecido (es decir, cuando ocurre un desbordamiento y se produce un evento de desbordamiento en cada 500 ms, realizamos una operación de volteo en el LED en la función de devolución de llamada).

## Referencias y agradecimientos

- [STM32CubeMX 实战教程（四）—— 基本定时器（还是点灯）](https://blog.csdn.net/weixin_43892323/article/details/104534920)
- [进阶篇 VI [Timer & PWM]](https://alchemicronin.github.io/posts/fd31d369/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.