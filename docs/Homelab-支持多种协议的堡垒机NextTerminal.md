---
id: Homelab-支持多种协议的堡垒机NextTerminal
title: Homelab - 支持多种协议的堡垒机 Next Terminal
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230312001443.png)

**Next Terminal** 是一个简单好用的跳板机（堡垒机），集成了 Apache Guacamole 无客户端的远程桌面网关的堡垒机方案，支持 RDP、SSH、VNC、TELNET、Kubernetes 多协议，能直接通过 web 访问内网资源，跨平台兼容性佳。它支持 MFA 多因子认证登录，也有审计录像功能和其他记录。

## 部署（Docker Compose）

首先创建 `compose.yaml` 文件，并粘贴以下内容：

```yaml title="compose.yaml"
version: "3.3"
services:
  guacd:
    container_name: ${STACK_NAME}_guacd
    image: dushixiang/guacd:${GUACD_VERSION}
    volumes:
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
  next-terminal:
    container_name: ${STACK_NAME}_app
    image: dushixiang/next-terminal:${APP_VERSION}
    environment:
      DB: sqlite
      GUACD_HOSTNAME: ${APP_GUACD_HOSTNAME}
      GUACD_PORT: ${APP_GUACD_PORT}
    ports:
      - ${APP_PORT}:8088
    volumes:
      - /etc/localtime:/etc/localtime
      - ${STACK_DIR}/data:/usr/local/next-terminal/data
    restart: always
```

（可选）推荐在 `compose.yaml` 同级目录下创建 `.env` 文件，并自定义你的环境变量。如果不想使用环境变量的方式，也可以直接在 `compose.yaml` 内自定义你的参数（比如把 `${STACK_NAME}` 替换为 `next-terminal`）。

```dotenv title=".env"
STACK_NAME=next-terminal
STACK_DIR=xxx # 自定义项目储存路径，例如 ./next-terminal

# next-terminal
APP_VERSION=latest
APP_PORT=xxxx # 自定义访问端口，选择不被占用的即可
APP_GUACD_HOSTNAME=guacd # 默认
APP_GUACD_PORT=4822 # 默认

# guacd
GUACD_VERSION=latest
```

最后，在 `compose.yaml` 同级目录下执行 `docker compose up -d` 命令即可启动编排的容器。

## 配置说明

初始账户 / 密码：`admin`。

## 参考与致谢

- [官网](https://next-terminal.typesafe.cn/)
- [文档](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [GitHub repo](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [Demo site](https://next.typesafe.cn/)（账号：test，密码：test）
- [Next Terminal | 开源 轻量 简单的堡垒机](https://blog.samliu.tech/2022/07/22/next-terminal-%E5%BC%80%E6%BA%90-%E8%BD%BB%E9%87%8F-%E7%AE%80%E5%8D%95%E7%9A%84%E5%A0%A1%E5%9E%92%E6%9C%BA/?utm_source=rss&utm_medium=rss&utm_campaign=next-terminal-%25e5%25bc%2580%25e6%25ba%2590-%25e8%25bd%25bb%25e9%2587%258f-%25e7%25ae%2580%25e5%258d%2595%25e7%259a%2584%25e5%25a0%25a1%25e5%259e%2592%25e6%259c%25ba)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
