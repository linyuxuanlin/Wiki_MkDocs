# Docker Compose - Image Orchestration Tool

![](https://img.wiki-power.com/d/wiki-media/img/20210117130925.jpg)

Docker Compose is an image orchestration tool for Docker. It is highly recommended to use Docker Compose as the default way to work with Docker, as it not only simplifies the configuration and deployment of images but also offers an easier way to manage multiple image services, including specifying their startup order, which is not possible when using command-line methods.

While Docker's philosophy emphasizes decoupling (one image, one process), maximizing reusability, and avoiding encapsulating multiple services within a single image, there are cases where multiple services need to be started simultaneously. For example, a typical web application requires coordination between a server and a database. In such scenarios, you would need to deploy separate containers for each, and sometimes certain services need to be started in a specific order. This complexity can lead to a considerable number of required images and operational steps.

Docker Compose addresses this issue by allowing you to define all the necessary images (including their attributes, network configurations, and mounted storage volumes) and their startup order in a single YAML file. By running this configuration file, you can start containers according to your requirements and procedures without manually handling each container. Below is an example of a Docker Compose file used to deploy a web service:

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

In this YAML file, instances of `web` and `database` are defined and launched.

## Installation and Configuration of Docker Compose

Docker Compose relies on Docker Engine, so make sure you have Docker Engine installed before proceeding. If you haven't installed Docker Engine yet, you can refer to the previous tutorial: [**Docker Fundamentals**](to_be_replace[3]), to install Docker Engine.

If you are using the Windows/MacOS/Linux desktop client, you don't need to install Docker Compose separately, as it's already included. Here, we will explain how to install Docker Compose on a Linux Docker Engine environment.

For Ubuntu and Debian, use the following commands to install Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

For RPM-based Linux distributions such as CentOS, use the following commands to install Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

Once the installation is complete, verify its success using the following command:

```shell
docker compose version
```

## How to Use Docker Compose

In general, we create a `compose.yaml` file (or the older version, `docker-compose.yml`, which is also compatible) and place it in a directory named after the application, for example, `web/compose.yaml`.

To run the application, simply execute the `docker compose up` command in this directory, and it will start the services according to the configuration in the YAML file. (You can run it in the background with the `-d` flag.)

To stop the running application stack, use `docker compose down`.

## Writing Docker Compose Files

The default way to work with Docker Compose is to create a YAML-format file, typically named `compose.yaml`. Below is a template example that includes all available parameters (although you don't necessarily need to use all of them):

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

In a `compose.yaml` file, you typically include the following parameters:


- **version**: This field is used solely to display the version information of the Compose file. It is associated with the Docker Engine version, and newer versions may introduce additional functionality features or syntax changes. For more information, please refer to the official documentation [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/).

- **services**: This section defines the various services (containers) included in this Compose file. Each service represents an independent container, and you can specify details such as its image, port mappings, environment variables, and more.

- **container_name**: This is the name of the container, not mandatory, but must be unique within the Compose file.

- **networks**: This section defines the network configurations between services. You can create custom networks and connect services to these networks to facilitate communication between containers.

- **volumes**: This section defines the volume mounting configuration for containers. It allows you to associate directories or files within the container with directories or files on the host, enabling data persistence and sharing. It is equivalent to the `-v` parameter in Docker CLI.

- **environment** (or `env_file`): This field specifies the file name and path for the container's environment variables or indicates that these variables should be loaded from the specified file. If there are no environment variables to configure, you can omit this field. If the environment variables are in a file named `.env` in the current directory, it can also be omitted. This is similar to the `-e` parameter in Docker CLI.

- **build**: This option allows you to start the container using a built image and specifies the path to the Dockerfile.

- **image**: It specifies the image to be used for the container. You can use images from public image repositories or specify a local Dockerfile.

- **ports**: This field defines the port mapping relationship between the container and the host machine and allows you to specify the mapping protocol (TCP or UDP). This is similar to the `-p` parameter in Docker CLI.

- **depends_on**: This field defines the dependency relationships between services. You can specify one or more service names, indicating that the current service depends on the successful startup of these services.

- **restart**: This field defines the container's restart strategy. It can be set to `no` (no automatic restart), `always` (always automatically restart), `unless-stopped` (automatically restart, unless manually stopped), or `on-failure` (only restart on failure). This is similar to the `--restart` parameter in Docker CLI.

- **command**: It specifies the command to be executed when the container starts, which can be used to override the default startup command in the container image.

- **volumes_from**: This field specifies the source container from which the container should mount volumes.

## Some Common Docker Compose Commands

Here are some commonly used Docker Compose commands for managing and operating the services defined in the `compose.yaml` file:

- `docker compose up`: This command builds the images defined in the compose file and starts the containers. If necessary, it will automatically build images (if the Dockerfile has changed) and then start all the defined services. To start in the background, add the `-d` parameter.

- `docker compose down`: This command stops and removes all containers, networks, and volumes defined in the compose file. It stops running services and cleans up all related resources.

- `docker compose pull`: This command pulls all the images defined in the compose file or is used to update images.

- `docker compose start`: It starts the containers created in the compose file without recreating containers or rebuilding images.

- `docker compose stop`: This command stops the containers created in the compose file but does not remove them.

- `docker compose restart`: It restarts the containers created in the compose file.

- `docker compose pause`: This command pauses the containers created in the compose file, temporarily halting their execution.

- `docker compose unpause`: This command resumes the containers in the compose file that have been paused, allowing them to continue running.

- `docker compose ps`: Displays the status of **all** containers running in the compose file.

- `docker compose logs`: View the log output of the containers in the compose file.

- `docker compose exec`: Executes a command within a running container in the compose file, for example, `docker exec -it [compose-name] /bin/bash`.

These are some common commands, and you can also execute `docker compose --help` to see more available commands.

## Environment Variables

In Docker Compose, while environment variables are not mandatory, they are highly recommended for several reasons:

1. **Flexibility and Configurability**: Easily adjust application configuration without modifying Docker images or rebuilding containers.

2. **Security and Isolation**: By storing sensitive information in environment variables rather than directly in code or configuration files, you can enhance the security of your application.

3. **Cross-Platform Compatibility**: Different operating systems or platforms can pass different configuration information via environment variables, avoiding the need to modify configuration files or image code.

4. **Simplified Deployment and Management**: Standardizing the use of environment variables to configure various container parameters reduces redundancy in configuration files, making the whole process clearer and easier to maintain.

5. **Integration and Automation**: By integrating with CI/CD and automation tools, you can automatically pass application configuration parameters to Docker containers, enabling automated deployment and integration.

Environment variables are typically stored in a file with a `.env` extension. This file is usually created in the same directory as the `compose.yaml` file. Here's an example:

```dotenv title=".env"
TAG=v1.5
```

In the `compose.yaml` file, you can directly reference environment variables:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Tips

There is a website called [**composerize**](https://www.composerize.com/) that can convert Docker CLI commands into Docker Compose YAML. Please note that the conversion results may not always be accurate and should be validated.

## References and Acknowledgments

- [Using Docker Compose Instead of Docker Run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Install Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [In-Depth Explanation of Docker-Compose Template File Parameters](https://blog.51cto.com/14154700/2466054)
- [Surprisingly, Synology NAS Can Also Use Docker Compose!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - From Basics to Practical Application](https://docker-practice.github.io/zh-cn/)
- [Docker Series - Understanding the Configuration Files of Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.