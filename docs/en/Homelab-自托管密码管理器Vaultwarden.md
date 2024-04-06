# Homelab - Self-hosted Password Manager Vaultwarden

![](https://media.wiki-power.com/img/20230304195414.jpg)

**Vaultwarden** is a third-party self-hosted Bitwarden server that protects and manages passwords for various websites with a master password. It can generate random passwords for different websites.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  vaultwarden:
    container_name: ${STACK_NAME}_app
    image: vaultwarden/server:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}:/data/
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you don't want to use environment variables, you can also directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # Customize your project storage path, e.g., ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not already in use
```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

Vaultwarden requires https login by default. It is recommended to use a reverse proxy (the setup of a reverse proxy server can be found in the article [**Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager**](https://wiki-power.com/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/)).

When using browser extensions, desktop and mobile apps, you need to click on the settings on the login page and configure the server URL to use the self-hosted service properly.

In addition, older versions (prior to 1.27.0) of Vaultwarden are not compatible with Bitwarden browser extensions, which may cause login issues. See the issue: [**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082).

Since it is a self-hosted service, you need to pay attention to data security. Remember to regularly back up the password database.

## References and Acknowledgements

- [Official Website](https://github.com/dani-garcia/vaultwarden/wiki)
- [Documentation](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [GitHub repo](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
