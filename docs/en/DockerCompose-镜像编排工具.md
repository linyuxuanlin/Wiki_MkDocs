# Docker Compose - Image Orchestration Tool

![](https://media.wiki-power.com/img/20210117130925.jpg)

Docker Compose is an image orchestration tool for Docker. It is recommended to use Docker Compose as the default way to work with Docker because it not only makes it convenient to configure and deploy images but also simplifies the setup of multi-image services and allows you to specify their startup order, which is not easily achievable when using command-based methods.

While Docker's philosophy encourages decoupling (one process per image) and promoting reusability without encapsulating multiple services within a single image, some applications require the simultaneous startup of multiple services. For instance, a typical web application necessitates the coordination of a server and a database. This would require you to deploy two containers separately, and in some cases, certain services need to be started in a specific order. This can make the required images and operational steps quite complex.

Docker Compose consolidates the images that need to be invoked (including all necessary service and container properties, network configuration, and mounted storage volumes), as well as their startup order, into a single YAML file. By executing this configuration file directly, you can run the containers according to your specific requirements and steps without the need for manual operations on each container. Below is a Docker Compose example used to deploy a web service:

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

In this YAML file, we define and start two instances: `web` and `database`.

## Installation and Configuration of Docker Compose

Docker Compose relies on Docker Engine, so make sure you have Docker Engine installed before proceeding. If you haven't installed it yet, you can refer to the previous tutorial: [**Docker Fundamentals**](https://wiki-power.com/Docker%E5%9F%BA%E7%A1%80%E7%9F%A5%E8%AF%86/), for Docker Engine installation.

If you are using the Windows/MacOS/Linux desktop client, you do not need to install Docker Compose separately because it is already included. Below are the installation instructions for Docker Compose in a Linux Docker Engine environment.

For Ubuntu and Debian, use the following commands to install Docker Compose:

```shell
sudo apt-get update
sudo apt-get install docker-compose-plugin
```

For RPM-based Linux distributions, such as CentOS, use the following commands to install Docker Compose:

```shell
sudo yum update
sudo yum install docker-compose-plugin
```

After installation, you can verify its success with the following command:

```shell
docker compose version
```

## How to Use Docker Compose

Typically, we create a `compose.yaml` file (in older versions, it was named `docker-compose.yml`, and it's still compatible) and place it in a directory named after your application, such as `web/compose.yaml`.

To run this program, simply execute the `docker compose up` command in this directory, and it will start the services as configured in the YAML file. You can run it in the background by adding the `-d` option.

To stop the running application stack, you can use `docker compose down`.

## Writing Docker Compose Files

The default way to open Docker Compose is by creating a YAML-formatted file named `compose.yaml`. Below is a template example that includes all available parameters (though not all of them are necessarily required):

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

- **version**: This is used solely to display the version information of the compose file. It is associated with the version of Docker Engine and may introduce new feature enhancements or syntax updates in updated versions. Please refer to the official documentation [**Compose file versions and upgrading**](https://docs.docker.com/compose/compose-file/compose-versioning/) for more details.

- **services**: This section defines the various services (containers) included in this compose file. Each service represents an independent container and can be configured with attributes such as image, port mappings, environment variables, and more.

- **container_name**: This specifies the name of the container. While not mandatory, it must be unique to avoid naming conflicts.

- **networks**: Networks define the network configurations between services. You can create custom networks and connect services to them, enabling communication between containers.

- **volumes**: This section defines the configuration for mounting volumes in containers. It allows you to associate directories or files within a container with directories or files on the host, facilitating data persistence and sharing. This is equivalent to the `-v` parameter in Docker CLI.

- **environment** (or `env_file`): This option specifies the file name and path for the container's environment variables or indicates that environment variables should be loaded from this file. If no environment variables are configured, you can omit this section. If the environment variable file is named `.env` and located in the current directory, it can also be omitted. This is equivalent to the `-e` parameter in Docker CLI.

- **build**: Launches the container using a built image and specifies the path to the Dockerfile.

- **image**: Specifies the image to be used by the container. You can use images from public image repositories or specify a local Dockerfile.

- **ports**: Defines the mapping of ports between the container and the host, allowing you to specify the protocol (TCP or UDP) for the mapping. This is equivalent to the `-p` parameter in Docker CLI.

- **depends_on**: Specifies the dependency relationships between services. You can specify one or more service names, indicating that the current service relies on these services to be running before it starts.

- **restart**: Defines the restart policy for the container. It can be set to `no` (no automatic restart), `always` (always automatically restart), `unless-stopped` (automatically restart unless manually stopped), or `on-failure` (automatically restart only if the container crashes). This is equivalent to the `--restart` parameter in Docker CLI.

- **command**: Specifies the command to be executed when the container starts. This can be used to override the default startup command defined in the container image.

- **volumes_from**: Specifies the source container from which the current container should mount volumes.

## Some Common Docker Compose Commands

Here are some commonly used Docker Compose commands for managing and operating services defined in the `compose.yaml` file:

- `docker compose up`: This command builds the images defined in the compose file and starts the containers. If necessary, it will automatically build the images (if the Dockerfile has changed) and then start all the defined services. To start it in the background, add the `-d` flag.

- `docker compose down`: This command stops and removes all containers, networks, and volumes defined in the compose file. It stops running services and cleans up all associated resources.

- `docker compose pull`: This command pulls all images defined in the compose file, or is used to update images.

- `docker compose start`: This command starts containers that have already been created in the compose file. It does not recreate containers or rebuild images.

- `docker compose stop`: This command stops containers that have already been created in the compose file but does not remove them.

- `docker compose restart`: This command restarts containers that have already been created in the compose file.

- `docker compose pause`: This command temporarily pauses containers that have already been created in the compose file, causing them to stop running.

- `docker compose unpause`: This command resumes containers that have been paused in the compose file, allowing them to continue running.

- `docker compose ps`: This command displays the status of **all** containers currently running in the compose file.

- `docker compose logs`: This command allows you to view the log output of containers in the compose file.

- `docker compose exec`: This command lets you execute commands within containers running in the compose file, similar to `docker exec -it [compose-name] /bin/bash`.

These are some common commands, and you can also run `docker compose --help` to see more available commands.

## Environment Variables

In Docker Compose, while environment variables are not mandatory, they are highly recommended for several reasons:

1. **Flexibility and Configurability**: They allow you to easily adjust the configuration of your application without modifying Docker images or rebuilding containers.

2. **Security and Isolation**: Storing sensitive information in environment variables rather than directly in code or configuration files improves the security of your application by enabling separate access control for these variables.

3. **Cross-Platform Compatibility**: Environment variables can pass different configuration information to containers on different operating systems or platforms without modifying configuration files or image code.

4. **Simplified Deployment and Management**: By uniformly using environment variables to configure parameters for different containers, you reduce redundancy in configuration files, making the process clearer and easier to maintain.

5. **Integration and Automation**: By combining environment variables with CI/CD and automation tools, you can automatically pass application configuration parameters to Docker containers, enabling automated deployment and integration.

Environment variables are typically defined in a `.env` file, which is commonly placed in the same directory as the `compose.yaml`. Here's an example:

```dotenv title=".env"
TAG=v1.5
```

You can reference these environment variables directly in your `compose.yaml`:

```yaml title="compose.yaml"
services:
  web:
    image: "webapp:${TAG}"
```

## Tips

There is a website called [**composerize**](https://www.composerize.com/) that can convert Docker CLI commands into Docker Compose YAML. The conversion results may not always be entirely accurate, so it's essential to verify the output.

## References and Acknowledgments

- [Using Docker Compose as an Alternative to Docker Run](https://beginor.github.io/2017/06/08/use-compose-instead-of-run.html)
- [How to Install Docker Compose](https://docs.docker.com/compose/install/#prerequisites)
- [In-Depth Explanation of Docker Compose Template File Parameters](https://blog.51cto.com/14154700/2466054)
- [Surprisingly, Synology NAS Can Also Utilize Docker Compose!](https://www.himiku.com/archives/docker-compose-for-synology-nas.html)
- [Docker - From Beginner to Practice](https://docker-practice.github.io/zh-cn/)
- [Docker Series - Understanding the Configuration Files of Docker Compose](https://blognas.hwb0307.com/linux/docker/3880)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
