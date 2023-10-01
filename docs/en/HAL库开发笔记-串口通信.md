# HAL Library Development Notes - Serial Communication

This article is based on the self-developed RobotCtrl development kit, with the MCU core being STM32F407ZET6 and RS-232 communication using the SP3232EEN chip. For schematic and detailed introduction, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Basic Principle

For the basic principle of serial communication, please refer to the article [**Communication Protocol - Serial Communication**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1).

## Serial Communication Experiment

Before proceeding to the next experiment, it is necessary to configure various parameters such as serial download and clock in CubeMX. 
For specific steps, please refer to the method in the article [**HAL Library Development Notes - Environment Configuration**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE).

### Configuring Serial Communication in CubeMX

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207100329.png)

According to the schematic, the serial port we use for communication experiments is `USART1`, which corresponds to the `PA9` and `PA10` pins. Therefore, we first need to configure these two pins in CubeMX as the send and receive functions of `USART1`, and then click on the USART1 tab on the left, set the mode to asynchronous, and modify the baud rate and other parameters below:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207100941.png)

The parameter details are as follows:

- **Baud Rate Setting**: There is no best baud rate, it should be modified according to the actual situation and consistent with the serial port debugging assistant.
- **Word Length**: If parity check is enabled, the actual data will be reduced by one bit.
- **Parity**: Odd or even parity can be selected, or no parity check.
- **Stop Bits**: An additional one or two bits are used as signal bits for sending or receiving completion.
- **Data Direction**: Only sending, only receiving, or sending and receiving modes can be selected.
- **Over Sampling**: 8x or 16x sampling rate can effectively prevent data errors.

Finally, enable the USART1 serial port interrupt in the NVIC tab, as shown in the figure:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207104641.png)

### Configuring the Serial Port in the Code

First, add the following code to the end of `stm32f4xx_it.c`:

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // Receive and write to aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // Send back the received aRxBuffer
    }
}
/* USER CODE END 1 */
```

Here, `Buffer` is a uint8_t type global variable defined in `main.c`. An interrupt is generated after each byte is received, and the byte data is returned and the interrupt is re-enabled. We need to define it in `main.c` and `stm32f4xx_it.c` respectively.

```c title="main.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "USART TEST\r\n"; // string for sending
uint8_t aRxBuffer[20]; // string for receiving

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

In addition, in `main.c`, we need to add a receive interrupt enable function after the UART initialization and before the main loop:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // receive interrupt enable function

/* USER CODE END 2 */
```

We can also send an initialization message to indicate that the UART has been started:

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // send the last customized aTxBuffer

/* USER CODE END 2 */
```

If you need to redirect printf (use printf function for serial output function in STM32), please refer to [**STM32CubeIDE Serial Redirection (printf) and Output Floating Point**](https://wiki-power.com/STM32CubeIDE%E4%B8%B2%E5%8F%A3%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%88printf%EF%BC%89%E5%8F%8A%E8%BE%93%E5%87%BA%E6%B5%AE%E7%82%B9%E5%9E%8B).

### Download Verification

After the program is successfully burned, we open the serial assistant and configure the corresponding port and baud rate.

After connecting to the serial port, the contents of `aTxBuffer` will be printed first, and then the received `aRxBuffer` will be printed back. As shown in the figure:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210403232628.png)

## References and Acknowledgments

- [STM32CubeMX Practical Tutorial (6) - Serial Communication](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [Advanced Part III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [STM32 Non-blocking HAL_UART_Receive_IT Analysis and Practical Application](https://zhuanlan.zhihu.com/p/147414331)
- [HAL Library Tutorial 6: Serial Data Reception](https://blog.csdn.net/geek_monkey/article/details/89165040)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.