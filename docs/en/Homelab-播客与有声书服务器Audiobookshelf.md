# Homelab - Podcast and Audiobook Server: Audiobookshelf

![Audiobookshelf](https://img.wiki-power.com/d/wiki-media/img/20230531204505.png)

**Audiobookshelf** is a self-hosted server for podcasts and audiobooks, making it easy to search for podcasts, automatically detect updates, and download podcasts while organizing them efficiently.

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

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can also directly customize your parameters within `compose.yaml` (for example, replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # Customize your project storage path, e.g., ./audiobookshelf
DATA_DIR=xxx # Customize your podcast storage path, e.g., ./podcast

# Audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose an available one
```

If you have a NAS, you can also mount storage space on your NAS via the NFS protocol to save server space. For more details, please refer to [**Expanding Space by Mounting Synology NAS Hard Drives Under Linux (NFS)**](https://wiki-power.com/en/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9A%84%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finally, in the same directory as `compose.yaml`, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Notes

Mobile App: Official apps are available for both iOS and Android, which can be used directly.

## References and Acknowledgments

- [Official Website](https://www.audiobookshelf.org/)
- [Documentation](https://www.audiobookshelf.org/docs#docker-compose-install)
- [GitHub Repository](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.