---
id: Homelab-云端音乐服务器Navidrome
title: Homelab - 云端音乐服务器 Navidrome
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230531212854.png)

**Navidrome** 是一个开源的基于 web 的音乐服务器和流媒体，你可以储存自己的音乐，并在多个客户端上收听。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  navidrome:
    container_name: ${STACK_NAME}_app
    image: deluan/navidrome:${APP_VERSION}
    user: 1000:1000 # 如果出现权限问题，可尝试使用root（0:0）部署
    ports:
      - "${APP_PORT}:4533"
    environment:
      # Optional: put your config options customization here. Examples:
      ND_SCANSCHEDULE: 24h
      ND_LOGLEVEL: info
      ND_SESSIONTIMEOUT: 24h
      ND_BASEURL: ""
    volumes:
      - ${STACK_DIR}:/data
      - ${DATA_DIR}:/music:ro
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `navidrome`）。

```dotenv title=".env"
STACK_NAME=navidrome
STACK_DIR=xxx # 自定义项目储存路径，例如 ./navidrome
DATA_DIR=xxx # 自定义播客储存路径，例如 ./music

# navidrome
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

如果你有个 NAS，也可以通过 NFS 协议挂载 NAS 上的储存空间，把音乐储存在 NAS 上以节省服务器空间，详情请参考 [**Linux 下挂载群晖 NAS 硬盘拓展空间（NFS）**](https://wiki-power.com/Linux%E4%B8%8B%E6%8C%82%E8%BD%BD%E7%BE%A4%E6%99%96NAS%E7%A1%AC%E7%9B%98%E6%8B%93%E5%B1%95%E7%A9%BA%E9%97%B4%EF%BC%88NFS%EF%BC%89/)。

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

移动端 App 有很多种选择，Android 上我自用体验最佳的是 substreamer，更多 App 可以参考官方列表 [**Apps **](https://www.navidrome.org/docs/overview/#apps)。

## 参考与致谢

- [官网](https://www.navidrome.org/)
- [文档](https://www.navidrome.org/docs/installation/docker/)
- [GitHub repo](https://github.com/navidrome/navidrome/)
- [Docker Hub](https://hub.docker.com/r/deluan/navidrome)
- [Demo site](https://demo.navidrome.org/app/)（用户名密码均为 demo）

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
