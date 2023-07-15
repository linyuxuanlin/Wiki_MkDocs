---
id: Homelab-网站状态监控工具UptimeKuma
title: Homelab - 网站状态监控工具 Uptime Kuma
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230410160253.jpg)

**Uptime Kuma** 是一个支持多种网络协议的状态监控工具，可监控多个自定义网站的实时可用状态、响应时长、证书有效期等，并提供了多种通知推送方式。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3"
services:
  uptime-kuma:
    container_name: ${STACK_NAME}_app
    image: louislam/uptime-kuma:${APP_VERSION}
    ports:
      - ${APP_PORT}:3001
    volumes:
      - ${STACK_DIR}:/app/data
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `uptime-kuma`）。

```dotenv title=".env"
STACK_NAME=uptime-kuma
STACK_DIR=xxx # 自定义项目储存路径，例如 ./uptime-kuma

# uptime-kuma
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

注：如使用反向代理，请开启 `Websockets Support` 功能。

## 参考与致谢

- [官网](https://uptime.kuma.pet/)
- [文档](https://github.com/louislam/uptime-kuma/wiki)
- [GitHub repo](https://github.com/louislam/uptime-kuma)
- [Docker Hub](https://hub.docker.com/r/louislam/uptime-kuma)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
