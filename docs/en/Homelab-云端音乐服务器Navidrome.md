# Homelab - Cloud Music Server Navidrome

![](https://img.wiki-power.com/d/wiki-media/img/20230531212854.png)

**Navidrome** is an open-source web-based music server and streaming platform where you can store your own music and listen to it on multiple clients.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # If there are permission issues, try deploying as root (0:0)
    ports:
      - "${APP_PORT}:4533"
    environment:
      # Optional: put your config options customization here. Examples:
      ND_SCANSCHEDULE: 24h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
    volumes:
      - ${STACK_DIR}:/data
      - ${DATA_DIR}:/music:ro
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (e.g. replace `${STACK_NAME}` with `navidrome`).

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # Custom project storage path, such as ./navidrome
DATA_DIR=xxx # Custom podcast storage path, such as ./music

# navidrome
APP_VERSION=latest
APP_PORT=xxxx # Custom access port, choose one that is not occupied
```

If you have a NAS, you can also mount the storage space on the NAS through the NFS protocol, store the music on the NAS to save server space, please refer to [**Mount Synology NAS hard disk expansion space (NFS) under Linux**](https://wiki-power.com/en/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/) for details.

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration

There are many choices for mobile apps. The best experience I have used on Android is substreamer. For more apps, please refer to the official list [**Apps **](https://www.navidrome.org/docs/overview/#apps).

## Reference and Acknowledgement

- [Official website](https://www.navidrome.org/)
- [Documentation](https://www.navidrome.org/docs/installation/docker/)
- [GitHub repo](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [Demo site](https://demo.navidrome.org/app/) (username and password are both demo)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
