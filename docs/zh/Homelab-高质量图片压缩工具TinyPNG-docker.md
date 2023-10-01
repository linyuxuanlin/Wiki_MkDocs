---
id: Homelab-高质量图片压缩工具TinyPNG-docker
title: Homelab - 高质量图片压缩工具 TinyPNG-docker
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416163137.png)

TinyPNG-docker 是一个调用 TinyPNG API 进行图片高质量压缩的工具，可以自动压缩指定路径下的 WEBP、JPEG 和 PNG 图片，然后输出到你想要的路径下。它能有效减少网站的带宽占用、流量和加载时间。顺带说一句，这是我借助 ChatGPT 开发的一个 Docker 应用。

## 部署（Docker Compose）

首先创建 `compose.yaml` ，并将以下的 `${DIR}` 替换为本地的目录（例如 `/DATA/AppData`）；将 `${API}` 替换为自己申请的 TinyPNG 密钥：

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

## 配置说明

使用这个 Docker 容器前，你需要先在 TinyPNG 官网上注册一个账户，并申请获取一个 API 密钥。

使用方法很简单，把需要压缩的图片贴进 `${DIR}/tinypng/input` 文件夹中，就能在 `${DIR}/tinypng/output` 文件夹找到压缩后的图片了。

如果容器无法正常使用，可以用以下的方法排除：

1. 确保 `compose.yaml` 文件中指定的 `input` 和 `output` 文件夹路径正确。
2. 检查你的 TinyPNG 账户，是否已达到 API 密钥允许的最大压缩次数。
3. 检查 `input` 文件夹是否包含正确格式的图像文件（WebP, PNG, JPEG）。注意，此容器只会检测并压缩 `created` 事件，因此如果文件已经存在，则需要手动将其移到 `input` 目录当中。
4. 检查压缩的图片是否在失真度上高于 API 的压缩设置，可能导致 API 解码失败（例如压缩前的图片已经压缩过）。
5. 尝试手动使用 tinify 官网提供的 API 压缩工具，上传压缩后的图片以进一步确定问题的所在，同时你可以在控制台输出调试信息定位问题。

---

## Docker 镜像开发流程

### 准备工作

1. 如还未注册 Docker Hub 账户，则需要先在 Docker Hub 上创建一个账户。

2. 登录 Docker Hub：

```shell
docker login
```

根据提示输入用户名和密码，登录到 Docker Hub。

### 创建容器

创建 `Dockerfile` 文件：

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

在相同路径下创建 `main.py`：

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

这里首先导入必需的 Python 库：tinify，os，time，sys，watchdog。随后定义了一个名为 MyHandler 的类，继承自 watchdog.events.FileSystemEventHandler。这个类包含一个 on_created 方法，当监测到指定文件夹下有新文件被创建时会被调用。on_created 函数获取源图像的路径，并将其压缩到指定的输出路径。最后开始监测输入文件夹，一旦检测到指定文件夹下有新文件被创建，就会自动执行压缩操作，并将压缩后的图像输出到指定的输出文件夹。

### 编译容器

在 `Dockerfile` 相同路径下执行以下命令编译容器：

```shell
docker build -t tinypng-docker .
```

其中，`tingpng-docker` 为要构建的镜像名称，`.` 为 `Dockerfile` 文件所在的路径。

### 为镜像打标签

使用以下命令为镜像打标签：

```shell
docker tag <image-name> <dockerhub-username>/<repository-name>:<tag>
```

例如：

```shell
docker tag tinypng-docker linyuxuanlin/tinypng-docker:latest
```

### 推送镜像到 Docker Hub

使用以下命令将镜像上传到 Docker Hub：

```shell
docker push <dockerhub-username>/<repository-name>:<tag>

```

例如：

```shell
docker push linyuxuanlin/tinypng-docker:latest
```

### 拉取镜像

上传完成后，其他人便可以通过以下命令拉取镜像：

```shell
docker pull linyuxuanlin/tinypng-docker:latest
```

## 参考与致谢

- [文档](https://wiki-power.com/Homelab-%E9%AB%98%E8%B4%A8%E9%87%8F%E5%9B%BE%E7%89%87%E5%8E%8B%E7%BC%A9%E5%B7%A5%E5%85%B7TinyPNG-docker)
- [GitHub repo](https://github.com/linyuxuanlin/Dockerfiles/tree/main/tinypng-docker)
- [Docker Hub](https://hub.docker.com/r/linyuxuanlin/tinypng-docker)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
