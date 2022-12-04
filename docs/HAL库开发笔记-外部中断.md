---
id: HAL库开发笔记-外部中断
title: HAL 库开发笔记 - 外部中断
---

上一篇文章我们提到，用轮询的方法消除按键抖动、检测输入，有可能会消耗过多的系统资源并导致卡机，也有可能会错过检测。这就是为什么我们需要使用中断了。

## 基本原理

### 轮询与中断

什么是轮询和中断？以取外卖举个例子，轮询就是每分钟我都要去一趟门口，看看外卖小哥来了没。那么这段时间我做不了别的事情了，就光盯着外卖；但假如外卖小哥在我恰好离开门口的时候送到了，那么就错过了外卖。相反的，中断就是让外卖小哥来的时候打个电话，我搁下手中的活去拿外卖，这样我既能够安心干活，又不怕错过外卖。

### 外部中断

中断分外部（Interrupt）和内部（Exception）。外部中断由外部外设来打断 MCU，内部中断由内部的软件程序自行打断 MCU.

### NVIC

NVIC 全称为 Nested Vectored Interrupt Controller，翻译过来就是 **嵌套向量中断控制器** 。它主要有三个参数，分别是：中断使能，抢占优先级，响应优先级。（优先级数值越小，优先级越高）

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210206121058.png)

**中断使能**：指的就是是否开启中断。如果开启中断，那么当满足中断触发条件的时候，会跳到中断服务程序运行；否则不理会中断服务程序，继续运行主程序。

**抢占优先级**：用于判断一个中断是否可以打断另一个中断的服务程序，抢先运行。举个例子，条件触发了 A 中断，A 中断的服务程序正在运行中，此时条件触发了 B 中断。此时如果 B 中断的抢占优先级比 A 的高，那么 A 的服务程序就会被打断，先去执行 B 的服务程序，执行完之后再继续执行 A，这也称为中断嵌套。如果 B 的抢占优先级不比 A 高，那还是乖乖先执行完 A，再去执行 B.

**响应优先级**：如果抢占优先相同的几个中断同时被触发，那么响应优先级高的最先运行。

欲判断中断的优先级，首先要先比较的是抢占优先级。抢占优先级相同的情况下，响应优先高的中断优先级别高。如果两个优先级都一样，那么就要根据中断向量表来确定。

### 中断回调函数参考

配置了 GPIO 中断和 NVIC 优先级之后，在 `stm32f4xx_it.c` 文件末尾重写中断回调函数即可实现功能。

```c
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{

}

/* USER CODE END 1 */
```

## 外部中断按键控灯

在进行下一步实验之前，需要在 CubeMX 里配置串口下载、时钟等各类参数。  
具体步骤请跳转文章 [**HAL 库开发笔记 - 环境配置**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) 中的方法进行配置。

### 在 CubeMX 内配置中断

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205150422.png)

如图，LED 还是按照上一篇文章的方法，配置为输出；按键因为是低电平触发，也就是在按下的一瞬间会产生一个下降沿，所以引脚应该配置为下降沿触发的中断。

在我的板子上，就是将 `PI8` 配置为 `GPIO_EXTI8` 模式（外部中断，挂载在中断线 8 上的），并配置为下降沿触发，根据原理图，选择内部上拉（Pull-up）。如图所示：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210403222304.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210206131409.png)

接着，点击跳转 NVIC 标签页面，使能我们配置的中断：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210206134916.png)

另外，要把抢占优先级降低一位（从 0 变为 1，原因下文会解释）。

### 在代码内配置中断

只需要在 `stm32f4xx_it.c` 末尾添加如下代码：

```c title="stm32f4xx_it.c"
/* USER CODE BEGIN 1 */

void HAL_GPIO_EXTI_Callback(uint16_t GPIO_Pin)
{
    if(HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0)
    {
        HAL_Delay(100);
        if(HAL_GPIO_ReadPin(KEY1_GPIO_Port, KEY1_Pin) == 0)
        {
            HAL_GPIO_TogglePin(LED1_GPIO_Port,LED1_Pin);
        }
    }
}

/* USER CODE END 1 */
```

这段代码的作用是重写中断的回调函数，增加用按键切换灯开关的功能。但是这里的 `HAL_Delay()` 延时函数有坑，因为其来源是 SysTick 定时器（在固定时间间隔内产生中断），所以就有所属的中断优先级。在上面配置 NVIC 的图中可以看出，SysTick 和我们配置的中断抢占优先级都是 0，所以便无法在外部中断触发时接着触发 SysTick 了。所以，我们要把外部中断的抢占优先级改低（由 0 改为 1）。

编译上传后即可通过按下按键，切换 LED 灯的亮灭状态了。

## 参考与致谢

- [进阶篇 II [Interrupt]](https://alchemicronin.github.io/posts/ff6aca34/)
- [STM32CubeMX 实战教程（三）—— 外部中断（中断及 HAL_Delay 函数避坑）](https://blog.csdn.net/weixin_43892323/article/details/104383560?utm_medium=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control&depth_1-utm_source=distribute.pc_relevant.none-task-blog-BlogCommendFromMachineLearnPai2-1.control)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

