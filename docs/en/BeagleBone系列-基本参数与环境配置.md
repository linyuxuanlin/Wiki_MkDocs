# BeagleBone Series - Basic Parameters and Environment Configuration

## Hardware Resources

![Image](https://img.wiki-power.com/d/wiki-media/img/20211008090724.png)

- USB Type-A: Used in USB host mode
- USB Micro: Powers the board and serves as a client
- LEDs
  - D2: Flashes as a heartbeat indicator during boot
  - D3: Lights up when reading/writing SD card data
  - D4: Illuminates when the CPU is active
  - D5: Shines when reading/writing eMMC
- Boot/User Button: Regardless of whether it's pressed or not, if an SD card is present, the system will boot from the SD card (converging paths). After booting, it functions as a regular button connected to GPIO_72.
- I2C Grove Interface: Connected to I2C2
- UART Grove Interface: Linked to UART2
- Serial Debug: Connected to UART0, with pins from near USB labeled as pin1 through pin6: GND, NC, NC, RX, TX, NC

## Environment Configuration

### Driver Installation Issue

On Windows 10 and later systems, driver installation might fail due to driver enforcement.

Solution:

- Hold down `Shift` and click on "Restart" your computer.
- Go to "Troubleshoot" - "Advanced Options" - "Startup Settings" and click "Restart."
- After rebooting, follow on-screen instructions and press key `7` to disable driver enforcement.
- After startup, you can install BeagleBone drivers as usual.

### Image Download and Flashing

Official image download link: [https://beagleboard.org/latest-images](https://beagleboard.org/latest-images)  
Flashing tool: [https://sourceforge.net/projects/win32diskimager/files/latest/download](https://sourceforge.net/projects/win32diskimager/files/latest/download)

Burn the image onto an SD card, disconnect power, insert it into BeagleBone, and the system will boot from the SD card on the next power-up.

## Accessing via Command Line Tools

### Using Serial Port

Connect to the onboard serial terminal using a USB-to-serial converter, and open a terminal tool on your computer (e.g., WindTerm). (The initial username and password are both `root`).

The baud rate is 115200!

### Using Ethernet

Within the serial connection, run the `ifconfig` command to find the Ethernet address and connect using it. Username is `debian`, and the password is `temppwd`.

### Access via USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

Access through SSH. Username is `debian`, and the password is `temppwd`.

## Enabling the Root Account for SSH

```shell
vi /etc/ssh/sshd_config
```

Change `#PermitRootLogin prohibit-password` to `PermitRootLogin yes` to enable SSH access with the root account.

## Driver for Seeed OLED (SSD1306, I2C, 12864)

Use pip3 to download the smbus2 package:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

Refer to the program at [Grove - OLED Display 0.96 inch](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green).

## References and Acknowledgments

- [Issues During Debugging Beaglebone Black 4G](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [Project](https://beagleboard.org/p)
- [Updating Software on Your Beagle](https://beagleboard.org/upgrade#connect)
- [Firmware Testing](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.