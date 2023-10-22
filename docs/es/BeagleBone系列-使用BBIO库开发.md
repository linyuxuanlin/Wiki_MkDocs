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
    GPIO.output(RELAY, GPIO.HIGH)
    time.sleep(1)
```

## GPIO

Library Invocation:

```python
import Adafruit_BBIO.GPIO as GPIO
```

### Configuring Pin Direction (Input/Output)

```python
GPIO.setup("P8_14", GPIO.OUT)
```

`Input`/`Output` can be set to `GPIO.IN`/`GPIO.OUT`.

### Setting Pin Output (High/Low)

```python
GPIO.output("P8_14", GPIO.HIGH)
```

`High`/`Low` can be set to `GPIO.HIGH`/`GPIO.LOW` or `1`/`0`.

### Pin Input Mode

Checking the state of an input port:

```python
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

Waiting for edge input, with parameters `GPIO.RISING`/`GPIO.FALLING`/`GPIO.BOTH`:

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

Adding a 1-second delay:

```python
import time
time.sleep(1)
```

## PWM Output

```python
import Adafruit_BBIO.PWM as PWM
# PWM.start(channel, duty cycle, default frequency=2000, polarity=0)
PWM.start("P9_14", 50)

# You can also define your own frequency and polarity
PWM.start("P9_14", 50, 1000, 1)
```

The valid duty cycle values range from 0.0 to 100.0, and the `start` function is used to activate PWM on that channel.

Once PWM is started, you can individually set the duty cycle or frequency:

```python
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

After use, you can stop PWM output or clean up the information:

```python
PWM.stop("P9_14")
PWM.cleanup()
```

## ADC Input

In this framework, ADC offers three functions: setup, read, and read_raw. You need to set up before reading data.

On the BeagleBone, the following pins can be used for ADC:

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```

**Nota:** El voltaje máximo de ADC es 1.8V, y la tierra de ADC es el pin GNDA_ADC (P9_34). Si es necesario detectar 3.3V, se puede utilizar una resistencia de división de voltaje, como se muestra en la imagen a continuación, para reducir de 0-3.3V a 0-1.65V y así leer el valor analógico.

### Inicialización de ADC

```python
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### Lectura del Valor Analógico

```python
valor = ADC.read("P9_40")

o

valor = ADC.read("AIN1")
```

Este marco tiene un pequeño error: necesita leer dos veces consecutivas para obtener el valor analógico más reciente.

El valor leído es un número entre 0 y 1.0, que se puede multiplicar por 1.8 para convertirlo en un valor de voltaje. Si prefiere una solución más sencilla, puede utilizar `read_raw` para obtener directamente el valor de voltaje real.

## Comunicación I2C

Para utilizar I2C, solo necesita importar la biblioteca, configurar la dirección I2C y seleccionar el bus I2C correspondiente (por defecto, es I2C-1).

```python
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

La funcionalidad I2C requiere la instalación del paquete de Python `python-smbus`, pero actualmente este paquete solo es compatible con Python 2. Puede reemplazarlo con [**smbus2**](https://pypi.org/project/smbus2/) como alternativa.

## Comunicación SPI

Importe la biblioteca SPI de la siguiente manera:

```python
from Adafruit_BBIO.SPI import SPI
```

## Otros

Si la instalación de Adafruit-BBIO falla, puede optar por una instalación manual:

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

Para actualizar Adafruit-BBIO:

```
sudo pip3 install --upgrade Adafruit_BBIO
```

Debido a la dependencia de python-smbus, la comunicación I2C solo es compatible con Python 2.

## Referencias y Agradecimientos

- [Ejemplos de Python Adafruit_GPIO.I2C](https://www.programcreek.com/python/example/92524/Adafruit_GPIO.I2C)
- [Adafruit-BBIO 1.2.0](https://pypi.org/project/Adafruit-BBIO/#description)
- [Configuración de la Biblioteca IO Python en BeagleBone Black](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.