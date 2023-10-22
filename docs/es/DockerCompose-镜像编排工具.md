# Docker Compose - Herramienta de orquestación de imágenes

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20210117130925.jpg)

Docker Compose es una herramienta de orquestación de imágenes de Docker. Se recomienda usar Docker Compose como la forma predeterminada de abrir Docker, ya que no solo facilita la configuración y implementación de imágenes, sino que también permite configurar servicios con múltiples imágenes de manera más conveniente e incluso diferenciar su secuencia de inicio, lo que no es posible con el método de línea de comandos.

Aunque la filosofía de Docker es la desvinculación (un proceso por imagen), aumentar la reutilización y no encapsular múltiples servicios en una sola imagen, hay aplicaciones que requieren el inicio simultáneo de varios servicios. Por ejemplo, una aplicación web típica necesita la colaboración de un servidor y una base de datos. Esto significa que debes implementar dos contenedores por separado, e incluso algunos servicios deben iniciarse en un orden específico. Esto puede complicar el proceso y las operaciones necesarias con imágenes.

Docker Compose reúne en un archivo YAML todo lo que se necesita para invocar las imágenes (todas las propiedades de los servicios necesarios, configuración de contenedores, redes y montaje de volúmenes). Al ejecutar directamente este archivo de configuración, puedes iniciar los contenedores de acuerdo a tus necesidades y pasos sin necesidad de operaciones manuales en cada contenedor. A continuación, se muestra un ejemplo de Docker Compose utilizado para implementar un servicio web:

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

En este archivo YAML, se definen y se inician las instancias `web` y `database`.

## Instalación y configuración de Docker Compose

Docker Compose depende de Docker Engine, por lo que asegúrate de tener Docker Engine instalado antes. Si aún no lo tienes, puedes consultar el tutorial anterior: [**Conceptos básicos de Docker**](to_be_replace[3]) para instalar Docker Engine.

Si estás utilizando el cliente de escritorio de Windows/MacOS/Linux, no es necesario instalar Docker Compose por separado, ya que ya está incluido. A continuación, se describen los métodos de instalación de Docker Compose en un entorno de Docker Engine en Linux.

Para Ubuntu y Debian, utiliza los siguientes comandos para instalar Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

Para distribuciones de Linux basadas en RPM, como CentOS, utiliza los siguientes comandos para instalar Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

Después de completar la instalación, verifica si se instaló correctamente mediante el siguiente comando:

```shell
docker compose version
```

## How to Use Docker Compose

Usually, we create a `compose.yaml` file (in older versions, it was `docker-compose.yml`, and it's still compatible) and place it in a directory named after the application, like `web/compose.yaml`.

To run this program, simply execute the `docker compose up` command in this directory to start the services according to the configuration in the YAML file. (You can run it in the background by adding the `-d` parameter.)

To stop the running application stack, use `docker compose down`.

## Writing Docker Compose Files

The default way to open Docker Compose is by creating a YAML format file, usually named `compose.yaml`. Below is a template example that includes all available parameters (though not all of them are necessarily required):

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

In a `compose.yaml` file, you typically include the following parameters:

- **version**: This is solely used to display the version information of the compose file. It is associated with the version of Docker Engine, and updated versions may introduce new features or syntax. Please refer to the official documentation [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/).

- **services**: Defines the various services (containers) included in this compose file. Each service represents an independent container and can be configured with its image, port mappings, environment variables, and more.

- **container_name**: Container name, not mandatory but must be unique.

- **networks**: Specifies the network configuration between services. Custom networks can be created, and services can be connected to these networks to facilitate communication between containers.

- **volumes**: Defines the configuration for mounting volumes in containers. This allows associating container directories or files with directories or files on the host, enabling data persistence and sharing. This is equivalent to the `-v` parameter in the Docker CLI.

- **environment** (or `env_file`): Specifies the file name and path for container environment variables, indicating that these variables should be loaded from this file. If no environment variables are configured, this can be omitted. If the environment variables are located in the current directory and named `.env`, it can also be omitted. This is equivalent to the `-e` parameter in the Docker CLI.

- **build**: Launches using a built image and specifies the path to the Dockerfile.

- **image**: Specifies the image used by the container. You can use images from public image repositories or specify a local Dockerfile.

- **ports**: Defines the mapping of ports between the container and the host, and can also specify the mapping protocol (TCP or UDP). This is equivalent to the `-p` parameter in the Docker CLI.

- **depends_on**: Defines the dependencies between services. You can specify one or more service names, indicating that the current service depends on the startup of these services.

- **restart**: Specifies the container's restart strategy, which can be set to `no` (no automatic restart), `always` (always automatically restart), `unless-stopped` (automatic restart unless the container is manually stopped), or `on-failure` (automatic restart only in case of failure). This is equivalent to the `--restart` parameter in the Docker CLI.

- **command**: Specifies the command to be executed when the container starts. This can be used to override the default startup command in the container image.

- **volumes_from**: Specifies the source container from which the container should mount volumes.

## Some Common Docker Compose Commands

Here are some common Docker Compose commands for managing and operating the services defined in the `compose.yaml` file:

- `docker compose up`: Este comando construye las imágenes definidas en el archivo Compose y pone en marcha los contenedores. Si es necesario, construirá automáticamente las imágenes (si el Dockerfile ha sido modificado) y luego iniciará todos los servicios definidos. Para ejecutar en segundo plano, añade el parámetro `-d`.

- `docker compose down`: Detiene y elimina todos los contenedores, redes y volúmenes definidos en el archivo Compose. Detendrá los servicios en ejecución y limpiará todos los recursos relacionados.

- `docker compose pull`: Descarga todas las imágenes definidas en el archivo Compose o las actualiza si es necesario.

- `docker compose start`: Inicia los contenedores ya creados en el archivo Compose sin recrearlos ni reconstruir las imágenes.

- `docker compose stop`: Detiene los contenedores ya creados en el archivo Compose sin eliminarlos.

- `docker compose restart`: Reinicia los contenedores ya creados en el archivo Compose.

- `docker compose pause`: Pausa temporalmente los contenedores creados en el archivo Compose, deteniendo su ejecución.

- `docker compose unpause`: Reanuda los contenedores previamente pausados en el archivo Compose, permitiéndoles continuar su ejecución.

- `docker compose ps`: Muestra el estado de **todos** los contenedores en ejecución definidos en el archivo Compose.

- `docker compose logs`: Visualiza la salida de registros de los contenedores en el archivo Compose.

- `docker compose exec`: Ejecuta comandos en los contenedores en ejecución del archivo Compose. Por ejemplo, `docker exec -it [nombre-de-compose] /bin/bash`.

Estos son comandos comunes, y puedes ejecutar `docker compose --help` para ver más comandos disponibles.

## Variables de entorno

En Docker Compose, aunque las variables de entorno no son obligatorias, se recomienda su uso por varias razones:

1. **Flexibilidad y configurabilidad**: Permite ajustar fácilmente la configuración de la aplicación sin necesidad de modificar las imágenes de Docker o reconstruir los contenedores.

2. **Seguridad y aislamiento**: Almacenar información sensible en variables de entorno en lugar de escribirla directamente en código o archivos de configuración mejora la seguridad de la aplicación al permitir un control separado sobre las variables.

3. **Compatibilidad multiplataforma**: Diferentes sistemas operativos o plataformas pueden pasar diferentes configuraciones a través de variables de entorno sin necesidad de modificar archivos de configuración o código de imagen.

4. **Simplificación de implementación y gestión**: La utilización uniforme de variables de entorno para configurar los parámetros de diferentes contenedores reduce la redundancia en los archivos de configuración, lo que facilita el mantenimiento.

5. **Integración y automatización**: Al combinar variables de entorno con herramientas de CI/CD y automatización, es posible automatizar la transferencia de parámetros de configuración a los contenedores Docker, lo que facilita la implementación y la integración.

Las variables de entorno se almacenan en un archivo con extensión `.env`, que generalmente se crea en el mismo directorio que el archivo `compose.yaml`. Aquí tienes un ejemplo:

```dotenv title=".env"
TAG=v1.5
```

En el archivo `compose.yaml`, puedes hacer referencia directa a las variables de entorno:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Consejos

Existe un sitio web llamado [**composerize**](https://www.composerize.com/) que convierte comandos de Docker CLI en archivos Docker Compose YAML. Ten en cuenta que la precisión de la conversión puede variar y debe verificarse.

## Referencias y Agradecimientos

- [Sustituir `docker run` con Docker Compose](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Explicación detallada de los parámetros de los archivos de plantilla de Docker-Compose](https://blog.51cto.com/14154700/2466054)
- [¡Descubre cómo usar Docker Compose en Synology NAS!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker: De principiante a experto](https://docker-practice.github.io/zh-cn/)
- [Serie sobre Docker: Comprender los archivos de configuración de Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

[Reemplazo[1]]
[Reemplazo[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.