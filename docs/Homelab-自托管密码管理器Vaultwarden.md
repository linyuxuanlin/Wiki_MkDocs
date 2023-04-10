---
id: Homelab-自托管密码管理器Vaultwarden
title: Homelab - 自托管密码管理器 Vaultwarden 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195414.jpg)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: "3"

services:
  todo:
    image: vaultwarden/server:latest
    restart: always
    ports:
      - [custom-port]:80
    volumes:
      - [custom-dir]/vaultwarden/:/data/
```

## 配置说明

## 参考与致谢

- [官网](https://github.com/dani-garcia/vaultwarden/wiki)
- [文档](https://github.com/dani-garcia/vaultwarden/wiki/Using-Docker-Compose)
- [GitHub repo](https://github.com/dani-garcia/vaultwarden)
- [Docker Hub](https://hub.docker.com/r/vaultwarden/server)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
