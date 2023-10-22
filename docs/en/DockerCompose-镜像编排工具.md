# Docker Compose - Image Orchestration Tool

![Docker Compose](https://img.wiki-power.com/d/wiki-media/img/20210117130925.jpg)

Docker Compose is the image orchestration tool for Docker. It is recommended to use Docker Compose as the default way to work with Docker, as it not only simplifies the configuration and deployment of images but also allows for the easy setup of multi-image services, with the ability to specify their startup sequence – a capability not present when using command-line methods.

While Docker promotes the idea of decoupling (one process per image), enhancing reusability and avoiding bundling multiple services within a single image, there are scenarios where multiple services need to run simultaneously. For example, a typical web application requires the coordination of a server and a database. This means you would need to deploy two containers separately, and in some cases, specific services must be started in a particular order. This complexity can lead to a need for multiple images and a more intricate set of operational steps.

Docker Compose allows you to define all the images to be invoked (including properties, network configurations, and mounted storage volumes) and their startup order in a single YAML file. By running this configuration file, you can start containers according to your requirements without manual intervention for each container. Below is a Docker Compose example for deploying a web service:

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

Docker Compose relies on Docker Engine, so please ensure you have Docker Engine already installed. If you haven't done so, you can refer to the previous tutorial on [**Docker Basics**](to_be_replace[3]) for Docker Engine installation.

For users of Windows, MacOS, or Linux desktop clients, Docker Compose is included by default, so there's no need for a separate installation. The following instructions cover the installation of Docker Compose in a Linux Docker Engine environment.

For Ubuntu and Debian, use the following commands to install Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

For RPM-based Linux distributions like CentOS, use the following commands to install Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

After installation, use the following command to verify a successful installation:

```markdown
```shell
docker compose version
```

## How to Use Docker Compose

In general, to use Docker Compose, you create a `compose.yaml` file (older versions used `docker-compose.yml`, which is also compatible) and place it in a directory named after your application, such as `web/compose.yaml`.

To run the application, simply execute the `docker compose up` command in this directory, and it will start the services as configured in the YAML file. You can run it in the background by adding the `-d` flag.

To stop the running application stack, you can use `docker compose down`.

## Writing Docker Compose Files

The default way to configure Docker Compose is by creating a YAML format file named `compose.yaml`. Below is a template example that includes all available parameters (though not all are necessarily required):

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
```

- **version**: This field is used solely to display the version information of the Compose file. It is associated with the Docker Engine version, and updates to the version may introduce new functionality features or syntax. Please refer to the official documentation [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/).

- **services**: This section defines the various services (containers) included in this Compose file. Each service represents an independent container and can specify its image, port mappings, environment variables, and more.

- **container_name**: This is the name of the container. It is not mandatory, but duplicate names should be avoided.

- **networks**: This section defines the network configuration between services. You can create custom networks and connect services to these networks to enable communication between containers.

- **volumes**: Here, you define the volume mounting configuration for containers. You can associate directories or files within a container with directories or files on the host, achieving data persistence and sharing. This is equivalent to the `-v` parameter in Docker CLI.

- **environment** (or `env_file`): You specify the filename and path for the container's environment variables or indicate that the environment variables should be loaded from this file. This field can be omitted if no environment variables are configured. If the environment variables are in the current directory and named `.env`, you can omit this field. This is equivalent to the `-e` parameter in Docker CLI.

- **build**: Launches using a built image and specifies the path to the Dockerfile.

- **image**: Specifies the image that the container will use. You can use images from public image repositories or specify a local Dockerfile.

- **ports**: Defines the port mapping relationship between the container and the host, and you can also specify the mapping protocol (TCP or UDP). This is equivalent to the `-p` parameter in Docker CLI.

- **depends_on**: Defines dependencies between services. You can specify one or more service names, indicating that the current service depends on the start of these services.

- **restart**: Defines the restart policy for the container. It can be set to `no` (no automatic restart), `always` (always automatically restart), `unless-stopped` (automatically restart unless the container is manually stopped), or `on-failure` (only automatically restart on failure). This is equivalent to the `--restart` parameter in Docker CLI.

- **command**: Specifies the command to be executed when the container starts. This can be used to override the default startup command in the container image.

- **volumes_from**: Specifies the source container from which the container should mount volumes.

## Some Common Docker Compose Commands

Here are some common Docker Compose commands used for managing and operating the services defined in the `compose.yaml` file:

- `docker compose up`: This command builds the images defined in the compose file and starts the containers. If necessary, it will automatically build images (if the Dockerfile has changed) and then start all the defined services. If you want to start it in the background, add the `-d` parameter.

- `docker compose down`: This command stops and removes all containers, networks, and volumes defined in the compose file. It will stop running services and clean up all related resources.

- `docker compose pull`: This command fetches all images defined in the compose file, or can be used to update images.

- `docker compose start`: This command starts the containers created in the compose file, without recreating the containers or rebuilding the images.

- `docker compose stop`: This command stops the containers created in the compose file but does not remove them.

- `docker compose restart`: This command restarts the containers created in the compose file.

- `docker compose pause`: This command pauses the containers created in the compose file, temporarily stopping their execution.

- `docker compose unpause`: This command resumes containers that have been paused in the compose file, allowing them to continue running.

- `docker compose ps`: This command displays the status of all containers currently running in the compose file.

- `docker compose logs`: This command allows you to view the log output of containers in the compose file.

- `docker compose exec`: This command is used to execute commands within running containers in the compose file, similar to `docker exec -it [compose-name] /bin/bash`.

These are some common commands, and you can also run `docker compose --help` to see more available commands.

## Environment Variables

In Docker Compose, while environment variables are not mandatory, it is highly recommended to use them for several reasons:

1. **Flexibility and Configurability**: Easily adjust application configuration without the need to modify Docker images or rebuild containers.

2. **Security and Isolation**: Storing sensitive information in environment variables, rather than hardcoding them in code or configuration files, enhances application security by isolating sensitive data.

3. **Cross-Platform Compatibility**: Different operating systems or platforms can pass different configuration information through environment variables, without the need to modify configuration files or image code.

4. **Simplified Deployment and Management**: Standardizing the use of environment variables to configure different container parameters reduces redundancy in configuration files, making the entire process clearer and easier to maintain.

5. **Integration and Automation**: By integrating with CI/CD and automation tools, you can automatically pass application configuration parameters to Docker containers, enabling automated deployment and integration.

Environment variables are typically stored in a file with a `.env` extension, usually created in the same directory as the `docker-compose.yaml` file. Here is an example:

```dotenv title=".env"
TAG=v1.5
```

In the `docker-compose.yaml` file, you can directly reference these environment variables:

```yaml title="docker-compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Tips

There is a website called [**composerize**](https://www.composerize.com/) that can convert Docker CLI commands into Docker Compose YAML. Please note that the conversion results may not always be entirely accurate and should be verified.

## References and Acknowledgments

- [Replacing `docker run` with Docker Compose](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [Installing Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [In-Depth Explanation of Docker-Compose Template Parameters](https://blog.51cto.com/14154700/2466054)
- [Surprisingly, You Can Use Docker Compose on Synology NAS!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - From Beginner to Practice](https://docker-practice.github.io/zh-cn/)
- [Docker Series - Understanding the Configuration Files of Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

[To be replaced[1]]
[To be replaced[2]]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.