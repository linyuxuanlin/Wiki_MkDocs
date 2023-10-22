# Notas de desarrollo de la biblioteca HAL - Comunicación Ethernet (LwIP) 🚧

A continuación se presenta un tutorial basado en la [**placa base principal STM32F407**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) y el [**módulo PHY Ethernet DP83848**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## Hardware

El módulo DP83848 utiliza la interfaz RMII y es compatible con velocidades de línea de 10M/100M. También cuenta con un oscilador pasivo de 50MHz en la placa.

| STM32 Main Control | Módulo DP83848 |
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

### Configuración interna de CubeMX

- RCC: Seleccionar HSE para el oscilador externo.
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN`, Entrada, Pull-up
  - PC13: `LED_GREEN`, Salida Push Pull, nivel Alto
  - PC14: `LED_BLUE`, Salida Push Pull, nivel Alto
  - PC15: `LED_RED`, Salida Push Pull, nivel Alto
- ETH
  - Modo: RMII
  - Parámetros avanzados
    - PHY: DP83848_PHY_ADDRESS
- LWIP
  - Opciones clave
    - Marcar Mostrar parámetros avanzados
    - Asegurarse de que LWIP_NETIF_LINK_CALLBACK esté habilitado (generalmente habilitado de forma predeterminada)
    - xLWIP_LOOPIF_MULTICAST: Habilitado
    - xLWIP_MULTICAST_TX_OPTIONS: Habilitado
    - xLWIP_NETIF_STATUS_CALLBACK: Habilitado
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: Habilitado
    - xLWIP_SO_RCVBUF: Habilitado
  - Configuración general
    - xLWIP_IGMP: Habilitado

Configuración del árbol de reloj: según el oscilador a bordo (en este caso, 8M).

![Configuración del árbol de reloj](https://img.wiki-power.com/d/wiki-media/img/20220702145310.png)

### Agregar código de funcionalidad

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */
```

```c
/* USER CODE BEGIN 0 */
void ethernetif_notify_conn_changed(struct netif *netif) {
	/* NOTA: Esta función puede implementarse en un archivo de usuario
	   cuando sea necesario el callback.
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

## Depuración

- Para ver las IP de los dispositivos conectados a esta computadora: `arp -a`
- Determinar la dirección IP del STM32 conectando y desconectando el cable de red.
- Hacer ping a la dirección IP: `ping [dirección IP] (-t)`
- Si se desconecta y vuelve a conectar el cable de red, puede mostrar "Fallo en la transmisión, error común", pero pronto se restablecerá automáticamente la conexión.

## Referencias y Agradecimientos

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

---

```
Este artículo se basa en el kit de desarrollo RobotCtrl desarrollado internamente, con un núcleo de microcontrolador STM32F407ZET6 y un chip PHY Ethernet LAN8720A. Para obtener el esquema y una descripción detallada, consulte [**RobotCtrl - Kit de Desarrollo Universal STM32**](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

LwIP es un protocolo IP ligero que puede funcionar sin importar si hay soporte para un sistema operativo. El enfoque de LwIP está en mantener las funciones principales del protocolo TCP y minimizar la utilización de RAM. Puede ejecutarse con tan solo unos pocos KB de RAM y alrededor de 40 KB de ROM, lo que lo hace adecuado para sistemas integrados de gama baja.

LwIP proporciona tres interfaces de programación: RAW/Callback API, NETCONN API y SOCKET API. Aumentan en facilidad de uso de izquierda a derecha, pero disminuyen en eficiencia de ejecución. Puede equilibrar las ventajas y desventajas y elegir la API que mejor se adapte a sus necesidades de desarrollo. En este artículo, se utiliza la API Raw, llamando a las siguientes funciones:
```

```markdown
| API Function  | Description                                 |
| ------------- | ------------------------------------------- |
| udp_new       | Create a new UDP PCB                        |
| udp_remove    | Remove UDP PCB and release related resources |
| udp_bind      | Bind UDP PCB to a local IP address and port |
| udp_connect   | Establish remote IP address and port for UDP PCB |
| udp_disconnect | Remove remote IP and port for UDP PCB        |
| udp_send      | Send UDP data                               |
| udp_recv      | Register a callback function to be called when new data is received |

## Configuration in CubeMX

1. In the `RCC` page, select an external crystal for HSE.
2. In the `ETH` page, configure the PHY mode as `RMII` and set the following parameters:
   1. On the `Parameter Setting` tab, set `PHY Address` to `0` (based on PHYAD0 pin configuration).
   2. On the `Advanced Parameter` tab, based on the LAN8720A datasheet, set `PHY special control/status register Offset` to `31`, `PHY Speed mask` to `0x0004`, and `PHY Duplex mask` to `0x0010`.
3. In the `LWIP` page, enable and configure the following parameters:
   1. On the `General Settings` tab, set `LWIP_DHCP (DHCP Module)` to `Disabled` (use static IP), `IP_ADDRESS` to `192.168.001.100`, `NETMASK_ADDRESS` to `255.255.255.000`, `GATEWAY_ADDRESS` to `192.168.001.001`, and enable `LWIP_UDP (UDP Module)` and `LWIP_TCP (TCP Module)`.

## References and Acknowledgments

- [LwIP TCP/IP stack demonstration for STM32F4x7 microcontrollers (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Developing applications on STM32Cube with LwIP TCP/IP stack (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> Article by: **Power Lin**
> Original Source: [https://wiki-power.com](https://wiki-power.com)
> Copyright Statement: This article is licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Please provide proper attribution when reposting.
```


> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.