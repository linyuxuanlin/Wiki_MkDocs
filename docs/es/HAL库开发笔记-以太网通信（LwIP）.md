# Notas de desarrollo de la biblioteca HAL - Comunicación Ethernet (LwIP) 🚧

A continuación, se presenta un tutorial basado en la [**tarjeta principal STM32F407 de Ersatz**](https://item.taobao.com/item.htm?spm=a230r.1.14.16.57314534365ZlN&id=569068950037&ns=1&abbucket=4#detail) y el [**módulo PHY Ethernet DP83848**](https://item.taobao.com/item.htm?spm=a230r.1.14.1.38df5bd3YTS6rE&id=12873819988&ns=1&abbucket=4#detail).

## Hardware

La interfaz DP83848 es RMII y admite velocidades de línea de 10M/100M, con un oscilador pasivo de 50MHz incorporado.

| STM32 Principal | Módulo DP83848 |
| --------------- | -------------- |
| ETH_REF_CLK     | PA1            |
| ETH_MDIO        | PA2            |
| ETH_MDC         | PC1            |
| ETH_CRS_DV      | PA7            |
| ETH_RXD0        | PC4            |
| ETH_RXD1        | PC5            |
| ETH_TX_EN       | PB11           |
| ETH_TXD0        | PB12           |
| ETH_TXD1        | PB13           |

## Software

### Configuración interna de CubeMX

- RCC: Seleccione HSE para el oscilador externo.
- SYS
  - DEBUG: SW
- GPIO
  - PA15: `USER_BTN`, Entrada, Pull-up
  - PC13: `LED_GREEN`, Salida Push Pull, nivel alto
  - PC14: `LED_BLUE`, Salida Push Pull, nivel alto
  - PC15: `LED_RED`, Salida Push Pull, nivel alto
- ETH
  - Modo: RMII
  - Parámetros avanzados
    - PHY: DP83848_PHY_ADDRESS
- LWIP
  - Opciones clave
    - Marque Mostrar parámetros avanzados
    - Asegúrese de que LWIP_NETIF_LINK_CALLBACK esté habilitado (generalmente está habilitado de forma predeterminada).
    - xLWIP_LOOPIF_MULTICAST: Habilitado
    - xLWIP_MULTICAST_TX_OPTIONS: Habilitado
    - xLWIP_NETIF_STATUS_CALLBACK: Habilitado
    - xLWIP_NETIF_EXT_STATUS_CALLBACK: Habilitado
    - xLWIP_SO_RCVBUF: Habilitado
  - Configuración general
    - xLWIP_IGMP: Habilitado

Configuración del árbol de reloj: de acuerdo con el oscilador incorporado en la placa (8M en este caso).

![Configuración del árbol de reloj](https://media.wiki-power.com/img/20220702145310.png)

### Agregar código de funcionalidad

```c title="main.c"
/* USER CODE BEGIN PV */
extern struct netif gnetif;
/* USER CODE END PV */
```

```c
void ethernetif_notify_conn_changed(struct netif *netif) {
	/* NOTA: Esta función puede ser implementada en un archivo de usuario
	 cuando se necesita la devolución de llamada.
	 */
	if (netif_is_link_up(netif)) {
		HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_RESET);
		HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_SET);
	} else {
		HAL_GPIO_WritePin(LED_GREEN_GPIO_Port, LED_GREEN_Pin, GPIO_PIN_SET);
		HAL_GPIO_WritePin(LED_RED_GPIO_Port, LED_RED_Pin, GPIO_PIN_RESET);
	}
}

ethernetif_notify_conn_changed(&gnetif);

MX_LWIP_Process();
```

```c title="lwip.c"
ethernetif_set_link(&gnetif);
if (netif_is_link_up(&gnetif) && !netif_is_up(&gnetif)) {
	netif_set_up(&gnetif);
	dhcp_start(&gnetif);
}
```

## Depuración

- Ver las direcciones IP de los dispositivos conectados a esta computadora: `arp -a`
- Determinar la dirección IP del STM32 mediante enchufar y desenchufar el cable de red.
- Realizar un ping a la dirección IP: `ping [dirección IP] (-t)`
- Cuando se desconecta y vuelve a conectar el cable de red, es posible que aparezca un mensaje de "Error de transferencia, problema común"; espere un momento y se restablecerá automáticamente la conexión.

## Referencias y Agradecimientos

- [Inicialización Ethernet HAL de STM32](https://blog.naver.com/eziya76/221852430347)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```

---

```

Este artículo se basa en el kit de desarrollo RobotCtrl de desarrollo propio, con un núcleo de microcontrolador STM32F407ZET6 y un chip PHY Ethernet LAN8720A. Para obtener el esquema y una descripción detallada, consulte [**RobotCtrl - STM32 通用开发套件**](https://wiki-power.com/RobotCtrl-STM32%E9%80%9A%E7%94%A8%E5%BC%80%E5%8F%91%E5%A5%97%E4%BB%B6).

LwIP es un protocolo IP ligero (Light Weight IP) que puede funcionar con o sin soporte de sistema operativo. El enfoque de LwIP es mantener las funciones principales del protocolo TCP mientras se reduce el uso de memoria RAM. Esta pila de protocolos LwIP puede funcionar con tan solo unos pocos KB de RAM y alrededor de 40 KB de ROM, lo que la hace adecuada para sistemas embebidos de gama baja.

LwIP proporciona tres interfaces de programación: RAW/Callback API, NETCONN API y SOCKET API. La facilidad de uso aumenta de izquierda a derecha, mientras que la eficiencia disminuye. Puede equilibrar estas consideraciones y elegir la API que mejor se adapte a su proyecto. En este artículo, se utiliza la API RAW, con las siguientes funciones:

```

| API Function  | Description                                  |
| -------------- | ---------------------------------------- |
| udp_new        | Crea un nuevo UDP PCB                         |
| udp_remove     | Elimina un UDP PCB y libera los recursos relacionados              |
| udp_bind       | Asocia el UDP PCB con una dirección IP local y un puerto         |
| udp_connect    | Establece una conexión remota para el UDP PCB con una dirección IP y un puerto          |
| udp_disconnect | Desconecta el UDP PCB de una dirección IP y un puerto remotos              |
| udp_send       | Envía datos UDP                            |
| udp_recv       | Registra una función de devolución de llamada para procesar los nuevos datagramas UDP recibidos |

## Configuración interna de CubeMX

1. En la página de `RCC`, selecciona un oscilador externo (HSE) para la fuente de reloj.
2. En la página de `ETH`, configura el modo PHY como `RMII`, y establece los siguientes parámetros:
   1. En la pestaña de `Parameter Setting`, configura la `Dirección PHY` como `0` (según la configuración del pin PHYAD0).
   2. En la pestaña de `Advanced Parameter`, según el manual del chip LAN8720A, configura `Desplazamiento de registro de control/estado especial PHY` como `31`; `Máscara de velocidad PHY` como `0x0004`; `Máscara de duplexación PHY` como `0x0010`.
3. En la página de `LWIP`, habilita la funcionalidad y configura los siguientes parámetros:
   1. En la pestaña de `General Settings`, configura `LWIP_DHCP (Módulo DHCP)` como `Desactivado` (usando una dirección IP estática); `IP_ADDRESS` como `192.168.001.100`; `NETMASK_ADDRESS` como `255.255.255.000`; `GATEWAY_ADDRESS` como `192.168.001.001`; `LWIP_UDP (Módulo UDP)` y `LWIP_TCP (Módulo TCP)` como `Habilitado`.

## Referencias y Agradecimientos

- [Demostración del stack TCP/IP LwIP para microcontroladores STM32F4x7 (AN3966)](https://www.st.com/en/embedded-software/stsw-stm32070.html)
- [Desarrollo de aplicaciones en STM32Cube con el stack TCP/IP LwIP (UM1713)](https://www.st.com/resource/en/user_manual/um1713-developing-applications-on-stm32cube-with-lwip-tcpip-stack-stmicroelectronics.pdf)
- [54zorb/stm32-lwip](https://github.com/54zorb/stm32-lwip)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
