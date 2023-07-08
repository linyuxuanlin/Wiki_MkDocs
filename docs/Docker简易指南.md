---
id: Docker简易指南
title: Docker 简易指南
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210116153041.png)

众所周知，软件开发中最麻烦的事情之一，就是环境的配置。运行环境的差异，可能导致意想不到的结果，而使用 Docker 可以避免出现这样的问题。

## Docker 与容器化技术

Docker 把软件本身和它所需的运行环境打包起来，使用的时候就不需要再去配置环境了（因为环境都在包里），这样就能确保你的环境和开发者的一模一样，避免因运行环境差异而造成问题。

Docker 使用的是 **容器化技术**。当我们谈论容器化技术时，可以将其类比 **集装箱**。它是一种 **标准化** 的大型容器，可以在各种运输工具（如船舶、火车、卡车）之间进行简单的装载和卸载，而无需考虑其内部的具体内容组成。类似地，容器化技术将应用程序及其所有依赖项打包在一个独立的、可移植的环境中，称为容器。

容器化技术的主要目标是实现应用程序的快速部署、可扩展性和环境隔离。通过将应用程序和相关依赖项打包在一个容器中，我们可以确保在不同的计算机或服务器上以一致的方式运行应用程序，而无需担心环境差异或依赖冲突的问题。这使得开发人员可以更快速地交付应用程序，同时也简化了应用程序的部署和管理过程。

容器化技术的一大优势是它提供了轻量级的虚拟化解决方案。与传统的虚拟机相比，容器化技术更加轻巧且资源消耗更少。每个容器都运行在宿主操作系统的相同内核上，共享操作系统的资源，因此容器启动更快、占用更少的内存，也可以在同一台机器上同时运行多个容器。

Docker 是目前比较流行的容器化解决方案。它主要包含三要素，分别是 Image（镜像）、Container（容器）和 Repository（仓库）。

- **Image（镜像）**：镜像是一个可执行文件，包含了应用程序及其依赖的所有文件系统（代码、runtime、系统工具、库文件）和配置。我们可以将镜像看作是容器的模板，通过它可以创建多个不同的容器实例。
- **Container（容器）**：容器是由镜像创建的运行实例。每个容器都是相互隔离的、独立运行的环境，可以在其中运行应用程序。
- **Repository（仓库）**：仓库是用来存储和分享镜像。我们可以将自己创建的镜像推送到仓库中，也可以从仓库中拉取他人创建的镜像。

容器与镜像的关系，就像面向对象编程中的对象与类。

## Docker 的安装配置

对于主流的 Linux 系统，可以使用官方脚本的方法下载安装 Docker：

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh
```

因为 Docker 运行在并依赖于 Linux 环境，所以它几乎没有效率损耗。但是，如果在其他系统上部署 Docker，就必须先安装一个虚拟 Linux 环境。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230708005714.png)

Windows 下 Docker 的安装方法，请参考官方文档 [**Install Docker Desktop on Windows**](https://docs.docker.com/desktop/install/windows-install/)。

MacOS 下的安装方法，请参考官方文档 [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/)。

按照流程安装后，我们可以使用以下的命令，验证 Docker 是否安装成功：

```shell
docker version
```

## 如何将应用封装为 Docker 容器

将应用封装为 Docker 容器，可以更加方便地部署管理。下面是一个示例，演示了如何将一个 Python 应用封装为 Docker 容器，并使用 Docker Compose 的方式执行。

### 基本模板

将应用 Docker 容器化，首先需要确保 Docker 已经安装。接着，需要在你的 Python 应用程序根目录下，创建这两个文件：`Dockerfile` 和 `docker-compose.yml`，它们的模板分别如下：

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

```yaml title="docker-compose.yml"
version: "3"
services:
  app:
    build: .
```

在这个 `docker-compose.yml` 文件中，我们定义了一个服务名为 `app` 的服务。通过 `build: .` 指令，它将使用当前目录下的 `Dockerfile` 文件来构建镜像。最后，在 `docker-compose.yml` 的目录下执行 `docker compose up`，即可构建并启动容器。

### 详细示例

---

## ?

### 配置权限

Docker 需要 `sudo` 权限。为了避免每次使用都要获取权限，可以把用户加入 Docker 用户组：

```shell
sudo usermod -aG docker $USER
```

### 启动 Docker

按如下命令启动 Docker：

```shell
sudo systemctl start docker
```

（也可以使用 `sudo service docker start`）

配置开机自启动（可选）：

```shell
sudo systemctl enable docker
```

### 换源

因为 Docker 的官方源地址在国外，所以有时候下载缓慢，我们通过更换国内镜像源来解决：

```shell
sudo vi /etc/default/docker
```

按 `a` 进入编辑模式，在尾部添加一行：

```
DOCKER_OPTS="--registry-mirror=https://registry.docker-cn.com"
```

按 `ESC` 推出编辑后按 `:wq` 保存退出。  
重启 Docker 服务：

```shell
sudo service docker restart
```

## Docker 基本操作

### Image 操作

#### 列出本地所有 Image

```shell
docker Image ls
```

#### 删除 Image

```shell
docker Image rm [ImageName]
```

虽然 Image 可以自己造，但我们推荐直接用别人的，既省时省力，又有利于维护环境统一。  
你可以在 [**Docker Hub**](https://hub.docker.com/) 搜索并下载 Image 文件，拣下载量较多的用。

### Container 操作

#### 列出正在运行的容器

```shell
docker Container ls
```

可以加上 `--all` 参数，列出所有（包括已经停止的）容器。

列出容器时，能看到容器对应的 ID，这个 ID 在很多地方会用到。

#### 新建并运行容器

```shell
docker Container run [ImageName]
```

#### 运行已经存在的容器

```shell
docker Container start [ContainerID]
```

#### 停止容器的运行

```shell
docker Container stop [ContainerID]
```

#### 删除容器

```shell
docker Container rm [ContainerID]
```

#### 查看容器的输出

```shell
docker Container logs [ContainerID]
```

#### 操作容器

```shell
docker Container exec -it [ContainerID] /bin/bash
```

## 实例：Hello World

下面将用官方 hello-world 例子来演示 Docker。

首先，将 Image 拉拉取到本地：

```shell
docker Image pull library/hello-world
```

拉取后，使用 ls 命令检查是否已经下载：

```shell
docker Image ls
```

生成容器并运行：

```shell
docker Container run hello-world
```

因为这个 hello-world 只运行一次，所以不用手动去停止。  
对于持续运行的容器，如果需要停止，就用以下命令：

```shell
docker Container kill [containID]
```

## 参考与致谢

- [Docker - 从入门到实践](https://yeasy.gitbook.io/docker_practice/)
- [Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [CentOS 安装 Docker](https://wiki-power.com/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
