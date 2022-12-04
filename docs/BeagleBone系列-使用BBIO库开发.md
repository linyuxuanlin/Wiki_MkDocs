---
id: BeagleBone系列-使用BBIO库开发
title: BeagleBone 系列 - 使用 BBIO 库开发
---

## 安装 Adafruit-BBIO

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO
```

## 基本程序框架

```py
import time
import Adafruit_BBIO.GPIO as GPIO

RELAY = "P9_22"            # GPIO P9_22
GPIO.setup(RELAY, GPIO.OUT)

while True:

    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(1)
```

## GPIO

调用库：

```py
import Adafruit_BBIO.GPIO as GPIO
```

### 设置引脚输入 / 输出

```py
GPIO.setup("P8_14", GPIO.OUT)
```

`输入` / `输出` 可选 `GPIO.IN`/`GPIO.OUT`。

### 设置输出高 / 低电平

```py
GPIO.output("P8_14", GPIO.HIGH)
```

`高` / `低` 电平可选 `GPIO.HIGH`/`GPIO.LOW`，或 `1`/`0`。

### 引脚输入模式

查看输入端口的状态：

```py
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

等待边沿输入，参数有 `GPIO.RISING`/`GPIO.FALLING`/`GPIO.BOTH`：

```py
GPIO.wait_for_edge(channel, GPIO.RISING)

或

GPIO.wait_for_edge(channel, GPIO.RISING, timeout)
```

### 监测输入

```py
GPIO.add_event_detect("P9_12", GPIO.FALLING)
if GPIO.event_detected("P9_12"):
    print "event detected!"
```

## 延时

延时 1 秒：

```py
import time
time.sleep(1)
```

## PWM 输出

```py
import Adafruit_BBIO.PWM as PWM
#PWM.start(通道, 占空比, 默认频率=2000, 极性=0)
PWM.start("P9_14", 50)

#也可以自己定义频率和极性
PWM.start("P9_14", 50, 1000, 1)
```

其中，占空比的有效值为 0.0-100.0，start 函数用于激活该通道上的 PWM。

当启动 PWM 之后，就可单独设置占空比或频率了：

```py
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

用完之后，也可以停止 PWM 输出，或清除信息：

```py
PWM.stop("P9_14")
PWM.cleanup()
```

## ADC 输入

在这个框架里面，ADC 有三个函数方法：setup，read 和 read_raw。在读取数据之前，要先 setup。

在 BeagleBone 上，以下引脚可以使用 ADC：

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```

注意：ADC 的最大电压为 1.8V，ADC 的地是 GNDA_ADC (P9_34) 引脚。如果需要检测 3.3V，可以用电阻分压，就像下图，把 0-3.3V 分到 0-1.65V 以读取模拟值。

### 初始化 ADC

```py
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### 读取模拟值

```py
value = ADC.read("P9_40")

或

value = ADC.read("AIN1")
```

这框架有个 bug，需要连续读两次，才能获取最新的的模拟值。

读回来的结果是一个 0-1.0 之间的值，可以乘以 1.8 以转换成电压值。如果不想这么麻烦，也可以用 read_raw 来直接读出真实电压值。

## I2C 通信

使用 I2C，只需要导入库，设置 I2C 地址，选择是哪个 I2C（默认是 I2C-1）。

```py
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

I2C 功能需要安装 python 包 `python-smbus`，但目前这个包只兼容 python 2 版本。我们可以用 [**smbus2**](https://pypi.org/project/smbus2/) 替换使用。

## SPI 通信

导入 SPI 库：

```py
from Adafruit_BBIO.SPI import SPI
```

## 其他

安装 Adafruit-BBIO 时，如果失败可选手动安装：

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

升级 Adafruit-BBIO：

```
sudo pip3 install --upgrade Adafruit_BBIO
```

因为 python-smbus 这个依赖的原因，I2C 仅限在 python2 下使用。

## 参考与致谢

- [Python Adafruit_GPIO.I2C Examples](https://www.programcreek.com/python/example/92524/Adafruit_GPIO.I2C)
- [Adafruit-BBIO 1.2.0](https://pypi.org/project/Adafruit-BBIO/#description)
- [Setting up IO Python Library on BeagleBone Black](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black)

> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

