# Docker Compose - Image Orchestration Tool

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20210117130925.jpg)

Docker Compose is an image orchestration tool for Docker. It is recommended to use Docker Compose as the default way to open Docker because it not only allows for easy configuration and deployment of images, but also makes it more convenient to configure multiple image services and even distinguish their startup order, which is not possible with command line opening.

Although the idea behind Docker is decoupling (one image per process), increasing reuse, and not encapsulating multiple services in one image, some applications require multiple services to be started simultaneously. For example, a typical web application requires at least a server and a database to work together. This means that you need to deploy two containers separately, and some services even need to be started in a certain order. This makes the required images and operations very complex.

Docker Compose writes all the required images (all required services, container properties, network configuration, and mounted storage volumes) and order in a YAML file. By running this configuration file directly, you can run containers according to the method and steps you need without manually operating each container. Here is a Docker Compose example for deploying a web service:

Translate the following Chinese article into English, maintain the original markdown format.

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

In this YAML file, two instances, `web` and `database`, are defined and started.

## Installation and Configuration of Docker Compose

Docker Compose depends on Docker Engine, so please make sure you have installed Docker Engine environment first. If you haven't installed it yet, you can refer to the previous tutorial: [**Docker Basics**](https://wiki-power.com/Docker%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/), to install Docker Engine.

If you are using the Windows/MacOS/Linux desktop client, you do not need to install Docker Compose separately, as it is already included. The following introduces the installation method of Docker Compose under Linux Docker Engine environment.

To install Docker Compose on Ubuntu and Debian, use the following command:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

For RPM-based Linux distributions (such as CentOS), use the following command:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

After installation, use the following command to check if it was successful:

```shell
docker compose version
```

## How to use Docker Compose

Generally, we create a `compose.yaml` file (old versions use `docker-compose.yml`, which is also compatible) and place it in a directory named after the application, such as `web/compose.yaml`.

To run the program, simply execute the `docker compose up` command in this directory to start the service according to the configuration in the YAML file. (Adding the `-d` parameter can run it in the background.)

To stop the application stack, use `docker compose down`.

## Writing Docker Compose files

The default way to open Docker Compose is to create a YAML format file named `compose.yaml`. Here is a sample template that includes all available parameters (but not necessarily all required):

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

In a `compose.yaml` file, the following parameters are typically included:

- **version**: Used to display the version information of the compose file. It is associated with the Docker Engine version, and updated versions may have new functional features or syntax. Please refer to the official documentation [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/).
- **services**: Defines the various services (containers) included in this compose file. Each service is an independent container and can define its image, port mapping, environment variables, etc.
- **container_name**: Container name, not required, but must not have duplicate names.
- **networks**: Defines the network configuration between services. Custom networks can be created and services can be connected to these networks to achieve communication between containers.
- **volumes**: Defines the mount configuration of the container's volumes. Directories or files in the container can be associated with directories or files on the host to achieve data persistence and sharing. Equivalent to the `-v` parameter in Docker CLI.
- **environment** (or `env_file`): Specifies the file name and path of the container's environment variables, and specifies that the environment variables are loaded from this file. If there are no configured environment variables, they can be ignored. If the environment variables are in the current directory and named `.env`, they can also be omitted. Equivalent to the `-e` parameter in Docker CLI.
- **build**: Start using the built image. Specify the path of the Dockerfile file.
- **image**: Specifies the image used by the container. Public images in the image repository can be used, or local Dockerfile files can be specified.
- **ports**: Defines the port mapping relationship between the container and the host, and can also specify the mapping protocol (TCP or UDP). Equivalent to the `-p` parameter in Docker CLI.
- **depends_on**: Defines the dependency relationship between services. One or more service names can be specified to indicate that the current service depends on the startup of these services.
- **restart**: Defines the restart strategy for the container. It can be set to `no` (no automatic restart), `always` (always automatically restart), `unless-stopped` (automatically restart unless the container is manually stopped), or `on-failure` (only automatically restart when it crashes). Equivalent to the `--restart` parameter in Docker CLI.
- **command**: Specifies the command to be executed when the container starts, which can be used to override the default startup command in the container image.
- **volumes_from**: Specifies the source container from which the container is to mount volumes.

## Some Common Docker Compose Commands

Here are some common Docker Compose commands used to manage and operate services defined in the `compose.yaml` file:

- `docker compose up`: Builds the images defined in the compose file and starts the containers. If necessary, it will automatically build the images (if the Dockerfile has changed) and then start all the defined services. Use the `-d` parameter to start in the background.
- `docker compose down`: Stops and removes all containers, networks, and volumes defined in the compose file. It will stop running services and clean up all related resources.
- `docker compose pull`: Pulls all images defined in the compose file or updates the images.
- `docker compose start`: Starts the containers already created in the compose file without recreating the containers or rebuilding the images.
- `docker compose stop`: Stops the containers already created in the compose file without removing the containers.
- `docker compose restart`: Restarts the containers already created in the compose file.
- `docker compose pause`: Pauses the containers already created in the compose file, temporarily stopping them from running.
- `docker compose unpause`: Resumes the paused containers in the compose file, allowing them to continue running.
- `docker compose ps`: Shows the status of **all** running containers in the compose file.
- `docker compose logs`: Views the log output of the containers in the compose file.
- `docker compose exec`: Executes a command in a running container in the compose file. For example, `docker exec -it [compose-name] /bin/bash`.

These are some common commands, and you can also execute `docker compose --help` to see more available commands.

## Environment Variables

In Docker Compose, although environment variables are not mandatory, it is recommended to use them more often because of the following advantages:

1. **Flexibility and Configurability**: Easily adjust application configuration information without modifying Docker images or rebuilding containers.
2. **Security and Isolation**: By storing sensitive information in environment variables instead of directly in code or configuration files, and authorizing environment variables separately, the security of the application can be improved.
3. **Cross-Platform Compatibility**: Different operating systems or platforms can pass different configuration information through environment variables without modifying configuration files or image code.
4. **Simplified Deployment and Management**: By using environment variables uniformly to configure parameters for different containers, duplicate content in configuration files can be reduced, making the entire process clearer and easier to maintain.
5. **Integration and Automation**: By combining with CI/CD and automation tools, application configuration parameters can be automatically passed to Docker containers, achieving automated deployment and integration.

An environment variable is a file with a `.env` suffix, usually created directly in the same directory as `compose.yaml` with a name like `.env`. Here is an example:

```dotenv title=".env"
TAG=v1.5
```

Environment variables can be called directly in `compose.yaml`:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Tips

There is a website called [**composerize**](https://www.composerize.com/) that converts Docker CLI to Docker Compose YAML, but the conversion results may not be accurate and should be verified.

## References and Acknowledgments

- [Using Docker Compose instead of Docker Run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Install Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [Detailed Explanation of Parameters in Docker-Compose Template Files](https://blog.51cto.com/14154700/2466054)
- [It turns out that Synology can also use Docker Compose!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - From Beginner to Practice](https://docker-practice.github.io/zh-cn/)
- [Docker Series - Understanding the Configuration File of Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.