---
id: Homelab-支持公有云的图床系统Cloudreve
title: Homelab - 支持公有云的图床系统 Cloudreve 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195423.png)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: "3.8"
services:
  cloudreve:
    image: cloudreve/cloudreve:latest
    restart: unless-stopped
    ports:
      - "[custom-port]:5212"
    volumes:
      - temp_data:/data
      - [custom-dir]/cloudreve/cloudreve/uploads:/cloudreve/uploads
      - [custom-dir]/cloudreve/cloudreve/conf.ini:/cloudreve/conf.ini
      - [custom-dir]/cloudreve/cloudreve/cloudreve.db:/cloudreve/cloudreve.db
      - [custom-dir]/cloudreve/cloudreve/avatar:/cloudreve/avatar
    depends_on:
      - aria2
  aria2:
    image: p3terx/aria2-pro
    restart: unless-stopped
    environment:
      - RPC_SECRET=[custom-password-aria2]
      - RPC_PORT=6800
    volumes:
      - [custom-dir]/cloudreve/aria2/config:/config
      - [custom-dir]/cloudreve/data:/var/lib/docker/volumes/cloudreve_temp_data/_data
volumes:
  temp_data:
    driver: local
    driver_opts:
      type: none
      device: [custom-dir]/cloudreve/temp_data
      o: bind
```

## 配置说明

## 参考与致谢

- [官网](https://docs.cloudreve.org/)
- [文档](https://docs.cloudreve.org/getting-started/install#docker-compose)
- [GitHub repo](https://github.com/cloudreve/Cloudreve)
- [Docker Hub](https://hub.docker.com/r/cloudreve/cloudreve)
- [Demo site](https://demo.cloudreve.org/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
