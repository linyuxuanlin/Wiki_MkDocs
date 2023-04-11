---
id: Homelab-跨设备同步工具Syncthing
title: Homelab - 跨设备同步工具 Syncthing 🚧
---


![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195228.png)

change picture

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：


```yml title="docker-compose.yml"
version: "3"
services:
  syncthing:
    image: syncthing/syncthing
    hostname: my-syncthing
    environment:
      - PUID=0
      - PGID=0
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

## 参考与致谢

- [官网](https://syncthing.net/)
- [文档](https://github.com/syncthing/syncthing/blob/main/README-Docker.md)
- [论坛](https://forum.syncthing.net/)
- [GitHub repo](https://github.com/syncthing/syncthing)
- [Docker Hub](https://hub.docker.com/r/syncthing/syncthing/)
- [Demo site](x)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
