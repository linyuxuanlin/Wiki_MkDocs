# Notas de Desarrollo de la Biblioteca HAL - Temporizador Básico TIM

En la serie STM32, existen tres tipos de temporizadores: el temporizador básico, el temporizador general y el temporizador avanzado. Estos temporizadores se utilizan para diversas tareas relacionadas con el tiempo. En este artículo, me enfocaré en el temporizador básico.

## Principios Fundamentales

Los temporizadores que solemos utilizar se dividen en tres categorías: básicos, generales y avanzados. En la serie de microcontroladores STM32F4, se corresponden de la siguiente manera:

- Temporizador Básico
  - TIM6
  - TIM7
- Temporizador General
  - TIM2-TIM5
  - TIM9-TIM14
- Temporizador Avanzado
  - TIM1
  - TIM8
- (Temporizador SysTick)

Normalmente, utilizamos los temporizadores básicos como contadores de tiempo y los temporizadores generales para generar señales PWM.

### Características del Temporizador Básico

En la serie de microcontroladores STM32F4, los temporizadores básicos TIM6 y TIM7 tienen las siguientes características:

- Están conectados al bus APB1.
- Son contadores de recarga automática de 16 bits.
- Tienen un preescalador programable de 16 bits que se utiliza para dividir la frecuencia del reloj del contador en tiempo de ejecución, con un valor de división que oscila entre 1 y 65536.
- Incluyen un circuito de sincronización para activar el DAC.
- Generan una interrupción/solicitud DMA cuando se produce un desbordamiento del contador.

### Referencia de Funciones Comunes del Temporizador

- **HAL_TIM_Base_Init()**: Inicializa la unidad de tiempo base del temporizador.
- **HAL_TIM_Base_DeInit()**: Deshabilita el temporizador, en sentido contrario a la inicialización.
- **HAL_TIM_Base_MspInit()**: Función de inicialización MSP, se llama automáticamente al inicializar el temporizador.
- **HAL_TIM_Base_MspDeInit()**: Lo opuesto a la función anterior.
- **HAL_TIM_Base_Start()**: Inicia el temporizador.
- **HAL_TIM_Base_Stop()**: Detiene el temporizador.
- **HAL_TIM_Base_Start_IT()**: Inicia el temporizador en modo de interrupción.
- **HAL_TIM_Base_Stop_IT()**: Detiene el temporizador en modo de interrupción.
- **HAL_TIM_Base_Start_DMA()**: Inicia el temporizador en modo DMA.
- **HAL_TIM_Base_Stop_DMA()**: Detiene el temporizador en modo DMA.

## Hacer Parpadear un LED con el Temporizador Básico

En este experimento, utilizamos un temporizador básico para medir el tiempo y hacer que un LED cambie su estado de encendido y apagado cada 0.5 segundos.

### Configuración del Temporizador Básico en CubeMX

En primer lugar, abrimos la página de configuración del árbol de reloj en "Clock Configuration" y encontramos el valor de los relojes APB1 Timer ubicados en el extremo derecho:

![Clock Configuration](https://img.wiki-power.com/d/wiki-media/img/20210407152250.png)

Esto se debe a que los temporizadores TIM2-TIM7 y TIM12-TIM14 de la serie STM32F4 están conectados al bus de baja velocidad APB1, mientras que TIM1, TIM8-TIM11 están conectados al bus de alta velocidad APB2. Para nuestro caso, estamos utilizando el temporizador básico TIM6, por lo que debemos conocer la velocidad de APB1 (después de la división y multiplicación, es de 90 MHz).

Luego, en la sección de Timer del panel lateral, buscamos TIM6 y activamos la casilla "Activated". A continuación, configuramos los siguientes parámetros:

![Configuración TIM6](https://img.wiki-power.com/d/wiki-media/img/20210407173136.png)

Significado de los parámetros:

- **Prescaler (Preescalador)**: 8999
- **Counter Mode (Modo de Contador)**: Up (Contador que cuenta desde 0 hasta el valor del preescalador y se reinicia al desbordar).
- **Counter Period (Período del Contador/Valor de Carga)**: 4999
- **Auto-reload preload (Recarga automática de la carga)**: Habilitada (Se recargará automáticamente al desbordar).

En mi caso, la fuente de reloj es de 90 MHz, por lo que establezco el preescalador en 8999 (lo que equivale a una división de 9000), lo que resulta en una frecuencia de 10 kHz (90 MHz/9000). El valor de carga se establece en 4999 (el contador cuenta hasta 5000), lo que da como resultado un período de 500 ms.

Luego, en la pestaña NVIC, habilitamos las interrupciones:

![Habilitación de Interrupciones](https://img.wiki-power.com/d/wiki-media/img/20210407155959.png)

### Configuración del temporizador básico en el código

En el archivo `main.c`, activa el temporizador de la siguiente manera:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_Base_Start_IT(&htim6);

/* USER CODE END 2 */
```

En el archivo `stm32f4xx_it.c`, agrega una función de devolución de llamada:

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

Para obtener información sobre la configuración del LED, consulta el artículo anterior [**Notas de desarrollo de la biblioteca HAL - GPIO**](https://blog.csdn.net/weixin_43892323/article/details/104534920).

Después de cargar el programa, podrás observar que el LED cambia su estado cada 500 ms, como se había previsto (es decir, ocurre un desbordamiento y se genera un evento de desbordamiento cada 500 ms, y en la función de devolución de llamada invertimos el estado del LED).

## Referencias y Agradecimientos

- [STM32CubeMX Practical Tutorial (Part Four) - Basic Timer (Still Blinking)](https://blog.csdn.net/weixin_43892323/article/details/104534920)
- [Advanced Series VI [Timer & PWM]](https://alchemicronin.github.io/posts/fd31d369/)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.