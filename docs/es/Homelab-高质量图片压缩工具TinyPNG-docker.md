# Homelab - Herramienta de compresión de imágenes de alta calidad TinyPNG-docker

![](https://media.wiki-power.com/img/20230416163137.png)

TinyPNG-docker es una herramienta que utiliza la API de TinyPNG para comprimir imágenes de alta calidad. Puede comprimir automáticamente imágenes WEBP, JPEG y PNG en la ruta especificada y guardarlas en la ruta deseada. Esto ayuda a reducir el ancho de banda, el tráfico y el tiempo de carga de un sitio web. Por cierto, esta es una aplicación Docker que desarrollé con la ayuda de ChatGPT.

## Despliegue (Docker Compose)

Primero, crea un archivo `compose.yaml` y reemplaza `${DIR}` con tu directorio local (por ejemplo, `/DATA/AppData`); reemplaza `${API}` con tu clave de API de TinyPNG:

```yaml title="compose.yaml"
version: "3"
services:
  tinypng-docker:
    image: linyuxuanlin/tinypng-docker
    environment:
      - TINYPNG_API_KEY=${API}
      - INPUT_DIR=/app/input
      - OUTPUT_DIR=/app/output
    volumes:
      - ${DIR}/tinypng-docker/input:/app/input
      - ${DIR}/tinypng-docker/output:/app/output
```

## Instrucciones de configuración

Antes de usar este contenedor Docker, debes registrarte en el sitio web de TinyPNG y solicitar una clave de API.

El uso es muy sencillo, simplemente coloca las imágenes que deseas comprimir en la carpeta `${DIR}/tinypng/input` y encontrarás las imágenes comprimidas en la carpeta `${DIR}/tinypng/output`.

Si el contenedor no funciona correctamente, puedes seguir estos pasos para solucionarlo:

1. Asegúrate de que las rutas de las carpetas `input` y `output` especificadas en el archivo `compose.yaml` sean correctas.
2. Verifica tu cuenta de TinyPNG para asegurarte de que no hayas alcanzado el límite máximo de compresiones permitidas por la clave de API.
3. Verifica que la carpeta `input` contenga archivos de imagen en el formato correcto (WebP, PNG, JPEG). Ten en cuenta que este contenedor solo detectará y comprimirá eventos de creación, por lo que si el archivo ya existe, deberás moverlo manualmente a la carpeta `input`.
4. Verifica si las imágenes que estás comprimiendo tienen una calidad superior a la configuración de compresión de la API, ya que esto puede provocar un fallo en la decodificación de la API (por ejemplo, si la imagen ya ha sido comprimida antes de la compresión inicial).
5. Intenta utilizar la herramienta de compresión de la API proporcionada por tinify en el sitio web de forma manual, subiendo las imágenes comprimidas para determinar el problema con mayor precisión. También puedes imprimir información de depuración en la consola para localizar el problema.

---

## Proceso de desarrollo de la imagen de Docker

### Preparación

1. Si aún no tienes una cuenta en Docker Hub, debes crear una cuenta en Docker Hub.

2. Inicia sesión en Docker Hub:

```shell
docker login
```

Sigue las instrucciones e introduce tu nombre de usuario y contraseña para iniciar sesión en Docker Hub.

### Creación del contenedor

Crea un archivo `Dockerfile`:

```Dockerfile title="Dockerfile"
FROM python:3.8-slim-buster

RUN pip install tinify watchdog

WORKDIR /app

COPY . /app

ENV TINYPNG_API_KEY=<your_tinypng_api_key>
ENV INPUT_DIR=/app/input
ENV OUTPUT_DIR=/app/output

CMD ["python", "main.py"]
```

Crea un archivo `main.py` en la misma ruta:

```py title="main.py"
import tinify
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Se ha recibido un evento de creación - %s." % event.src_path)
            source_path = event.src_path
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.basename(source_path))
            compress_image(source_path, output_path)

def compress_image(source_path, output_path):
    tinify.key = os.environ['TINYPNG_API_KEY']
    source = tinify.from_file(source_path)
    source.to_file(output_path)
    print(f"{source_path} comprimido y guardado en {output_path}")

if __name__ == "__main__":
    print("Observando nuevas imágenes...")
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, path=os.environ['INPUT_DIR'], recursive=False)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

Aquí se importan las bibliotecas de Python necesarias: tinify, os, time, sys, watchdog. Luego se define una clase llamada MyHandler que hereda de FileSystemEventHandler de watchdog.events. Esta clase contiene un método llamado on_created que se llama cuando se detecta la creación de un nuevo archivo en la carpeta especificada. La función on_created obtiene la ruta de la imagen de origen y la comprime en la ruta de salida especificada. Por último, se inicia la observación de la carpeta de entrada y, una vez que se detecta la creación de un nuevo archivo en la carpeta especificada, se realiza automáticamente la compresión y se guarda la imagen comprimida en la carpeta de salida especificada.

### Compilar el contenedor

Ejecute el siguiente comando en la misma ubicación que el archivo `Dockerfile` para compilar el contenedor:

```shell
docker build -t tinypng-docker .
```

Donde `tingpng-docker` es el nombre de la imagen que se va a construir y `.` es la ruta donde se encuentra el archivo `Dockerfile`.

### Etiquetar la imagen

Utilice el siguiente comando para etiquetar la imagen:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

Por ejemplo:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```

### Subir la imagen a Docker Hub

Utiliza el siguiente comando para subir la imagen a Docker Hub:

```shell
docker push <nombre-de-usuario-de-DockerHub>/<nombre-del-repositorio>:<etiqueta>
```

Por ejemplo:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### Descargar la imagen

Una vez que se haya subido, otras personas pueden descargar la imagen utilizando el siguiente comando:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## Referencias y Agradecimientos

- [Documentación](https://wiki-power.com/Homelab-%E9%AB%98%E8%B4%A8%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7TinyPNG-docker)
- [Repositorio de GitHub](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.
