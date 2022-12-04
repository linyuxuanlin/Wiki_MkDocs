---
id: BeagleBone系列-BBAI入坑
title: BeagleBone 系列 - BBAI 入坑
---

## 初始化

首先，连接 Cape 的 12V 电源输入，使用 USB 转串口模块，连接板载串口（J3 口才能用于调试）：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211027164010.png)

确保 USB 转串口模块有驱动（我用到是 FTDI 模块，驱动下载地址是 <https://ftdichip.com/drivers/vcp-drivers/>）。

使用命令行工具连接串口（我用的是 MobaXterm），波特率设置为 115200。

## 安装补丁包

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

改名为 `k3-j721e-beagleboneai64.dtb`，移至 `/boot` 目录下并覆盖原文件。（我将文件传到 GitHub 仓库，使用 `wget` 命令获取。可能需要修改 GitHub host 才能正常下载）

也可以直接使用 sftp 传输文件。

## evtest

event test 工具是打印 evdev 内核事件的工具，它直接从内核设备读取并打印设备描述的带有值和符号名的事件，可以用来调试鼠标、键盘、触摸板等输入设备。

下载 evtest 工具：

```shell
sudo apt install evtest
```

使用工具：

```shell
sudo evtest /dev/input/eventｘ（ｘ就是时间编号）
```

## 按键

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

## SPI 总线上设备

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

## BeagleConnect 通信

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

测试不成功，未收发到数据。

## LEDs

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightnessb

echo 0 > beaglebone:green:cape1/brightness # 关不掉
```

## 激光雷达

如果提示没有权限，请见 [**启用 ssh 的 root 帐户**](https://wiki-power.com/BeagleBone%E7%B3%BB%E5%88%97-%E5%9F%BA%E6%9C%AC%E5%8F%82%E6%95%B0%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E5%90%AF%E7%94%A8-ssh-%E7%9A%84-root-%E5%B8%90%E6%88%B7)，使用 root 权限执行。

首先，操作 GPIO 使激光雷达转起来。

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

确认接口：

```shell
ls -l /sys/class/tty/

lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

下载最新的 SDK：<https://github.com/Slamtec/rplidar_sdk/releases>

修改 `/sdk/sdk/src/hal/event.h` 文件以正常编译：

```shell
enum
     {
         EVENT_OK = 1,
-        EVENT_TIMEOUT = -1,
+        EVENT_TIMEOUT = 2,
         EVENT_FAILED = 0,
     };
```

切换到 `/sdk` 目录下，使用 `make` 命令编译，编译出来的文件在 `/sdk/output` 目录下。

切换到 `/sdk/output/Linux/Release` 目录下，使用以下命令跑测试例程：

```shell
./ultra_simple /dev/ttyS0
```

## 参考与致谢

- [原理图](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [镜像](https://rcn-ee.net/rootfs/debian-arm64/)
- [测试代码](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Cape 问题](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [激光雷达](https://github.com/Slamtec/rplidar_sdk)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

