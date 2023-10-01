# HAL Library Development Notes - Ethernet Communication (LwIP) 🚧

This tutorial is based on the [**Fanke STM32F407 control core board**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) and [**DP83848 Ethernet PHY module**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## Hardware

The DP83848 interface is RMII, and it supports 10M/100M line speed. The board has a 50MHz passive crystal oscillator.

| STM32 Control Core | DP83848 Module |
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

## Software

### Configuration in CubeMX

- RCC: HSE selects external crystal oscillator
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN`, Input, Pull-up
  - PC13: `LED_GREEN`, Output Push Pull, level High
  - PC14: `LED_BLUE`, Output Push Pull, level High
  - PC15: `LED_RED`, Output Push Pull, level High
- ETH
  - Mode: RMII
  - Advanced Parameters
    - PHY: DP83848_PHY_ADDRESS
- LWIP
  - Key Options
    - Check Show Advanced Parameters
    - Ensure LWIP_NETIF_LINK_CALLBACK is Enable (usually default)
    - xLWIP_LOOPIF_MULTICAST: Enabled
    - xLWIP_MULTICAST_TX_OPTIONS: Enabled
    - xLWIP_NETIF_STATUS_CALLBACK: Enabled
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: Enabled
    - xLWIP_SO_RCVBUF: Enabled
  - General Settings
    - xLWIP_IGMP: Enabled

Clock tree configuration: configured according to the onboard crystal oscillator (8M for this board).

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220702145310.png)

### Adding functional code

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

## Debugging

- View devices connected to this computer's IP: `arp -a`
- Determine the IP address of the STM32 by plugging and unplugging
- `ping [ip address] (-t)`
- Hot-plugging the Ethernet cable may result in "Transmission failed, common fault", but the connection will automatically be re-established after a short wait.

## References and Acknowledgements

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

---

```
This article is based on our self-developed RobotCtrl development kit, with the STM32F407ZET6 microcontroller as the core and the LAN8720A Ethernet PHY chip. For the schematic and detailed introduction, please refer to [**RobotCtrl - STM32 Universal Development Kit**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

LwIP is a lightweight IP protocol that can run regardless of whether there is operating system support. The focus of LwIP implementation is to reduce RAM usage while maintaining the main functions of the TCP protocol. It only requires about a dozen KB of RAM and around 40K of ROM to run, making it suitable for use in low-end embedded systems.

LwIP provides three programming interfaces: RAW/Callback API, NETCONN API, and SOCKETAPI. Their ease of use increases from left to right, while their execution efficiency decreases from left to right. You can choose the API that suits you best based on the trade-offs. In this article, we use the Raw API and call the following functions:

| API Function  | Description                                |
| ------------- | ------------------------------------------ |
| udp_new       | Create a new UDP PCB                        |
| udp_remove    | Remove the UDP PCB and release related resources |
| udp_bind      | Bind the UDP PCB to the local IP address and port |
| udp_connect   | Establish the remote IP address and port of the UDP PCB |
| udp_disconnect | Remove the remote IP and port of the UDP PCB |
| udp_send      | Send UDP data                               |
| udp_recv      | Register a callback function to be called when new data is received |

## Configuration in CubeMX

1. Select external crystal for HSE on the RCC page.
2. Configure PHY mode as RMII on the ETH page and set the following parameters:
   1. Under the Parameter Setting tab, set PHY Address to 0 (determined by PHYAD0 pin configuration).
   2. Under the Advanced Parameter tab, according to the LAN8720A chip manual, set PHY special control/status register Offset to 31; PHY Speed mask to 0x0004; and PHY Duplex mask to 0x0010.
3. Enable LWIP on the LWIP page and set the following parameters:
   1. Under the General Settings tab, set LWIP_DHCP (DHCP Module) to Disabled (use static IP); set IP_ADDRESS to 192.168.001.100; set NETMASK_ADDRESS to 255.255.255.000; set GATEWAY_ADDRESS to 192.168.001.001; and set LWIP_UDP (UDP Module) and LWIP_TCP (TCP Module) to Enabled.

## References and Acknowledgements

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> Article author: **Power Lin**
> Original address: <https://wiki-power.com>
> Copyright statement: The article is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). 
> Please indicate the source when reprinting.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.