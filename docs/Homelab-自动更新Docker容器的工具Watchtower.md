---
id: Homelab-自动更新Docker容器的工具Watchtower
title: Homelab - 自动更新 Docker 容器的工具 Watchtower
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304092337531.png)

**Watchtower** 是一个自动化更新全部或选定 Docker 容器的工具。

## 部署（docker-compose）

```yml title="docker-compose.yml"
version: "3"
services:
  watchtower:
    image: containrrr/watchtower
    volumes:
      - /var/run/docker.sock:/var/run/docker.sock
```

## 参考与致谢

- [官网 / 文档](https://containrrr.dev/watchtower)
- [GitHub repo](https://github.com/containrrr/watchtower/)
- [Docker Hub](https://hub.docker.com/r/containrrr/watchtower)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
