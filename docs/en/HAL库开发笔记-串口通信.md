# HAL Library Development Notes - Serial Communication

In this article, based on our in-house RobotCtrl development kit, the microcontroller core is STM32F407ZET6, and RS-232 communication utilizes the SP3232EEN chip. For the schematic and detailed information, please refer to [**RobotCtrl - STM32 General Development Kit**](to_be_replace[3]).

## Basic Principles

For the fundamental principles of serial communication, please visit the article on [**Communication Protocols - Serial Communication**](to_be_replace[3]).

## Serial Communication Experiment

Before proceeding with the next experiment, you need to configure various parameters such as serial download and clock settings in CubeMX. For specific steps, please refer to the article [**HAL Library Development Notes - Environment Configuration**](to_be_replace[3]).

### Configuring Serial Communication in CubeMX

![CubeMX Serial Configuration](https://img.wiki-power.com/d/wiki-media/img/20210207100329.png)

According to the schematic, the USART to be used for communication experiments is `USART1`, corresponding to pins `PA9` and `PA10`. To set this up in CubeMX, you need to configure these two pins as the transmit and receive functions for `USART1`. Then, click on the left-hand `USART1` tab and set the mode to asynchronous, adjusting parameters such as baud rate:

![USART1 Configuration in CubeMX](https://img.wiki-power.com/d/wiki-media/img/20210207100941.png)

Here are the parameter details:

- **Baud Rate Setting**: The baud rate should match your actual requirements and align with the settings in your serial terminal software.
- **Data Bits**: If parity is enabled, the actual data bits will be reduced by one.
- **Parity**: You can choose between odd, even parity, or no parity.
- **Stop Bits**: An additional bit or two is used for signaling the end of transmission.
- **Data Direction**: You can select transmit-only, receive-only, or full-duplex modes.
- **Over Sampling**: Choosing between 8x or 16x sampling rates helps in preventing data errors.

Finally, in the NVIC tab, enable USART1's serial interrupt, as shown in the image:

![Enable USART1 Interrupt in NVIC](https://img.wiki-power.com/d/wiki-media/img/20210207104641.png)

### Configuring Serial Communication in Code

First, you need to add the following code at the end of the `stm32f4xx_it.c` file:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance == USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // Receive and write to aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // Send back the received aRxBuffer
    }
}
/* USER CODE END 1 */
```

In this code, `aRxBuffer` is a uint8_t global variable defined in `main.c`. This code generates an interrupt for each received byte, returning the byte data and re-enabling the interrupt. You should define this variable in both `main.c` and `stm32f4xx_it.c`.

```c title="main.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "USART TEST\r\n"; // String for sending
uint8_t aRxBuffer[20]; // String for receiving

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

In addition, in `main.c`, we need to enable the receive interrupt function after initializing the UART and before entering the main loop:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // Enable receive interrupt

/* USER CODE END 2 */
```

You can also send an initialization message to indicate that the UART has started:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // Send the previously defined aTxBuffer

/* USER CODE END 2 */
```

If you need to redirect `printf` (use the `printf` function for UART output in STM32), please refer to [STM32CubeIDE UART Redirection for Printf and Floating-Point Output](to_be_replace[3]).

### Download and Verification

After successfully programming the code, open a terminal program and configure the corresponding port and baud rate.

Once the UART is connected, it will first print the content of `aTxBuffer`, and then it will print the received `aRxBuffer`. As shown below:

![](https://img.wiki-power.com/d/wiki-media/img/20210403232628.png)

## References and Acknowledgments

- [STM32CubeMX Practical Tutorial (Part Six) - Serial Communication](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [Advanced Tutorial III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [Non-Blocking UART Receive with HAL_UART_Receive_IT - Explanation and Practical Application](https://zhuanlan.zhihu.com/p/147414331)
- [HAL Library Tutorial 6: UART Data Reception](https://blog.csdn.net/geek_monkey/article/details/89165040)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.