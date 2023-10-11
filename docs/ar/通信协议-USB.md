# Protocolo de comunicación - USB 🚧

## Versiones de USB

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094423.png)

## Interfaz mecánica de USB

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094855.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094944.png)

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

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094829.png)

---

## USB Tipo-C

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520105345.png)

### Tipos de puertos

Datos:

- **Puerto de bajada (Downstream Facing Port, DFP)**: Puerto del host / concentrador descendente. Un ejemplo típico es el puerto estándar Type-A tradicional.
- **Puerto de subida (Upstream Facing Port, UFP)**: Puerto del dispositivo / concentrador ascendente. Un ejemplo típico es el puerto estándar Type-B tradicional.
- **Puerto de doble función (Dual-Role Port, DRP)**: Puerto que cambia entre el puerto DFP y el puerto UFP antes de que ocurra un evento de conexión. Después del evento de conexión inicial, se puede realizar un intercambio dinámico a través de la negociación del protocolo de suministro de energía USB.

Suministro de energía:

- **Fuente de corriente de tracción / dispositivo de suministro de energía**: La corriente de tracción máxima es de 5 A cuando se suministra energía de 5 V a 20 V. Un ejemplo típico es el puerto Type-A estándar tradicional.
- **Fuente de corriente de inundación / dispositivo de consumo de energía**: La corriente de inundación máxima es de 5 A cuando se suministra energía de 5 V a 20 V. Un ejemplo típico es el puerto Type-B estándar tradicional.

## Definición de pines

El Tipo-C tiene cabezales macho y hembra, y la mayoría de los pines están distribuidos en espejo.

Conector Tipo-C:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520134239.png)

Cabezal Tipo-C:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520134304.png)

Diagrama de conexión (función completa):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520140019.png)

Definición de pines:

| Pin | Nombre | Función                  | Detalles                                                                                             |
| --- | ------ | ------------------------ | ---------------------------------------------------------------------------------------------------- |
| A1  | GND    | Fuente de poder          | Soporta un mínimo de 60W (en combinación con VBUS)                                                   |
| A2  | TX1+   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con TX1-                                                         |
| A3  | TX1-   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con TX1+                                                         |
| A4  | VBUS   | Fuente de poder          | Soporta un mínimo de 60W (en combinación con VBUS)                                                   |
| A5  | CC1    | CC o VCONN               | Utilizado para detección de dirección, detección de capacidad de corriente y comunicación BMC USB2.0 |
| A6  | D+     | USB2.0                   | -                                                                                                    |
| A7  | D-     | USB2.0                   | -                                                                                                    |
| A8  | SBU1   | Modo de reserva          | Señal de banda lateral de baja velocidad, solo para uso en modo de reserva                           |
| A9  | VBUS   | Fuente de poder          | Soporta un mínimo de 60W (en combinación con VBUS)                                                   |
| A10 | RX2-   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con RX2+                                                         |
| A11 | RX2+   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con RX2-                                                         |
| A12 | GND    | Fuente de poder          | Soporta un mínimo de 60W (en combinación con VBUS)                                                   |
| B1  | GND    | Fuente de poder          | Soporta un mínimo de 60W (en combinación con VBUS)                                                   |
| B2  | TX2+   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con TX2-                                                         |
| B3  | TX2-   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con TX2+                                                         |
| B4  | VBUS   | Fuente de poder          | Soporta un mínimo de 60W (en combinación con VBUS)                                                   |
| B5  | CC2    | CC o VCONN               | Utilizado para detección de dirección, detección de capacidad de corriente y comunicación BMC USB2.0 |
| B6  | D+     | USB2.0                   | -                                                                                                    |
| B7  | D-     | USB2.0                   | -                                                                                                    |
| B8  | SBU2   | Modo de reserva          | Señal de banda lateral de baja velocidad, solo para uso en modo de reserva                           |
| B9  | VBUS   | Fuente de poder          | Soporta un mínimo de 60W                                                                             |
| B10 | RX1-   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con RX1+                                                         |
| B11 | RX1+   | USB3.1 o modo de reserva | Forma un par diferencial de 10 Gbps con RX1-                                                         |
| B12 | GND    | Fuente de poder          | Soporta un mínimo de 60W                                                                             |

Acuerdo de suministro de energía:

| Modo                        | Voltaje nominal | Corriente máxima |
| --------------------------- | --------------- | ---------------- |
| USB2.0                      | 5V              | 500 mA           |
| USB3.0/USB3.1               | 5V              | 900 mA           |
| USB BC1.2                   | 5V              | 1.5A             |
| USB Type-C Corriente @ 1.5A | 5V              | 1.5A             |
| USB Type-C Corriente @ 2.0A | 5V              | 3.0A             |
| USB PD                      | Máximo 20V      | Máximo 5A        |

### Pin CC

La resistencia de pull-up o pull-down utilizada en el pin CC depende de si es un puerto descendente (DFP), un puerto ascendente (UFP) o un cable activo / marcado electrónicamente, y siempre debe ser monitoreada a través del puerto para detectar la inserción y extracción, la detección de dirección y la capacidad de corriente.

**El host / puerto descendente (DFP) utiliza una resistencia de pull-up**. La resistencia de pull-up Rp debe estar conectada a los pines CC1 y CC2, y debe ser pull-up a 3.3V/5V/fuente de corriente. El valor de la resistencia de pull-up se ajustará a la capacidad de suministro de corriente del dispositivo a través del puerto, como se muestra en la siguiente tabla:

| Capacidad de suministro de corriente DFP                 | Pull-up a 4.75V~5.5V | Pull-up a 3.3V±5% | Fuente de corriente de 1.7~5.5V |
| -------------------------------------------------------- | -------------------- | ----------------- | ------------------------------- |
| Potencia USB predeterminada (USB2.0-500mA, USB3.0-900mA) | 56kΩ±20%             | 36kΩ±20%          | 80µA±20%                        |
| 1.5A@5V                                                  | 22kΩ±5%              | 12kΩ±5%           | 180µA±8%                        |
| 3A@5V                                                    | 10kΩ±5%              | 4.7kΩ±5%          | 330µA±8%                        |

**El dispositivo / puerto ascendente (UFP) utiliza una resistencia de pull-down o una abrazadera de voltaje**. El valor de la resistencia de pull-down Rd es constante y es de 5.1kΩ±10%.

La detección de la dirección del cable, si el pin CC1 detecta una resistencia de pull-up o pull-down válida, significa que está en la dirección correcta (no invertida); si CC1 no detecta nada, significa que está invertido:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520141738.png)

## Referencias y agradecimientos

- [Introducción a USB](https://blog.infonet.io/2020/03/21/USB%E7%9B%B8%E5%85%B3%E4%BB%8B%E7%BB%8D/)
- [USB](https://zh.wikipedia.org/wiki/USB)
- [Directrices para el uso del logotipo USB](https://www.usb.org/sites/default/files/usb-if_logo_usage_guidelines_final_103019.pdf)
- [AN1953 | Introducción a USB Type-C™](http://www.microchip.com.cn/community/Uploads/Download/Library/00001953a_cn.pdf)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
