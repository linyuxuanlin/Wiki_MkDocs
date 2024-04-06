# Homelab - Cross-Device Synchronization Tool: Syncthing

![Syncthing Logo](https://media.wiki-power.com/img/202304111529987.png)

**Syncthing** is a free and open-source file synchronization application that allows you to sync files and folders across multiple devices while supporting incremental synchronization. I use it to back up data from my server to a NAS for centralized management.

## Deployment (Docker Compose)

To begin, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    environment: # It needs to run as root, or it won't be able to access other Docker directories or the host machine's root directory.
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

(Optional) It's recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `syncthing`).

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # Customize your project storage path, e.g., ./syncthing

# syncthing
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose one that is not already in use
APP_SYNC_DIR=xxxx # Customize the path you want to sync, e.g., /DATA
```

Finally, in the same directory as `compose.yaml`, execute the `docker compose up -d` command to start the orchestrated container.

## Configuration Notes

If you encounter permission issues, try changing the `PUID` and `PGID` values to `0` to run it with root privileges.

## References and Acknowledgments

- [Official Website](https://syncthing.net/)
- [Documentation](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [Forum](https://forum.syncthing.net/)
- [GitHub Repository](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

[Replace with Reference 1]  
[Replace with Reference 2]

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
