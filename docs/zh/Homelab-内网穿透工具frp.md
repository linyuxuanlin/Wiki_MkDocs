# Homelab - 内网穿透工具 frp

![](https://media.wiki-power.com/img/20230304195137.png)

**frp** 是一种内网穿透的方法。你可以通过有公网 IP 的服务器，将内网主机端口暴露到互联网。frp 支持 TCP、UDP、HTTP、HTTPS 等多种协议多种协议。

## 服务端 frps 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  frps:
    container_name: ${STACK_NAME}_app
    image: fatedier/frps:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frps.toml:/etc/frp/frps.toml
    command: "-c /etc/frp/frps.toml"
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `frps`）。

```dotenv title=".env"
STACK_NAME=frps
STACK_DIR=/DATA/AppData/frps # 自定义项目储存路径，例如 ./frps

# frps
APP_VERSION=v0.56.0
```

在你的项目储存路径 `${STACK_DIR}` 中添加配置文件 `frps.ini`：

```toml title="frpc.toml"
bindAddr = "0.0.0.0"
bindPort = 7000 # 服务器开放的 frp 端口，需要与之后 frpc 的设置保持一致

kcpBindPort = 7000

transport.maxPoolCount = 5

webServer.addr = "0.0.0.0" # 面板的地址，如果要外网访问必须是 0.0.0.0
webServer.port = 7500 # frps 面板的端口
webServer.user = "xxxxxx" # 面板的用户名
webServer.password = "xxxxxx" # 密码

auth.method = "token"
auth.token = "xxxxxx" # 自定义 token，需要与 frpc 的保持一致

allowPorts = [
  { start = 2000, end = 3000 },
  { single = 3001 },
  { single = 3003 },
  { start = 4000, end = 50000 }
]
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

如果你不用 docker 的方法，也可以参考这篇文章：[**服务端配置·如何实现外网 RDP 远控（frp）**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2)。

## 客户端 frpc 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  frpc:
    container_name: ${STACK_NAME}_app
    image: fatedier/frpc:${APP_VERSION}
    network_mode: host
    volumes:
      - ${STACK_DIR}/frpc.toml:/etc/frp/frpc.toml
    command: "-c /etc/frp/frpc.toml"
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `frpc`）。

```dotenv title=".env"
STACK_NAME=frpc
STACK_DIR=/DATA/AppData/frpc # 自定义项目储存路径，例如 ./frpc

# frpc
APP_VERSION=v0.56.0
```

在你的项目储存路径 `${STACK_DIR}` 中添加配置文件 `frps.toml`：

```toml title="frpc.toml"
user = "client-device-1" # 当前设备名

serverAddr = xx.xx.xx.xx # 服务器的公网 IP
serverPort = 7000 # 服务器开放的 frp 端口，需要与 frps 的设置保持一致

auth.method = "token"
auth.token = "xxxxxx" # 需要与 frps 的设置保持一致

transport.poolCount = 5

[[proxies]]
name = "app-name" # 应用名称
type = "tcp"
remotePort = xx # 公网访问的端口号
localIP = "127.0.0.1"
localPort = xx # 内网的端口号
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

请务必确保 toml 文件的格式正确，否则无法正常启动服务。可以用 Toml 在线编辑校验器检查。

## 参考与致谢

- [GitHub repo · fatedier/frp](https://github.com/fatedier/frp)
- [GitHub repo · snowdreamtech/frps](https://github.com/snowdreamtech/frp)
- [GitHub repo · stilleshan/frpc
  ](https://github.com/stilleshan/frpc)
- [Docker Hub · snowdreamtech/frps](https://hub.docker.com/r/snowdreamtech/frps)
- [Docker Hub · stilleshan/frpc](https://hub.docker.com/r/stilleshan/frpc)
- [如何实现外网 RDP 远控（frp）](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89/)
- [使用 frp 访问群晖 NAS](https://wiki-power.com/%E4%BD%BF%E7%94%A8frp%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96NAS/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
