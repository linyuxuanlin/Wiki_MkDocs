---
id: DockerCompose-镜像编排工具
title: Docker Compose - 镜像编排工具
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210117130925.jpg)

Docker Compose 是 Docker 镜像的编排工具。推荐使用 Docker Compose 作为 Docker 的默认打开方式，因为它不仅可以方便地配置与部署镜像，还可以更方便地配置多镜像服务，甚至区分它们的启动顺序，这是使用命令的打开方式所不具备的。

虽然 Docker 的思想是解耦（一个镜像一个进程）、提高复用率、不在一个镜像内封装多个服务，但是，有些应用是需要多个服务同时启动的。例如，一个典型的 web 应用，至少需要服务端和数据库配合。这样一来，你需要分别部署两个容器，甚至有些服务需要按一定先后顺序启动。这样一来，需要的镜像和操作步骤会很复杂。

Docker Compose 把所需要调用的镜像（所有需要的服务、容器的属性、网络配置以及存储卷的挂载）和顺序等，全部写在一个 YAML 文件里，直接运行这个配置文件，就可以按照你所需的方法和步骤运行容器，而不需要手动操作每个容器。以下是一个 Docker Compose 示例，用于部署一个 web 服务：

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

在这个 YAML 文件中，定义并启动了`web` 和 `database` 这两个实例。

## Docker Compose 的安装与配置

Docker Compose 依赖 Docker Engine，所以请先确保你已经安装了 Docker Engine 环境。如果你还没安装，可以参考上一篇教程：[**Docker 基础知识**](https://wiki-power.com/Docker%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/)，安装 Docker Engine.

如果你用的是 Windows/MacOS/Linux 桌面客户端，那就不用另外安装 Docker Compose 了，因为已经包含在内。下面介绍 Linux Docker Engine 环境下 Docker Compose 的安装方法。

对于 Ubuntu 和 Debian，使用以下的命令安装 Docker Compose：

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

对于 RPM 发行版的 Linux（比如 CentOS），使用以下的命令安装 Docker Compose：

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

完成后，使用以下的命令检验安装是否成功：

```shell
docker compose version
```

## 如何使用 Docker Compose

一般我们创建一个 `compose.yaml` 文件（老版本为 `docker-compose.yml`，也是兼容的），并将其放到一个以应用名称命名目录下，比如 `web/compose.yaml`。

要运行这个程序，只要在这个目录下执行 `docker compose up` 命令，即可按 YAML 文件中的配置启动服务。（加参数 `-d` 可以后台运行）

要停止应用栈的运行，用 `docker compose down` 就可以了。

## Docker Compose 文件的写法

Docker Compose 的默认打开方式，是创建一个 YAML 格式的文件，默认命名为 `compose.yaml`。以下是一个示例的模板，包含所有可用的参数（但并不一定要全部用上）：

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

在一个 `compose.yaml` 中，通常会包含以下的参数：

- **version**：仅用来展示 compose 文件的版本信息。与 Docker Engine 版本相关联，更新的版本可能会有新增功能特性或语法。请参考官方文档 [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/)。
- **services**：定义了此 compose 文件中包含的各个服务（容器）。每个服务都是一个独立的容器，可以定义其镜像、端口映射、环境变量等。
- **container_name**：容器名称，非必须，但不能出现重名。
- **networks**：定义了服务之间的网络配置。可以创建自定义网络，并将服务连接到这些网络上，实现容器之间的通信。
- **volumes**：定义了容器的卷的挂载配置。可以将容器的目录或文件与主机的目录或文件进行关联，实现数据持久化和共享。相当于 Docker CLI 中的 `-v` 参数。
- **environment**（或 `env_file`）：指定容器的环境变量的文件名与路径，指定以这文件来加载环境变量。如果没有配置环境变量可忽略。如果环境变量在当前目录下且名为 `.env`，也可以省略。相当于 Docker CLI 中的 `-e` 参数。
- **build**：使用构建的镜像启动。指定 Dockerfile 文件的路径。
- **image**：指定容器所使用的镜像。可以使用公共镜像仓库中的镜像，或者指定本地的 Dockerfile 文件。
- **ports**：定义容器与宿主机之间的端口映射关系，也可指定映射协议（TCP 或 UDP）。相当于 Docker CLI 中的 `-p` 参数。
- **depends_on**：定义服务之间的依赖关系。可以指定一个或多个服务的名称，表示当前服务依赖于这些服务的启动。
- **restart**：定义容器的重启策略。可以设置为 `no`（不自动重启）、`always`（始终自动重启）、`unless-stopped`（自动重启，除非手动停止容器）或 `on-failure`（仅奔溃时自动重启）。相当于 Docker CLI 中的 `--restart` 参数。
- **command**：指定容器启动时要执行的命令，可用于覆盖容器镜像中默认的启动命令。
- **volumes_from**：指定容器要挂载卷的来源容器。

## 一些常用的 Docker Compose 命令

以下是一些常见的 Docker Compose 命令，用于管理和操作 `compose.yaml`` 文件定义的服务：

- `docker compose up`：构建 compose 中定义的镜像并启动容器。如果需要，它会自动构建镜像（如果 Dockerfile 已更改），然后启动所有定义的服务。如果需要在后台启动，请加上 `-d` 参数。
- `docker compose down`：停止并移除 compose 中的所有容器、网络和卷。它会停止正在运行的服务并清理所有相关的资源。
- `docker compose pull`：拉取 compose 中定义的所有镜像，或用于更新镜像、
- `docker compose start`：启动已经创建的 compose 中的容器，不会重新创建容器或重新构建镜像。
- `docker compose stop`：停止已经创建的 compose 中的容器，但不会移除容器。
- `docker compose restart`：重启已经创建的 compose 中的容器。
- `docker compose pause`：暂停已经创建的 compose 中的容器，使其暂时停止运行。
- `docker compose unpause`：恢复已经暂停的 compose 中的容器，使其继续运行。
- `docker compose ps`：显示 **所有** 正在运行的 compose 中的容器的状态。
- `docker compose logs`：查看 compose 中的容器的日志输出。
- `docker compose exec`：在运行的 compose 中的容器中执行命令。比如 `docker exec -it [compose-name] /bin/bash`

这是一些常见的命令，你也可以执行 `docker compose --help` 查看更多可用的命令。

## 环境变量

在 Docker Compose 中，虽然环境变量并非必选项，但是推荐多使用，因为以下几个优点：

1. **灵活性和可配置性**：轻松调整应用的配置信息，而无需修改 Docker 镜像或重新构建容器。
2. **安全性和隔离性**：通过将敏感信息存储在环境变量中，而不是直接写在代码或配置文件中，对环境变量单独授权，可以提高应用程序的安全性。
3. **跨平台兼容性**：不同的操作系统或平台都可以通过环境变量传递不同的配置信息，无需对配置文件或镜像代码进行修改。
4. **部署和管理的简化**：通过统一使用环境变量来配置不同容器的参数，可以减少配置文件中的重复内容，使整个过程更加清晰和易于维护。
5. **集成和自动化**：通过与 CI/CD 和自动化工具结合，可自动将应用的配置参数传递给 Docker 容器，实现自动化部署和集成。

环境变量是一个 `.env` 后缀的文件，一般是直接在 `compose.yaml` 同级目录下创建一个名为 `.env` 的文件，以下是一个示例：

```dotenv title=".env"
TAG=v1.5
```

在 `compose.yaml` 中可以直接调用环境变量：

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## 小技巧

有一个将 Docker CLI 转换为 Docker Compose YAML 的网站：[**composerize**](https://www.composerize.com/)，转换结果不一定准确，需检验。

## 参考与致谢

- [使用 docker compose 替代 docker run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Install Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Docker-Compose 模板文件参数详解](https://blog.51cto.com/14154700/2466054)
- [原来，群晖也能用 Docker Compose！](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - 从入门到实践](https://docker-practice.github.io/zh-cn/)
- [Docker 系列 - 了解 Docker Compose 的配置文件](https://blognas.hwb0307.com/linux/docker/3880)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
