# Homelab - Smart Home Server with Home Assistant

![Home Assistant](https://img.wiki-power.com/d/wiki-media/img/202306011647498.png)

**Home Assistant** is an open-source smart home server that allows you to monitor all your home devices. It functions similarly to Mi Home, with a user-friendly and aesthetically pleasing interface, making deployment relatively straightforward.

## Deployment (Docker Compose)

Start by creating a `compose.yaml` file and paste the following contents:

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

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly define your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # Customize your project storage path, e.g., ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # Choose an available access port of your choice
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the container orchestration.

## Configuration Notes

For mobile access, you can use the official Home Assistant App.

## References and Acknowledgments

- [Official Website](https://www.home-assistant.io/)
- [Documentation](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [GitHub Repository](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Demo Site](https://demo.home-assistant.io/#/lovelace/0)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.