---
id: Homelab-免费的内网穿透替代方案Cloudflared
title: Homelab - 免费的内网穿透替代方案 Cloudflared 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

**Cloudflared** 是一个免费的内网穿透方案，用于外网访问无公网 IP 的主机。

---

仍在撰写中。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（例如 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3"
services:
  syncthing:
    image: syncthing/syncthing
    hostname: my-syncthing
    environment:
      - PUID=1000
      - PGID=1000
    volumes:
      # - /DATA:/DATA # 需要同步的目录
      - ${DIR}/syncthing/config:/var/syncthing/config/
    ports:
      - ${PORT}:8384 # Web UI
      - 22000:22000/tcp # TCP file transfers
      - 22000:22000/udp # QUIC file transfers
      - 21027:21027/udp # Receive local discovery broadcasts
    restart: unless-stopped
```

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

---

条件：

- paypal/visa（免费但要绑定）
- 域名绑定至 Cloudflare
- DNS 记录启用 Cloudflare CDN

优点：

- 不需要公网 IP 的服务器
- 不需要防火墙、反向代理
- 不需要备案就可以使用 80 和 443 端口
- 不需要自行申请 SSL 证书
- 免费

缺点：

- 速度慢
- 依赖 Cloudflare

[免费的 Cloudflared 实现外网访问群晖](https://laosu.ml/2022/04/06/%E5%85%8D%E8%B4%B9%E7%9A%84Cloudflared%E5%AE%9E%E7%8E%B0%E5%A4%96%E7%BD%91%E8%AE%BF%E9%97%AE%E7%BE%A4%E6%99%96/#%E8%8E%B7%E5%8F%96%E9%9A%A7%E9%81%93-token)

Cloudflare Zero Trust - Tunnels - Create a tunnel

记录 Tunnel ID (UUID)（格式为：xxxxxxxx-xxxx-xxxx-xxxx-xxxxxxxxxxxx）

记录 token `xxx`

在 docker/cloudflared 目录下放 config.yaml 文件:

```yml
tunnel: [Tunnel UUID]
credentials-file: /root/.cloudflared/[Tunnel UUID].json
```

启动 cloudflare/cloudflared

- 启动命令：`tunnel --config /etc/cloudflared/config.yaml --no-autoupdate run --token [token]`
- 网络：host
- docker/cloudflared:/etc/cloudflared

在 cloudflare 面板配置域名
