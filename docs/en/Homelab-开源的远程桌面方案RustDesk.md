# Homelab - Open Source Remote Desktop Solution RustDesk

![](https://media.wiki-power.com/img/20230531212854.png)

**RustDesk** is an open-source remote desktop solution that allows for remote access within the local network using clients from various platforms. This article primarily focuses on setting up your own server for external access.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"

networks:
  rustdesk-net:
    external: false

services:
  hbbs:
    container_name: ${STACK_NAME}_hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbs -r ${STACK_DOMAIN}:21117 -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: ${STACK_NAME}_hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbr -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

Within this docker compose file, two services are orchestrated:

- hbbs: RustDesk ID registration server
- hbbr: RustDesk relay server

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replacing `${STACK_NAME}` with `rustdesk-server`).

```dotenv title=".env"
STACK_NAME=rustdesk-server
STACK_DIR=xxx # Customize the project storage path, e.g., ./rustdesk-server
STACK_DOMAIN=xxx # Domain or IP where RustDesk server is deployed

# rustdesk-server
APP_VERSION=latest
```

Finally, run the command `docker compose up -d` at the same directory level as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

If you encounter the error `Registered email required (-m option). Please pay and register on https://rustdesk.com/server...`, it indicates that you may have downloaded an outdated package. To resolve this issue:

1. Find the latest DIGEST number (e.g., `83e259792b50`) on <https://hub.docker.com/r/rustdesk/rustdesk-server/tags>.
2. Use the command `docker image pull rustdesk/rustdesk-server:latest@sha256:83e259792b50` locally to download the latest package, ensuring to replace the final characters with your own.

## References and Acknowledgements

- [Official Website](https://rustdesk.com/)
- [Documentation](https://rustdesk.com/docs/en/self-host/)
- [GitHub Repository](https://github.com/rustdesk/rustdesk)
- [Docker Hub](https://hub.docker.com/r/rustdesk/rustdesk-server)
- [Setting up a RustDesk server using Docker](https://developer.aliyun.com/article/1299504)
- [Self-hosting Guide](https://rustdesk.com/docs/zh-cn/self-host/rustdesk-server-oss/install/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.