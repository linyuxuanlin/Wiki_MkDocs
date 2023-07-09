---
id: 将应用封装为Docker容器
title: 将应用封装为 Docker 容器
---

将应用封装为 Docker 容器，可以更加方便地部署管理。下面是一个示例，演示了如何将一个 Python 应用封装为 Docker 容器，并使用 Docker Compose 的方式执行。

## 基本模板

将应用 Docker 容器化，首先需要确保 Docker 已经安装。接着，需要在你的 Python 应用程序根目录下，创建这两个文件：`Dockerfile` 和 `compose.yaml`，它们大致包含以下内容：

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

在这个 `compose.yaml` 文件中，我们定义了一个服务名为 `app` 的服务。通过 `build: .` 指令，它将使用当前目录下的 `Dockerfile` 文件来构建镜像。最后，在 `compose.yaml` 的目录下执行 `docker compose up`，即可构建并启动容器。

## 实例：
