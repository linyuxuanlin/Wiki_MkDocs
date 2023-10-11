# Homelab - Website Status Monitoring Tool Uptime Kuma

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410160253.jpg)

**Uptime Kuma** is a status monitoring tool that supports multiple network protocols. It can monitor the real-time availability, response time, certificate validity period, etc. of multiple custom websites, and provides various notification methods.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  uptime-kuma:
    container_name: ${STACK_NAME}_app
    image: louislam/uptime-kuma:${APP_VERSION}
    ports:
      - ${APP_PORT}:3001
    volumes:
      - ${STACK_DIR}:/app/data
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `uptime-kuma`).

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # Customize the project storage path, such as ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

Note: If using a reverse proxy, please enable the `Websockets Support` feature.

## Reference and Acknowledgement

- [Official website](https://uptime.kuma.pet/)
- [Documentation](https://github.com/louislam/uptime-kuma/wiki)
- [GitHub repo](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
