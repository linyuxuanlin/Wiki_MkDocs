# HAL Library Development Notes - TIM General Timer

In the previous article, we provided a brief introduction to the three types of timers in STM32F4 and delved into the details of the basic timer. In this article, we will continue our exploration of the general timer.

## Basic Principles

In STM32F4, the general timer comprises TIM2-TIM5 and TIM9-TIM14.

### Characteristics of the General Timer

The general timer in STM32F4 boasts the following features:

- 16/32-bit incremental, decremental, and incremental/decremental auto-reload counters.
- A 16-bit programmable prescaler for dividing the counter clock frequency (with division factors ranging from 1 to 65536).
- Four independent channels that can be utilized for:
  - Input capture
  - Output comparison
  - PWM generation (both edge-aligned and center-aligned modes)
  - Single-pulse mode output
- External signal control of the timer with the ability to create synchronous circuits connecting multiple timers.
- Generation of interrupts/DMA requests upon the occurrence of events such as:
  - Update: Counter overflow/underflow, counter initialization (triggered by software or internal/external sources)
  - Trigger events (counter start, stop, initialization, or counting through internal/external triggers)
  - Input capture
  - Output comparison
- Support for incremental (quadrature) encoder and Hall sensor circuits.
- External clock trigger input or periodic current management.

### Common Timer Function References

The following are commonly used timer function references, which are similar to those of the basic timer:

- **HAL_TIM_Base_Init()**: Initialize the timer's basic unit.
- **HAL_TIM_Base_DeInit()**: Disable the timer, opposite of initialization.
- **HAL_TIM_Base_MspInit()**: MSP initialization function, automatically called during timer initialization.
- **HAL_TIM_Base_MspDeInit()**: Opposite of the previous function.
- **HAL_TIM_Base_Start()**: Start the timer.
- **HAL_TIM_Base_Stop()**: Stop the timer.
- **HAL_TIM_Base_Start_IT()**: Start the timer in interrupt mode.
- **HAL_TIM_Base_Stop_IT()**: Stop the timer in interrupt mode.
- **HAL_TIM_Base_Start_DMA()**: Start the timer in DMA mode.
- **HAL_TIM_Base_Stop_DMA()**: Stop the timer in DMA mode.

## Generating a 1 kHz/50% Duty Cycle PWM Using a General Timer

In this experiment, we will use a general timer to generate a 1 kHz PWM signal with a 50% duty cycle, which can be visualized using an oscilloscope.

### Configuring the General Timer in CubeMX

First, open the Clock Configuration and Clock Tree Configuration page. Since the general timer is on the high-speed APB2 bus, find and note the clock frequency of APB2 Timer clocks (180 MHz):

![APB2 Timer Clock Frequency](https://img.wiki-power.com/d/wiki-media/img/20210627133951.png)

Next, go to the Timer section on the sidebar, select TIM8, and set Channel 1 (`Channel 1`) for PWM generation (`PWM Generation CH1`). To generate a 1 kHz PWM square wave, configure the following parameters:

- **Prescaler**: 180-1
- **Counter Mode**: Up (counts from 0 to the prescaler value and overflows)
- **Counter Period**: 1000-1
- **Auto-reload preload**: Enable (automatically reloads the initial value upon overflow)

![TIM8 Configuration](https://img.wiki-power.com/d/wiki-media/img/20210627153422.png)

In this case, the clock source is 180 MHz, so set the prescaler to 180-1 = 179, resulting in a 1 MHz frequency after division. Set the counter period to 1000-1 = 9999 to achieve a 1 kHz frequency.

### Configuring the General Timer in Code

In `main.c`, activate the timer:

```c title="main.c"
/* USER CODE BEGIN 2 */
```

```markdown
```cpp
HAL_TIM_PWM_Start(&htim8, TIM_CHANNEL_1);

// Set the duty cycle to 500 (50% for 500 Hz/1 kHz)
__HAL_TIM_SetCompare(&htim8, TIM_CHANNEL_1, 500);

/* USER CODE END 2 */
```

After compiling and flashing, you can observe the waveform using an oscilloscope:

![Waveform](https://img.wiki-power.com/d/wiki-media/img/20210627154737.jpg)

## References and Acknowledgments

- [STM32CubeMX Practical Tutorial (Part Five) - General Timers (PWM Output)](https://blog.csdn.net/weixin_43892323/article/details/104776035)

[1] to_be_replace[1]
[2] to_be_replace[2]
```


> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.