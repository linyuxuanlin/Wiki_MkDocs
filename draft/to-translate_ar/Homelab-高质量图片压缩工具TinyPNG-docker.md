# Homelab - Herramienta de compresión de imágenes de alta calidad TinyPNG-docker

![](https://f004.backblazeb2.com/file/wiki-media/img/20230416163137.png)

TinyPNG-docker es una herramienta que utiliza la API de TinyPNG para comprimir imágenes de alta calidad. Puede comprimir automáticamente imágenes WEBP, JPEG y PNG en la ruta especificada y luego guardarlas en la ruta deseada. Esto puede reducir efectivamente el ancho de banda, el tráfico y el tiempo de carga del sitio web. Por cierto, esta es una aplicación Docker que desarrollé con la ayuda de ChatGPT.

## Implementación (Docker Compose)

Primero, cree `compose.yaml` y reemplace `${DIR}` con el directorio local (por ejemplo, `/DATA/AppData`); reemplace `${API}` con su propia clave de API de TinyPNG:

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

Antes de usar este contenedor Docker, debe registrarse en el sitio web de TinyPNG y solicitar una clave de API.

El uso es muy simple, simplemente coloque las imágenes que necesita comprimir en la carpeta `${DIR}/tinypng/input`, y encontrará las imágenes comprimidas en la carpeta `${DIR}/tinypng/output`.

Si el contenedor no se puede usar normalmente, puede excluirlo de la siguiente manera:

1. Asegúrese de que la ruta de la carpeta `input` y `output` especificada en el archivo `compose.yaml` sea correcta.
2. Verifique su cuenta de TinyPNG para ver si ha alcanzado el número máximo de compresiones permitidas por la clave de API.
3. Verifique si la carpeta `input` contiene archivos de imagen con el formato correcto (WebP, PNG, JPEG). Tenga en cuenta que este contenedor solo detectará y comprimirá eventos `created`, por lo que si el archivo ya existe, debe moverlo manualmente a la carpeta `input`.
4. Verifique si las imágenes comprimidas tienen una tasa de distorsión mayor que la configuración de compresión de la API, lo que puede provocar un fallo en la decodificación de la API (por ejemplo, si la imagen antes de la compresión ya se ha comprimido).
5. Intente usar la herramienta de compresión de la API proporcionada por Tinify para cargar las imágenes comprimidas y determinar el problema. También puede imprimir información de depuración en la consola para localizar el problema.

---

## Proceso de desarrollo de la imagen Docker

### Preparación

1. Si aún no ha registrado una cuenta de Docker Hub, primero debe crear una cuenta en Docker Hub.

2. Inicie sesión en Docker Hub:

```shell
docker login
```

Ingrese su nombre de usuario y contraseña según las instrucciones para iniciar sesión en Docker Hub.

### Crear contenedor

Cree el archivo `Dockerfile`:

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

Cree `main.py` en la misma ruta:

```python
import os
import tinify
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

tinify.key = os.environ.get('TINYPNG_API_KEY')

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return
        print(f'Compressing {event.src_path}...')
        source = tinify.from_file(event.src_path)
        source.to_file(event.src_path.replace(os.environ.get('INPUT_DIR'), os.environ.get('OUTPUT_DIR')))
        print(f'Compressed {event.src_path} successfully.')

if __name__ == "__main__":
    event_handler = MyHandler()
    observer = Observer()
    observer.schedule(event_handler, os.environ.get('INPUT_DIR'), recursive=True)
    observer.start()
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
```

¡Listo! Ahora puede construir y publicar su imagen Docker en Docker Hub.

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
            print("Evento creado recibido - %s." % event.src_path)
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

Aquí se importan las bibliotecas de Python necesarias: tinify, os, time, sys, watchdog. Luego se define una clase llamada MyHandler, que hereda de watchdog.events.FileSystemEventHandler. Esta clase contiene un método llamado on_created, que se llama cuando se crea un nuevo archivo en la carpeta especificada. La función on_created obtiene la ruta de la imagen de origen y la comprime en la ruta de salida especificada. Finalmente, comienza a observar la carpeta de entrada y, una vez que se detecta un nuevo archivo en la carpeta especificada, se ejecuta automáticamente la operación de compresión y se guarda la imagen comprimida en la carpeta de salida especificada.

### Compilar el contenedor

Ejecute el siguiente comando para compilar el contenedor en la misma ruta que el archivo `Dockerfile`:

```shell
docker build -t tinypng-docker .
```

Donde `tingpng-docker` es el nombre de la imagen que se va a construir y `.` es la ruta del archivo `Dockerfile`.

### Etiquetar la imagen

Use el siguiente comando para etiquetar la imagen:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

Por ejemplo:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```

### Subir una imagen a Docker Hub

Utilice el siguiente comando para subir una imagen a Docker Hub:

```shell
docker push <nombre-de-usuario-de-dockerhub>/<nombre-del-repositorio>:<etiqueta>

```

Por ejemplo:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### Descargar una imagen

Una vez que se haya subido la imagen, otros usuarios pueden descargarla con el siguiente comando:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## Referencias y agradecimientos

- [Documentación](https://wiki-power.com/es/Homelab-%E9%AB%98%E8%B4%A8%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7TinyPNG-docker)
- [Repositorio de GitHub](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> Dirección original del artículo: <https://wiki-power.com/>  
> Este artículo está protegido por la licencia [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh). Si desea reproducirlo, por favor indique la fuente.

> Este post está traducido usando ChatGPT, por favor [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) si hay alguna omisión.