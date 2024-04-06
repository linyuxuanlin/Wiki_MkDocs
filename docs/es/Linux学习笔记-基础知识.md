# Apuntes de Estudio de Linux - Fundamentos

## Conexión a un Host Remoto

Para conectarte a un host remoto, puedes utilizar el comando `ssh` de la siguiente manera:

```shell
ssh usuario@IP
```

## Estructura del Directorio Raíz

![Estructura del directorio raíz](https://media.wiki-power.com/img/20211009094302.png)

| Directory   | Contents of the Directory                                                                                                                                                                                  |
| ----------- | ---------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| bin         | Directorio de archivos binarios que almacena comandos del sistema, como cat, cp, mkdir.                                                                                                                    |
| boot        | Contiene los archivos necesarios para el proceso de arranque, como el gestor de arranque grub2.                                                                                                            |
| dev         | Directorio de todos los archivos de dispositivos, como tarjetas de sonido, discos duros y unidades de CD/DVD.                                                                                              |
| etc         | "Etcétera", almacena los archivos de configuración principales del sistema.                                                                                                                                |
| home        | Directorio de almacenamiento de datos de los directorios de inicio de los usuarios.                                                                                                                        |
| lib         | Biblioteca, almacena archivos de biblioteca necesarios para los comandos de los directorios sbin y bin, evitando duplicaciones.                                                                            |
| lib32/lib64 | Contiene bibliotecas binarias que admiten arquitecturas de 32 y 64 bits.                                                                                                                                   |
| lost+found  | En sistemas EXT3/4, se generan archivos fragmentados en este directorio cuando el sistema se bloquea o se apaga de manera inesperada. El programa fsck verifica y repara los archivos dañados al arrancar. |
| media       | Utilizado para montar dispositivos como CD-ROM, disquetes y DVD.                                                                                                                                           |
| mnt         | Abreviatura de "mount" (montar), tiene la misma función que el directorio "media" y se utiliza para montar dispositivos de almacenamiento temporales.                                                      |
| opt         | Directorio para la instalación de software de terceros.                                                                                                                                                    |
| proc        | Almacena información sobre procesos y el kernel, no ocupa espacio en disco.                                                                                                                                |
| root        | Directorio de inicio del usuario "root".                                                                                                                                                                   |
| run         | Un sistema de archivos temporal que almacena información desde el inicio del sistema. Los archivos en este directorio deben eliminarse o limpiarse al reiniciar el sistema.                                |
| sbin        | "System bin", contiene comandos utilizados por el usuario "root", como el comando de formateo "mkfs".                                                                                                      |
| srv         | Almacena archivos de datos necesarios para algunos servicios de red.                                                                                                                                       |
| sys         | Similar al directorio "proc", se utiliza para registrar información sobre la CPU y el hardware del sistema.                                                                                                |
| tmp         | Directorio que almacena archivos temporales generados durante la ejecución de programas.                                                                                                                   |
| usr         | Directorio del sistema para almacenar programas, similar a la carpeta "Program Files" en Windows.                                                                                                          |
| var         | Directorio que almacena archivos que cambian con frecuencia, como registros del sistema.                                                                                                                   |

## Types of Files

En Linux, todo es un archivo.

Las extensiones de archivo comunes son las siguientes:

- Las extensiones .tar, .tar.gz, .tgz, .zip, .tar.bz indican archivos comprimidos, generalmente creados con comandos como tar, gzip o zip. La extensión en un archivo comprimido suele indicar el formato de compresión utilizado, lo que facilita la elección del comando a utilizar al descomprimir.
- .sh representa archivos de script de shell, que son programas desarrollados en lenguaje de shell.
- .pl representa archivos de lenguaje Perl, que son programas desarrollados en Perl.
- .py representa archivos de lenguaje Python, que son programas desarrollados en Python.
- .html, .htm, .php, .jsp, .do representan archivos de lenguaje web.
- .conf representa archivos de configuración de servicios del sistema.
- .rpm representa archivos de paquetes de instalación RPM.

Los archivos se dividen principalmente en los siguientes tipos:

### Archivos Normales

Incluyen archivos de texto, binarios, y más.

### Archivos Ejecutables

Incluyen scripts y aplicaciones que el sistema puede cargar y ejecutar, similares a los archivos de script .bat y programas .exe en Windows.

### Archivos de Enlace

Los archivos de enlace se dividen en enlaces duros y enlaces simbólicos:

- Un enlace duro se refiere a diferentes alias de un mismo archivo.
- Un enlace simbólico es similar a los accesos directos de Windows y, de hecho, es un tipo especial de archivo. En un enlace simbólico, el archivo es en realidad un archivo de texto que contiene información sobre la ubicación de otro archivo.

### Archivos de Directorio

En Linux, incluso los directorios son considerados archivos.

### Archivos de Dispositivo

Los dispositivos de hardware también se tratan como archivos. Al abrir el archivo del dispositivo correspondiente, se puede inicializar el dispositivo y, en algunos casos, controlar el hardware mediante lectura y escritura en el archivo del dispositivo.

## Permisos de Usuario y Archivo

### Permisos de Usuario

Linux es un sistema operativo multiusuario, y el usuario que tiene acceso a todos los recursos del sistema y la administración de otros usuarios y máquinas se llama usuario root. En Linux, cada usuario tiene un identificador único (UID) que se utiliza para identificar a un usuario del sistema. El usuario root tiene un UID de 0. Puede verificar el UID del usuario actual utilizando el comando `id`. Un usuario puede pertenecer a varios grupos (GID) para obtener diferentes permisos de archivo.

### Permisos de Archivo

Las propiedades de archivo en Linux se dividen en permisos de lectura, escritura y ejecución (cargar en la memoria y ejecutar un archivo) .

Puede modificar los permisos de un archivo utilizando el comando `chmod`.

## Línea de Comandos

### Símbolo del Terminal

Cuando abrimos una terminal, se muestra un símbolo como este:

```shell
power@Linuxbook:~$
```

Esto representa que el usuario actual es `power`, el nombre del host es `Linuxbook`, `~` indica que el directorio actual es el directorio de inicio (es decir, `/home/power`), y `$` es el símbolo del indicador de comandos, lo que significa que es un usuario normal. Si fuera un superusuario, sería `#`.

### Comandos

El formato básico de un comando (donde los dos últimos elementos son opcionales) es:

```shell
comando [-opciones] [argumento]
```

Puede utilizar la tecla `Tab` para autocompletar y `Ctrl` + `C` para detener la ejecución en la línea de comandos.

- comando: el nombre del comando, como `cd` o `ls`.
- -opciones: opciones adicionales del comando, como `ls -l`. Las opciones hacen que el comando realice diferentes acciones específicas.
- argumento: un argumento para el comando, como `/home` en `cd /home`.

Algunos comandos comunes son:

- `ls`: Listado de directorios y nombres de archivos

  - `-a`: Mostrar archivos ocultos (los que tienen un punto `.` antes del nombre)
  - `-l`: Listar detalladamente información sobre el tipo de archivo, permisos, propietario y tamaño
  - `-t`: Listar en orden de creación
  - `-A`: Igual que `-a`, pero sin incluir `.` y `..` (directorio actual y directorio padre)
  - `-R`: Si hay archivos en el directorio, se listarán los archivos de ese directorio, es decir, se mostrará de forma recursiva.

- `cd`: Cambiar de directorio

  - Rutas especiales
    - `~`: Directorio raíz del usuario actual
    - `/`: Directorio raíz
    - `.`: Directorio actual
    - `..`: Directorio superior
    - `-`: Cambiar al último directorio al que se accedió con `cd`

- `pwd`: Mostrar el directorio actual

- `mkdir`: Crear directorios

  - `-p`: Crear directorios que no existen en la jerarquía especificada

- `rmdir`: Eliminar un directorio vacío

- `touch`: Crear archivos

- `cp`: Copiar archivos o directorios

- `rm`: Eliminar archivos o directorios

  - `-r`: Eliminar directorios y su contenido
  - `-f`: Forzar la eliminación

- `mv`: Mover archivos o directorios o cambiar el nombre de archivos y directorios

- `cat`: Ver el contenido de un archivo

- `echo`: Mostrar texto en la terminal

- Redireccionar la salida a un archivo: Guardar el resultado de un comando en un archivo

  - `comando > nombre_archivo`: Crear el archivo si no existe, sobrescribirlo si existe
  - `comando >> nombre_archivo`: Crear el archivo si no existe, agregar al final si existe

- `sudo`: Cambiar al usuario root para ejecutar comandos que requieren permisos de administrador. Si un comando falla debido a la falta de permisos mientras se ejecuta como usuario normal, se puede utilizar `sudo !!` para ejecutar el último comando con privilegios de root.

- `clear`: Limpiar la pantalla de la terminal

- `reboot` / `poweroff`: Reiniciar / Apagar el sistema

## Gestión de paquetes

La gestión de paquetes se refiere a la instalación de software mediante comandos. En sistemas operativos Linux, los dos tipos de paquetes más comunes son deb y rpm.

## Referencias y Agradecimientos

- [Tutorial de Linux](https://www.runoob.com/linux/linux-tutorial.html)
- [Guía práctica de desarrollo de Linux i.MX](https://doc.embedfire.com/linux/imx6/base/zh/latest/index.html)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
