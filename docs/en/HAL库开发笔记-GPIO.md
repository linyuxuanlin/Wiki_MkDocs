# HAL Library Development Notes - GPIO

## Basic Principles

GPIO stands for General Purpose Input Output.

![](https://img.wiki-power.com/d/wiki-media/img/20200615205256.jpg)

Taking the F103C8T6 chip as an example (shown above), all pins except for the colored ones (power and certain functional pins) are called GPIO. This demonstrates its versatility.

The function of GPIO is to input/output electrical signals. Let's take a look at its internal structure:

![](https://img.wiki-power.com/d/wiki-media/img/20200615211744.jpg)

- The rightmost I/O pin is the physical chip pin. The upper and lower `protective diodes` can prevent abnormal external voltages from burning out the chip to a certain extent.
- The red dashed box represents the input function (the chip reads external signals). The two switches with pull-up/pull-down resistors are used to implement pull-up/pull-down input functions. If both switches are not closed, it is called floating input (no reference level, neither high nor low). These three input modes all output digital signals (high/low level). In addition, there is an analog input function, which directly reads the analog signal on the pin. (We will mention the multiplexed input function later).
- The blue dashed box represents the output function. There are four output modes: push-pull, open-drain, multiplexed push-pull, and multiplexed open-drain.

### Input/Output Modes

Input modes:

- **Floating Input**: Neither pull-up nor pull-down. This is the default mode after STM32 reset.
- **Pull-up Input**: Close the switch of the pull-up resistor to keep the reference level always high. When the input signal is low, it triggers.
- **Pull-down Input**: Close the switch of the pull-down resistor to keep the reference level always low. When the input signal is high, it triggers.
- **Analog Input**: In this mode, neither pull-up nor pull-down is used, and the signal is directly read by STM32 without going through a TTL trigger.

Output modes:

- **Open-drain output**: Open-drain refers to the drain (bottom pin) of the N-MOS transistor below being open. This mode only uses the N-MOS transistor below. We know that MOS transistors are voltage-controlled components. Think of it like a faucet. When a low-level signal is input to the gate (left pin) of the N-MOS, it conducts.
- **Push-pull output**: There are two modes for push-pull. The first is to simultaneously apply a low-level signal to the gates of both MOS transistors. At this time, the P-MOS conducts while the N-MOS is cut off, and the current flows from VDD to the external pin, which is high. The second mode is the opposite. Simultaneously apply a high-level signal to the gates of both MOS transistors. At this time, the P-MOS is cut off while the N-MOS conducts, and the current flows from the external pin to the internal GND, and the pin is low.
- **Multiplexed open-drain**
- **Multiplexed push-pull**

### Common GPIO function reference

Read GPIO status and return high/low level:

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin);
```

Write GPIO status and write high/low level:

```c
HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState);
```

Toggle GPIO level:

```c
HAL_GPIO_TogglePin(GPIOx, GPIO_Pin);
```

## Light up LED

Before proceeding to the next experiment, you need to configure various parameters such as serial port download and clock in CubeMX.  
This will not be repeated here. Please refer to the method in the article [**HAL Library Development Notes - Environment Configuration**](https://wiki-power.com/en/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) for configuration.

### Configure GPIO in CubeMX

Set the corresponding GPIO port of the LED as output and set the initial level.

![](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

For my board, I need to set the GPIOs of `PD4` and `PI3` as output (`GPIO_Output`).  
If you want to turn on the LED when powered on, set the initial voltage to low (`Low`) according to the circuit schematic.

### Configuring GPIO in Code

If the configuration is correct, the two user LEDs can be lit up by powering on.  
If you want to add a flashing effect, just add a few lines of code in the user code area of the main loop:

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI, GPIO_PIN_3);

}
/* USER CODE END 3 */
```

![](https://img.wiki-power.com/d/wiki-media/img/20210205151322.png)

The flashing effect can be achieved.

## Controlling LEDs with Buttons

After learning about GPIO output, we will learn about GPIO input mode using buttons.

### Configuring GPIO in CubeMX

After configuring the GPIO port to which the LED belongs using the above method, according to the schematic diagram of the onboard button:

![](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

Set the GPIO (`PI8`) to which the button belongs to input (`GPIO_Input`). According to the schematic diagram, select internal pull-up (`Pull-up`). Generate code.

### Configuring GPIO in Code

Add the following code to the user code area of the main loop:

```c title="main.c"
/* USER CODE BEGIN 3 */

if(HAL_GPIO_ReadPin(KEY1_GPIO_Port,KEY1_Pin)==0)
{
	HAL_Delay(100);
	if(HAL_GPIO_ReadPin(KEY1_GPIO_Port,KEY1_Pin)==0)
	{
		HAL_GPIO_WritePin(LED1_GPIO_Port,LED1_Pin,GPIO_PIN_RESET);
	}
}else{
	HAL_GPIO_WritePin(LED1_GPIO_Port,LED1_Pin,GPIO_PIN_SET);
}

}
/* USER CODE END 3 */
```

By pressing the button, the light can be turned on, and by releasing the button, the light can be turned off.

Many people are confused about what `GPIO_PIN_SET` and `GPIO_PIN_RESET` mean. In fact, the only function of these two variables is to set the GPIO pin to a high or low level. Whether the light is on or off depends on the circuit schematic.

In addition, the function of `HAL_Delay(100)` is to eliminate button bounce in the code. However, the `HAL_Delay()` function uses polling, which will occupy resources and cause the system to freeze. In the next article, we will use hardware interrupts to solve this problem.

## References and Acknowledgements

- [【STM32】STM32CubeMX Tutorial 2 -- Basic Usage (Creating a Project to Light Up an LED)](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX Practical Tutorial 2 -- Press a Button to Light Up a LED](https://blog.csdn.net/weixin_43892323/article/details/104343933)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
