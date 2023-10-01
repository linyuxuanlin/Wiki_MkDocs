# BeagleBone Series - Wireless Connectivity

## Differences between BeagleBone versions

| 版本 | CPU | 内存 | 存储 | 无线连接 |
| --- | --- | --- | --- | --- |
| BeagleBone Black | AM335x 1GHz ARM Cortex-A8 | 512MB DDR3 | 4GB eMMC | 无线 |
| BeagleBone Black Wireless | AM335x 1GHz ARM Cortex-A8 | 512MB DDR3 | 4GB eMMC | Wi-Fi + 蓝牙 |
| BeagleBone Green | AM335x 1GHz ARM Cortex-A8 | 512MB DDR3 | 4GB eMMC | 无线 |
| BeagleBone Green Wireless | AM335x 1GHz ARM Cortex-A8 | 512MB DDR3 | 4GB eMMC | Wi-Fi + 蓝牙 |
| BeagleBone AI | AM5729 1.5GHz ARM Cortex-A15 | 1GB DDR4 | 16GB eMMC | Wi-Fi + 蓝牙 |

## 无线连接

BeagleBone Black Wireless、BeagleBone Green Wireless 和 BeagleBone AI 都支持 Wi-Fi 和蓝牙连接。这使得它们可以更方便地与其他设备进行通信，例如智能手机、笔记本电脑和其他 IoT 设备。

### Wi-Fi 连接

要连接 Wi-Fi，需要使用适配器。BeagleBone Black Wireless 和 BeagleBone Green Wireless 都有内置的 Wi-Fi 适配器。对于 BeagleBone AI，需要使用 USB Wi-Fi 适配器。

要启用 Wi-Fi，需要在 BeagleBone 上运行以下命令：

```
sudo connmanctl
```

然后输入以下命令：

```
enable wifi
```

接下来，输入以下命令扫描可用的 Wi-Fi 网络：

```
scan wifi
```

最后，输入以下命令连接到所需的 Wi-Fi 网络：

```
agent on
connect wifi_XXX password_XXX
```

其中，XXX 是 Wi-Fi 网络的名称和密码。

### 蓝牙连接

要连接蓝牙，需要在 BeagleBone 上运行以下命令：

```
sudo bluetoothctl
```

然后输入以下命令扫描可用的蓝牙设备：

```
scan on
```

接下来，输入以下命令连接到所需的蓝牙设备：

```
connect XX:XX:XX:XX:XX:XX
```

其中，XX:XX:XX:XX:XX:XX 是蓝牙设备的 MAC 地址。

## 结论

BeagleBone Black Wireless、BeagleBone Green Wireless 和 BeagleBone AI 都支持 Wi-Fi 和蓝牙连接，使得它们可以更方便地与其他设备进行通信。要启用这些连接，需要在 BeagleBone 上运行一些命令。

| BeagleBone® Black | Seeed Studio BeagleBone® Green | Seeed Studio BeagleBone® Green Wireless       | Seeed Studio BeagleBone® Green Gateway                                 |
| ----------------- | ------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------- |
| $ 60.00 USD       | $ 44.00 USD                    | $ 52.90 USD                                   | $ 78.90 USD                                                            |
| 1 x USB Host      | 1 x USB Host                   | 4 x USB2.0 Host                               | 2 x USB2.0 Host                                                        |
| Ethernet          | Ethernet 10/100M               | Wi-Fi 802.11b/g/n 2.4GHz and Bluetooth 4.1 LE | Ethernet 10/100M Bit and Wi-Fi 802.11b/g/n 2.4GHz and Bluetooth 4.1 LE |
| HDMI Port         | 2 x Grove Connectors           | 2 x Grove Connectors                          | 2 x Grove Connectors                                                   |

The table above shows the specifications and prices of different BeagleBone® models offered by Seeed Studio. The BeagleBone® Black is priced at $60.00 USD and has 1 USB Host and Ethernet. The Seeed Studio BeagleBone® Green is priced at $44.00 USD and has 1 USB Host, Ethernet 10/100M, and 2 Grove Connectors. The Seeed Studio BeagleBone® Green Wireless is priced at $52.90 USD and has 4 USB2.0 Hosts, Wi-Fi 802.11b/g/n 2.4GHz, Bluetooth 4.1 LE, and 2 Grove Connectors. The Seeed Studio BeagleBone® Green Gateway is priced at $78.90 USD and has 2 USB2.0 Hosts, Ethernet 10/100M Bit, Wi-Fi 802.11b/g/n 2.4GHz, Bluetooth 4.1 LE, and 2 Grove Connectors.

## BeagleBone Green Gateway

### Connect to Wi-Fi

```shell
debian@beaglebone:~$ connmanctl
connmanctl> scan wifi
Scan completed for wifi
connmanctl> services
    se.101               wifi_1862e41aec0d_73652e313031_managed_psk
    STU-EE               wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> agent on
Agent registered
connmanctl> connect wifi_1862e41aec0d_5354552d4545_managed_psk
Agent RequestInput wifi_1862e41aec0d_5354552d4545_managed_psk
  Passphrase = [ Type=psk, Requirement=mandatory, Alternates=[ WPS ] ]
  WPS = [ Type=wpspin, Requirement=alternate ]
Passphrase? Enter password
Connected wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> quit
```

### Connect to Bluetooth

```shell
sudo apt install bluez
```

If there are errors, update first:

```shell
sudo apt update
```

Connect to nearby Bluetooth devices:

```shell
bb-wl18xx-bluetooth
bluetoothctl
scan on
```

Pair and connect to a device (the string of characters at the end is the MAC address of the device to be paired):

```shell
pair A4:xx:xx:xx:xx:30
trust A4:xx:xx:xx:xx:30
connect A4:xx:xx:xx:xx:30
```

Use `quit` to exit the Bluetooth command line.

## References and Acknowledgments

- [Seeed Studio BeagleBone® Green Gateway](https://wiki.seeedstudio.com/BeagleBone-Green-Gateway/)

The Seeed Studio BeagleBone® Green Gateway is a low-cost, open-source, and expandable platform for building IoT applications. It is based on the BeagleBone® Green and features a built-in Ethernet port, Wi-Fi, and Bluetooth connectivity. The Gateway also has a variety of interfaces, including USB, HDMI, and GPIO, making it easy to connect to a wide range of devices.

One of the key features of the BeagleBone® Green Gateway is its ability to act as a gateway between IoT devices and the cloud. It supports a variety of cloud platforms, including AWS IoT, Microsoft Azure IoT, and Google Cloud IoT, making it easy to connect to the cloud and manage your IoT devices.

The BeagleBone® Green Gateway is also highly customizable, with a variety of expansion boards available to add additional functionality. These expansion boards include sensors, relays, and other modules that can be used to build a wide range of IoT applications.

Overall, the Seeed Studio BeagleBone® Green Gateway is a powerful and flexible platform for building IoT applications. Its low cost, open-source design, and expandability make it an ideal choice for hobbyists, students, and professionals alike.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.