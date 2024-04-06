# BeagleBone Series - Basic Parameters and Environment Configuration

## Hardware Resources

![Imagen](https://media.wiki-power.com/img/20211008090724.png)

- USB Tipo-A: Utilizado en modo Host USB
- USB Micro: Para alimentar la placa y como dispositivo esclavo
- LEDs
  - D2: Parpadea como un latido al arrancar
  - D3: Se enciende al leer/escribir datos en la tarjeta SD
  - D4: Se enciende cuando la CPU está activa
  - D5: Se enciende cuando se leen/escriben datos en la memoria eMMC
- Botones de Inicio/Usuario: Independientemente de si se presionan o no, si hay una tarjeta SD, se iniciará desde la tarjeta SD de manera predeterminada (dos caminos que llevan al mismo lugar). Después del arranque, funcionan como botones normales conectados a GPIO_72.
- Interfaz Grove I2C: Conectada a I2C2
- Interfaz Grove UART: Conectada a UART2
- Depuración Serial: Conectada a UART0, el pin 1 está cerca del USB, y del pin 1 al pin 6 se corresponden con: GND, NC, NC, RX, TX, NC

## Environment Configuration

### Driver Installation Issue

On Windows 10 and newer versions, driver installations may fail due to driver signature enforcement.

Solution:

- Hold down the `Shift` key and click on "Restart" on your computer.
- Go to "Troubleshoot" - "Advanced options" - "Startup Settings" and click "Restart."
- After the restart, follow the on-screen instructions, and press the `7` key on your keyboard to disable driver signature enforcement.
- Upon booting, you should be able to install BeagleBone's driver software without any issues.

### Image Download and Flashing

Official image download link: [https://beagleboard.org/latest-images](https://beagleboard.org/latest-images)  
Flashing tool: [https://sourceforge.net/projects/win32diskimager/files/latest/download](https://sourceforge.net/projects/win32diskimager/files/latest/download)

Burn the image onto an SD card, power down, insert it into BeagleBone, and the system will boot from the SD card upon the next power-up.

## Access Using Command-Line Tools

### Access via Serial Port

Connect the onboard serial terminal using a USB-to-serial adapter and open a serial terminal tool on your computer (e.g., WindTerm). The initial username and password are both `root`.

The baud rate is 115200!

### Access via Ethernet

Within the serial connection, use the `ifconfig` command to find the Ethernet address for connection. The username is `debian`, and the password is `temppwd`.

### Access via USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

Access using SSH. The username is `debian`, and the password is `temppwd`.

## Enabling the Root Account for SSH

```shell
vi /etc/ssh/sshd_config
```

Change `#PermitRootLogin prohibit-password` to `PermitRootLogin yes`.

## Driver for Seeed OLED (SSD1306, I2C, 12864)

Download the smbus2 package using pip3:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

Refer to the program [**Grove - OLED Display 0.96 inch**](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green).

## References and Acknowledgments

- [Problemas en la depuración de Beaglebone Black 4G](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [Proyecto](https://beagleboard.org/p)
- [Actualizar el software en tu Beagle](https://beagleboard.org/upgrade#connect)
- [Firmware de prueba](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
