# Docker Basics

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210116153041.png)

As we all know, one of the most troublesome things in software development is environment configuration. Differences in runtime environments can lead to unexpected results, but using Docker can avoid such problems.

## Docker and Containerization

Docker packages the software itself and its required runtime environment, so there is no need to configure the environment when using it (because the environment is all in the package). This ensures that your environment is exactly the same as the developer's, avoiding problems caused by differences in runtime environments.

Docker uses **containerization technology**. When we talk about containerization technology, we can compare it to **shipping containers**. It is a standardized large container that can be loaded and unloaded between various transportation tools (such as ships, trains, and trucks) without considering the specific content inside. Similarly, containerization technology packages the application and all its dependencies in an independent, portable environment called a container.

The main goal of containerization technology is to achieve fast deployment, scalability, and environment isolation of applications. By packaging the application and related dependencies in a container, we can ensure that the application runs in a consistent manner on different computers or servers without worrying about environment differences or dependency conflicts. This enables developers to deliver applications more quickly, while also simplifying the deployment and management process.

One of the major advantages of containerization technology is that it provides a lightweight virtualization solution. Compared to traditional virtual machines, containerization technology is lighter and consumes fewer resources. Each container runs on the same kernel of the host operating system, sharing the resources of the operating system. Therefore, containers start faster, occupy less memory, and can run multiple containers on the same machine at the same time.

Docker is currently a popular containerization solution. It mainly includes three elements: Image, Container, and Repository.

- **Image**: An image is an executable file that contains all the files and configurations necessary for an application and its dependencies (code, runtime, system tools, library files). We can think of an image as a template for containers, and multiple different container instances can be created from it.
- **Container**: A container is a running instance created from an image. Each container is an isolated and independent environment where applications can run.
- **Repository**: A repository is used to store and share images. We can push our own created images to a repository, or pull images created by others from the repository.

The relationship between containers and images is like that between objects and classes in object-oriented programming.

## Installation and Configuration of Docker

Before installing Docker, we can use the following command to uninstall old version packages to avoid conflicts:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

For mainstream Linux systems, we can use the official script method to download and install Docker Engine (requires root user privileges):

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Because Docker runs and depends on the Linux environment, it has almost no efficiency loss. However, if deploying Docker on other systems, a virtual Linux environment must be installed first.

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230708005714.png)

For the installation method of Docker on Windows, please refer to the official document [**Install Docker Desktop on Windows**](https://docs.docker.com/desktop/install/windows-install/).

For installation on MacOS, please refer to the official documentation [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/).

After following the installation process, we can use the following command to verify if Docker has been successfully installed:

```shell
docker version
```

After installing Docker Engine on Linux, if you want to use it as a non-root user, you can use the following command to configure permissions:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

After completing the configuration, you may need to log out and log back in to update the permissions.

If there are any installation issues, please refer to the official documentation [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/).

## Example: Hello World

Next, we will use the official hello-world example to demonstrate Docker. Open the terminal or command prompt and enter the following command to run the hello-world container:

```shell
docker run hello-world
```

This will download the hello-world image from the Docker image repository, create and run the container. When you see the output of "hello world", it means that the operation was successful.

## Some commonly used Docker CLI commands

Docker provides a powerful and rich set of commands for managing and operating container, image, network and other resources. Here are some commonly used Docker CLI commands:

- `docker run`: Create and run a new container based on a specified image. For example, `docker run -d -p 8080:80 nginx` will run an NGINX container in the background and map the host's port 8080 to the container's port 80.
- `docker ps`: List running containers. By default, it displays information such as the container ID, image, and command. Using the `docker ps -a` command will show all containers, including stopped ones.
- `docker stop`: Stop one or more running containers. You can specify the container ID or name. For example, `docker stop mycontainer` will stop the container named `mycontainer`.
- `docker start`: Start one or more stopped containers. You can use the container ID or name to specify the container.
- `docker restart`: Restart one or more containers.
- `docker rm`: Remove one or more containers. If you want to remove a running container, you can use the `docker rm -f` command.
- `docker images`: List local images. It displays a list of Docker images downloaded and created on the local computer, including image ID, size, and creation time.
- `docker rmi`: Remove one or more images. You can use the image ID or tag to specify the image. For example, `docker rmi myimage:1.0` will remove the image named `myimage` with the tag `1.0`.
- `docker build`: Build a custom image based on a Dockerfile. For example, `docker build -t myimage:1.0 .` will build an image named `myimage` with the tag `1.0` based on the Dockerfile in the current directory.
- `docker exec`: Execute a command in a running container. You can specify the container ID or name and the command to execute. For example, `docker exec -it mycontainer bash` will start a new interactive terminal in the container named `mycontainer`.

These are some commonly used Docker commands for managing and operating containers and images. There are many more commands to explore, which can be viewed by using the `docker --help` command to see the complete command list and other available options, or by referring to the official documentation [**Use the Docker command line**](https://docs.docker.com/engine/reference/commandline/cli/).

For more Docker-related knowledge, please refer to the following articles:

- [**Docker Compose - Image Orchestration Tool**](https://wiki-power.com/DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**Packaging Applications as Docker Containers**](https://wiki-power.com/%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

If you want to get started with practical exercises, you can also refer to the following series of articles:

- [Building Your Own Homelab](https://wiki-power.com/Building-Your-Own-Homelab)
- [Homelab - Lightweight Server Management Panel CasaOS](https://wiki-power.com/Homelab-Lightweight-Server-Management-Panel-CasaOS)
- [Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager](https://wiki-power.com/Homelab-Reverse-Proxy-Certificate-Management-Panel-Nginx-Proxy-Manager)
- [Homelab - Intranet Penetration Tool frp](https://wiki-power.com/Homelab-Intranet-Penetration-Tool-frp)
- [Homelab - Free Intranet Penetration Alternative Cloudflared](https://wiki-power.com/Homelab-Free-Intranet-Penetration-Alternative-Cloudflared)
- [Homelab - Online Code Editor code-server](https://wiki-power.com/Homelab-Online-Code-Editor-code-server)
- [Homelab - Website Status Monitoring Tool Uptime Kuma](https://wiki-power.com/Homelab-Website-Status-Monitoring-Tool-Uptime-Kuma)
- [Homelab - High-Quality Image Compression Tool TinyPNG-docker](https://wiki-power.com/Homelab-High-Quality-Image-Compression-Tool-TinyPNG-docker)
- [Homelab - Minimalist Personal Bookmark Navigation Site Flare](https://wiki-power.com/Homelab-Minimalist-Personal-Bookmark-Navigation-Site-Flare)
- [Homelab - Container Application Management Platform Portainer](https://wiki-power.com/Homelab-Container-Application-Management-Platform-Portainer)
- [Homelab - Cross-Device Synchronization Tool Syncthing](https://wiki-power.com/Homelab-Cross-Device-Synchronization-Tool-Syncthing)
- [Homelab - Fragmented Note Tool memos](https://wiki-power.com/Homelab-Fragmented-Note-Tool-memos)
- [Homelab - Powerful Wiki System Wiki.js](https://wiki-power.com/Homelab-Powerful-Wiki-System-Wikijs)
- [Homelab - Self-Hosted Password Manager Vaultwarden](https://wiki-power.com/Homelab-Self-Hosted-Password-Manager-Vaultwarden)
- [Homelab - Cloud-Based Image Bed System Cloudreve](https://wiki-power.com/Homelab-Cloud-Based-Image-Bed-System-Cloudreve)
- [Homelab - Self-Hosted RSS Aggregator FreshRSS](https://wiki-power.com/Homelab-Self-Hosted-RSS-Aggregator-FreshRSS)
- [Homelab - Bastion Host Supporting Multiple Protocols Next Terminal](https://wiki-power.com/Homelab-Bastion-Host-Supporting-Multiple-Protocols-NextTerminal)
- [Homelab - Multi-Functional PDF Toolbox Stirling-PDF](https://wiki-power.com/Homelab-Multi-Functional-PDF-Toolbox-Stirling-PDF)
- [Homelab - Website Favicon Capture Tool iconserver](https://wiki-power.com/Homelab-Website-Favicon-Capture-Tool-iconserver)
- [Homelab - Tool for Automatically Updating Docker Containers Watchtower](https://wiki-power.com/Homelab-Tool-for-Automatically-Updating-Docker-Containers-Watchtower)
- [Homelab - File List Program Supporting Multiple Storage Alist](https://wiki-power.com/Homelab-File-List-Program-Supporting-Multiple-Storage-Alist)
- [Homelab - Feature-Rich Kanban Software WeKan](https://wiki-power.com/Homelab-Feature-Rich-Kanban-Software-WeKan)
- [Homelab - Podcast and Audiobook Server Audiobookshelf](https://wiki-power.com/Homelab-Podcast-and-Audiobook-Server-Audiobookshelf)
- [Homelab - Cloud-Based Music Server Navidrome](https://wiki-power.com/Homelab-Cloud-Based-Music-Server-Navidrome)
- [Homelab - Film and Television Media Server Jellyfin](https://wiki-power.com/Homelab-Film-and-Television-Media-Server-Jellyfin)
- [Homelab - E-Book Management Server calibre-web](https://wiki-power.com/Homelab-E-Book-Management-Server-calibre-web)
- [Homelab - Smart Home Server Home Assistant](https://wiki-power.com/Homelab-Smart-Home-Server-Home-Assistant)
- [Homelab - Card-Assisted Memory Software Anki](https://wiki-power.com/Homelab-Card-Assisted-Memory-Software-Anki)

## References and Acknowledgements

- [Docker - From Beginner to Practice](https://yeasy.gitbook.io/docker_practice/)
- [Docker Tutorial](https://www.runoob.com/docker/docker-tutorial.html)
- [Docker Getting Started Tutorial](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [CentOS Installation of Docker](https://wiki-power.com/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.