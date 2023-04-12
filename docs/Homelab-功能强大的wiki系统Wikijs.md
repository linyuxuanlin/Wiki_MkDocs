---
id: Homelab-功能强大的wiki系统Wikijs
title: Homelab - 功能强大的 wiki 系统 Wiki.js
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195348.png)

**Wiki.js** 是一个带后台编辑器和管理页面的 wiki 文档工具，包括多用户权限管理、Markdown、多种同步与储存方式（比如 git 同步）等功能。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）；自定义 `${USERNAME-DB}` 与 `${PASSWORD-DB}`：

```yml title="docker-compose.yml"
version: "3"
services:
  db:
    image: postgres:10-alpine # 此版本经测试可正常安装
    environment:
      POSTGRES_DB: wikijs
      POSTGRES_PASSWORD: ${PASSWORD-DB}
      POSTGRES_USER: ${USERNAME-DB}
    logging:
      driver: "none"
    restart: unless-stopped
    volumes:
      - ${DIR}/wikijs/postgres/db-data:/var/lib/postgresql/data

  wiki:
    image: ghcr.io/requarks/wiki:2
    depends_on:
      - db
    environment:
      DB_TYPE: postgres
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: ${USERNAME-DB}
      DB_PASS: ${PASSWORD-DB}
      DB_NAME: wikijs
    restart: unless-stopped
    ports:
      - "${PORT}:3000"

volumes:
  db-data:
```

## 配置说明

配置 git 仓库同步的详细教程：<https://docs.requarks.io/storage/git>

## 参考与致谢

- [官网](https://js.wiki)
- [文档](https://docs.requarks.io/install/docker)
- [GitHub repo](https://github.com/requarks/wiki)
- [Docker Hub](https://hub.docker.com/r/requarks/wiki)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
