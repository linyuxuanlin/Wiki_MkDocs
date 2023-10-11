# Homelab - Jellyfin Media Server

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230531213856.png)

**Jellyfin** is an open-source media server that can be used to manage movies, TV shows, and more, and can be accessed and viewed on different devices. It can be used as an alternative to closed-source software such as Emby and Plex.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.5"
services:
  jellyfin:
    container_name: ${STACK_NAME}_app
    image: jellyfin/jellyfin:${APP_VERSION}
    #user: uid:gid
    #network_mode: 'host'
    ports:
      - ${APP_PORT}:8096
    volumes:
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/cache:/cache
      - ${DATA_DIR}:/media
    restart: "unless-stopped"
    # Optional - alternative address used for autodiscovery
    #environment:
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # Optional - may be necessary for docker healthcheck to pass if running in host network mode
    #extra_hosts:
    #  - "host.docker.internal:host-gateway"
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `jellyfin`).

```dotenv title=".env"
STACK_NAME=jellyfin
STACK_DIR=xxx # Custom project storage path, for example, ./jellyfin
DATA_DIR=xxx # Custom podcast storage path, for example, ./video

# jellyfin
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not occupied
```

If you have a NAS, you can also mount the storage space on the NAS through the NFS protocol, store music on the NAS to save server space, please refer to [**Expanding Synology NAS Hard Disk Space (NFS) under Linux**](https://wiki-power.com/en/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration

The official Jellyfin App can be used on mobile devices.

## References and Acknowledgments

- [Official website](https://jellyfin.org/)
- [Documentation](https://jellyfin.org/docs/general/installation/container#using-docker-compose)
- [GitHub repo](https://github.com/jellyfin/jellyfin)
- [Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin)
- [Demo site](https://demo.jellyfin.org/stable)

Sorry, there is no Chinese article provided for translation. Please provide the article for translation.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
