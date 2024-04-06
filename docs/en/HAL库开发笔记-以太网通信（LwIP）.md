# HAL Library Development Notes - Ethernet Communication (LwIP) 🚧

The following is a tutorial based on the [**Reverse Customer STM32F407 Main Control Core Board**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) and [**DP83848 Ethernet PHY Module**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## Hardware

The DP83848 interface is RMII, and DP83848 supports 10M/100M line speed, with a built-in 50MHz passive crystal oscillator.

| STM32 Main Control | DP83848 Module |
| ------------------ | -------------- |
| ETH_REF_CLK        | PA1            |
| ETH_MDIO           | PA2            |
| ETH_MDC            | PC1            |
| ETH_CRS_DV         | PA7            |
| ETH_RXD0           | PC4            |
| ETH_RXD1           | PC5            |
| ETH_TX_EN          | PB11           |
| ETH_TXD0           | PB12           |
| ETH_TXD1           | PB13           |

## Software

### CubeMX Configuration

- RCC: Select external crystal oscillator for HSE.
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN`, Input, Pull-up
  - PC13: `LED_GREEN`, Output Push Pull, Level High
  - PC14: `LED_BLUE`, Output Push Pull, Level High
  - PC15: `LED_RED`, Output Push Pull, Level High
- ETH
  - Mode: RMII
  - Advanced Parameters
    - PHY: DP83848_PHY_ADDRESS
- LWIP
  - Key Options
    - Check Show Advanced Parameters
    - Ensure LWIP_NETIF_LINK_CALLBACK is Enable (usually the default)
    - xLWIP_LOOPIF_MULTICAST: Enabled
    - xLWIP_MULTICAST_TX_OPTIONS: Enabled
    - xLWIP_NETIF_STATUS_CALLBACK: Enabled
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: Enabled
    - xLWIP_SO_RCVBUF: Enabled
  - General Settings
    - xLWIP_IGMP: Enabled

Clock Tree Configuration: Set according to the onboard crystal oscillator (in this case, 8M).

![Clock Tree Configuration](https://media.wiki-power.com/img/20220702145310.png)

### Adding Functional Code

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */
```

Please let me know if you need further information or assistance!

```c
ethernetif_notify_conn_changed(struct netif *netif)
```

This function, as noted, can be implemented in a user file when the callback is needed. It checks if the network link is up using `netif_is_link_up(netif)` and then controls the state of two LEDs using `HAL_GPIO_WritePin`. If the link is up, it turns on the green LED and turns off the red LED, and vice versa if the link is down.

```c
ethernetif_notify_conn_changed(&gnetif);
```

This line calls the `ethernetif_notify_conn_changed` function and passes the `gnetif` structure as an argument.

```c title="lwip.c"
ethernetif_set_link(&gnetif);
if (netif_is_link_up(&gnetif) && !netif_is_up(&gnetif)) {
	netif_set_up(&gnetif);
	dhcp_start(&gnetif);
}
```

In this part of the code from the `lwip.c` file, it first sets the link status using `ethernetif_set_link(&gnetif)`. Then, it checks if the link is up and the network interface is not up. If both conditions are met, it sets the network interface up and starts DHCP.

## Debugging

- To view the IP addresses of devices connected to this computer, you can use the command `arp -a`.
- To determine the IP address of the STM32 by plugging and unplugging, you can use the `ping` command with the `-t` flag.
- When hot-plugging the network cable, you may encounter "Transmission failed, common fault" messages. Just wait for the connection to be automatically reestablished.

## References and Acknowledgments

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

[Replace_1]  
[Replace_2]

---

```
This article is based on the self-developed RobotCtrl development kit, with the STM32F407ZET6 microcontroller as the core and the LAN8720A Ethernet PHY chip. For the schematic and detailed information, please refer to [**RobotCtrl - STM32 General Development Kit**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

LwIP is a lightweight IP protocol that can run regardless of operating system support. LwIP's key focus is on reducing RAM usage while retaining the core functionality of the TCP protocol. It only requires about ten kilobytes of RAM and around 40 kilobytes of ROM to operate, making it suitable for low-end embedded systems.

LwIP provides three programming interfaces: RAW/Callback API, NETCONN API, and SOCKETAPI. They vary in ease of use and efficiency from left to right. Developers can choose the API that best suits their needs. In this article, the Raw API is used, and the following functions are called:
```

```markdown
| API Function   | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| udp_new        | Create a new UDP PCB                                                |
| udp_remove     | Remove UDP PCB and release related resources                        |
| udp_bind       | Bind UDP PCB to a local IP address and port                         |
| udp_connect    | Establish remote IP address and port for UDP PCB                    |
| udp_disconnect | Remove remote IP and port from UDP PCB                              |
| udp_send       | Send UDP data                                                       |
| udp_recv       | Register a callback function to be called when new data is received |

## Configuration within CubeMX

1. In the `RCC` page, select an external crystal for HSE.
2. In the `ETH` page, configure the PHY mode as `RMII` and set the following parameters:
   1. Under the `Parameter Setting` tab, configure the `PHY Address` as `0` (determined by PHYAD0 pin).
   2. Under the `Advanced Parameter` tab, based on the LAN8720A datasheet, configure `PHY special control/status register Offset` as `31`; `PHY Speed mask` as `0x0004`; `PHY Duplex mask` as `0x0010`.
3. In the `LWIP` page, enable and configure the following parameters:
   1. Under the `General Settings` tab, set `LWIP_DHCP (DHCP Module)` to `Disabled` (use static IP); configure `IP_ADDRESS` as `192.168.001.100`; `NETMASK_ADDRESS` as `255.255.255.000`; `GATEWAY_ADDRESS` as `192.168.001.001`; and enable `LWIP_UDP (UDP Module)` and `LWIP_TCP (TCP Module)`.

## References and Acknowledgments

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
