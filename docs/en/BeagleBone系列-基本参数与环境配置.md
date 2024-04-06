# BeagleBone Series - Basic Parameters and Environment Configuration

## Hardware Resources

![BeagleBone Hardware](https://media.wiki-power.com/img/20211008090724.png)

- USB Type-A: Used in USB Host mode
- USB Micro: Provides power to the board and also serves as a client device
- LEDs
  - D2: Blinks as a heartbeat LED during boot
  - D3: Lights up when reading/writing data to the SD card
  - D4: Illuminates during CPU activity
  - D5: Lights up when reading/writing to the eMMC
- Boot/User Button: Regardless of pressing it or not, if there is an SD card, it will default to boot from the SD card (converging paths). After booting, it functions as a regular button connected to GPIO_72.
- I2C Grove Interface: Connected to I2C2
- Uart Grove Interface: Connected to UART2
- Serial Debug: Connected to UART0, with the pins near the USB port arranged from pin1 to pin6 as follows: GND, NC, NC, RX, TX, NC

## Environment Configuration

### Driver Installation Issue

In Windows 10 and higher versions, driver installation may fail due to driver enforcement signing by default.

Solution:

- Hold down `Shift` and click on "Restart" on your computer.
- Navigate to "Troubleshoot" - "Advanced options" - "Startup Settings" and click "Restart."
- Upon restart, follow the on-screen instructions and press key `7` on your keyboard to disable driver enforcement signing.
- After booting, you can proceed to install the BeagleBone driver without any issues.

### Image Download and Burning

Official image download link: [https://beagleboard.org/latest-images](https://beagleboard.org/latest-images)  
Burning tool: [https://sourceforge.net/projects/win32diskimager/files/latest/download](https://sourceforge.net/projects/win32diskimager/files/latest/download)

Burn the image to an SD card, power off, and insert it into the BeagleBone. The system will boot from the SD card on the next power-up.

## Access Using Command Line Tools

### Access via Serial Port

Connect to the onboard serial terminal using a USB to serial adapter, and open a terminal tool on your computer (e.g., WindTerm). The initial username and password are both `root`.

The baud rate is 115200!

### Access via Ethernet

Within the serial connection, use the `ifconfig` command to find the Ethernet address, and connect using that address. The username is `debian`, and the password is `temppwd`.

### Access via USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

Access using SSH, where the username is `debian`, and the password is `temppwd`.

## Enabling the Root Account with SSH

```shell
vi /etc/ssh/sshd_config
```

Change `#PermitRootLogin prohibit-password` to `PermitRootLogin yes`.

## Driver for Seeed OLED (SSD1306, I2C, 12864)

Install the smbus2 package using pip3:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

Reference the program [**Grove - OLED Display 0.96 inch**](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green).

## References and Acknowledgments

- [Issues in Beaglebone Black 4G Debugging](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [Project](https://beagleboard.org/p)
- [Upgrading Software on Your Beagle](https://beagleboard.org/upgrade#connect)
- [Firmware Testing](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
