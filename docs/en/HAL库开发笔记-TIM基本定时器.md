# HAL Library Development Notes - TIM Basic Timer

In the STM32 ecosystem, we have three types of timers: basic timers, general-purpose timers, and advanced timers, each designed for handling various periodic tasks. In this article, I'll provide a detailed overview of basic timers.

## Fundamental Principles

The timers we typically use are categorized into basic, general-purpose, and advanced timers. For the STM32F4 series microcontrollers, the corresponding timers are as follows:

- Basic Timers
  - TIM6
  - TIM7
- General-Purpose Timers
  - TIM2-TIM5
  - TIM9-TIM14
- Advanced Timers
  - TIM1
  - TIM8
- (SysTick Timer)

Usually, we use basic timers for timekeeping purposes and general-purpose timers for generating PWM signals.

### Characteristics of Basic Timers

In the STM32F4 series microcontrollers, TIM6 and TIM7, the two basic timers, exhibit the following characteristics:

- Mounted on the APB1 bus
- 16-bit auto-reload incrementing counter
- 16-bit programmable prescaler for dividing the counter clock frequency (modifiable during runtime) with a prescaler value ranging between 1 and 65536
- Synchronization circuit for triggering the DAC
- Generates interrupts/DMA requests upon counter overflow update events

### Common Timer Functions Reference

- **HAL_TIM_Base_Init()**: Initialize the timer's base unit.
- **HAL_TIM_Base_DeInit()**: Disable the timer, the opposite of initialization.
- **HAL_TIM_Base_MspInit()**: MSP initialization function, automatically called during timer initialization.
- **HAL_TIM_Base_MspDeInit()**: Opposite of the previous function.
- **HAL_TIM_Base_Start()**: Start the timer.
- **HAL_TIM_Base_Stop()**: Stop the timer.
- **HAL_TIM_Base_Start_IT()**: Start the timer in interrupt mode.
- **HAL_TIM_Base_Stop_IT()**: Stop the timer in interrupt mode.
- **HAL_TIM_Base_Start_DMA()**: Start the timer in DMA mode.
- **HAL_TIM_Base_Stop_DMA()**: Stop the timer in DMA mode.

## Using the Basic Timer to Make an LED Blink Periodically

In this experiment, we will utilize the basic timer to implement a timing function, causing an LED to toggle its state every 0.5 seconds.

### Configuring the Basic Timer within CubeMX

First, open the Clock Configuration page in the clock tree configuration of CubeMX and find the value of APB1 Timer clocks on the far right:

![Clock Configuration](https://img.wiki-power.com/d/wiki-media/img/20210407152250.png)

This is crucial because in the STM32F4 series, TIM2-TIM7 and TIM12-TIM14 are mounted on the low-speed APB1 bus, while TIM1, TIM8-TIM11 are on the high-speed APB2 bus. Since we are using the basic timer TIM6, we need to consider the speed of APB1 (which is 90 MHz after division and multiplication).

Next, locate TIM6 on the Timer sidebar and activate the timer by checking the "Activated" box. Configure the following parameters:

![TIM6 Configuration](https://img.wiki-power.com/d/wiki-media/img/20210407173136.png)

Here's what each parameter means:

- **Prescaler**: 8999
- **Counter Mode**: Up (counts up from 0 to the prescaler value before overflow)
- **Counter Period**: 4999
- **Auto-reload preload**: Enable (automatic reload of the initial value on overflow)

In my case, the clock source is 90 MHz, so I set the prescaler to 8999 (which results in a 9000 division). After division, the frequency is 10 kHz (90 MHz/9000). I set the counter period to 4999 (counting 5000 times per cycle), resulting in a 500 ms period.

Next, enable interrupts on the NVIC tab:

![NVIC Configuration](https://img.wiki-power.com/d/wiki-media/img/20210407155959.png)

### Configuring the Basic Timer in the Code

To activate the timer in `main.c`:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_Base_Start_IT(&htim6);

/* USER CODE END 2 */
```

Add a callback function in `stm32f4xx_it.c`:

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

For information on configuring the LED, please refer to the previous article [**HAL Library Development Notes - GPIO**](https://wiki-power.com/en/HAL Development Notes (Part Two) - GPIO](link).

After downloading and burning the code, you will observe that the LED toggles its state according to the 500 ms interval as predefined (meaning it overflows and generates an overflow event every 500 ms, and we have a toggle operation on the LED in the callback function).

## References and Acknowledgments

- [STM32CubeMX Practical Tutorial (Part Four) - Basic Timer (Still Blinking)](link)
- [Advanced Part VI [Timer & PWM]](link)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.