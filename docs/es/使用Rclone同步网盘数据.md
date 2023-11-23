# Sincronización de datos en la nube con Rclone

Rclone es una herramienta de línea de comandos para gestionar archivos en la nube, compatible con más de 40 proveedores de almacenamiento en la nube (incluyendo S3). Rclone también cuenta con una interfaz gráfica llamada RcloneBrowser, que facilita su uso para usuarios generales. En este artículo se explica cómo sincronizar datos con Tencent Cloud Object Storage utilizando Rclone.

## Instalación del software

- [**Rclone**](https://rclone.org/downloads/): Descarga el archivo `.exe` y descomprímelo, luego guarda la ruta.
- [**RcloneBrowser**](https://github.com/kapitainsky/RcloneBrowser/releases): Herramienta gráfica. Después de instalarla, selecciona la ruta de Rclone.
- (Opcional) [**WinFsp**](http://www.secfs.net/winfsp/rel/): Biblioteca de dependencia, necesaria si deseas montar un disco virtual.

## Proceso de configuración

Abre RcloneBrowser y haz clic en `Config...` en la esquina inferior izquierda. A continuación, sigue las instrucciones:

Ingresa `n` para crear una nueva conexión remota:

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

Asigna un nombre a la conexión remota (por ejemplo, `test`):

```shell
name> test
```

Selecciona el proveedor de servicios (en este ejemplo, usaré Tencent Cloud Object Storage, selecciona `4`):

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
```

proveedor> 11
```

Selecciona el tipo de autenticación. Como es la primera vez que se configura, elige `1`:

```shell
Elige un número de la lista o escribe tu propio valor
 1 / Ingresa las credenciales de AWS en el siguiente paso
   \ "false"
 2 / Obtén las credenciales de AWS del entorno (variables de entorno o IAM)
   \ "true"

env_auth> 1
```

Ingresa la cuenta del servicio en la nube, esto sería equivalente a SecretId de Tencent COS:

```shell
AWS Access Key ID.

access_key_id> ******
```

Ingresa la contraseña, equivalente a SecretKey:

```shell
AWS Secret Access Key (password)

secret_access_key> ******
```

Selecciona la región del servicio en la nube:

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

Selecciona el tipo de lectura y escritura, generalmente para un repositorio de imágenes se utiliza lectura pública y escritura privada:

```shell
Canned ACL utilizado al crear buckets y almacenar o copiar objetos.
 1 / El propietario tiene control total. Nadie más tiene derechos de acceso (por defecto).
   \ "default"
 2 / El propietario tiene control total. El grupo AllUsers tiene acceso de lectura.
   \ "public-read"
   / El propietario tiene control total. El grupo AllUsers tiene acceso de lectura y escritura.
...

acl> 2
```

Selecciona el tipo de almacenamiento (puedes elegir `1` por defecto):

```shell
La clase de almacenamiento a utilizar al almacenar nuevos objetos en Tencent COS.
 1 / Por defecto
   \ ""
 2 / Clase de almacenamiento estándar
   \ "STANDARD"
 3 / Modo de almacenamiento de archivo.
   \ "ARCHIVE"
 4 / Modo de almacenamiento de acceso poco frecuente.
   \ "STANDARD_IA"

storage_class> 1
```

¿Deseas editar la configuración avanzada? (elige `n` para no):

```shell
¿Editar configuración avanzada? (s/n)
s) Sí
n) No (por defecto)

s/n> n
```

Finalmente, confirma y verifica que todo esté correcto ingresando `y`:

```shell
Configuración remota

[Txcos]
type = s3
provider = TencentCOS
env_auth = false
access_key_id = 我是马赛克
secret_access_key = 我是马赛克
endpoint = cos.ap-guangzhou.myqcloud.com
acl = public-read

y) Sí, está bien (por defecto)
e) Editar esta configuración remota
d) Eliminar esta configuración remota
y/e/d> y
```

Ingresa `q` para salir:

```shell
Remotos actuales:

Nombre                 Tipo
====                 ====
Txcos                 s3

e) Editar remoto existente
n) Nuevo remoto
d) Eliminar remoto
r) Renombrar remoto
c) Copiar remoto
s) Establecer contraseña de configuración
q) Salir de la configuración
e/n/d/r/c/s/q> q
```

A continuación, abre la conexión remota configurada haciendo doble clic, selecciona la carpeta y haz clic en `Descargar` para descargarla localmente. En la ventana emergente, elige la siguiente configuración:

- Selecciona el modo `Copia` (sincronización unidireccional desde la nube hasta local) para copiar solo los archivos nuevos y modificados, útil para realizar copias de seguridad.
- Marca la opción `Omitir todos los archivos existentes` en la sección "Omitir archivos" para evitar descargas repetidas y ahorrar ancho de banda.
- En la sección "Descripción de la tarea", ingresa un nombre para la tarea para facilitar su uso en futuras sincronizaciones.

Una vez completada la configuración, ve a la pestaña "Tareas", selecciona la tarea correspondiente y haz clic en `Ejecutar` para iniciar la descarga.

## Configuración en un NAS Synology

Nota: Se recomienda utilizar CloudSync en un NAS Synology y no realizar modificaciones en el código subyacente.

Preparativos:

- Habilitar SSH
- Activar directorios de usuario (`homes`)
- Crear una carpeta para la sincronización (por ejemplo, `/volume1/wiki-media`)

Instalar Rclone:

```shell
curl https://rclone.org/install.sh | sudo bash
```

Configurar el servicio:

```shell
rclone config
```

Sigue los pasos anteriores.

Comandos de sincronización:

```shell
# De local a la nube
rclone [opciones de función] <ruta local> <nombre remoto:ruta> [parámetros] [parámetros] ...

# De la nube a local
rclone [opciones de función] <nombre remoto:ruta> <ruta local> [parámetros] [parámetros] ...

# De la nube a la nube
rclone [opciones de función] <nombre remoto:ruta> <nombre remoto:ruta> [parámetros] [parámetros] ...
```

Por ejemplo, en mi caso:

```shell
rclone sync COS_backup:/wiki-media-1253965369 /volume1/wiki-media -P
```

Crea un script de automatización en la ruta seleccionada (por ejemplo, `rclone-sync.sh`) y coloca el comando anterior en el archivo del script.

En el panel de control de Synology, ve a `Tareas programadas` > `Crear` > `Tarea programada` > `Script definido por el usuario` y configura el tiempo de ejecución periódica en las pestañas "Programa" y "Configuración de la tarea", junto con el comando para ejecutar el script (por ejemplo, `bash /volume1/stash/permanent/rclone-sync.sh`).

Puedes configurar la salida de resultados en la sección "Configuración" y luego seleccionar la tarea y hacer clic en `Ejecutar` para probar la ejecución y abrir la ruta de salida configurada para ver los resultados.

## Referencias y agradecimientos

- [Tutorial de instalación, configuración y uso de Rclone, con explicación detallada de los parámetros más comunes](https://www.wazhuji.com/jiaocheng/17.html)
- [Creación de una nube privada de bajo costo y con todas las funciones basada en [almacenamiento de objetos]](https://zhuanlan.zhihu.com/p/104628740)
- [Montar Alibaba Cloud OSS / Tencent Cloud COS como disco en Windows utilizando Rclone y WinFsp](https://www.boxmoe.com/486.html)
- [Montar Google Drive personal / de equipo en Windows utilizando Rclone](https://blog.rhilip.info/archives/874/)
- [Realizar copias de seguridad diarias programadas de contenido y base de datos de un sitio web de Typecho en Google Drive/OneDrive u otros servicios de almacenamiento en la nube utilizando Rclone](https://omo.moe/archives/616/)'

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.