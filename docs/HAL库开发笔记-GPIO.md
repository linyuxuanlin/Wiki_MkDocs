---
id: HAL库开发笔记-GPIO
title: HAL 库开发笔记 - GPIO
---

## 基本原理

GPIO 是 **通用输入输出端口**（General Purpose Input Output）。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200615205256.jpg)

拿 F103C8T6 芯片举个例子（上图），除了有颜色的引脚（电源和某些功能引脚）之外的，都叫 GPIO. 可见其通用程度。

GPIO 的功能是输入 / 输出电信号。我们来看看它的内部结构：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20200615211744.jpg)

- 最右边的 I/O 引脚 ，就是实物芯片的引脚。上下的 `保护二极管` 在一定程度上可防止外部不正常电压经引脚烧毁芯片。
- 红色虚线框内是输入功能（芯片读取外部信号）。两个带开关的上拉 / 下拉电阻，是用来实现上下拉输入功能的。如果两个开关都不闭合，我们则称其为浮空输入（上不顶天下不着地，没有参考电平）。这三种输入模式读出来的都是数字量（高 / 低电平）。此外，还有模拟输入功能，顾名思义就是直接读取引脚上的模拟量。（复用功能输入我们后面再提及）。
- 蓝色虚线框内是输出功能。输出有 4 种模式：推挽、开漏、复用推挽、复用开漏。

### 输入输出模式

输入模式：

- **浮空输入**：既不上拉也不下拉， STM32 复位之后的默认模式。
- **上拉输入**：闭合上拉电阻的开关，使参考电平永远保持在高位，当输入信号为低电平时就触发。
- **下拉输入**：闭合下拉电阻的开关，使参考电平永远保持在低位，当输入信号为高电平时就触发。
- **模拟输入**：这个模式下，既不上拉也不下拉，也不经过 TTL 触发器，STM32 直接读取引脚上的模拟信号。

输出模式：

- **开漏输出**：开漏指的是开下方的 N-MOS 管的漏极（上面的引脚），这个模式仅仅用到下方的 N-MOS 管。我们知道，MOS 管是电压控的元器件。理解为水龙头，给 N-MOS 的栅极（左边的引脚）输入低电平信号时，N-MOS 就导通。
- **推挽输出**：推挽有两种模式，第一种是同时给两个 MOS 管的栅极通低电平，此时 P-MOS 导通而 N-MOS 截止，电流从 VDD 流向外部引脚，引脚呈高电平。第二种则相反，同时给两个 MOS 管的栅极通高电平，此时 P-MOS 截止而 N-MOS 导通，电流从外部引脚流向内部的 GND，引脚呈低电平。
- **复用开漏**
- **复用推挽**

### 常用的 GPIO 函数参考

读取 GPIO 状态，返回高 / 低电平：

```c
GPIO_PinState HAL_GPIO_ReadPin(GPIOx, GPIO_Pin);
```

写 GPIO 状态，写入高 / 低电平：

```c
HAL_GPIO_WritePin(GPIOx, GPIO_Pin, PinState);
```

翻转 GPIO 电平：

```c
HAL_GPIO_TogglePin(GPIOx, GPIO_Pin);
```

## 点亮 LED

在进行下一步实验之前，需要在 CubeMX 里配置串口下载、时钟等各类参数。  
此处不再赘述，请跳转文章 [**HAL 库开发笔记 - 环境配置**](https://wiki-power.com/HAL%E5%BA%93%E5%BC%80%E5%8F%91%E7%AC%94%E8%AE%B0-%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE) 中的方法进行配置。

### 在 CubeMX 内配置 GPIO

将 LED 相应的 GPIO 口设置为输出，并设置初始电平。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205150422.png)

对应到我的板子上，就需要把 `PD4` 和 `PI3` 这两个 GPIO 设置为输出（`GPIO_Output`）。  
如果想要上电就点亮，那么根据电路原理图，将初始电位设置为低（`Low`）。

### 在代码内配置 GPIO

如果配置之无误的话，上电即可点亮两颗用户 LED.  
如果要添加闪灯效果，只需要在主循环的用户代码区域内添加几行代码：

```c title="main.c"
/* USER CODE BEGIN 3 */

HAL_Delay(500);
HAL_GPIO_TogglePin(GPIOD, GPIO_PIN_4);
HAL_GPIO_TogglePin(GPIOI, GPIO_PIN_3);

}
/* USER CODE END 3 */
```

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205151322.png)

即可实现闪灯效果。

## 按键控灯

在学习了 GPIO 的输出后，我们用按键来学习 GPIO 的输入模式。

### 在 CubeMX 内配置 GPIO

按照上面的方法配置 LED 所属的 GPIO 端口后，根据板载按键的原理图：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210205150422.png)

将按键所属的 GPIO（`PI8`）设置为输入（`GPIO_Input`）。根据原理图，选择内部上拉（`Pull-up`）。生成代码。

### 在代码内配置 GPIO

在主循环的用户代码区域内添加如下代码：

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

即可实现按下按键开灯，松开按键关灯的效果。

有许多人搞不清楚 `GPIO_PIN_SET` 和 `GPIO_PIN_RESET` 是什么意思。其实这两个变量的功能仅仅为设置 GPIO 引脚高 / 低电平。具体灯是开是关，还得看电路原理图。

另外，`HAL_Delay(100);` 的功能是代码消除按键抖动。不过 `HAL_Delay()` 函数用的是轮询，会占用资源导致卡机，下一篇文章我们将用硬件中断来解决这个缺陷。

## 参考与致谢

- [【STM32】STM32CubeMX 教程二 -- 基本使用 (新建工程点亮 LED 灯)](https://blog.csdn.net/as480133937/article/details/98947162)
- [STM32CubeMX 实战教程（二）—— 按键点个灯](https://blog.csdn.net/weixin_43892323/article/details/104343933)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

