---
id: Homelab-支持多种协议的堡垒机NextTerminal
title: Homelab - 支持多种协议的堡垒机 Next Terminal 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230312001443.png)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `[custom-dir]` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`[custom-port]` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: '3.3'
services:
  guacd:
    image: dushixiang/guacd:latest
    volumes:
      - [custom-dir]/next-terminal/data:/usr/local/next-terminal/data
    restart:
      always
  next-terminal:
    image: dushixiang/next-terminal:latest
    environment:
      DB: sqlite
      GUACD_HOSTNAME: guacd
      GUACD_PORT: 4822
    ports:
      - "[custom-port]:8088"
    volumes:
      - /etc/localtime:/etc/localtime
      - [custom-dir]/next-terminal/data:/usr/local/next-terminal/data
    restart:
      always
```

## 配置说明

## 参考与致谢

- [官网](https://next-terminal.typesafe.cn/)
- [文档](https://next-terminal.typesafe.cn/docs/install/docker-install.html)
- [GitHub repo](https://github.com/dushixiang/next-terminal)
- [Docker Hub](https://hub.docker.com/r/dushixiang/next-terminal)
- [Demo site](https://next.typesafe.cn/)（账号：test，密码：test）


> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
