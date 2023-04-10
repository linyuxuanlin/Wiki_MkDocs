---
id: Homelab-自托管RSS聚合器FreshRSS
title: Homelab - 自托管 RSS 聚合器 FreshRSS 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230310205330.png)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: "2.4"
services:
  freshrss:
    image: freshrss/freshrss
    hostname: freshrss
    restart: unless-stopped
    logging:
      options:
        max-size: 10m
    ports:
      - "[custom-port]:80"
    volumes:
      - [custom-dir]/freshrss/data:/var/www/FreshRSS/data
      - [custom-dir]/freshrss/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: '*/5' # 每 5 分钟拉取一次文章更新
```

## 配置说明

## 参考与致谢

- [官网](https://freshrss.org)
- [文档](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [GitHub repo](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Demo site](https://demo.freshrss.org/i/?rid=64342708bf322)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
