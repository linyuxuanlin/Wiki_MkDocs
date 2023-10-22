# HAL Library Development Notes - GPIO

## Basic Principles

GPIO stands for **General Purpose Input Output**.

![](https://img.wiki-power.com/d/wiki-media/img/20200615205256.jpg)

To illustrate, let's take the F103C8T6 chip as an example (as shown in the image above). Except for the colored pins (power and some specific function pins), all the others are referred to as GPIO pins. This showcases their versatility.

The function of GPIO is to handle input and output electrical signals. Let's delve into its internal structure:

![](https://img.wiki-power.com/d/wiki-media/img/20200615211744.jpg)

- The rightmost I/O pins represent the physical chip's pins. The upper and lower "protection diodes" to some extent protect the chip from abnormal external voltages that might otherwise damage it.
- Inside the red dashed box are the input functions (where the chip reads external signals). Two switches with pull-up/pull-down resistors are used to implement pull-up and pull-down input functions. If neither switch is closed, it's considered a floating input (with no reference voltage, i.e., no defined logic level). All three of these input modes read digital values (high/low levels). Additionally, there is an analog input function, which directly reads the analog voltage on the pin (we'll discuss multiplexing input functions later).
- Inside the blue dashed box are the output functions. There are four output modes: push-pull, open-drain, multiplexed push-pull, and multiplexed open-drain.

### Input and Output Modes

Input Modes:

- **Floating Input**: No pull-up or pull-down resistors enabled; this is the default mode after an STM32 reset.
- **Pull-up Input**: Closing the pull-up resistor switch ensures that the reference voltage is always high. An input signal of low voltage triggers it.
- **Pull-down Input**: Closing the pull-down resistor switch ensures that the reference voltage is always low. An input signal of high voltage triggers it.
- **Analog Input**: In this mode, there is neither pull-up nor pull-down, and it doesn't pass through TTL trigger circuitry. STM32 directly reads the analog signal on the pin.

Output Modes:

- **Open-Drain Output**: "Open-drain" refers to the drain terminal (the pin below). This mode exclusively uses the lower N-MOS transistor. MOS transistors are voltage-controlled devices. Think of it like a faucet; when a low voltage signal is applied to the gate of the N-MOS transistor (the left pin), it turns on.
- **Push-Pull Output**: Push-pull has two modes. In the first mode, both MOS transistor gates receive a low voltage signal, causing the P-MOS transistor to conduct while the N-MOS transistor is cut off. This results in current flowing from VDD to the external pin, making the pin high. In the second mode, the opposite happens: both MOS transistor gates receive a high voltage signal, causing the P-MOS transistor to cut off and the N-MOS transistor to conduct. This results in current flowing from the external pin to the internal GND, making the pin low.
- **Multiplexed Open-Drain**
- **Multiplexed Push-Pull**

### Common GPIO Function References

To read the GPIO state and return high or low level:

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin);
```

To write the GPIO state and set it to high or low level:

```c
HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState);
```

To toggle the GPIO level:

```c
HAL_GPIO_TogglePin(GPIOx, GPIO_Pin);
```

## Illuminating an LED

Before proceeding to the next experiment, it's necessary to configure various parameters such as serial download and clock settings in CubeMX.
For details on configuring the environment, please refer to the article [**HAL Library Development Notes - Environment Configuration**](to_be_replace[3]).

### Configuring GPIO in CubeMX

Set the corresponding GPIO pins for LEDs as outputs and set the initial logic level.

![](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

On my board, you need to configure GPIO pins `PD4` and `PI3` as outputs (`GPIO_Output`). If you want the LEDs to be initially lit when powered, according to the circuit schematic, set the initial level to low (`Low`).

### Configuring GPIO in the Code


If the configuration is correct, you can power it up to illuminate two user LEDs. If you want to add a flashing effect, you just need to add a few lines of code in the main loop's user code section:

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI, GPIO_PIN_3);

}
/* USER CODE END 3 */
```

This will achieve the flashing effect.

![Flashing LED](https://img.wiki-power.com/d/wiki-media/img/20210205151322.png)

## Controlling Lights with Buttons

After learning about GPIO output, we will now learn about GPIO input mode using buttons.

### Configuring GPIO in CubeMX

After configuring the GPIO port for the LEDs as described above, according to the onboard button's schematic:

![Button Schematic](https://img.wiki-power.com/d/wiki-media/img/20210205150422.png)

Set the GPIO (`PI8`) corresponding to the button as an input (`GPIO_Input`). According to the schematic, choose internal pull-up (`Pull-up`). Generate the code.

### Configuring GPIO in Code

Add the following code in the user code section of the main loop:

```c title="main.c"
/* USER CODE BEGIN 3 */

if (HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0)
{
	HAL_Delay(100);
	if (HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0)
	{
		HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_RESET);
	}
}
else
{
	HAL_GPIO_WritePin(LED1_GPIO_Port, LED1_Pin, GPIO_PIN_SET);
}

}
/* USER CODE END 3 */
```

This will achieve the effect of turning the light on when the button is pressed and turning it off when the button is released.

Many people are confused about what `GPIO_PIN_SET` and `GPIO_PIN_RESET` mean. In fact, the only function of these two variables is to set the GPIO pin to a high or low level. Whether the light is on or off depends on the circuit schematic.

Additionally, the function of `HAL_Delay(100)` is to eliminate button bouncing in the code. However, `HAL_Delay()` uses polling and consumes resources, which may cause the system to hang. In the next article, we will use hardware interrupts to address this issue.

## References and Acknowledgments

- [STM32CubeMX Tutorial 2 - Basic Usage (Creating a Project to Light an LED)](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX Practical Tutorial 2 - Lighting a LED with a Button](https://blog.csdn.net/weixin_43892323/article/details/104343933)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.