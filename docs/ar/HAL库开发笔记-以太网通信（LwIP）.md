# ملاحظات تطوير مكتبة HAL - اتصال الإيثرنت (LwIP) 🚧

فيما يلي بعض المعلومات المستمدة من [**لوحة تحكم معالج STM32F407 المعكوسة**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) و[**موديول PHY الإيثرنت DP83848**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## الأجهزة

واجهة DP83848 هي RMII، ويمكن لـ DP83848 دعم سرعات خطية 10M/100M، وتحتوي على مذبذب غير نشط بسرعة 50 ميجاهرتز.

| المعالج الرئيسي STM32 | موديول DP83848 |
| --------------------- | -------------- |
| ETH_REF_CLK           | PA1            |
| ETH_MDIO              | PA2            |
| ETH_MDC               | PC1            |
| ETH_CRS_DV            | PA7            |
| ETH_RXD0              | PC4            |
| ETH_RXD1              | PC5            |
| ETH_TX_EN             | PB11           |
| ETH_TXD0              | PB12           |
| ETH_TXD1              | PB13           |

## البرمجيات

### إعدادات داخل CubeMX

- RCC: اختر HSE كمذبذب خارجي
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN`, مدخل، مقاومة تأثير السحب إلى أعلى
  - PC13: `LED_GREEN`, مخرج بوش بول، مستوى عال
  - PC14: `LED_BLUE`, مخرج بوش بول، مستوى عال
  - PC15: `LED_RED`, مخرج بوش بول، مستوى عال
- ETH
  - الوضع: RMII
  - معلمات متقدمة
    - PHY: عنوان DP83848_PHY
- LWIP
  - خيارات مهمة
    - تحديد خيارات المعلمات المتقدمة
    - تأكد من أن LWIP_NETIF_LINK_CALLBACK مفعل (عادة مفعل بشكل افتراضي)
    - xLWIP_LOOPIF_MULTICAST: تم تفعيله
    - xLWIP_MULTICAST_TX_OPTIONS: تم تفعيله
    - xLWIP_NETIF_STATUS_CALLBACK: تم تفعيله
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: تم تفعيله
    - xLWIP_SO_RCVBUF: تم تفعيله
  - إعدادات عامة
    - xLWIP_IGMP: تم تفعيله

إعداد شجرة الساعة: وفقًا لمذبذب اللوحة (هذه اللوحة تحتوي على مذبذب 8 ميجاهرتز).

![الصورة](https://img.wiki-power.com/d/wiki-media/img/20220702145310.png)

### إضافة الشيفرة البرمجية

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */
```

/_ USER CODE BEGIN 0 _/
void ethernetif_notify_conn_changed(struct netif _netif) {
/_ ملحوظة: يمكن تنفيذ هذه الوظيفة في ملف المستخدم عند الحاجة إلى الاستدعاء. _/
if (netif_is_link_up(netif)) {
HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_RESET);
HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_SET);
} else {
HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_SET);
HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_RESET);
}
}
/_ USER CODE END 0 \*/

/_ USER CODE BEGIN 2 _/
ethernetif_notify_conn_changed(&gnetif);
/_ USER CODE END 2 _/

/_ USER CODE BEGIN 3 _/
MX_LWIP_Process();
}
/_ USER CODE END 3 _/

````

```c title="lwip.c"
/* USER CODE BEGIN 4_3 */
ethernetif_set_link(&gnetif);
if (netif_is_link_up(&gnetif) && !netif_is_up(&gnetif)) {
	netif_set_up(&gnetif);
	dhcp_start(&gnetif);
}
/* USER CODE END 4_3 */
````

## Debugging

- View devices connected to this computer's IP: `arp -a`
- Determine the STM32's IP address by plugging and unplugging
- `ping [ip address] (-t)`
- Hot-plugging the network cable may result in "Transmit Failed, Common Error," but it will automatically reconnect after a short wait.

## References and Acknowledgments

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

[to_be_replaced[1]]
[to_be_replaced[2]]

---

```
This article is based on the self-developed RobotCtrl development kit, with the STM32F407ZET6 microcontroller core and LAN8720A as the Ethernet PHY chip. For the schematic and detailed introduction, please see [**RobotCtrl - STM32 Universal Development Kit**[to_be_replaced[3]]RobotCtrl-STM32-Universal-Development-Kit).

LwIP is a lightweight IP protocol stack that can run with or without the support of an operating system. LwIP's focus is on reducing RAM usage while maintaining the core functionality of the TCP protocol. It can run with just over ten KB of RAM and around 40K of ROM, making it suitable for low-end embedded systems.

LwIP provides three programming interfaces: RAW/Callback API, NETCONN API, and SOCKETAPI. They vary in terms of ease of use and efficiency, with RAW API being the most efficient but less user-friendly. You can choose the API that best suits your development needs. In this article, we use the Raw API and call the following functions:
```

| API Function   | Description                                                         |
| -------------- | ------------------------------------------------------------------- |
| udp_new        | Create a new UDP PCB                                                |
| udp_remove     | Remove UDP PCB and release related resources                        |
| udp_bind       | Bind UDP PCB to local IP address and port                           |
| udp_connect    | Establish remote IP address and port for UDP PCB                    |
| udp_disconnect | Remove remote IP and port for UDP PCB                               |
| udp_send       | Send UDP data                                                       |
| udp_recv       | Register a callback function to be called when new data is received |

## Configuration in CubeMX

1. Select an external crystal oscillator for HSE on the `RCC` page.
2. Configure PHY mode as `RMII` on the `ETH` page, and set the following parameters:
   1. On the `Parameter Setting` tab, configure `PHY Address` to `0` (determined by the PHYAD0 pin).
   2. On the `Advanced Parameter` tab, following the LAN8720A datasheet, configure `PHY special control/status register Offset` to `31`; `PHY Speed mask` to `0x0004`; `PHY Duplex mask` to `0x0010`.
3. Enable LWIP on the `LWIP` page and set the following parameters:
   1. On the `General Settings` tab, set `LWIP_DHCP (DHCP Module)` to `Disabled` (use static IP); `IP_ADDRESS` to `192.168.001.100`; `NETMASK_ADDRESS` to `255.255.255.000`; `GATEWAY_ADDRESS` to `192.168.001.001`; `LWIP_UDP (UDP Module)` and `LWIP_TCP (TCP Module)` to `Enabled`.

## References and Acknowledgments

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> عنوان النص: <https://wiki-power.com/>
> يتم حماية هذا المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh)، يُرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
