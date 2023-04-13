---
id: Homelab-网站状态监控工具UptimeKuma
title: Homelab - 网站状态监控工具 Uptime Kuma
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410160253.jpg)

**Uptime Kuma** 是一个支持多种网络协议的状态监控工具，可监控多个自定义网站的实时可用状态、响应时长、证书有效期等，并提供了多种通知推送方式。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3"
services:
  uptime-kuma:
    image: louislam/uptime-kuma
    restart: always
    ports:
      - "${PORT}:3001"
    volumes:
      - ${DIR}/uptime-kuma:/app/data
```

注：如使用反向代理，请开启 `Websockets Support` 功能。

## 参考与致谢

- [官网](https://uptime.kuma.pet/)
- [文档](https://github.com/louislam/uptime-kuma/wiki)
- [GitHub repo](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
