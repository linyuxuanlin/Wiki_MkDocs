---
id: Homelab-内网穿透工具frp
title: Homelab - 内网穿透工具 frp
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195137.png)

**frp** 是一种内网穿透的方法。你可以通过有公网 IP 的服务器，将内网主机端口暴露到互联网。frp 支持 TCP、UDP、HTTP、HTTPS 等多种协议多种协议。

## 服务端 frps

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）：

```yml title="docker-compose.yml"
version: "3"
services:
  frps:
    image: "snowdreamtech/frps:latest"
    restart: always
    network_mode: host
    volumes:
      - ${DIR}/frps/frps.ini:/etc/frp/frps.ini
```

并添加配置文件 `frps.ini`：

```ini title="frps.ini"
[common]
bind_port = 7000 # 客户端和服务端连接的端口，在之后配置客户端时会用上。
dashboard_port = 7500 # 服务端 dashboard 的端口
token = ${TOKEN-FRPS} # 客户端和服务端连接的口令，请自行设置。
dashboard_user = ${USERNAME-FRPS} # 用户名
dashboard_pwd = ${PASSWORD-FRPS} # 密码
```

如果你不用 docker 的方法，也可以参考这篇文章：[**服务端配置·如何实现外网 RDP 远控（frp）**](https://wiki-power.com/%E5%A6%82%E4%BD%95%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91RDP%E8%BF%9C%E6%8E%A7%EF%BC%88frp%EF%BC%89#_2)。

## 客户端 frpc

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）：

```yml title="docker-compose.yml"
version: "3.3"
services:
  frpc:
    restart: always
    network_mode: "host"
    volumes:
      - ${DIR}/frpc/frpc.ini:/frp/frpc.ini
    image: stilleshan/frpc
```

并添加配置文件 `frpc.ini`：

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
