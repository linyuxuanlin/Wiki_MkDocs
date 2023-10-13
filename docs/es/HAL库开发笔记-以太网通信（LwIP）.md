# Notas de desarrollo de la biblioteca HAL - Comunicación Ethernet (LwIP) 🚧

Este es un tutorial basado en la [**placa principal STM32F407 de Reka**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) y el [**módulo PHY Ethernet DP83848**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## Hardware

La interfaz DP83848 es RMII, y DP83848 admite una velocidad de línea de 10M/100M, con un oscilador pasivo de 50MHz integrado en la placa.

| Controlador principal STM32 | Módulo DP83848 |
| --------------------------- | -------------- |
| ETH_REF_CLK                 | PA1            |
| ETH_MDIO                    | PA2            |
| ETH_MDC                     | PC1            |
| ETH_CRS_DV                  | PA7            |
| ETH_RXD0                    | PC4            |
| ETH_RXD1                    | PC5            |
| ETH_TX_EN                   | PB11           |
| ETH_TXD0                    | PB12           |
| ETH_TXD1                    | PB13           |

## Software

### Configuración interna de CubeMX

- RCC: seleccione HSE como oscilador externo.
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN`, entrada, pull-up
  - PC13: `LED_GREEN`, salida push-pull, nivel alto
  - PC14: `LED_BLUE`, salida push-pull, nivel alto
  - PC15: `LED_RED`, salida push-pull, nivel alto
- ETH
  - Modo: RMII
  - Parámetros avanzados
    - PHY: DP83848_PHY_ADDRESS
- LWIP
  - Opciones clave
    - Seleccione Mostrar parámetros avanzados.
    - Asegúrese de que LWIP_NETIF_LINK_CALLBACK esté habilitado (generalmente de forma predeterminada).
    - xLWIP_LOOPIF_MULTICAST: habilitado
    - xLWIP_MULTICAST_TX_OPTIONS: habilitado
    - xLWIP_NETIF_STATUS_CALLBACK: habilitado
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: habilitado
    - xLWIP_SO_RCVBUF: habilitado
  - Configuración general
    - xLWIP_IGMP: habilitado

Configuración del árbol de reloj: configure según el oscilador integrado en la placa (8M en este caso).

![](https://img.wiki-power.com/d/wiki-media/img/20220702145310.png)

### Agregar código de funcionalidad

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */
```

# Implementación de Ethernet en STM32 con LwIP

En este artículo, se describe cómo implementar Ethernet en un microcontrolador STM32 utilizando el protocolo LwIP. Se utiliza la API RAW para la implementación.

## Configuración de hardware

Para la implementación de Ethernet en STM32, se utiliza el chip PHY LAN8720A. La configuración de hardware se puede encontrar en el siguiente enlace: [RobotCtrl - STM32 通用开发套件](https://wiki-power.com/es/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

## Configuración de software

Para la configuración de software, se utiliza el protocolo LwIP. Se utiliza la API RAW para la implementación. A continuación, se muestra el código utilizado para la notificación de cambios de conexión:

```c
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

A continuación, se muestra el código utilizado para la configuración de Ethernet:

```c
/* USER CODE BEGIN 4_3 */
ethernetif_set_link(&gnetif);
if (netif_is_link_up(&gnetif) && !netif_is_up(&gnetif)) {
	netif_set_up(&gnetif);
	dhcp_start(&gnetif);
}
/* USER CODE END 4_3 */
```

## Depuración

- Verifique la dirección IP de los dispositivos conectados a la computadora: `arp -a`
- Determine la dirección IP de STM32 conectando y desconectando el cable de red.
- Realice un ping a la dirección IP: `ping [dirección IP] (-t)`
- Si se produce un error de "falla en la transmisión", espere un momento y se restablecerá automáticamente la conexión.

## Referencias y agradecimientos

- [STM32 HAL Ethernet initialization](https://blog.naver.com/eziya76/221852430347)

| Función de API | Descripción                                                                                    |
| -------------- | ---------------------------------------------------------------------------------------------- |
| udp_new        | Crea un nuevo PCB UDP                                                                          |
| udp_remove     | Elimina el PCB UDP y libera los recursos relacionados                                          |
| udp_bind       | Asocia el PCB UDP con la dirección IP y el puerto local                                        |
| udp_connect    | Establece la dirección IP y el puerto remoto del PCB UDP                                       |
| udp_disconnect | Elimina la dirección IP y el puerto remoto del PCB UDP                                         |
| udp_send       | Envía datos UDP                                                                                |
| udp_recv       | Registra una función de devolución de llamada que se llama cuando se recibe un nuevo datagrama |

## Configuración interna de CubeMX

1. En la página `RCC`, seleccione un cristal externo para HSE.
2. En la página `ETH`, configure el modo PHY como `RMII` y configure los siguientes parámetros:
   1. En la pestaña `Parameter Setting`, configure `PHY Address` como `0` (según la configuración de los pines PHYAD0).
   2. En la pestaña `Advanced Parameter`, según el manual del chip LAN8720A, configure `PHY special control/status register Offset` como `31`; `PHY Speed mask` como `0x0004`; `PHY Duplex mask` como `0x0010`.
3. En la página `LWIP`, habilite y configure los siguientes parámetros:
   1. En la pestaña `General Settings`, configure `LWIP_DHCP (DHCP Module)` como `Disabled` (use una dirección IP estática); `IP_ADDRESS` como `192.168.001.100`; `NETMASK_ADDRESS` como `255.255.255.000`; `GATEWAY_ADDRESS` como `192.168.001.001`; `LWIP_UDP (UDP Module)` y `LWIP_TCP (TCP Module)` como `Enabled`.

## Referencias y agradecimientos

- [Demostración de la pila TCP/IP LwIP para microcontroladores STM32F4x7 (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Desarrollo de aplicaciones en STM32Cube con la pila TCP/IP LwIP (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> Autor del artículo: **Power Lin**
> Dirección original: <https://wiki-power.com>
> Declaración de derechos de autor: Este artículo utiliza la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si reproduce este artículo, indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
