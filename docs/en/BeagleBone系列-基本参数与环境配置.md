# BeagleBone Series - Basic Parameters and Environment Configuration

## Hardware Resources

![](https://f004.backblazeb2.com/file/wiki-media/img/20211008090724.png)

- USB Type-A: used as a USB host mode
- USB Micro: used to power the board and as a slave
- LEDs
  - D2: flashes as a heartbeat light during startup
  - D3: lights up when reading/writing SD card data
  - D4: lights up when the CPU is active
  - D5: lights up when reading/writing eMMC
- Boot/User button: regardless of whether it is pressed or not, if there is an SD card, it will default to boot from the SD card (different paths lead to the same goal). After booting, it acts as a normal button, connected to GPIO_72.
- I2C Grove interface: connected to I2C2
- Uart Grove interface: connected to UART2
- Serial Debug: connected to UART0, with the pins near USB as pin1, and from pin1-pin6 as: GND, NC, NC, RX, TX, NC

## Environment Configuration

### Driver Installation Issues

In Windows 10 and above, the default is to use driver program forced signature, which may be the reason for the driver installation failure.

Solution:

- Hold down `shift` and click restart the computer
- Enter `Troubleshoot` - `Advanced Options` - `Startup Settings`, and click `Restart`
- After restarting, follow the page prompts and press `7` on the keyboard to disable driver program forced signature
- After booting, you can install the BeagleBone driver program normally

### Image Download and Burning

Official image download address: https://beagleboard.org/latest-images  
Burning tool: https://sourceforge.net/projects/win32diskimager/files/latest/download

Burn the image into the SD card, power off and insert it into the BeagleBone, and the system will boot from the SD card next time it is powered on.

## Using Command Line Tools for Access

### Using Serial Port Access

Use a USB-to-serial connection to connect to the onboard serial port, and open a serial port tool (such as WindTerm) on the computer for connection. (The initial username and password are both `root`)

The baud rate is 115200!

### Using Ethernet Access

Use the command `ifconfig` in the serial connection to find the Ethernet address and connect through it. The username is `debian` and the password is `temppwd`.

### Access via USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

Access using SSH, with the username `debian` and password `temppwd`.

## Enable root account with SSH

```shell
vi /etc/ssh/sshd_config
```

Change `#PermitRootLogin prohibit-password` to `PermitRootLogin yes`.

## Seeed OLED Driver (SSD1306, I2C, 12864)

Use pip3 to download the smbus2 package:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

Refer to the program in [**Grove - OLED Display 0.96 inch**](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green).

## References and Acknowledgments

- [Beaglebone black 4G debugging issues](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [Projects](https://beagleboard.org/p)
- [Upgrade the software on your Beagle](https://beagleboard.org/upgrade#connect)
- [Test firmware](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.