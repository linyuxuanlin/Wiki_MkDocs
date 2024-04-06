# Homelab - 开源的远程桌面方案 RustDesk

![](https://media.wiki-power.com/img/20230531212854.png)

**RustDesk** 是一套开源的远程桌面方案，在内网可直接使用各平台的客户端进行远程，本文章主要讲解公网下如何搭建自己的服务器。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"

networks:
  rustdesk-net:
    external: false

services:
  hbbs:
    container_name: ${STACK_NAME}_hbbs
    ports:
      - 21115:21115
      - 21116:21116
      - 21116:21116/udp
      - 21118:21118
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbs -r ${STACK_DOMAIN}:21117 -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    depends_on:
      - hbbr
    restart: unless-stopped

  hbbr:
    container_name: ${STACK_NAME}_hbbr
    ports:
      - 21117:21117
      - 21119:21119
    image: rustdesk/rustdesk-server:${APP_VERSION}
    command: hbbr -k _
    volumes:
      - ${STACK_DIR}/data:/root
    networks:
      - rustdesk-net
    restart: unless-stopped
```

在这个 docker compose 中，编排了两个服务：

- hbbs: RustDesk ID 注册服务器
- hbbr: RustDesk 中继服务器

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `rustdesk-server`）。

```dotenv title=".env"
STACK_NAME=rustdesk-server
STACK_DIR=xxx # 自定义项目储存路径，例如 ./rustdesk-server
STACK_DOMAIN=xxx # 部署 RustDesk 服务器的域名或 IP

# rustdesk-server
APP_VERSION=latest
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

如果遇到错误 `Registered email required (-m option). Please pay and register on https://rustdesk.com/server...`，说明可能下载的不是最新版本的包，解决方法如下：

1. 在 <https://hub.docker.com/r/rustdesk/rustdesk-server/tags> 上找到最新版本的 DIGEST 编号（比如 `83e259792b50`）。
2. 在本地使用命令 `docker image pull rustdesk/rustdesk-server:latest@sha256:83e259792b50` 下载最新的包，注意把最后的字符替换为你自己的。

## 参考与致谢

- [官网](https://rustdesk.com/)
- [文档](https://rustdesk.com/docs/en/self-host/)
- [GitHub repo](https://github.com/rustdesk/rustdesk)
- [Docker Hub](https://hub.docker.com/r/rustdesk/rustdesk-server)
- [使用 docker 自建 rustdesk 服务器](https://developer.aliyun.com/article/1299504)
- [self-host](https://rustdesk.com/docs/zh-cn/self-host/rustdesk-server-oss/install/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
