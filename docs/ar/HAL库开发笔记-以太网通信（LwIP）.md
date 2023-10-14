# مذكرات تطوير مكتبة HAL - Ethernet Communication (LwIP) 🚧

هذا هو دليل استنادًا إلى [** لوحة المفاتيح الرئيسية STM32F407 المعكوسة **] (https://item.taobao.com/item.htm؟spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) و [** DP83848 وحدة PHY Ethernet **] (https://item.taobao.com/item.htm؟spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## الأجهزة

واجهة DP83848 هي RMII ، ويمكن لـ DP83848 دعم سرعة الخط 10M / 100M ، ويوجد على اللوحة مذبذب غير نشط بسرعة 50 ميجا هرتز.

| STM32 المراقب الرئيسي | وحدة DP83848 PHY |
| --------------------- | ---------------- |
| ETH_REF_CLK           | PA1              |
| ETH_MDIO              | PA2              |
| ETH_MDC               | PC1              |
| ETH_CRS_DV            | PA7              |
| ETH_RXD0              | PC4              |
| ETH_RXD1              | PC5              |
| ETH_TX_EN             | PB11             |
| ETH_TXD0              | PB12             |
| ETH_TXD1              | PB13             |

## البرمجيات

### التكوين الداخلي لـ CubeMX

- RCC: HSE يختار المذبذب الخارجي
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN` ، Input ، Pull-up
  - PC13: `LED_GREEN` ، Output Push Pull ، level High
  - PC14: `LED_BLUE` ، Output Push Pull ، level High
  - PC15: `LED_RED` ، Output Push Pull ، level High
- ETH
  - Mode: RMII
  - Advanced Parameters
    - PHY: DP83848_PHY_ADDRESS
- LWIP
  - Key Options
    - تحقق من Show Advanced Parameters
    - تأكد من أن LWIP_NETIF_LINK_CALLBACK هو Enable (عادة ما يكون الافتراضي)
    - xLWIP_LOOPIF_MULTICAST: تمكين
    - xLWIP_MULTICAST_TX_OPTIONS: تمكين
    - xLWIP_NETIF_STATUS_CALLBACK: تمكين
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: تمكين
    - xLWIP_SO_RCVBUF: تمكين
  - Genetal Settings
    - xLWIP_IGMP: تمكين

تكوين شجرة الساعة: تكوينها وفقًا للمذبذب المدمج (8 ميجا هرتز في هذا اللوحة).

![](https://img.wiki-power.com/d/wiki-media/img/20220702145310.png)

### إضافة رمز الوظيفة

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */

/* USER CODE BEGIN 0 */
void ethernetif_notify_conn_changed(struct netif *netif) {
	/* ملاحظة: يمكن تنفيذ هذه الوظيفة في ملف المستخدم عند الحاجة إلى الاستدعاء العائد */
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

## تصحيح الأخطاء

- عرض عناوين IP للأجهزة المتصلة بالكمبيوتر الحالي: `arp -a`
- تحديد عنوان IP لـ STM32 عن طريق الإدخال والإخراج
- `ping [عنوان IP] (-t)`
- سيتم إعادة الاتصال تلقائيًا بعد قليل من الوقت عند فصل الكابل.

## المراجع والشكر

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

| API الدالة     | الوصف                                                     |
| -------------- | --------------------------------------------------------- |
| udp_new        | إنشاء PCB UDP جديد                                        |
| udp_remove     | إزالة PCB UDP وتحرير الموارد ذات الصلة                    |
| udp_bind       | PCB UDP مرتبط بعنوان IP المحلي والمنفذ                    |
| udp_connect    | إنشاء PCB UDP عن بعد عنوان IP ومنفذ                       |
| udp_disconnect | إزالة PCB UDP عن بعد عنوان IP ومنفذ                       |
| udp_send       | إرسال بيانات UDP                                          |
| udp_recv       | تسجيل دالة الاستدعاء العائدة عند استلام حزمة بيانات جديدة |

## تكوين داخل CubeMX

1. في صفحة `RCC` ، حدد المذبذب الخارجي لـ HSE.
2. في صفحة `ETH` ، قم بتكوين وضع PHY كـ `RMII` ، وقم بتكوين المعلمات التالية:
   1. في علامة التبويب `Parameter Setting` ، قم بتكوين `عنوان PHY` إلى `0` (وفقًا لتكوين دبوس PHYAD0).
   2. في علامة التبويب `Advanced Parameter` ، وفقًا لكتيب شرائح LAN8720A ، قم بتكوين `PHY special control/status register Offset` إلى `31` ؛ `PHY Speed mask` إلى `0x0004` ؛ `PHY Duplex mask` إلى `0x0010`.
3. في صفحة `LWIP` ، قم بتمكينها وتكوين المعلمات التالية:
   1. في علامة التبويب `General Settings` ، قم بتكوين `LWIP_DHCP (DHCP Module)` إلى `Disabled` (استخدام عنوان IP ثابت) ؛ `IP_ADDRESS` إلى `192.168.001.100` ؛ `NETMASK_ADDRESS` إلى `255.255.255.000` ؛ `GATEWAY_ADDRESS` إلى `192.168.001.001` ؛ `LWIP_UDP (UDP Module)` و `LWIP_TCP (TCP Module)` إلى `Enabled`.

## المراجع والشكر

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> مؤلف المقال: **Power Lin**
> العنوان الأصلي: <https://wiki-power.com>
> إعلان حقوق النشر: يتم استخدام المقال بموجب اتفاقية [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) ، يرجى ذكر المصدر عند إعادة النشر.

> تمت ترجمة هذه المشاركة باستخدام ChatGPT، يرجى [**تزويدنا بتعليقاتكم**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) إذا كانت هناك أي حذف أو إهمال.
