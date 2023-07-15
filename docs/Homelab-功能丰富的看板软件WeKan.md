---
id: Homelab-功能丰富的看板软件WeKan
title: Homelab - 功能丰富的看板软件 WeKan
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230508175842.png)

**WeKan** 是一款灵活、易用且高效的开源看板软件，它可以帮助团队协作管理任务、项目和工作流程。它提供了一个简单而强大的用户界面，用户可以轻松创建多个看板，为每个看板添加列表和卡片，并将任务分配给不同的成员，从而更好地管理项目并跟踪进度。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

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

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `wekan`）。

```dotenv title=".env"
STACK_NAME=wekan
STACK_DIR=xxx # 自定义项目储存路径，例如 ./wekan

# wekandb
DB_VERSION=6

# wekan
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

接着我们初始化目录结构。切换到我们自定义的 `STACK_DIR` 下（例如 `./wekan`），执行命令创建文件夹：

```shell
mkdir -vp {wekan-files,wekan-db,wekan-db-dump}
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

上文的 `compose.yaml` 经过了简化与修改，如需查看完整版本请参考 [**wekan/compose.yaml**](https://github.com/wekan/wekan/blob/master/compose.yaml)。

部署完成后，首次注册的账户为管理员账户。如果是自己使用，建议在设置面板中关闭用户注册功能。

## 参考与致谢

- [官网](https://wekan.github.io/)
- [文档](https://github.com/wekan/wekan/wiki/Docker#note-docker-composeyml-works)
- [GitHub repo](https://github.com/wekan/wekan)
- [Docker Hub](https://hub.docker.com/r/wekanteam/wekan)
- [Demo site](https://boards.wekan.team/b/D2SzJKZDS4Z48yeQH/wekan-open-source-kanban-board-with-mit-license)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
