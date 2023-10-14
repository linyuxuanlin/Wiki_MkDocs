# HAL Library Development Notes - External Interrupt

In the previous article, we mentioned that using polling to eliminate button bouncing and detect input may consume too many system resources and cause the system to freeze, or it may miss the detection. That's why we need to use interrupts.

## Basic Principles

### Polling vs Interrupts

What are polling and interrupts? Let's take the example of ordering takeout. Polling is like checking the doorstep every minute to see if the delivery person has arrived. During this time, you can't do anything else but wait for the delivery. But if the delivery person arrives when you happen to be away from the doorstep, you will miss the delivery. On the other hand, interrupts are like receiving a phone call from the delivery person when they arrive. You can put down what you're doing and go get the delivery, so you can work without worrying about missing the delivery.

### External Interrupts

Interrupts can be divided into external (Interrupt) and internal (Exception). External interrupts are triggered by external peripherals to interrupt the MCU, while internal interrupts are triggered by internal software programs to interrupt the MCU.

### NVIC

NVIC stands for Nested Vectored Interrupt Controller. It has three main parameters: interrupt enable, preemption priority, and response priority. (The lower the priority value, the higher the priority.)

![](https://img.wiki-power.com/d/wiki-media/img/20210206121058.png)

**Interrupt Enable**: This refers to whether the interrupt is enabled. If the interrupt is enabled, when the interrupt trigger condition is met, the interrupt service program will be executed. Otherwise, the interrupt service program will be ignored and the main program will continue to run.

**Preemption Priority**: This is used to determine whether an interrupt can interrupt another interrupt service program and run first. For example, if condition A triggers interrupt A and the service program of interrupt A is running, and at this time condition B triggers interrupt B. If the preemption priority of interrupt B is higher than that of interrupt A, the service program of interrupt A will be interrupted and the service program of interrupt B will be executed first. After it is finished, the service program of interrupt A will continue to run. This is also called interrupt nesting. If the preemption priority of B is not higher than that of A, then A will be executed first, and then B.

**Response Priority**: If several interrupts with the same preemption priority are triggered at the same time, the one with the higher response priority will run first.

To determine the priority of an interrupt, first compare the preemption priority. If the preemption priorities are the same, the interrupt with the higher response priority has a higher priority. If both priorities are the same, then the interrupt vector table is used to determine the priority.

### Interrupt Callback Function Reference

After configuring GPIO interrupts and NVIC priorities, you can implement the function by rewriting the interrupt callback function at the end of the `stm32f4xx_it.c` file.

```c
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{

}

/* USER CODE END 1 */
```

## External Interrupt Button Controls LED

Before proceeding to the next experiment, various parameters such as serial port download and clock need to be configured in CubeMX. For specific steps, please refer to the method in the article [**HAL Library Development Notes - Environment Configuration**](https://wiki-power.com/en/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE).

### Configuring Interrupts in CubeMX

![](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

As shown in the figure, the LED is still configured as output using the method in the previous article. Since the button is triggered by a low level, that is, a falling edge is generated at the moment of pressing, the pin should be configured as an interrupt triggered by a falling edge.

On my board, `PI8` is configured as `GPIO_EXTI8` mode (external interrupt, mounted on interrupt line 8), and configured as a falling edge trigger. According to the schematic diagram, select internal pull-up (Pull-up). As shown in the figure:

![](https://img.wiki-power.com/d/wiki-media/img/20210403222304.png)

![](https://img.wiki-power.com/d/wiki-media/img/20210206131409.png)

Next, click the NVIC label page to enable the interrupt we configured:

![](https://img.wiki-power.com/d/wiki-media/img/20210206134916.png)

In addition, the preemption priority should be lowered by one (from 0 to 1, the reason will be explained below).

### Configuring Interrupts in Code

Simply add the following code to the end of `stm32f4xx_it.c`:

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

This code overrides the interrupt callback function and adds the ability to toggle the LED on and off with a button. However, the `HAL_Delay()` function has a pitfall because it relies on the SysTick timer (which generates interrupts at fixed intervals), and therefore has a priority level. As shown in the NVIC configuration diagram above, both SysTick and our configured interrupt have a preemption priority of 0, so SysTick cannot be triggered after an external interrupt is triggered. Therefore, we need to lower the preemption priority of the external interrupt (from 0 to 1).

After compiling and uploading, you can toggle the LED on and off by pressing the button.

## References and Acknowledgements

- [Advanced Part II [Interrupt]](https://alchemicronin.github.io/posts/ff6aca34/)
- [STM32CubeMX Practical Tutorial (Part III) - External Interrupts (Avoiding Pitfalls in Interrupts and HAL_Delay Function)](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
