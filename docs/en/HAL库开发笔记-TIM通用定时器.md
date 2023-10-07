# HAL Library Development Notes - TIM General Purpose Timer

In the previous article, we briefly introduced the three types of timers in STM32F4 and provided a detailed explanation of the basic timer. In this article, we will continue to introduce the general-purpose timer.

## Basic Principles

In STM32F4, the general-purpose timer includes TIM2-TIM5 and TIM9-TIM14.

### Characteristics of General Purpose Timers

In STM32F4, the characteristics of general-purpose timers are as follows:

- 16/32-bit increment, decrement, and increment/decrement auto-reload counters
- 16-bit programmable prescaler for dividing the counter clock frequency (divisor range is 1-65536)
- 4 independent channels, which can be used for:
  - Input capture
  - Output comparison
  - PWM generation (edge and center-aligned modes)
  - Single pulse mode output
- Use external signals to control the timer and realize a synchronous circuit of multiple timers
- Generate interrupts/DMA requests when the following events occur:
  - Update: counter overflow/underflow, counter initialization (through software or internal/external trigger)
  - Trigger event (counter start, stop, initialization, or count through internal/external trigger)
  - Input capture
  - Output comparison
- Support incremental (orthogonal) encoder and Hall sensor circuits
- External clock trigger input or per-cycle current management

### Common Timer Function Reference

The following are common timer function references, which are the same as the functions of the basic timer.

- **HAL_TIM_Base_Init()**: Initialize the timer base unit
- **HAL_TIM_Base_DeInit()**: Disable the timer, opposite of initialization
- **HAL_TIM_Base_MspInit()**: MSP initialization function, automatically called when the timer is initialized
- **HAL_TIM_Base_MspDeInit()**: Opposite of the previous function
- **HAL_TIM_Base_Start()**: Start the timer
- **HAL_TIM_Base_Stop()**: Stop the timer
- **HAL_TIM_Base_Start_IT()**: Start the timer in interrupt mode
- **HAL_TIM_Base_Stop_IT()**: Stop the timer in interrupt mode
- **HAL_TIM_Base_Start_DMA()**: Start the timer in DMA mode
- **HAL_TIM_Base_Stop_DMA()**: Stop the timer in DMA mode

## Using General Purpose Timers to Output 1 kHz/50% Duty Cycle PWM

This experiment uses a general-purpose timer to output a 1 kHz, 50% duty cycle PWM signal, which can be displayed on an oscilloscope.

### Configuring the General-Purpose Timer in CubeMX

First, we open the Clock Configuration page and find the clock frequency of APB2 Timer clocks (180 MHz) since the general-purpose timer is mounted on the high-speed APB2 bus:

![](https://f004.backblazeb2.com/file/wiki-media/img/20210627133951.png)

Next, we find TIM8 in the Timer section of the sidebar and set Channel 1 to PWM Generation (PWM Generation CH1). To generate a 1 kHz frequency PWM square wave, we need to configure the following parameters:

- **Prescaler**: 180-1
- **Counter Mode**: Up (counts up from 0 to the prescaler value and overflows)
- **Counter Period**: 1000-1
- **Auto-reload preload**: Enable (automatically reloads the initial value when overflowing)

![](https://f004.backblazeb2.com/file/wiki-media/img/20210627153422.png)

Since the clock source used here is 180 MHz, we set the prescaler to 180-1 = 179, resulting in a frequency of 1 MHz after division. We set the counter period to 1000-1 = 9999, resulting in a frequency of 1 kHz.

### Configuring the Basic Timer in the Code

In `main.c`, we start the timer:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_PWM_Start(&htim8,TIM_CHANNEL_1);

// Set the duty cycle to 500 (500 Hz/1 kHz=50%)
__HAL_TIM_SetCompare(&htim8,TIM_CHANNEL_1,500);

/* USER CODE END 2 */
```

After compiling and burning, we can observe the waveform using an oscilloscope.

## Reference and Acknowledgments

- [STM32CubeMX Practical Tutorial (Part 5) - General Timer (PWM Output)](https://blog.csdn.net/weixin_43892323/article/details/104776035)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.