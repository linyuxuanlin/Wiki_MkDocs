---
id: Homelab-免费的内网穿透替代方案Cloudflared
title: Homelab - 免费的内网穿透替代方案 Cloudflared
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

**Cloudflared** 是一个免费的内网穿透方案，用于外网访问无公网 IP 的主机。

必需条件：

- 虽然 Cloudflared 是免费的，但需要绑定 VISA/PayPal。
- 域名 NameServer 需要指向 Cloudflare
- 需要启用 Cloudflare CDN（国内访问速度偏慢）

优点：

- 不需要公网 IP 的服务器
- 不需要防火墙、反向代理
- 不需要备案就可以使用 80 和 443 端口
- 不需要自行申请 SSL 证书
- 免费

缺点：

- 国内访问速度慢
- 相对依赖 Cloudflare 平台

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  cloudflared:
    container_name: ${STACK_NAME}_app
    image: cloudflare/cloudflared:${APP_VERSION}
    network_mode: host
    restart: unless-stopped
    command: tunnel run
    environment:
      - TUNNEL_TOKEN=${APP_TUNNEL_TOKEN}
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `cloudflared`）。

```dotenv title=".env"
STACK_NAME=cloudflared

# cloudflared
APP_VERSION=latest
APP_TUNNEL_TOKEN=xxx # 替换为你的 token
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

访问 [**Cloudflare Zero Trust**](https://one.dash.cloudflare.com/) 面板，在左侧栏选择 `Access` - `Tunnels`，点击 `Create a tunnel` 创建隧道，填写隧道名称（用于区分不同的物理机器）然后保存。记录下 token 后填写在 `compose.yaml` 中。

随后点进你创建的隧道，在 `Public Hostname Page` 选项卡中添加代理的端口。举个例子，我绑定在 Cloudflare 的域名是 `wiki-power.com`，我需要代理的服务本地的端口是 `80`、`HTTP` 协议，那么我只需要这样填写：

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416183438.png)

即可通过 <https://dashboard.wiki-power.com> 访问本地的端口。并且，它会帮你自动申请 SSL 证书，直接在公网通过 https 访问。

## 参考与致谢

- [官网 / 文档](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [GitHub repo](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
