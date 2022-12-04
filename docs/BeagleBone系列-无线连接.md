---
id: BeagleBone系列-无线连接
title: BeagleBone 系列 - 无线连接
---

## 各版本 BeagleBone 的区别

| BeagleBone® Black | Seeed Studio BeagleBone® Green | Seeed Studio BeagleBone® Green Wireless       | Seeed Studio BeagleBone® Green Gateway                                 |
| ----------------- | ------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------- |
| $ 60.00 USD       | $ 44.00 USD                    | $ 52.90 USD                                   | $ 78.90 USD                                                            |
| 1 x USB Host      | 1 x USB Host                   | 4 x USB2.0 Host                               | 2 x USB2.0 Host                                                        |
| Ethernet          | Ethernet 10/100M               | Wi-Fi 802.11b/g/n 2.4GHz and Bluetooth 4.1 LE | Ethernet 10/100M Bit and Wi-Fi 802.11b/g/n 2.4GHz and Bluetooth 4.1 LE |
| HDMI Port         | 2 x Grove Connectors           | 2 x Grove Connectors                          | 2 x Grove Connectors                                                   |

## BeagleBone Green Gateway

### 连接 Wi-Fi

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
Passphrase? 输入密码
Connected wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> quit
```

### 连接蓝牙

```shell
sudo apt install bluez
```

如果有错误，就先更新一下：

```shell
sudo apt update
```

连接附近的蓝牙：

```shell
bb-wl18xx-bluetooth
bluetoothctl
scan on
```

配对连接设备（后面一串是要配对设备的 MAC 地址）：

```shell
pair A4:xx:xx:xx:xx:30
trust A4:xx:xx:xx:xx:30
connect A4:xx:xx:xx:xx:30
```

可使用 `quit` 推出蓝牙命令行。

## 参考与致谢

- [Seeed Studio BeagleBone® Green Gateway](https://wiki.seeedstudio.com/BeagleBone-Green-Gateway/)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

