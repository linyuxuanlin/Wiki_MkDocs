---
id: Homelab-碎片笔记工具memos
title: Homelab - 碎片笔记工具 memos 🚧
---

![](https://wiki-media-1253965369.cos.ap-guangzhou.myqcloud.com/img/20230304195311.png)

**xxx** 是一个

## 部署（docker-compose）

先创建 `docker-compose.yml` ，并将以下的 `${DIR}` 替换为本地的目录（比如我的是 `/DATA/AppData`）；`${PORT}` 替换为自定义的端口号（比如 `1234`，选择不被占用就可以了）：

```yml title="docker-compose.yml"
version: "3.0"
services:
  memos:
    image: neosmemo/memos:latest
    volumes:
      - ${DIR}/memos:/var/opt/memos
    ports:
      - ${PORT}:5230
```

## 配置说明

## 参考与致谢

- [官网](https://usememos.com/)
- [文档](https://usememos.com/docs/install#docker-compose)
- [GitHub repo](https://github.com/usememos/memos)
- [Docker Hub](https://hub.docker.com/r/neosmemo/memos)
- [Demo site](https://demo.usememos.com/)

> 原文地址：<https://wiki-power.com/>  
> 本篇文章受 [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by/4.0/deed.zh) 协议保护，转载请注明出处。
