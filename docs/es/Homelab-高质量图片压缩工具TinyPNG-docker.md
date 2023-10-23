# Homelab - Herramienta de compresión de imágenes TinyPNG-docker de alta calidad

![Imagen](https://img.wiki-power.com/d/wiki-media/img/20230416163137.png)

TinyPNG-docker es una herramienta que utiliza la API de TinyPNG para comprimir imágenes de alta calidad. Puede comprimir automáticamente imágenes WEBP, JPEG y PNG ubicadas en la ruta especificada y guardarlas en la ubicación que desees. Esto ayuda a reducir el consumo de ancho de banda, el tráfico y el tiempo de carga de tu sitio web. Por cierto, esta es una aplicación Docker que desarrollé con la ayuda de ChatGPT.

## Implementación (Docker Compose)

Primero, crea un archivo `compose.yaml` y reemplaza `${DIR}` por la ruta local (por ejemplo, `/DATA/AppData`) y `${API}` por tu propia clave de API de TinyPNG:

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

La forma de uso es sencilla: coloca las imágenes que deseas comprimir en la carpeta `${DIR}/tinypng/input` y encontrarás las imágenes comprimidas en la carpeta `${DIR}/tinypng/output`.

Si el contenedor no funciona correctamente, puedes seguir estos pasos de solución:

1. Asegúrate de que las rutas de las carpetas `input` y `output` especificadas en el archivo `compose.yaml` sean correctas.
2. Verifica tu cuenta de TinyPNG para asegurarte de que no hayas alcanzado el límite de compresiones permitido por la clave de API.
3. Asegúrate de que la carpeta `input` contenga archivos de imagen con el formato correcto (WebP, PNG, JPEG). Ten en cuenta que este contenedor solo detectará y comprimirá eventos de creación, por lo que deberás mover manualmente los archivos existentes a la carpeta `input`.
4. Comprueba que las imágenes que intentas comprimir no tengan una calidad superior a la configuración de compresión de la API, ya que esto podría causar un fallo en la decodificación de la API (por ejemplo, si las imágenes ya han sido comprimidas previamente).
5. Puedes intentar utilizar la herramienta de compresión de API proporcionada por Tinify en su sitio web de forma manual para identificar y solucionar el problema, y también puedes ver la información de depuración en la consola para localizar el problema.

---

## Proceso de desarrollo de la imagen de Docker

### Preparación

1. Si aún no has registrado una cuenta en Docker Hub, debes crear una cuenta en Docker Hub primero.

2. Inicia sesión en Docker Hub:

```shell
docker login
```

Sigue las indicaciones e ingresa tu nombre de usuario y contraseña para iniciar sesión en Docker Hub.

### Creación del contenedor

Crea un archivo `Dockerfile`:

```Dockerfile title="Dockerfile"
FROM python:3.8-slim-buster

RUN pip install tinify watchdog

WORKDIR /app

COPY . /app

ENV TINYPNG_API_KEY=<tu_clave_de_API_de_TinyPNG>
ENV INPUT_DIR=/app/input
ENV OUTPUT_DIR=/app/output

CMD ["python", "main.py"]
```

Luego, crea un archivo `main.py` en la misma ubicación:

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
            print("Evento de creación detectado - %s." % event.src_path)
            source_path = event.src_path
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.basename(source_path))
            comprimir_imagen(source_path, output_path)

def comprimir_imagen(source_path, output_path):
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

En este código, primero importamos las bibliotecas de Python necesarias: tinify, os, time, sys y watchdog. Luego, definimos una clase llamada MyHandler que hereda de FileSystemEventHandler de watchdog. Esta clase contiene un método on_created, que se llama cuando se detecta la creación de un nuevo archivo en la carpeta especificada. El método on_created obtiene la ruta de origen de la imagen y la comprime en la ruta de salida especificada. Finalmente, iniciamos la observación de la carpeta de entrada, y cuando se detecta la creación de un nuevo archivo en esa carpeta, se ejecuta automáticamente la compresión y se guarda la imagen comprimida en la carpeta de salida especificada.

### Compilación del contenedor

Para compilar el contenedor, ejecute el siguiente comando en la misma ubicación que el archivo Dockerfile:

```shell
docker build -t tinypng-docker .
```

Donde "tingpng-docker" es el nombre de la imagen que se va a construir, y "." representa la ubicación del archivo Dockerfile.

### Etiquetar la imagen

Use el siguiente comando para etiquetar la imagen:

```shell
docker tag <nombre-de-la-imagen> <nombre-de-usuario-de-DockerHub>/<nombre-del-repositorio>:<etiqueta>
```

Por ejemplo:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```
```

### Subir una imagen a Docker Hub

Utiliza el siguiente comando para cargar la imagen en Docker Hub:

```shell
docker push <nombre-de-usuario-de-dockerhub>/<nombre-del-repositorio>:<etiqueta>
```

Por ejemplo:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### Descargar una imagen

Una vez que la carga esté completa, otras personas pueden descargar la imagen mediante el siguiente comando:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## Referencias y Agradecimientos

- [Documentación](to_be_replace[3])
- [Repositorio en GitHub](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> Dirección original del artículo: <https://wiki-power.com/>
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.