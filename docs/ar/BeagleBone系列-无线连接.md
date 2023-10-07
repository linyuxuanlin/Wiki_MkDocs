# Serie BeagleBone - Conexión inalámbrica

## Diferencias entre las diferentes versiones de BeagleBone

| BeagleBone® Black | Seeed Studio BeagleBone® Green | Seeed Studio BeagleBone® Green Wireless       | Seeed Studio BeagleBone® Green Gateway                                 |
| ----------------- | ------------------------------ | --------------------------------------------- | ---------------------------------------------------------------------- |
| $ 60.00 USD       | $ 44.00 USD                    | $ 52.90 USD                                   | $ 78.90 USD                                                            |
| 1 x USB Host      | 1 x USB Host                   | 4 x USB2.0 Host                               | 2 x USB2.0 Host                                                        |
| Ethernet          | Ethernet 10/100M               | Wi-Fi 802.11b/g/n 2.4GHz y Bluetooth 4.1 LE    | Ethernet 10/100M Bit y Wi-Fi 802.11b/g/n 2.4GHz y Bluetooth 4.1 LE      |
| Puerto HDMI       | 2 x conectores Grove           | 2 x conectores Grove                          | 2 x conectores Grove                                                   |

## BeagleBone Green Gateway

### Conexión Wi-Fi

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
Passphrase? Ingrese la contraseña
Connected wifi_1862e41aec0d_5354552d4545_managed_psk
connmanctl> quit
```

### Conexión Bluetooth

```shell
sudo apt install bluez
```

Si hay algún error, actualice primero:

```shell
sudo apt update
```

Conecte el dispositivo Bluetooth cercano:

```shell
bb-wl18xx-bluetooth
bluetoothctl
scan on
```

Empareje y conecte el dispositivo (la cadena posterior es la dirección MAC del dispositivo a emparejar):

```shell
pair A4:xx:xx:xx:xx:30
trust A4:xx:xx:xx:xx:30
connect A4:xx:xx:xx:xx:30
```

Puede usar `quit` para salir del terminal de Bluetooth.

## Referencias y agradecimientos

- [Seeed Studio BeagleBone® Green Gateway](https://wiki.seeedstudio.com/BeagleBone-Green-Gateway/)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.