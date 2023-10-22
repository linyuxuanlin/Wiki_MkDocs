# Docker Basics

![Image](https://img.wiki-power.com/d/wiki-media/img/20210116153041.png)

It's a well-known fact that one of the most cumbersome tasks in software development is setting up the environment. Variations in runtime environments can lead to unexpected issues, but Docker offers a solution to this problem.

## Docker and Containerization Technology

Docker packages the software itself along with its required runtime environment, eliminating the need for manual environment configuration. Everything the application requires is encapsulated within the Docker container, ensuring that your environment matches that of the developer. This mitigates problems arising from disparities in runtime environments.

Docker employs containerization technology, often likened to **containers** themselves. Think of containers as standardized, large containers, similar to cargo containers used in various transportation modes like ships, trains, and trucks. These cargo containers can be loaded and unloaded across different carriers without consideration for the specific contents inside. Likewise, containerization technology bundles an application and all its dependencies into a self-contained, portable environment, known as a container.

The primary objective of containerization technology is rapid application deployment, scalability, and environment isolation. By packaging applications and their dependencies into containers, developers can ensure consistent application execution across different computers or servers without worrying about environment differences or dependency conflicts. This streamlines the application development process and simplifies deployment and management.

One significant advantage of containerization technology is its provision of lightweight virtualization. In contrast to traditional virtual machines, containers are more lightweight and consume fewer resources. Each container runs on the same host operating system kernel, sharing the host's resources. Consequently, containers start quickly, use minimal memory, and allow multiple containers to run concurrently on a single machine.

Docker is currently a popular containerization solution, consisting of three key components: Image, Container, and Repository.

- **Image**: An image is an executable file containing all the filesystem components (code, runtime, system tools, library files) and configurations required for an application. Images serve as templates for creating multiple container instances.
- **Container**: Containers are runtime instances created from images. Each container operates in an isolated and independent environment, allowing the execution of applications within them.
- **Repository**: Repositories are used for storing and sharing images. Users can push their own images to repositories and pull images created by others.

The relationship between containers and images is akin to objects and classes in object-oriented programming.

## Docker Installation and Configuration

Before installing Docker, you can use the following command to uninstall any previous package versions to avoid conflicts:

```shell
for pkg in docker.io docker-doc docker-compose podman-docker containerd runc; do sudo apt-get remove $pkg; done
```

For mainstream Linux systems, you can download and install Docker Engine using the official script. This requires root user privileges:

```shell
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh ./get-docker.sh --dry-run
```

Since Docker runs on and depends on the Linux environment, it has minimal efficiency overhead. However, if deploying Docker on other systems, you may need to install a virtual Linux environment first.

![Image](https://img.wiki-power.com/d/wiki-media/img/20230708005714.png)

For Docker installation on Windows, please refer to the official documentation [**Install Docker Desktop on Windows**](https://docs.docker.com/desktop/install/windows-install/).

For macOS installation, consult the official documentation [**Install Docker Desktop on Mac**](https://docs.docker.com/desktop/install/mac-install/).

After following the installation process, you can use the following command to verify if Docker has been successfully installed:

```shell
docker version
```

If you have installed Docker Engine on Linux and wish to use it as a non-root user, you can configure permissions using the following commands:

```shell
sudo groupadd docker
sudo usermod -aG docker $USER
```

After completing the configuration, you may need to log out and log back in to update the permissions.

If you encounter any installation issues, please refer to the official documentation [**Troubleshoot Docker Engine installation**](https://docs.docker.com/engine/install/troubleshoot/).

## Example: Hello World

Let's demonstrate Docker using the official hello-world example. Open your terminal or command prompt and enter the following command to run the hello-world container:

```shell
docker run hello-world
```

This command will download the hello-world image from the Docker image repository, create, and run the container. When you see the "hello world" output, it means the execution was successful.

## Some Common Docker CLI Commands

Docker provides a powerful set of commands for managing and operating containers, images, networks, and other resources. Here are some commonly used Docker CLI commands:

- `docker run`: Creates and runs a new container based on a specified image. For example, `docker run -d -p 8080:80 nginx` will run an NGINX container in the background, mapping the host's port 8080 to the container's port 80.
- `docker ps`: Lists running containers. By default, it displays information such as the container ID, image, and command of running containers. You can use `docker ps -a` to show all containers, including those that have stopped.
- `docker stop`: Stops one or more running containers, specifying the container's ID or name. For example, `docker stop mycontainer` stops the container named `mycontainer`.
- `docker start`: Starts one or more stopped containers, using either the container's ID or name.
- `docker restart`: Restarts one or more containers.
- `docker rm`: Deletes one or more containers. To delete a running container, you can use `docker rm -f`.
- `docker images`: Lists local images, showing image IDs, sizes, creation times, and more.
- `docker rmi`: Deletes one or more images, specifying the image's ID or tag. For example, `docker rmi myimage:1.0` deletes an image named `myimage` with tag `1.0`.
- `docker build`: Builds a custom image based on a Dockerfile. For instance, `docker build -t myimage:1.0 .` builds an image named `myimage` with tag `1.0` from the Dockerfile in the current directory.
- `docker exec`: Executes a command within a running container, specifying the container's ID or name and the command. For example, `docker exec -it mycontainer bash` starts a new interactive terminal in the container named `mycontainer`.

These are some common Docker commands for managing and operating containers and images. There are more commands to explore, which you can find by running `docker --help` to view the full command list and additional options. For further Docker-related knowledge, please refer to upcoming articles.

- [**Docker Compose - Image Orchestration Tool**](https://example.com/DockerCompose-Image-Orchestration-Tool/)
- [**Encapsulating Applications as Docker Containers**](https://example.com/Encapsulating-Applications-as-Docker-Containers/)

If you wish to dive right into practical implementation, you can also refer to the following series of articles:

- [Setting Up Your Own HomeLab](Homelab - Setting Up Your Own HomeLab)
- [Homelab - Lightweight Server Management Panel CasaOS](Homelab - Lightweight Server Management Panel CasaOS)
- [Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager](Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager)
- [Homelab - Intranet Penetration Tool frp](Homelab - Intranet Penetration Tool frp)
- [Homelab - Free Intranet Penetration Alternative Cloudflared](Homelab - Free Intranet Penetration Alternative Cloudflared)
- [Homelab - Online Code Editor code-server](Homelab - Online Code Editor code-server)
- [Homelab - Website Status Monitoring Tool Uptime Kuma](Homelab - Website Status Monitoring Tool Uptime Kuma)
- [Homelab - High-Quality Image Compression Tool TinyPNG-docker](Homelab - High-Quality Image Compression Tool TinyPNG-docker)
- [Homelab - Minimalist Personal Bookmark Navigation Site Flare](Homelab - Minimalist Personal Bookmark Navigation Site Flare)
- [Homelab - Container Application Management Platform Portainer](Homelab - Container Application Management Platform Portainer)
- [Homelab - Cross-Device Synchronization Tool Syncthing](Homelab - Cross-Device Synchronization Tool Syncthing)
- [Homelab - Fragmented Note Tool memos](Homelab - Fragmented Note Tool memos)
- [Homelab - Powerful Wiki System Wiki.js](Homelab - Powerful Wiki System Wiki.js)
- [Homelab - Self-Hosted Password Manager Vaultwarden](Homelab - Self-Hosted Password Manager Vaultwarden)
- [Homelab - Cloud-Compatible Image Hosting System Cloudreve](Homelab - Cloud-Compatible Image Hosting System Cloudreve)
- [Homelab - Self-Hosted RSS Aggregator FreshRSS](Homelab - Self-Hosted RSS Aggregator FreshRSS)
- [Homelab - Multi-Protocol Bastion Host Next Terminal](Homelab - Multi-Protocol Bastion Host Next Terminal)
- [Homelab - Multifunctional PDF Toolbox Stirling-PDF](Homelab - Multifunctional PDF Toolbox Stirling-PDF)
- [Homelab - Website Favicon Retrieval Tool iconserver](Homelab - Website Favicon Retrieval Tool iconserver)
- [Homelab - Tool for Automatically Updating Docker Containers Watchtower](Homelab - Tool for Automatically Updating Docker Containers Watchtower)
- [Homelab - File List Program Supporting Multiple Storage Alist](Homelab - File List Program Supporting Multiple Storage Alist)
- [Homelab - Feature-Rich Kanban Software WeKan](Homelab - Feature-Rich Kanban Software WeKan)
- [Homelab - Podcast and Audiobook Server Audiobookshelf](Homelab - Podcast and Audiobook Server Audiobookshelf)
- [Homelab - Cloud Music Server Navidrome](Homelab - Cloud Music Server Navidrome)
- [Homelab - Movie and Media Server Jellyfin](Homelab - Movie and Media Server Jellyfin)
- [Homelab - eBook Management Server calibre-web](Homelab - eBook Management Server calibre-web)
- [Homelab - Smart Home Server Home Assistant](Homelab - Smart Home Server Home Assistant)
- [Homelab - Flashcard-Based Memory Aid Software Anki](Homelab - Flashcard-Based Memory Aid Software Anki)

## References and Acknowledgments

- [Docker - From Beginner to Practice](https://yeasy.gitbook.io/docker_practice/)
- [Docker Tutorial](https://www.runoob.com/docker/docker-tutorial.html)
- [Getting Started with Docker](http://www.ruanyifeng.com/blog/2018/02/docker-tutorial.html)
- [Installing Docker on CentOS](to_be_replaced[3])

[to_be_replaced[1]]
[to_be_replaced[2]]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.