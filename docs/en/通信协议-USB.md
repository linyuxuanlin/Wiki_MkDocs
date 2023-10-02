# Communication Protocol - USB 🚧

## USB Versions

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094423.png)

## USB Mechanical Interface

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094855.png)

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094944.png)

Interface Definition - Standard USB:

| Pin  | Function              |
| ---- | ---------------------|
| 1    | VBUS (4.75-5.25 V)    |
| 2    | D-                    |
| 3    | D+                    |
| 4    | GND                   |

Interface Definition - Mini USB:

| Pin  | Function              | Color |
| ---- | ---------------------| ----- |
| 1    | VBUS (4.75-5.25 V)    | Red   |
| 2    | D-                    | White |
| 3    | D+                    | Green |
| 4    | ID                    |       |
| 5    | GND                   | Black |

## USB Plug and Version Compatibility

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211129094829.png)

---

## USB Type-C

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520105345.png)

### Port Types

Data:

- **Downstream Facing Port (DFP)**: Host/Downstream hub port. A typical example is the traditional standard Type-A port.
- **Upstream Facing Port (UFP)**: Device/Upstream hub port. A typical example is the traditional standard Type-B port.
- **Dual-Role Port (DRP)**: A port that switches between DFP and UFP ports before a connection event occurs. After the initial connection event, dynamic swapping can be negotiated through the USB Power Delivery protocol.

Power:

- **Pull-up Current Power/Power Supply Device**: The pull-up current is up to 5A when 5V-20V. A typical example is the traditional standard Type-A port.
- **Sink Current Power/Power Consumption Device**: The sink current is up to 5A when 5V-20V. A typical example is the traditional standard Type-B port.

## Pin Definitions

Type-C has male and female heads (plugs and sockets), and most of the pins are distributed in a mirrored manner.

Type-C Socket:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520134239.png)

Type-C Plug:

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520134304.png)

Docking Diagram (Full Functionality):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520140019.png)

Pin Definitions:

| Pin  | Name | Function          | Details                                           |
| ---- | ---- | ----------------- | ------------------------------------------------- |
| A1   | GND  | Power             | Minimum support 60W (used in conjunction with all VBUS) |
| A2   | TX1+ | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with TX1- |
| A3   | TX1- | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with TX1+ |
| A4   | VBUS | Power             | Minimum support 60W (used in conjunction with all VBUS) |
| A5   | CC1  | CC or VCONN       | Used for direction detection, current capability notification detection, and USB2.0 BMC communication |
| A6   | D+   | USB2.0            | -                                                 |
| A7   | D-   | USB2.0            | -                                                 |
| A8   | SBU1 | Alternate Mode    | Low-speed sideband signal, for use in Alternate Mode only |
| A9   | VBUS | Power             | Minimum support 60W (used in conjunction with all VBUS) |
| A10  | RX2- | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with RX2+ |
| A11  | RX2+ | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with RX2- |
| A12  | GND  | Power             | Minimum support 60W (used in conjunction with all VBUS) |
| B1   | GND  | Power             | Minimum support 60W (used in conjunction with all VBUS) |
| B2   | TX2+ | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with TX2- |
| B3   | TX2- | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with TX2+ |
| B4   | VBUS | Power             | Minimum support 60W (used in conjunction with all VBUS) |
| B5   | CC2  | CC or VCONN       | Used for direction detection, current capability notification detection, and USB2.0 BMC communication |
| B6   | D+   | USB2.0            | -                                                 |
| B7   | D-   | USB2.0            | -                                                 |
| B8   | SBU2 | Alternate Mode    | Low-speed sideband signal, for use in Alternate Mode only |
| B9   | VBUS | Power             | Minimum support 60W |
| B10  | RX1- | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with RX1+ |
| B11  | RX1+ | USB3.1 or Alternate Mode | Forms a 10 Gbps differential pair with RX1- |
| B12  | GND  | Power             | Minimum support 60W |

Power Supply Agreement:

| Mode                      | Nominal Voltage | Maximum Current |
| ------------------------- | -------------- | --------------- |
| USB2.0                    | 5V             | 500 mA          |
| USB3.0/USB3.1             | 5V             | 900 mA          |
| USB BC1.2                 | 5V             | 1.5A            |
| USB Type-C Current @ 1.5A | 5V             | 1.5A            |
| USB Type-C Current @ 2.0A | 5V             | 3.0A            |
| USB PD                    | Up to 20V      | Up to 5A        |

### CC Pin

The pull-up and pull-down resistors used on the CC pin depend on whether it is a downstream-facing port (DFP), upstream-facing port (UFP), or electronic marker/active cable. Port monitoring must always be used to achieve insertion and removal detection, direction detection, and current capability notification.

**Host/Downstream-Facing Port (DFP) uses pull-up resistors**. The pull-up resistor Rp must be connected to both CC1 and CC2 pins and pulled up to 3.3V/5V/current source. The value of the pull-up resistor will determine the device's power supply current capability through the port, as shown in the following table:

| DFP Power Supply Current Capability          | Pull-up to 4.75V~5.5V | Pull-up to 3.3V±5% | Pull-up to 1.7~5.5V current source |
| ------------------------------------------- | --------------------- | ------------------ | ---------------------------------- |
| Default USB Power (USB2.0-500mA, USB3.0-900mA) | 56kΩ±20%              | 36kΩ±20%           | 80µA±20%                           |
| 1.5A@5V                                     | 22kΩ±5%               | 12kΩ±5%            | 180µA±8%                           |
| 3A@5V                                       | 10kΩ±5%               | 4.7kΩ±5%           | 330µA±8%                           |

**Device/Upstream-Facing Port (UFP) uses pull-down resistors or voltage clamps**. The value of the pull-down resistor Rd is always 5.1kΩ±10%.

Cable direction detection: If CC1 detects a valid pull-up or pull-down, it represents the forward direction (not reversed); if CC1 detects the opposite, it represents the reverse direction (reversed):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20220520141738.png)

## References and Acknowledgments

- [Introduction to USB](https://blog.infonet.io/2020/03/21/USB%E7%9B%B8%E5%85%B3%E4%BB%8B%E7%BB%8D/)
- [USB](https://en.wikipedia.org/wiki/USB)
- [USB Logo Usage Guidelines](https://www.usb.org/sites/default/files/usb-if_logo_usage_guidelines_final_103019.pdf)
- [AN1953 | Introduction to USB Type-C™](http://www.microchip.com.cn/community/Uploads/Download/Library/00001953a_cn.pdf)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.