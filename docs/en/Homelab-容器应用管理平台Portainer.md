# Homelab - Container Application Management Platform Portainer

![Portainer](https://media.wiki-power.com/img/202304111545899.png)

**Portainer** is a graphical management tool for container applications, including Docker, Docker Compose, Swarm, and Kubernetes. It allows you to manage Docker environments through a web interface and offers various features such as log viewing, container start and stop, image management, network management, and volume management.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.3"
services:
  portainer:
    container_name: ${STACK_NAME}_app
    image: portainer/portainer-ce:${APP_VERSION}
    ports:
      - ${APP_PORT_HTTP}:9000 # HTTP
    # - ${APP_PORT_HTTPS}:9443 # HTTPS (optional)
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
      - ${STACK_DIR}/portainer_data:/data
    restart: always
```

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `portainer`).

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # Customize your project storage path, e.g., ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose an available one
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Notes

Please note that the image for the community edition is `portainer/portainer-ce` and should be distinguished from the commercial edition (portainer-be).

## References and Acknowledgments

- [Official Website](https://www.portainer.io/)
- [Documentation](https://docs.portainer.io/)
- [GitHub Repository](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
