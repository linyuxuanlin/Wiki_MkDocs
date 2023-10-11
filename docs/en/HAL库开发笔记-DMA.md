# HAL Library Development Notes - DMA

DMA (Direct Memory Access) allows hardware devices with different speeds to communicate directly without relying on a large interrupt load on the CPU.

## Basic Principles

### What is DMA

DMA provides high-speed data transfer between peripherals/memory or memory/memory without occupying CPU resources.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404153423.png)

As shown in the above figure, the STM32F4 series has two DMA controllers with a total of 12 channels (7 for DMA1 and 5 for DMA2). The DMA controller shares the system data bus with the Cortex-M3 core.

Simply put, when the CPU is too lazy to transfer a large amount of data to another location, or when it has more important things to do, it can hand over this task to DMA to do it, and DMA will notify the CPU when it is done or if there is a problem.

### DMA Usage Scenarios

- **Serial Communication**: The most common usage scenario is when a large amount of data is read from or written to the serial port, let DMA handle it. This frees up the CPU to handle more important tasks.
- **ADC**: DMA can be used in channel scanning mode when ADC is needed.
- **SD Card Read/Write**: DMA is generally used when a large amount of data needs to be read from or written to the SD card.

### DMA Transfer Direction

- **P2P** (Peripheral to Peripheral, from peripheral to peripheral).
- **P2M** (Peripheral to Memory, from peripheral to memory): Generally used when sensors send readings back to the microcontroller via the serial port.
- **M2P** (Memory to Peripheral, from memory to peripheral): Generally used when the microcontroller sends data to the actuator via the serial port.
- **M2M** (Memory to Memory, from memory to memory): Data transfer within the MCU, commonly used for transferring data between buffers or reading/writing data from buffers. Only DMA2 can perform M2M operations.

### DMA Transfer Modes

- **DMA_Mode_Normal**: Normal mode. DMA stops after completing the task. If it needs to be used again, it must be manually restarted.
- **DMA_Mode_Circular**: Circular transfer mode. When the transfer is complete, the hardware automatically reloads the transfer data register for the next round of data transfer.

### Common DMA Function Reference

#### UART DMA Transmit Data

```c
HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

Function: Transmit specified length of data through UART using DMA.  
Parameters:

- **UART_HandleTypeDef \*huart**: Alias of UART (e.g. UART_HandleTypeDef huart1 -> huart1)
- **\*pData**: Data to be transmitted
- **Size**: Number of bytes to be transmitted

Example:

```c
HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));  //Transmit Senbuff array through UART
```

#### UART DMA Receive Data

```c
HAL_UART_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

Function: Receive specified length of data through UART using DMA.  
Parameters:

- **UART_HandleTypeDef \*huart**: Alias of UART (e.g. UART_HandleTypeDef huart1 -> huart1)
- **\*pData**: Array to store received data
- **Size**: Number of bytes to be received

Example:

```c
HAL_UART_Receive_DMA(&huart1, (uint8_t *)Recbuff, sizeof(Recbuff));  //Receive and store data in Recbuff array through UART
```

#### UART DMA Resume Function

```c
HAL_UART_DMAResume(&huart1)
```

Function: Resume DMA transfer  
Return value: 0 (resuming), 1 (resumed)

## DMA UART Transfer Experiment

### Configuring DMA in CubeMX

For the configuration of the UART section, please refer to the article [**HAL Library Development Notes - Serial Communication**](https://wiki-power.com/en/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1).

After configuring the USART pins and NVIC interrupts, switch to the `DMA Settings` tab and configure as shown in the following figure:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404165541.png)

- Click `Add` to add channels (USART1_RX and USART1_TX).
- Set the priority of both channels to `Medium`.
- Set the DMA transfer mode to `Normal`.
- Set the DMA memory address to increment by one byte each time.

Then, in the `System Core` tab, find `DMA` and add a `MEMTOMEM` section as shown in the following figure:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404170002.png)

### Configuring DMA in the Code

```c title="main.c"
/* USER CODE BEGIN Init */

uint8_t Senbuff[] = "Serial Output Message by DMA \r\n";  // Custom string to be sent

/* USER CODE END Init */

......

/* USER CODE BEGIN 3 */

HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));
HAL_Delay(1000);

}
/* USER CODE END 3 */
```

After burning the program, open the serial assistant to see the custom array being sent repeatedly.

## References and Acknowledgments

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
