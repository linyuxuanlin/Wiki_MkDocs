---
id: Homelab-支持多种协议的堡垒机NextTerminal
title: Homelab - 支持多种协议的堡垒机 Next Terminal
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230312001443.png)

**Next Terminal** 是一个简单好用的跳板机（堡垒机），集成了 Apache Guacamole 无客户端的远程桌面网关的堡垒机方案，支持 RDP、SSH、VNC、TELNET、Kubernetes 多协议，能直接通过 web 访问内网资源，跨平台兼容性佳。它支持 MFA 多因子认证登录，也有审计录像功能和其他记录。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3.3"
services:
  guacd:
    image: dushixiang/guacd:latest
    volumes:
      - ${DIR}/next-terminal/data:/usr/local/next-terminal/data
    restart: always
  next-terminal:
    image: dushixiang/next-terminal:latest
    environment:
      DB: sqlite
      GUACD_HOSTNAME: guacd
      GUACD_PORT: 4822
    ports:
      - "${PORT}:8088"
    volumes:
      - /etc/localtime:/etc/localtime
      - ${DIR}/next-terminal/data:/usr/local/next-terminal/data
    restart: always
```

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
