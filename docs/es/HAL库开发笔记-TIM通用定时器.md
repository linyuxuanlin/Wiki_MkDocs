# Apuntes de desarrollo de la biblioteca HAL - Temporizador universal TIM

En el artículo anterior, presentamos brevemente las tres clases de temporizadores del STM32F4 y proporcionamos una explicación detallada del temporizador básico. En este artículo, continuaremos explorando el temporizador universal.

## Principios fundamentales

En el STM32F4, los temporizadores universales comprenden TIM2-TIM5 y TIM9-TIM14.

### Características de los temporizadores universales

En el STM32F4, los temporizadores universales tienen las siguientes características:

- Contadores que aumentan, disminuyen o aumentan/disminuyen automáticamente de 16/32 bits.
- Un predivisor programable de 16 bits que se utiliza para dividir la frecuencia del reloj del contador (con un factor de división de 1-65536).
- Cuatro canales independientes que se pueden utilizar para:
  - Captura de entrada.
  - Comparación de salida.
  - Generación de PWM (modo de borde y alineación central).
  - Salida de modo de pulso único.
- Posibilidad de controlar el temporizador mediante señales externas y lograr la sincronización de múltiples temporizadores.
- Generación de interrupciones o solicitudes de DMA en los siguientes eventos:
  - Actualización: desbordamiento o subdesbordamiento del contador, inicialización del contador (a través de software o disparo interno/externo).
  - Evento de disparo (inicio, parada, inicialización del contador o contador disparado interna/externamente).
  - Captura de entrada.
  - Comparación de salida.
- Soporte para encoders incrementales (cuadratura) y circuitos de sensores Hall.
- Entrada de disparo de reloj externo o gestión de corriente periódica.

### Referencia de funciones de temporizador comunes

A continuación, se presentan funciones comunes de temporizador que son similares a las del temporizador básico.

- **HAL_TIM_Base_Init()**: Inicializa la unidad base del temporizador.
- **HAL_TIM_Base_DeInit()**: Desactiva el temporizador, en sentido contrario a la inicialización.
- **HAL_TIM_Base_MspInit()**: Función de inicialización de MSP que se llama automáticamente durante la inicialización del temporizador.
- **HAL_TIM_Base_MspDeInit()**: Lo opuesto a la función anterior.
- **HAL_TIM_Base_Start()**: Inicia el temporizador.
- **HAL_TIM_Base_Stop()**: Detiene el temporizador.
- **HAL_TIM_Base_Start_IT()**: Inicia el temporizador en modo de interrupción.
- **HAL_TIM_Base_Stop_IT()**: Detiene el temporizador en modo de interrupción.
- **HAL_TIM_Base_Start_DMA()**: Inicia el temporizador en modo DMA.
- **HAL_TIM_Base_Stop_DMA()**: Detiene el temporizador en modo DMA.

## Generación de PWM al 1 kHz con un ciclo de trabajo del 50% mediante el temporizador universal

En esta ocasión, vamos a generar una señal PWM de 1 kHz con un ciclo de trabajo del 50% utilizando un temporizador universal. La forma de onda resultante se puede visualizar utilizando un osciloscopio.

### Configuración en CubeMX

En primer lugar, abrimos la página de configuración del árbol de relojes en Clock Configuration, ya que los temporizadores universales se encuentran en el bus APB2 de alta velocidad. A continuación, encontramos y anotamos la frecuencia de reloj de APB2 Timer clocks (180 MHz):

![Frecuencia de reloj APB2](https://img.wiki-power.com/d/wiki-media/img/20210627133951.png)

A continuación, en la barra lateral de temporizadores, localizamos TIM8 y configuramos el Canal 1 (`Channel 1`) para la generación PWM (`PWM Generation CH1`). Para lograr una frecuencia de PWM de 1 kHz, configuramos los siguientes parámetros:

- **Prescaler** (predivisor): 180-1
- **Counter Mode** (modo del contador): Up (contando hacia arriba desde 0 hasta el valor del predivisor antes de desbordarse).
- **Counter Period** (período del contador/valor de recarga): 1000-1
- **Auto-reload preload** (recarga automática): Habilitada (se recargará automáticamente cuando se desborde).

![Configuración TIM8](https://img.wiki-power.com/d/wiki-media/img/20210627153422.png)

Dado que la fuente de reloj utilizada aquí es de 180 MHz, configuramos el predivisor en 180-1 = 179, lo que resulta en una frecuencia de 1 MHz. Luego, configuramos el valor de recarga en 1000-1 = 9999, lo que nos da una frecuencia de 1 kHz.

### Configuración en el código

Para habilitar el temporizador en `main.c`:

```c title="main.c"
/* USER CODE BEGIN 2 */
```

```markdown
```c
HAL_TIM_PWM_Start(&htim8, TIM_CHANNEL_1);

// Set the duty cycle to 500 (500 Hz/1 kHz=50%)
__HAL_TIM_SetCompare(&htim8, TIM_CHANNEL_1, 500);

/* USER CODE END 2 */
```

After compiling and flashing, you can observe the waveform using an oscilloscope:

![Waveform](https://img.wiki-power.com/d/wiki-media/img/20210627154737.jpg)

## References and Acknowledgments

- [STM32CubeMX Practical Tutorial (Part Five) - General Timer (PWM Output)](https://blog.csdn.net/weixin_43892323/article/details/104776035)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```

```markdown
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.