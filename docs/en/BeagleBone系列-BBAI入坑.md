# BeagleBone Series - BBAI Getting Started

## Initialization

First, connect the 12V power input of the Cape and use a USB to serial module to connect to the onboard serial port (J3 port can be used for debugging):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211027164010.png)

Make sure the USB to serial module has a driver (I used the FTDI module, and the driver download address is <https://ftdichip.com/drivers/vcp-drivers/>).

Use a command line tool to connect to the serial port (I used MobaXterm), and set the baud rate to 115200.

## Install Patch Package

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

Rename it to `k3-j721e-beagleboneai64.dtb`, move it to the `/boot` directory and overwrite the original file. (I uploaded the file to the GitHub repository and used the `wget` command to get it. You may need to modify the GitHub host to download it properly)

You can also transfer files directly using sftp.

## evtest

The event test tool is a tool for printing evdev kernel events. It reads and prints events with values and symbol names directly from the kernel device, and can be used to debug input devices such as mice, keyboards, and touchpads.

Download the evtest tool:

```shell
sudo apt install evtest
```

Use the tool:

```shell
sudo evtest /dev/input/eventｘ (ｘ is the event number)
```

## Key Press

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

## Device on SPI Bus

The above code output is from running the `evtest` command on a BeagleBone device. It shows the available input devices, and in this case, the selected device is `gpio-keys`. The supported events for this device include `EV_SYN` and `EV_KEY`, with specific event codes for different buttons (`BTN_0`, `BTN_1`, `BTN_2`). The key repeat handling is also specified.

The output then shows the testing of the device, with events being generated when a button is pressed (`value 1`) and released (`value 0`). These events are timestamped and labeled with their event type and code.

- Barometer - BMP280
- 6-DOF - LSM6DS3TR
- Compass - BMM150

```shell
cd /sys/bus/iio/devices && ls -l

cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## BeagleConnect Communication

```shell
# BC_RST
cd /sys/class/gpio
echo 326 > export
echo out > gpio326/direction
echo 0 > gpio326/value
echo 1 > gpio326/value


# Uart2
root@BeagleBone:/sys/class/tty# ls -l
lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS4 -> ../../devices/platform/bus@100000/2820000.serial/tty/ttyS4

sudo apt-get install minicom
sudo minicom -D /dev/ttyS4

Welcome to minicom 2.8
OPTIONS: I18n
Port /dev/ttyS4, 10:57:41
Press CTRL-A Z for help on special keys

hello
```

Test unsuccessful, no data received or transmitted.

## LEDs

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightnessb

echo 0 > beaglebone:green:cape1/brightness # Cannot turn off
```

## LiDAR

If prompted with no permission, please refer to [**Enabling the Root Account with SSH**](https://wiki-power.com/en/BeagleBone%E7%B3%BB%E5%88%97-%E5%9F%BA%E6%9C%AC%E5%8F%82%E6%95%B0%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E5%90%AF%E7%94%A8-ssh-%E7%9A%84-root-%E5%B8%90%E6%88%B7), and execute with root permission.

First, operate GPIO to make the LIDAR spin.

```shell
cd /sys/class/gpio
echo 306 > export
echo 374 > export
echo out > gpio306/direction
echo out > gpio374/direction
echo 0 > gpio374/value
echo 1 > gpio306/value
```

echo 1 > gpio374/value
echo 0 > gpio306/value

Confirm the interface:

```shell
ls -l /sys/class/tty/

lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

Download the latest SDK: <https://github.com/Slamtec/rplidar_sdk/releases>

Modify the `/sdk/sdk/src/hal/event.h` file to compile normally:

```shell
enum
     {
         EVENT_OK = 1,
-        EVENT_TIMEOUT = -1,
+        EVENT_TIMEOUT = 2,
         EVENT_FAILED = 0,
     };
```

Switch to the `/sdk` directory and use the `make` command to compile. The compiled files are in the `/sdk/output` directory.

Switch to the `/sdk/output/Linux/Release` directory and use the following command to run the test program:

```shell
./ultra_simple /dev/ttyS0
```

## References and Acknowledgements

- [Schematic](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [Image](https://rcn-ee.net/rootfs/debian-arm64/)
- [Test code](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Cape issues](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [Lidar](https://github.com/Slamtec/rplidar_sdk)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.