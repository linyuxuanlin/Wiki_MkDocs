# Homelab - Cross-Device Sync Tool Syncthing

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111529987.png)

**Syncthing** is a free and open-source file synchronization application that can synchronize files and folders between multiple devices and supports incremental synchronization. I use it to back up data from my server to my NAS for centralized management.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    environment: # Needs to be run as root to read other docker directories or host root directories
      - PUID=0
      - PGID=0
    volumes:
      - ${APP_SYNC_DIR}:/DATA
      - ${STACK_DIR}/config:/var/syncthing/config/
    ports:
      - ${APP_PORT}:8384 # Web UI
      - 22000:22000/tcp # TCP file transfers
      - 22000:22000/udp # QUIC file transfers
      - 21027:21027/udp # Receive local discovery broadcasts
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `syncthing`).

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # Custom project storage path, for example ./syncthing

# syncthing
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not occupied
APP_SYNC_DIR=xxxx # Custom path to be synchronized, such as /DATA
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

If you are prompted with insufficient permissions, try changing the `PUID` and `PGID` values to `0` and start with root permissions.

## References and Acknowledgments

- [Official Website](https://syncthing.net/)
- [Documentation](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [Forum](https://forum.syncthing.net/)
- [GitHub repo](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.