# Docker Compose - Herramienta de Orquestación de Imágenes

![](https://img.wiki-power.com/d/wiki-media/img/20210117130925.jpg)

Docker Compose es una herramienta de orquestación de imágenes de Docker. Se recomienda utilizar Docker Compose como la forma predeterminada de abrir Docker, ya que no solo facilita la configuración y implementación de imágenes, sino que también permite configurar servicios de múltiples imágenes de manera más conveniente, incluso diferenciando su secuencia de inicio, algo que no es posible mediante la apertura con comandos.

A pesar de que la filosofía de Docker es la desacoplar (un proceso por imagen), mejorar la reutilización y evitar empaquetar varios servicios en una sola imagen, existen aplicaciones que requieren el inicio simultáneo de múltiples servicios. Por ejemplo, una aplicación web típica requiere al menos la coordinación entre el servidor y la base de datos. Esto significa que necesitas desplegar dos contenedores por separado, y en algunos casos, es necesario iniciarlos en un orden específico. Esto puede complicar la selección de imágenes y los pasos de operación necesarios.

Docker Compose reúne toda la información necesaria para invocar las imágenes (todos los atributos de los servicios necesarios, configuración de red y montaje de volúmenes) y su secuencia en un solo archivo YAML. Al ejecutar directamente este archivo de configuración, puedes iniciar los contenedores según tus necesidades y pasos sin tener que operar manualmente cada contenedor. A continuación, se muestra un ejemplo de Docker Compose utilizado para implementar un servicio web:

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

En este archivo YAML se definen e inician las instancias `web` y `database`.

## Instalación y Configuración de Docker Compose

Docker Compose depende de Docker Engine, así que asegúrate de haber instalado previamente el entorno de Docker Engine. Si aún no lo has hecho, puedes consultar el tutorial anterior: [**Conocimientos Básicos de Docker**](to_be_replace[3]) para instalar Docker Engine.

Si estás utilizando el cliente de escritorio de Windows/MacOS/Linux, no necesitas instalar Docker Compose por separado, ya que se incluye en el paquete. A continuación, se describen los pasos para instalar Docker Compose en un entorno de Linux con Docker Engine.

Para Ubuntu y Debian, utiliza los siguientes comandos para instalar Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

Para las distribuciones de Linux basadas en RPM, como CentOS, utiliza los siguientes comandos para instalar Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

Una vez completada la instalación, verifica su éxito mediante los siguientes comandos:

```shell
docker compose version
```

## How to Use Docker Compose

In general, we create a `compose.yaml` file (the older version is `docker-compose.yml`, which is also compatible) and place it in a directory named after the application, such as `web/compose.yaml`.

To run this program, simply execute the `docker compose up` command in this directory to start the services according to the configuration in the YAML file. (You can run it in the background by adding the `-d` parameter).

To stop the running application stack, use `docker compose down`.

## Writing Docker Compose Files

The default way to use Docker Compose is to create a YAML-formatted file, usually named `compose.yaml`. Here is a template example that includes all available parameters (although you don't necessarily have to use them all):

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

- **version**: Esta etiqueta se utiliza exclusivamente para mostrar la información de la versión del archivo `compose`. Está asociada a la versión del Docker Engine y las actualizaciones pueden incluir nuevas características o cambios en la sintaxis. Consulta la documentación oficial en [**Versiones de archivos Compose y actualizaciones**](https://docs.docker.com/compose/compose-file/compose-versioning/) para obtener más detalles.

- **services**: Aquí se definen los diferentes servicios (contenedores) que se incluirán en este archivo `compose`. Cada servicio es un contenedor independiente y se pueden definir aspectos como la imagen a utilizar, mapeo de puertos, variables de entorno, entre otros.

- **container_name**: El nombre del contenedor es opcional, pero no debe repetirse.

- **networks**: Esta sección define la configuración de redes entre los servicios. Puedes crear redes personalizadas y conectar servicios a estas redes para permitir la comunicación entre los contenedores.

- **volumes**: Aquí se especifican las configuraciones de montaje de volúmenes para los contenedores. Esto te permite asociar directorios o archivos del contenedor con directorios o archivos del host, lo que permite la persistencia de datos y el uso compartido. Equivale al parámetro `-v` en la línea de comandos de Docker.

- **environment** (o `env_file`): Se utiliza para especificar el nombre y la ubicación de un archivo que contiene las variables de entorno del contenedor. Si no se configuran variables de entorno, esto puede omitirse. Si el archivo de variables de entorno se llama `.env` y se encuentra en el directorio actual, también puede omitirse. Esto equivale al parámetro `-e` en la línea de comandos de Docker.

- **build**: Inicia el servicio utilizando una imagen que se ha construido previamente. Debes especificar la ruta del archivo Dockerfile.

- **image**: Define la imagen que utilizará el contenedor. Puedes usar imágenes de repositorios públicos o especificar un archivo Dockerfile local.

- **ports**: Esta etiqueta define las relaciones de mapeo de puertos entre el contenedor y el host. También puedes especificar el protocolo de mapeo (TCP o UDP). Equivale al parámetro `-p` en la línea de comandos de Docker.

- **depends_on**: Define las relaciones de dependencia entre los servicios. Puedes especificar uno o varios nombres de servicios, lo que significa que el servicio actual depende de que estos servicios se inicien primero.

- **restart**: Establece la estrategia de reinicio del contenedor. Puede configurarse como `no` (sin reinicio automático), `always` (reinicio siempre), `unless-stopped` (reinicio a menos que se detenga manualmente) o `on-failure` (reinicio solo en caso de fallo). Equivale al parámetro `--restart` en la línea de comandos de Docker.

- **command**: Se utiliza para especificar el comando que se ejecutará al iniciar el contenedor. Esto puede utilizarse para anular el comando de inicio predeterminado definido en la imagen del contenedor.

- **volumes_from**: Indica desde qué contenedor se deben montar los volúmenes en este contenedor.

## Algunos comandos comunes de Docker Compose

A continuación, se presentan algunos comandos comunes de Docker Compose que se utilizan para administrar y operar los servicios definidos en el archivo `compose.yaml`:

- `docker compose up`: Este comando construye las imágenes definidas en el archivo Compose y luego inicia los contenedores. Si es necesario, construirá automáticamente las imágenes (si el Dockerfile ha cambiado) y luego arrancará todos los servicios definidos. Si desea ejecutarlo en segundo plano, agregue el parámetro `-d`.

- `docker compose down`: Detiene y elimina todos los contenedores, redes y volúmenes definidos en el archivo Compose. Esto detendrá los servicios en ejecución y limpiará todos los recursos relacionados.

- `docker compose pull`: Este comando descarga todas las imágenes definidas en el archivo Compose, útil para actualizar las imágenes.

- `docker compose start`: Inicia los contenedores creados previamente en el archivo Compose sin volver a crearlos ni reconstruir las imágenes.

- `docker compose stop`: Detiene los contenedores previamente creados en el archivo Compose, pero no los elimina.

- `docker compose restart`: Reinicia los contenedores creados previamente en el archivo Compose.

- `docker compose pause`: Pausa temporalmente los contenedores previamente creados en el archivo Compose, deteniendo su ejecución.

- `docker compose unpause`: Reanuda los contenedores previamente pausados en el archivo Compose, permitiendo que continúen ejecutándose.

- `docker compose ps`: Muestra el estado de **todos** los contenedores en ejecución definidos en el archivo Compose.

- `docker compose logs`: Permite visualizar los registros de los contenedores definidos en el archivo Compose.

- `docker compose exec`: Ejecuta comandos dentro de los contenedores en ejecución definidos en el archivo Compose, por ejemplo, `docker exec -it [nombre-del-compose] /bin/bash`.

Estos son algunos de los comandos comunes. También puedes ejecutar `docker compose --help` para ver más comandos disponibles.

## Variables de entorno

En Docker Compose, aunque las variables de entorno no son obligatorias, se recomienda su uso debido a varias ventajas:

1. **Flexibilidad y configurabilidad**: Facilita el ajuste de la configuración de la aplicación sin necesidad de modificar imágenes de Docker o reconstruir contenedores.

2. **Seguridad e aislamiento**: Almacenar información sensible en variables de entorno en lugar de en código o archivos de configuración mejora la seguridad al permitir un control separado de las variables.

3. **Compatibilidad multiplataforma**: Las variables de entorno permiten pasar diferentes configuraciones en función del sistema operativo o plataforma, sin necesidad de modificar archivos de configuración o código de imágenes.

4. **Simplificación de implementación y gestión**: Utilizar variables de entorno para configurar parámetros de diferentes contenedores reduce la duplicación en archivos de configuración y facilita el mantenimiento.

5. **Integración y automatización**: Al combinar variables de entorno con herramientas de CI/CD y automatización, es posible automatizar la configuración de contenedores para implementación y pruebas.

Las variables de entorno se almacenan en un archivo con extensión `.env`, generalmente ubicado en el mismo directorio que el archivo `docker-compose.yaml`. Aquí tienes un ejemplo:

```dotenv title=".env"
TAG=v1.5
```

En el archivo `docker-compose.yaml`, puedes hacer referencia a las variables de entorno de la siguiente manera:

```yaml title="docker-compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Consejos

Existe un sitio web llamado [**composerize**](https://www.composerize.com/) que convierte comandos de Docker CLI en archivos YAML de Docker Compose. Sin embargo, ten en cuenta que los resultados de la conversión pueden no ser siempre precisos, por lo que se recomienda verificar el archivo resultante.

## Referencias y Agradecimientos


- [Sustituir el uso de `docker run` con Docker Compose](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Explicación detallada de los parámetros de los archivos de plantilla de Docker-Compose](https://blog.51cto.com/14154700/2466054)
- [¡Descubre cómo usar Docker Compose en Synology NAS!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker: Desde principiantes hasta la práctica](https://docker-practice.github.io/zh-cn/)
- [Serie sobre Docker: Comprender los archivos de configuración de Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

[por_reemplazar[1]]
[por_reemplazar[2]]

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.