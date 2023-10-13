# Homelab - Podcast and Audiobook Server Audiobookshelf

![](https://img.wiki-power.com/d/wiki-media/img/20230531204505.png)

**Audiobookshelf** is a self-hosted podcast and audiobook server that allows for easy searching, automatic detection and downloading of podcasts, and automatic archiving and organization.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.7"
services:
  audiobookshelf:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/advplyr/audiobookshelf:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}/audiobooks:/audiobooks
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/metadata:/metadata
      - ${DATA_DIR}:/podcasts
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # Customize the project storage path, for example ./audiobookshelf
DATA_DIR=xxx # Customize the podcast storage path, for example ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not already in use
```

If you have a NAS, you can also mount the storage space on the NAS through the NFS protocol to save server space for storing podcasts. For details, please refer to [Mounting Synology NAS Hard Disk Expansion Space (NFS) under Linux](https://wiki-power.com/en/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

Mobile App: There is an official app for both iOS and Android that can be used directly.

## References and Acknowledgments

- [Official Website](https://www.audiobookshelf.org/)
- [Documentation](https://www.audiobookshelf.org/docs#docker-compose-install)
- [GitHub repo](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
