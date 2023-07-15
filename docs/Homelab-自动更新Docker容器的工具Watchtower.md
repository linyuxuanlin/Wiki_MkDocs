---
id: Homelab-自动更新Docker容器的工具Watchtower
title: Homelab - 自动更新 Docker 容器的工具 Watchtower
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304092337531.png)

**Watchtower** 是一个自动化更新全部或选定 Docker 容器的工具。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

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

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `watchtower`）。

```dotenv title=".env"
STACK_NAME=watchtower

# watchtower
APP_VERSION=latest
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 参考与致谢

- [官网 / 文档](https://containrrr.dev/watchtower)
- [GitHub repo](https://github.com/containrrr/watchtower/)
- [Docker Hub](https://hub.docker.com/r/containrrr/watchtower)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
