# Homelab - Minimalist Personal Bookmark Navigation Site Flare

![Flare](https://media.wiki-power.com/img/20230410170939.png)

**Flare** is a lightweight, fast, and visually appealing personal navigation page. It doesn't rely on any databases, and its application data is completely open and transparent. It supports online editing and comes with over 6,000 Material Design Icons.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

```yaml title="compose.yaml"
version: "3.6"

services:
  flare:
    container_name: ${STACK_NAME}_app
    image: soulteary/flare:${APP_VERSION}
    # For more startup parameters, please refer to the documentation at https://github.com/soulteary/docker-flare/blob/main/docs/advanced-startup.md
    ports:
      - ${APP_PORT}:5005
    volumes:
      - ${STACK_DIR}:/app
    command: flare --nologin=0 # Enable user login mode, make sure to set the `nologin` startup parameter to `0` first
    environment:
      - FLARE_USER= ${APP_USER} # If user login mode is enabled and FLARE_USER is not set, the default user is `flare`
      - FLARE_PASS= ${APP_PASS} # If user login mode is enabled and FLARE_USER is not set, a default password will be generated and displayed in the application startup logs
    restart: always
```

(Optional) It's recommended to create a `.env` file at the same directory level as `compose.yaml` to customize your environment variables. If you don't want to use environment variables, you can also customize your parameters directly within `compose.yaml` (e.g., replace `${STACK_NAME}` with `flare`).

```dotenv title=".env"
STACK_NAME=flare
STACK_DIR=xxx # Customize your project storage path, e.g., ./flare

# flare
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port; choose an unoccupied one
APP_USER=xxxx # Customize the username
APP_PASS=xxxx # Customize the password
```

Finally, in the same directory as `compose.yaml`, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Instructions

You can modify the addresses of applications and bookmarks in `${DIR}/flare` by editing `apps.yml` and `bookmarks.yml`. The container will update in real-time. You can also debug by adding the following parameters to the URL:

- Getting Started: `/guide`
- Settings Page: `/settings`
- Online Editing: `/editor`
- Icon Retrieval: `/icons`
- Help Page: `/help`

## References and Acknowledgments

- [Official Website](https://soulteary.com/2022/02/23/building-a-personal-bookmark-navigation-app-from-scratch-flare.html)
- [Documentation / GitHub Repository](https://github.com/soulteary/docker-flare)
- [Docker Hub](https://hub.docker.com/r/soulteary/flare/)

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
