# Serie BeagleBone - Iniciación al BBAI

## Inicialización

En primer lugar, conecta la fuente de alimentación de 12V de la Cape y utiliza un módulo USB a serie para conectar el puerto serie en la placa (el puerto J3 se utiliza para depuración):

![](https://media.wiki-power.com/img/20211027164010.png)

Asegúrate de que el módulo USB a serie tenga los controladores instalados (yo usé un módulo FTDI, puedes descargar los controladores [aquí](https://ftdichip.com/drivers/vcp-drivers/)).

Utiliza una herramienta de línea de comandos para conectar al puerto serie (yo utilicé MobaXterm) y configura la velocidad de baudios a 115200.

## Instalación del paquete de parches

```shell
wget https://github.com/linyuxuanlin/File-host/blob/main/stash/k3-j721e-beagleboneai64.dtb?raw=true
```

Cambia el nombre del archivo a `k3-j721e-beagleboneai64.dtb`, muévelo a la carpeta `/boot` y sobrescribe el archivo original. (Subí el archivo a un repositorio de GitHub y lo obtuve utilizando el comando `wget`. Puede que necesites modificar el host de GitHub para que la descarga sea exitosa).

También puedes transferir el archivo directamente mediante SFTP.

## evtest

La herramienta de prueba de eventos (evtest) es una herramienta que imprime eventos del kernel evdev. Lee directamente de los dispositivos del kernel y muestra eventos con valores y nombres simbólicos de dispositivos, lo que la convierte en una herramienta útil para depurar dispositivos de entrada como ratones, teclados, touchpads, entre otros.

Descarga la herramienta evtest:

```shell
sudo apt install evtest
```

Usa la herramienta de la siguiente manera:

```shell
sudo evtest /dev/input/eventｘ（ｘ es el número de evento）
```

## Teclas

```shell
debian@BeagleBone:~$ evtest
No se especificó ningún dispositivo, intentando escanear todos los dispositivos en /dev/input/event*
Dispositivos disponibles:
/dev/input/event0:      gpio-keys
Selecciona el número de evento del dispositivo [0-0]: 0
La versión del controlador de entrada es 1.0.1
ID del dispositivo de entrada: bus 0x19, vendedor 0x1, producto 0x1, versión 0x100
Nombre del dispositivo de entrada: "gpio-keys"
Eventos admitidos:
  Tipo de evento 0 (EV_SYN)
  Tipo de evento 1 (EV_KEY)
    Código de evento 256 (BTN_0)
    Código de evento 257 (BTN_1)
    Código de evento 258 (BTN_2)
Manejo de repetición de teclas:
  Tipo de repetición 20 (EV_REP)
    Código de repetición 0 (REP_DELAY)
      Valor    250
    Código de repetición 1 (REP_PERIOD)
      Valor     33
Propiedades:
Pruebas ... (interrumpe para salir)
Evento: tiempo 1634868166.060258, tipo 1 (EV_KEY), código 257 (BTN_1), valor 1
Evento: tiempo 1634868166.060258, -------------- SYN_REPORT ------------
Evento: tiempo 1634868166.284257, tipo 1 (EV_KEY), código 257 (BTN_1), valor 0
Evento: tiempo 1634868166.284257, -------------- SYN_REPORT ------------
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
Presione CTRL-A Z para obtener ayuda sobre teclas especiales

hello
```

La prueba no fue exitosa, no se recibieron ni se enviaron datos.

## LEDs

```shell
cd /sys/class/leds && ls -l

echo 255 > beaglebone:green:cape0/brightness
echo 255 > beaglebone:green:cape3/brightness

echo 0 > beaglebone:green:cape1/brightness # No se apaga
```

## LIDAR láser

Si se recibe un mensaje de falta de permisos, consulte [**Habilitar la cuenta raíz con SSH**](https://wiki-power.com/BeagleBone%E7%B3%BB%E5%88%97-%E5%9F%BA%E6%9C%AC%E5%8F%82%E6%95%B0%E4%B8%8E%E7%8E%AF%E5%A2%83%E9%85%8D%E7%BD%AE#%E5%90%AF%E7%94%A8-ssh-%E7%9A%84-root-%E5%B8%90%E6%88%B7). Realice estos pasos con permisos de root.

Primero, active el LIDAR láser manipulando los GPIO.

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

Descargue la última SDK en: <https://github.com/Slamtec/rplidar_sdk/releases>

Realice modificaciones en el archivo `/sdk/sdk/src/hal/event.h` para una compilación correcta:

```shell
enum
     {
         EVENT_OK = 1,
-        EVENT_TIMEOUT = -1,
+        EVENT_TIMEOUT = 2,
         EVENT_FAILED = 0,
     };
```

````markdown
Dirígete a la carpeta `/sdk` y utiliza el comando `make` para compilar. Los archivos compilados se encontrarán en la carpeta `/sdk/output`.

Luego, navega hasta la carpeta `/sdk/output/Linux/Release` y ejecuta el siguiente comando para ejecutar el programa de prueba:

```shell
./ultra_simple /dev/ttyS0
```
````

## Referencias y Agradecimientos

- [Esquema de circuitos](file:///C:/Users/Power/Projects/Internship_at_Seeed/Projects/Robotics_Cape_Rev2/Reference/BeagleBone%20AI%20TDA4VM_SCH_V1.0_210805.pdf)
- [Imagen del sistema](https://rcn-ee.net/rootfs/debian-arm64/)
- [Código de prueba](https://gitee.com/gary87m/notes_seeed/blob/master/BBAI_Robotics%20Cape.md)
- [Problemas con Cape](https://docs.qq.com/sheet/DU1BBZnNORlJhRG5w)
- [SDK de LIDAR láser](https://github.com/Slamtec/rplidar_sdk)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

```


> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
```
