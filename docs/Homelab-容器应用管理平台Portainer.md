---
id: Homelab-容器应用管理平台Portainer
title: Homelab - 容器应用管理平台 Portainer 🚧
---



**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: '3.3'
services:
    portainer:
        ports:
            - [custom-port]:9000 # HTTP
          # - [custom-port]:9443 # HTTPS
        restart: always
        volumes:
            - /var/run/docker.sock:/var/run/docker.sock
            - [custom-port]/portainer/portainer_data:/data
        image: portainer/portainer-ce:latest
```

## 配置说明

## 参考与致谢

- [官网]()
- [文档]()
- [GitHub repo]()
- [Docker Hub]()
- [Demo site]()

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
