# HAL Library Development Notes - External Interrupts

In the previous article, we mentioned that eliminating key bounce and detecting input using a polling method might consume excessive system resources, leading to system sluggishness, or potentially missing detections. This is why we need to use interrupts.

## Basic Principles

### Polling vs. Interrupts

What are polling and interrupts? To illustrate, consider ordering takeout. Polling is like going to the doorstep every minute to check if the delivery person has arrived. During this time, you can't do anything else but wait for the delivery. If the delivery person arrives while you happen to step away from the door, you'll miss the delivery. In contrast, interrupts are like having the delivery person call you when they arrive. You can continue with your tasks and don't have to worry about missing the delivery.

### External Interrupts

Interrupts can be categorized as external (Interrupt) or internal (Exception). External interrupts are triggered by external peripherals, while internal interrupts are initiated by the software programs within the MCU.

### NVIC

NVIC stands for Nested Vectored Interrupt Controller. It has three main parameters: interrupt enable, preemption priority, and subpriority. (Lower priority values indicate higher priority.)

**Interrupt enable:** This indicates whether interrupts are enabled. If interrupts are enabled, when the conditions for interrupt triggering are met, the program will jump to the interrupt service routine. Otherwise, it will ignore the interrupt service routine and continue running the main program.

**Preemption priority:** It is used to determine if one interrupt can preempt another interrupt's service routine and run before it. For example, if condition A triggers interrupt A, and interrupt A's service routine is running, and then condition B triggers interrupt B, if interrupt B's preemption priority is higher than that of interrupt A, it will interrupt and execute interrupt B's service routine first, and then continue with interrupt A, which is known as interrupt nesting. If B's preemption priority is not higher than A's, it will finish executing A first before processing B.

**Subpriority:** If multiple interrupts with the same preemption priority are triggered simultaneously, the one with the higher subpriority will run first.

To determine the interrupt priority, you should first compare the preemption priority. If preemption priorities are the same, the interrupt with the higher subpriority will have a higher priority. If both priorities are identical, you'll need to consult the interrupt vector table.

### Interrupt Callback Function Reference

After configuring GPIO interrupts and NVIC priorities, you can implement the functionality by rewriting the interrupt callback function at the end of the `stm32f4xx_it.c` file:

```c
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{

}

/* USER CODE END 1 */
```

## External Interrupt for Controlling LEDs with Buttons

Before proceeding with the next experiment, you need to configure various parameters such as serial downloading and clocks in CubeMX. For specific steps, please refer to the article [**HAL Library Development Notes - Environment Configuration**](to_be_replaced[3]).

### Configuring Interrupts in CubeMX

![Configuring Interrupts in CubeMX](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

As shown in the diagram, configure the LED as an output following the method described in the previous article. For the button, since it triggers on a low level, generating a falling edge at the moment of pressing, configure the pin as an interrupt triggered on a falling edge.

On my board, this means configuring `PI8` as `GPIO_EXTI8` mode (external interrupt, attached to interrupt line 8) and configuring it for falling edge triggering with internal pull-up, as shown in the images.

![Configuring GPIO_EXTI8](https://img.wiki-power.com/d/wiki-media/img/20210403222304.png)

![Pull-up Configuration](https://img.wiki-power.com/d/wiki-media/img/20210206131409.png)

Next, jump to the NVIC tab page and enable the interrupts you've configured.

![](https://img.wiki-power.com/d/wiki-media/img/20210206134916.png)

Furthermore, it is necessary to lower the preemptive priority by one (from 0 to 1, the reason for this will be explained below).

### Configuring Interrupts in the Code

You simply need to add the following code to the end of `stm32f4xx_it.c`:

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

The purpose of this code is to override the callback function for interrupts and add the functionality of toggling the LED with a button press. However, there is a caveat with the `HAL_Delay()` delay function because it relies on the SysTick timer (which generates interrupts at fixed time intervals) and, therefore, has its own interrupt priority. As shown in the NVIC configuration diagram above, both SysTick and the interrupt preemptive priority we configured are set to 0. Consequently, it won't be possible for SysTick to trigger immediately after an external interrupt. To address this, we need to lower the preemptive priority of the external interrupt (from 0 to 1).

After compiling and uploading, you can switch the LED on and off by pressing the button.

## References and Acknowledgments

- [Advanced Guide II [Interrupt]](https://alchemicronin.github.io/posts/ff6aca34/)
- [STM32CubeMX Practical Tutorial (Part 3) - External Interrupts (Avoiding Pitfalls with Interrupts and HAL_Delay Function)](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

[Replace with the appropriate references]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.