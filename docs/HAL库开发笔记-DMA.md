---
id: HAL库开发笔记-DMA
title: HAL 库开发笔记 - DMA
---

DMA（Direct Memory Access，直接存储器访问）允许不同速度的硬件装置直接沟通，而不需要依赖于 CPU 的大量中断负载。

## 基本原理

### DMA 是什么

DMA 提供外设 / 存储器或存储器 / 存储器之间的高速数据传输，其过程中无需占用 CPU 资源。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404153423.png)

如上图所示，STM32F4 系列有两个 DMA 控制器，共 12 通道（DMA1 有 7 个，DMA2 有 5 个）。DMA 控制器与 Cortex-M3 核心共享系统的数据总线。

简单地理解，当 CPU 懒得把一大串数据转移到另一个地方，或者说它还有更重要的事情要做的时候，就可以把这个任务丢给 DMA 去干，DMA 干完 / 出问题了跟 CPU 说一声就行。

### DMA 的使用场景

- **串口通讯**：最常见的使用情况，当有大量数据从串口读入或者写入的时候，让 DMA 处理。这样可以将 CPU 解放出来，让 CPU 处理更重要的事情。
- **ADC**：一般在需要 ADC 时的通道扫描模式下，可以用 DMA 处理。
- **SD 卡读写**：需要往 SD 卡里面读写大量数据的时候，一般也用 DMA 来处理。

### DMA 的传输方向

- **P2P**（Peripheral to Peripheral，从外设到外设）。
- **P2M**（Peripheral to Memory，从外设到内存）：一般用于传感器通过串口发送读数回单片机。
- **M2P**（Memory to Peripheral，从内存到外设）：一般用于单片机通过串口发送数据到执行器。
- **M2M**（Memory to Memory，从内存到内存）：MCU 内部的数据转移，常见于 Buffer 之间互相转移数据，或者从 Buffer 读写数据。只有 DMA2 能够进行 M2M 操作。

### DMA 的传输模式

- **DMA_Mode_Normal**：正常模式。任务完成后就停止 DMA，如果还需使用，要再次手动启动。
- **DMA_Mode_Circular**： 循环传输模式。当传输结束时，硬件自动会将传输数据量寄存器进行重装，进行下一轮的数据传输。

### 常用的 DMA 函数参考

#### 串口 DMA 发送数据

```c
HAL_UART_Transmit_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

功能：串口通过 DMA 发送指定长度的数据。  
参数：

- **UART_HandleTypeDef \*huart**：UATR 的别名（如 : UART_HandleTypeDef huart1 -> huart1）
- **\*pData**：需要发送的数据
- **Size**：发送的字节数

例子：

```c
HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));  //串口发送 Senbuff 数组
```

#### 串口 DMA 接收数据

```c
HAL_UART_Receive_DMA(UART_HandleTypeDef *huart, uint8_t *pData, uint16_t Size)
```

功能：串口通过 DMA 接收指定长度的数据。  
参数：

- **UART_HandleTypeDef \*huart**：UATR 的别名（如 : UART_HandleTypeDef huart1 -> huart1）
- **\*pData**：需要存放接收数据的数组
- **Size**：接收的字节数

例子：

```c
HAL_UART_Receive_DMA(&huart1, (uint8_t *)Recbuff, sizeof(Recbuff));  //串口接收，存放到 Recbuff 数组
```

#### 串口 DMA 恢复函数

```c
HAL_UART_DMAResume(&huart1)
```

作用：恢复 DMA 的传输  
返回值：0（正在恢复）；1（已经完成恢复）

## DMA 串口传输实验

### 在 CubeMX 内配置 DMA

串口部分的配置请跳转文章 [**HAL 库开发笔记 - 串口通信**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1)。

配置完 USART 引脚和 NVIC 中断后，切换到 `DMA Settings` 标签页，按照下图进行配置：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404165541.png)

- 点击 `Add` 添加通道（USART1_RX 与 USART1_TX）
- 将两个的优先级都设置为 `Medium`（中优先级）
- DMA 传输模式为 `Normal`（正常模式）
- DMA 内存地址自增，每次增加一个 Byte（字节）

随后，在 `System Core` 标签页找到 `DMA`，增加一个 `MEMTOMEM` 栏目，如图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210404170002.png)

### 在代码内配置 DMA

```c title="main.c"
/* USER CODE BEGIN Init */

uint8_t Senbuff[] = "Serial Output Message by DMA \r\n";  // 自定义发送的字符串

/* USER CODE END Init */

......

/* USER CODE BEGIN 3 */

HAL_UART_Transmit_DMA(&huart1, (uint8_t *)Senbuff, sizeof(Senbuff));
HAL_Delay(1000);

}
/* USER CODE END 3 */
```

烧录程序，打开串口助手，即可看见循环发送的自定义数组。

## 参考与致谢

- [进阶篇 IV [DMA]](https://alchemicronin.github.io/posts/90d72de/#4-0-%E7%BB%83%E4%B9%A0%E9%A1%B9%E7%9B%AE)
- [【STM32】HAL 库 STM32CubeMX 教程十一 ---DMA (串口 DMA 发送接收)](https://blog.csdn.net/as480133937/article/details/104827639)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

