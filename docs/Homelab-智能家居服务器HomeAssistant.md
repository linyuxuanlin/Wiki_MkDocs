---
id: Homelab-智能家居服务器HomeAssistant
title: Homelab - 智能家居服务器 Home Assistant
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202306011647498.png)

**Home Assistant** 是一个开源的智能家居服务器，能够监控家里的所有设备，功能类似米家，界面友好美观，部署也相对简单。

## 部署（docker-compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  homeassistant:
    container_name: ${STACK_NAME}_app
    image: ghcr.io/home-assistant/home-assistant:${APP_VERSION}
    ports:
      - ${APP_PORT}:8123
    volumes:
      - ${STACK_DIR}:/config
      - /etc/localtime:/etc/localtime:ro
    privileged: true
    #network_mode: host
    restart: unless-stopped
```

接下来，在与 `compose.yaml` 相同的目录下创建 `.env` 文件，并自定义你的环境变量（推荐）。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 自定义你的参数（比如把 `${STACK_NAME}` 替换为 `audiobookshelf`）。

```dotenv title=".env"
STACK_NAME=homeassistant
STACK_DIR=xxx # 自定义项目储存路径，例如 ./homeassistant

# homeassistant
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

如果你有个 NAS，也可以通过 NFS 协议挂载 NAS 上的储存空间，把音乐储存在 NAS 上以节省服务器空间，详情请参考 [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/)。

最后，在 `compose.yaml` 目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

移动端 App 可直接使用官方的 Home Assistant App

## 参考与致谢

- [官网](https://www.home-assistant.io/)
- [文档](https://www.home-assistant.io/installation/generic-x86-64#docker-compose)
- [GitHub repo](https://github.com/home-assistant)
- [Docker Hub](https://hub.docker.com/r/homeassistant/home-assistant)
- [Demo site](https://demo.home-assistant.io/#/lovelace/0)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
