# Homelab - Jellyfin Media Server for Movies and TV Shows

![Jellyfin](https://media.wiki-power.com/img/20230531213856.png)

**Jellyfin** is an open-source media server designed for managing movies, TV shows, and more, allowing you to access and view your content on various devices. It serves as an alternative to proprietary software like Emby and Plex.

## Deployment (Using Docker Compose)

Start by creating a `compose.yaml` file and paste the following content:

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
    # Optional - an alternative address used for autodiscovery
    #environment:
    #  - JELLYFIN_PublishedServerUrl=http://example.com
    # Optional - may be necessary for docker healthcheck to pass if running in host network mode
    #extra_hosts:
    #  - "host.docker.internal:host-gateway"
```

(Optional) It's recommended to create a `.env` file at the same level as `compose.yaml` to customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `jellyfin`).

```dotenv title=".env"
STACK_NAME=jellyfin
STACK_DIR=xxx # Customize your project storage path, e.g., ./jellyfin
DATA_DIR=xxx # Customize your media storage path, e.g., ./video

# jellyfin
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose an available one
```

If you have a NAS, you can also mount storage space from your NAS using the NFS protocol, saving server space for your media. For more details, please refer to [**Mounting Synology NAS Hard Drives for Space Expansion on Linux (NFS)**](https://wiki-power.com/en/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9C%BC%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Notes

For mobile access, you can consider using the official Jellyfin App.

## References and Acknowledgments

- [Official Website](https://jellyfin.org/)
- [Documentation](https://jellyfin.org/docs/general/installation/container#using-docker-compose)
- [GitHub Repository](https://github.com/jellyfin/jellyfin)
- [Docker Hub](https://hub.docker.com/r/jellyfin/jellyfin)
- [Demo Website](https://demo.jellyfin.org/stable)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
