# Homelab - Reverse Proxy Certificate Management Panel Nginx Proxy Manager

![](https://f004.backblazeb2.com/file/wiki-media/img/20230408182138.png)

**Nginx Proxy Manager** is a graphical panel for Nginx that allows users to easily configure reverse proxies and apply SSL certificates to websites through a web interface, without needing to understand the underlying principles of Nginx/Letsencrypt.

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

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `nginx-proxy-manager`).

```dotenv title=".env"
STACK_NAME=nginx-proxy-manager
STACK_DIR=xxx # Custom project storage path, such as ./nginx-proxy-manager

# nginx-proxy-manager
APP_VERSION=latest
APP_PORT=81 # Default is 81, refer to documentation for changes
```

Finally, execute the command `docker compose up -d` in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

Initial account credentials:

- Email: `admin@example.com`
- Password: `changeme`

To obtain the IP address of Docker:

```shell
ip addr show docker0
```

Note: For self-hosted services, it is recommended to use reverse proxy and bind to a second-level domain for access (port 80/443), and close other ports in the firewall of the public server management console to improve security.

## References and Acknowledgements

- [Official Website](https://nginxproxymanager.com)
- [Documentation](https://nginxproxymanager.com/guide)
- [GitHub repo](https://github.com/NginxProxyManager/nginx-proxy-manager)
- [Docker Hub](https://hub.docker.com/r/jlesage/nginx-proxy-manager)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.