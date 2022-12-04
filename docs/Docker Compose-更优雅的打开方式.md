---
id: DockerCompose-更优雅的打开方式
title: Docker Compose - 更优雅的打开方式
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210117130925.jpg)

Docker Compose 是一种对 Docker 镜像的编排方式，解决了传统命令行 Docker 运行多镜像的麻烦。

Docker 的思想是解耦，即一个镜像一个进程，提高复用率，而不是把多个服务封装成一个镜像。但像一个典型的 web 应用，至少需要服务端和数据库配合，这样至少需要两条以上的 Docker 命令；甚至有些服务需要按一定先后顺序启动，这样一来，需要的镜像和操作步骤会很复杂。

Docker Compose 把所需要调用的镜像（包括各种参数）和顺序等，全部写在一个 `yaml` 文件里，直接运行这个配置文件，就可以 **按照你所需的方法和步骤运行容器** 。所以称 Docker Compose 为一种 **镜像编排的方式** 。一个 web 应用的例子：

```yaml
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

在这个 `yaml` 文件中，定义了两个服务：web 和 database，一个服务在运行时对应一个容器的实例， 上面的文件表示要启动两个实例。

## 安装 Docker Compose

### 前提

Docker Compose 依赖 Docker Engine，所以请先确保你已经安装了 Docker Engine 环境。如果你还没安装，可以参考上一篇教程：[**Docker 简易指南**](https://wiki-power.com/Docker%E7%AE%80%E6%98%93%E6%8C%87%E5%8D%97) 安装 Docker Engine.

如果你用的是 Windows 和 MacOS 的桌面客户端，那就不用另外安装 Docker Compose 了，因为已经包含在 Docker Desktop 内了。

本教程详细讲解 Linux 下的 Docker Compose 安装。

### 下载 Docker Compose

```shell
sudo curl -L "https://github.com/docker/compose/releases/download/1.27.4/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

### 授权

```shell
sudo chmod +x /usr/local/bin/docker-compose
```

### 测试是否安装成功

```shell
docker-compose --version
```

### 其他操作

#### 版本更新

```shell
docker-compose migrate-to-labels
```

#### 卸载

```shell
sudo rm /usr/local/bin/docker-compose
```

## 如何使用 Docker Compose

通常我们将 `docker-compose.yml` 文件放到一个目录，表示一个应用。

要运行这个程序，只要在这个目录下执行 `docker-compose up` 命令，即可按 `yaml` 文件中的配置启动服务。（加参数 `-d` 可以后台运行）

要停止服务的运行，用 `docker-compose down` 就可以了。

## Docker Compose 的模板

Docker Compose 默认的模板文件名称为 `docker-compose.yml`，为 `yaml` 格式，内容如下：

```yaml
version: "3"
services:
  webapp:
    image: examples/web
    ports:
      - "80:80"
    volumes:
      - "/data"
```

一般来说，`yaml` 文件在 Docker 项目简介中会提供。

## 参考与致谢

- [使用 docker-compose 替代 docker run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Install Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Docker-Compose 模板文件参数详解](https://blog.51cto.com/14154700/2466054)



> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

