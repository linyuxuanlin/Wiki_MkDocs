# Fundamentos de Docker

![](https://f004.backblazeb2.com/file/wiki-media/img/20210116153041.png)

Es bien sabido que una de las cosas más molestas en el desarrollo de software es la configuración del entorno. Las diferencias en los entornos de ejecución pueden causar resultados inesperados, pero el uso de Docker puede evitar este tipo de problemas.

## Docker y la tecnología de contenedores

Docker empaqueta el software en sí mismo y su entorno de ejecución necesario, por lo que no es necesario configurar el entorno al utilizarlo (ya que el entorno está dentro del paquete). Esto asegura que su entorno sea exactamente igual al del desarrollador, evitando problemas causados por diferencias en los entornos de ejecución.

Docker utiliza la tecnología de **contenedores**. Cuando hablamos de tecnología de contenedores, podemos compararla con los **contenedores de carga**. Son contenedores grandes y estandarizados que se pueden cargar y descargar fácilmente entre diferentes medios de transporte (como barcos, trenes y camiones) sin tener que preocuparse por su contenido interno específico. De manera similar, la tecnología de contenedores empaqueta la aplicación y todas sus dependencias en un entorno independiente y portátil, llamado contenedor.

El objetivo principal de la tecnología de contenedores es lograr una implementación rápida, escalabilidad y aislamiento del entorno de las aplicaciones. Al empaquetar la aplicación y sus dependencias en un contenedor, podemos asegurarnos de que se ejecute de manera consistente en diferentes computadoras o servidores sin preocuparnos por las diferencias en los entornos o conflictos de dependencias. Esto permite a los desarrolladores entregar aplicaciones más rápidamente y simplifica el proceso de implementación y gestión de aplicaciones.

Una de las principales ventajas de la tecnología de contenedores es que proporciona una solución de virtualización ligera. En comparación con las máquinas virtuales tradicionales, la tecnología de contenedores es más liviana y consume menos recursos. Cada contenedor se ejecuta en el mismo kernel del sistema operativo host, compartiendo los recursos del sistema operativo, lo que significa que los contenedores se inician más rápido, ocupan menos memoria y pueden ejecutarse varios contenedores en la misma máquina.

Docker es una solución de contenedorización popular en la actualidad. Incluye principalmente tres elementos: Image (imagen), Container (contenedor) y Repository (repositorio).

- **Image (imagen)**: Una imagen es un archivo ejecutable que contiene todos los sistemas de archivos (código, tiempo de ejecución, herramientas del sistema, archivos de biblioteca) y configuraciones necesarias para la aplicación y sus dependencias. Podemos considerar una imagen como una plantilla para contenedores, a través de la cual se pueden crear múltiples instancias de contenedores diferentes.
- **Container (contenedor)**: Un contenedor es una instancia de ejecución creada a partir de una imagen. Cada contenedor es un entorno aislado e independiente en el que se puede ejecutar una aplicación.
- **Repository (repositorio)**: Un repositorio es un lugar para almacenar y compartir imágenes. Podemos cargar nuestras propias imágenes en el repositorio y descargar imágenes creadas por otros.

La relación entre contenedores e imágenes es similar a la relación entre objetos y clases en la programación orientada a objetos.

## Instalación y configuración de Docker

Antes de instalar Docker, puede desinstalar los paquetes de versiones antiguas con el siguiente comando para evitar conflictos:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

Para los sistemas Linux principales, puede descargar e instalar Docker Engine utilizando el script oficial (se requieren permisos de usuario root):

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Dado que Docker se ejecuta y depende del entorno de Linux, prácticamente no tiene pérdida de eficiencia. Sin embargo, si desea implementar Docker en otros sistemas, primero debe instalar un entorno de Linux virtual.

![](https://f004.backblazeb2.com/file/wiki-media/img/20230708005714.png)

Para obtener información sobre cómo instalar Docker en Windows, consulte la documentación oficial [**Instalar Docker Desktop en Windows**](https://docs.docker.com/desktop/install/windows-install/).

Para instalar Docker Desktop en MacOS, consulte la documentación oficial [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/).

Una vez instalado, podemos verificar si Docker se ha instalado correctamente con el siguiente comando:

```shell
docker version
```

Después de instalar Docker Engine en Linux, si desea usarlo como usuario no root, puede configurar los permisos con el siguiente comando:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

Después de completar la configuración, es posible que deba cerrar sesión y volver a iniciar sesión para actualizar los permisos.

Si tiene problemas durante la instalación, consulte la documentación oficial [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/).

## Ejemplo: Hola mundo

A continuación, usaremos el ejemplo oficial de hello-world para demostrar Docker. Abra la terminal o el símbolo del sistema e ingrese el siguiente comando para ejecutar el contenedor hello-world:

```shell
docker run hello-world
```

Esto descargará la imagen hello-world del repositorio de imágenes de Docker, creará y ejecutará el contenedor. Cuando vea la salida de hello world, significa que se ha ejecutado correctamente.

## Algunos comandos de Docker CLI comunes

Docker proporciona un conjunto de comandos poderosos y ricos para administrar y operar recursos como contenedores, imágenes, redes, etc. A continuación se muestran algunos comandos de Docker CLI comunes:

- `docker run`: crea y ejecuta un nuevo contenedor basado en la imagen especificada. Por ejemplo, `docker run -d -p 8080:80 nginx` ejecutará un contenedor NGINX en segundo plano y mapeará el puerto 8080 del host al puerto 80 del contenedor.
- `docker ps`: lista los contenedores en ejecución. De forma predeterminada, mostrará información como el ID del contenedor, la imagen y el comando en ejecución. Use `docker ps -a` para mostrar todos los contenedores, incluidos los detenidos.
- `docker stop`: detiene uno o más contenedores en ejecución. Puede especificar el ID o el nombre del contenedor. Por ejemplo, `docker stop mycontainer` detendrá el contenedor llamado `mycontainer`.
- `docker start`: inicia uno o más contenedores detenidos. Puede especificar el ID o el nombre del contenedor.
- `docker restart`: reinicia uno o más contenedores.
- `docker rm`: elimina uno o más contenedores. Use `docker rm -f` para eliminar un contenedor en ejecución.
- `docker images`: lista las imágenes locales. Muestra una lista de imágenes de Docker descargadas y creadas en la computadora local, incluida información como el ID de la imagen, el tamaño y la hora de creación.
- `docker rmi`: elimina una o más imágenes. Puede especificar el ID o la etiqueta de la imagen. Por ejemplo, `docker rmi myimage:1.0` eliminará la imagen llamada `myimage` con la etiqueta `1.0`.
- `docker build`: construye una imagen personalizada basada en un Dockerfile. Por ejemplo, `docker build -t myimage:1.0 .` construirá una imagen llamada `myimage` con la etiqueta `1.0` basada en el Dockerfile en el directorio actual.
- `docker exec`: ejecuta un comando en un contenedor en ejecución. Puede especificar el ID o el nombre del contenedor y el comando a ejecutar. Por ejemplo, `docker exec -it mycontainer bash` iniciará una nueva terminal interactiva en el contenedor llamado `mycontainer`.

Estos son algunos comandos de Docker comunes utilizados para administrar y operar contenedores e imágenes. Hay muchos más comandos para explorar, se pueden ver la lista completa de comandos y otras opciones disponibles a través del comando `docker --help`, o consultando la documentación oficial [**Use the Docker command line**](https://docs.docker.com/engine/reference/commandline/cli/).

Para obtener más información sobre Docker, consulte los siguientes artículos:

- [**Docker Compose - Herramienta de orquestación de imágenes**](https://wiki-power.com/es/DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**Empaquetar aplicaciones como contenedores Docker**](https://wiki-power.com/es/%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

Si desea comenzar a practicar directamente, también puede consultar la siguiente serie de artículos:

- [Cómo construir tu propio HomeLab](https://wiki-power.com/es/Construyendo-tu-propio-HomeLab)
- [Homelab - Panel de gestión de servidores ligero CasaOS](https://wiki-power.com/es/Homelab-Panel-de-gestión-de-servidores-ligero-CasaOS)
- [Homelab - Panel de gestión de certificados de proxy inverso Nginx Proxy Manager](https://wiki-power.com/es/Homelab-Panel-de-gestión-de-certificados-de-proxy-inverso-Nginx-Proxy-Manager)
- [Homelab - Herramienta de penetración de red frp](https://wiki-power.com/es/Homelab-Herramienta-de-penetración-de-red-frp)
- [Homelab - Alternativa gratuita de penetración de red interna Cloudflared](https://wiki-power.com/es/Homelab-Alternativa-gratuita-de-penetración-de-red-interna-Cloudflared)
- [Homelab - Editor de código en línea code-server](https://wiki-power.com/es/Homelab-Editor-de-código-en-línea-code-server)
- [Homelab - Herramienta de monitoreo de estado de sitio web Uptime Kuma](https://wiki-power.com/es/Homelab-Herramienta-de-monitoreo-de-estado-de-sitio-web-Uptime-Kuma)
- [Homelab - Herramienta de compresión de imágenes de alta calidad TinyPNG-docker](https://wiki-power.com/es/Homelab-Herramienta-de-compresión-de-imágenes-de-alta-calidad-TinyPNG-docker)
- [Homelab - Sitio de navegación de marcadores personales minimalista Flare](https://wiki-power.com/es/Homelab-Sitio-de-navegación-de-marcadores-personales-minimalista-Flare)
- [Homelab - Plataforma de gestión de aplicaciones de contenedores Portainer](https://wiki-power.com/es/Homelab-Plataforma-de-gestión-de-aplicaciones-de-contenedores-Portainer)
- [Homelab - Herramienta de sincronización entre dispositivos Syncthing](https://wiki-power.com/es/Homelab-Herramienta-de-sincronización-entre-dispositivos-Syncthing)
- [Homelab - Herramienta de notas fragmentadas memos](https://wiki-power.com/es/Homelab-Herramienta-de-notas-fragmentadas-memos)
- [Homelab - Sistema wiki potente Wiki.js](https://wiki-power.com/es/Homelab-Sistema-wiki-potente-Wiki.js)
- [Homelab - Gestor de contraseñas autohospedado Vaultwarden](https://wiki-power.com/es/Homelab-Gestor-de-contraseñas-autohospedado-Vaultwarden)
- [Homelab - Sistema de almacenamiento de imágenes en la nube compatible con la nube pública Cloudreve](https://wiki-power.com/es/Homelab-Sistema-de-almacenamiento-de-imágenes-en-la-nube-compatible-con-la-nube-pública-Cloudreve)
- [Homelab - Agregador de RSS autohospedado FreshRSS](https://wiki-power.com/es/Homelab-Agregador-de-RSS-autohospedado-FreshRSS)
- [Homelab - Bastión que admite varios protocolos Next Terminal](https://wiki-power.com/es/Homelab-Bastión-que-admite-varios-protocolos-Next-Terminal)
- [Homelab - Caja de herramientas PDF multifuncional Stirling-PDF](https://wiki-power.com/es/Homelab-Caja-de-herramientas-PDF-multifuncional-Stirling-PDF)
- [Homelab - Herramienta de captura de favicon de sitio web iconserver](https://wiki-power.com/es/Homelab-Herramienta-de-captura-de-favicon-de-sitio-web-iconserver)
- [Homelab - Herramienta de actualización automática de contenedores Docker Watchtower](https://wiki-power.com/es/Homelab-Herramienta-de-actualización-automática-de-contenedores-Docker-Watchtower)
- [Homelab - Programa de lista de archivos compatible con múltiples almacenamientos Alist](https://wiki-power.com/es/Homelab-Programa-de-lista-de-archivos-compatible-con-múltiples-almacenamientos-Alist)
- [Homelab - Software de pizarra rico en funciones WeKan](https://wiki-power.com/es/Homelab-Software-de-pizarra-rico-en-funciones-WeKan)
- [Homelab - Servidor de podcast y audiolibros Audiobookshelf](https://wiki-power.com/es/Homelab-Servidor-de-podcast-y-audiolibros-Audiobookshelf)
- [Homelab - Servidor de música en la nube Navidrome](https://wiki-power.com/es/Homelab-Servidor-de-música-en-la-nube-Navidrome)
- [Homelab - Servidor multimedia de películas y series Jellyfin](https://wiki-power.com/es/Homelab-Servidor-multimedia-de-películas-y-series-Jellyfin)
- [Homelab - Servidor de gestión de libros electrónicos calibre-web](https://wiki-power.com/es/Homelab-Servidor-de-gestión-de-libros-electrónicos-calibre-web)
- [Homelab - Servidor de hogar inteligente Home Assistant](https://wiki-power.com/es/Homelab-Servidor-de-hogar-inteligente-Home-Assistant)
- [Homelab - Software de memoria asistida por tarjetas Anki](https://wiki-power.com/es/Homelab-Software-de-memoria-asistida-por-tarjetas-Anki)

## Referencias y Agradecimientos

- [Docker - Desde principiante hasta práctico](https://yeasy.gitbook.io/docker_practice/)
- [Tutorial de Docker](https://www.runoob.com/docker/docker-tutorial.html)
- [Tutorial de introducción a Docker](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [Instalación de Docker en CentOS](https://wiki-power.com/es/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

por_reemplazar[1]  
por_reemplazar[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.