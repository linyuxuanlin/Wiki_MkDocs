# BeagleBone Series - Developing with BBIO Library

## Installing Adafruit-BBIO

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO
```

## Basic Program Framework

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

Library call:

```py
import Adafruit_BBIO.GPIO as GPIO
```

### Setting Pin Input / Output

```py
GPIO.setup("P8_14", GPIO.OUT)
```

`Input` / `Output` can be set to `GPIO.IN`/`GPIO.OUT`.

### Setting Output High / Low Level

```py
GPIO.output("P8_14", GPIO.HIGH)
```

`High` / `Low` level can be set to `GPIO.HIGH`/`GPIO.LOW`, or `1`/`0`.

### Pin Input Mode

Check the status of the input port:

```py
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

Wait for edge input, with parameters `GPIO.RISING`/`GPIO.FALLING`/`GPIO.BOTH`:

```py
GPIO.wait_for_edge(channel, GPIO.RISING)

or

GPIO.wait_for_edge(channel, GPIO.RISING, timeout)
```

### Monitoring Input

## Delay

Delay for 1 second:

```py
import time
time.sleep(1)
```

## PWM Output

```py
import Adafruit_BBIO.PWM as PWM
#PWM.start(channel, duty, freq=2000, polarity=0)
PWM.start("P9_14", 50)

#Custom frequency and polarity can also be defined
PWM.start("P9_14", 50, 1000, 1)
```

The valid range for duty is 0.0-100.0. The start function is used to activate PWM on the channel.

Once PWM is started, duty cycle or frequency can be set separately:

```py
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

After use, PWM output can also be stopped or cleaned up:

```py
PWM.stop("P9_14")
PWM.cleanup()
```

## ADC Input

In this framework, there are three functions for ADC: setup, read, and read_raw. Before reading data, setup must be done.

On BeagleBone, the following pins can be used for ADC:

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```

Note: The maximum voltage for ADC is 1.8V, and the ground for ADC is the GNDA_ADC (P9_34) pin. If you need to detect 3.3V, you can use a voltage divider, like the one in the following image, to divide 0-3.3V into 0-1.65V for reading analog values.

### Initialize ADC

```py
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### Read Analog Value

```py
value = ADC.read("P9_40")

or

```

# Adafruit-BBIO Library for BeagleBone

The Adafruit-BBIO library is a Python library that allows easy access to the GPIO, PWM, ADC, I2C, and SPI functionalities of the BeagleBone Black and other BeagleBone models.

## Installation

To install the library, run the following command:

```
sudo pip3 install Adafruit_BBIO
```

## GPIO

To use the GPIO pins, simply import the library and use the `setup()` and `output()` functions:

```py
import Adafruit_BBIO.GPIO as GPIO

GPIO.setup("P8_10", GPIO.OUT)
GPIO.output("P8_10", GPIO.HIGH)
```

## PWM

To use the PWM pins, import the library and use the `start()` and `set_duty_cycle()` functions:

```py
import Adafruit_BBIO.PWM as PWM

PWM.start("P8_13", 50)
PWM.set_duty_cycle("P8_13", 25.5)
```

## ADC

To use the ADC pins, import the library and use the `read()` function:

```py
import Adafruit_BBIO.ADC as ADC

value = ADC.read("AIN1")
```

There is a bug in this framework that requires reading the pin twice to get the latest analog value.

The result returned is a value between 0 and 1.0, which can be multiplied by 1.8 to convert to a voltage value. If you don't want to do this, you can use `read_raw` to directly read the actual voltage value.

## I2C Communication

To use I2C, simply import the library, set the I2C address, and choose which I2C to use (default is I2C-1):

```py
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

The I2C functionality requires the installation of the `python-smbus` package, but currently this package is only compatible with Python 2. We can use [**smbus2**](https://pypi.org/project/smbus2/) as a replacement.

## SPI Communication

To use SPI, import the SPI library:

```py
from Adafruit_BBIO.SPI import SPI
```

## Other

If the installation of Adafruit-BBIO fails, you can manually install it:

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

To upgrade Adafruit-BBIO:

```
sudo pip3 install --upgrade Adafruit_BBIO
```

Due to the dependency on `python-smbus`, I2C can only be used with Python 2.

## References and Acknowledgements

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.