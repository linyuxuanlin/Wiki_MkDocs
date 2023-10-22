# BeagleBone Series - Getting Started with BBAI

## Initialization

First, connect the Cape's 12V power input and use a USB to serial module to connect to the onboard serial port (use the J3 port for debugging):

![Connection Image](https://img.wiki-power.com/d/wiki-media/img/20211027164010.png)

Ensure that the USB to serial module has the necessary drivers installed (I used an FTDI module, and you can find the driver download link here: [FTDI Drivers](https://ftdichip.com/drivers/vcp-drivers/)).

Use a command-line tool to connect to the serial port (I used MobaXterm) and set the baud rate to 115200.

## Installing Patch Files

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

Rename it to `k3-j721e-beagleboneai64.dtb` and move it to the `/boot` directory, overwriting the original file. (I uploaded the file to a GitHub repository and used the `wget` command to retrieve it. You may need to modify the GitHub host for successful downloading).

You can also transfer the file directly using sftp.

## evtest

The `evtest` tool is used to print evdev kernel events. It reads and prints events with values and symbolic names directly from kernel devices and can be used to debug input devices like mice, keyboards, touchpads, and more.

Download the `evtest` tool:

```shell
sudo apt install evtest
```

Use the tool:

```shell
sudo evtest /dev/input/eventｘ (where ｘ is the event number)
```

## Keyboards

```shell
debian@BeagleBone:~$ evtest
No device specified, trying to scan all of /dev/input/event*
Available devices:
/dev/input/event0:      gpio-keys
Select the device event number [0-0]: 0
Input driver version is 1.0.1
Input device ID: bus 0x19 vendor 0x1 product 0x1 version 0x100
Input device name: "gpio-keys"
Supported events:
  Event type 0 (EV_SYN)
  Event type 1 (EV_KEY)
    Event code 256 (BTN_0)
    Event code 257 (BTN_1)
    Event code 258 (BTN_2)
Key repeat handling:
  Repeat type 20 (EV_REP)
    Repeat code 0 (REP_DELAY)
      Value    250
    Repeat code 1 (REP_PERIOD)
      Value     33
Properties:
Testing ... (interrupt to exit)
Event: time 1634868166.060258, type 1 (EV_KEY), code 257 (BTN_1), value 1
Event: time 1634868166.060258, -------------- SYN_REPORT ------------
Event: time 1634868166.284257, type 1 (EV_KEY), code 257 (BTN_1), value 0
Event: time 1634868166.284257, -------------- SYN_REPORT ------------
```

## Devices on the SPI Bus

- Barometer - BMP280
- 6-DOF - LSM6DS3TR
- Compass - BMM150

```shell
# BeagleConnect Communication

Change directory to the IIO devices and list them:
```shell
cd /sys/bus/iio/devices && ls -l
```

Display the names of IIO devices:
```shell
cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## BeagleConnect Reset

Set up the BC_RST pin for communication:
```shell
cd /sys/class/gpio
echo 326 > export
echo out > gpio326/direction
echo 0 > gpio326/value
echo 1 > gpio326/value
```

## Uart2 Configuration

List the Uart2 configuration:
```shell
ls -l /sys/class/tty
```

Install Minicom and access Uart2 for communication:
```shell
sudo apt-get install minicom
sudo minicom -D /dev/ttyS4
```

Upon successful setup, you will be able to send and receive data. If no data is being transmitted or received, further troubleshooting is required.

## LEDs Control

Navigate to the LED control directory and set the brightness of LEDs:
```shell
cd /sys/class/leds && ls -l
echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightness
echo 0 > beaglebone:green:cape1/brightness # Cannot turn off
```

## Laser Radar Setup

If you encounter permission issues, please refer to the [Enabling the Root SSH Account](to_be_replaced[3]) section in the BeagleBone Series Basic Parameters and Environment Configuration documentation.

To begin, operate the GPIO to activate the laser radar:

```shell
cd /sys/class/gpio
echo 306 > export
echo 374 > export
echo out > gpio306/direction
echo out > gpio374/direction
echo 0 > gpio374/value
echo 1 > gpio306/value
```

To turn off the laser radar:

```shell
echo 1 > gpio374/value
echo 0 > gpio306/value
```

Confirm the interface:

```shell
ls -l /sys/class/tty/
lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

Download the latest SDK from [Slamtec/rplidar_sdk/releases](https://github.com/Slamtec/rplidar_sdk/releases).

Modify the `/sdk/sdk/src/hal/event.h` file for proper compilation:

```shell
enum
{
    EVENT_OK = 1,
    EVENT_TIMEOUT = 2,
    EVENT_FAILED = 0,
};
```

Switch to the `/sdk` directory and use the `make` command for compilation. The compiled files will be located in the `/sdk/output` directory.

Navigate to the `/sdk/output/Linux/Release` directory and execute the following command to run the test routine:

```shell
./ultra_simple /dev/ttyS0
```

## References and Acknowledgments

- [Schematics](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [Image](https://rcn-ee.net/rootfs/debian-arm64/)
- [Test Code](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Cape Issues](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [Lidar](https://github.com/Slamtec/rplidar_sdk)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.