# Docker Compose - Herramienta de Orquestación de Imágenes

![Imagen](https://media.wiki-power.com/img/20210117130925.jpg)

Docker Compose es una herramienta de orquestación de imágenes de Docker. Se recomienda utilizar Docker Compose como la forma predeterminada de trabajar con Docker, ya que no solo facilita la configuración y implementación de imágenes, sino que también permite configurar servicios con múltiples imágenes de manera más sencilla, incluso diferenciando su orden de inicio, algo que no se puede lograr con el uso de comandos convencionales.

Aunque la filosofía de Docker se basa en la desvinculación (un proceso por imagen), la mejora de la reutilización y no la encapsulación de múltiples servicios en una sola imagen, existen aplicaciones que requieren el inicio simultáneo de varios servicios. Por ejemplo, una aplicación web típica necesita, como mínimo, que el servidor y la base de datos funcionen en conjunto. Esto implica implementar dos contenedores por separado, e incluso algunos servicios deben iniciarse en un orden específico. Esto puede resultar en la necesidad de imágenes y pasos operativos bastante complejos.

Docker Compose almacena en un archivo YAML todas las imágenes requeridas, las propiedades de los contenedores, la configuración de red, así como la vinculación de volúmenes, y la secuencia de inicio, entre otros detalles. Al ejecutar este archivo de configuración, puedes implementar los contenedores de acuerdo a tus necesidades y pasos operativos, sin tener que manipular cada contenedor manualmente. A continuación, se muestra un ejemplo de Docker Compose utilizado para implementar un servicio web:

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

En este archivo YAML, se definen e inician las instancias `web` y `database`.

## Instalación y Configuración de Docker Compose

Docker Compose depende de Docker Engine, por lo que debes asegurarte de que ya has instalado el entorno de Docker Engine. Si aún no lo has hecho, puedes consultar el tutorial anterior: [**Conocimientos Básicos de Docker**](https://wiki-power.com/Docker%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/), para instalar Docker Engine.

Si estás utilizando el cliente de escritorio de Windows/MacOS/Linux, no es necesario instalar Docker Compose por separado, ya que ya está incluido. A continuación, se detallan los pasos para instalar Docker Compose en un entorno de Linux con Docker Engine.

Para Ubuntu y Debian, utiliza los siguientes comandos para instalar Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

Para distribuciones de Linux basadas en RPM (como CentOS), usa los siguientes comandos para instalar Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

Una vez completada la instalación, verifica su éxito mediante el siguiente comando:

```shell
docker-compose --version
```

Ahora estás listo para utilizar Docker Compose de manera eficiente en tu entorno Docker.

```shell
docker compose version
```

## Cómo usar Docker Compose

Normalmente, creamos un archivo `compose.yaml` (en versiones anteriores se llamaba `docker-compose.yml` y sigue siendo compatible) y lo colocamos en un directorio con el nombre de la aplicación, por ejemplo, `web/compose.yaml`.

Para ejecutar este programa, simplemente ejecute el comando `docker compose up` en este directorio para iniciar los servicios según la configuración en el archivo YAML. (Puede utilizar la opción `-d` para ejecutarlo en segundo plano).

Para detener la ejecución del conjunto de aplicaciones, utilice el comando `docker compose down`.

## Cómo escribir archivos de Docker Compose

La forma predeterminada de abrir archivos Docker Compose es crear un archivo en formato YAML con el nombre predeterminado `compose.yaml`. A continuación, se muestra una plantilla de ejemplo que incluye todos los parámetros disponibles (aunque no es necesario utilizarlos todos):

```yaml title="compose.yaml"
version: "3"

services:
  service1:
    build:
      context: .
      dockerfile: Dockerfile
    image: tu-imagen-1
    command: ["python", "app.py"]
    ports:
      - "8000:8000"
    volumes:
      - ./data:/app/data
    networks:
      - tu-red
    environment:
      - VARIABLE_DE_ENTORNO=valor
    depends_on:
      - db

  db:
    image: mysql:5.7
    environment:
      - MYSQL_ROOT_PASSWORD=tucontraseña
    volumes:
      - db-data:/var/lib/mysql

networks:
  tu-red:

volumes:
  tu-volumen:
  db-data:
```

En un archivo `compose.yaml`, generalmente incluirá los siguientes parámetros:

- **version**: Utilizado exclusivamente para mostrar la información de la versión del archivo Compose. Está relacionado con la versión de Docker Engine, y las versiones actualizadas pueden incluir nuevas características o sintaxis. Consulta la documentación oficial [**Versiones del archivo Compose y actualización**](https://docs.docker.com/compose/compose-file/compose-versioning/) para obtener más información.

- **services**: Define los distintos servicios (contenedores) incluidos en este archivo Compose. Cada servicio es un contenedor independiente y se pueden definir detalles como la imagen, el mapeo de puertos y las variables de entorno.

- **container_name**: Nombre del contenedor. No es obligatorio, pero debe ser único.

- **networks**: Define la configuración de red entre los servicios. Puedes crear redes personalizadas y conectar los servicios a estas redes para permitir la comunicación entre los contenedores.

- **volumes**: Define la configuración de montaje de volúmenes en los contenedores. Esto permite relacionar directorios o archivos en el contenedor con directorios o archivos en el sistema anfitrión, lo que facilita la persistencia de datos y el intercambio. Es equivalente al parámetro `-v` en la línea de comandos de Docker.

- **environment** (o `env_file`): Especifica el nombre y la ubicación del archivo de variables de entorno del contenedor. Esto permite cargar variables de entorno desde un archivo. Si no se configuran variables de entorno, este campo se puede omitir. Si el archivo de variables de entorno se encuentra en el directorio actual y se llama `.env`, también se puede omitir. Equivalente al parámetro `-e` en la línea de comandos de Docker.

- **build**: Inicia el contenedor utilizando una imagen construida a partir de un archivo Dockerfile. Debes especificar la ubicación del archivo Dockerfile.

- **image**: Especifica la imagen utilizada por el contenedor. Puedes usar imágenes de repositorios públicos o indicar un archivo Dockerfile local.

- **ports**: Define la relación de mapeo de puertos entre el contenedor y el host. También puedes especificar el protocolo de mapeo (TCP o UDP). Equivalente al parámetro `-p` en la línea de comandos de Docker.

- **depends_on**: Define las relaciones de dependencia entre los servicios. Puedes especificar uno o varios nombres de servicios a los que el servicio actual depende para su inicio.

- **restart**: Define la estrategia de reinicio del contenedor. Puede configurarse como `no` (no reiniciar automáticamente), `always` (reiniciar siempre), `unless-stopped` (reiniciar automáticamente, a menos que se detenga manualmente) o `on-failure` (reiniciar solo en caso de fallo). Equivalente al parámetro `--restart` en la línea de comandos de Docker.

- **command**: Especifica el comando que se ejecutará al iniciar el contenedor, lo que permite reemplazar el comando de inicio predeterminado definido en la imagen del contenedor.

- **volumes_from**: Indica la fuente de los volúmenes que el contenedor debe montar.

## Algunos comandos comunes de Docker Compose

Aquí tienes algunos comandos comunes de Docker Compose que se utilizan para administrar y operar los servicios definidos en el archivo `docker-compose.yaml`:

- `docker compose up`: Este comando construye las imágenes definidas en el archivo Compose y arranca los contenedores. Si es necesario, construirá automáticamente las imágenes (si el Dockerfile ha cambiado) y luego iniciará todos los servicios definidos. Para iniciar en segundo plano, agrega el parámetro `-d`.

- `docker compose down`: Detiene y elimina todos los contenedores, redes y volúmenes definidos en el archivo Compose. Esto detendrá los servicios en ejecución y limpiará todos los recursos relacionados.

- `docker compose pull`: Descarga todas las imágenes definidas en el archivo Compose, útil para actualizar las imágenes.

- `docker compose start`: Inicia los contenedores creados previamente en el archivo Compose sin recrear los contenedores ni reconstruir las imágenes.

- `docker compose stop`: Detiene los contenedores creados previamente en el archivo Compose sin eliminarlos.

- `docker compose restart`: Reinicia los contenedores creados previamente en el archivo Compose.

- `docker compose pause`: Pausa temporalmente los contenedores creados previamente en el archivo Compose, deteniendo su ejecución.

- `docker compose unpause`: Reanuda la ejecución de los contenedores que se habían pausado en el archivo Compose.

- `docker compose ps`: Muestra el estado de **todos** los contenedores en ejecución definidos en el archivo Compose.

- `docker compose logs`: Permite ver la salida de registro de los contenedores definidos en el archivo Compose.

- `docker compose exec`: Ejecuta comandos dentro de los contenedores en ejecución definidos en el archivo Compose. Por ejemplo, `docker exec -it [nombre-compose] /bin/bash`.

Estos son algunos comandos comunes, también puedes ejecutar `docker compose --help` para ver más comandos disponibles.

## Variables de entorno

En Docker Compose, aunque las variables de entorno no son obligatorias, se recomienda su uso por las siguientes razones:

1. **Flexibilidad y configuración**: Permite ajustar la configuración de la aplicación sin necesidad de modificar imágenes Docker o reconstruir contenedores.

2. **Seguridad y aislamiento**: Almacenar información sensible en variables de entorno en lugar de en código o archivos de configuración mejora la seguridad al permitir autorizaciones separadas para variables de entorno.

3. **Compatibilidad multiplataforma**: Diferentes sistemas operativos o plataformas pueden transmitir diferentes configuraciones a través de variables de entorno sin necesidad de modificar archivos de configuración o código de imágenes.

4. **Simplificación de implementación y gestión**: Usar variables de entorno de manera uniforme para configurar parámetros de diferentes contenedores reduce la duplicación en archivos de configuración, lo que facilita el mantenimiento.

5. **Integración y automatización**: Al combinarlas con herramientas de CI/CD y automatización, las variables de entorno pueden transmitir automáticamente parámetros de configuración de la aplicación a los contenedores Docker, facilitando la implementación y la integración automáticas.

Las variables de entorno se almacenan en un archivo con extensión `.env`, generalmente ubicado en el mismo directorio que el archivo `compose.yaml`. A continuación, se muestra un ejemplo:

```dotenv title=".env"
TAG=v1.5
```

En el archivo `compose.yaml`, puedes hacer referencia directa a las variables de entorno de la siguiente manera:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Consejos

Existe un sitio web llamado [**composerize**](https://www.composerize.com/) que convierte comandos de Docker CLI en archivos YAML de Docker Compose. Ten en cuenta que los resultados de la conversión pueden no ser siempre precisos y deberán ser verificados.

## Referencias y Agradecimientos

- [Sustituir `docker run` con Docker Compose](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Instalar Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Explicación detallada de los parámetros de los archivos de plantilla de Docker-Compose](https://blog.51cto.com/14154700/2466054)
- [¡Sorprendentemente, Synology también es compatible con Docker Compose!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker: Desde los conceptos básicos hasta la práctica](https://docker-practice.github.io/zh-cn/)
- [Serie sobre Docker: Comprender los archivos de configuración de Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
