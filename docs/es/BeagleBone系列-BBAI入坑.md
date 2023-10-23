# Serie BeagleBone - Introducción a BBAI

## Inicialización

En primer lugar, conecta la fuente de alimentación de 12V del Cape y utiliza un módulo USB a serie para conectar el puerto serie integrado (solo se puede utilizar el puerto J3 para depuración):

![](https://img.wiki-power.com/d/wiki-media/img/20211027164010.png)

Asegúrate de tener los controladores del módulo USB a serie instalados (yo utilicé el módulo FTDI, puedes descargar los controladores en <https://ftdichip.com/drivers/vcp-drivers/>).

Utiliza una herramienta de línea de comandos para conectar al puerto serie (yo utilicé MobaXterm) y configura la velocidad de transmisión en 115200.

## Instalación del paquete de parches

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

Renombra el archivo como `k3-j721e-beagleboneai64.dtb`, muévelo al directorio `/boot` y sobrescribe el archivo original. (Yo subí el archivo a un repositorio de GitHub y lo descargué utilizando el comando `wget`. Es posible que necesites modificar el host de GitHub para descargarlo correctamente).

También puedes transferir el archivo directamente utilizando SFTP.

## evtest

La herramienta evtest es una utilidad para imprimir eventos del kernel evdev. Lee directamente del dispositivo del kernel y muestra eventos con nombres y valores simbólicos, lo que puede ser útil para depurar dispositivos de entrada como ratones, teclados y touchpads.

Descarga la herramienta evtest:

```shell
sudo apt install evtest
```

Utiliza la herramienta:

```shell
sudo evtest /dev/input/eventｘ (ｘ es el número de evento)
```

## Teclas

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

## Dispositivos en el bus SPI

- Barómetro - BMP280
- 6-DOF - LSM6DS3TR
- Brújula - BMM150

```shell
cd /sys/bus/iio/devices && ls -l

cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## Comunicación BeagleConnect

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

Bienvenido a minicom 2.8
OPCIONES: I18n
Puerto /dev/ttyS4, 10:57:41
Presione CTRL-A Z para obtener ayuda sobre las teclas especiales

hola
```

La prueba no fue exitosa, no se recibieron ni se enviaron datos.

## LEDs

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightnessb

echo 0 > beaglebone:green:cape1/brightness # No se puede apagar
```

## LIDAR

Si se muestra un mensaje de falta de permisos, consulte [**Habilitar la cuenta root con ssh**](https://wiki-power.com/BeagleBone%E7%B3%BB%E5%88%97-%E5%9F%BA%E6%9C%AC%E5%8F%82%E6%95%B0%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E5%90%AF%E7%94%A8-ssh-%E7%9A%84-root-%E5%B8%90%E6%88%B7)，y ejecute los comandos con permisos de root.

Primero, configure los GPIO para que el LIDAR funcione.

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

Confirme la interfaz:

```shell
ls -l /sys/class/tty/

lrwxrwxrwx 1 root root 0 Jul 13 17:29 ttyS0 -> ../../devices/platform/bus@100000/2880000.serial/tty/ttyS0
```

Descargue la última versión del SDK en: <https://github.com/Slamtec/rplidar_sdk/releases>

Modifique el archivo `/sdk/sdk/src/hal/event.h` para compilar correctamente:

```shell
enum
     {
         EVENT_OK = 1,
-        EVENT_TIMEOUT = -1,
+        EVENT_TIMEOUT = 2,
         EVENT_FAILED = 0,
     };
```


Cambia al directorio `/sdk` y compila usando el comando `make`. Los archivos compilados se encontrarán en el directorio `/sdk/output`.

Luego, cambia al directorio `/sdk/output/Linux/Release` y ejecuta el siguiente comando para ejecutar el programa de prueba:

```shell
./ultra_simple /dev/ttyS0
```

## Referencias y Agradecimientos

- [Esquema](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [Imagen](https://rcn-ee.net/rootfs/debian-arm64/)
- [Código de prueba](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Problemas con la Cape](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [Lidar láser](https://github.com/Slamtec/rplidar_sdk)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.