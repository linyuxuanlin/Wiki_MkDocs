# Fundamentos de Docker

![](https://img.wiki-power.com/d/wiki-media/img/20210116153041.png)

Es bien sabido que una de las tareas más tediosas en el desarrollo de software es la configuración del entorno. Las diferencias en los entornos de ejecución pueden llevar a resultados inesperados, pero el uso de Docker puede evitar este tipo de problemas.

## Docker y la Tecnología de Contenedores

Docker empaqueta el software en sí y el entorno en el que se ejecuta, de modo que no es necesario configurar el entorno al usarlo (ya que el entorno está contenido en el paquete). Esto asegura que su entorno sea idéntico al del desarrollador, evitando problemas causados por diferencias en el entorno de ejecución.

Docker utiliza la **tecnología de contenedores**. Cuando hablamos de tecnología de contenedores, podemos compararla con un **contenedor de carga estándar**. Es un contenedor grande y normalizado que se puede cargar y descargar fácilmente entre varios medios de transporte, como barcos, trenes y camiones, sin necesidad de conocer su contenido interno. De manera similar, la tecnología de contenedores empaca una aplicación y todas sus dependencias en un entorno independiente y portátil, llamado contenedor.

El objetivo principal de la tecnología de contenedores es lograr una implementación rápida de aplicaciones, escalabilidad y aislamiento del entorno. Al empaquetar la aplicación y sus dependencias en un contenedor, podemos asegurarnos de que la aplicación se ejecute de manera coherente en diferentes computadoras o servidores, sin preocuparnos por las diferencias de entorno o conflictos de dependencias. Esto acelera la entrega de aplicaciones y simplifica el proceso de implementación y gestión de aplicaciones.

Una de las principales ventajas de la tecnología de contenedores es que proporciona una solución de virtualización ligera. En comparación con las máquinas virtuales tradicionales, la tecnología de contenedores es más liviana y consume menos recursos. Cada contenedor se ejecuta en el mismo núcleo del sistema operativo anfitrión, compartiendo los recursos del sistema operativo. Esto significa que los contenedores se inician más rápidamente, consumen menos memoria y pueden ejecutarse varios contenedores en la misma máquina.

Docker es una de las soluciones de contenedores más populares en la actualidad. Está compuesto principalmente por tres elementos: Imagen (Image), Contenedor (Container) y Repositorio (Repository).

- **Imagen (Image)**: Una imagen es un archivo ejecutable que contiene todos los sistemas de archivos necesarios para una aplicación, incluyendo código, tiempo de ejecución, herramientas del sistema y bibliotecas. Puedes pensar en una imagen como una plantilla para contenedores, a partir de la cual se pueden crear múltiples instancias de contenedores.
- **Contenedor (Container)**: Un contenedor es una instancia en ejecución creada a partir de una imagen. Cada contenedor es un entorno aislado e independiente en el que se puede ejecutar una aplicación.
- **Repositorio (Repository)**: Un repositorio es un lugar para almacenar y compartir imágenes. Puedes cargar tus propias imágenes en un repositorio y también descargar imágenes creadas por otros.

La relación entre contenedores y imágenes es similar a la relación entre objetos y clases en la programación orientada a objetos.

## Instalación y Configuración de Docker

Antes de instalar Docker, puedes desinstalar versiones anteriores del paquete con el siguiente comando para evitar conflictos:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Para sistemas Linux populares, puedes usar el siguiente método con el script oficial para descargar e instalar Docker Engine (requiere permisos de usuario root):

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Dado que Docker se ejecuta en un entorno Linux y depende de él, tiene un impacto de eficiencia prácticamente nulo en ese sistema. Sin embargo, si deseas implementar Docker en otros sistemas, primero debes instalar un entorno Linux virtual.

![](https://img.wiki-power.com/d/wiki-media/img/20230708005714.png)

Para obtener información sobre cómo instalar Docker en Windows, consulta la documentación oficial [**Instalar Docker Desktop en Windows**](https://docs.docker.com/desktop/install/windows-install/).

Para obtener información sobre cómo instalar Docker en macOS, consulta la documentación oficial [**Instalar Docker Desktop en Mac**](https://docs.docker.com/desktop/install/mac-install/).

Después de instalar Docker siguiendo el procedimiento, puedes verificar si Docker se ha instalado correctamente utilizando el siguiente comando:

```shell
docker version
```

Si has instalado Docker Engine en Linux y deseas usarlo como un usuario no root, puedes configurar los permisos con los siguientes comandos:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

Una vez completada la configuración, es posible que necesites cerrar la sesión y volver a iniciarla para actualizar los permisos.

Si encuentras problemas durante la instalación, consulta la documentación oficial [**Solución de problemas de la instalación de Docker Engine**](https://docs.docker.com/engine/install/troubleshoot/).

## Ejemplo: Hello World

A continuación, vamos a usar el ejemplo oficial de "hello-world" para demostrar Docker. Abre la terminal o el símbolo del sistema e ingresa el siguiente comando para ejecutar el contenedor "hello-world":

```shell
docker run hello-world
```

Esto descargará la imagen "hello-world" desde el repositorio de Docker, creará y ejecutará un contenedor. Cuando veas la salida de "hello world", significará que la ejecución se ha realizado con éxito.

## Algunos comandos comunes de la CLI de Docker

Docker proporciona un conjunto poderoso y completo de comandos para gestionar y operar recursos como contenedores, imágenes y redes. A continuación, se presentan algunos comandos comunes de la CLI de Docker:

- `docker run`: Crea y ejecuta un nuevo contenedor basado en una imagen específica. Por ejemplo, `docker run -d -p 8080:80 nginx` ejecutará un contenedor NGINX en segundo plano y mapeará el puerto 8080 del host al puerto 80 del contenedor.
- `docker ps`: Lista los contenedores en ejecución. De manera predeterminada, mostrará información como el ID del contenedor, la imagen y el comando. Puedes utilizar `docker ps -a` para ver todos los contenedores, incluyendo los detenidos.
- `docker stop`: Detiene uno o varios contenedores en ejecución, especificándolos por su ID o nombre. Por ejemplo, `docker stop mycontainer` detendrá el contenedor llamado "mycontainer".
- `docker start`: Inicia uno o varios contenedores previamente detenidos, especificándolos por su ID o nombre.
- `docker restart`: Reinicia uno o varios contenedores.
- `docker rm`: Elimina uno o varios contenedores. Si deseas eliminar un contenedor en ejecución, utiliza `docker rm -f`.
- `docker images`: Lista las imágenes locales, mostrando información como el ID, tamaño y fecha de creación.
- `docker rmi`: Elimina una o varias imágenes, especificándolas por su ID o etiqueta. Por ejemplo, `docker rmi myimage:1.0` eliminará la imagen llamada "myimage" con la etiqueta "1.0".
- `docker build`: Construye una imagen personalizada basada en un Dockerfile. Por ejemplo, `docker build -t myimage:1.0 .` construirá una imagen llamada "myimage" con la etiqueta "1.0" utilizando el Dockerfile del directorio actual.
- `docker exec`: Ejecuta comandos en un contenedor en ejecución, especificándolo por su ID o nombre y el comando que deseas ejecutar. Por ejemplo, `docker exec -it mycontainer bash` abrirá un nuevo terminal interactivo en el contenedor llamado "mycontainer".

Estos son algunos de los comandos comunes de Docker para gestionar y operar contenedores e imágenes. Hay muchos más comandos que puedes explorar utilizando `docker --help` para ver la lista completa y sus opciones, o consultando la documentación oficial [**Uso de la línea de comandos de Docker**](https://docs.docker.com/engine/reference/commandline/cli/) para obtener más información sobre Docker.

Para obtener más conocimientos relacionados con Docker, consulta los artículos posteriores.

- [**Docker Compose - Herramienta de Orquestación de Imágenes**](DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**Envolver tu Aplicación en Contenedores Docker**](%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

Si deseas comenzar a practicar de inmediato, también puedes consultar la siguiente serie de artículos:

- [Configurando tu propio HomeLab](Configurando tu propio HomeLab)
- [HomeLab - Panel de Gestión de Servidores Ligeros CasaOS](HomeLab - Panel de Gestión de Servidores Ligeros CasaOS)
- [HomeLab - Panel de Gestión de Certificados de Proxy Nginx](HomeLab - Panel de Gestión de Certificados de Proxy Nginx)
- [HomeLab - Herramienta de Penetración de Redes Internas frp](HomeLab - Herramienta de Penetración de Redes Internas frp)
- [HomeLab - Alternativa Gratuita de Penetración de Redes Internas Cloudflared](HomeLab - Alternativa Gratuita de Penetración de Redes Internas Cloudflared)
- [HomeLab - Editor de Código en Línea code-server](HomeLab - Editor de Código en Línea code-server)
- [HomeLab - Herramienta de Monitoreo de Estado de Sitios Web Uptime Kuma](HomeLab - Herramienta de Monitoreo de Estado de Sitios Web Uptime Kuma)
- [HomeLab - Herramienta de Compresión de Imágenes de Alta Calidad TinyPNG-docker](HomeLab - Herramienta de Compresión de Imágenes de Alta Calidad TinyPNG-docker)
- [HomeLab - Sencillo Sitio de Navegación de Marcadores Personales Flare](HomeLab - Sencillo Sitio de Navegación de Marcadores Personales Flare)
- [HomeLab - Plataforma de Gestión de Aplicaciones en Contenedores Portainer](HomeLab - Plataforma de Gestión de Aplicaciones en Contenedores Portainer)
- [HomeLab - Herramienta de Sincronización entre Dispositivos Syncthing](HomeLab - Herramienta de Sincronización entre Dispositivos Syncthing)
- [HomeLab - Herramienta de Notas Fragmentadas memos](HomeLab - Herramienta de Notas Fragmentadas memos)
- [HomeLab - Sistema de Wiki de Gran Potencia Wiki.js](HomeLab - Sistema de Wiki de Gran Potencia Wiki.js)
- [HomeLab - Gestor de Contraseñas Autohospedado Vaultwarden](HomeLab - Gestor de Contraseñas Autohospedado Vaultwarden)
- [HomeLab - Sistema de Hosting de Imágenes Compatible con la Nube Cloudreve](HomeLab - Sistema de Hosting de Imágenes Compatible con la Nube Cloudreve)
- [HomeLab - Agregador de RSS Autohospedado FreshRSS](HomeLab - Agregador de RSS Autohospedado FreshRSS)
- [HomeLab - Bastión de Múltiples Protocolos Next Terminal](HomeLab - Bastión de Múltiples Protocolos Next Terminal)
- [HomeLab - Caja de Herramientas PDF Multifunción Stirling-PDF](HomeLab - Caja de Herramientas PDF Multifunción Stirling-PDF)
- [HomeLab - Herramienta para Capturar Favicon de Sitios Web iconserver](HomeLab - Herramienta para Capturar Favicon de Sitios Web iconserver)
- [HomeLab - Herramienta para Actualización Automática de Contenedores Docker Watchtower](HomeLab - Herramienta para Actualización Automática de Contenedores Docker Watchtower)
- [HomeLab - Programa de Listado de Archivos Compatible con Múltiples Almacenamientos Alist](HomeLab - Programa de Listado de Archivos Compatible con Múltiples Almacenamientos Alist)
- [HomeLab - Software de Tablero Rico en Funciones WeKan](HomeLab - Software de Tablero Rico en Funciones WeKan)
- [HomeLab - Servidor de Podcasts y Audiolibros Audiobookshelf](HomeLab - Servidor de Podcasts y Audiolibros Audiobookshelf)
- [HomeLab - Servidor de Música en la Nube Navidrome](HomeLab - Servidor de Música en la Nube Navidrome)
- [HomeLab - Servidor de Medios de Cine y TV Jellyfin](HomeLab - Servidor de Medios de Cine y TV Jellyfin)
- [HomeLab - Servidor de Gestión de Libros Electrónicos calibre-web](HomeLab - Servidor de Gestión de Libros Electrónicos calibre-web)
- [HomeLab - Servidor de Hogar Inteligente Home Assistant](HomeLab - Servidor de Hogar Inteligente Home Assistant)
- [HomeLab - Software de Memoria Asistida con Tarjetas Anki](HomeLab - Software de Memoria Asistida con Tarjetas Anki)

## References and Acknowledgments

- [Docker - From Beginner to Practice](https://yeasy.gitbook.io/docker_practice/)
- [Docker Tutorial](https://www.runoob.com/docker/docker-tutorial.html)
- [Docker Getting Started Tutorial](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [CentOS Installation of Docker](to_be_replaced[3])

[to_be_replaced[1]]
[to_be_replaced[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.