````markdown
# Running VS Code on a Browser (Old Method)

Note: For deploying code-server version ≥v3.8.0, please refer to [**How to Run VS Code on an iPad**](https://wiki-power.com/如何在iPad上运行VSCode) for a more streamlined approach.

## Background

It is well known that VS Code is a highly powerful code editor. If we could use VS Code on lightweight platforms like the iPad (with iPadOS offering mouse and keyboard support that rivals desktop systems), we could work anytime, anywhere.

Fortunately, there is a service that allows VS Code to run on a server: code-server. Once deployed, it can be accessed through a web browser. This way, with an internet connection, any device can easily make use of VS Code.

## Prerequisites

You will need a server with Linux installed (I used the lowest configuration student server from Alibaba Cloud).

Official system requirements are as follows:

- 64-bit host.
- At least 1GB of RAM.
- 2 cores or more are recommended (1 core works but not optimally).
- Secure connection over HTTPS or localhost (required for service workers and clipboard support).
- For Linux: GLIBC 2.17 or later and GLIBCXX 3.4.15 or later.

## Installation

### 1. Download

```shell
wget https://github.com/cdr/code-server/releases/download/3.1.0/code-server-3.1.0-linux-x86_64.tar.gz # Download code-server
```
````

Do not copy the command verbatim. Instead, on the [**Release**](https://github.com/cdr/code-server/releases) page for code-server, copy the link for the latest version (choose the one that matches your server's architecture; I used the `code-server-3.1.0-linux-x86_64.tar.gz` version), and use `wget` or `SFTP` to download/transfer it to your server.

If the download speed is slow, you can copy the download link and use the [**GitHub File Accelerator**](https://gh.api.99988866.xyz/) website to obtain a domestically accelerated download link.

```shell
tar -xvf code-server-3.1.0-linux-x86_64.tar.gz # Extract
```

### 2. Installation

```shell
cd code-server
export PASSWORD="yourpassword"
./code-server --port 8888 --host 0.0.0.0
```

- Change `yourpassword` to your desired password; otherwise, a random password will be generated.
- `--port 8888` specifies the running port. You can set it to `80` (HTTP protocol) so you won't need to add a port number when accessing it.
- `--host 0.0.0.0` allows the service to be accessed from the external network. The default `127.0.0.1` restricts access to the local machine.
- If you don't need password authentication, you can add `--auth none`.
- If the service does not start successfully, it may be due to choosing the wrong **processor architecture version**. Try another version.

### 3. Configure Background Running

By default, when running directly, the connection is lost when the SSH connection is terminated. To run it in the background, you can use `screen`:

```shell
yum install screen
or
apt-get install screen
```

```shell
screen -S VSCode-online # VSCode-online is a name of your choice
export PASSWORD="password" && ./code-server --port 8888 --host 0.0.0.0
```

To re-enter the running screen job:

```shell
screen -r JobName
```

````

Si necesitas detener la ejecución en segundo plano de `screen`:

```shell
screen -ls # Ver IDs de servicios en ejecución
screen -X -S id quit # Reemplaza 'id' con el ID correspondiente
````

Para salir de `screen`: `Ctrl + A + D`

### 4. Uso Sencillo

Simplemente ingresa `http://tu_dirección_ip_de_servidor` en tu navegador para disfrutar de VS Code en la nube.

![Imagen](https://media.wiki-power.com/img/20200413181001.jpg)

Configuración de acceso mediante un dominio: _Pendiente de exploración..._

## Problemas Actuales

- La cantidad de complementos descargables de manera directa es limitada, lo que hace que la instalación manual de complementos sea tediosa, y no hay funcionalidad de sincronización automática de complementos o configuraciones de usuario. Esto se abordará en futuras actualizaciones.

## Referencias y Agradecimientos

- [Ejecución de VS Code en el navegador, code-server (en servidores de Alibaba Cloud)](https://copyfuture.com/blogs-details/20200405045150018h4edt0f4q8486jq)
- [Ejecución de VS Code en el navegador, code-server](https://segmentfault.com/a/1190000022267386)
- [Herramienta en línea recomendada para VS Code: instalación y uso de code-server en servidores en la nube con solución de problemas detallada](https://blog.csdn.net/Granery/article/details/90415636)
- [Configuración de una versión web de VS Code para aprender a programar en iPad](https://blog.icodef.com/2019/11/17/1670)

> Autor del artículo: **Power Lin**
> Fuente original: <https://wiki-power.com>
> Declaración de derechos de autor: El artículo está licenciado bajo la [licencia CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Por favor, menciona la fuente si decides compartirlo.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
