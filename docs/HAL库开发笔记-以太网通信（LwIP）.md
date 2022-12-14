---
id: HAL库开发笔记-以太网通信（LwIP）
title: HAL 库开发笔记 - 以太网通信（LwIP） 🚧
---

以下是基于 [**反客 STM32F407 主控核心板**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) 与 [**DP83848 以太网 PHY 模块**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail) 的教程。

## 硬件

DP83848 接口为 RMII，DP83848 可支持 10M/100M 的线速，板载 50MHz 无源晶振。

| STM32 主控  | DP83848 模块 |
| ----------- | ------------ |
| ETH_REF_CLK | PA1          |
| ETH_MDIO    | PA2          |
| ETH_MDC     | PC1          |
| ETH_CRS_DV  | PA7          |
| ETH_RXD0    | PC4          |
| ETH_RXD1    | PC5          |
| ETH_TX_EN   | PB11         |
| ETH_TXD0    | PB12         |
| ETH_TXD1    | PB13         |

## 软件

### CubeMX 内配置

- RCC：HSE 选择外部晶振
- SYS
  - DEBUG：SW
- GPIO
  - PA15：`USER_BTN`, Input, Pull-up
  - PC13：`LED_GREEN`, Output Push Pull, level High
  - PC14：`LED_BLUE`, Output Push Pull, level High
  - PC15：`LED_RED`, Output Push Pull, level High
- ETH
  - Mode：RMII
  - Advanced Parameters
    - PHY：DP83848_PHY_ADDRESS
- LWIP
  - Key Options
    - 勾选 Show Advanced Parameters
    - 确保 LWIP_NETIF_LINK_CALLBACK 为 Enable（一般默认）
    - xLWIP_LOOPIF_MULTICAST：Enabled
    - xLWIP_MULTICAST_TX_OPTIONS：Enabled
    - xLWIP_NETIF_STATUS_CALLBACK：Enabled
    - xLWIP_NETIF_EXT_STATUS_CALLBACK：Enabled
    - xLWIP_SO_RCVBUF：Enabled
  - Genetal Settings
    - xLWIP_IGMP：Enabled

时钟树配置：按照板载晶振（此板为 8M）配置。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220702145310.png)

### 添加功能代码

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */

/* USER CODE BEGIN 0 */
void ethernetif_notify_conn_changed(struct netif *netif) {
	/* NOTE : This is function could be implemented in user file
	 when the callback is needed,
	 */
	if (netif_is_link_up(netif)) {
		HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_RESET);
		HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_SET);
	} else {
		HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_SET);
		HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_RESET);
	}
}
/* USER CODE END 0 */

/* USER CODE BEGIN 2 */
ethernetif_notify_conn_changed(&gnetif);
/* USER CODE END 2 */

/* USER CODE BEGIN 3 */
MX_LWIP_Process();
}
/* USER CODE END 3 */
```

```c title="lwip.c"
/* USER CODE BEGIN 4_3 */
ethernetif_set_link(&gnetif);
if (netif_is_link_up(&gnetif) && !netif_is_up(&gnetif)) {
	netif_set_up(&gnetif);
	dhcp_start(&gnetif);
}
/* USER CODE END 4_3 */
```

## 调试

- 查看连接到此电脑的设备 IP：`arp -a`
- 通过插拔确定 STM32 的 IP 地址
- `ping [ip 地址] (-t)`
- 热插拔网线会出现 `传输失败，常见故障`，稍等即可自动重新建立连接。

## 参考与致谢

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。


---

```
本篇基于自研 RobotCtrl 开发套件，单片机内核为 STM32F407ZET6，以太网 PHY 芯片为 LAN8720A，原理图及详细介绍请见 [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6)。

LwIP 是 轻型（Light Weight）IP 协议，不管有没有操作系统的支持，都可以运行。LwIP 实现的重点是在保持 TCP 协议主要功能的基础上减少对 RAM 的占用，它只需十几 KB 的 RAM 和 40K 左右的 ROM 就可以运行，这使 LwIP 协议栈适合在低端的嵌入式系统中使用。

LwIP 提供了三种编程接口，分别为 RAW/Callback API、NETCONN API、SOCKETAPI。它们的易用性从左到右依次提高，而执行效率从左到右依次降低。可以权衡利弊选择适合自己的 API 进行开发。在本文中，使用 Raw API，调用以下的函数：

| API 函数       | 说明                                     |
| -------------- | ---------------------------------------- |
| udp_new        | 创建新的 UDP PCB                         |
| udp_remove     | 移除 UDP PCB 并释放相关资源              |
| udp_bind       | UDP PCB 与本地 IP 地址和端口绑定         |
| udp_connect    | 建立 UDP PCB 远程 IP 地址和端口          |
| udp_disconnect | 移除 UDP PCB 远程 IP 和端口              |
| udp_send       | 发送 UDP 数据                            |
| udp_recv       | 注册回调函数，当收到新数据报时即对其调用 |

## CubeMX 内配置

1. 在 `RCC` 页面内为 HSE 选择外部晶振。
2. 在 `ETH` 页面内配置 PHY 模式为`RMII`，并配置以下参数：
   1. 在 `Parameter Setting` 标签页下，将 `PHY Address` 配置为 `0`（根据 PHYAD0 管脚配置决定的）。
   2. 在 `Advanced Parameter` 标签页下，根据 LAN8720A 的芯片手册，将 `PHY special control/status register Offset` 配置为 `31`； `PHY Speed mask` 配置为 `0x0004`； `PHY Duplex mask` 配置为 `0x0010`。
3. 在 `LWIP` 页面内开启使能，并配置以下参数：
   1. 在 `General Settings` 标签页下，将 `LWIP_DHCP (DHCP Module)` 配置为 `Disabled`（使用静态 IP）； `IP_ADDRESS` 配置为 `192.168.001.100`； `NETMASK_ADDRESS` 配置为 `255.255.255.000`；`GATEWAY_ADDRESS` 配置为 `192.168.001.001`；`LWIP_UDP (UDP Module)` 和 `LWIP_TCP (TCP Module)` 配置为 `Enabled`。

## 参考与致谢

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> 文章作者：**Power Lin**
> 原文地址：<https://wiki-power.com>
> 版权声明：文章采用 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议，转载请注明出处。

```
