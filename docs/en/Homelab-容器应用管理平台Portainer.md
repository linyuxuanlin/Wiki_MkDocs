# Homelab - Container Application Management Platform Portainer

![](https://img.wiki-power.com/d/wiki-media/img/202304111545899.png)

**Portainer** is a graphical management tool for container applications (including Docker / Docker compose / Swarm / Kubernetes) that allows you to manage Docker environments through a web interface. It also provides many features such as log viewing, container start and stop, image management, network, volume management, etc.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you don't want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `portainer`).

```dotenv title=".env"
STACK_NAME=portainer
STACK_DIR=xxx # Custom project storage path, such as ./portainer

# portainer
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Notes

Note that the community edition image is `portainer/portainer-ce`, which is different from the commercial edition (portainer-be).

## References and Acknowledgments

- [Official Website](https://www.portainer.io/)
- [Documentation](https://docs.portainer.io/)
- [GitHub repo](https://github.com/portainer/portainer)
- [Docker Hub](https://hub.docker.com/r/portainer/portainer-ce)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
