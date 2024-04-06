# Notas de desarrollo de la biblioteca HAL - Temporizador básico TIM

En STM32, existen tres tipos de temporizadores: temporizadores básicos, temporizadores generales y temporizadores avanzados, que se utilizan para manejar diversas tareas cíclicas. En este artículo, proporcionaré una descripción detallada del temporizador básico.

## Principio básico

Los temporizadores que solemos utilizar se dividen en tres categorías: temporizadores básicos, temporizadores generales y temporizadores avanzados. En la serie de microcontroladores STM32F4, la correspondencia es la siguiente:

- Temporizadores básicos
  - TIM6
  - TIM7
- Temporizadores generales
  - TIM2-TIM5
  - TIM9-TIM14
- Temporizadores avanzados
  - TIM1
  - TIM8
- (Temporizador SysTick)

Por lo general, utilizamos los temporizadores básicos como cronómetros y los temporizadores generales para generar señales PWM.

### Características del temporizador básico

En la serie de microcontroladores STM32F4, los temporizadores básicos TIM6 y TIM7 tienen las siguientes características:

- Montados en el bus APB1
- Contador de recarga automática de 16 bits
- Predivisor programable de 16 bits para dividir la frecuencia del contador (es decir, se puede modificar durante la ejecución), con un coeficiente de división entre 1 y 65536
- Circuitos de sincronización utilizados para activar el DAC de forma sincrónica
- Generan interrupciones/solicitudes de DMA cuando se produce un desbordamiento del contador

### Referencia de funciones de temporizador comunes

- **HAL_TIM_Base_Init()**: Inicializa la unidad de tiempo base del temporizador
- **HAL_TIM_Base_DeInit()**: Desactiva el temporizador, el opuesto de la inicialización
- **HAL_TIM_Base_MspInit()**: Función de inicialización MSP, se llama automáticamente durante la inicialización del temporizador
- **HAL_TIM_Base_MspDeInit()**: Lo opuesto a la función anterior
- **HAL_TIM_Base_Start()**: Inicia el temporizador
- **HAL_TIM_Base_Stop()**: Detiene el temporizador
- **HAL_TIM_Base_Start_IT()**: Inicia el temporizador en modo de interrupción
- **HAL_TIM_Base_Stop_IT()**: Detiene el temporizador en modo de interrupción
- **HAL_TIM_Base_Start_DMA()**: Inicia el temporizador en modo DMA
- **HAL_TIM_Base_Stop_DMA()**: Detiene el temporizador en modo DMA

## Hacer que el LED parpadee utilizando el temporizador básico

En este experimento, utilizaremos el temporizador básico para implementar una función de temporización que haga que el LED cambie de estado cada 0.5 segundos.

### Configuración del temporizador básico en CubeMX

Primero, abrimos la página de configuración del árbol de relojes en la configuración de Clock Configuration y encontramos y anotamos el valor de APB1 Timer clocks en el extremo derecho:

![](https://media.wiki-power.com/img/20210407152250.png)

Esto se debe a que los temporizadores TIM2-TIM7 y TIM12-TIM14 de la serie STM32F4 están montados en el bus APB1 de baja velocidad, mientras que TIM1, TIM8-TIM11 están montados en el bus APB2 de alta velocidad. En este caso, utilizaremos el temporizador básico TIM6, por lo que debemos verificar la velocidad de APB1 (que es de 90 MHz después de la división y multiplicación).

A continuación, en la barra lateral Timer, encontramos TIM6 y activamos "Activated" para activar el temporizador, y configuramos los siguientes parámetros:

![](https://media.wiki-power.com/img/20210407173136.png)

Significado de los parámetros:

- **Prescaler** (coeficiente de predivisión): 8999
- **Counter Mode** (modo de contador): Up (cuenta desde 0 hasta el coeficiente de predivisión y luego se desborda)
- **Counter Period** (período de tiempo/carga): 4999
- **auto-reload preload** (recarga automática): Enable (se recarga automáticamente cuando se produce un desbordamiento)

Dado que estoy utilizando una fuente de reloj de 90 MHz, establezco el coeficiente de predivisión en 8999 (es decir, una división de 9000), lo que resulta en una frecuencia de 10 kHz después de la división (90 MHz/9000). Establezco el período de tiempo en 4999 (cuenta 5000 veces por período), lo que da como resultado un período de 500 ms.

Luego, en la pestaña NVIC, habilitamos las interrupciones:

![](https://media.wiki-power.com/img/20210407155959.png)

### Configuración básica del temporizador en el código

En el archivo `main.c`, activa el temporizador:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_Base_Start_IT(&htim6);

/* USER CODE END 2 */
```

Agrega una función de devolución de llamada en el archivo `stm32f4xx_it.c`:

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

Para obtener información sobre la configuración del LED, consulta el artículo anterior [**HAL 库开发笔记-GPIO**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0%EF%BC%88%E4%BA%8C%EF%BC%89-GPIO).

Después de descargar y grabar el programa, podrás ver que el LED cambia de estado cada 500 ms (es decir, ocurre un desbordamiento y se genera un evento de desbordamiento cada 500 ms, y en la función de devolución de llamada se invierte el estado del LED).

## Referencias y agradecimientos

- [STM32CubeMX 实战教程（四）—— 基本定时器（还是点灯）](https://blog.csdn.net/weixin_43892323/article/details/104534920)
- [进阶篇 VI [Timer & PWM]](https://alchemicronin.github.io/posts/fd31d369/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
