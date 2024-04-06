# Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager

![Nginx Proxy Manager](https://media.wiki-power.com/img/20230408182138.png)

**Nginx Proxy Manager** is a graphical interface for Nginx that allows users to easily configure reverse proxies and request SSL certificates for websites through a web interface, without needing an in-depth understanding of Nginx or Letsencrypt's underlying principles.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  nginx-proxy-manager:
    container_name: ${STACK_NAME}_app
    image: "jc21/nginx-proxy-manager:${APP_VERSION}"
    ports:
      - "${APP_PORT}:81" # Panel address
      - "80:80"
      - "443:443"
    volumes:
      - ${STACK_DIR}/data:/data
      - ${STACK_DIR}/letsencrypt:/etc/letsencrypt
    restart: unless-stopped
```

(Optional) It's recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters in `compose.yaml` (for example, replace `${STACK_NAME}` with `nginx-proxy-manager`).

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # Customize your project storage path, e.g., ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # Default is 81; change as needed, referring to the documentation
```

Finally, run the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Details

Initial account credentials:

- Email: `admin@example.com`
- Password: `changeme`

To obtain the IP address of Docker, use the following command:

```shell
ip addr show docker0
```

Note: For self-hosted services, it is advisable to access them through a reverse proxy, binding to a subdomain (port 80/443), and close other ports in the public server's firewall management console to enhance security.

## References and Acknowledgments

- [Official Website](https://nginxproxymanager.com)
- [Documentation](https://nginxproxymanager.com/guide)
- [GitHub Repository](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
