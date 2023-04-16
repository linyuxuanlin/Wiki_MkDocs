---
id: Homelab-免费的内网穿透替代方案Cloudflared
title: Homelab - 免费的内网穿透替代方案 Cloudflared 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

**Cloudflared** 是一个免费的内网穿透方案，用于外网访问无公网 IP 的主机。

必需条件：

- 虽然 Cloudflared 是免费的，但需要绑定 VISA/PayPal。
- 域名 NameServer 需要指向 Cloudflare
- 需要启用 Cloudflare CDN

- paypal/visa（免费但要绑定）
- 域名绑定至 Cloudflare
- DNS 记录启用

优点：

- 不需要公网 IP 的服务器
- 不需要防火墙、反向代理
- 不需要备案就可以使用 80 和 443 端口
- 不需要自行申请 SSL 证书
- 免费

缺点：

- 速度慢
- 依赖 Cloudflare

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${TOKEN}` 替换为你自己的 tunnel token：

```yml title="docker-compose.yml"
version: "3"
services:
  cloudflared:
    image: cloudflare/cloudflared:latest
    network_mode: host # 必需要设置为 host
    restart: unless-stopped
    command: tunnel run
    environment:
      - TUNNEL_TOKEN=${TOKEN}
```

## 配置说明

## 参考与致谢

- [官网 / 文档](https://developers.cloudflare.com/cloudflare-one/connections/connect-apps/)
- [GitHub repo](https://github.com/cloudflare/cloudflared)
- [Docker Hub](https://hub.docker.com/r/cloudflare/cloudflared)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。

---

---

[免费的 Cloudflared 实现外网访问群晖](https://laosu.ml/2022/04/06/%E5%85%8D%E8%B4%B9%E7%9A%84Cloudflared%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96/#%E8%8E%B7%E5%8F%96%E9%9A%A7%E9%81%93-token)

Cloudflare Zero Trust - Tunnels - Create a tunnel

记录 Tunnel ID (UUID)（格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx）

记录 token `xxx`

在 docker/cloudflared 目录下放 config.yaml 文件:

```yml
tunnel: [Tunnel UUID]
credentials-file: /root/.cloudflared/[Tunnel UUID].json
```

在 cloudflare 面板配置域名
