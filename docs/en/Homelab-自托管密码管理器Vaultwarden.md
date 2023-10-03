# Homelab - Self-Hosted Password Manager Vaultwarden

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195414.jpg)

**Vaultwarden** is a third-party self-hosted Bitwarden server that protects and manages passwords for various websites with a master password, and can generate random passwords for different websites.

## Deployment (Docker Compose)

First, create the `compose.yaml` file and paste the following content:

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

(Optional) It is recommended to create a `.env` file at the same level as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # Customize the project storage path, such as ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated container.

## Configuration Instructions

Vaultwarden requires https login by default, and it is recommended to use a reverse proxy (the setup of a reverse proxy server can refer to the article [Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager](https://wiki-power.com/en/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/)).

When using browser extensions, desktop and mobile apps, you need to click on settings on the login page and configure the server URL to use the self-hosted service normally.

In addition, old versions (less than 1.27.0) of Vaultwarden and Bitwarden browser extensions are not compatible and will cause login failure. See issue: [Client fails to connect or login](https://github.com/dani-garcia/vaultwarden/issues/3082).

Because it is a self-hosted service, you need to pay attention to data security and remember to back up the password database regularly.

## References and Acknowledgments

- [Official website](https://github.com/dani-garcia/vaultwarden/wiki)
- [Documentation](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [GitHub repo](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.