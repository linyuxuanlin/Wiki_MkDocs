# Homelab - Podcast and Audiobook Server: Audiobookshelf

![Audiobookshelf](https://media.wiki-power.com/img/20230531204505.png)

**Audiobookshelf** is a self-hosted server for podcasts and audiobooks, designed to make podcast searching, automatic update detection, and downloading, as well as seamless organization, a breeze.

## Deployment (Docker Compose)

To get started, create a `compose.yaml` file and paste the following content:

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

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # Customize your project storage path, e.g., ./audiobookshelf
DATA_DIR=xxx # Customize your podcast storage path, e.g., ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, ensuring it's not already in use
```

If you have a NAS (Network Attached Storage), you can also mount storage space from your NAS using the NFS protocol. This allows you to store your podcasts on the NAS to save server space. For details, refer to [**Mounting Synology NAS Hard Drive for Space Expansion on Linux (NFS)**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/).

Finally, in the directory where `compose.yaml` is located, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Notes

Mobile App: There are official apps available for both iOS and Android platforms, making it easy to access and use.

## References and Acknowledgments

- [Official Website](https://www.audiobookshelf.org/)
- [Documentation](https://www.audiobookshelf.org/docs#docker-compose-install)
- [GitHub Repository](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
