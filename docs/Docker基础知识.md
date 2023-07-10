---
id: Docker基础知识
title: Docker 基础知识
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

## Docker 的安装与配置

在安装 Docker 之前，可以先用以下的命令卸载旧版本包，避免冲突：

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

对于主流的 Linux 系统，可以使用官方脚本的方法下载安装 Docker Engine：（需要使用 root 用户权限）

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

因为 Docker 运行在并依赖于 Linux 环境，所以它几乎没有效率损耗。但是，如果在其他系统上部署 Docker，就必须先安装一个虚拟 Linux 环境。

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230708005714.png)

Windows 下 Docker 的安装方法，请参考官方文档 [**Install Docker Desktop on Windows**](https://docs.docker.com/desktop/install/windows-install/)。

MacOS 下的安装方法，请参考官方文档 [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/)。

按照流程安装后，我们可以使用以下的命令，验证 Docker 是否安装成功：

```shell
docker version
```

在 Linux 下安装 Docker Engine 后，如果想要以非 root 用户使用，可以使用以下的命令配置权限：

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

完成配置后，可能需要注销重新登录，以更新权限。

如果安装出现问题，请参考官方文档 [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/)。

## 实例：Hello World

下面将用官方 hello-world 例子来演示 Docker。打开终端或命令提示符，并输入以下命令运行 hello-world 容器：

```shell
docker run hello-world
```

这将从 Docker 镜像仓库中下载 hello-world 镜像，创建并运行容器。当看见 hello world 的输出时，说明运行成功。

## 一些常用的 Docker CLI 命令

Docker 提供了一组强大而丰富的命令，用于管理和操作容器、镜像、网络等资源。下面是一些常用的 Docker CLI 命令：

- `docker run`：基于指定的镜像创建并运行一个新容器。例如，`docker run -d -p 8080:80 nginx` 会在后台运行一个 NGINX 容器，将主机的 8080 端口映射到容器的 80 端口。
- `docker ps`：列出正在运行的容器。默认情况下，它会显示正在运行的容器的 ID、镜像、命令等信息。使用`docker ps -a`命令可以显示所有的容器，包括已停止的容器。
- `docker stop`：停止一个或多个运行中的容器。可以指定容器的 ID 或名称。例如，`docker stop mycontainer` 会停止名为 `mycontainer` 的容器。
- `docker start`：启动一个或多个已停止的容器。可使用容器的 ID 或名称来指定容器。
- `docker stop`：停止一个或多个运行中的容器。
- `docker restart`：重启一个或多个容器。
- `docker rm`：删除一个或多个容器。如果要删除运行中的容器，可以使用 `docker rm -f` 命令。
- `docker images`：列出本地镜像。它会显示本地计算机上已经下载和创建的 Docker 镜像的列表，包括镜像 ID、大小和创建时间等信息。
- `docker rmi`：删除一个或多个镜像。可以使用镜像的 ID 或标签来指定镜像。例如，`docker rmi myimage:1.0` 会删除名为 `myimage` 且标签为 `1.0` 的镜像。
- `docker build`：基于 Dockerfile 构建一个自定义镜像。例如，`docker build -t myimage:1.0 .`会根据当前目录下的 Dockerfile 构建一个名为 `myimage` 且标签为 `1.0` 的镜像。
- `docker exec`：在运行中的容器中执行命令。可以指定容器的 ID 或名称，以及要执行的命令。例如，`docker exec -it mycontainer bash`会在名为 `mycontainer` 的容器中启动一个新的交互式终端。

这些是一些常用的 Docker 命令，用于管理和操作容器和镜像。还有更多的命令可以探索，可以通过`docker --help`命令查看完整的命令列表和其它可用选项，也可以参考官方文档 [**Use the Docker command line**](https://docs.docker.com/engine/reference/commandline/cli/)。

如需了解更多 Docker 相关的知识，请移步后续的文章：

- [**Docker Compose - 镜像编排工具**](https://wiki-power.com/DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**将应用封装为 Docker 容器**](https://wiki-power.com/%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

如果你想直接上手实践，也可参考以下系列的文章：

- [搭建属于自己的 HomeLab](https://wiki-power.com/搭建属于自己的HomeLab)
- [Homelab - 轻量服务器管理面板 CasaOS](https://wiki-power.com/Homelab-轻量服务器管理面板CasaOS)
- [Homelab - 反代证书管理面板 Nginx Proxy Manager](https://wiki-power.com/Homelab-反代证书管理面板NginxProxyManager)
- [Homelab - 内网穿透工具 frp](https://wiki-power.com/Homelab-内网穿透工具frp)
- [Homelab - 免费的内网穿透替代方案 Cloudflared](https://wiki-power.com/Homelab-免费的内网穿透替代方案Cloudflared)
- [Homelab - 在线代码编辑器 code-server](https://wiki-power.com/Homelab-在线代码编辑器code-server)
- [Homelab - 网站状态监控工具 Uptime Kuma](https://wiki-power.com/Homelab-网站状态监控工具UptimeKuma)
- [Homelab - 高质量图片压缩工具 TinyPNG-docker](https://wiki-power.com/Homelab-高质量图片压缩工具TinyPNG-docker)
- [Homelab - 极简个人书签导航站 Flare](https://wiki-power.com/Homelab-极简个人书签导航站Flare)
- [Homelab - 容器应用管理平台 Portainer](https://wiki-power.com/Homelab-容器应用管理平台Portainer)
- [Homelab - 跨设备同步工具 Syncthing](https://wiki-power.com/Homelab-跨设备同步工具Syncthing)
- [Homelab - 碎片笔记工具 memos](https://wiki-power.com/Homelab-碎片笔记工具memos)
- [Homelab - 功能强大的 wiki 系统 Wiki.js](https://wiki-power.com/Homelab-功能强大的wiki系统Wikijs)
- [Homelab - 自托管密码管理器 Vaultwarden](https://wiki-power.com/Homelab-自托管密码管理器Vaultwarden)
- [Homelab - 支持公有云的图床系统 Cloudreve](https://wiki-power.com/Homelab-支持公有云的图床系统Cloudreve)
- [Homelab - 自托管 RSS 聚合器 FreshRSS](https://wiki-power.com/Homelab-自托管RSS聚合器FreshRSS)
- [Homelab - 支持多种协议的堡垒机 Next Terminal](https://wiki-power.com/Homelab-支持多种协议的堡垒机NextTerminal)
- [Homelab - 播客订阅管理器 Podgrab](https://wiki-power.com/Homelab-播客订阅管理器Podgrab)
- [Homelab - 多功能 PDF 工具箱 Stirling-PDF](https://wiki-power.com/Homelab-多功能PDF工具箱Stirling-PDF)
- [Homelab - 网站 favicon 抓取工具 iconserver](https://wiki-power.com/Homelab-网站favicon抓取工具iconserver)
- [Homelab - 极简的待办系统 todo](https://wiki-power.com/Homelab-极简的待办系统todo)
- [Homelab - 自动更新 Docker 容器的工具 Watchtower](https://wiki-power.com/Homelab-自动更新Docker容器的工具Watchtower)
- [Homelab - 支持多存储的文件列表程序 Alist](https://wiki-power.com/Homelab-支持多存储的文件列表程序Alist)
- [Homelab - 功能丰富的看板软件 WeKan](https://wiki-power.com/Homelab-功能丰富的看板软件WeKan)
- [Homelab - 播客与有声书服务器 Audiobookshelf](https://wiki-power.com/Homelab-播客与有声书服务器Audiobookshelf)
- [Homelab - 云端音乐服务器 Navidrome](https://wiki-power.com/Homelab-云端音乐服务器Navidrome)
- [Homelab - 影视媒体服务器 Jellyfin](https://wiki-power.com/Homelab-影视媒体服务器Jellyfin)
- [Homelab - 电子书管理服务器 calibre-web](https://wiki-power.com/Homelab-电子书管理服务器calibre-web)
- [Homelab - 智能家居服务器 Home Assistant](https://wiki-power.com/Homelab-智能家居服务器HomeAssistant)
- [Homelab - 卡片辅助记忆软件 Anki](https://wiki-power.com/Homelab-卡片辅助记忆软件Anki)

## 参考与致谢

- [Docker - 从入门到实践](https://yeasy.gitbook.io/docker_practice/)
- [Docker 教程](https://www.runoob.com/docker/docker-tutorial.html)
- [Docker 入门教程](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [CentOS 安装 Docker](https://wiki-power.com/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
