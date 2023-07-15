---
id: Homelab-跨设备同步工具Syncthing
title: Homelab - 跨设备同步工具 Syncthing
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304111529987.png)

**Syncthing** 是一款免费开源的文件同步应用程序，可在多个设备间同步文件和文件夹，支持增量同步。我用它将服务器的数据备份到 NAS 上做统一管理。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  syncthing:
    container_name: ${STACK_NAME}_app
    image: syncthing/syncthing:${APP_VERSION}
    hostname: my-syncthing
    volumes:
      - ${APP_SYNC_DIR}:/DATA
      - ${STACK_DIR}/config:/var/syncthing/config/
    ports:
      - ${APP_PORT}:8384 # Web UI
      - 22000:22000/tcp # TCP file transfers
      - 22000:22000/udp # QUIC file transfers
      - 21027:21027/udp # Receive local discovery broadcasts
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `syncthing`）。

```dotenv title=".env"
STACK_NAME=syncthing
STACK_DIR=xxx # 自定义项目储存路径，例如 ./syncthing

# syncthing
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
APP_SYNC_DIR=xxxx # 自定义需要同步的路径，比如 /DATA
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

如果提示权限不足，可尝试将 `PUID` 与 `PGID` 值都修改为 `0`，用 root 权限启动。

## 参考与致谢

- [官网](https://syncthing.net/)
- [文档](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [论坛](https://forum.syncthing.net/)
- [GitHub repo](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
