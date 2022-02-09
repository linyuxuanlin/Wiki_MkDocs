---
id: HAL库开发笔记（四）-串口通信
title: HAL 库开发笔记（四）- 串口通信
---

串口通信算得上是单片机中最常用、最基础的一种通讯方式。常用可作为一种调试的手段，与单片机通讯监控数据、发送指令，也可以用作两个单片机之间互相通讯使用。

## 基本原理

### 并行和串行

- **并行通信**：各个数据位同时传输，速度快但占用引脚资源多。
- **串行通信**：数据按位顺序传输，占用引脚资源少但速度相对慢。

### 单工、半双工和全双工

- **单工**：数据只在一个方向上进行传输。
- **半双工**：允许数据在两个方向上传输，但是同一时刻，只允许数据在一个方向上传输，相当于方向可切换的单工通信。
- **全双工**：允许数据同时在两个方向上传输，因此，全双工通信是两个单工通信方式的结合，要求发送和接收设备都有独立的接发能力。

### 同步和异步

- **同步通信**：带时钟同步信号传输。例如 SPI，IIC 等通信接口。
- **异步通信**：不带时钟同步信号。例如 UART，单总线。

### USART 和 UART

- **UART**：通用异步收发器（Universal Asynchronous Receiver/Transmitter）
- **USART**：通用同步异步收发器（Universal Synchronous/Asynchronous Receiver/Transmitter）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207095411.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210207095433.png)

USART 是 UART 的升级版，区别在于多了 CLK 线，在 CLK 没有信号的时候，就表明没有数据传输任务，有 CLK 信号的时候，就是正在传输信号，并且 CLK 提供了时钟同步功能，效验也更精确。

## 串口通讯实验

在进行下一步实验之前，需要在 CubeMX 里配置串口下载、时钟等各类参数。  
具体步骤请参考文章 [**HAL 库开发笔记（一） - 环境配置**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0%EF%BC%88%E4%B8%80%EF%BC%89-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E9%A1%B9%E7%9B%AE%E7%9A%84%E9%85%8D%E7%BD%AE) 中的方法进行配置。

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
        HAL_UART_Transmit(&huart1, &Buffer, 1, 0xff);
        HAL_UART_Receive_IT(&huart1,&Buffer,1);
    }
}

/* USER CODE END 1 */
```

其中，`Buffer` 是在 `main.c` 中定义的 uint8_t 类型全局变量。这里每接受的一个字节后就产生中断，将该字节数据返回并重新开启中断。我们需要分别在 `main.c` 和 `stm32f4xx_it.c` 中定义它：

```c title="main.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

uint8_t Buffer;

/* USER CODE END PV */
```

```c title="stm32f4xx_it.c"
/* Private variables -----------------------------------------------------------*/
/* USER CODE BEGIN PV */

extern uint8_t Buffer;

/* USER CODE END PV */

```

另外，在 `main.c` 中，我们需要在串口初始化后、主循环前，添加接收中断开启函数：

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_UART_Receive_IT(&huart1,&Buffer,1);

/* USER CODE END 2 */
```

最后，我们需要对 printf 进行重定向。意思就是把 printf 函数用在 STM32 中做串口是输出功能。只需要在 `usart.c` 中重写 fputc 函数并使其作用于串口即可：

```c title="usart.c"
/* USER CODE BEGIN 0 */

#include "stdio.h"

/* USER CODE END 0 */

......

/* USER CODE BEGIN 0 */

int fputc(int ch,FILE *f)
{
	HAL_UART_Transmit(&huart1,(uint8_t*)&ch,1,100);
	return ch;
}

/* USER CODE END 0 */
```

### 下载验证

程序烧录成功后，我们打开串口助手，配置对应的端口和波特率。  
本实验的效果是，发送什么内容，就返回同样的内容，如图所示：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210403232628.png)

## 参考与致谢

- [STM32CubeMX 实战教程（六）—— 串口通信](https://blog.csdn.net/weixin_43892323/article/details/105339949)
- [进阶篇 III [UART & USART]](https://alchemicronin.github.io/posts/b4c69a89/#1-0-%E4%BB%80%E4%B9%88%E6%98%AFUART%E5%92%8CUSART%EF%BC%9F%E6%9C%89%E4%BB%80%E4%B9%88%E5%8C%BA%E5%88%AB%E5%98%9B%EF%BC%9F)

> 文章作者：**Power Lin**  
> 原文地址：<https://wiki-power.com>  
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。
