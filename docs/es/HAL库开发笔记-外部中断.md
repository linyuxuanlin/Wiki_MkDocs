# Notas de desarrollo de la biblioteca HAL: Interrupciones externas

En el artículo anterior mencionamos que el uso del método de encuesta para eliminar el rebote de los botones y detectar la entrada puede consumir demasiados recursos del sistema y causar bloqueos, o incluso perder la detección. Por eso necesitamos utilizar interrupciones.

## Principios básicos

### Encuesta vs Interrupciones

¿Qué es la encuesta y qué son las interrupciones? Tomemos como ejemplo pedir comida a domicilio. La encuesta sería ir a la puerta cada minuto para ver si ha llegado el repartidor. Durante ese tiempo no puedo hacer otra cosa más que esperar la comida; pero si el repartidor llega justo cuando me alejo de la puerta, me perderé la entrega. Por otro lado, una interrupción sería llamar al repartidor cuando llega, dejar lo que estoy haciendo y recoger la comida. De esta manera puedo seguir trabajando tranquilamente sin perderme la entrega.

### Interrupciones externas

Las interrupciones se dividen en externas (Interrupt) e internas (Exception). Las interrupciones externas son generadas por dispositivos externos que interrumpen al MCU, mientras que las internas son generadas por programas de software internos que interrumpen al MCU.

### NVIC

NVIC significa Nested Vectored Interrupt Controller, que se traduce como **Controlador de Interrupciones Vectorizadas Anidadas**. Tiene tres parámetros principales: habilitación de interrupciones, prioridad de prelación y prioridad de respuesta (a menor valor, mayor prioridad).

![](https://media.wiki-power.com/img/20210206121058.png)

**Habilitación de interrupciones**: se refiere a si se activa o no la interrupción. Si se habilita la interrupción, cuando se cumpla la condición de activación de la interrupción, se saltará a la ejecución del programa de servicio de interrupción; de lo contrario, el programa de servicio de interrupción no se tendrá en cuenta y se seguirá ejecutando el programa principal.

**Prioridad de prelación**: se utiliza para determinar si una interrupción puede interrumpir a otra interrupción y ejecutarse primero. Por ejemplo, si se cumple la condición de activación de la interrupción A y el programa de servicio de la interrupción A está en ejecución, y en ese momento se cumple la condición de activación de la interrupción B. Si la prioridad de prelación de la interrupción B es mayor que la de la interrupción A, el programa de servicio de la interrupción A se interrumpirá y se ejecutará primero el programa de servicio de la interrupción B, y una vez finalizado, se continuará con la ejecución del programa de servicio de la interrupción A. Esto se conoce como anidamiento de interrupciones. Si la prioridad de prelación de B no es mayor que la de A, entonces se ejecutará primero A y luego B.

**Prioridad de respuesta**: si varias interrupciones con la misma prioridad de prelación se activan al mismo tiempo, la de mayor prioridad de respuesta se ejecutará primero.

Para determinar la prioridad de una interrupción, primero se compara la prioridad de prelación. Si la prioridad de prelación es la misma, se compara la prioridad de respuesta. Si ambas prioridades son iguales, se debe consultar la tabla de vectores de interrupción.

### Referencia de la función de devolución de llamada de interrupción

Después de configurar la interrupción GPIO y la prioridad NVIC, se puede implementar la función de devolución de llamada de interrupción en el archivo `stm32f4xx_it.c` para que funcione.

```c
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{

}

/* USER CODE END 1 */
```

## Control de luz mediante interrupción de botón externo

Antes de continuar con el siguiente experimento, es necesario configurar varios parámetros en CubeMX, como la descarga a través del puerto serie y la configuración del reloj.  
Para obtener instrucciones detalladas, consulte el artículo [**Notas de desarrollo de la biblioteca HAL: Configuración del entorno**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) en el método de configuración.

### Configuración de la interrupción en CubeMX

![](https://media.wiki-power.com/img/20210205150422.png)

Como se muestra en la imagen, el LED se configura como salida utilizando el método descrito en el artículo anterior. El botón, debido a que es activado por nivel bajo, es decir, genera un flanco descendente en el momento de ser presionado, por lo que el pin debe configurarse como una interrupción activada por flanco descendente.

En mi placa, se configura el pin `PI8` como modo `GPIO_EXTI8` (interrupción externa, conectada a la línea de interrupción 8) y se configura como flanco descendente. Según el esquemático, se selecciona la resistencia de pull-up interna. Como se muestra en la imagen:

![](https://media.wiki-power.com/img/20210403222304.png)

![](https://media.wiki-power.com/img/20210206131409.png)

A continuación, haga clic en la pestaña NVIC para habilitar la interrupción configurada.

![](https://media.wiki-power.com/img/20210206134916.png)

Además, se debe reducir en un nivel la prioridad de prelación (de 0 a 1, la razón se explicará más adelante).

### Configuración de interrupciones en el código

Solo es necesario agregar el siguiente código al final de `stm32f4xx_it.c`:

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

Este fragmento de código tiene la función de reescribir la función de devolución de llamada de la interrupción, agregando la función de cambiar el estado del LED con un botón. Sin embargo, la función de retardo `HAL_Delay()` tiene un problema, ya que su fuente es el temporizador SysTick (que genera interrupciones en intervalos de tiempo fijos), por lo que tiene su propia prioridad de interrupción. En el diagrama de configuración del NVIC mostrado anteriormente, se puede ver que tanto SysTick como la prioridad de prelación de la interrupción que configuramos son 0, por lo que no se puede activar SysTick después de una interrupción externa. Por lo tanto, debemos cambiar la prioridad de prelación de la interrupción externa a un nivel más bajo (de 0 a 1).

Después de compilar y cargar el código, se puede cambiar el estado del LED al presionar el botón.

## Referencias y agradecimientos

- [Advanced Part II [Interrupt]](https://alchemicronin.github.io/posts/ff6aca34/)
- [STM32CubeMX Practical Tutorial (Part III) - External Interrupts (Interrupt and HAL_Delay Function Pitfalls)](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
