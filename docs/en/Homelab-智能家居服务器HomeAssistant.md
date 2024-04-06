# Homelab - Smart Home Server Home Assistant

![](https://media.wiki-power.com/img/202306011647498.png)

**Home Assistant** is an open-source smart home server that can monitor all devices in your home. It has similar features to the Xiaomi Mi Home app, with a friendly and beautiful interface and relatively simple deployment.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following contents:

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml`, and customize your environment variables there. If you do not want to use environment variables, you can directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `audiobookshelf`).

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # Customize the project storage path, e.g., ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, run the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

The official Home Assistant App can be used directly on mobile devices.

If you encounter a `400 Bad Request` error when accessing from the Internet, you can add the following statements to the configuration file `configuration.yaml`:

```yaml
http:
  use_x_forwarded_for: true
  trusted_proxies:
    - 10.0.0.200 # IP address of the proxy server
    - 172.30.33.0/24 # You can also provide IP addresses with subnet masks
```

If you do not know the IP address of the proxy server, you can try accessing Home Assistant from the Internet, and you will be able to see it from the error information in the log.

## References and Acknowledgments

- [Official Website](https://www.home-assistant.io/)
- [Documentation](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [GitHub repo](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Demo Site](https://demo.home-assistant.io/#/lovelace/0)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
