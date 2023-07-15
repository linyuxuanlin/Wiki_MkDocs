---
id: Homelab-自托管RSS聚合器FreshRSS
title: Homelab - 自托管 RSS 聚合器 FreshRSS
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/202304102312005.png)

**FreshRSS** 是一个托管的 RSS 聚合器，支持订阅多个 RSS 源，并自动刷新。提供 web 在线阅读和 API 供移动端 app 使用。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "2.4"
services:
  freshrss:
    container_name: ${STACK_NAME}_app
    image: freshrss/freshrss:${APP_VERSION}
    hostname: freshrss
    logging:
      options:
        max-size: 10m
    ports:
      - "${APP_PORT}:80"
    volumes:
      - ${STACK_DIR}/data:/var/www/FreshRSS/data
      - ${STACK_DIR}/extensions:/var/www/FreshRSS/extensions
    environment:
      TZ: Asia/Shanghai
      CRON_MIN: "*/60" # 每 60 分钟拉取一次文章更新
    restart: unless-stopped
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `freshrss`）。

```dotenv title=".env"
STACK_NAME=freshrss
STACK_DIR=xxx # 自定义项目储存路径，例如 ./freshrss

# freshrss
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

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
