# Serie BeagleBone - Desarrollo con la biblioteca BBIO

## Instalación de Adafruit-BBIO

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
sudo pip3 install Adafruit_BBIO
```

## Estructura básica del programa

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

Llamando a la biblioteca:

```py
import Adafruit_BBIO.GPIO as GPIO
```

### Configuración de pines de entrada / salida

```py
GPIO.setup("P8_14", GPIO.OUT)
```

`Entrada` / `Salida` se pueden seleccionar como `GPIO.IN`/`GPIO.OUT`.

### Configuración de nivel alto / bajo de salida

```py
GPIO.output("P8_14", GPIO.HIGH)
```

Los niveles `alto` / `bajo` se pueden seleccionar como `GPIO.HIGH`/`GPIO.LOW`, o `1`/`0`.

### Modo de entrada de pin

Verificar el estado del puerto de entrada:

```py
if GPIO.input("P8_14"):
  print("HIGH")
else:
  print("LOW")
```

Esperar entrada de borde, los parámetros son `GPIO.RISING`/`GPIO.FALLING`/`GPIO.BOTH`:

```py
GPIO.wait_for_edge(channel, GPIO.RISING)

o

GPIO.wait_for_edge(channel, GPIO.RISING, timeout)
```

### Monitoreo de entrada

```py
GPIO.add_event_detect("P9_12", GPIO.FALLING)
if GPIO.event_detected("P9_12"):
    print "event detected!"
```

## Retardo

Retardo de 1 segundo:

```py
import time
time.sleep(1)
```

## Salida PWM

```py
import Adafruit_BBIO.PWM as PWM
#PWM.start(通道, 占空比, 默认频率=2000, 极性=0)
PWM.start("P9_14", 50)

#También se pueden definir la frecuencia y la polaridad
PWM.start("P9_14", 50, 1000, 1)
```

El valor efectivo del ciclo de trabajo es de 0.0-100.0, la función start se utiliza para activar el PWM en ese canal.

Una vez que se ha iniciado el PWM, se pueden establecer el ciclo de trabajo o la frecuencia por separado:

```py
PWM.set_duty_cycle("P9_14", 25.5)
PWM.set_frequency("P9_14", 10)
```

Después de su uso, también se puede detener la salida PWM o borrar la información:

```py
PWM.stop("P9_14")
PWM.cleanup()
```

## Entrada ADC

En este marco, ADC tiene tres métodos de función: setup, read y read_raw. Antes de leer los datos, primero se debe configurar.

En BeagleBone, los siguientes pines se pueden usar como ADC:

```
"AIN4", "P9_33"
"AIN6", "P9_35"
"AIN5", "P9_36"
"AIN2", "P9_37"
"AIN3", "P9_38"
"AIN0", "P9_39"
"AIN1", "P9_40"
```

Nota: El voltaje máximo del ADC es de 1.8V y la tierra del ADC es el pin GNDA_ADC (P9_34). Si se necesita detectar 3.3V, se puede utilizar una división de voltaje con resistencias, como se muestra en la siguiente imagen, para leer el valor analógico en un rango de 0-1.65V.

### Inicialización del ADC

```py
import Adafruit_BBIO.ADC as ADC

ADC.setup()
```

### Lectura de valores analógicos

```py
value = ADC.read("P9_40")

o

value = ADC.read("AIN1")
```

Este marco tiene un error que requiere leer dos veces consecutivas para obtener el valor analógico más reciente.

El valor leído es un valor entre 0 y 1.0, que se puede multiplicar por 1.8 para convertirlo en un valor de voltaje. Si no se desea hacer esto, también se puede utilizar read_raw para leer directamente el valor de voltaje real.

## Comunicación I2C

Para utilizar I2C, solo es necesario importar la biblioteca, establecer la dirección I2C y seleccionar el I2C que se va a utilizar (por defecto es I2C-1).

```py
from Adafruit_I2C import Adafruit_I2C

i2c = Adafruit_I2C(0x77)
```

La función I2C requiere la instalación del paquete de Python `python-smbus`, pero actualmente este paquete solo es compatible con la versión 2 de Python. En su lugar, se puede utilizar [**smbus2**](https://pypi.org/project/smbus2/).

## Comunicación SPI

Importar la biblioteca SPI:

```py
from Adafruit_BBIO.SPI import SPI
```

## Otros

Si la instalación de Adafruit-BBIO falla, se puede realizar una instalación manual:

```
sudo apt-get update
sudo apt-get install build-essential python3-dev python3-pip -y
git clone git://github.com/adafruit/adafruit-beaglebone-io-python.git
cd adafruit-beaglebone-io-python
sudo python3 setup.py install
```

Actualizar Adafruit-BBIO:

```
sudo pip3 install --upgrade Adafruit_BBIO
```

Debido a la dependencia de python-smbus, I2C solo se puede utilizar en Python 2.

## Referencias y agradecimientos

- [Python Adafruit_GPIO.I2C Examples](https://www.programcreek.com/python/example/92524/Adafruit_GPIO.I2C)
- [Adafruit-BBIO 1.2.0](https://pypi.org/project/Adafruit-BBIO/#description)
- [Setting up IO Python Library on BeagleBone Black](https://learn.adafruit.com/setting-up-io-python-library-on-beaglebone-black)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.