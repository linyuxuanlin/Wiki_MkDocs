# Homelab - Feature-rich Kanban software WeKan

![](https://f004.backblazeb2.com/file/wiki-media/img/20230508175842.png)

**WeKan** is a flexible, easy-to-use, and efficient open-source Kanban software that helps teams collaborate and manage tasks, projects, and workflows. It provides a simple yet powerful user interface where users can easily create multiple boards, add lists and cards to each board, and assign tasks to different members to better manage projects and track progress.

## Deployment (Docker Compose)

First, create a `compose.yaml` file and paste the following content:

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


(Optional) It is recommended to create a `.env` file in the same directory as `compose.yaml` and customize your environment variables. If you do not want to use environment variables, you can also customize your parameters directly in `compose.yaml` (such as replacing `${STACK_NAME}` with `wekan`).

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # Customize the project storage path, for example, ./wekan

# wekandb
DB_VERSION=6

# wekan
APP_VERSION=latest
APP_PORT=xxxx # Customize the access port, choose one that is not occupied
```

Next, we initialize the directory structure. Switch to our custom `STACK_DIR` (such as `./wekan`) and execute the following command to create folders:

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
```

Finally, execute the `docker compose up -d` command in the same directory as `compose.yaml` to start the orchestrated containers.

## Configuration Instructions

The `compose.yaml` in the previous section has been simplified and modified. If you need to view the full version, please refer to [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml).

After deployment, the first registered account will be the administrator account. If you are using it for yourself, it is recommended to disable user registration in the settings panel.

## References and Acknowledgments

- [Official website](https://wekan.github.io/)
- [Documentation](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [GitHub repo](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [Demo site](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

> Original: <https://wiki-power.com/>  
> This post is protected by [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.en) agreement, should be reproduced with attribution.

> This post is translated using ChatGPT, please [**feedback**](https://github.com/linyuxuanlin/Wiki_MkDocs/issues/new) if any omissions.