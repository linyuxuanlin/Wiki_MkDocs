---
id: BeagleBone系列-基本参数与环境配置
title: BeagleBone 系列 - 基本参数与环境配置
---

## 硬件资源

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211008090724.png)

- USB Type-A：作为 USB 从机（Host）模式使用
- USB Micro：为板子供电并且作为从机
- LEDs
  - D2：在启动时以心跳灯闪烁
  - D3：读写 SD 卡数据时亮起
  - D4：当 CPU 活动时亮起
  - D5：当 eMMC 读写时亮起
- Boot/User 按钮：不管按不按，如果有 SD 卡都会默认从 SD 卡启动（殊途同归），当启动后就作为一个普通按钮，连接到 GPIO_72
- I2C Grove 接口：连接到 I2C2
- Uart Grove 接口：连接到 UART2
- Serial Debug：连接到 UART0，靠近 USB 的引脚为 pin1，从 pin1-pin6 分别为：GND, NC, NC, RX, TX, NC

## 环境配置

### 驱动安装问题

在 Windows 10 及以上版本系统，默认采用驱动程序强制签名，这可能是驱动安装失败的原因。

解决方法：

- 按住 `shift`，点击重启电脑
- 进入 `疑难解答` - `高级选项` - `启动设置`，点击 `重启`
- 重启后，按页面提示，按键盘 `7`，即可禁用驱动程序强制签名
- 开机后，即可正常安装 BeagleBone 的驱动程序

### 镜像下载烧录

官网镜像下载地址：https://beagleboard.org/latest-images  
烧录工具：https://sourceforge.net/projects/win32diskimager/files/latest/download

将镜像烧录进 SD 卡，断电插入 BeagleBone，下次上电就会从 SD 卡启动系统

## 使用命令行工具访问

### 使用串口访问

使用 USB 转串口连接板载的串行端子，在电脑端打开串口工具（如 WindTerm）进行连接。（初始用户名和密码均为 `root`）

波特率是 115200！

### 使用以太网访问

在串口连接内使用命令 `ifconfig` 找到以太网地址，通过地址连接。用户名为 `debian`，密码为 `temppwd`。

### 通过 USB 访问

usb0：192.168.7.2  
usb1：192.168.6.2

使用 SSH 方式访问，用户名为 `debian`，密码为 `temppwd`。

## 启用 ssh 的 root 帐户

```shell
vi /etc/ssh/sshd_config
```

将 `#PermitRootLogin prohibit-password` 修改为 `PermitRootLogin yes` 即可。

## 驱动 Seeed OLED（SSD1306，I2C，12864）

使用 pip3 下载 smbus2 包：

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

程序参考 [**Grove - OLED Display 0.96 inch**](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green)。

## 参考与致谢

- [Beaglebone black 4G 调试中的问题](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [项目](https://beagleboard.org/p)
- [Upgrade the software on your Beagle](https://beagleboard.org/upgrade#connect)
- [测试固件](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)
