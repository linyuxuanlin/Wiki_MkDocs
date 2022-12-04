---
id: HAL库开发笔记-串口通信
title: HAL 库开发笔记 - 串口通信
---

本篇基于自研 RobotCtrl 开发套件，单片机内核为 STM32F407ZET6，RS-232 通信使用 SP3232EEN 芯片，原理图及详细介绍请见 [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6)。

## 基本原理

串口通信的基本原理请跳转文章 [**通信协议-串口通信**](https://wiki-power.com/%E9%80%9A%E4%BF%A1%E5%8D%8F%E8%AE%AE-%E4%B8%B2%E5%8F%A3%E9%80%9A%E4%BF%A1)。

## 串口通讯实验

在进行下一步实验之前，需要在 CubeMX 里配置串口下载、时钟等各类参数。  
具体步骤请跳转文章 [**HAL 库开发笔记 - 环境配置**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) 中的方法进行配置。

### 在 CubeMX 内配置串口

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207100329.png)

根据原理图，我们用来进行通讯实验的串口是 `USART1` ，即 `PA9` `PA10` 引脚。那么，我们首先需要在 CubeMX 内将这两个引脚配置为 `USART1` 的发送和接受功能，然后点击左侧 USART1 标签页，将模式（Mode）设为异步（Asynchronous），并在下方修改波特率（Baud Rate）等参数：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207100941.png)

参数详情如下：

- **波特率设置**（Baud Rate）：没有哪种波特率最好，根据实际情况进行修改，要与串口调试助手上一致。
- **数据位数**（Word Length）：如果使能了奇偶校验，那么实际数据将在该位数上减一。
- **校验**（Parity）：可选择奇偶校验或不校验。
- **停止位**（Stop Bits）：额外一位或两位用于作为发送或接收完毕信号位。
- **数据方向**（Data Direction）：可选择仅发送，仅接收或收发模式。
- **过采样**（Over Sampling）：8 倍或 16 倍采样率可以有效防止数据出错。

最后，在 NVIC 标签页使能 USART1 的串口中断，如图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207104641.png)

### 在代码内配置串口

首先需要在 `stm32f4xx_it.c` 末尾添加如下代码：

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */
void HAL_UART_RxCpltCallback(UART_HandleTypeDef *huart)
{
    if(huart->Instance==USART1)
    {
        HAL_UART_Receive_IT(huart, &aRxBuffer, 1); // 接收并写入 aRxBuffer
        HAL_UART_Transmit(huart, &aRxBuffer, 10, 0xFFFF); // 把接收到的 aRxBuffer 发回去
    }
}
/* USER CODE END 1 */
```

其中，`Buffer` 是在 `main.c` 中定义的 uint8_t 类型全局变量。这里每接受的一个字节后就产生中断，将该字节数据返回并重新开启中断。我们需要分别在 `main.c` 和 `stm32f4xx_it.c` 中定义它：

```c title="main.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t aTxBuffer[] = "USART TEST\r\n"; //用于发送的字符串
uint8_t aRxBuffer[20]; //用于接收的字符串

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t aTxBuffer;
extern uint8_t aRxBuffer;

/* USER CODE END PV */

```

另外，在 `main.c` 中，我们需要在串口初始化后、主循环前，添加接收中断开启函数：

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1, (uint8_t *)aRxBuffer, 1); // 接收中断开启函数

/* USER CODE END 2 */
```

也可以发送一条初始化消息，代表串口已启动：

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Transmit(&huart1, (uint8_t*) aTxBuffer, sizeof(aTxBuffer) - 1, 0xFFFF); // 发上一次自定义的 aTxBuffer

/* USER CODE END 2 */
```

如果需要对 printf 进行重定向（把 printf 函数用在 STM32 中做串口输出功能），请参考 [**STM32CubeIDE 串口重定向（printf）及输出浮点型**](https://wiki-power.com/STM32CubeIDE%E4%B8%B2%E5%8F%A3%E9%87%8D%E5%AE%9A%E5%90%91%EF%BC%88printf%EF%BC%89%E5%8F%8A%E8%BE%93%E5%87%BA%E6%B5%AE%E7%82%B9%E5%9E%8B)。

### 下载验证

程序烧录成功后，我们打开串口助手，配置对应的端口和波特率。

连上串口后，会先打印一行 `aTxBuffer` 的内容，然后将会把接收到的 `aRxBuffer` 回传打印出来。如图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210403232628.png)

## 参考与致谢

- [STM32CubeMX 实战教程（六）—— 串口通信](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [进阶篇 III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)
- [STM32 非阻塞 HAL_UART_Receive_IT 解析与实际应用](https://zhuanlan.zhihu.com/p/147414331)
- [HAL 库教程 6：串口数据接收](https://blog.csdn.net/geek_monkey/article/details/89165040)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

