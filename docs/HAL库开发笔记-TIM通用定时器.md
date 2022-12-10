---
id: HAL库开发笔记-TIM通用定时器
title: HAL 库开发笔记 - TIM 通用定时器
---

在上一篇文章中，简单介绍了 STM32F4 的三类定时器，也详细讲解了基本定时器。在本篇文章中，我们将继续介绍通用定时器。

## 基本原理

在 STM32F4 中，通用定时器有 TIM2-TIM5，TIM9-TIM14。

### 通用定时器的特性

在 STM32F4 中，通用定时器的特性如下：

- 16/32 位递增、递减和递增 / 递减自动重载计数器
- 16 位可编程预分频器，用于对计数器时钟频率进行分频（分频系数为 1-65536）
- 4 个独立通道，分别可用于：
  - 输入捕获
  - 输出比较
  - PWM 生成（边沿和中心对齐模式）
  - 单脉冲模式输出
- 使用外部信号控制定时器且可实现多个定时器互连的同步电路
- 发生如下事件时生成中断 / DMA 请求：
  - 更新：计数器上溢 / 下溢、计数器初始化（通过软件或内部 / 外部触发）
  - 触发事件（计数器启动、停止、初始化或通过内部 / 外部触发计数）
  - 输入捕获
  - 输出比较
- 支持定位用增量（正交）编码器和霍尔传感器电路
- 外部时钟触发输入或逐周期电流管理

### 常用的定时器函数参考

以下是常用的定时器函数参考，与基本定时器的函数相同。

- **HAL_TIM_Base_Init()**：初始化定时器时基单元
- **HAL_TIM_Base_DeInit()**：禁用定时器，与初始化相反
- **HAL_TIM_Base_MspInit()**：MSP 初始化函数，定时器初始化时会自动调用
- **HAL_TIM_Base_MspDeInit()**：与上一个相反
- **HAL_TIM_Base_Start()**：开启定时器
- **HAL_TIM_Base_Stop()**：停止定时器
- **HAL_TIM_Base_Start_IT()**：以中断模式开启定时器
- **HAL_TIM_Base_Stop_IT()**：关闭中断模式的定时器
- **HAL_TIM_Base_Start_DMA()**：以 DMA 模式开启定时器
- **HAL_TIM_Base_Stop_DMA()**：关闭 DMA 模式的定时器

## 用通用定时器输出 1 kHz/50% 占空比的 PWM

本次实验使用通用定时器输出 1 kHz，50% 占空比的 PWM 信号，可用示波器显示输出的波形。

### 在 CubeMX 内配置通用定时器

首先，我们打开 Clock Configuratgion 时钟树配置页面，因通用定时器挂载在挂载在高速 APB2 总线上，所以我们找到并记下 APB2 Timer clocks 的时钟频率（180 MHz）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210627133951.png)

接着，我们找到侧边栏 Timer 中找到 TIM8，设置通道 1（`Channel 1`）为 PWM 生成（`PWM Generation CH1`），为了能生成 1 kHz 频率的 PWM 方波，我们需要在下方配置以下参数：

- **Prescaler**（预分频系数）：180-1
- **Counter Mode**（计数模式）：Up（从 0 开始向上计数至预分频系数后溢出）
- **Counter Period**（计时周期 / 装载值）：1000-1
- **auto-reload preload**（是否自动重装载）：Enable（溢出时会自动重装初值）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210627153422.png)

因此处选用的时钟源为 180 MHz，因此将预分频系数设置为 180-1 = 179，分频后为 1 MHz，将装载值设置为 1000-1 = 9999，所以得到 1 kHz 的频率。

### 在代码内配置基本定时器

在 `main.c` 中开启定时器：

```c title="main.c"
/* USER CODE BEGIN 2 */

HAL_TIM_PWM_Start(&htim8,TIM_CHANNEL_1);

// 设置占空比为 500（500 Hz/1 kHz=50%）
__HAL_TIM_SetCompare(&htim8,TIM_CHANNEL_1,500);

/* USER CODE END 2 */
```

编译并烧录，用示波器可以看出波形：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210627154737.jpg)

## 参考与致谢

- [STM32CubeMX 实战教程（五）—— 通用定时器（PWM 输出）](https://blog.csdn.net/weixin_43892323/article/details/104776035)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

