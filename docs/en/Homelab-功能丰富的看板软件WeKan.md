# Homelab - Feature-Rich Kanban Software WeKan

![](https://media.wiki-power.com/img/20230508175842.png)

**WeKan** is a flexible, user-friendly, and highly efficient open-source Kanban software that facilitates team collaboration in managing tasks, projects, and workflows. It offers a simple yet powerful user interface, enabling users to effortlessly create multiple boards, add lists and cards to each board, and assign tasks to different team members, thereby enhancing project management and progress tracking.

## Deployment (Docker Compose)

To begin with, create a `compose.yaml` file and paste the following contents:

```yaml title="compose.yaml"
version: "2"
services:
  wekandb:
    container_name: ${STACK_NAME}_db
    image: mongo:${DB_VERSION}
    command: mongod --logpath /dev/null --oplogSize 128 --quiet
    networks:
      - wekan-tier
    expose:
      - 27017
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - /etc/timezone:/etc/timezone:ro
      - wekan-db:/data/db
      - wekan-db-dump:/dump
    restart: no
  wekan:
    container_name: ${STACK_NAME}_app
    image: quay.io/wekan/wekan:${APP_VERSION}
    user: 0:0
    networks:
      - wekan-tier
    ports:
      - ${APP_PORT}:8080
    environment:
      - WRITABLE_PATH=/data
      - MONGO_URL=mongodb://wekandb:27017/wekan
      - ROOT_URL=http://localhost
      - MAIL_URL=smtp://<mail_url>:25/?ignoreTLS=true&tls={rejectUnauthorized:false}
      - MAIL_FROM=Wekan Notifications <noreply.wekan@mydomain.com>
      - WITH_API=true
      - RICHER_CARD_COMMENT_EDITOR=false
      - CARD_OPENED_WEBHOOK_ENABLED=false
    depends_on:
      - wekandb
    volumes:
      - /etc/localtime:/etc/localtime:ro
      - wekan-files:/data:rw
    restart: no
volumes:
  wekan-files:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-files
      o: bind
  wekan-db:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-db
      o: bind
  wekan-db-dump:
    driver: local
    driver_opts:
      type: none
      device: ${STACK_DIR}/wekan-db-dump
      o: bind
networks:
  wekan-tier:
    driver: bridge
```

Note: The provided Docker Compose configuration is tailored for deploying WeKan.

(Optional) It is recommended to create a `.env` file in the same directory as your `compose.yaml` and customize your environment variables. If you prefer not to use environment variables, you can also directly customize your parameters within the `compose.yaml` (e.g., replace `${STACK_NAME}` with `wekan`).

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # Customize your project storage path, e.g., ./wekan

# wekandb
DB_VERSION=6

# wekan
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, ensuring it is not already in use
```

Next, let's initialize the directory structure. Change to the custom `STACK_DIR` you've specified (e.g., `./wekan`) and execute the following command to create the necessary folders:

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
```

Finally, in the directory where your `compose.yaml` is located, execute the `docker compose up -d` command to start the orchestrated containers.

## Configuration Details

The `compose.yaml` mentioned above has been simplified and modified. For the complete version, please refer to [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml).

After deployment, the first registered account will be the administrator account. If you are using it for personal use, it's advisable to disable user registration in the settings panel.

## References and Acknowledgments

- [Official Website](https://wekan.github.io/)
- [Documentation](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [GitHub Repository](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [Demo Site](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

> Original: <https://wiki-power.com/>
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.
