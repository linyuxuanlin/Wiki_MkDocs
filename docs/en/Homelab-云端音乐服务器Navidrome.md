# Homelab - Cloud Music Server Navidrome

![](https://img.wiki-power.com/d/wiki-media/img/20230531212854.png)

**Navidrome** is an open-source web-based music server and streaming platform that allows you to store your music collection and listen to it on multiple clients.

## Deployment (Docker Compose)

To begin, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # If permission issues arise, you can try deploying as root (0:0)
    ports:
      - "${APP_PORT}:4533"
    environment:
      # Optional: customize your configuration options here. Examples:
      ND_SCANSCHEDULE: 24h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
    volumes:
      - ${STACK_DIR}:/data
      - ${DATA_DIR}:/music:ro
    restart: unless-stopped
```

(Optionally) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (e.g., replace `${STACK_NAME}` with `navidrome`).

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # Customize your project storage path, e.g., ./navidrome
DATA_DIR=xxx # Customize your music storage path, e.g., ./music

# Navidrome
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose an available one
```

If you have a NAS, you can also mount storage space on your NAS using the NFS protocol to save your music there and conserve server space. For details, please refer to [**Mounting Synology NAS Hard Drive for Space Expansion (NFS) on Linux**](to_be_replace[3]).

Finally, in the directory where `compose.yaml` is located, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Details

There are various mobile apps to choose from, and for Android, the one I personally find to offer the best experience is Substreamer. For more app options, you can refer to the official list [**Apps**](https://www.navidrome.org/docs/overview/#apps).

## References and Acknowledgments

- [Official Website](https://www.navidrome.org/)
- [Documentation](https://www.navidrome.org/docs/installation/docker/)
- [GitHub Repository](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [Demo Site](https://demo.navidrome.org/app/) (Both the username and password are "demo")

Certainly, here is the translation of the provided text into English:

```markdown
[to_be_replaced[1]]
[to_be_replaced[2]]
```

If you have any specific context or content to replace in the placeholders "[to_be_replaced[1]]" and "[to_be_replaced[2]]", please provide that information, and I'd be happy to assist further.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.