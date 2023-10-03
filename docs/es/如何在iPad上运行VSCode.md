# Cómo ejecutar VS Code en iPad

Nota: este tutorial se basa en code-server v3.8.0, CentOS 8.2.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20201221140748.jpg)

Se recomienda instalar el servicio code-server mediante Docker compose.  
Solo se necesita una línea de comando para implementar y no es necesario configurar la ejecución en segundo plano, ya que viene con Git y otros entornos.  
Consulte: [**Homelab - Editor de código en línea code-server**](https://wiki-power.com/Homelab-%E5%9C%A8%E7%BA%BF%E4%BB%A3%E7%A0%81%E7%BC%96%E8%BE%91%E5%99%A8code-server)

Si no desea implementar mediante Docker compose, continúe leyendo.

## Configurar el servidor

En primer lugar, necesita un servidor que no se detenga las 24 horas (se recomienda comprar una máquina estudiantil de Alibaba Cloud / Tencent Cloud, por solo ¥9.9 / mes)  
Para garantizar la experiencia de uso, se recomienda la siguiente configuración del servidor:

- 2 núcleos o más
- 1 GB de RAM o más

Instale Linux (aquí uso CentOS 8.2) y asegúrese de que ssh pueda conectarse correctamente.

## Instalar code-server

En la nueva versión (≥v3.8.0), puede instalar directamente mediante script:

```shell
curl -fsSL https://code-server.dev/install.sh | sh
```

Si no puede descargarlo durante mucho tiempo, es probable que se deba a la contaminación DNS. Consulte [**GitHub Change Host**](https://wiki-power.com/GitHub改Host) para solucionarlo.

## Ejecutar code-server

Use el comando:

```shell
export PASSWORD="establezca una contraseña de acceso" && code-server --port 80 --host 0.0.0.0 --auth password
```

Si no hay errores, abra el navegador, ingrese la dirección IP del servidor y podrá ver un VS Code en línea.

## Configurar la ejecución en segundo plano

El code-server que se ejecuta en primer plano finalizará el proceso debido a la salida de ssh.  
Para que se ejecute en segundo plano, puede usar el programa screen (puede considerarlo como un contenedor).

### Instalar screen

```shell
yum install screen
```

### Crear un trabajo de screen

```shell
screen -S VSCode-online # VSCode-online es un nombre personalizado
```

### Iniciar el servicio code-server

```shell
export PASSWORD="establezca una contraseña de acceso" && code-server --port 80 --host 0.0.0.0 --auth password
```

Si todo va bien, puede acceder a él ingresando la dirección IP en el navegador.

## Expansión

### Agregar un acceso directo de escritorio

Si lo usa en iPad, puede abrirlo con el navegador Safari, hacer clic en el icono `Compartir` en la esquina superior derecha y luego en `Agregar a la pantalla de inicio`.  
Puede fingir que es una aplicación y ocultar la barra de estado del navegador.  
Por cierto, también es compatible con teclado y ratón externos.

### Otras operaciones de screen

- Ver el ID del trabajo en ejecución: `screen -ls`
- Volver a ingresar al trabajo de screen en ejecución: `screen -r jobid # El ID del trabajo debe incluir un identificador numérico de prefijo`
- Finalizar la ejecución de un trabajo: `screen -X -S jobid quit`
- Salir de la interfaz de screen del trabajo actual: `Ctrl + A + D`

### Parámetros de comando relacionados con code-server

- Acceso a través de Internet: el servicio code-server se ejecuta de forma predeterminada solo en local (`127.0.0.1`). Para poder acceder a través de una dirección IP, se puede agregar el parámetro `--host 0.0.0.0`.
- Especificar el puerto de ejecución: `--port xxxx`, donde `xxxx` puede ser reemplazado por `8888` o `80` (para usar el protocolo HTTP y acceder directamente a través de la dirección IP sin agregar el número de puerto).
- Establecer una contraseña de acceso: agregar `--auth password` para establecer una contraseña o no agregar ningún parámetro o agregar `--auth none` si no se necesita.

### Instalación de Git

VS Code se puede utilizar junto con Git para facilitar el desarrollo en la nube. Se puede instalar Git con el siguiente comando:

```shell
yum install git
```

### Acceso a través de un nombre de dominio

Puede resultar extraño acceder al servicio code-server a través de la dirección IP del servidor. Para solucionarlo, se puede vincular un nombre de dominio personalizado y acceder al servicio a través de él. Para ello, se debe comprar un nombre de dominio y agregar la dirección IP del servidor en la configuración DNS utilizando el tipo A.

### Errores conocidos y soluciones en la versión actual

- No se puede sincronizar la configuración del usuario a través del servicio de sincronización de configuración integrado en VS Code: se puede solucionar instalando el complemento [**Settings Sync**](https://marketplace.visualstudio.com/items?itemName=Shan.code-settings-sync).
- Error al iniciar sesión en GitHub a través de Settings Sync: se puede solucionar configurando la extensión en un navegador web en lugar de en VS Code.
- No se puede desplazar la página con la rueda del ratón en un iPad: actualmente, solo se puede desplazar la página tocando directamente la pantalla o utilizando las teclas de dirección del teclado.

## Referencias y agradecimientos

- [Running VSCode in a Browser (Old)](https://wiki-power.com/在浏览器上运行VSCode（旧）)
- [GitHub Hosts](https://wiki-power.com/GitHub改Host)
- [Installation and Usage of screen](https://www.jianshu.com/p/420569381e74)
- [Setup Guide · cdr/code-server](https://github.com/cdr/code-server/blob/v3.8.0/doc/guide.md)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.