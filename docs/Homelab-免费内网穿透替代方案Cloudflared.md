---
id: Homelab-免费内网穿透替代方案Cloudflared
title: Homelab - 免费内网穿透替代方案 Cloudflared 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230416143051.png)

仍在撰写中。

**Syncthing** 是一款免费开源的文件同步应用程序，可在多个设备间同步文件和文件夹，支持增量同步。我用它将服务器的数据备份到 NAS 上做统一管理。

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
