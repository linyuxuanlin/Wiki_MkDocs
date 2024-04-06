# Homelab - Tool for Automatically Updating Docker Containers: Watchtower

![Watchtower](https://media.wiki-power.com/img/202304092337531.png)

**Watchtower** is a tool for automating the updates of all or selected Docker containers.

## Deployment (Docker Compose)

To begin, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3"
services:
  watchtower:
    container_name: ${STACK_NAME}_app
    image: containrrr/watchtower:${APP_VERSION}
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
    restart: always
```

(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can directly customize your parameters within `compose.yaml` (for example, replacing `${STACK_NAME}` with `watchtower`).

```dotenv title=".env"
STACK_NAME=watchtower

# watchtower
APP_VERSION=latest
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## References and Acknowledgments

- [Official Website / Documentation](https://containrrr.dev/watchtower)
- [GitHub Repository](https://github.com/containrrr/watchtower/)
- [Docker Hub](https://hub.docker.com/r/containrrr/watchtower)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
