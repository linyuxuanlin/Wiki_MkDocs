# Ejecutar VS Code en el navegador (antiguo)

Nota: Para la implementación de code-server v3.8.0 o superior, consulte [**Cómo ejecutar VS Code en iPad**](https://wiki-power.com/es/如何在iPad上运行VSCode) para obtener un método más simple.

## Antecedentes

Como se sabe, VS Code es un editor muy potente. Si se pudiera usar VS Code en plataformas ligeras como el iPad (el soporte de teclado y ratón de iPadOS ya es comparable al de los sistemas de escritorio), podríamos trabajar en cualquier momento y lugar.

Afortunadamente, hay un servicio que permite ejecutar VS Code en un servidor: code-server. Después de la implementación, se puede acceder a él a través del navegador. De esta manera, cualquier dispositivo puede usar VS Code fácilmente siempre que tenga una conexión a Internet.

## Preparar el entorno

Un servidor con Linux instalado (utilicé la máquina de estudiante de menor especificación de Alibaba Cloud).

Los requisitos oficiales son los siguientes:

> - Host de 64 bits.
> - Al menos 1 GB de RAM.
> - Se recomiendan 2 núcleos o más (1 núcleo funciona pero no de manera óptima).
> - Conexión segura a través de HTTPS o localhost (requerido para los trabajadores de servicio y el soporte de portapapeles).
> - Para Linux: GLIBC 2.17 o posterior y GLIBCXX 3.4.15 o posterior.

## Proceso de instalación

### 1. Descargar

```shell
wget https://github.com/cdr/code-server/releases/download/3.1.0/code-server-3.1.0-linux-x86_64.tar.gz # Descargar code-server
```

No copie el comando directamente, copie el enlace de la última versión en la página de [**Release**](https://github.com/cdr/code-server/releases) de code-server (seleccione según la arquitectura del servidor, yo utilicé la versión `code-server-3.1.0-linux-x86_64.tar.gz`), y descargue o transfiera al servidor con `wget` o `SFTP`.

Si la velocidad de descarga es lenta, puede copiar el enlace de descarga y utilizar el sitio web [**GitHub 文件加速**](https://gh.api.99988866.xyz/) para obtener un enlace de descarga acelerado en China.

```shell
tar -xvf code-server-3.1.0-linux-x86_64.tar.gz # Descomprimir
```

### 2. Instalar

```shell
cd code-server
export PASSWORD="yourpassword"
./code-server --port 8888 --host 0.0.0.0
```

- Cambie `yourpassword` a su propia contraseña, de lo contrario se generará una contraseña aleatoria.
- `--port 8888` significa especificar el puerto de ejecución. Puede configurarlo en el puerto `80` (protocolo Http) para que no tenga que agregar el número de puerto al acceder.
- `--host 0.0.0.0` permite que el servicio sea accesible desde Internet. El valor predeterminado `127.0.0.1` solo permite el acceso local.
- Si no necesita autenticación de contraseña, puede agregar `--auth none`.
- Si el servicio no se inicia correctamente, es posible que haya seleccionado la **versión de arquitectura del procesador** incorrecta. Simplemente cambie a otra versión.

### 3. Configurar la ejecución en segundo plano

Por defecto, si se ejecuta directamente, se cerrará cuando se desconecte la conexión ssh. Para que se ejecute en segundo plano, puede usar `screen`:

```shell
yum install screen
o
apt-get install screen
```

```shell
screen -S VSCode-online # VS Code-online es el nombre que elija
export PASSWORD="password" && ./code-server --port 8888 --host 0.0.0.0
```

Para volver a la tarea en ejecución de la pantalla:

```shell
screen -r nombre de la tarea
```

Si necesita detener la ejecución en segundo plano de screen:

```shell
screen -ls # Ver el ID del servicio en ejecución
screen -X -S id quit # Reemplazar id
```

Salir de screen: `Ctrl + A + D`

### 4. Uso fácil

Ingrese `http://your_server_ip` directamente en su navegador para disfrutar de VS Code en la nube.

![](https://f004.backblazeb2.com/file/wiki-media/img/20200413181001.jpg)

Configuración de acceso de dominio: `Por explorar...`

## Problemas actuales

- La cantidad de complementos descargables directamente es limitada, la instalación manual de complementos es complicada y no hay una función de sincronización automática de complementos/configuraciones de usuario. Se espera que se resuelva en futuras versiones.

## Referencias y agradecimientos

- [Ejecutar VS Code en el navegador, code-server (servidor de Alibaba Cloud)](https://copyfuture.com/blogs-details/20200405045150018h4edt0f4q8486jq)
- [Ejecutar VS Code en el navegador, code-server](https://segmentfault.com/a/1190000022267386)
- [Herramienta en línea de VS code - Instalación y uso de code-server en un servidor en la nube y solución a problemas comunes (muy detallado)](https://blog.csdn.net/Granery/article/details/90415636)
- [Entorno de aprendizaje de programación en iPad - Configuración de la versión web de VS Code](https://blog.icodef.com/2019/11/17/1670)

> Autor del artículo: **Power Lin**
> Dirección original: <https://wiki-power.com>
> Declaración de derechos de autor: Este artículo utiliza la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Por favor, indique la fuente al volver a publicar.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.