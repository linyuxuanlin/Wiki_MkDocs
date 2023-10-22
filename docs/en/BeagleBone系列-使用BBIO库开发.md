# BeagleBone Series - Developing with the BBIO Library

## Installing Adafruit-BBIO

```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO
```

## Basic Program Structure

```python
import time
import Adafruit_BBIO.GPIO as GPIO

RELAY = "P9_22"            # GPIO P9_22
GPIO.setup(RELAY, GPIO.OUT)

while True:

    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(1)
    GPIO.output(RELAY, GPIO.LOW)
    time.sleep(1)
```

## GPIO

Library Import:

```python
import Adafruit_BBIO.GPIO as GPIO
```

### Setting Pin Direction (Input/Output)

```python
GPIO.setup("P8_14", GPIO.OUT)
```

Options for `Input` / `Output` are `GPIO.IN` or `GPIO.OUT`.

### Setting Output High/Low

```python
GPIO.output("P8_14", GPIO.HIGH)
```

Options for `High` / `Low` are `GPIO.HIGH` / `GPIO.LOW`, or `1` / `0`.

### Pin Input Mode

Checking the state of an input port:

```python
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

Waiting for edge input with parameters like `GPIO.RISING`/`GPIO.FALLING`/`GPIO.BOTH`:

```python
GPIO.wait_for_edge(channel, GPIO.RISING)

or

GPIO.wait_for_edge(channel, GPIO.RISING, timeout)
```

### Monitoring Input

```python
GPIO.add_event_detect("P9_12", GPIO.FALLING)
if GPIO.event_detected("P9_12"):
    print "event detected!"
```

## Delay

Delay for 1 second:

```python
import time
time.sleep(1)
```

## PWM Output

```python
import Adafruit_BBIO.PWM as PWM
#PWM.start(channel, duty cycle, default frequency=2000, polarity=0)
PWM.start("P9_14", 50)

#You can also define your own frequency and polarity
PWM.start("P9_14", 50, 1000, 1)
```

The valid duty cycle values range from 0.0 to 100.0. The start function is used to activate PWM on that channel.

Once PWM is started, you can independently set the duty cycle or frequency:

```python
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

After usage, you can stop PWM output or clean up:

```python
PWM.stop("P9_14")
PWM.cleanup()
```

## ADC Input

Within this framework, ADC has three functions: setup, read, and read_raw. You need to set up before reading data.

On the BeagleBone, you can use the following pins for ADC:

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```

Note: The maximum voltage for ADC is 1.8V, and the ground for ADC is the GNDA_ADC (P9_34) pin. If you need to measure 3.3V, you can use a voltage divider, just like in the diagram below, to scale 0-3.3V to 0-1.65V for reading analog values.

### Initializing the ADC

```python
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### Reading Analog Values

```python
value = ADC.read("P9_40")

or

value = ADC.read("AIN1")
```

There is a bug in this framework that requires reading twice consecutively to obtain the most recent analog value.

The result you get from reading is a value between 0 and 1.0, which can be multiplied by 1.8 to convert it to a voltage value. If you prefer a simpler approach, you can use `read_raw` to directly read the actual voltage value.

## I2C Communication

To use I2C, simply import the library, set the I2C address, and specify which I2C interface to use (default is I2C-1).

```python
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

I2C functionality requires the installation of the python package `python-smbus`. However, this package is currently only compatible with Python 2. You can use [**smbus2**](https://pypi.org/project/smbus2/) as an alternative.

## SPI Communication

Import the SPI library:

```python
from Adafruit_BBIO.SPI import SPI
```

## Other Information

If the installation of Adafruit-BBIO fails, you can try installing it manually:

```bash
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

To upgrade Adafruit-BBIO:

```bash
sudo pip3 install --upgrade Adafruit_BBIO
```

I2C is only supported in Python 2 due to its dependency on python-smbus.

## References and Acknowledgments

- [Python Adafruit_GPIO.I2C Examples](https://www.programcreek.com/python/example/92524/Adafruit_GPIO.I2C)
- [Adafruit-BBIO 1.2.0](https://pypi.org/project/Adafruit-BBIO/#description)
- [Setting up IO Python Library on BeagleBone Black](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.