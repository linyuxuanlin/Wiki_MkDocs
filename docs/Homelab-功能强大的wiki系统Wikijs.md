---
id: Homelab-功能强大的wiki系统Wikijs
title: Homelab - 功能强大的 wiki 系统 Wiki.js
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195348.png)

**Wiki.js** 是一个带后台编辑器和管理页面的 wiki 文档工具，包括多用户权限管理、Markdown、多种同步与储存方式（比如 git 同步）等功能。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  wikijs:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/requarks/wiki:${APP_VERSION}
    depends_on:
      - db
    environment:
      DB_TYPE: ${APP_DB_TYPE}
      DB_HOST: ${APP_DB_HOST}
      DB_PORT: ${APP_DB_PORT}
      DB_USER: ${APP_DB_USER}
      DB_PASS: ${APP_DB_PASS}
      DB_NAME: ${APP_DB_NAME}
    restart: unless-stopped
    ports:
      - "${APP_PORT}:3000"
  db:
    container_name: ${STACK_NAME}_db
    image: postgres:${DB_VERSION}
    environment:
      POSTGRES_DB: ${DB_POSTGRES_DB}
      POSTGRES_PASSWORD: ${DB_POSTGRES_PASSWORD}
      POSTGRES_USER: ${DB_POSTGRES_USER}
    logging:
      driver: "none"
    volumes:
      - ${STACK_DIR}/postgres/db-data:/var/lib/postgresql/data
    restart: unless-stopped
volumes:
  db-data:
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `wikijs`）。

```dotenv title=".env"
STACK_NAME=wikijs
STACK_DIR=xxx # 自定义项目储存路径，例如 ./wikijs

# wikijs
APP_VERSION=2
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可 
APP_DB_TYPE=postgres
APP_DB_HOST=db
APP_DB_PORT=5432 # 默认数据库的内部端口
APP_DB_USER=xxx # 数据库用户名
APP_DB_PASS=xxx # 数据库密码
APP_DB_NAME=wikijs # 数据库名称

# db
DB_VERSION=10-alpine
DB_POSTGRES_DB=wikijs # 数据库名称，与上方保持相同
DB_POSTGRES_PASSWORD=xxx # 数据库密码，与上方保持相同
DB_POSTGRES_USER=xxx # 数据库用户名，与上方保持相同
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

配置 git 仓库同步的详细教程：<https://docs.requarks.io/storage/git>

## 参考与致谢

- [官网](https://js.wiki)
- [文档](https://docs.requarks.io/install/docker)
- [GitHub repo](https://github.com/requarks/wiki)
- [Docker Hub](https://hub.docker.com/r/requarks/wiki)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
