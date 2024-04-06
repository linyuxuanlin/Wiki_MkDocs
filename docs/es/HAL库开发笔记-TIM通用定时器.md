# Notas de desarrollo de la biblioteca HAL - Temporizador universal TIM

En el artículo anterior, proporcionamos una introducción básica a los tres tipos de temporizadores disponibles en STM32F4, centrándonos especialmente en el temporizador básico. En esta ocasión, continuaremos explorando el temporizador universal.

## Principios fundamentales

En la serie STM32F4, los temporizadores universales abarcan TIM2-TIM5 y TIM9-TIM14.

### Características del temporizador universal

Los temporizadores universales en STM32F4 presentan las siguientes características:

- Contador de recarga automática de 16/32 bits en modos ascendente, descendente y ascendente/descendente.
- Un predivisor programable de 16 bits que permite dividir la frecuencia del reloj del contador (con un factor de división entre 1 y 65536).
- Cuatro canales independientes que pueden utilizarse para las siguientes funciones:
  - Captura de entrada
  - Comparación de salida
  - Generación de PWM (en modos de borde y alineación central)
  - Salida en modo pulso único
- Posibilidad de controlar el temporizador mediante señales externas y sincronizar múltiples temporizadores con circuitos sincrónicos.
- Generación de interrupciones/solicitudes DMA en respuesta a los siguientes eventos:
  - Actualización: desbordamiento o subdesbordamiento del contador, inicialización del contador (a través de software o activación interna/externa).
  - Eventos de activación (inicio, parada, inicialización del contador o conteo a través de activación interna/externa).
  - Captura de entrada
  - Comparación de salida
- Admite la localización de codificadores incrementales (cuadratura) y circuitos de sensores Hall.
- Entrada de reloj externo o gestión de corriente periódica por disparo.

### Referencia de funciones de temporizador comunes

A continuación, se presentan las funciones comunes del temporizador, que son idénticas a las del temporizador básico.

- **HAL_TIM_Base_Init()**: Inicializa la unidad base del temporizador.
- **HAL_TIM_Base_DeInit()**: Deshabilita el temporizador, contrario a la inicialización.
- **HAL_TIM_Base_MspInit()**: Función de inicialización MSP que se llama automáticamente durante la inicialización del temporizador.
- **HAL_TIM_Base_MspDeInit()**: Contraparte de la función anterior.
- **HAL_TIM_Base_Start()**: Inicia el temporizador.
- **HAL_TIM_Base_Stop()**: Detiene el temporizador.
- **HAL_TIM_Base_Start_IT()**: Inicia el temporizador en modo de interrupción.
- **HAL_TIM_Base_Stop_IT()**: Detiene el temporizador en modo de interrupción.
- **HAL_TIM_Base_Start_DMA()**: Inicia el temporizador en modo DMA.
- **HAL_TIM_Base_Stop_DMA()**: Detiene el temporizador en modo DMA.

## Generar una señal PWM del 1 kHz con un ciclo de trabajo del 50% utilizando el temporizador universal

En este experimento, generaremos una señal PWM con una frecuencia de 1 kHz y un ciclo de trabajo del 50% utilizando el temporizador universal. Luego, podremos visualizar la forma de onda de la señal utilizando un osciloscopio.

### Configuración del temporizador universal en CubeMX

En primer lugar, abriremos la página de configuración del árbol de reloj en "Clock Configuration" (Configuración del reloj). Dado que el temporizador universal está en la línea de alta velocidad APB2, buscaremos y anotaremos la frecuencia del reloj de "APB2 Timer clocks" (Relojes de temporizadores APB2) (180 MHz):

![Captura de pantalla](https://media.wiki-power.com/img/20210627133951.png)

A continuación, en el lateral, encontraremos TIM8, donde configuraremos el canal 1 (`Channel 1`) para la generación de PWM (`PWM Generation CH1`). Para lograr una frecuencia de 1 kHz para la onda cuadrada PWM, configuraremos los siguientes parámetros:

- **Predivisor** (Factor de división): 180-1
- **Modo de contador**: Ascendente (comenzando desde 0 y contando hacia arriba hasta el valor del factor de división).
- **Período de contador**: 1000-1
- **Recarga automática de periodo**: Habilitada (el valor se recargará automáticamente al desbordar).

![Captura de pantalla](https://media.wiki-power.com/img/20210627153422.png)

Dado que la fuente de reloj utilizada aquí es de 180 MHz, configuramos el factor de división en 180-1 = 179, lo que resulta en una frecuencia de 1 MHz después de la división. Luego, configuramos el valor del período en 1000-1 = 9999 para obtener una frecuencia de 1 kHz.

### Configuración del temporizador en el código

En el archivo `main.c`, iniciaremos el temporizador:

```c title="main.c"
/* USER CODE BEGIN 2 */
```

Espero que esta traducción sea útil. Si tienes alguna pregunta adicional o necesitas más ayuda, no dudes en preguntar.

````markdown
Inicie la modulación por ancho de pulso (PWM) en el canal 1 del temporizador HAL_TIM8:

```c
HAL_TIM_PWM_Start(&htim8, TIM_CHANNEL_1);
```
````

Luego, configure el ciclo de trabajo al 50% (500 en una escala de 1000) de la señal PWM generada a 500 Hz (500 Hz / 1 kHz = 50%):

```c
__HAL_TIM_SetCompare(&htim8, TIM_CHANNEL_1, 500);
```

Una vez realizadas estas configuraciones, compile y grabe el código en el dispositivo. Puede observar la forma de onda utilizando un osciloscopio:

![Forma de onda](https://media.wiki-power.com/img/20210627154737.jpg)

## Referencias y Agradecimientos

- [STM32CubeMX Tutorial Práctico (Parte Cinco) - Temporizador General (Salida PWM)](https://blog.csdn.net/weixin_43892323/article/details/104776035)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
