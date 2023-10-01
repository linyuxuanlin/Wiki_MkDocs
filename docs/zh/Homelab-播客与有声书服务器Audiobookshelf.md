---
id: Homelab-播客与有声书服务器Audiobookshelf
title: Homelab - 播客与有声书服务器 Audiobookshelf
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230531204505.png)

**Audiobookshelf** 是一款自托管的播客与有声书服务器，可以方便地搜索播客、自动检测更新并下载播客、自动归档整理。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.7"
services:
  audiobookshelf:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/advplyr/audiobookshelf:${APP_VERSION}
    ports:
      - ${APP_PORT}:80
    volumes:
      - ${STACK_DIR}/audiobooks:/audiobooks
      - ${STACK_DIR}/config:/config
      - ${STACK_DIR}/metadata:/metadata
      - ${DATA_DIR}:/podcasts
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `audiobookshelf`）。

```dotenv title=".env"
STACK_NAME=audiobookshelf
STACK_DIR=xxx # 自定义项目储存路径，例如 ./audiobookshelf
DATA_DIR=xxx # 自定义播客储存路径，例如 ./podcast

# audiobookshelf
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

如果你有个 NAS，也可以通过 NFS 协议挂载 NAS 上的储存空间，把播客储存在 NAS 上以节省服务器空间，详情请参考 [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/)。

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

移动端 App：在 iOS 与 Android 端都有官方的 App，可直接使用。

## 参考与致谢

- [官网](https://www.audiobookshelf.org/)
- [文档](https://www.audiobookshelf.org/docs#docker-compose-install)
- [GitHub repo](https://github.com/advplyr/audiobookshelf)
- [Docker Hub](https://hub.docker.com/r/advplyr/audiobookshelf)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
