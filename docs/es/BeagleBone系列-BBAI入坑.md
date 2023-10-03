# Serie BeagleBone - Iniciando con BBAI

## Inicialización

En primer lugar, conecte la entrada de alimentación de 12V de la Cape, use un módulo USB a serie para conectar el puerto serie integrado (solo se puede usar el puerto J3 para la depuración):

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211027164010.png)

Asegúrese de que el módulo USB a serie tenga controladores (utilicé el módulo FTDI, la dirección de descarga del controlador es <https://ftdichip.com/drivers/vcp-drivers/>).

Conecte el puerto serie con una herramienta de línea de comandos (utilicé MobaXterm), configure la velocidad de transmisión en 115200.

## Instalación del paquete de parches

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

Renombre el archivo como `k3-j721e-beagleboneai64.dtb`, muévalo al directorio `/boot` y sobrescriba el archivo original. (Subí el archivo a mi repositorio de GitHub y lo obtuve con el comando `wget`. Es posible que deba modificar el host de GitHub para descargarlo correctamente).

También puede transferir el archivo directamente a través de sftp.

## evtest

La herramienta de prueba de eventos es una herramienta que imprime eventos del kernel evdev. Lee directamente del dispositivo del kernel y muestra eventos con nombres de valores y símbolos, lo que se puede utilizar para depurar dispositivos de entrada como ratones, teclados y touchpads.

Descargue la herramienta evtest:

```shell
sudo apt install evtest
```

Usando la herramienta:

```shell
sudo evtest /dev/input/eventｘ（ｘes el número de evento）
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

# Comunicación BeagleConnect

```shell
cd /sys/bus/iio/devices && ls -l

cat iio\:device0/name
cat iio\:device1/name
cat iio\:device2/name
cat iio\:device3/name
cat iio\:device4/name
cat iio\:device5/name
```

## BeagleConnect Comunicación

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

La prueba no tuvo éxito, no se recibió ni se envió ningún dato.

## LEDs

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightnessb

echo 0 > beaglebone:green:cape1/brightness # No se puede apagar
```

## LIDAR

Si se muestra un mensaje de falta de permisos, consulte [**Habilitar la cuenta de root con ssh**](https://wiki-power.com/es/BeagleBone%E7%B3%BB%E5%88%97-%E5%9F%BA%E6%9C%AC%E5%8F%82%E6%95%B0%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E5%90%AF%E7%94%A8-ssh-%E7%9A%84-root-%E5%B8%90%E6%88%B7)，y ejecute con permisos de root.

Primero, opere GPIO para hacer que el LIDAR gire.

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

Descargue el último SDK: <https://github.com/Slamtec/rplidar_sdk/releases>

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

Cambie al directorio `/sdk` y use el comando `make` para compilar. Los archivos compilados se encuentran en el directorio `/sdk/output`.

Cambie al directorio `/sdk/output/Linux/Release` y use el siguiente comando para ejecutar el programa de prueba:

```shell
./ultra_simple /dev/ttyS0
```

## Referencias y agradecimientos

- [Esquema eléctrico](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [Imagen del sistema operativo](https://rcn-ee.net/rootfs/debian-arm64/)
- [Código de prueba](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Problemas con la cape](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [Lidar láser](https://github.com/Slamtec/rplidar_sdk)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.