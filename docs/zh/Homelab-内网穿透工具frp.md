---
id: Homelab-内网穿透工具frp
title: Homelab - 内网穿透工具 frp
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195137.png)

**frp** 是一种内网穿透的方法。你可以通过有公网 IP 的服务器，将内网主机端口暴露到互联网。frp 支持 TCP、UDP、HTTP、HTTPS 等多种协议多种协议。

## 服务端 frps 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  frps:
    container_name: ${STACK_NAME}_app
    image: snowdreamtech/frps:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frps.ini:/etc/frp/frps.ini
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `frps`）。

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=xxx # 自定义项目储存路径，例如 ./frps

# frps
APP_VERSION=latest
```

在你的项目储存路径 `${STACK_DIR}` 中添加配置文件 `frps.ini`：

```ini title="frps.ini"
[common]
bind_port = 7000 # 客户端和服务端连接的端口，在之后配置客户端时会用上。
dashboard_port = 7500 # 服务端 dashboard 的端口
token = ${TOKEN-FRPS} # 客户端和服务端连接的口令，请自行设置。
dashboard_user = ${USERNAME-FRPS} # 用户名
dashboard_pwd = ${PASSWORD-FRPS} # 密码
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

如果你不用 docker 的方法，也可以参考这篇文章：[**服务端配置·如何实现外网 RDP 远控（frp）**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2)。

## 客户端 frpc 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.3"
services:
  frpc:
    container_name: ${STACK_NAME}_app
    image: stilleshan/frpc:${APP_VERSION}
    network_mode: "host"
    volumes:
      - ${STACK_DIR}/frpc.ini:/frp/frpc.ini
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `replace`）。

```dotenv title=".env"
STACK_NAME=replace
STACK_DIR=xxx # 自定义项目储存路径，例如 ./replace

# replace
APP_VERSION=latest
```

在你的项目储存路径 `${STACK_DIR}` 中添加配置文件 `frps.ini`：

```ini title="frpc.ini"
[common]
server_addr = xx.xx.xx.xx # 服务器的公网 IP
server_port = 7000 # 与服务端的端口保持一致
tls_enable = true
token = ${TOKEN-FRPS} # 与服务端的 token 保持一致

[xxx]
type = tcp
remote_port = xx # 公网访问的端口号
local_ip = localhost
local_port = xx # 内网的端口号
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 参考与致谢

- [GitHub repo · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [GitHub repo · stilleshan/frpc
  ](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [如何实现外网 RDP 远控（frp）](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [使用 frp 访问群晖 NAS](https://wiki-power.com/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
