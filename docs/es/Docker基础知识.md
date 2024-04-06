# Fundamentos de Docker

![Imagen](https://media.wiki-power.com/img/20210116153041.png)

Como es ampliamente conocido, una de las tareas más tediosas en el desarrollo de software es la configuración del entorno. Las diferencias en los entornos de ejecución pueden llevar a resultados inesperados, pero el uso de Docker puede evitar este tipo de problemas.

## Docker y la Tecnología de Contenedores

Docker empaca el software en sí mismo junto con el entorno de ejecución necesario, de modo que no es necesario configurar el entorno al utilizarlo (ya que el entorno se encuentra dentro del paquete). Esto asegura que tu entorno sea idéntico al de los desarrolladores, evitando problemas causados por diferencias en el entorno de ejecución.

Docker utiliza la tecnología de **contenedorización**. Cuando hablamos de contenedorización, podemos compararla con un **contenedor de envío**. Es un contenedor grande y estandarizado que se puede cargar y descargar fácilmente entre varios medios de transporte, como barcos, trenes y camiones, sin preocuparse por su contenido interno específico. De manera similar, la tecnología de contenedorización empaqueta la aplicación y todas sus dependencias en un entorno independiente y portátil, llamado contenedor.

El objetivo principal de la tecnología de contenedorización es lograr una implementación rápida de aplicaciones, escalabilidad y aislamiento del entorno. Al empaquetar la aplicación y sus dependencias en un contenedor, garantizamos que la aplicación se ejecute de manera coherente en diferentes computadoras o servidores, sin preocuparnos por las diferencias en el entorno o los conflictos de dependencias. Esto permite a los desarrolladores entregar aplicaciones más rápidamente y simplifica el proceso de implementación y gestión de aplicaciones.

Una de las principales ventajas de la tecnología de contenedorización es que proporciona una solución de virtualización ligera. En comparación con las máquinas virtuales tradicionales, la tecnología de contenedorización es más liviana y consume menos recursos. Cada contenedor se ejecuta en el mismo kernel del sistema operativo anfitrión, compartiendo los recursos del sistema operativo. Como resultado, los contenedores se inician más rápido, utilizan menos memoria y pueden ejecutarse simultáneamente en la misma máquina.

Docker es una de las soluciones de contenedorización más populares en la actualidad. Se compone principalmente de tres elementos: Imagen (Image), Contenedor (Container) y Repositorio (Repository).

- **Imagen (Image)**: Una imagen es un archivo ejecutable que contiene el sistema de archivos completo de una aplicación, incluyendo código, tiempo de ejecución, herramientas del sistema y bibliotecas. Puedes pensar en una imagen como una plantilla para crear múltiples instancias de contenedores diferentes.

- **Contenedor (Container)**: Un contenedor es una instancia en ejecución creada a partir de una imagen. Cada contenedor es un entorno aislado e independiente en el que se puede ejecutar una aplicación.

- **Repositorio (Repository)**: Un repositorio es un lugar para almacenar y compartir imágenes. Puedes cargar tus propias imágenes en un repositorio y también descargar imágenes creadas por otros.

La relación entre los contenedores y las imágenes es similar a la relación entre objetos y clases en la programación orientada a objetos.

## Instalación y Configuración de Docker

Antes de instalar Docker, puedes desinstalar versiones antiguas de paquetes con el siguiente comando para evitar conflictos:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Para los sistemas Linux más comunes, puedes utilizar el siguiente script oficial para descargar e instalar Docker Engine (debes tener permisos de usuario root):

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Dado que Docker se ejecuta en un entorno Linux y depende de él, tiene un impacto prácticamente nulo en la eficiencia. Sin embargo, si deseas implementar Docker en otros sistemas, primero debes instalar un entorno Linux virtual.

![Imagen](https://media.wiki-power.com/img/20230708005714.png)

Para obtener instrucciones sobre cómo instalar Docker en Windows, consulta la documentación oficial [**Instalar Docker Desktop en Windows**](https://docs.docker.com/desktop/install/windows-install/).

Para obtener instrucciones sobre cómo instalar Docker en MacOS, consulta la documentación oficial [**Instalar Docker Desktop en Mac**](https://docs.docker.com/desktop/install/mac-install/).

Una vez que hayas instalado Docker siguiendo el procedimiento, puedes verificar si la instalación se realizó con éxito utilizando el siguiente comando:

```shell
docker version
```

Si deseas utilizar Docker Engine en Linux sin ser un usuario root, puedes configurar los permisos con los siguientes comandos:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

Después de configurar esto, es posible que necesites cerrar sesión y volver a iniciarla para actualizar los permisos.

Si encuentras problemas durante la instalación, puedes consultar la documentación oficial en [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/).

## Ejemplo: Hello World

A continuación, se utilizará el ejemplo oficial de hello-world para demostrar Docker. Abre una terminal o símbolo del sistema e ingresa el siguiente comando para ejecutar un contenedor hello-world:

```shell
docker run hello-world
```

Esto descargará la imagen hello-world desde el repositorio de Docker, creará y ejecutará el contenedor. Cuando veas la salida de "hello world", significará que la ejecución fue exitosa.

## Algunos comandos comunes de Docker CLI

Docker proporciona una serie de comandos potentes y completos para administrar y operar recursos como contenedores, imágenes, redes, y más. Aquí tienes algunos comandos comunes de Docker CLI:

- `docker run`: Crea y ejecuta un nuevo contenedor basado en una imagen especificada. Por ejemplo, `docker run -d -p 8080:80 nginx` ejecutará un contenedor NGINX en segundo plano y mapeará el puerto 8080 del host al puerto 80 del contenedor.

- `docker ps`: Lista los contenedores en ejecución. Por defecto, muestra información sobre los contenedores en ejecución, como su ID, imagen y comando. Puedes usar `docker ps -a` para ver todos los contenedores, incluyendo los detenidos.

- `docker stop`: Detiene uno o varios contenedores en ejecución. Puedes especificar el ID o nombre del contenedor. Por ejemplo, `docker stop mycontainer` detendrá el contenedor llamado `mycontainer`.

- `docker start`: Inicia uno o varios contenedores que están detenidos. Puedes usar el ID o nombre del contenedor para especificar cuál iniciar.

- `docker restart`: Reinicia uno o varios contenedores.

- `docker rm`: Elimina uno o varios contenedores. Si necesitas eliminar un contenedor en ejecución, puedes usar `docker rm -f`.

- `docker images`: Enumera las imágenes locales, mostrando información como ID, tamaño y fecha de creación.

- `docker rmi`: Elimina una o varias imágenes. Puedes especificar las imágenes por su ID o etiqueta. Por ejemplo, `docker rmi myimage:1.0` eliminará la imagen llamada `myimage` con la etiqueta `1.0`.

- `docker build`: Construye una imagen personalizada basada en un Dockerfile. Por ejemplo, `docker build -t myimage:1.0 .` construirá una imagen llamada `myimage` con la etiqueta `1.0` en función del Dockerfile en el directorio actual.

- `docker exec`: Ejecuta un comando en un contenedor en ejecución. Puedes especificar el ID o nombre del contenedor, así como el comando que deseas ejecutar. Por ejemplo, `docker exec -it mycontainer bash` abrirá un terminal interactivo en el contenedor llamado `mycontainer`.

Estos son algunos de los comandos más comunes de Docker para administrar contenedores e imágenes. Existen más comandos que puedes explorar utilizando `docker --help` para ver la lista completa y otras opciones disponibles. También puedes consultar la documentación oficial en [**Use the Docker command line**](https://docs.docker.com/engine/reference/commandline/cli/) para obtener más información sobre Docker. Si deseas obtener más conocimientos relacionados con Docker, te invitamos a consultar artículos adicionales.

- [**Docker Compose - Herramienta de Orquestación de Imágenes**](https://wiki-power.com/DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**Empaquetar una Aplicación como Contenedor Docker**](https://wiki-power.com/%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

Si deseas sumergirte directamente en la práctica, también puedes consultar la siguiente serie de artículos:

- [Configurar tu propio HomeLab](https://wiki-power.com/Configurar-tu-propio-HomeLab)
- [HomeLab - Panel de gestión de servidores ligero CasaOS](https://wiki-power.com/HomeLab-Panel-de-gestion-de-servidores-ligero-CasaOS)
- [HomeLab - Panel de gestión de certificados y proxy Nginx Proxy Manager](https://wiki-power.com/HomeLab-Panel-de-gestion-de-certificados-y-proxy-Nginx-Proxy-Manager)
- [HomeLab - Herramienta de túneles internos frp](https://wiki-power.com/HomeLab-Herramienta-de-tuneles-internos-frp)
- [HomeLab - Alternativa gratuita para túneles internos Cloudflared](https://wiki-power.com/HomeLab-Alternativa-gratuita-para-tuneles-internos-Cloudflared)
- [HomeLab - Editor de código en línea code-server](https://wiki-power.com/HomeLab-Editor-de-codigo-en-linea-code-server)
- [HomeLab - Herramienta de monitoreo de estado de sitios web Uptime Kuma](https://wiki-power.com/HomeLab-Herramienta-de-monitoreo-de-estado-de-sitios-web-Uptime-Kuma)
- [HomeLab - Herramienta de compresión de imágenes de alta calidad TinyPNG-docker](https://wiki-power.com/HomeLab-Herramienta-de-compresion-de-imagenes-de-alta-calidad-TinyPNG-docker)
- [HomeLab - Sencillo sitio de navegación de marcadores personales Flare](https://wiki-power.com/HomeLab-Sencillo-sitio-de-navegacion-de-marcadores-personales-Flare)
- [HomeLab - Plataforma de gestión de aplicaciones en contenedores Portainer](https://wiki-power.com/HomeLab-Plataforma-de-gestion-de-aplicaciones-en-contenedores-Portainer)
- [HomeLab - Herramienta de sincronización entre dispositivos Syncthing](https://wiki-power.com/HomeLab-Herramienta-de-sincronizacion-entre-dispositivos-Syncthing)
- [HomeLab - Herramienta de notas fragmentadas memos](https://wiki-power.com/HomeLab-Herramienta-de-notas-fragmentadas-memos)
- [HomeLab - Potente sistema de wiki Wiki.js](https://wiki-power.com/HomeLab-Potente-sistema-de-wiki-Wiki.js)
- [HomeLab - Gestor de contraseñas autohospedado Vaultwarden](https://wiki-power.com/HomeLab-Gestor-de-contraseñas-autohospedado-Vaultwarden)
- [HomeLab - Sistema de alojamiento de imágenes con soporte para la nube pública Cloudreve](https://wiki-power.com/HomeLab-Sistema-de-alojamiento-de-imagenes-con-soporte-para-la-nube-publica-Cloudreve)
- [HomeLab - Agregador de RSS autohospedado FreshRSS](https://wiki-power.com/HomeLab-Agregador-de-RSS-autohospedado-FreshRSS)
- [HomeLab - Bastión con soporte para múltiples protocolos Next Terminal](https://wiki-power.com/HomeLab-Bastion-con-soporte-para-multiples-protocolos-Next-Terminal)
- [HomeLab - Caja de herramientas PDF multifuncional Stirling-PDF](https://wiki-power.com/HomeLab-Caja-de-herramientas-PDF-multifuncional-Stirling-PDF)
- [HomeLab - Herramienta de extracción de favicon de sitios web iconserver](https://wiki-power.com/HomeLab-Herramienta-de-extraccion-de-favicon-de-sitios-web-iconserver)
- [HomeLab - Herramienta para la actualización automática de contenedores Docker Watchtower](https://wiki-power.com/HomeLab-Herramienta-para-la-actualizacion-automatica-de-contenedores-Docker-Watchtower)
- [HomeLab - Programa de listas de archivos con soporte para múltiples almacenes Alist](https://wiki-power.com/HomeLab-Programa-de-listas-de-archivos-con-soporte-para-multiples-almacenes-Alist)
- [HomeLab - Software de tableros rico en funciones WeKan](https://wiki-power.com/HomeLab-Software-de-tableros-rico-en-funciones-WeKan)
- [HomeLab - Servidor de podcasts y audiolibros Audiobookshelf](https://wiki-power.com/HomeLab-Servidor-de-podcasts-y-audiolibros-Audiobookshelf)
- [HomeLab - Servidor de música en la nube Navidrome](https://wiki-power.com/HomeLab-Servidor-de-musica-en-la-nube-Navidrome)
- [HomeLab - Servidor multimedia para películas y series Jellyfin](https://wiki-power.com/HomeLab-Servidor-multimedia-para-peliculas-y-series-Jellyfin)
- [HomeLab - Servidor de gestión de libros electrónicos calibre-web](https://wiki-power.com/HomeLab-Servidor-de-gestion-de-libros-electronicos-calibre-web)
- [HomeLab - Servidor de hogar inteligente Home Assistant](https://wiki-power.com/HomeLab-Servidor-de-hogar-inteligente-Home-Assistant)
- [HomeLab - Software de tarjetas de memoria asistida Anki](https://wiki-power.com/HomeLab-Software-de-tarjetas-de-memoria-asistida-Anki)

## Referencias y Agradecimientos

- [Docker - De Principiante a Profesional](https://yeasy.gitbook.io/docker_practice/)
- [Tutorial de Docker](https://www.runoob.com/docker/docker-tutorial.html)
- [Tutorial de Iniciación a Docker](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [Instalación de Docker en CentOS](https://wiki-power.com/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
