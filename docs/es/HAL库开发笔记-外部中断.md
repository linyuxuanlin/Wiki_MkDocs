# Notas de desarrollo de la biblioteca HAL - Interrupciones externas

En el artículo anterior, mencionamos que eliminar el rebote de las teclas y detectar la entrada utilizando un método de encuesta constante podría consumir demasiados recursos del sistema y provocar bloqueos, o incluso perder algunas detecciones. Esto es precisamente por qué necesitamos utilizar interrupciones.

## Principios básicos

### Encuesta vs. Interrupción

¿Qué son la encuesta y las interrupciones? Para dar un ejemplo, la encuesta es como ir a la puerta cada minuto para ver si el repartidor de comida ha llegado. Durante ese tiempo, no podemos hacer nada más excepto esperar a que llegue la comida. Sin embargo, si el repartidor de comida llega justo cuando salimos de la puerta, perderemos la entrega. Por otro lado, las interrupciones son como recibir una llamada del repartidor cuando llega. Podemos dejar lo que estamos haciendo, recoger la comida y continuar trabajando sin preocuparnos de perderla.

### Interrupciones externas

Las interrupciones se dividen en externas (Interrupt) e internas (Exception). Las interrupciones externas son generadas por dispositivos externos que interrumpen el microcontrolador (MCU), mientras que las internas son generadas por programas de software internos que interrumpen el MCU.

### NVIC

NVIC significa Controlador de Interrupción Anidado de Vectores Múltiples, y sus siglas en inglés son **Nested Vectored Interrupt Controller**. Tiene tres parámetros principales: habilitar la interrupción, prioridad de prelación y prioridad de respuesta (cuanto menor es el valor de prioridad, mayor es la prioridad).

![NVIC](https://img.wiki-power.com/d/wiki-media/img/20210206121058.png)

**Habilitar la interrupción**: esto se refiere a si la interrupción está habilitada o no. Si está habilitada, cuando se cumplan las condiciones de activación de la interrupción, se ejecutará el servicio de interrupción. De lo contrario, el servicio de interrupción se ignorará y el programa principal continuará ejecutándose.

**Prioridad de prelación**: se utiliza para determinar si una interrupción puede interrumpir el servicio de otra interrupción, es decir, para tomar prioridad. Por ejemplo, si la condición para la interrupción A se cumple y el servicio de interrupción de A está en curso, si la prioridad de prelación de la interrupción B es mayor que la de A, el servicio de A se interrumpirá para ejecutar primero el servicio de B y luego se continuará con A. Esto se conoce como interrupción anidada. Si la prioridad de prelación de B no es mayor que la de A, el servicio de A se completará antes de ejecutar B.

**Prioridad de respuesta**: si varias interrupciones con la misma prioridad de prelación se activan al mismo tiempo, la de mayor prioridad de respuesta se ejecutará primero.

Para determinar la prioridad de una interrupción, primero se compara la prioridad de prelación. Si las prioridades de prelación son iguales, se determina según la tabla de vectores de interrupción.

### Referencia de funciones de devolución de llamada de interrupción

Una vez configuradas las interrupciones GPIO y las prioridades NVIC, se puede implementar la funcionalidad mediante la reescritura de las funciones de devolución de llamada de interrupción en el archivo `stm32f4xx_it.c`.

```c
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{

}

/* USER CODE END 1 */
```

## Control de luces mediante interrupciones externas de teclas

Antes de realizar experimentos adicionales, es necesario configurar varios parámetros, como la descarga de puertos serie y las configuraciones de reloj, en CubeMX. Para obtener instrucciones detalladas, consulte el artículo [**Notas de desarrollo de la biblioteca HAL - Configuración del entorno**](enlace_a_tu_artículo) en el método de configuración.

### Configuración de interrupciones en CubeMX

![Configuración de interrupciones en CubeMX](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

Como se muestra en la figura, el LED se configura como salida siguiendo el método descrito en el artículo anterior. Debido a que la tecla se activa a nivel bajo, lo que significa que genera un flanco descendente en el momento de presionarla, el pin debe configurarse como una interrupción activada por flanco descendente.

En mi placa, esto significa configurar `PI8` como modo `GPIO_EXTI8` (interrupción externa en la línea 8), y configurarlo como flanco descendente según el esquemático, eligiendo una resistencia interna de pull-up. Como se muestra en las imágenes:

![Configuración del pin para interrupción](https://img.wiki-power.com/d/wiki-media/img/20210403222304.png)

![Configuración de la resistencia pull-up](https://img.wiki-power.com/d/wiki-media/img/20210206131409.png)

A continuación, vaya a la etiqueta NVIC y habilite las interrupciones que ha configurado:

[Translation End]

```markdown
![](https://img.wiki-power.com/d/wiki-media/img/20210206134916.png)

Moreover, the priority of preemption needs to be lowered by one (from 0 to 1, as explained below).

### Configuring Interrupts in the Code

You only need to add the following code at the end of `stm32f4xx_it.c`:

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

The purpose of this code is to rewrite the callback function for the interrupt, adding the ability to toggle the LED on and off using the button. However, there is a caveat with the `HAL_Delay()` delay function because it originates from the SysTick timer (which generates interrupts at fixed time intervals), and therefore, it has its own interrupt priority. As shown in the NVIC configuration diagram above, both SysTick and the interrupt priority we configured are set to 0, so SysTick cannot be triggered immediately after an external interrupt. Hence, we need to lower the preemption priority of the external interrupt (from 0 to 1).

After compiling and uploading, you can switch the state of the LED on and off by pressing the button.

## References and Acknowledgments

- [Advanced Tutorial II [Interrupt]](https://alchemicronin.github.io/posts/ff6aca34/)
- [STM32CubeMX Practical Tutorial (Part Three) - External Interrupts (Avoiding Pitfalls with Interrupts and HAL_Delay Function)](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

[Reemplazo[1]]
[Reemplazo[2]]
```

**Spanish Translation:**

```markdown
![](https://img.wiki-power.com/d/wiki-media/img/20210206134916.png)

Además, la prioridad de prelación debe reducirse en uno (de 0 a 1, como se explica a continuación).

### Configuración de Interrupciones en el Código

Solo necesita agregar el siguiente código al final de `stm32f4xx_it.c`:

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

El propósito de este código es reescribir la función de devolución de llamada para la interrupción, agregando la capacidad de alternar el LED encendido y apagado utilizando el botón. Sin embargo, hay un detalle con la función de retardo `HAL_Delay()` porque proviene del temporizador SysTick (que genera interrupciones a intervalos de tiempo fijos) y, por lo tanto, tiene su propia prioridad de interrupción. Como se muestra en el diagrama de configuración NVIC anterior, tanto SysTick como la prioridad de interrupción que configuramos se establecen en 0, por lo que SysTick no puede ser activado inmediatamente después de una interrupción externa. Por lo tanto, debemos reducir la prioridad de prelación de la interrupción externa (de 0 a 1).

Después de compilar y cargar, puede cambiar el estado del LED encendido y apagado presionando el botón.

## Referencias y Agradecimientos

- [Tutorial Avanzado II [Interrupciones]](https://alchemicronin.github.io/posts/ff6aca34/)
- [Tutorial Práctico de STM32CubeMX (Parte Tres) - Interrupciones Externas (Evitando Problemas con Interrupciones y la Función HAL_Delay)](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

[Reemplazo[1]]
[Reemplazo[2]]
```

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.