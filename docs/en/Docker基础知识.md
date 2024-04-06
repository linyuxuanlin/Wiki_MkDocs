# Docker Fundamentals

![Image](https://media.wiki-power.com/img/20210116153041.png)

As we all know, one of the most troublesome aspects of software development is environment configuration. Differences in runtime environments can lead to unexpected results, and Docker can help prevent such issues.

## Docker and Containerization

Docker packages the software itself along with the required runtime environment, eliminating the need for manual environment configuration. This ensures that your environment matches that of the developer, thereby avoiding problems caused by runtime environment discrepancies.

Docker utilizes containerization technology. When we talk about containerization, we can liken it to **shipping containers**. It's a standardized, large container that can be easily loaded and unloaded between various modes of transport, such as ships, trains, and trucks, without needing to consider the specific contents inside. Similarly, containerization technology packages an application and all its dependencies in a self-contained, portable environment known as a container.

The primary goals of containerization technology are rapid application deployment, scalability, and environment isolation. By packaging an application and its dependencies into a container, we can ensure that the application runs consistently across different computers or servers, without worrying about environment differences or dependency conflicts. This enables developers to deliver applications more quickly while simplifying the deployment and management process.

One significant advantage of containerization technology is that it provides a lightweight virtualization solution. Compared to traditional virtual machines, containerization technology is more lightweight and resource-efficient. Each container runs on the same kernel as the host operating system, sharing the OS's resources. As a result, containers start faster, consume less memory, and can run multiple containers on the same machine simultaneously.

Docker is currently one of the most popular containerization solutions, comprising three key elements: Image, Container, and Repository.

- **Image**: An image is an executable file containing all the file systems (code, runtime, system tools, library files) and configurations required for an application. Think of an image as a template for creating multiple different container instances.

- **Container**: A container is a running instance created from an image. Each container runs in an isolated and independent environment where applications can be executed.

- **Repository**: A repository is used to store and share images. You can push your own created images to a repository and pull images created by others from the repository.

The relationship between containers and images is akin to objects and classes in object-oriented programming.

## Installing and Configuring Docker

Before installing Docker, you can use the following command to uninstall old package versions to prevent conflicts:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

For mainstream Linux systems, you can download and install Docker Engine using the official script method (requires root user privileges):

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Since Docker runs on and depends on the Linux environment, it incurs minimal efficiency overhead. However, if deploying Docker on other systems, a virtual Linux environment must be installed first.

![Image](https://media.wiki-power.com/img/20230708005714.png)

For instructions on installing Docker on Windows, please refer to the official documentation [**Install Docker Desktop on Windows**](https://docs.docker.com/desktop/install/windows-install/).

For macOS installation, consult the official documentation [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/).

After following the installation process, you can use the following command to verify if Docker has been successfully installed:

```shell
docker version
```

In Linux, after installing Docker Engine, if you want to use it as a non-root user, you can configure permissions with the following commands:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

After configuring, you may need to log out and log back in to update the permissions.

If you encounter any installation issues, please refer to the official documentation [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/).

## Example: Hello World

Next, we'll use the official hello-world example to demonstrate Docker. Open your terminal or command prompt and enter the following command to run the hello-world container:

```shell
docker run hello-world
```

This will download the hello-world image from the Docker image repository, create, and run the container. When you see the "hello world" output, it means the operation was successful.

## Some Common Docker CLI Commands

Docker provides a powerful set of commands for managing and operating containers, images, networks, and other resources. Here are some commonly used Docker CLI commands:

- `docker run`: Create and run a new container based on a specified image. For example, `docker run -d -p 8080:80 nginx` will run an NGINX container in the background, mapping port 8080 on the host to port 80 in the container.
- `docker ps`: List running containers. By default, it displays information such as container ID, image, and command for running containers. You can use `docker ps -a` to show all containers, including stopped ones.
- `docker stop`: Stop one or more running containers, specifying the container ID or name. For example, `docker stop mycontainer` will stop a container named `mycontainer`.
- `docker start`: Start one or more stopped containers using their ID or name.
- `docker restart`: Restart one or more containers.
- `docker rm`: Remove one or more containers. To delete a running container, you can use the `docker rm -f` command.
- `docker images`: List local images, displaying information like image ID, size, and creation time.
- `docker rmi`: Remove one or more images by specifying the image ID or tag. For instance, `docker rmi myimage:1.0` will delete an image named `myimage` with tag `1.0`.
- `docker build`: Build a custom image based on a Dockerfile. For example, `docker build -t myimage:1.0 .` will create an image named `myimage` with tag `1.0` based on the Dockerfile in the current directory.
- `docker exec`: Execute a command in a running container, specifying the container ID or name and the command to run. For example, `docker exec -it mycontainer bash` will start a new interactive terminal in a container named `mycontainer`.

These are some common Docker commands for managing and working with containers and images. There are many more commands to explore, and you can view the complete list and options by using `docker --help` or refer to the official documentation [**Use the Docker command line**](https://docs.docker.com/engine/reference/commandline/cli/) for more information.

For further Docker-related knowledge, please proceed to the following articles.

- [**Docker Compose - Image Orchestration Tool**](https://wiki-power.com/DockerCompose-%E9%95%9C%E5%83%8F%E7%BC%96%E6%8E%92%E5%B7%A5%E5%85%B7/)
- [**Encapsulating Applications into Docker Containers**](https://wiki-power.com/%E5%B0%86%E5%BA%94%E7%94%A8%E5%B0%81%E8%A3%85%E4%B8%BADocker%E5%AE%B9%E5%99%A8/)

If you're eager to dive right into practical application, you can also refer to the following series of articles:

- [Setting Up Your Own HomeLab](https://wiki-power.com/Setting-Up-Your-Own-HomeLab)
- [Homelab - Lightweight Server Management Panel CasaOS](https://wiki-power.com/Homelab-Lightweight-Server-Management-Panel-CasaOS)
- [Homelab - Reverse Proxy and Certificate Management Panel Nginx Proxy Manager](https://wiki-power.com/Homelab-Reverse-Proxy-and-Certificate-Management-Panel-Nginx-Proxy-Manager)
- [Homelab - Intranet Penetration Tool frp](https://wiki-power.com/Homelab-Intranet-Penetration-Tool-frp)
- [Homelab - Free Intranet Penetration Alternative Cloudflared](https://wiki-power.com/Homelab-Free-Intranet-Penetration-Alternative-Cloudflared)
- [Homelab - Online Code Editor code-server](https://wiki-power.com/Homelab-Online-Code-Editor-code-server)
- [Homelab - Website Status Monitoring Tool Uptime Kuma](https://wiki-power.com/Homelab-Website-Status-Monitoring-Tool-Uptime-Kuma)
- [Homelab - High-Quality Image Compression Tool TinyPNG-docker](https://wiki-power.com/Homelab-High-Quality-Image-Compression-Tool-TinyPNG-docker)
- [Homelab - Minimalist Personal Bookmark Navigation Site Flare](https://wiki-power.com/Homelab-Minimalist-Personal-Bookmark-Navigation-Site-Flare)
- [Homelab - Container Application Management Platform Portainer](https://wiki-power.com/Homelab-Container-Application-Management-Platform-Portainer)
- [Homelab - Cross-Device Synchronization Tool Syncthing](https://wiki-power.com/Homelab-Cross-Device-Synchronization-Tool-Syncthing)
- [Homelab - Fragmented Note-Taking Tool memos](https://wiki-power.com/Homelab-Fragmented-Note-Taking-Tool-memos)
- [Homelab - Powerful Wiki System Wiki.js](https://wiki-power.com/Homelab-Powerful-Wiki-System-Wiki.js)
- [Homelab - Self-Hosted Password Manager Vaultwarden](https://wiki-power.com/Homelab-Self-Hosted-Password-Manager-Vaultwarden)
- [Homelab - Cloud-Supported Image Hosting System Cloudreve](https://wiki-power.com/Homelab-Cloud-Supported-Image-Hosting-System-Cloudreve)
- [Homelab - Self-Hosted RSS Aggregator FreshRSS](https://wiki-power.com/Homelab-Self-Hosted-RSS-Aggregator-FreshRSS)
- [Homelab - Multi-Protocol Bastion Host Next Terminal](https://wiki-power.com/Homelab-Multi-Protocol-Bastion-Host-Next-Terminal)
- [Homelab - Multifunctional PDF Toolbox Stirling-PDF](https://wiki-power.com/Homelab-Multifunctional-PDF-Toolbox-Stirling-PDF)
- [Homelab - Website Favicon Retrieval Tool iconserver](https://wiki-power.com/Homelab-Website-Favicon-Retrieval-Tool-iconserver)
- [Homelab - Docker Container Auto-Update Tool Watchtower](https://wiki-power.com/Homelab-Docker-Container-Auto-Update-Tool-Watchtower)
- [Homelab - Multi-Storage File Listing Program Alist](https://wiki-power.com/Homelab-Multi-Storage-File-Listing-Program-Alist)
- [Homelab - Feature-Rich Kanban Software WeKan](https://wiki-power.com/Homelab-Feature-Rich-Kanban-Software-WeKan)
- [Homelab - Podcast and Audiobook Server Audiobookshelf](https://wiki-power.com/Homelab-Podcast-and-Audiobook-Server-Audiobookshelf)
- [Homelab - Cloud Music Server Navidrome](https://wiki-power.com/Homelab-Cloud-Music-Server-Navidrome)
- [Homelab - Video and Media Server Jellyfin](https://wiki-power.com/Homelab-Video-and-Media-Server-Jellyfin)
- [Homelab - Ebook Management Server calibre-web](https://wiki-power.com/Homelab-Ebook-Management-Server-calibre-web)
- [Homelab - Smart Home Server Home Assistant](https://wiki-power.com/Homelab-Smart-Home-Server-Home-Assistant)
- [Homelab - Flashcard-Assisted Memory Software Anki](https://wiki-power.com/Homelab-Flashcard-Assisted-Memory-Software-Anki)

## References and Acknowledgments

- [Docker - Getting Started to Practical Use](https://yeasy.gitbook.io/docker_practice/)
- [Docker Tutorial](https://www.runoob.com/docker/docker-tutorial.html)
- [Introduction to Docker](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [Installing Docker on CentOS](https://wiki-power.com/unlist/CentOS%E5%AE%89%E8%A3%85Docker)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
