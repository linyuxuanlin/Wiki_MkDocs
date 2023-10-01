---
id: 将应用封装为Docker容器
title: 将应用封装为 Docker 容器
---

将应用封装为 Docker 容器，可以更加方便地部署管理。下面是一个示例，演示了如何将一个 Python 应用封装为 Docker 容器，并使用 Docker Compose 的方式执行。

## 基本模板

将应用 Docker 容器化，首先需要确保 Docker 已经安装。接着，需要在你的 Python 应用程序根目录下，创建这两个文件：`Dockerfile` 和 `compose.yaml`，它们大致会包含以下内容：

```Dockerfile title="Dockerfile"
# 设置基础镜像为 Python 官方镜像，版本可自定义
FROM python:3.9

# 设置工作目录为 /app
WORKDIR /app

# 复制 Python 应用程序的依赖文件
COPY requirements.txt .

# 安装应用程序依赖
RUN pip install --no-cache-dir -r requirements.txt

# 复制应用程序文件，从当前目录拷贝进容器内的目录
COPY . .

# 设置默认执行命令
CMD ["python", "app.py"]
```

```yaml title="compose.yaml"
version: "3"
services:
  app:
    build: .
```

在这个 `compose.yaml` 文件中，我们定义了一个服务名为 `app` 的服务。通过 `build: .` 指令，它将使用当前目录下的 `Dockerfile` 文件来构建镜像。在 `compose.yaml` 的目录下执行 `docker compose up`，即可构建并启动这个应用。

## 实例：将一个简单的 Python 应用封装为 Docker 容器

以下是一个简单的 Hello World 应用示例，

这是一个示例的 Python 应用，用于在网页上打印 Hello World：

```python title="app.py"
from flask import Flask
app = Flask(__name__)
@app.route("/")
def hello():
    return "Hello World!"
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=int("8000"), debug=True)
```

如果我们按照普通的流程部署 Python 应用，而不采用容器化的方法，则需要先安装依赖，对于某些需要编译安装包，在 Windows 环境下还可能出错，可能会缺失必要的头文件。如果我们将其封装为 Docker，就可以忽略环境的差；即使 Host 主机不联网，也只需拷贝镜像即可完成部署。以下的步骤展示将其 Docker 容器化，并用 Docker Compose 部署。

首先，创建一个名为 `Dockerfile` 的文件，在其中填写以下内容：

```Dockerfile title="Dockerfile"
# 设置基础镜像为Python官方镜像
FROM python:3.9

# 复制应用程序文件
COPY . /app

# 设置工作目录
WORKDIR /app

# 安装依赖
RUN pip install flask

# 暴露 8000 端口用于访问
EXPOSE 8000

# 启动应用程序
CMD python ./app.py
```

然后，在同一目录下创建一个名为`compose.yaml`的文件，将以下内容复制到其中：

```yaml title="compose.yaml"
version: "3"
services:
  helloworld-flask:
    build: .
    ports:
      - "8099:8000" # 端口 8099 可自定义
```

现在，你可以打开终端，进入包含 `Dockerfile` 和 `compose.yaml` 文件的目录，并运行以下命令来启动应用程序：

```shell
docker compose up
```

Docker 将会构建镜像并启动容器。访问 <http://localhost:8099> 即可看到 Hello World 的字符。通过以上步骤，可以将一个简单的 Python 应用容器化，并使用 Docker Compose 进行部署。

## 参考与致谢

- [Containerize an application](https://docs.docker.com/get-started/02_our_app/)
- [3 分钟将 Python 应用容器化](https://cloud.tencent.com/developer/article/1752513)
