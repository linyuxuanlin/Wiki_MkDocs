# Homelab - Self-hosted Password Manager Vaultwarden

![Vaultwarden](https://img.wiki-power.com/d/wiki-media/img/20230304195414.jpg)

**Vaultwarden** is a third-party self-hosted Bitwarden server that helps protect and manage your website passwords with a master password and generate random passwords for different websites.

## Deployment (Docker Compose)

Start by creating a `compose.yaml` file and paste the following content:

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

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters in `compose.yaml` (e.g., replace `${STACK_NAME}` with `vaultwarden`).

```dotenv title=".env"
STACK_NAME=vaultwarden
STACK_DIR=xxx # Customize your project storage path, e.g., ./vaultwarden

# vaultwarden
APP_VERSION=latest
APP_PORT=xxxx # Customize your access port, choose an unoccupied one
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the container deployment.

## Configuration Notes

Vaultwarden requires https for login by default and it's recommended to use a reverse proxy (you can refer to the article [**Homelab - Nginx Proxy Manager for Reverse Proxy and SSL Certificates**](https://wiki-power.com/en/Homelab-%E5%8F%8D%E4%BB%A3%E8%AF%81%E4%B9%A6%E7%AE%A1%E7%90%86%E9%9D%A2%E6%9D%BFNginxProxyManager/) for setting up a reverse proxy server).

When using browser extensions, desktop and mobile apps, you need to click on the settings on the login page and configure the server's URL to use the self-hosted service.

Additionally, older versions (below 1.27.0) of Vaultwarden are not compatible with Bitwarden browser extensions and can result in login issues. Refer to the issue: [**Client fails to connect or login**](https://github.com/dani-garcia/vaultwarden/issues/3082).

Since it's a self-hosted service, data security is your responsibility. Remember to regularly back up the password database.

## References and Acknowledgments

- [Official Website](https://github.com/dani-garcia/vaultwarden/wiki)
- [Documentation](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [GitHub Repository](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.