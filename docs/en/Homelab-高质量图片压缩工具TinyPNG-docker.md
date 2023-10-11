# Homelab - High-quality image compression tool TinyPNG-docker

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416163137.png)

TinyPNG-docker is a tool that uses the TinyPNG API to compress images with high quality. It can automatically compress WEBP, JPEG, and PNG images in the specified path and output them to the desired path. It can effectively reduce website bandwidth usage, traffic, and loading time. By the way, this is a Docker application I developed with the help of ChatGPT.

## Deployment (Docker Compose)

First, create `compose.yaml` and replace `${DIR}` with the local directory (e.g. `/DATA/AppData`); replace `${API}` with your own TinyPNG key:

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

## Configuration Instructions

Before using this Docker container, you need to register an account on the TinyPNG website and apply for an API key.

The usage is simple, paste the images to be compressed into the `${DIR}/tinypng/input` folder, and you can find the compressed images in the `${DIR}/tinypng/output` folder.

If the container cannot be used normally, you can use the following methods to troubleshoot:

1. Ensure that the `input` and `output` folder paths specified in the `compose.yaml` file are correct.
2. Check your TinyPNG account to see if you have reached the maximum compression limit allowed by the API key.
3. Check if the `input` folder contains image files in the correct format (WebP, PNG, JPEG). Note that this container only detects and compresses `created` events, so if the file already exists, you need to manually move it to the `input` directory.
4. Check if the compressed images have a higher level of distortion than the API's compression settings, which may cause the API to fail to decode (e.g. if the image was already compressed before compression).
5. Try using the API compression tool provided by tinify's official website manually, upload the compressed image to further determine the problem, and output debugging information in the console to locate the problem.

---

## Docker Image Development Process

### Preparation

1. If you have not registered a Docker Hub account yet, you need to create one on Docker Hub first.

2. Log in to Docker Hub:

```shell
docker login
```

Enter your username and password as prompted to log in to Docker Hub.

### Create Container

Create the `Dockerfile`:

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

Create `main.py` in the same path:

```py title="main.py"
import tinify
import os
import time
import sys
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
```

The following is a Python script that uses the FileSystemEventHandler class to monitor a directory for newly created files. When a file is created, the on_created method is called. If the event is not a directory and is of type 'created', the script compresses the image using the TinyPNG API and saves it to the specified output directory.

```python
import os
import tinify
from watchdog.events import FileSystemEventHandler

class MyHandler(FileSystemEventHandler):
    def on_created(self, event):
        if event.is_directory:
            return None
        elif event.event_type == 'created':
            print("Received created event - %s." % event.src_path)
            source_path = event.src_path
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.basename(source_path))
            compress_image(source_path, output_path)

def compress_image(source_path, output_path):
    tinify.key = os.environ['TINYPNG_API_KEY']
    source = tinify.from_file(source_path)
    source.to_file(output_path)
    print(f"{source_path} compressed and saved to {output_path}")
```

Note that the script requires the TinyPNG API key to be set as an environment variable named 'TINYPNG_API_KEY', and the output directory to be set as an environment variable named 'OUTPUT_DIR'.

if **name** == "**main**":
print("Watching for new images...")
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

First, the necessary Python libraries are imported: tinify, os, time, sys, and watchdog. Then, a class named MyHandler is defined, which inherits from watchdog.events.FileSystemEventHandler. This class contains an on_created method, which is called when a new file is created in the specified folder. The on_created function gets the path of the source image and compresses it to the specified output path. Finally, the input folder is monitored, and once a new file is detected in the specified folder, the compression operation is automatically executed, and the compressed image is output to the specified output folder.

### Building the Container

Execute the following command to build the container in the same path as the `Dockerfile`:

```shell
docker build -t tinypng-docker .
```

Here, `tingpng-docker` is the name of the image to be built, and `.` is the path where the `Dockerfile` is located.

### Tagging the Image

Use the following command to tag the image:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

For example:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```

### Pushing the Image to Docker Hub

Use the following command to upload the image to Docker Hub:

```shell
docker push <dockerhub-username>/<repository-name>:<tag>

```

For example:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### Pull the image

After uploading, others can pull the image with the following command:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## References and Acknowledgments

- [Documentation](https://wiki-power.com/en/Homelab-%E9%AB%98%E8%B4%A8%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7TinyPNG-docker)
- [GitHub repo](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
