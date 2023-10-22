# Serie BeagleBone - Iniciando con BBAI

## Inicialización

En primer lugar, conecta la fuente de alimentación de 12V de la Cape y utiliza un módulo USB a serie para conectar el puerto serie a bordo (el puerto J3 se puede utilizar para fines de depuración):

![](https://img.wiki-power.com/d/wiki-media/img/20211027164010.png)

Asegúrate de que el módulo USB a serie tenga el controlador instalado (yo utilicé un módulo FTDI, puedes descargar el controlador desde <https://ftdichip.com/drivers/vcp-drivers/>).

Utiliza una herramienta de línea de comandos para conectar al puerto serie (yo usé MobaXterm) y configura la velocidad de bits a 115200.

## Instalación del paquete de parches

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

Renómbralo como `k3-j721e-beagleboneai64.dtb`, muévelo al directorio `/boot` y sobrescribe el archivo original. (Yo subí el archivo a un repositorio de GitHub y lo descargué usando el comando `wget`. Es posible que necesites modificar el host de GitHub para que la descarga sea exitosa).

También puedes transferir el archivo directamente mediante sftp.

## evtest

La herramienta de prueba de eventos es una utilidad que imprime eventos del kernel evdev. Lee directamente del dispositivo del kernel y muestra eventos con nombres de valores y símbolos de dispositivos. Puede ser útil para depurar dispositivos de entrada como ratones, teclados, touchpads, entre otros.

Descarga la herramienta evtest:

```shell
sudo apt install evtest
```

Utiliza la herramienta:

```shell
sudo evtest /dev/input/eventｘ（ｘ es el número de evento）
```

## Teclas

```shell
debian@BeagleBone:~$ evtest
No se especificó un dispositivo, intentando escanear todos los eventos en /dev/input/event*
Dispositivos disponibles:
/dev/input/event0: gpio-keys
Selecciona el número de evento del dispositivo [0-0]: 0
La versión del controlador de entrada es 1.0.1
ID del dispositivo de entrada: bus 0x19, fabricante 0x1, producto 0x1, versión 0x100
Nombre del dispositivo de entrada: "gpio-keys"
Eventos admitidos:
  Tipo de evento 0 (EV_SYN)
  Tipo de evento 1 (EV_KEY)
    Código de evento 256 (BTN_0)
    Código de evento 257 (BTN_1)
    Código de evento 258 (BTN_2)
Gestión de repetición de teclas:
  Tipo de repetición 20 (EV_REP)
    Código de repetición 0 (REP_DELAY)
      Valor    250
    Código de repetición 1 (REP_PERIOD)
      Valor     33
Propiedades:
Pruebas en curso... (interrumpe para salir)
Evento: tiempo 1634868166.060258, tipo 1 (EV_KEY), código 257 (BTN_1), valor 1
Evento: tiempo 1634868166.060258, -------------- INFORME SYN --------------
Evento: tiempo 1634868166.284257, tipo 1 (EV_KEY), código 257 (BTN_1), valor 0
Evento: tiempo 1634868166.284257, -------------- INFORME SYN --------------
```

## Dispositivos en el bus SPI

- Barómetro - BMP280
- 6-DOF - LSM6DS3TR
- Brújula - BMM150

```shell
# Cambio de directorio a /sys/bus/iio/devices y listado de archivos y directorios
cd /sys/bus/iio/devices && ls -l

# Lectura del nombre de los dispositivos IIO
cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## Comunicación BeagleConnect

```shell
# Reinicio de BC_RST
cd /sys/class/gpio
echo 326 > export
echo out > gpio326/direction
echo 0 > gpio326/value
echo 1 > gpio326/value

# Configuración y uso de Uart2
root@BeagleBone:/sys/class/tty# ls -l
lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS4 -> ../../devices/platform/bus@100000/2820000.serial/tty/ttyS4

# Instalación de minicom
sudo apt-get install minicom

# Inicio de minicom en el puerto /dev/ttyS4
sudo minicom -D /dev/ttyS4

Welcome to minicom 2.8
OPTIONS: I18n
Port /dev/ttyS4, 10:57:41
Press CTRL-A Z for help on special keys

hello
```

La prueba no fue exitosa, ya que no se recibieron ni enviaron datos.

## LEDs

```shell
# Cambio de directorio a /sys/class/leds y listado de archivos y directorios
cd /sys/class/leds && ls -l

# Encender los LEDs con brillo máximo
echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightness

# Apagar el LED cape1
echo 0 > beaglebone:green:cape1/brightness
```

## LIDAR (Láser Imaging Detection and Ranging)

Si se muestra un mensaje de "permiso denegado", consulte [**Habilitar la cuenta de root con SSH**](https://wiki-power.com/es/BeagleBone-Series-Basic-Parameters-and-Environment-Configuration#Enable-root-account-for-SSH], y luego ejecute los siguientes comandos con privilegios de root.

Primero, activamos los pines GPIO para que el LIDAR empiece a girar.

```shell
cd /sys/class/gpio
echo 306 > export
echo 374 > export
echo out > gpio306/direction
echo out > gpio374/direction
echo 0 > gpio374/value
echo 1 > gpio306/value
```

Después de habilitar los pines GPIO, confirmamos la interfaz disponible:

```shell
ls -l /sys/class/tty/

lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

Para descargar la última versión del SDK, visite: <https://github.com/Slamtec/rplidar_sdk/releases>

Realice una modificación en el archivo `/sdk/sdk/src/hal/event.h` para permitir una compilación exitosa:

```shell
enum
{
    EVENT_OK = 1,
    EVENT_TIMEOUT = 2,  # Cambio de -1 a 2
    EVENT_FAILED = 0,
};
```

```markdown
Dirígete a la carpeta `/sdk`, y utiliza el comando `make` para compilar. Los archivos generados se encontrarán en la carpeta `/sdk/output`.

Luego, cambia al directorio `/sdk/output/Linux/Release` y ejecuta las pruebas utilizando el siguiente comando:

```shell
./ultra_simple /dev/ttyS0
```

## Referencias y Agradecimientos

- [Esquema original](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [Imagen del sistema](https://rcn-ee.net/rootfs/debian-arm64/)
- [Código de prueba](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Problemas con el Cape](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [Lidar láser](https://github.com/Slamtec/rplidar_sdk)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.
```


> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.