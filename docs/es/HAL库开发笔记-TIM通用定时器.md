# Notas de desarrollo de la biblioteca HAL - Temporizador universal TIM

En el artículo anterior, se presentaron brevemente los tres tipos de temporizadores de STM32F4, y se explicó en detalle el temporizador básico. En este artículo, continuaremos presentando el temporizador universal.

## Principios básicos

En STM32F4, los temporizadores universales son TIM2-TIM5, TIM9-TIM14.

### Características del temporizador universal

En STM32F4, las características del temporizador universal son las siguientes:

- Contador de recarga automática de 16/32 bits para incremento, decremento e incremento / decremento
- Predivisor programable de 16 bits para dividir la frecuencia del reloj del contador (factor de división de 1-65536)
- 4 canales independientes, que se pueden utilizar para:
  - Captura de entrada
  - Comparación de salida
  - Generación de PWM (modo de borde y alineación central)
  - Salida de modo de pulso único
- Circuito de sincronización que permite controlar el temporizador con una señal externa y sincronizar varios temporizadores
- Generación de interrupciones / solicitudes DMA en los siguientes eventos:
  - Actualización: desbordamiento / subdesbordamiento del contador, inicialización del contador (por software o por activación interna / externa)
  - Evento de activación (inicio, parada, inicialización del contador o conteo por activación interna / externa)
  - Captura de entrada
  - Comparación de salida
- Admite codificadores incrementales (ortogonales) y circuitos de sensor Hall
- Entrada de disparo de reloj externo o gestión de corriente periódica

### Referencia de funciones de temporizador comunes

A continuación se presentan las funciones de temporizador comunes que se utilizan con el temporizador universal y que son las mismas que las del temporizador básico.

- **HAL_TIM_Base_Init()**: Inicializa la unidad de tiempo base del temporizador
- **HAL_TIM_Base_DeInit()**: Desactiva el temporizador, lo contrario de la inicialización
- **HAL_TIM_Base_MspInit()**: Función de inicialización MSP, que se llama automáticamente al inicializar el temporizador
- **HAL_TIM_Base_MspDeInit()**: Lo contrario del anterior
- **HAL_TIM_Base_Start()**: Inicia el temporizador
- **HAL_TIM_Base_Stop()**: Detiene el temporizador
- **HAL_TIM_Base_Start_IT()**: Inicia el temporizador en modo de interrupción
- **HAL_TIM_Base_Stop_IT()**: Detiene el temporizador en modo de interrupción
- **HAL_TIM_Base_Start_DMA()**: Inicia el temporizador en modo DMA
- **HAL_TIM_Base_Stop_DMA()**: Detiene el temporizador en modo DMA

## Generación de una señal PWM con una frecuencia de 1 kHz y un ciclo de trabajo del 50% utilizando el temporizador universal

En este experimento, se utiliza el temporizador universal para generar una señal PWM con una frecuencia de 1 kHz y un ciclo de trabajo del 50%, que se puede mostrar en un osciloscopio.

### Configuración del temporizador universal en CubeMX

En primer lugar, abrimos la página de configuración del árbol de relojes de la configuración de Clock Configuration, y como el temporizador universal está montado en el bus APB2 de alta velocidad, encontramos y anotamos la frecuencia del reloj APB2 Timer clocks (180 MHz):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210627133951.png)

A continuación, encontramos TIM8 en la barra lateral de Timer y configuramos el canal 1 (`Channel 1`) para la generación de PWM (`PWM Generation CH1`). Para generar una señal cuadrada PWM con una frecuencia de 1 kHz, necesitamos configurar los siguientes parámetros:

- **Prescaler** (factor de división previo): 180-1
- **Modo de contador**: Up (contar desde 0 hasta el factor de división previo y luego desbordar)
- **Periodo del contador** (valor de carga / período de tiempo): 1000-1
- **auto-reload preload** (recarga automática): Enable (se recarga automáticamente cuando se desborda)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210627153422.png)

Por lo tanto, como la fuente de reloj seleccionada aquí es de 180 MHz, configuramos el factor de división previo en 180-1 = 179, lo que resulta en una frecuencia de 1 MHz después de la división. Configuramos el valor de carga en 1000-1 = 9999, lo que resulta en una frecuencia de 1 kHz.

### Configuración del temporizador universal en el código

En `main.c`, iniciamos el temporizador:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_PWM_Start(&htim8,TIM_CHANNEL_1);

// Establecer el ciclo de trabajo en 500 (500 Hz/1 kHz=50%)
__HAL_TIM_SetCompare(&htim8,TIM_CHANNEL_1,500);

/* USER CODE END 2 */
```

Compilar y grabar, se puede ver la forma de onda con un osciloscopio:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210627154737.jpg)

## Referencias y agradecimientos

- [STM32CubeMX 实战教程（五）—— 通用定时器（PWM 输出）](https://blog.csdn.net/weixin_43892323/article/details/104776035)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
