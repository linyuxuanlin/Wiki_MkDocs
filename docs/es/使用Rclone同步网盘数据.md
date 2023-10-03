# Sincronización de datos en la nube con Rclone

Rclone es una herramienta de línea de comandos para administrar archivos en la nube, compatible con más de 40 servicios de almacenamiento en la nube (incluyendo S3). Rclone también cuenta con una interfaz gráfica de usuario llamada RcloneBrowser, que facilita su uso para los usuarios comunes. En este artículo se explica cómo sincronizar datos en la nube de Tencent Cloud Object Storage mediante Rclone.

## Instalación del software

- [**Rclone**](https://rclone.org/downloads/): Después de descargarlo, descomprima el archivo `.exe` y tome nota de la ruta.
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases): Herramienta GUI. Después de instalarla, seleccione la ruta de Rclone.
- ([**WinFsp**](http://www.secfs.net/winfsp/rel/): Biblioteca de dependencias, necesaria para montar discos virtuales)

## Proceso de configuración

Abra RcloneBrowser y haga clic en `Config...` en la esquina inferior izquierda. A continuación, siga las instrucciones para ingresar:

Ingrese `n` para crear una nueva conexión remota:

```shell
Name                 Type
====                 ====
rclone config        s3
e) Edit existing remote
n) New remote
d) Delete remote
r) Rename remote
c) Copy remote
s) Set configuration password
q) Quit config

e/n/d/r/c/s/q> n
```

Asigne un nombre a la conexión remota (por ejemplo, `test`):

```shell
name> test
```

Seleccione el proveedor de servicios (en este ejemplo, se utiliza Tencent Cloud Object Storage, seleccione `4`):

```shell
Choose a number from below, or type in your own value
 1 / 1Fichier
   \ "fichier"
 2 / Alias for an existing remote
   \ "alias"
 3 / Amazon Drive
   \ "amazon cloud drive"
 4 / Amazon S3 Compliant Storage Providers including AWS, Alibaba, Ceph, Digital Ocean, Dreamhost, IBM COS, Minio, and Tencent COS
   \ "s3"
...

Storage> 4
```

```shell
Choose a number from below, or type in your own value
 1 / Amazon Web Services (AWS) S3
   \ "AWS"
 2 / Alibaba Cloud Object Storage System (OSS) formerly Aliyun
   \ "Alibaba"
 3 / Ceph Object Storage
   \ "Ceph"
 4 / Digital Ocean Spaces
   \ "DigitalOcean"
 5 / Dreamhost DreamObjects
   \ "Dreamhost"
 6 / IBM COS S3
   \ "IBMCOS"
 7 / Minio Object Storage
   \ "Minio"
 8 / Netease Object Storage (NOS)
   \ "Netease"
 9 / Scaleway Object Storage
   \ "Scaleway"
10 / StackPath Object Storage
   \ "StackPath"
11 / Tencent Cloud Object Storage (COS)
   \ "TencentCOS"
12 / Wasabi Object Storage
   \ "Wasabi"
13 / Any other S3 compatible provider
   \ "Other"

Español:

```

Seleccione el tipo de autenticación. Como es la primera vez que se configura, seleccione `1`:

```shell
Elija un número de la siguiente lista o escriba su propio valor
 1 / Ingrese las credenciales de AWS en el siguiente paso
   \ "false"
 2 / Obtenga las credenciales de AWS del entorno (variables de entorno o IAM)
   \ "true"

env_auth> 1
```

Ingrese la cuenta del servicio en la nube, que es equivalente a SecretId de Tencent Cloud COS:

```shell
ID de clave de acceso de AWS.

access_key_id> ******
```

Ingrese la contraseña, que es equivalente a SecretKey:

```shell
AWS Secret Access Key (contraseña)

secret_access_key> ******
```

Seleccione la región del servicio en la nube:

```shell
Endpoint para la API de Tencent COS.
 1 / Región de Beijing.
   \ "cos.ap-beijing.myqcloud.com"
 2 / Región de Nanjing.
   \ "cos.ap-nanjing.myqcloud.com"
 3 / Región de Shanghai.
   \ "cos.ap-shanghai.myqcloud.com"
 4 / Región de Guangzhou.
   \ "cos.ap-guangzhou.myqcloud.com"
...

endpoint> 4
```

Seleccione el tipo de lectura y escritura, generalmente es lectura pública y escritura privada para la plataforma de imágenes:

```shell
ACL predefinido utilizado al crear buckets y almacenar o copiar objetos.
 1 / El propietario obtiene CONTROL_TOTAL. Nadie más tiene derechos de acceso (predeterminado).
   \ "default"
 2 / El propietario obtiene CONTROL_TOTAL. El grupo AllUsers obtiene acceso de LECTURA.
   \ "public-read"
   / El propietario obtiene CONTROL_TOTAL. El grupo AllUsers obtiene acceso de LECTURA y ESCRITURA.
...

acl> 2
```

Seleccione el tipo de almacenamiento (seleccione `1` por defecto):

```shell
La clase de almacenamiento que se utilizará al almacenar objetos nuevos en Tencent COS.
 1 / Predeterminado
   \ ""
 2 / Clase de almacenamiento estándar
   \ "STANDARD"
 3 / Modo de almacenamiento de archivo.
   \ "ARCHIVE"
 4 / Modo de almacenamiento de acceso poco frecuente.
   \ "STANDARD_IA"

storage_class> 1
```

¿Desea editar la configuración avanzada? (seleccione `n` para no):

```shell
¿Editar la configuración avanzada? (s/n)
y) Sí
n) No (predeterminado)

y/n> n
```

Finalmente, confirme y escriba `y` después de verificar que todo es correcto:

Configuración remota
--------------------
[Txcos]
type = s3
provider = TencentCOS
env_auth = false
access_key_id = 我是马赛克
secret_access_key = 我是马赛克
endpoint = cos.ap-guangzhou.myqcloud.com
acl = public-read
--------------------
y) Sí, esto está bien (predeterminado)
e) Editar esta conexión remota
d) Eliminar esta conexión remota
y/e/d> y
```

Ingrese `q` para salir:

```shell
Conexiones remotas actuales:

Nombre                 Tipo
====                 ====
Txcos                 s3

e) Editar conexión remota existente
n) Nueva conexión remota
d) Eliminar conexión remota
r) Renombrar conexión remota
c) Copiar conexión remota
s) Establecer contraseña de configuración
q) Salir de la configuración
e/n/d/r/c/s/q> q
```

A continuación, abra la conexión remota configurada haciendo doble clic, seleccione la carpeta y haga clic en `Descargar` para descargarla en su dispositivo local. En la ventana emergente, seleccione la siguiente configuración:

- Seleccione el modo `Copiar` (sincronización unidireccional desde la nube al dispositivo local), solo copie los archivos nuevos y modificados para hacer una copia de seguridad.
- Marque la casilla `Omitir todos los archivos que existen` en la zona de omisión de archivos para evitar la descarga repetida y el consumo de datos.
- En la zona de descripción de tareas, escriba el nombre de la tarea para facilitar la sincronización la próxima vez.

Una vez que haya terminado de configurar, cambie a la pestaña `Tareas`, seleccione la tarea correspondiente y haga clic en `Ejecutar` para comenzar la descarga.

## Configuración en un NAS Synology

Nota: se recomienda utilizar CloudSync en Synology y no modificar el código subyacente.

Preparación:

- Habilitar SSH
- Habilitar la carpeta de inicio del usuario (`homes`)
- Crear una carpeta para la sincronización (por ejemplo, `/volume1/wiki-media`)

Instale Rclone:

```shell
curl https://rclone.org/install.sh | sudo bash
```

Configure el servicio:

```shell
rclone config
```

Siga los pasos anteriores.

Comando de sincronización:

```shell
# De local a la nube
rclone [opciones de función] <ruta local> <nombre de la conexión remota:ruta> [parámetros] [parámetros] ...

# De la nube a local
rclone [opciones de función] <nombre de la conexión remota:ruta> <ruta local> [parámetros] [parámetros] ...

# De la nube a la nube
rclone [opciones de función] <nombre de la conexión remota:ruta> <nombre de la conexión remota:ruta> [parámetros] [parámetros] ...
```

Por ejemplo, en mi caso:

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

Cree un script de automatización en la ruta seleccionada (por ejemplo, `rclone-sync.sh`) y agregue el comando anterior al archivo del script.

En Synology, vaya a `Panel de control` - `Programador de tareas` - `Nueva` - `Tarea programada` - `Script definido por el usuario` y configure la hora de ejecución periódica y la ruta del script.

1. En la pestaña `Tarea programada` y `Configuración de la tarea`, configure la hora de ejecución periódica y el comando para ejecutar el script (por ejemplo, `bash /volume1/stash/permanent/rclone-sync.sh`).
2. En la pestaña `Configuración`, configure la salida de resultados y seleccione la tarea. Haga clic en `Ejecutar` para probar la ejecución y abra la ruta de salida configurada para ver los resultados.

## Referencias y agradecimientos

- [Tutorial de instalación, configuración y uso de Rclone, con explicación detallada de los parámetros más utilizados](https://www.wazhuji.com/jiaocheng/17.html)
- [Creación de una nube privada de bajo costo y con todas las funciones basada en almacenamiento de objetos](https://zhuanlan.zhihu.com/p/104628740)
- [Montar Alibaba Cloud OSS / Tencent Cloud COS como disco de Windows utilizando Rclone y WinFsp](https://www.boxmoe.com/486.html)
- [Montar Google Drive personal / de equipo en Windows utilizando Rclone](https://blog.rhilip.info/archives/874/)
- [Realizar copias de seguridad diarias programadas del contenido del sitio web y la base de datos de Typecho en Google Drive / Onedrive y otros servicios de almacenamiento en la nube utilizando Rclone](https://omo.moe/archives/616/)

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.