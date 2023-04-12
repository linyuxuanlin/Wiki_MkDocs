---
id: Homelab-网站favicon抓取工具iconserver
title: Homelab - 网站 favicon 抓取工具 iconserver
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195157.png)

**iconserver** 是一个网站 favicon 图标抓取工具。支持抓取 `favicon.ico` 与
`apple-touch-icon.png`，拥有简单的 URL API 与 web 操作页面，如果抓取失败则会生成首字母开头的 favicon。

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用的端口就可以）：

```yml title="docker-compose.yml"
version: "3"
services:
  iconserver:
    image: "matthiasluedtke/iconserver:latest"
    restart: always
    ports:
      - ${PORT}:8080
```

## 配置说明

## 参考与致谢

- [文档](https://github.com/mat/besticon#docker)
- [GitHub repo](https://github.com/mat/besticon)
- [Docker Hub](https://hub.docker.com/r/matthiasluedtke/iconserver)
- [Demo site](https://besticon-demo.herokuapp.com/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
