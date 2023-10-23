# Homelab - High-Quality Image Compression Tool TinyPNG-docker

![](https://img.wiki-power.com/d/wiki-media/img/20230416163137.png)

TinyPNG-docker is a tool that utilizes the TinyPNG API for high-quality image compression. It automatically compresses WEBP, JPEG, and PNG images located in a specified directory and outputs them to your desired destination. This tool is effective in reducing website bandwidth usage, traffic, and loading times. By the way, this is a Docker application I developed with the help of ChatGPT.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and replace `${DIR}` with your local directory (e.g., `/DATA/AppData`) and `${API}` with your obtained TinyPNG API key:

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

Before using this Docker container, you need to register an account on the TinyPNG website and obtain an API key.

The usage is straightforward. Place the images you want to compress in the `${DIR}/tinypng/input` folder, and you will find the compressed images in the `${DIR}/tinypng/output` folder.

If the container is not functioning correctly, you can troubleshoot using the following steps:

1. Ensure that the paths for `input` and `output` folders specified in the `compose.yaml` file are correct.
2. Check your TinyPNG account to see if you have reached the maximum compression limit allowed by the API key.
3. Verify that the `input` folder contains image files in the correct formats (WebP, PNG, JPEG). Please note that this container only detects and compresses files created after the container is started, so you may need to manually move existing files into the `input` directory.
4. Check if the image compression level is higher than the API's compression settings, as this may lead to API decoding failure (e.g., if the images were already compressed before).
5. Try manually using the API compression tool provided by Tinify's website, uploading the compressed images to further pinpoint the issue and utilize console output for debugging.

---

## Docker Image Development Process

### Preparation

1. If you haven't registered a Docker Hub account yet, you need to create one on Docker Hub.

2. Log in to Docker Hub:

```shell
docker login
```

Follow the prompts to enter your username and password and log in to Docker Hub.

### Creating the Container

Create a `Dockerfile`:

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

Create a `main.py` file in the same directory:

[Original content of the 'main.py' file should be provided here]

```markdown
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
            print("Received created event - %s." % event.src_path)
            source_path = event.src_path
            output_path = os.path.join(os.environ['OUTPUT_DIR'], os.path.basename(source_path))
            compress_image(source_path, output_path)

def compress_image(source_path, output_path):
    tinify.key = os.environ['TINYPNG_API_KEY']
    source = tinify.from_file(source_path)
    source.to_file(output_path)
    print(f"{source_path} compressed and saved to {output_path}")

if __name__ == "__main__":
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
```

Here, we start by importing the necessary Python libraries: tinify, os, time, sys, and watchdog. Then, we define a class named MyHandler, which inherits from watchdog.events.FileSystemEventHandler. This class contains an on_created method that is called when a new file is created in the specified folder. The on_created function retrieves the path of the source image and compresses it to the specified output path. Finally, we begin monitoring the input folder, and whenever a new file is created in the specified folder, it automatically performs the compression operation and saves the compressed image to the specified output folder.

### Build the Container

To build the container, execute the following command in the same directory as the Dockerfile:

```shell
docker build -t tinypng-docker .
```

In this command, `tinypng-docker` is the name of the image you want to build, and `.` represents the path where the Dockerfile is located.

### Tag the Image

Use the following command to tag the image:

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

For example:

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```
```

### Pushing Images to Docker Hub

To upload your image to Docker Hub, you can use the following command:

```shell
docker push <dockerhub-username>/<repository-name>:<tag>
```

For example:

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### Pulling Images

Once the upload is complete, others can pull the image using the following command:

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## References and Acknowledgments

- [Documentation](to_be_replace[3]) on setting up a high-quality image compression tool using TinyPNG in a Homelab environment.
- [GitHub repository](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker) for the Dockerfiles used in this project.
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker) repository for the Docker image.

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.