# Notas de desarrollo de la biblioteca HAL - Interrupción externa

En el artículo anterior, mencionamos que eliminar el rebote de los botones y detectar la entrada mediante encuesta puede consumir demasiados recursos del sistema y provocar bloqueos, y también puede perder la detección. Es por eso que necesitamos usar interrupciones.

## Principios básicos

### Encuesta e interrupción

¿Qué son la encuesta y la interrupción? Tomemos la entrega de comida como ejemplo. La encuesta es que tengo que ir a la puerta cada minuto para ver si el repartidor de comida ha llegado. Entonces, durante este tiempo, no puedo hacer nada más que mirar la comida; pero si el repartidor de comida llega justo cuando salgo de la puerta, entonces perderé la comida. Por el contrario, la interrupción es que cuando llega el repartidor de comida, me llama por teléfono, dejo lo que estoy haciendo y voy a buscar la comida, de esta manera puedo trabajar con tranquilidad y no perder la comida.

### Interrupción externa

Las interrupciones se dividen en externas (Interrupt) e internas (Exception). La interrupción externa es interrumpida por un dispositivo externo al MCU, y la interrupción interna es interrumpida por el programa de software interno.

### NVIC

NVIC significa Nested Vectored Interrupt Controller, que se traduce como **Controlador de interrupción vectorial anidado**. Tiene tres parámetros principales: habilitación de interrupción, prioridad de preempción y prioridad de respuesta. (Cuanto menor sea el valor de prioridad, mayor será la prioridad).

![](https://img.wiki-power.com/d/wiki-media/img/20210206121058.png)

**Habilitación de interrupción**: se refiere a si se habilita la interrupción. Si se habilita la interrupción, cuando se cumple la condición de activación de la interrupción, se saltará al programa de servicio de interrupción para ejecutar; de lo contrario, el programa de servicio de interrupción no se tendrá en cuenta y el programa principal seguirá ejecutándose.

**Prioridad de preempción**: se utiliza para determinar si una interrupción puede interrumpir el programa de servicio de otra interrupción y ejecutarse primero. Tomemos un ejemplo. Se cumple la condición de activación de la interrupción A, el programa de servicio de la interrupción A está en ejecución, y en este momento se cumple la condición de activación de la interrupción B. Si la prioridad de preempción de la interrupción B es mayor que la de la interrupción A, el programa de servicio de la interrupción A será interrumpido y se ejecutará primero el programa de servicio de la interrupción B, y luego se continuará ejecutando la interrupción A. Esto también se llama interrupción anidada. Si la prioridad de preempción de B no es mayor que la de A, entonces primero se ejecutará A y luego se ejecutará B.

**Prioridad de respuesta**: si varias interrupciones con la misma prioridad de preempción se activan al mismo tiempo, se ejecutará primero la de mayor prioridad de respuesta.

Para determinar la prioridad de la interrupción, primero debe compararse la prioridad de preempción. Si la prioridad de preempción es la misma, la interrupción con la prioridad de respuesta más alta tiene una prioridad más alta. Si ambas prioridades son iguales, entonces se debe determinar según la tabla de vectores de interrupción.

### Referencia de la función de devolución de llamada de interrupción

Después de configurar la interrupción GPIO y la prioridad NVIC, simplemente reescriba la función de devolución de llamada de interrupción al final del archivo `stm32f4xx_it.c` para implementar la función.

```c
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{

}

/* USER CODE END 1 */
```

## Control de luz de tecla de interrupción externa

Antes de realizar el siguiente experimento, debe configurar varios parámetros como la descarga de serie, el reloj, etc. en CubeMX.  
Para obtener información detallada, consulte el método en el artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del entorno**](https://wiki-power.com/es/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE).

### Configuración de interrupción en CubeMX

![](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

Como se muestra en la figura, el LED todavía se configura como salida utilizando el método del artículo anterior; debido a que la tecla es activada por nivel bajo, es decir, se genera un flanco descendente en el momento de la presión, el pin debe configurarse como una interrupción activada por flanco descendente.

En mi placa, se configura `PI8` como modo `GPIO_EXTI8` (interrupción externa, montada en la línea de interrupción 8) y se configura como activada por flanco descendente. Según el esquemático, se selecciona la resistencia pull-up interna. Como se muestra en la figura:

![](https://img.wiki-power.com/d/wiki-media/img/20210403222304.png)

Configuración de interrupciones externas en STM32CubeMX

En este tutorial, aprenderemos cómo configurar interrupciones externas en STM32CubeMX para controlar el encendido y apagado de un LED mediante un botón.

## Requisitos previos

- STM32CubeMX
- IDE de desarrollo de STM32 (por ejemplo, STM32CubeIDE)
- Placa de desarrollo STM32

## Configuración de hardware

Conecte un botón y un LED a la placa de desarrollo STM32. En este tutorial, usaremos el botón KEY1 y el LED LED1.

## Configuración de software

### Configuración de pines

Abra STM32CubeMX y cree un nuevo proyecto. Seleccione la placa de desarrollo STM32 que está utilizando y configure los pines correspondientes al botón y al LED.

En este tutorial, el botón KEY1 está conectado al pin PA0 y el LED LED1 está conectado al pin PD12.

### Configuración de interrupciones externas

Haga clic en la pestaña NVIC y habilite la interrupción externa correspondiente al pin del botón. En este tutorial, la interrupción externa correspondiente al pin PA0 se habilita.

A continuación, haga clic en la página de etiquetas NVIC para habilitar la interrupción que hemos configurado.

Además, debemos reducir la prioridad de prelación en un nivel (de 0 a 1, se explicará más adelante).

### Configuración de interrupciones en el código

Solo necesitamos agregar el siguiente código al final de `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if(HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0)
    {
        HAL_Delay(100);
        if(HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0)
        {
            HAL_GPIO_TogglePin(LED1_GPIO_Port,LED1_Pin);
        }
    }
}

/* USER CODE END 1 */
```

Este código reescribe la función de devolución de llamada de la interrupción y agrega la función de cambiar el estado del LED mediante el botón. Sin embargo, la función de retardo `HAL_Delay()` tiene un problema porque proviene del temporizador SysTick (genera interrupciones en intervalos de tiempo fijos), por lo que tiene una prioridad de interrupción correspondiente. En la figura de configuración NVIC anterior, podemos ver que SysTick y la prioridad de prelación de la interrupción que configuramos son ambos 0, por lo que no se puede continuar con SysTick después de que se produce una interrupción externa. Por lo tanto, debemos reducir la prioridad de prelación de la interrupción externa (de 0 a 1).

Después de compilar y cargar el código, puede cambiar el estado del LED presionando el botón.

## Referencias y agradecimientos

- [Advanced II [Interrupt]](https://alchemicronin.github.io/posts/ff6aca34/)
- [STM32CubeMX Practical Tutorial (3) - External Interrupts (Interrupts and HAL_Delay Function Pitfalls)](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
