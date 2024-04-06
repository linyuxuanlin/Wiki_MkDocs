# Protocolo de comunicación - USB 🚧

## Versiones de USB

![](https://media.wiki-power.com/img/20211129094423.png)

## Interfaz mecánica de USB

![](https://media.wiki-power.com/img/20211129094855.png)

![](https://media.wiki-power.com/img/20211129094944.png)

Definición de la interfaz - USB estándar:

| Pin | Función            |
| --- | ------------------ |
| 1   | VBUS (4.75-5.25 V) |
| 2   | D-                 |
| 3   | D+                 |
| 4   | GND                |

Definición de la interfaz - Mini USB:

| Pin | Función            | Color  |
| --- | ------------------ | ------ |
| 1   | VBUS (4.75-5.25 V) | Rojo   |
| 2   | D-                 | Blanco |
| 3   | D+                 | Verde  |
| 4   | ID                 |        |
| 5   | GND                | Negro  |

## Compatibilidad entre conectores USB y versiones

![](https://media.wiki-power.com/img/20211129094829.png)

---

## USB Tipo-C

![](https://media.wiki-power.com/img/20220520105345.png)

### Tipos de puertos

Datos:

- **Puerto de bajada (Downstream Facing Port, DFP)**: Puerto del host / concentrador de bajada. Un ejemplo típico es el puerto estándar Type-A tradicional.
- **Puerto de subida (Upstream Facing Port, UFP)**: Puerto del dispositivo / concentrador de subida. Un ejemplo típico es el puerto estándar Type-B tradicional.
- **Puerto de doble función (Dual-Role Port, DRP)**: Puerto que cambia entre el puerto DFP y el puerto UFP antes de que ocurra un evento de conexión. Después del evento de conexión inicial, se puede realizar un intercambio dinámico mediante la negociación del protocolo de suministro de energía USB.

Alimentación:

- **Fuente de corriente de tracción / Dispositivo de alimentación**: La corriente de tracción puede ser de hasta 5A con voltajes de 5V a 20V. Un ejemplo típico es el puerto estándar Type-A tradicional.
- **Fuente de corriente de suministro / Dispositivo de consumo**: La corriente de suministro puede ser de hasta 5A con voltajes de 5V a 20V. Un ejemplo típico es el puerto estándar Type-B tradicional.

## Definición de pines

El conector Type-C tiene una versión macho (conector) y una versión hembra (zócalo), y la mayoría de los pines están distribuidos de manera simétrica.

Zócalo Type-C:

![](https://media.wiki-power.com/img/20220520134239.png)

Conector Type-C:

![](https://media.wiki-power.com/img/20220520134304.png)

Diagrama de conexión (funcionalidad completa):

![](https://media.wiki-power.com/img/20220520140019.png)

Definición de pines:

| Pin | Nombre | Función           | Detalles                                                                                |
| --- | ------ | ----------------- | --------------------------------------------------------------------------------------- |
| A1  | GND    | Alimentación      | Mínimo soporte de 60W (en combinación con VBUS)                                         |
| A2  | TX1+   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con TX1-                                            |
| A3  | TX1-   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con TX1+                                            |
| A4  | VBUS   | Alimentación      | Mínimo soporte de 60W (en combinación con VBUS)                                         |
| A5  | CC1    | CC o VCONN        | Utilizado para detección de dirección, capacidad de corriente y comunicación BMC USB2.0 |
| A6  | D+     | USB2.0            | —                                                                                       |
| A7  | D-     | USB2.0            | —                                                                                       |
| A8  | SBU1   | Modo Alt          | Señal de banda lateral de baja velocidad, solo para uso en Modo Alt                     |
| A9  | VBUS   | Alimentación      | Mínimo soporte de 60W (en combinación con VBUS)                                         |
| A10 | RX2-   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con RX2+                                            |
| A11 | RX2+   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con RX2-                                            |
| A12 | GND    | Alimentación      | Mínimo soporte de 60W (en combinación con VBUS)                                         |
| B1  | GND    | Alimentación      | Mínimo soporte de 60W (en combinación con VBUS)                                         |
| B2  | TX2+   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con TX2-                                            |
| B3  | TX2-   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con TX2+                                            |
| B4  | VBUS   | Alimentación      | Mínimo soporte de 60W (en combinación con VBUS)                                         |
| B5  | CC2    | CC o VCONN        | Utilizado para detección de dirección, capacidad de corriente y comunicación BMC USB2.0 |
| B6  | D+     | USB2.0            | —                                                                                       |
| B7  | D-     | USB2.0            | —                                                                                       |
| B8  | SBU2   | Modo Alt          | Señal de banda lateral de baja velocidad, solo para uso en Modo Alt                     |
| B9  | VBUS   | Alimentación      | Mínimo soporte de 60W                                                                   |
| B10 | RX1-   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con RX1+                                            |
| B11 | RX1+   | USB3.1 o Modo Alt | Forma un par diferencial de 10 Gbps con RX1-                                            |
| B12 | GND    | Alimentación      | Mínimo soporte de 60W                                                                   |

Acuerdo de suministro de energía:

| Modo                      | Voltaje nominal | Corriente máxima |
| ------------------------- | --------------- | ---------------- |
| USB2.0                    | 5V              | 500 mA           |
| USB3.0/USB3.1             | 5V              | 900 mA           |
| USB BC1.2                 | 5V              | 1.5A             |
| USB Type-C Current @ 1.5A | 5V              | 1.5A             |
| USB Type-C Current @ 2.0A | 5V              | 3.0A             |
| USB PD                    | Hasta 20V       | Hasta 5A         |

### Pines CC

La resistencia de pull-up o pull-down utilizada en los pines CC depende de si es un puerto descendente (DFP), un puerto ascendente (UFP) o un cable de marcado electrónico/activo. Siempre se debe realizar un monitoreo del puerto para lograr la detección de inserción y extracción, la detección de dirección y la notificación de capacidad de corriente.

**El host / puerto descendente (DFP) utiliza resistencias de pull-up**. La resistencia de pull-up Rp debe estar conectada a los pines CC1 y CC2, y se debe tirar hacia arriba a 3.3V/5V/fuente de corriente. El valor de la resistencia de pull-up determinará la capacidad de corriente suministrada por el dispositivo a través del puerto, como se muestra en la siguiente tabla:

| Capacidad de corriente suministrada por DFP              | Tirar hacia 4.75V~5.5V | Tirar hacia 3.3V±5% | Tirar hacia 1.7~5.5V fuente de corriente |
| -------------------------------------------------------- | ---------------------- | ------------------- | ---------------------------------------- |
| Potencia USB predeterminada (USB2.0-500mA, USB3.0-900mA) | 56kΩ±20%               | 36kΩ±20%            | 80µA±20%                                 |
| 1.5A@5V                                                  | 22kΩ±5%                | 12kΩ±5%             | 180µA±8%                                 |
| 3A@5V                                                    | 10kΩ±5%                | 4.7kΩ±5%            | 330µA±8%                                 |

**El dispositivo / puerto ascendente (UFP) utiliza resistencias de pull-down o terminación de voltaje**. El valor de la resistencia de pull-down Rd es siempre de 5.1kΩ±10%.

La detección de la dirección del cable se realiza mediante la detección de pull-up o pull-down en el pin CC1. Si se detecta una resistencia de pull-up o pull-down válida, significa que está en la dirección correcta (sin invertir). Si no se detecta ninguna resistencia, significa que está en la dirección inversa (invertido):

![](https://media.wiki-power.com/img/20220520141738.png)

## Referencias y agradecimientos

- [Introducción a USB](https://blog.infonet.io/2020/03/21/USB%E7%9B%B8%E5%85%B3%E4%BB%8B%E7%BB%8D/)
- [USB](https://zh.wikipedia.org/wiki/USB)
- [Directrices de uso del logotipo USB](https://www.usb.org/sites/default/files/usb-if_logo_usage_guidelines_final_103019.pdf)
- [AN1953 | Introducción a USB Type-C™](http://www.microchip.com.cn/community/Uploads/Download/Library/00001953a_cn.pdf)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
