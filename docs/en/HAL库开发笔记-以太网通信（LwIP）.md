# HAL Library Development Notes - Ethernet Communication (LwIP) 🚧

The following is a tutorial based on the [**Anti-Client STM32F407 Main Control Board**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) and [**DP83848 Ethernet PHY Module**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## Hardware

The DP83848 interface is RMII, and DP83848 supports 10M/100M line speed, with a built-in 50MHz passive crystal.

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

- RCC: Select external crystal for HSE.
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

Clock Tree Configuration: Set according to the onboard crystal (8M for this board).

![Clock Tree Configuration](https://img.wiki-power.com/d/wiki-media/img/20220702145310.png)

### Adding Functional Code

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */
```

Please let me know if you need any further assistance or information.

```c
void ethernetif_notify_conn_changed(struct netif *netif) {
    /* NOTE: This function could be implemented in a user file when the callback is needed. */
    if (netif_is_link_up(netif)) {
        HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_RESET);
        HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_SET);
    } else {
        HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_SET);
        HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_RESET);
    }
}
```

```c title="lwip.c"
/* Set the link status for the network interface. */
ethernetif_set_link(&gnetif);

/* If the link is up and the network interface is not yet up, set it up and start DHCP. */
if (netif_is_link_up(&gnetif) && !netif_is_up(&gnetif)) {
    netif_set_up(&gnetif);
    dhcp_start(&gnetif);
}
```

## Debugging

- View the devices connected to this computer's IP: `arp -a`
- Determine the STM32's IP address by plugging and unplugging.
- `ping [ip address] (-t)`
- Hot-plugging the network cable may result in a "Transmission failed, common issue," but it will automatically reconnect after a short delay.

## References and Acknowledgments

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

[to_be_replaced[1]]
[to_be_replaced[2]]

---

```
This article is based on the self-developed RobotCtrl development kit, with the STM32F407ZET6 microcontroller as the core and the LAN8720A Ethernet PHY chip. For the schematic and detailed information, please refer to [**RobotCtrl - STM32 General Development Kit**[to_be_replaced[3]]RobotCtrl-STM32 General Development Kit).

LwIP is a lightweight IP protocol that can run without the support of an operating system. LwIP's main focus is on minimizing RAM usage while maintaining the essential functions of the TCP protocol. It can run with just over ten kilobytes of RAM and around 40 kilobytes of ROM, making it suitable for low-end embedded systems.

LwIP provides three programming interfaces: RAW/Callback API, NETCONN API, and SOCKET API. Their ease of use and efficiency decrease from left to right. You can choose the API that suits your development needs. In this article, we use the Raw API and call the following functions:
```

| API Function   | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| udp_new        | Create a new UDP PCB                                                |
| udp_remove     | Remove UDP PCB and release related resources                        |
| udp_bind       | Bind UDP PCB to a local IP address and port                         |
| udp_connect    | Establish remote IP address and port for UDP PCB                    |
| udp_disconnect | Remove remote IP and port for UDP PCB                               |
| udp_send       | Send UDP data                                                       |
| udp_recv       | Register a callback function to be called when new data is received |

## Configuration within CubeMX

1. On the `RCC` page, select an external crystal for HSE.
2. On the `ETH` page, configure the PHY mode as `RMII` and set the following parameters:
   1. Under the `Parameter Setting` tab, set `PHY Address` to `0` (determined by the PHYAD0 pin configuration).
   2. Under the `Advanced Parameter` tab, according to the LAN8720A datasheet, set `PHY special control/status register Offset` to `31`; `PHY Speed mask` to `0x0004`; `PHY Duplex mask` to `0x0010`.
3. On the `LWIP` page, enable and configure the following parameters:
   1. Under the `General Settings` tab, set `LWIP_DHCP (DHCP Module)` to `Disabled` (use static IP); configure `IP_ADDRESS` as `192.168.001.100`; `NETMASK_ADDRESS` as `255.255.255.000`; `GATEWAY_ADDRESS` as `192.168.001.001`; and enable `LWIP_UDP (UDP Module)` and `LWIP_TCP (TCP Module)`.

## References and Acknowledgments

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
