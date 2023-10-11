# Homelab - Smart Home Server Home Assistant

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202306011647498.png)

**Home Assistant** is an open-source smart home server that can monitor all devices in your home. Its functionality is similar to that of Mi Home, and its interface is user-friendly and visually appealing. Deployment is also relatively simple.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  homeassistant:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/home-assistant/home-assistant:${APP_VERSION}
    ports:
      - ${APP_PORT}:8123
    volumes:
      - ${STACK_DIR}:/config
      - /etc/localtime:/etc/localtime:ro
    privileged: true
    #network_mode: host
    restart: unless-stopped
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (for example, replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # Customize your project storage path, for example, ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose one that is not already in use
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

Mobile Apps can now directly use the official Home Assistant App.

## References and Acknowledgements

- [Official Website](https://www.home-assistant.io/)
- [Documentation](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [GitHub Repo](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Demo Site](https://demo.home-assistant.io/#/lovelace/0)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
