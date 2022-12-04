---
id: HAL库开发笔记-CAN通信
title: HAL 库开发笔记 - CAN 通信 🚧
---

本篇基于自研 RobotCtrl 开发套件，单片机内核为 STM32F407ZET6，CAN 通信使用 TJA1050 芯片，原理图及详细介绍请见 [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6)。

## 回环测试简单步骤

### CubeMX 内配置

1. 根据所用的 CAN 硬件，在左侧栏点开 `CAN1` 或 `CAN2` 页面，勾选 `Activated`，在参数页面，配置这些参数：
   1. 将 `Prescaler (for Time Quantum)` 设置为 `6`，`Time Quanta in Bit Segment 1` 和 `Time Quanta in Bit Segment 2` 都设置为 `3 Times`，这个组合将比特率设置为 1Mbps（最高）。
   2. 将 `ReSynchronization Jump Width` 配置为 `1 Time` ，这是重新同步时可调整的最大步长。
   3. 将 `Operating Mode` 配置为 `Loopback`，用于回环测试。
2. 在 `NVIC Settings` 标签页，开启 `CANx RX0 interrupts`。

### 代码内配置

在项目下创建 `can.c`，设置筛选器，这里配置的是列表模式，筛选了拓展 ID `0x2233` 和标准 ID `0`：

```c title="can.c"/*
 * 函数名：CAN_Filter_Config
 * 描述  ：CAN的过滤器 配置
 * 输入  ：无
 * 输出  : 无
 * 调用  ：内部调用
 */
static void CAN_Filter_Config(void) {
	CAN_FilterTypeDef CAN_FilterTypeDef;

	/*CAN筛选器初始化*/
	CAN_FilterTypeDef.FilterBank = 0;						//筛选器组0
	CAN_FilterTypeDef.FilterMode = CAN_FILTERMODE_IDLIST;	//工作在列表模式
	CAN_FilterTypeDef.FilterScale = CAN_FILTERSCALE_32BIT;	//筛选器位宽为单个32位。
	/* 使能筛选器，按照标志的内容进行比对筛选，扩展ID不是如下的就抛弃掉，是的话，会存入FIFO0。 */

	CAN_FilterTypeDef.FilterIdHigh = ((((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF0000) >> 16;		//要筛选的ID高位
	CAN_FilterTypeDef.FilterIdLow = (((uint32_t) 0x2233 << 3) | CAN_ID_EXT
			| CAN_RTR_DATA) & 0xFFFF; //要筛选的ID低位
	CAN_FilterTypeDef.FilterMaskIdHigh = 0;		//第二个ID的高位
	CAN_FilterTypeDef.FilterMaskIdLow = 0;			//第二个ID的低位
	CAN_FilterTypeDef.FilterFIFOAssignment = CAN_FILTER_FIFO0;	//筛选器被关联到FIFO0
	CAN_FilterTypeDef.FilterActivation = ENABLE;			//使能筛选器
	HAL_CAN_ConfigFilter(&hcan1, &CAN_FilterTypeDef);
}
```

### 测试

打开设备管理器查看设备是否已经显示，如果没有发现设备，或有黄色的感叹号，请到 ST 官网下载驱动 [**STM32 Virtual COM Port Driver**](https://www.st.com/content/st_com/en/products/development-tools/software-development-tools/stm32-software-development-tools/stm32-utilities/stsw-stm32102.html)。

如果安装了驱动还是未能正常识别，可尝试在 CubeMX - `Project Manager` - `Project` - `Linker Settings`，将 `Minimum Heap Size` 调整为 `0x600` 或更高。

打开串口工具（波特率任意），可发现发送任意字符，将返回相同字符。

## 参考与致谢

- [STM32CubeMX 与 HAL 库学习--简单的 CAN 回环测试](https://blog.csdn.net/weixin_45209978/article/details/119850600)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

