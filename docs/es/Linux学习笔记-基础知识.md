# Notas de estudio de Linux - Conocimientos básicos

## Conexión a un host remoto

Usando ssh:

```shell
ssh usuario@IP
```

## Estructura del directorio raíz

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20211009094302.png)

| Directorio  | Contenido del directorio                                                                                                                                                                            |
| ----------- | --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bin         | Archivos binarios, donde se almacenan los comandos del sistema, como cat, cp, mkdir.                                                                                                                |
| boot        | Contiene los archivos necesarios para el proceso de arranque, como el gestor de arranque grub2.                                                                                                     |
| dev         | Directorio que contiene todos los archivos de dispositivos, como tarjetas de sonido, discos duros, unidades de CD/DVD.                                                                              |
| etc         | Directorio que contiene los archivos de configuración principales del sistema.                                                                                                                      |
| home        | Directorio donde se almacenan los datos de los usuarios.                                                                                                                                            |
| lib         | Biblioteca, donde se almacenan los archivos de biblioteca necesarios para los comandos en los directorios sbin y bin, para evitar duplicados.                                                       |
| lib32/lib64 | Directorios que contienen bibliotecas de funciones binarias, compatibles con 32/64 bits.                                                                                                            |
| lost+found  | En sistemas EXT3/4, cuando el sistema se bloquea o se apaga inesperadamente, se generan algunos archivos fragmentados en este directorio. El comando fcsk los revisa y repara los archivos dañados. |
| media       | Directorio utilizado para montar dispositivos como CD, DVD, disquetes, etc.                                                                                                                         |
| mnt         | Directorio utilizado para montar dispositivos de almacenamiento temporalmente.                                                                                                                      |
| opt         | Directorio donde se instalan aplicaciones de terceros.                                                                                                                                              |
| proc        | Directorio donde se almacena información del proceso y del kernel, no ocupa espacio en disco.                                                                                                       |
| root        | Directorio de inicio del usuario root.                                                                                                                                                              |
| run         | Es un sistema de archivos temporal, donde se almacena información desde el inicio del sistema. Cuando se reinicia el sistema, los archivos de este directorio deben eliminarse o limpiarse.         |
| sbin        | Binarios del sistema, donde se almacenan los comandos que utiliza el usuario root, como el comando de formato mkfs.                                                                                 |
| srv         | Directorio que contiene archivos de datos necesarios para algunos servicios de red.                                                                                                                 |
| sys         | Al igual que el directorio proc, se utiliza para registrar información relacionada con la CPU y el hardware del sistema.                                                                            |
| tmp         | Directorio donde se almacenan los archivos temporales generados durante la ejecución de programas.                                                                                                  |
| usr         | Directorio donde se almacenan los programas del sistema, similar a la carpeta programefiles en Windows.                                                                                             |
| var         | Directorio donde se almacenan los archivos que cambian con frecuencia, como los archivos de registro del sistema.                                                                                   |

## Tipos de archivos

En Linux, todo es un archivo.

Las extensiones de archivo comunes son las siguientes:

- Los sufijos .tar, .tar.gz, .tgz, .zip, .tar.bz indican archivos comprimidos, y los comandos de creación suelen ser tar, gzip, zip, etc. El sufijo en el archivo comprimido generalmente indica el formato de compresión utilizado para empaquetarlo, lo que facilita la selección del comando a utilizar para descomprimirlo.
- .sh indica un archivo de script de shell, un programa desarrollado en lenguaje shell.
- .pl indica un archivo de lenguaje Perl, un programa desarrollado en lenguaje Perl.
- .py indica un archivo de lenguaje Python, un programa desarrollado en lenguaje Python.
- .html, .htm, .php, .jsp, .do indican archivos de lenguaje web.
- .conf indica archivos de configuración de servicios del sistema.
- .rpm indica archivos de paquetes de instalación RPM.

Los archivos tienen principalmente los siguientes tipos:

### Archivos normales

Archivos de texto, binarios, etc.

### Archivos ejecutables

Incluyen scripts y aplicaciones, estos archivos pueden ser cargados y ejecutados por el sistema, similares a los archivos de script bat y los archivos de programa exe en Windows.

### Archivos de enlace

Los archivos de enlace se dividen en enlaces duros y enlaces simbólicos:

- Los enlaces duros se refieren a diferentes nombres para el mismo archivo.
- Los enlaces simbólicos son similares a los accesos directos de Windows. En realidad, es un archivo especial. En el enlace simbólico, el archivo es en realidad un archivo de texto que contiene información sobre la ubicación de otro archivo.

### Archivos de directorio

En Linux, los directorios también son archivos.

### Archivos de dispositivo

Los dispositivos de hardware también son archivos, se pueden inicializar a través de los archivos de dispositivo correspondientes, y algunos dispositivos también se pueden controlar mediante la lectura y escritura de archivos de dispositivo.

## Usuarios y permisos de archivo

### Permisos de usuario

Linux es un sistema operativo multiusuario, donde los usuarios que tienen acceso a todos los recursos de otros usuarios y computadoras se llaman cuentas de root. En Linux, cada usuario tiene un número de identificación único (UID) para identificar a un usuario del sistema. El UID de la cuenta root es el número 0. Podemos usar el comando `id` para ver el valor UID del usuario actual. Un usuario puede pertenecer a varios GID (grupos) para obtener diferentes permisos de archivo.

### Permisos de archivo

Las propiedades de archivo de Linux se dividen en permisos de lectura, escritura y ejecución (archivos que se pueden cargar en la memoria y ejecutar por el sistema operativo).

Los permisos de archivo se pueden modificar mediante el comando `chmod`.

## Línea de comandos

### Indicador de terminal

Cuando abrimos una terminal, aparece una cadena de indicadores como:

```shell
power@Linuxbook:~$
```

Esto representa que el usuario actual es `power`, el nombre del host en ejecución es `Linuxbook`, `~` representa el directorio actual es el directorio de inicio (es decir, `/home/power`), y `$` es el indicador de comando, lo que indica que es un usuario normal. Si es un usuario superusuario, será `#`.

### Comandos

El formato básico de un comando (los dos últimos elementos son opcionales) es:

```shell
command [-options] [argument]
```

Puede usar la tecla `Tab` para completar automáticamente y `Ctrl` + `C` para detener la ejecución en la línea de comandos.

- command: nombre del comando, como `cd`, `ls`, etc.
- -options: opciones adicionales del comando, como `ls -l`. El comando realizará diferentes operaciones según las opciones específicas.
- argument: argumento del comando, como en `cd /home`, `/home` es el nombre del argumento.

Los comandos comunes son:

- `ls`: Lista los nombres de los archivos y directorios
  - `-a`: Muestra los archivos ocultos (nombres de archivo que comienzan con `.`)
  - `-l`: Muestra información detallada sobre el tipo de archivo, permisos, propietario, tamaño, etc.
  - `-t`: Lista los archivos en orden cronológico de creación
  - `-A`: Igual que `-a`, pero no muestra `.` y `..` (directorio actual y directorio padre)
  - `-R`: Si hay archivos en el directorio, también se listarán los archivos en ese directorio, es decir, se mostrarán de forma recursiva.
- `cd`: Cambia de directorio
  - Rutas especiales
    - `~`: Directorio home del usuario actual
    - `/`: Directorio raíz
    - `.`: Directorio actual
    - `..`: Directorio superior
    - `-`: Cambia al directorio anterior al último `cd`
- `pwd`: Muestra el directorio actual
- `mkdir`: Crea un directorio
  - `-p`: Crea directorios en caso de que no existan
- `rmdir`: Elimina un directorio vacío
- `touch`: Crea un archivo
- `cp`: Copia archivos o directorios
- `rm`: Elimina archivos o directorios
  - `-r`: Elimina todos los subdirectorios y archivos dentro del directorio
  - `-f`: Elimina forzosamente
- `mv`: Mueve archivos o directorios, o cambia el nombre de archivos o directorios
- `cat`: Muestra el contenido de un archivo
- `echo`: Muestra el contenido en la terminal
- Redireccionamiento de salida a un archivo: Guarda el resultado de un comando en un archivo
  - `comando > nombre_archivo`, si el archivo no existe, se creará, si ya existe, se sobrescribirá
  - `comando >> nombre_archivo`, si el archivo no existe, se creará, si ya existe, se agregará al final
- `sudo`: Switch user do, agrega `sudo` antes de un comando que requiere permisos de root para que el usuario actual obtenga permisos de root y ejecute el comando. Si el usuario normal no tiene permisos y falla la ejecución, se puede usar `sudo !!` para volver a ejecutar el último comando con permisos.
- `clear`: Limpia la pantalla
- `reboot`/`poweroff`: Reinicia / Apaga el sistema

## Gestión de paquetes

La gestión de paquetes es el uso de comandos para instalar software. En el sistema operativo Linux, los dos tipos de paquetes más comunes son deb y rpm.

## Referencias y agradecimientos

- [Tutorial de Linux](https://www.runoob.com/linux/linux-tutorial.html)
- [[Wildfire] Guía práctica de desarrollo de Linux i.MX](https://doc.embedfire.com/linux/imx6/base/zh/latest/index.html)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
