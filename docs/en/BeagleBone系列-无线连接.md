# BeagleBone Series - Wireless Connectivity

## Differences between BeagleBone Versions

| BeagleBone® Black | Seeed Studio BeagleBone® Green | Seeed Studio BeagleBone® Green Wireless | Seeed Studio BeagleBone® Green Gateway |
| ----------------- | ------------------------------ | ------------------------------------- | ----------------------------------- |
| $60.00 USD        | $44.00 USD                     | $52.90 USD                           | $78.90 USD                          |
| 1 x USB Host      | 1 x USB Host                    | 4 x USB2.0 Host                       | 2 x USB2.0 Host                     |
| Ethernet          | Ethernet 10/100M                | Wi-Fi 802.11b/g/n 2.4GHz and Bluetooth 4.1 LE | Ethernet 10/100M Bit and Wi-Fi 802.11b/g/n 2.4GHz and Bluetooth 4.1 LE |
| HDMI Port         | 2 x Grove Connectors            | 2 x Grove Connectors                   | 2 x Grove Connectors                 |

## BeagleBone Green Gateway

### Connecting to Wi-Fi

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
Passphrase? Enter the password
Connected to wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> quit
```

### Connecting to Bluetooth

```shell
# Install Bluez with superuser privileges
sudo apt install bluez

# If you encounter any errors, start by updating the package list
sudo apt update

# Discover nearby Bluetooth devices
bb-wl18xx-bluetooth
bluetoothctl
scan on

# Pair and connect to a specific device (replace the MAC address with the target device's address)
pair A4:xx:xx:xx:xx:30
trust A4:xx:xx:xx:xx:30
connect A4:xx:xx:xx:xx:30

# You can exit the Bluetooth command line using 'quit'.

## References and Acknowledgments

- [Seeed Studio BeagleBone® Green Gateway](https://wiki.seeedstudio.com/BeagleBone-Green-Gateway/)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.
```

Please note that this translation maintains the original markdown format while ensuring that the content is both colloquial and professionally presented.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.