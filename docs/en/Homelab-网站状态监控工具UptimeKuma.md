# Homelab - Website Status Monitoring Tool: Uptime Kuma

![Uptime Kuma](https://media.wiki-power.com/img/20230410160253.jpg)

**Uptime Kuma** is a versatile network protocol-supported status monitoring tool. It can monitor real-time availability, response times, certificate expiration, and more for multiple custom websites, while also providing various notification methods.

## Deployment (Docker Compose)

Start by creating a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  uptime-kuma:
    container_name: ${STACK_NAME}_app
    image: louislam/uptime-kuma:${APP_VERSION}
    ports:
      - ${APP_PORT}:3001
    volumes:
      - ${STACK_DIR}:/app/data
    restart: always
```

(Optional) It is recommended to create a `.env` file at the same level as the `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within the `compose.yaml` (e.g., replace `${STACK_NAME}` with `uptime-kuma`).

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # Customize your project storage path, e.g., ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, ensuring it's not already in use
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Notes

Note: If you are using a reverse proxy, please enable the 'Websockets Support' feature.

## References and Acknowledgments

- [Official Website](https://uptime.kuma.pet/)
- [Documentation](https://github.com/louislam/uptime-kuma/wiki)
- [GitHub Repository](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
