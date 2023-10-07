# HAL Library Development Notes - Basic Timer (TIM)

In STM32, there are three types of timers: basic, general-purpose, and advanced timers, used for handling various periodic tasks. In this article, I will provide a detailed introduction to the basic timer.

## Basic Principles

The timers we commonly use are divided into three categories: basic, general-purpose, and advanced timers. In the STM32F4 series microcontroller, they correspond to the following:

- Basic Timer
  - TIM6
  - TIM7
- General-purpose Timer
  - TIM2-TIM5
  - TIM9-TIM14
- Advanced Timer
  - TIM1
  - TIM8
- (SysTick Timer)

Usually, we use the basic timer as a timer and the general-purpose timer to output PWM signals.

### Characteristics of Basic Timer

In the STM32F4 series microcontroller, the characteristics of the two basic timers, TIM6 and TIM7, are as follows:

- Mounted on the APB1 bus
- 16-bit auto-reload incrementing counter
- 16-bit programmable prescaler for dividing the counter clock frequency (i.e., modified at runtime), with a division factor between 1 and 65536
- Used for triggering the synchronous circuit of the DAC
- Generates interrupt/DMA requests when a counter overflow update event occurs

### Common Timer Function Reference

- **HAL_TIM_Base_Init()**: Initializes the timer base unit
- **HAL_TIM_Base_DeInit()**: Disables the timer, opposite of initialization
- **HAL_TIM_Base_MspInit()**: MSP initialization function, automatically called during timer initialization
- **HAL_TIM_Base_MspDeInit()**: Opposite of the previous function
- **HAL_TIM_Base_Start()**: Starts the timer
- **HAL_TIM_Base_Stop()**: Stops the timer
- **HAL_TIM_Base_Start_IT()**: Starts the timer in interrupt mode
- **HAL_TIM_Base_Stop_IT()**: Stops the timer in interrupt mode
- **HAL_TIM_Base_Start_DMA()**: Starts the timer in DMA mode
- **HAL_TIM_Base_Stop_DMA()**: Stops the timer in DMA mode

## Use Basic Timer to Make LED Blink

This experiment uses the basic timer to implement a timing function that makes the LED switch status every 0.5 seconds.

### Configuring the Basic Timer in CubeMX

First, we open the Clock Configuration page and find the value of APB1 Timer clocks on the far right:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210407152250.png)

This is because the STM32F4 series TIM2-TIM7, TIM12-TIM14 are mounted on the low-speed APB1 bus, while TIM1, TIM8-TIM11 are mounted on the high-speed APB2 bus. We will be using the basic timer TIM6, so we need to look at the speed of APB1 (which is 90 MHz after division and multiplication).

Next, we find TIM6 in the Timer sidebar, activate the timer by checking "Activated", and configure the following parameters below:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210407173136.png)

The meanings of each parameter are:

- **Prescaler**: 8999
- **Counter Mode**: Up (counting from 0 to the prescaler value and then overflowing)
- **Counter Period**: 4999 (the timer will count 5000 times per period)
- **auto-reload preload**: Enable (the initial value will be automatically reloaded when the timer overflows)

Since we are using a clock source of 90 MHz, we set the prescaler to 8999 (which is a division of 9000), resulting in a frequency of 10 kHz (90 MHz/9000). The counter period is set to 4999 (counting 5000 times per period), resulting in a period of 500 ms.

Then, in the NVIC tab, we enable interrupts:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210407155959.png)

### Configuring the Basic Timer in the Code

In `main.c`, we start the timer:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_Base_Start_IT(&htim6);

/* USER CODE END 2 */
```

Add callback function in `stm32f4xx_it.c`:

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

For LED configuration, please refer to the previous article [**HAL Development Notes - GPIO**](https://wiki-power.com/en/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0%EF%BC%88%E4%BA%8C%EF%BC%89-GPIO).

After downloading and burning, we can see that the LED switches its state according to the preset 500ms period (that is, an overflow event occurs every 500ms, and we flip the LED in the callback function).

## Reference and Acknowledgement

- [STM32CubeMX Practical Tutorial (Part Four) - Basic Timer (Still Blinking)](https://blog.csdn.net/weixin_43892323/article/details/104534920)
- [Advanced VI [Timer & PWM]](https://alchemicronin.github.io/posts/fd31d369/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.