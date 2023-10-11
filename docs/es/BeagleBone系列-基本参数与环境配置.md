# Serie BeagleBone - Parámetros básicos y configuración del entorno

## Recursos de hardware

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211008090724.png)

- USB tipo A: se utiliza como modo de host USB
- USB Micro: alimenta la placa y actúa como esclavo
- LEDs
  - D2: parpadea como un latido al arrancar
  - D3: se enciende al leer/escribir datos en la tarjeta SD
  - D4: se enciende cuando la CPU está activa
  - D5: se enciende al leer/escribir en la memoria eMMC
- Botones de arranque/usuario: si hay una tarjeta SD, se iniciará desde ella por defecto (el mismo resultado se obtiene de cualquier manera). Después del arranque, actúa como un botón normal conectado a GPIO_72.
- Interfaz I2C Grove: conectado a I2C2
- Interfaz Uart Grove: conectado a UART2
- Depuración en serie: conectado a UART0, el pin cerca del USB es el pin1, y los pines del 1 al 6 son: GND, NC, NC, RX, TX, NC.

## Configuración del entorno

### Problemas de instalación de controladores

En Windows 10 y versiones posteriores, se utiliza por defecto la firma de controladores obligatoria, lo que puede ser la causa de la falla en la instalación de controladores.

Solución:

- Mantenga presionada la tecla `shift` y haga clic en reiniciar la computadora.
- Ingrese a `Solución de problemas` - `Opciones avanzadas` - `Configuración de inicio` y haga clic en `Reiniciar`.
- Después del reinicio, siga las instrucciones de la página y presione la tecla `7` en el teclado para deshabilitar la firma de controladores obligatoria.
- Después del inicio, se pueden instalar los controladores de BeagleBone normalmente.

### Descarga e instalación de imágenes

Dirección de descarga de imágenes oficiales: https://beagleboard.org/latest-images  
Herramienta de grabación: https://sourceforge.net/projects/win32diskimager/files/latest/download

Grabe la imagen en la tarjeta SD, desconecte la alimentación e inserte la tarjeta SD en BeagleBone. La próxima vez que se encienda, el sistema se iniciará desde la tarjeta SD.

## Acceso mediante herramientas de línea de comandos

### Acceso mediante puerto serie

Conecte el puerto serie integrado en la placa mediante un convertidor USB a serie y abra una herramienta de serie en la computadora (como WindTerm) para conectarse. (El nombre de usuario y la contraseña predeterminados son `root`).

La velocidad de transmisión es de 115200.

### Acceso mediante Ethernet

En la conexión serie, use el comando `ifconfig` para encontrar la dirección Ethernet y conectarse a ella mediante la dirección. El nombre de usuario es `debian` y la contraseña es `temppwd`.

### Acceso mediante USB

usb0: 192.168.7.2  
usb1: 192.168.6.2

Conéctese mediante SSH, el nombre de usuario es `debian` y la contraseña es `temppwd`.

## Habilitar la cuenta root con SSH

```shell
vi /etc/ssh/sshd_config
```

Cambie `#PermitRootLogin prohibit-password` a `PermitRootLogin yes`.

## Controlador Seeed OLED (SSD1306, I2C, 12864)

Descargue el paquete smbus2 con pip3:

```py
sudo apt-get install python3-pip
pip3 install smbus2
```

El programa se puede encontrar en [**Grove - OLED Display 0.96 inch**](https://wiki.seeedstudio.com/Grove-OLED_Display_0.96inch/#play-with-beaglebone-green).

## Referencias y agradecimientos

- [Problemas en la depuración de Beaglebone black 4G](https://blog.csdn.net/qq_32543253/article/details/53536266)
- [Proyecto](https://beagleboard.org/p)
- [Actualiza el software de tu Beagle](https://beagleboard.org/upgrade#connect)
- [Firmware de prueba](http://plm.seeedstudio.com.cn:9002/Windchill/app/#ptc1/tcomp/infoPage?oid=VR%3Awt.doc.WTDocument%3A30844361&u8=1)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
