# Docker Compose - Herramienta de orquestación de imágenes

![](https://f004.backblazeb2.com/file/wiki-media/img/20210117130925.jpg)

Docker Compose es una herramienta de orquestación de imágenes de Docker. Se recomienda utilizar Docker Compose como la forma predeterminada de abrir Docker, ya que no solo permite configurar y desplegar imágenes de manera conveniente, sino que también permite configurar servicios de múltiples imágenes de manera más conveniente e incluso distinguir su orden de inicio, lo que no es posible con la forma de abrir mediante comandos.

Aunque la idea de Docker es desacoplar (una imagen por proceso), aumentar la reutilización y no encapsular múltiples servicios en una sola imagen, hay algunas aplicaciones que requieren el inicio simultáneo de múltiples servicios. Por ejemplo, una aplicación web típica requiere al menos la colaboración del servidor y la base de datos. De esta manera, es necesario implementar dos contenedores por separado, e incluso algunos servicios deben iniciarse en un orden determinado. De esta manera, las imágenes y los pasos de operación necesarios serán muy complejos.

Docker Compose escribe todas las imágenes necesarias para llamar (todas las propiedades de los servicios y contenedores necesarios, la configuración de red y el montaje del volumen de almacenamiento) y el orden en un archivo YAML. Al ejecutar directamente este archivo de configuración, se pueden ejecutar los contenedores según el método y los pasos que necesite, sin necesidad de operar manualmente cada contenedor. A continuación se muestra un ejemplo de Docker Compose para implementar un servicio web:

```yaml title="compose.yaml"
version: "3"
services:
  web:
    image: beginor/geoserver:2.11.1
    container_name: geoserver-web
    hostname: geoserver-web
    ports:
      - 8080:8080
    volumes:
      - ./web/data_dir:/geoserver/data_dir
      - ./web/logs:/geoserver/logs
    restart: unless-stopped
    links:
      - database:database
  database:
    image: beginor/postgis:9.3
    container_name: postgis
    hostname: postgis
    ports:
      - 5432:5432
    volumes:
      - ./database/data:/var/lib/postgresql/data
    environment:
      POSTGRES_PASSWORD: 1q2w3e4R
    restart: unless-stopped
```

En este archivo YAML, se definen y se inician dos instancias, `web` y `database`.

## Instalación y configuración de Docker Compose

Docker Compose depende de Docker Engine, así que asegúrese de haber instalado el entorno de Docker Engine primero. Si aún no lo ha instalado, consulte el tutorial anterior: [**Conocimientos básicos de Docker**](https://wiki-power.com/es/Docker%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/) para instalar Docker Engine.

Si está utilizando el cliente de escritorio de Windows/MacOS/Linux, no es necesario instalar Docker Compose por separado, ya que ya está incluido. A continuación se describe cómo instalar Docker Compose en el entorno de Docker Engine de Linux.

Para Ubuntu y Debian, utilice el siguiente comando para instalar Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

Para las distribuciones de Linux basadas en RPM (como CentOS), utilice el siguiente comando para instalar Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

Después de la instalación, verifique si la instalación fue exitosa con el siguiente comando:

```shell
docker compose version
```

## Cómo usar Docker Compose

Por lo general, creamos un archivo `compose.yaml` (la versión anterior es `docker-compose.yml`, que también es compatible) y lo colocamos en un directorio nombrado según el nombre de la aplicación, como `web/compose.yaml`.

Para ejecutar este programa, simplemente ejecute el comando `docker compose up` en este directorio para iniciar los servicios según la configuración en el archivo YAML. (Agregar el parámetro `-d` ejecutará el servicio en segundo plano)

Para detener la ejecución del stack de la aplicación, simplemente use `docker compose down`.

## Cómo escribir un archivo Docker Compose

La forma predeterminada de abrir Docker Compose es crear un archivo en formato YAML, con el nombre predeterminado `compose.yaml`. A continuación se muestra una plantilla de ejemplo que incluye todos los parámetros disponibles (pero no es necesario usarlos todos):

```yaml title="compose.yaml"
version: "3"

services:
  service1:
    build:
      context: .
      dockerfile: Dockerfile
    image: your-image1
    command: ["python", "app.py"]
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    networks:
      - your-network
    environment:
      - ENV_VARIABLE=value
    depends_on:
      - db

  db:
    image: mysql:5.7
    environment:
      - MYSQL_ROOT_PASSWORD=yourpassword
    volumes:
      - db-data:/var/lib/mysql

networks:
  your-network:

volumes:
  your-volume:
  db-data:
```

En un archivo `compose.yaml`, generalmente incluimos los siguientes parámetros:

- **version**: Solo se utiliza para mostrar la información de la versión del archivo compose. Está relacionado con la versión de Docker Engine y las nuevas versiones pueden tener nuevas características o sintaxis. Consulte la documentación oficial [**Versiones de archivo Compose y actualización**](https://docs.docker.com/compose/compose-file/compose-versioning/).
- **services**: Define los diferentes servicios (contenedores) incluidos en este archivo compose. Cada servicio es un contenedor independiente y se pueden definir su imagen, mapeo de puertos, variables de entorno, etc.
- **container_name**: Nombre del contenedor, no es obligatorio, pero no puede haber nombres duplicados.
- **networks**: Define la configuración de red entre los servicios. Se pueden crear redes personalizadas y conectar los servicios a ellas para permitir la comunicación entre contenedores.
- **volumes**: Define la configuración de montaje de volúmenes del contenedor. Se pueden asociar los directorios o archivos del contenedor con los directorios o archivos del host para lograr la persistencia y el intercambio de datos. Equivalente al parámetro `-v` en la CLI de Docker.
- **environment** (o `env_file`): Especifica el nombre y la ruta del archivo de variables de entorno del contenedor. Si no se configuran variables de entorno, se pueden ignorar. Si las variables de entorno están en el directorio actual y se llaman `.env`, también se pueden omitir. Equivalente al parámetro `-e` en la CLI de Docker.
- **build**: Inicia el contenedor utilizando la imagen construida. Especifica la ruta del archivo Dockerfile.
- **image**: Especifica la imagen utilizada por el contenedor. Se pueden utilizar imágenes públicas del repositorio de imágenes o especificar un archivo Dockerfile local.
- **ports**: Define la relación de mapeo de puertos entre el contenedor y el host. También se puede especificar el protocolo de mapeo (TCP o UDP). Equivalente al parámetro `-p` en la CLI de Docker.
- **depends_on**: Define la relación de dependencia entre los servicios. Se pueden especificar uno o varios nombres de servicios, lo que indica que el servicio actual depende de que estos servicios se inicien.
- **restart**: Define la estrategia de reinicio del contenedor. Se puede establecer en `no` (no se reinicia automáticamente), `always` (siempre se reinicia automáticamente), `unless-stopped` (se reinicia automáticamente a menos que se detenga manualmente el contenedor) o `on-failure` (solo se reinicia automáticamente si falla). Equivalente al parámetro `--restart` en la CLI de Docker.
- **command**: Especifica el comando que se ejecutará al iniciar el contenedor. Se puede utilizar para anular el comando de inicio predeterminado de la imagen del contenedor.
- **volumes_from**: Especifica la fuente del contenedor de la que se deben montar los volúmenes.

## Algunos comandos comunes de Docker Compose

A continuación se muestran algunos comandos comunes de Docker Compose que se utilizan para administrar y operar los servicios definidos en el archivo `compose.yaml`:

- `docker compose up`: Construye las imágenes definidas en el archivo compose y arranca los contenedores. Si es necesario, construye automáticamente las imágenes (si el Dockerfile ha sido modificado) y arranca todos los servicios definidos. Si se desea arrancar en segundo plano, se debe añadir el parámetro `-d`.
- `docker compose down`: Detiene y elimina todos los contenedores, redes y volúmenes definidos en el archivo compose. Detiene los servicios en ejecución y limpia todos los recursos relacionados.
- `docker compose pull`: Descarga todas las imágenes definidas en el archivo compose, o las actualiza si ya existen.
- `docker compose start`: Arranca los contenedores ya creados en el archivo compose, sin crear nuevos contenedores ni construir nuevas imágenes.
- `docker compose stop`: Detiene los contenedores ya creados en el archivo compose, sin eliminarlos.
- `docker compose restart`: Reinicia los contenedores ya creados en el archivo compose.
- `docker compose pause`: Pausa los contenedores ya creados en el archivo compose, deteniendo temporalmente su ejecución.
- `docker compose unpause`: Reanuda los contenedores pausados en el archivo compose, permitiendo que continúen su ejecución.
- `docker compose ps`: Muestra el estado de **todos** los contenedores en ejecución definidos en el archivo compose.
- `docker compose logs`: Muestra los registros de salida de los contenedores definidos en el archivo compose.
- `docker compose exec`: Ejecuta comandos en los contenedores en ejecución definidos en el archivo compose. Por ejemplo, `docker exec -it [nombre-compose] /bin/bash`.

Estos son algunos de los comandos más comunes, pero se pueden encontrar más ejecutando `docker compose --help`.

## Variables de entorno

Aunque no son obligatorias en Docker Compose, se recomienda el uso de variables de entorno por las siguientes razones:

1. **Flexibilidad y configurabilidad**: Permite ajustar fácilmente la configuración de la aplicación sin necesidad de modificar las imágenes de Docker o reconstruir los contenedores.
2. **Seguridad y aislamiento**: Almacenar información sensible en variables de entorno en lugar de escribirla directamente en el código o en los archivos de configuración, y otorgar permisos específicos a las variables de entorno, puede mejorar la seguridad de la aplicación.
3. **Compatibilidad multiplataforma**: Diferentes sistemas operativos o plataformas pueden pasar diferentes configuraciones a través de variables de entorno, sin necesidad de modificar los archivos de configuración o el código de la imagen.
4. **Simplificación del despliegue y la gestión**: Al utilizar variables de entorno para configurar los parámetros de diferentes contenedores, se puede reducir la duplicación de contenido en los archivos de configuración, lo que hace que todo el proceso sea más claro y fácil de mantener.
5. **Integración y automatización**: Al combinar con herramientas de CI/CD y automatización, se pueden pasar automáticamente los parámetros de configuración de la aplicación a los contenedores de Docker, lo que permite la implementación y la integración automáticas.

Las variables de entorno se almacenan en un archivo con la extensión `.env`, que generalmente se crea en el mismo directorio que el archivo `compose.yaml`. A continuación se muestra un ejemplo:

```dotenv title=".env"
TAG=v1.5
```

Las variables de entorno se pueden llamar directamente en el archivo `compose.yaml`:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Consejos

Hay un sitio web llamado [**composerize**](https://www.composerize.com/) que convierte la CLI de Docker en YAML de Docker Compose. El resultado de la conversión no siempre es preciso y debe ser verificado.

## Referencias y agradecimientos

- [Usar docker compose en lugar de docker run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Explicación detallada de los parámetros del archivo de plantilla Docker-Compose](https://blog.51cto.com/14154700/2466054)
- [¡Resulta que también se puede usar Docker Compose en Synology NAS!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - De principiante a experto](https://docker-practice.github.io/zh-cn/)
- [Serie Docker - Comprender el archivo de configuración de Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

a_reemplazar[1]
a_reemplazar[2]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.