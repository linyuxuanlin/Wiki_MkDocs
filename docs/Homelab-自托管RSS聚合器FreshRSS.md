---
id: Homelab-自托管RSS聚合器FreshRSS
title: Homelab - 自托管 RSS 聚合器 FreshRSS
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304102312005.png)

**FreshRSS** 是一个托管的 RSS 聚合器，支持订阅多个 RSS 源，并自动刷新。提供 web 在线阅读和 API 供移动端 app 使用。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

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
      - "${PORT}:80"
    volumes:
      - ${DIR}/freshrss/data:/var/www/FreshRSS/data
      - ${DIR}/freshrss/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: "*/5" # 每 5 分钟拉取一次文章更新
```

## 配置说明

RSS 源可推荐 saveweb 的中文博客列表 [**rss-list**](https://github.com/saveweb/rss-list)。

移动端 App 推荐使用 FeedMe(Android)，NetNewsWire(iOS)。

更多 RSS 相关的内容可参考文章 [**RSS - 高效率的阅读方式**](https://wiki-power.com/RSS-%E9%AB%98%E6%95%88%E7%8E%87%E7%9A%84%E9%98%85%E8%AF%BB%E6%96%B9%E5%BC%8F/)。

## 参考与致谢

- [官网](https://freshrss.org)
- [文档](https://github.com/FreshRSS/FreshRSS/tree/edge/Docker#docker-compose)
- [GitHub repo](https://github.com/FreshRSS/FreshRSS)
- [Docker Hub](https://hub.docker.com/r/freshrss/freshrss)
- [Demo site](https://demo.freshrss.org/i/?rid=64342708bf322)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
