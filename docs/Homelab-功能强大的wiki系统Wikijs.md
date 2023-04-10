---
id: Homelab-功能强大的wiki系统Wikijs
title: Homelab - 功能强大的 wiki 系统 Wiki.js 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195348.png)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: "3"
services:

  db:
    image: postgres:10-alpine # 必须用这个版本
    environment:
      POSTGRES_DB: wikijs
      POSTGRES_PASSWORD: [custom-password-db]
      POSTGRES_USER: [custom-username-db]
    logging:
      driver: "none"
    restart: unless-stopped
    volumes:
      - [custom-dir]/wikijs/postgres/db-data:/var/lib/postgresql/data

  wiki:
    image: ghcr.io/requarks/wiki:2
    depends_on:
      - db
    environment:
      DB_TYPE: postgres
      DB_HOST: db
      DB_PORT: 5432
      DB_USER: [custom-username-db]
      DB_PASS: [custom-password-db]
      DB_NAME: wikijs
    restart: unless-stopped
    ports:
      - "[custom-port]:3000"

volumes:
  db-data:
```

## 配置说明

## 参考与致谢

- [官网](https://js.wiki)
- [文档](https://docs.requarks.io/install/docker)
- [GitHub repo](https://github.com/requarks/wiki)
- [Docker Hub](https://hub.docker.com/r/requarks/wiki)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
